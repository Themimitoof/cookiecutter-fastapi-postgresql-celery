from celery import Celery

from {{cookiecutter.package_dir}}.config import settings

app = Celery(__name__, broker=settings.CELERY_BROKER_DSN)

app.conf.task_default_queue = "dummy"
app.conf.imports = ["{{cookiecutter.package_dir}}.backend.tasks.dummy"]
