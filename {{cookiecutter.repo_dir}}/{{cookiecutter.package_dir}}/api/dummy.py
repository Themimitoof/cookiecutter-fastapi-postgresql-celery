from typing import Any, Dict, List

from fastapi import APIRouter, HTTPException

from {{cookiecutter.package_dir}} import models
from {{cookiecutter.package_dir}}.backend.tasks.dummy import dummy_created
from {{cookiecutter.package_dir}}.models import DBSession
from {{cookiecutter.package_dir}}.schemas.dummy import (
    DummyCreateSchema,
    DummyInDBBaseSchema,
    DummyReturnSchema,
    DummyUpdateSchema,
)

router = APIRouter()


@router.get("", response_model=List[DummyReturnSchema])
def read_dummies(skip: int = 0, limit: int = 100) -> Any:
    """
    Retrieve dummies.
    """

    with DBSession() as db:
        dummies = db.query(models.Dummy).offset(skip).limit(limit).all()

    return dummies


@router.get("/{id}", response_model=DummyReturnSchema)
def read_item(*, id: int) -> Any:
    """
    Get dummy by ID.
    """

    dummy = models.Dummy.by_id(id)

    if not dummy:
        raise HTTPException(status_code=404, detail="Item not found.")

    return dummy


@router.post("", response_model=DummyReturnSchema)
def create_dummy(*, dummy: DummyCreateSchema) -> Any:
    """
    Create new dummy.
    """

    dummy = models.Dummy.create(dummy)

    dummy_created.delay(DummyInDBBaseSchema.from_orm(dummy).dict())

    return dummy


@router.patch("/{id}", response_model=DummyReturnSchema)
def update_item(*, id: int, dummy_in: DummyUpdateSchema) -> Any:
    """
    Update a dummy.
    """

    dummy = models.Dummy.by_id(id)

    if not dummy:
        raise HTTPException(status_code=404, detail="Item not found")

    dummy = dummy.update(dummy_in)

    return dummy


@router.delete("/{id}", response_model=Dict[Any, Any])
def delete_item(*, id: int) -> Any:
    """
    Delete a dummy.
    """

    dummy = models.Dummy.by_id(id)

    if not dummy:
        raise HTTPException(status_code=404, detail="Item not found")

    dummy.delete()

    return {}
