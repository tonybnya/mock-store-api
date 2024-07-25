"""
This is the main file.
The entry point of the entire application.
"""

from __future__ import annotations

from enum import Enum
from typing import Union

from fastapi import FastAPI

app = FastAPI(title="Mock Store API", version="1.0.0")


@app.get("/")
async def index() -> dict[str, str]:
    """Return `Hello, World!`
    A message in a JSON format.
    """
    return {"message": "Hello, World!"}
