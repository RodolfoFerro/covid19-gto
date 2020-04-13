FROM python:3-alpine

COPY . /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install gunicorn

EXPOSE 5000

CMD ["gunicorn", "--bind", ":5000", "app:app"]
