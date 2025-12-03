# 베이스 이미지
FROM python:3.13-slim

# 필수 패키지 설치
RUN apt-get update && apt-get install -y curl build-essential

# 작업 디렉토리 설정
WORKDIR /app


# 파이썬 패키지 설치
RUN pip install pydantic pika psycopg2-binary python-dotenv

# 앱 소스 복사
COPY . .

# mintybot 사용자 생성 (권한 문제 방지)
RUN groupadd -r PASCAI && useradd -r -g PASCAI PASCAI 
USER PASCAI

# 앱 실행
CMD ["python", "src/main.py"]