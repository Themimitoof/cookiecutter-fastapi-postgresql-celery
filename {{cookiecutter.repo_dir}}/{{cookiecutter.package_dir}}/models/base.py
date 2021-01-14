from typing import Any

from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.declarative import declarative_base, declared_attr

from {{cookiecutter.package_dir}}.models import DBSession


class Base_:
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

        with DBSession() as db:
            return db.query(cls).filter(cls.id == id).first()

    @classmethod
    def create(cls, schema):
        """
        Creates an entry for the current table and returns it once in the database.
        """

        content = jsonable_encoder(schema)
        obj = cls(**content)

        with DBSession() as db:
            db.add(obj)
            db.commit()
            db.refresh(obj)

        return obj

    def delete(self):
        """
        Hard delete the current object.
        """

        with DBSession() as db:
            db.delete(self)
            db.commit()

        return

    def update(self, schema, **kwargs):
        """
        Updates the current object.
        """

        content = jsonable_encoder(schema)

        for key, value in content.items():
            setattr(self, key, value)

        with DBSession() as db:
            db.commit()

        return self


Base = declarative_base(cls=Base_)
