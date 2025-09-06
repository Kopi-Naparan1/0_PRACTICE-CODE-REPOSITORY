from pydantic import BaseModel, Field
from typing import Optional


class UserData(BaseModel):
    username: str = Field(min_length=1, max_length=64)
    password: str = Field(min_length=8, max_length=128)
    role: str = Field(default='user')


class GiveToken(BaseModel):
    access_token: str
    token_type: str


class GiveUserInfo(BaseModel):
    username: str
    role: str


class GiveAdminInfo(BaseModel):
    username: str
    role: str
    registered_users: int


