from dotenv import load_dotenv
import sys
import os
import openai
import pymysql
import io
import logging
from flask import Flask, request, jsonify
import json
import re
import datetime

app = Flask(__name__)

# Load environment variables from .env
load_dotenv()
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler("app.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

# Set up OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

# Path to JSON schema file
SCHEMA_JSON_PATH = "hsse_info.json"

# Function to read schema from JSON file
def load_schema():
    with open(SCHEMA_JSON_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

# Load schema at startup
schema_info = load_schema()

# Function to query MySQL database
def query_database(sql_query):
    connection = pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_DATABASE_NAME")
    )
    try:
        with connection.cursor() as cursor:
            app.logger.info(f"Executing SQL query: {sql_query}")
            cursor.execute(sql_query)
            result = cursor.fetchall()
            app.logger.info(f"Query result: {result}")
        return result
    finally:
        connection.close()

# Function to extract SQL query from GPT response
def extract_sql_from_response(response):
    # Use regex to find the first SQL query in the response
    sql_match = re.search(r"(?i)(select|insert|update|delete).*;", response, re.DOTALL)
    if sql_match:
        return sql_match.group(0).strip()
    return None

# Function to send question to GPT
def ask_gpt(question):
    # Convert schema information to JSON string
    schema_text = json.dumps(schema_info, ensure_ascii=False, indent=2)

    # Create the dynamic prompt with user's question and filtered khối
    prompt = (
        f"Bạn là trợ lý AI chuyên tạo truy vấn SQL từ câu hỏi người dùng. "
        f"Dưới đây là thông tin về cơ sở dữ liệu của tôi:\n{schema_text}\n\n"
      
         f"Lưu ý:\n"
        f"- Khi người dùng hỏi có từ 'dự án', hãy sử dụng 'LIKE' để tìm kiếm Ten_du_an thay vì '='. "
        f"- Thêm ký tự '%' trước và sau giá trị tìm kiếm trong 'LIKE'.\n"
         f"- Cột `Ngay_ghi_nhan` có định dạng `YYYY-MM-DD`.\n"
          f"- Nếu người dùng chỉ hỏi về **tháng**, sử dụng `MONTH(Ngay_ghi_nhan)` để lọc.\n"
    f"- Nếu người dùng hỏi về **năm**, sử dụng `YEAR(Ngay_ghi_nhan)`.\n"
    f"- Nếu người dùng hỏi về **ngày cụ thể**, so sánh trực tiếp `Ngay_ghi_nhan = 'YYYY-MM-DD'`.\n"
    
        f"Câu hỏi: {question}\n"
    )

    # Get the SQL query response from GPT-4
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "Bạn là trợ lý AI giúp tạo truy vấn SQL."},
                  {"role": "user", "content": prompt}]
    )

    # Return the response content
    return response['choices'][0]['message']['content'].strip()

# Function to process question
def process_question(question):
   
    sql_response = ask_gpt(question)
    sql_query = extract_sql_from_response(sql_response)

    if not sql_query:
        return f"Lỗi: GPT không trả về câu truy vấn SQL hợp lệ. Kết quả GPT: {sql_response}"

    app.logger.info(f"Executing SQL query: {sql_query}")
    try:
        result = query_database(sql_query)

        if result and len(result) > 0:
            # Convert all datetime.date and float values to strings
            result_as_strings = [
                [str(value) if isinstance(value, (datetime.date, float)) else value for value in row]
                for row in result
            ]

            # Format the result as a readable string
            formatted_result = "\n".join(
                [", ".join(map(str, row)) for row in result_as_strings]
            )

            # Generate response using GPT with formatted result
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[ 
                    {"role": "system", "content": "Bạn là trợ lý AI chuyên giúp trả lời các câu hỏi với dữ liệu đầu vào."},
                    {
                        "role": "user",
                        "content": (
                            f"Tôi vừa thực hiện một câu hỏi: '{question.strip()}' "
                            f"và kết quả nhận được là:\n{formatted_result}\n\n"
                            f"Hãy viết một câu trả lời hoàn chỉnh, lịch sự.\n\n"
                        )
                    }
                ]
            )
            return response['choices'][0]['message']['content'].strip().replace(
                "Chân thành cảm ơn và mong nhận được phản hồi từ quý vị! Trân trọng, [Your Name] [Your Position]",
                "Chân thành cảm ơn và mong nhận được phản hồi từ quý vị! Trân trọng, Phòng Số Hóa"
            )
        else:
            return "Xin hãy hỏi kỹ hơn."
    except Exception as e:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[ 
                {"role": "system", "content": "Bạn là trợ lý AI chuyên giải thích lỗi và tạo câu trả lời thân thiện."},
                {
                    "role": "user",
                    "content": (
                        f"Tôi vừa thực hiện một truy vấn với câu hỏi: '{question.strip()}' "
                        f"Hãy viết một câu trả lời phù hợp để thông báo cho người dùng, lịch sự và dễ hiểu.\n\n"
                    )
                }
            ]
        )
        return response['choices'][0]['message']['content'].strip().replace(
            "Chân thành cảm ơn và mong nhận được phản hồi từ quý vị! Trân trọng, [Your Name] [Your Position]",
            "Chân thành cảm ơn và mong nhận được phản hồi từ quý vị! Trân trọng, Phòng Số Hóa"
        )

@app.route('/api/v1/process', methods=['POST'])
def process_question_route():
    question = request.json.get('question')
    if not question:
        error_msg = "No question provided"
        app.logger.warning(error_msg)
        return jsonify({"error": error_msg}), 400

    answer = process_question(question)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    from waitress import serve
    serve(app, host='0.0.0.0', port=5000, threads=10)
