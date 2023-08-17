FROM python:3.9.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 7005

CMD ["python", "start_server.py"]