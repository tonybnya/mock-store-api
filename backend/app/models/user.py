"""
Model for the request body of a user.
A request body is the data sent by a client to the API.
"""

from __future__ import annotations

from datetime import datetime
from typing import Dict

from pydantic import BaseModel, EmailStr, Field, constr

# The pattern below ensures the password meets these criteria:
# Minimum length of 8 characters.
# Maximum length of 16 characters.
# At least one uppercase letter.
# At least one lowercase letter.
# At least one digit.
# At least one special character.
pattern: str = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,16}$"


class UserBase(BaseModel):
    """Define a base model with common attributes for a user."""

    is_active: bool = True
    shipping_address: Dict[str, str]
    billing_address: Dict[str, str]
    registration_date: datetime = Field(default_factory=datetime.now)
    update_date: datetime = Field(default_factory=datetime.now)

    # Provide configurations to Pydantic
    # Pydantic model will read the data even if it is not a dict,
    # but an ORM model: `id = data["id"]` as well as `id = data.id`
    class Config:
        orm_mode = True


class UserCreate(UserBase):
    """Define a model for creating a new user."""

    password: constr(min_length=8, max_length=16, pattern=pattern)


class User(UserBase):
    """Define a model for reading user data (excluding sensitive information)."""

    id: int
    username: str = Field(min_length=1)
    email: EmailStr
