"""
SQLAlchemy schema for the order model.
"""

from datetime import datetime

from db.base import Base
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Order(Base):
    """Define the Order model."""

    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    total_price = Column(Float, nullable=False)
    status = Column(String, nullable=False)
    creation_date = Column(DateTime, default=datetime.now)
    update_date = Column(DateTime, default=datetime.now)

    # Relationship with User
    user = relationship("User", back_populates="orders")

    # Relationship with OrderItem
    order_items = relationship("OrderItem", back_populates="order")


class OrderItem(Base):
    """Define the OrderItem model."""

    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)

    # Relationship with Order
    order = relationship("Order", back_populates="order_items")

    # Relationship with Product
    product = relationship("Product", back_populates="order_items")
