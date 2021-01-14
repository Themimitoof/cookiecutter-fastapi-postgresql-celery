FROM python:3.7-slim

RUN pip install --no-cache-dir poetry

WORKDIR /srv/fastapi-dummy-api
COPY pyproject.toml poetry.lock alembic.ini /srv/fastapi-dummy-api/
COPY fastapi_dummy_api/ /srv/fastapi-dummy-api/fastapi_dummy_api

RUN poetry install

EXPOSE 8000

CMD poetry run uvicorn fastapi_dummy_api.main:app --host 0.0.0.0
