FROM python:3-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install gunicorn

COPY . .

EXPOSE 5000

CMD ["gunicorn", "--bind", ":5000", "app:app"]
