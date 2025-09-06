# routes/token_routes.py

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.auth.hashing import Hasher
from app.auth.auth_handler import sign_jwt
from app.schemas.token_schema import TokenResponse
from app.schemas.auth_schema import LoginRequest
from app.models.user_model import users_db  # fake DB

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/token", response_model=TokenResponse)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    🎯 Accepts form input: username and password.
    If valid, returns JWT token.
    """
    username = form_data.username
    password = form_data.password

    # 1️⃣ Check if user exists in fake DB
    user = next((u for u in users_db if u["username"] == username), None)

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid user")

    # 2️⃣ Verify password using hasher
    if not Hasher.verify_password(password, user["hashed_password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password")

    # 3️⃣ Create signed JWT token
    token = sign_jwt(user["username"])

    return {"access_token": token, "token_type": "bearer"}
