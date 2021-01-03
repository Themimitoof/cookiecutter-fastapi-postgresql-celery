from typing import Optional

from pydantic import BaseModel


# Shared properties
class DummyBaseSchema(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


# Properties shared by models stored in DB
class DummyInDBBaseSchema(DummyBaseSchema):
    id: int
    title: str

    class Config:
        orm_mode = True


# Properties properties stored in DB
class DummyInDBSchema(DummyInDBBaseSchema):
    pass


# Properties to receive on dummy creation
class DummyCreateSchema(DummyBaseSchema):
    title: str


# Properties to receive on dummy update
class DummyUpdateSchema(DummyBaseSchema):
    pass


# Properties to return to client
class DummyReturnSchema(DummyInDBBaseSchema):
    pass
