FROM python:3-alpine

COPY . /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]