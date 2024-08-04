"""
Model for the request body of an user.
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
pattern: str = r"^(?=.*[a-zA-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,16}$"


class User(BaseModel):
    """Define a model for a user."""

    id: int
    username: str
    email: EmailStr
    shipping_address: Dict[str, str]
    billing_address: Dict[str, str]
    password: constr(min_length=8, max_length=16, pattern=pattern)
    registration_date: datetime = Field(default_factory=datetime.now)
    update_date: datetime = Field(default_factory=datetime.now)
