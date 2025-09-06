# routes/user_routes.py

from fastapi import APIRouter, Depends, HTTPException, status
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import decode_access_token
from app.models.user_model import users_db
from app.schemas.user_schema import UserPublic

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    dependencies=[Depends(JWTBearer())]  # ✅ Require token for all routes
)


@router.get("/me", response_model=UserPublic)
def get_my_profile(token: str = Depends(JWTBearer())):
    """
    🧑‍💼 Get current user info (based on token)
    """
    payload = decode_access_token(token)
    username = payload["sub"]

    user = next((u for u in users_db if u["username"] == username), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "username": user["username"],
        "email": user["email"],
        "full_name": user["full_name"]
    }


@router.get("/{username}", response_model=UserPublic)
def get_user_profile(username: str):
    """
    🧾 View public profile of another user
    """
    user = next((u for u in users_db if u["username"] == username), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "username": user["username"],
        "email": user["email"],
        "full_name": user["full_name"]
    }


@router.put("/disable/{username}", status_code=204)
def disable_user(username: str):
    """
    ❌ Admin disables a user (sets disabled: True)
    """
    user = next((u for u in users_db if u["username"] == username), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user["disabled"] = True
    return
