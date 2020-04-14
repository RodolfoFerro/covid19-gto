FROM python:3-alpine


ENV PIP_NO_CACHE_DIR=false

RUN pip install pipenv

WORKDIR /app

COPY Pipfile* ./

RUN pipenv install --system --deploy

COPY . .

EXPOSE 5000

CMD ["gunicorn", "--bind", ":5000", "app:app"]
