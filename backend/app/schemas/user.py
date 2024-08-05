"""
SQLAlchemy schema for the user model.
"""

from datetime import datetime

from db.base import Base
from sqlalchemy import JSON, Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import relationship


class User(Base):
    """Define the user schema."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    shipping_address = Column(JSON)  # Using JSON type for storing dictionaries
    billing_address = Column(JSON)  # Using JSON type for storing dictionaries
    registration_date = Column(DateTime, default=datetime.now)
    update_date = Column(DateTime, default=datetime.now)

    orders = relationship("Order", back_populates="user")
    reviews = relationship("Review", back_populates="user")
    cart = relationship("Cart", uselist=False, back_populates="user")
