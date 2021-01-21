FROM python:3.7-slim

RUN pip install --no-cache-dir poetry

WORKDIR /srv/{{cookiecutter.repo_dir}}
COPY pyproject.toml poetry.lock alembic.ini /srv/{{cookiecutter.repo_dir}}/
COPY {{cookiecutter.package_dir}}/ /srv/{{cookiecutter.repo_dir}}/{{cookiecutter.package_dir}}

RUN poetry install --no-dev

EXPOSE 8000

CMD poetry run uvicorn {{cookiecutter.package_dir}}.main:app --host 0.0.0.0
