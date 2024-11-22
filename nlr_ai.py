from dotenv import load_dotenv
import sys
import os
import openai
import pymysql
import io
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load biến từ file .env
load_dotenv()
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Cấu hình OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

# Hàm thực hiện truy vấn MySQL
def query_database(sql_query):
    connection = pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_DATABASE_NAME")
    )
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql_query)
            result = cursor.fetchall()
        return result
    finally:
        connection.close()

# Hàm gửi câu hỏi tới GPT
def ask_gpt(question):
    schema_info = """
    Cấu trúc cơ sở dữ liệu:
    - Bảng: ent_checklistreplace
        - Cột: ID_ChecklistReplace (INTEGER), ID_Checklist (INTEGER), MotaLoi (TEXT), 
                Songay (INTEGER), Solan (INTEGER), Ngaybatdau (DATE), isDelete (INTEGER)
    
    - Bảng: ent_chinhanh
        - Cột: ID_Chinhanh (INTEGER, primary key), Tenchinhanh (VARCHAR), isDelete (INTEGER),
                createdAt (TIMESTAMP), updatedAt (TIMESTAMP)
    
    - Bảng: ent_chucvu
        - Cột: ID_Chucvu (INTEGER, primary key), Chucvu (VARCHAR), Role (INTEGER), Ghichu (VARCHAR),
                isDelete (INTEGER), createdAt (TIMESTAMP), updatedAt (TIMESTAMP)
    
    - Bảng: ent_duan
        - Cột: ID_Duan (INTEGER, primary key), ID_Nhom (INTEGER), ID_Chinhanh (INTEGER), ID_Linhvuc (INTEGER),
                ID_Loaihinh (INTEGER), ID_Phanloai (INTEGER), Ngaybatdau (DATE), Duan (VARCHAR), Diachi (VARCHAR),
                Vido (TEXT), Kinhdo (TEXT), Logo (TEXT), ID_LoaiCS (VARCHAR), isDelete (INTEGER), createdAt (TIMESTAMP),
                updatedAt (TIMESTAMP)
    
    - Bảng: ent_duan_khoicv
        - Cột: ID_Duan_KhoiCV (INTEGER, primary key), ID_KhoiCV (INTEGER), ID_Duan (INTEGER), Chuky (INTEGER),
                Ngaybatdau (DATE), isDelete (INTEGER), createdAt (TIMESTAMP), updatedAt (TIMESTAMP)
    
    - Bảng: ent_duan_loai
        - Cột: ID_Duan_Loai (INTEGER, primary key), Loaiduan (VARCHAR)
    
    - Bảng: ent_duan_loai_chiso
        - Cột: ID_Duan_LoaiCS (INTEGER, primary key), ID_Duan (INTEGER), ID_Loai (INTEGER), isDelete (INTEGER),
                createdAt (TIMESTAMP), updatedAt (TIMESTAMP)
    
    - Bảng: ent_duan_user
        - Cột: ID_Duan_User (INTEGER, primary key), ID_Duan (INTEGER), ID_User (INTEGER), isDelete (INTEGER),
                updatedAt (TIMESTAMP), createdAt (TIMESTAMP)
    
    - Bảng: ent_hangmuc
        - Cột: ID_Hangmuc (INTEGER, primary key), ID_Khuvuc (INTEGER), Important (INTEGER), 
                MaQrCode (VARCHAR), Hangmuc (TEXT), Tieuchuankt (TEXT), FileTieuChuan (VARCHAR), 
                Sothutu (INTEGER), isDelete (INTEGER), createdAt (TIMESTAMP), updatedAt (TIMESTAMP)
    
    - Bảng: ent_hangmuc_chiso
        - Cột: ID_Hangmuc_Chiso (INTEGER, primary key), ID_Duan (INTEGER), ID_LoaiCS (INTEGER), 
                Ten_Hangmuc_Chiso (VARCHAR), isDelete (INTEGER), createdAt (TIMESTAMP), updatedAt (TIMESTAMP)
    
    - Bảng: ent_khoicv
        - Cột: ID_KhoiCV (INTEGER, primary key), ID_Duan (INTEGER), KhoiCV (VARCHAR), 
                Ngaybatdau (DATE), Chuky (INTEGER), isDelete (INTEGER), createdAt (TIMESTAMP), updatedAt (TIMESTAMP)
    
    - Bảng: ent_khuvuc
        - Cột: ID_Khuvuc (INTEGER, primary key), ID_Toanha (INTEGER), ID_Tang (INTEGER), ID_KhoiCVs (JSON),
                Makhuvuc (VARCHAR), Sothutu (INTEGER), MaQrCode (VARCHAR), Tenkhuvuc (VARCHAR), 
                ID_User (INTEGER), isDelete (INTEGER), createdAt (TIMESTAMP), updatedAt (TIMESTAMP)
    
    - Bảng: ent_khuvuc_khoicv
        - Cột: ID_KV_CV (INTEGER, primary key), ID_Khuvuc (INTEGER), ID_KhoiCV (INTEGER), 
                isDelete (INTEGER), createdAt (TIMESTAMP), updatedAt (TIMESTAMP)
    
    - Bảng: ent_linhvuc
        - Cột: ID_Linhvuc (INTEGER, primary key), Linhvuc (VARCHAR), isDelete (INTEGER),
                createdAt (TIMESTAMP), updatedAt (TIMESTAMP)
    
    - Bảng: ent_loai_chiso
        - Cột: ID_LoaiCS (INTEGER, primary key), ID_Duan_Loai (INTEGER), TenLoaiCS (VARCHAR), 
                isDelete (INTEGER), createdAt (TIMESTAMP), updatedAt (TIMESTAMP)
    
    - Bảng: ent_loaihinhbds
        - Cột: ID_Loaihinh (INTEGER, primary key), Loaihinh (VARCHAR), isDelete (INTEGER), 
                createdAt (TIMESTAMP), updatedAt (TIMESTAMP)
    
    - Bảng: ent_nhom
        - Cột: ID_Nhom (INTEGER, primary key), Tennhom (VARCHAR), isDelete (INTEGER), 
                createdAt (TIMESTAMP), updatedAt (TIMESTAMP)
    
    - Bảng: ent_phanloaida
        - Cột: ID_Phanloai (INTEGER, primary key), Phanloai (VARCHAR), isDelete (INTEGER),
                createdAt (TIMESTAMP), updatedAt (TIMESTAMP)
    
    - Bảng: ent_tang
        - Cột: ID_Tang (INTEGER, primary key), Tentang (VARCHAR), ID_Duan (INTEGER), isDelete (INTEGER),
                createdAt (TIMESTAMP), updatedAt (TIMESTAMP)
    
    - Bảng: ent_thietlapca
        - Cột: ID_ThietLapCa (INTEGER, primary key), Ngaythu (INTEGER), ID_Calv (INTEGER), 
                ID_Hangmucs (JSON), ID_Duan (INTEGER), Sochecklist (INTEGER), isDelete (INTEGER), 
                createdAt (TIMESTAMP), updatedAt (TIMESTAMP)
    
    - Bảng: ent_thietlaptsda
        - Cột: ID_Thietlaptsda (INTEGER, primary key), ID_Duan (INTEGER), Tenbangchecklistc (VARCHAR), 
                Tenbangchecklistct (VARCHAR), Tenbangchecklistctdone (VARCHAR), isDelete (INTEGER),
                createdAt (TIMESTAMP), updatedAt (TIMESTAMP)
    
    - Bảng: ent_tile
        - Cột: ID_Tile (INTEGER, primary key), Tenduan (VARCHAR), Ngay (DATE), Khoibaove (VARCHAR),
                Khoilamsach (VARCHAR), Khoikythuat (VARCHAR), Khoidichvu (VARCHAR), KhoiFB (VARCHAR),
                isDelete (INTEGER), createdAt (TIMESTAMP), updatedAt (TIMESTAMP)
    
    - Bảng: ent_toanha
        - Cột: ID_Toanha (INTEGER, primary key), ID_Duan (INTEGER), Toanha (VARCHAR), Sotang (INTEGER), 
                Vido (TEXT), Kinhdo (TEXT), isDelete (INTEGER), createdAt (TIMESTAMP), updatedAt (TIMESTAMP)
    
    - Bảng: HSSE
        - Cột: ID (INTEGER), Ten_du_an (VARCHAR), Ngay_ghi_nhan (DATE), Nguoi_tao (VARCHAR),
                Dien_cu_dan (FLOAT), Dien_cdt (FLOAT), Nuoc_cu_dan (FLOAT), Nuoc_cdt (FLOAT),
                Xa_thai (FLOAT), Rac_sh (FLOAT), Muoi_dp (FLOAT), PAC (FLOAT), NaHSO3 (FLOAT),
                NaOH (FLOAT), Mat_rd (FLOAT), Polymer_Anion (FLOAT), Chlorine_bot (FLOAT),
                Chlorine_vien (FLOAT), Methanol (FLOAT), Dau_may (FLOAT), Tui_rac240 (FLOAT),
                Tui_rac120 (FLOAT), Tui_rac20 (FLOAT), Tui_rac10 (FLOAT), Tui_rac5 (FLOAT),
                giayvs_235 (FLOAT), giaivs_120 (FLOAT), giay_lau_tay (FLOAT), hoa_chat (FLOAT),
                nuoc_rua_tay (FLOAT), nhiet_do (FLOAT), nuoc_bu (FLOAT), clo (FLOAT), PH (FLOAT),
                Poolblock (FLOAT), trat_thai (FLOAT), Email (VARCHAR), pHMINUS (FLOAT), axit (FLOAT),
                PN180 (FLOAT), chiSoCO2 (FLOAT), modifiedBy (VARCHAR), createdAt (TIMESTAMP),
                updatedAt (TIMESTAMP)

    - Bảng: ent_baocaochiso
        - Cột: ID_Baocaochiso (INTEGER), ID_User (INTEGER), ID_Duan (INTEGER), 
                ID_Hangmuc_Chiso (INTEGER), Day (DATE), Month (INTEGER), Year (INTEGER),
                Electrical (FLOAT), Water (FLOAT), ImageElectrical (VARCHAR), ImageWater (VARCHAR),
                ElectricalBefore (FLOAT), WaterBefore (FLOAT), Electrical_Read_Img (FLOAT),
                Water_Read_Img (FLOAT), Ghichu (TEXT), isDelete (INTEGER), updatedAt (TIMESTAMP),
                createdAt (TIMESTAMP)

    - Bảng: ent_calv
        - Cột: ID_Calv (INTEGER), ID_Duan (INTEGER), ID_KhoiCV (INTEGER), Tenca (VARCHAR),
                Giobatdau (TIME), Gioketthuc (TIME), ID_User (INTEGER), isDelete (INTEGER),
                createdAt (TIMESTAMP), updatedAt (TIMESTAMP)

    - Bảng: ent_checklist
        - Cột: ID_Checklist (INTEGER), ID_Khuvuc (INTEGER), ID_Hangmuc (INTEGER), ID_Tang (INTEGER),
                Sothutu (INTEGER), Maso (VARCHAR), MaQrCode (VARCHAR), Checklist (TEXT),
                Giatridinhdanh (VARCHAR), Giatrinhan (VARCHAR), Giatriloi (VARCHAR), Ghichu (TEXT),
                Tieuchuan (TEXT), ID_User (INTEGER), sCalv (JSON), Tinhtrang (INTEGER), isCheck (INTEGER),
                isImportant (INTEGER), calv_1 (INTEGER), calv_2 (INTEGER), calv_3 (INTEGER), calv_4 (INTEGER),
                isDelete (INTEGER), createdAt (TIMESTAMP), updatedAt (TIMESTAMP)

    - Bảng: ent_duan
        - Cột: ID_Duan (INTEGER), ID_Nhom (INTEGER), ID_Chinhanh (INTEGER), ID_Linhvuc (INTEGER),
                ID_Loaihinh (INTEGER), ID_Phanloai (INTEGER), Ngaybatdau (DATE), Duan (VARCHAR),
                Diachi (VARCHAR), Vido (TEXT), Kinhdo (TEXT), Logo (TEXT), ID_LoaiCS (VARCHAR),
                isDelete (INTEGER), createdAt (TIMESTAMP), updatedAt (TIMESTAMP)

    - Bảng: ent_user
        - Cột: ID_User (INTEGER), UserName (VARCHAR), Password (TEXT), PasswordPrivate (VARCHAR),
                ID_Chucvu (INTEGER), ID_KhoiCV (INTEGER), ID_Duan (INTEGER), ID_Chinhanh (INTEGER),
                arr_Duan (VARCHAR), updateTime (VARCHAR), Email (VARCHAR), Hoten (VARCHAR), Gioitinh (VARCHAR),
                Sodienthoai (VARCHAR), Ngaysinh (DATE), deviceToken (VARCHAR), isError (INTEGER), 
                isDelete (INTEGER), createdAt (TIMESTAMP), updatedAt (TIMESTAMP)

    - Bảng: nrl_ai
        - Cột: ID_AI (INTEGER), Tenduan (CHAR), Tenkhoi (CHAR), Tenca (CHAR), Giamsat (VARCHAR),
                Ngay (DATETIME), Tilehoanthanh (FLOAT), TongC (INTEGER), Tong (INTEGER),
                Thoigianmoca (TIME), Thoigianchecklistbatdau (TIME), Thoigianchecklistkethuc (TIME),
                Thoigiantrungbinh (TIME), Thoigianchecklistngannhat (TIME), Thoigianchecklistlaunhau (TIME),
                Soluongghichu (INTEGER), Soluonghinhanh (INTEGER), isDelete (INTEGER), createdAt (TIMESTAMP),
                updatedAt (TIMESTAMP)
     - Bảng: tb_checklistc
        - Cột: ID_ChecklistC (INTEGER), ID_Duan (INTEGER), ID_KhoiCV (INTEGER), Ngay (DATE),
                ID_ThietLapCa (INTEGER), ID_Calv (INTEGER), ID_User (INTEGER), ID_Hangmucs (JSON),
                TongC (INTEGER), Tong (INTEGER), Giobd (TIME), Giochupanh1 (TIME), Anh1 (VARCHAR),
                Giochupanh2 (TIME), Anh2 (VARCHAR), Giochupanh3 (TIME), Anh3 (VARCHAR), Giochupanh4 (TIME),
                Anh4 (VARCHAR), Giokt (TIME), Ghichu (LONGTEXT), Tinhtrang (INTEGER), isDelete (INTEGER),
                createdAt (TIMESTAMP), updatedAt (TIMESTAMP)

    - Bảng: tb_checklistchitiet
        - Cột: ID_Checklistchitiet (INTEGER), ID_ChecklistC (INTEGER), ID_Checklist (INTEGER),
                Ketqua (VARCHAR), Anh (VARCHAR), Ngay (DATE), Gioht (TIME), Vido (VARCHAR), Kinhdo (VARCHAR),
                Docao (VARCHAR), isScan (INTEGER), isCheckListLai (INTEGER), Ghichu (LONGTEXT), 
                isDelete (INTEGER), createdAt (TIMESTAMP), updatedAt (TIMESTAMP)

    - Bảng: tb_checklistchitietdone
        - Cột: ID_Checklistchitietdone (INTEGER), ID_ChecklistC (INTEGER), Description (VARCHAR), 
                Gioht (TIME), Vido (VARCHAR), Kinhdo (VARCHAR), Docao (VARCHAR), isScan (INTEGER),
                isCheckListLai (INTEGER), isDelete (INTEGER), createdAt (TIMESTAMP), updatedAt (TIMESTAMP)

    - Bảng: tb_sucongoai
        - Cột: ID_Suco (INTEGER), ID_KV_CV (INTEGER), ID_Hangmuc (INTEGER), Ngaysuco (DATE), 
                Giosuco (TIME), Noidungsuco (VARCHAR), Duongdancacanh (VARCHAR), Anhkiemtra (TEXT),
                Ghichu (TEXT), ID_User (INTEGER), Tinhtrangxuly (INTEGER), Ngayxuly (DATE),
                isDelete (INTEGER), createdAt (TIMESTAMP), updatedAt (TIMESTAMP)

    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f"Bạn là trợ lý AI chuyên tạo truy vấn SQL từ câu hỏi người dùng. Dưới đây là thông tin về cơ sở dữ liệu: {schema_info}"},
            {"role": "user", "content": question}
        ]
    )
    return response['choices'][0]['message']['content']

# Hàm xử lý câu hỏi
def process_question(question):
    # GPT tạo câu SQL
    sql_query = ask_gpt(f"Chuyển câu hỏi sau thành câu truy vấn SQL: {question}")

    # Loại bỏ dấu markdown (nếu có) từ câu trả về
    new_sql_query = sql_query.replace("```sql", "").replace("```", "").strip()

    # Tạo câu SQL linh hoạt bằng cách sử dụng LIKE cho các tìm kiếm khối và dự án
    format_sql_query = generate_sql(question, new_sql_query)

    # Gợi ý bảng cần sử dụng
    table_suggestion = get_table_suggestion(question)
    print(f"Gợi ý bảng để lấy dữ liệu: {table_suggestion}")

    # In ra câu SQL sẽ chạy (không cần xác nhận từ người dùng)
    print("===========================================================")
    print('Query: ', format_sql_query)

    # Thực hiện truy vấn SQL tự động
    try:
        result = query_database(format_sql_query)
        return result
    except Exception as e:
        return f"Lỗi khi thực hiện truy vấn: {e}"

def get_table_suggestion(question):
    # Kiểm tra câu hỏi để gợi ý bảng cần sử dụng
    if "checklist" in question.lower():
        return "ent_checklist, tb_checklistc, tb_checklistchitiet"
    elif "dự án" in question.lower():
        return "ent_duan"
    elif "khối" in question.lower():
        return "ent_khoicv"
    elif "user" in question.lower():
        return "ent_user, ent_calv"
    else:
        return "Không xác định bảng cụ thể, bạn có thể thử với bảng ent_user, ent_duan, ent_khoicv."

def get_blocks_and_projects():
    # Truy vấn MySQL để lấy danh sách khối công việc (KhoiCV) và dự án (Duan)
    query = """
    SELECT DISTINCT KhoiCV FROM ent_khoicv WHERE isDelete = 0;
    """
    blocks = query_database(query)  # Giả sử query_database là hàm truy vấn của bạn

    query = """
    SELECT DISTINCT Duan FROM ent_duan WHERE isDelete = 0;
    """
    projects = query_database(query)  # Truy vấn tất cả dự án

    return [block[0] for block in blocks], [project[0] for project in projects]

def generate_sql(question, sql_query):
    # Lấy danh sách khối công việc và dự án từ cơ sở dữ liệu
    blocks, projects = get_blocks_and_projects()

    # Kiểm tra xem câu hỏi có chứa các khối công việc
    for block in blocks:
        if block.lower() in question.lower():
            # Thay thế điều kiện tìm khối công việc trong câu truy vấn SQL và loại bỏ các điều kiện khác liên quan đến khối công việc
            sql_query = sql_query.replace(f"k.KhoiCV = '{block}'", f"k.KhoiCV LIKE '%{block}%'")
            sql_query = sql_query.replace("AND ID_Chucvu IN (", "")  # Loại bỏ tất cả các điều kiện liên quan đến ID_Chucvu
            sql_query = sql_query.replace("AND ID_Linhvuc IN (", "")  # Loại bỏ tất cả các điều kiện liên quan đến ID_Linhvuc
            sql_query = sql_query.replace("AND ID_Loaihinh IN (", "")  # Loại bỏ tất cả các điều kiện liên quan đến Loaihinh

    # Kiểm tra xem câu hỏi có chứa các dự án
    for project in projects:
        if project.lower() in question.lower():
            # Sử dụng LIKE cho tìm kiếm linh hoạt dự án
            sql_query = sql_query.replace(f"d.Duan = '{project}'", f"d.Duan LIKE '%{project}%'")
            sql_query = sql_query.replace("AND ID_Linhvuc IN (", "")  # Loại bỏ bất kỳ điều kiện không cần thiết liên quan đến Lĩnh vực

    return sql_query

@app.route('/api/v1/process', methods=['POST'])
def process_question_route():
    # Nhận câu hỏi từ client
    question = request.json.get('question')

    if not question:
        return jsonify({"error": "No question provided"}), 400

    answer = process_question(question)

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000,debug=True)