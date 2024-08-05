"""
SQLAlchemy schema for the delivery model.
"""

from datetime import datetime

from db.base import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import relationship


class Delivery(Base):
    """Define the delivery model."""

    __tablename__ = "deliveries"

    id = Column(Integer, primary_key=True, index=True)
    delivery_address = Column(JSON, nullable=False)
    status = Column(String(50), nullable=False)
    estimated_delivery_date = Column(DateTime, nullable=False)
    actual_delivery_date = Column(DateTime, nullable=True)
    creation_date = Column(DateTime, default=datetime.now)
    update_date = Column(DateTime, default=datetime.now)

    # Relationship with Order
    # a delivery is linked to an order
    order_id = Column(Integer, ForeignKey("orders.id"))
    order = relationship("Order", back_populates="delivery")
