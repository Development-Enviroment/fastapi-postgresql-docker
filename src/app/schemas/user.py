"""User Schemas Module."""

from lib.schemas.base_schemas import CustomBaseSchemas


class UserSchema(CustomBaseSchemas):
    """User Schema Class."""

    id: int
    name: str
    email: str


class NewUserSchema(CustomBaseSchemas):
    """New User Schema Class."""

    name: str
    email: str


class UpdateUserSchema(CustomBaseSchemas):
    """Update User Schema Class."""

    name: str
    email: str
