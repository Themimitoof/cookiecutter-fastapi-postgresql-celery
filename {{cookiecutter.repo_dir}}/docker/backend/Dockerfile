FROM python:3.7-slim

RUN pip install --no-cache-dir poetry

WORKDIR /srv/{{cookiecutter.repo_dir}}
COPY pyproject.toml poetry.lock alembic.ini /srv/{{cookiecutter.repo_dir}}/
COPY {{cookiecutter.package_dir}}/ /srv/{{cookiecutter.repo_dir}}/{{cookiecutter.package_dir}}

RUN poetry install --no-dev

EXPOSE 8000

ENV CELERY_WORKER_CONCURRENCY=2

CMD poetry run celery worker -A {{cookiecutter.package_dir}}.backend -l INFO --concurrency ${CELERY_WORKER_CONCURRENCY}
