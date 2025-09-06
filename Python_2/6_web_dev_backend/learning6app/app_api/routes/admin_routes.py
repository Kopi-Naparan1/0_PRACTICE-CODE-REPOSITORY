# APIRouter: Modular route group
from fastapi import APIRouter, Depends, HTTPException, status
from learning6app.app_api.auth.auth_handler import get_current_user
from learning6app.app_api.models.user_model import User


# Creates a route group: all endpoints will start with /admin. They will appear under the"Admin" tag in Swagger
router = APIRouter(prefix="/admin", tags=["Admin"])


# Get /admin/dashboard. This is connected to the router.
@router.get("/dashboard", response_model=dict)  # The response model must be a dictionary.
def get_admin_dashboard(current_user: User = Depends(get_current_user)):
    # "User" is from the model.py. Then current user depends on the get_current_user from auth_handler.py

    # Check if the current user's role is 'admin'. If not, deny access with HTTP 403.
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admins only",

        )

    return {"message": f"Welcome Admin {current_user.username}!"}
