
FROM python:3.12-slim

LABEL authors="jerieljan"

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 7860

ENV GRADIO_SERVER_NAME="0.0.0.0"

CMD ["python", "6-gradio-chat.py"]
