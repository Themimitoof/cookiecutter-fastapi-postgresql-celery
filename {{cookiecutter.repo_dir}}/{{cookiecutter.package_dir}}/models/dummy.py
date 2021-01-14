from sqlalchemy import Column, Integer, String

from {{cookiecutter.package_dir}}.models import Base


class Dummy(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
