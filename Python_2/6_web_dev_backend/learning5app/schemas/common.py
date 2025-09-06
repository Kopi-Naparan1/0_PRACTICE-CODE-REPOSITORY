# common.py

from pydantic import BaseModel


class Message(BaseModel):
    detail: str