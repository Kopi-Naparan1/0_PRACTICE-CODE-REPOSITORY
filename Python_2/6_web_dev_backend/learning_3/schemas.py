# from schemas.py
from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str
