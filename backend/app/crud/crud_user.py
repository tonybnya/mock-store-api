"""
CRUD utils for the User Pydantic model.
"""

from __future__ import annotations

from typing import List, Optional

from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int) -> Optional[models.User]:
    """
    READ a single user by id
    Input:  db      | database session
    Input:  user_id | the id of the user to read
    Output: the first result found with the given id, otherwise None
    """
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> Optional[models.User]:
    """
    READ a single user by email
    Input:  db      | database session
    Input:  email   | the email of the user to read
    Output: the first result found with the given email, otherwise None
    """
    return db.query(models.User).filter(models.User.email == email).first()


def get_user_by_username(db: Session, username: str) -> Optional[models.User]:
    """
    READ a single user by username
    Input:  db          | database session
    Input:  username    | the username of the user to read
    Output: the first result found with the given username, otherwise None
    """
    return db.query(models.User).filter(models.User.username == username).first()

def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[models.User]:
    """
    READ all the users in the database
    Input:  db      | database session
    Input:  skip    | the offset to apply for the fecthing
    Input:  limit   | the limit of data for fetching
    Ouput:  a list containing all the data/users fetched
    """
    return db.query(models.User).offset(skip).limit(limit).all()
