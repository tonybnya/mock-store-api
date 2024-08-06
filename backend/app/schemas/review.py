"""
SQLAlchemy schema for the review model.
"""

from datetime import datetime

from db.base import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship


class Review(Base):
    """Define the Review model."""

    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    rating = Column(Integer, nullable=False)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    creation_date = Column(DateTime, default=datetime.now)
    update_date = Column(DateTime, default=datetime.now)

    # Relationship with User
    users = relationship("User", back_populates="reviews")

    # Relationship with Product
    products = relationship("Product", back_populates="reviews")
