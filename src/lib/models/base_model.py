"""Base Modele Module."""

from datetime import datetime

from sqlalchemy import Column, DateTime
from sqlalchemy.sql.functions import current_timestamp


class BaseModele:
    """Base Model Class."""

    created_at = Column(DateTime, server_default=current_timestamp(), nullable=False)
    updated_at = Column(DateTime, onupdate=datetime.now())
    deleted_at = Column(DateTime)
