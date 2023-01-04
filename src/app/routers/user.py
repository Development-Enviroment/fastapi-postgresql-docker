"""User API Router."""

import logging
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

from app.cruds import user as cruds
from app.models.user import UserModel
from app.schemas.user import NewUserSchema, UpdateUserSchema, UserSchema
from lib.database.database import get_db

router = APIRouter(
    prefix="/api",
    tags=["users"]
)


@router.get("/users/", response_model=List[UserSchema])
def get_users(db: Session = Depends(get_db)) -> List[UserModel]:
    """User一覧取得API."""
    try:
        return cruds.get_users(db)

    except Exception as error:
        logging.exception(error)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))


@router.get("/users/{user_id}", response_model=UserSchema)
def get_user(user_id: int, db: Session = Depends(get_db)) -> UserModel:
    """User取得API(id検索)."""
    try:
        return cruds.get_user_by_id(db, user_id)

    except NoResultFound as no_result_error:
        logging.exception(no_result_error)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(no_result_error))

    except Exception as error:
        logging.exception(error)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))


@router.post("/users/", response_model=UserSchema)
def create_user(user: NewUserSchema, db: Session = Depends(get_db)) -> UserModel:
    """User登録API."""
    try:
        result = cruds.create_user(db, user)
        return result

    except Exception as error:
        db.rollback()
        logging.exception(error)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))


@router.put("/users/{user_id}", response_model=UserSchema)
def update_user(user_id: int, user: UpdateUserSchema, db: Session = Depends(get_db)) -> UserModel:
    """User更新API."""
    try:
        result = cruds.update_user(db, user_id, user)
        return result

    except NoResultFound as no_result_error:
        logging.exception(no_result_error)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(no_result_error))

    except Exception as error:
        db.rollback()
        logging.exception(error)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))


@router.delete("/users/{user_id}", response_model=UserSchema)
def delete_user(user_id: int, db: Session = Depends(get_db)) -> UserModel:
    """User削除API."""
    try:
        result = cruds.delete_user(db, user_id)
        return result

    except NoResultFound as no_result_error:
        logging.exception(no_result_error)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(no_result_error))

    except Exception as error:
        db.rollback()
        logging.exception(error)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))
