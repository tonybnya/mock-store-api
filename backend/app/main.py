"""
This is the main file.
The entry point of the entire application.
"""

from __future__ import annotations

from fastapi import FastAPI

app = FastAPI(title="Mock Store API", version="1.0.0")


@app.get("/")
def index() -> dict[str, str]:
    """Return `Hello, World!`
    The message is a dictionary.
    """
    return {"message": "Hello, World!"}
