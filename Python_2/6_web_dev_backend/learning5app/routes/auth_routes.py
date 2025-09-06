# routes/auth_routes.py

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.auth.hashing import Hash
from app.auth.jwt_handler import create_access_token
from app.schemas.token_schema import TokenResponse
from app.schemas.auth_schema import LoginRequest
from app.models.user_model import fake_users_db  # Replace this with DB in real apps
from app.models.user_model import UserModel


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


# Route: /auth/login
@router.post("/login", response_model=TokenResponse)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    🔐 This is the LOGIN route.
    ✅ It receives form data (username + password)
    ✅ Checks if the user exists and password is correct
    ✅ Returns a JWT access token
    """
    # 1. Look for the user in the database
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials (user not found)"
        )

    # 2. Convert dict to model (for easier attribute access)
    user = UserModel(**user_dict)

    # 3. Check if password is correct
    if not Hash.verify(user.password, form_data.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials (wrong password)"
        )

    # 4. Create the JWT token (valid for 30 minutes)
    access_token = create_access_token(data={"sub": user.username})

    # 5. Return the token
    return {"access_token": access_token, "token_type": "bearer"}
