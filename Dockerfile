FROM python:3.10

WORKDIR /app

COPY . /app

ENV TELEGRAM_BOT_TOKEN=""

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app/bots/telegram_bot

CMD ["python3", "main.py"]
