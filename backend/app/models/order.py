"""
Model for the request body of an order.
A request body is the data sent by a client to the API.
"""

from __future__ import annotations

from datetime import datetime
from typing import List

from pydantic import BaseModel, Field

from .product import Product


class OrderItem(BaseModel):
    """Define a model for an item in the order."""

    product: Product
    quantity: int
    price: float

    # Provide configurations to Pydantic
    # Pydantic model will read the data even if it is not a dict,
    # but an ORM model: `id = data["id"]` as well as `id = data.id`
    class Config:
        orm_mode = True


class Order(BaseModel):
    """Define a model for an order."""

    id: int
    user_id: int
    items: List[OrderItem]
    total_price: float
    status: str
    creation_date: datetime = Field(default_factory=datetime.now)
    update_date: datetime = Field(default_factory=datetime.now)

    # Provide configurations to Pydantic
    # Pydantic model will read the data even if it is not a dict,
    # but an ORM model: `id = data["id"]` as well as `id = data.id`
    class Config:
        orm_mode = True
