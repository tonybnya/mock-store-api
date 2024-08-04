"""
Model for the request body of a product.
A request body is the data sent by a client to the API.
"""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field, HttpUrl


class Product(BaseModel):
    """Define a model for a product."""

    id: int
    name: str
    category: str
    price: float
    stock: int
    description: str | None = None
    image_url: HttpUrl
    creation_date: datetime = Field(default_factory=datetime.now)
    update_date: datetime = Field(default_factory=datetime.now)
