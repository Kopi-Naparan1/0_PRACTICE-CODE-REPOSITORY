# main.py
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel, Field

from auth_handler import create_access_token, JWTBearer
from hashing import get_password_hash, verify_password_hash

app = FastAPI()

fake_db = {}


class UserInfo(BaseModel):
    """Defines the schema for registration."""
    username: str = Field(min_length=1, max_length=32)
    password: str = Field(min_length=1, max_length=64)


class UserLogin(BaseModel):
    """Same fields as UserInfo, but used separately for /login just to show decoupled input models (good practice)."""
    username: str = Field(min_length=1, max_length=32)
    password: str = Field(min_length=1, max_length=64)


class Token(BaseModel):
    access_token: str
    token_type: str


@app.post("/register")  # This endpoint expects a POST request with UserInfo schema.
def register_user(data: UserInfo):
    """Accepts username + password, stores hashed password in fake_db"""

    if data.username in fake_db:
        raise HTTPException(400, "User already exist")

    hashed_password = get_password_hash(data.password)
    fake_db[data.username] = hashed_password
    return {"message": "User is now registered"}


@app.post("/token", response_model=Token)
def login_user(form_data: OAuth2PasswordRequestForm = Depends()):  # Receives login credentialsReceives login credential
    """	Verifies user, returns JWT token"""
    username = form_data.username
    password = form_data.password

    stored_password_hash = fake_db.get(username)  # Retrieves the stored hash for that username

    if not stored_password_hash:
        raise HTTPException(404, "Username not found")

    if not verify_password_hash(password, stored_password_hash):
        raise HTTPException(401, "Wrong username or password")

    token = create_access_token({"sub": username})
    return Token(
        access_token=token,
        token_type="bearer"
    )


@app.get("/me")  # blocks access without valid token
def current_logged_in_user(payload: dict = Depends(JWTBearer)):
    """Protected route that shows current user by decoding token"""

    username = payload.get('sub')

    if username is None:
        raise HTTPException(401, detail="Invalid token payload")
    return {"username": username}
