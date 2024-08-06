"""
Model for the request body of a product.
A request body is the data sent by a client to the API.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union

from pydantic import BaseModel, Field, HttpUrl


class Product(BaseModel):
    """Define a model for a product."""

    id: int
    name: str
    category: str
    price: float
    stock: int
    description: Union[str, None] = None
    image_url: HttpUrl
    creation_date: datetime = Field(default_factory=datetime.now)
    update_date: datetime = Field(default_factory=datetime.now)

    # Provide configurations to Pydantic
    # Pydantic model will read the data even if it is not a dict,
    # but an ORM model: `id = data["id"]` as well as `id = data.id`
    class Config:
        orm_mode = True
