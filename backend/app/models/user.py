"""
Model for the request body of a user.
A request body is the data sent by a client to the API.
"""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, EmailStr, Field

# Pattern for password validation
# The pattern below ensures the password meets these criteria:
# Minimum length of 8 characters
# Maximum length of 16 characters
# At least one uppercase letter
# At least one lowercase letter
# At least one digit
# At least one special character
pattern_pwd: str = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,16}$"

# Pattern for email validation
pattern_email: str = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,24}$"


class Address(BaseModel):
    """Define an address class."""

    country: str
    state: str
    city: str
    street: str
    zip: str


class UserBase(BaseModel):
    """Define a base model with common attributes for a user."""

    is_active: bool = True
    shipping_address: Address
    billing_address: Address
    registration_date: datetime = Field(default=datetime.now)
    update_date: datetime = Field(default=datetime.now)

    # Provide configurations to Pydantic
    # Pydantic model will read the data even if it is not a dict,
    # but an ORM model: `id = data["id"]` as well as `id = data.id`
    class Config:
        orm_mode = True


class UserCreate(UserBase):
    """Define a model for creating a new user."""

    password: str = Field(min_length=8, max_length=16, pattern=pattern_pwd)


class User(UserBase):
    """Define a model for reading user data (excluding sensitive information)."""

    id: int
    username: str = Field(min_length=1)
    email: EmailStr = Field(pattern=pattern_email)
