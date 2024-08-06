"""
SQLAlchemy schema for the product model.
"""

from datetime import datetime

from db.base import Base
from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.orm import relationship


class Product(Base):
    """Define the product schema."""

    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category = Column(String, index=True)
    price = Column(Float)
    stock = Column(Integer)
    description = Column(String, nullable=True)
    image_url = Column(String)
    creation_date = Column(DateTime, default=datetime.now)
    update_date = Column(DateTime, default=datetime.now)

    # Relationship with Review
    reviews = relationship("Review", back_populates="products")

    # Relationship with OrderItem
    order_items = relationship("OrderItem", back_populates="products")

    # Relationship with CartItem
    cart_items = relationship("CartItem", back_populates="products")
