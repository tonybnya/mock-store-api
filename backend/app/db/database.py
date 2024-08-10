"""
Handle the session and create the SQLAlchemy engine for the database.
Define the base class for my models.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a database URL for SQLAlchemy
SQLALCHEMY_DATABASE_URL = "sqlite:///./mock_store_api.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# Create the SQLAlchemy engine
# The argument 'connect_args={"check_same_thread": False}'
# is needed only for SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create a SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class
Base = declarative_base()
