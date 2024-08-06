"""
Model for request body of a cart.
A request body is the data sent by a client to the API.
"""

from __future__ import annotations

from datetime import datetime
from typing import List

from pydantic import BaseModel, Field

from .product import Product


class CartItem(BaseModel):
    """Define a model for an item in the cart."""

    product: Product
    quantity: int

    # Provide configurations to Pydantic
    # Pydantic model will read the data even if it is not a dict,
    # but an ORM model: `id = data["id"]` as well as `id = data.id`
    class Config:
        orm_mode = True


class Cart(BaseModel):
    """Define a model for the cart."""

    id: int
    user_id: int
    items: List[CartItem]
    creation_date: datetime = Field(default_factory=datetime.now)
    update_date: datetime = Field(default_factory=datetime.now)

    # Provide configurations to Pydantic
    # Pydantic model will read the data even if it is not a dict,
    # but an ORM model: `id = data["id"]` as well as `id = data.id`
    class Config:
        orm_mode = True
