from pydantic import BaseModel, EmailStr


# This defines a schema for new user registration
class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str  # plan for now, hash this later


# This schema is for logging in
class UserLogin(BaseModel):
    username: str
    password: str


# This schema is used when returning user data
class UserOut(BaseModel):
    id: int
    email: EmailStr
    username: str
    role: str
    is_active: bool

    # FastAPI supports returning ORM objects (like SQLAlchemy models).
    # By default, Pydantic doesn't know how to convert ORM models.

    class Config:
        orm_mode = True  # “This data will come from a SQLAlchemy object — treat it like a dictionary
