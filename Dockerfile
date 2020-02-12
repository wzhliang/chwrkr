FROM python:3.7.0-slim

RUN mkdir /app
WORKDIR /app
ADD main.py /app

ENTRYPOINT ["python", "main.py"]
