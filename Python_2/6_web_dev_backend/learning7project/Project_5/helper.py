# helper.py

from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel, Field
from typing import List


TOKEN_EXPIRATION = 30


class UserData(BaseModel):
    username: str = Field(min_length=1, max_length=32)
    password: str = Field(min_length=1, max_length=64)


class UserLoginInfo(BaseModel):
    username: str
    password: str


class GiveToken(BaseModel):
    access_token: str
    token_type:  str


class ArticleInfoIn(BaseModel):
    title: str
    body: str


class ArticleInfoOut(BaseModel):
    id: int
    posts: ArticleInfoIn
