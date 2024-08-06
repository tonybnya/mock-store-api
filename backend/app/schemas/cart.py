"""
SQLAlchemy schema for the cart model.
"""

from datetime import datetime

from db.base import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Cart(Base):
    """Define the cart schema."""

    __tablename__ = "carts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    creation_date = Column(DateTime, default=datetime.now)
    update_date = Column(DateTime, default=datetime.now)

    users = relationship("User", back_populates="carts")
    cart_items = relationship("CartItem", back_populates="carts")


class CartItem(Base):
    """Define the cart item schema."""

    __tablename__ = "cart_items"

    id = Column(Integer, primary_key=True, index=True)
    cart_id = Column(Integer, ForeignKey("carts.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)

    # Relationship with Cart
    carts = relationship("Cart", back_populates="cart_items")

    # Relationship with Product
    products = relationship("Product", back_populates="cart_items")
