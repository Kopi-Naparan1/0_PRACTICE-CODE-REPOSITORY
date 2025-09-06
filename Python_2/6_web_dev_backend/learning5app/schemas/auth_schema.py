# auth_schema.py

from pydantic import BaseModel, EmailStr, Field

class LoginForm(BaseModel):
    username: EmailStr
    password: str = Field(min_length=6)



