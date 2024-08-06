"""
Model for the request body of a review.
A request body is the data sent by a client to the API.
"""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field, conint, constr


class Review(BaseModel):
    """Define a model for a product review."""

    id: int
    user_id: int
    product_id: int
    rating: conint(ge=1, le=5)
    title: constr(max_length=100)
    content: str
    creation_update: datetime = Field(default_factory=datetime.now)
    update_date: datetime = Field(default_factory=datetime.now)

    # Provide configurations to Pydantic
    # Pydantic model will read the data even if it is not a dict,
    # but an ORM model: `id = data["id"]` as well as `id = data.id`
    class Config:
        orm_mode = True
