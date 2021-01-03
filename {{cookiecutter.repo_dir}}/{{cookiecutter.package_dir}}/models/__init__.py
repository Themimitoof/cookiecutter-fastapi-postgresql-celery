# Import all the models, so that Base has them before being imported by Alembic
from {{cookiecutter.package_dir}}.db import Base  # noqa
from {{cookiecutter.package_dir}}.models.dummy import Dummy  # noqa
