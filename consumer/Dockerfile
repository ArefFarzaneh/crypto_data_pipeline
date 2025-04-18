FROM python:3.9-slim

WORKDIR /app

COPY ./requirements.txt .
COPY ./config/settings.py /app/config/
COPY ./consumer/consumer.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "consumer.py"]