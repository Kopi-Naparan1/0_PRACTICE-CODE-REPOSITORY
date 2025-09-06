from fastapi import APIRouter, Depends
from learning6app.app_api.auth.auth_handler import get_current_user
from learning6app.app_api.models.user_model import User

# You're creating a sub-router that will handle all routes defined here
# This will later be included in main.py or api.py using app.include_router(...)
router = APIRouter()


@router.get("/users/me")
def read_users_me(current_user: User = Depends(get_current_user)):
    # This function job is to return username and email of the valid user.
    return {
        "username": current_user.username,
        "email": current_user.email
    }



