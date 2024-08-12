"""
Dependencies Module.
"""

from __future__ import annotations

from app import models
from app.db.database import SessionLocal, engine

# Create the database  and the tables
# if they doesn't already exist
models.Base.metadata.create_all(bind=engine)


# Use the SessionLocal class to create a dependency
# This dependency will create a new SQLAlchemy SessionLocal
# that will be used in a single request, and then close it
# once the request is finished
def get_db():
    """
    Create a dependency.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
