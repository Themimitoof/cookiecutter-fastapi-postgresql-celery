from typing import Any, List, Dict

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from {{cookiecutter.package_dir}} import models
from {{cookiecutter.package_dir}}.db import get_db
from {{cookiecutter.package_dir}}.schemas.dummy import (
    DummyCreateSchema,
    DummyReturnSchema,
    DummyUpdateSchema,
)

router = APIRouter()


@router.get("/", response_model=List[DummyReturnSchema])
def read_dummies(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve dummies.
    """

    dummies = db.query(models.Dummy).offset(skip).limit(limit).all()

    return dummies


@router.get("/{id}", response_model=DummyReturnSchema)
def read_item(
    *,
    db: Session = Depends(get_db),
    id: int,
) -> Any:
    """
    Get dummy by ID.
    """

    dummy = models.Dummy.by_id(id)

    if not dummy:
        raise HTTPException(status_code=404, detail="Item not found.")

    return dummy


@router.post("/", response_model=DummyReturnSchema)
def create_dummy(
    *,
    db: Session = Depends(get_db),
    dummy_in: DummyCreateSchema,
) -> Any:
    """
    Create new dummy.
    """

    dummy = models.Dummy.create(**dummy_in)

    return dummy


@router.put("/{id}", response_model=DummyReturnSchema)
def update_item(
    *,
    db: Session = Depends(get_db),
    id: int,
    dummy_in: DummyUpdateSchema,
) -> Any:
    """
    Update a dummy.
    """

    dummy = models.Dummy.by_id(id)
    if not dummy:
        raise HTTPException(status_code=404, detail="Item not found")

    dummy = dummy.update(**dummy_in)

    return dummy


@router.delete("/{id}", response_model=Dict[Any, Any])
def delete_item(
    *,
    db: Session = Depends(get_db),
    id: int,
) -> Any:
    """
    Delete a dummy.
    """
    dummy = models.Dummy.by_id(id)

    if not dummy:
        raise HTTPException(status_code=404, detail="Item not found")

    dummy.delete()

    return {}
