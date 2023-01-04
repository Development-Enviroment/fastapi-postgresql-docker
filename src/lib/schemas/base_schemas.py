"""Base Schemas Module."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CustomBaseSchemas(BaseModel):
    """Base Schemas Class."""

    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]

    class Config:
        """Base Schemas Config Class."""

        orm_mode = True
