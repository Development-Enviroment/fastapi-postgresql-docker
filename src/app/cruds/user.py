"""User CRUD Module."""

from datetime import datetime
from typing import List

from sqlalchemy.orm import Session

from app.models.user import UserModel
from app.schemas.user import NewUserSchema, UpdateUserSchema


def get_users(db: Session) -> List[UserModel]:
    """User一覧取得."""
    return db.query(UserModel).filter(UserModel.deleted_at == None)\
                              .order_by(UserModel.id).all()


def get_user_by_id(db: Session, user_id: int) -> UserModel:
    """User取得(id検索)."""
    return db.query(UserModel).filter(UserModel.deleted_at == None,
                                      UserModel.id == user_id).one()


def create_user(db: Session, user: NewUserSchema) -> UserModel:
    """User登録."""
    record = UserModel(name=user.name, email=user.email)
    db.add(record)
    db.commit()
    db.refresh(record)

    return record


def update_user(db: Session, user_id: int, user: UpdateUserSchema) -> UserModel:
    """User更新."""
    record = get_user_by_id(db, user_id)
    record.name = user.name
    record.email = user.email
    db.commit()

    return record


def delete_user(db: Session, user_id: int) -> UserModel:
    """User削除."""
    record = get_user_by_id(db, user_id)
    record.deleted_at = datetime.now()
    db.commit()

    return record
