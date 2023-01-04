"User Model Module."

from sqlalchemy import Column, Integer, String

from lib.database.database import Base
from lib.models.base_model import BaseModele


class UserModel(Base, BaseModele):
    """User Model Class."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
