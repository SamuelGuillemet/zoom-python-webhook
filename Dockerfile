FROM python:3.11-alpine

WORKDIR /code

ENV ENVIRONMENT=production

ENV POETRY_NO_INTERACTION=false \
    POETRY_VIRTUALENVS_IN_PROJECT=false \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR=/tmp/poetry_cache

RUN pip install poetry

RUN touch README.md

COPY pyproject.toml poetry.lock ./

RUN poetry install --only main --no-root --no-directory && rm -rf $POETRY_CACHE_DIR

COPY ./src /code/src

RUN poetry install --only-root

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080", "--proxy-headers", "--no-access-log"]