from typing import Any, Generator

from fastapi.encoders import jsonable_encoder
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import sessionmaker

from {{cookiecutter.package_dir}}.config import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@as_declarative()
class Base:
    id: Any
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        """Generate automatically the table name."""

        return cls.__name__.lower()

    # -- Common filters

    @classmethod
    def by_id(cls, id: str) -> Any:
        """
        Get the first entry in the database with the given id.
        """

        db = get_db()

        return db.query(cls).filter(cls.id == id).first()

    @classmethod
    def create(cls, **kwargs):
        """
        Creates an entry for the current table and returns it once in the database.
        """

        db = get_db()

        content = jsonable_encoder(**kwargs)
        obj = cls(**content)

        db.add(obj)
        db.commit()
        db.refresh(obj)

        return obj

    def delete(self):
        """
        Hard delete the current object.
        """

        db = get_db()
        db.delete(self)
        db.commit()

        return

    def update(self, **kwargs):
        """
        Updates the current object.
        """

        pass
