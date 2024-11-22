# Sử dụng hình ảnh Python chính thức
FROM python:3.11-slim

# Đặt thư mục làm việc trong container
WORKDIR /app

# Sao chép các file cần thiết vào container
COPY requirements.txt requirements.txt
COPY nlr_ai.py nlr_ai.py

# Cài đặt các thư viện Python
RUN pip install --no-cache-dir -r requirements.txt

# Chạy Flask trên cổng 5000
EXPOSE 5000
CMD ["python", "nlr_ai.py"]
