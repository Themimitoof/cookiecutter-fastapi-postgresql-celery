from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from {{cookiecutter.package_dir}}.config import settings


engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True, pool_recycle=3600,
)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class DBSession:
    def __init__(self, commit_on_exit: bool = False):
        self.session = Session()
        self.commit_on_exit = commit_on_exit

    def __enter__(self):
        return self.session

    def __exit__(self, exc_type, exc_value, traceback):
        sess = self.session

        if exc_type is not None:
            sess.rollback()

        if self.commit_on_exit:
            sess.commit()

        sess.close()


# Import all the models, so that Base has them before being imported by Alembic
from {{cookiecutter.package_dir}}.models.base import Base  # noqa
from {{cookiecutter.package_dir}}.models.dummy import Dummy  # noqa
