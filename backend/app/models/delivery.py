"""
Model for the request body of a delivery.
A request body is the data sent by a client to the API.
"""

from __future__ import annotations

from datetime import datetime
from typing import Dict

from pydantic import BaseModel, Field, constr


class Delivery(BaseModel):
    """Define a model for delivery details."""

    id: int
    delivery_address: Dict[str, str]
    status: constr(max_length=50)
    estimated_delivery_date: datetime
    actual_deliveray_date: datetime = Field(default_factory=None)
    creation_date: datetime = Field(default_factory=datetime.now)
    update_date: datetime = Field(default_factory=datetime.now)
