# user_schema.py

from pydantic import BaseModel, EmailStr
from typing import Optional


# shared base class (used internally)
class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None
    disabled: Optional[bool] = False


# Input schema when registering or creating
class UserCreate(UserBase):
    password: str


# Output schema when sending user info back
class UserRead(UserBase):
    id: int


# Optional update schema
class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    disabled: Optional[bool] = None
