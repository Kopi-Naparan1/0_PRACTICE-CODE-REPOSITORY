from fastapi.security import OAuth2PasswordRequestForm
from fastapi import FastAPI, HTTPException, Depends
from models import UserData, GiveToken, GiveUserInfo, GiveAdminInfo
from hashing import hash_plain_password, verify_plain_password
from auth_handler import create_access_token
from helper import user_id_generator
from dependencies import get_current_user_payload, get_current_admin_payload

app = FastAPI()

fake_db = {}


@app.post("/register")
def register_user(user_data: UserData):

    user_id = user_id_generator()
    hashed_password = hash_plain_password(user_data.password)

    fake_db[user_id] = {
        "username": user_data.username,
        "password": hashed_password,
        "role": user_data.role
    }

    if fake_db[user_id]["role"] == "admin":
        return {"message": "Admin is now registered!"}
    return {"message": "User is now registered!"}


@app.post("/login", response_model=GiveToken)
def login_user(form: OAuth2PasswordRequestForm = Depends()):
    username = form.username
    password = form.password

    for user_id, data in fake_db.items():
        if data["username"] == username:
            if verify_plain_password(password, data["password"]):
                token = create_access_token({"user_id": user_id,
                                             "role": data["role"]})
                return GiveToken(
                    access_token=token,
                    token_type="bearer",
                ).dict()

            else:
                raise HTTPException(401, detail="Incorrect password or username")

    raise HTTPException(401, detail="User not found")


@app.get("/users/me", response_model=GiveUserInfo)
def get_user_profile(user_payload: dict = Depends(get_current_user_payload)):
    user_id = user_payload["user_id"]
    user_data = fake_db.get(user_id)

    if not user_data:
        raise HTTPException(401, detail="Invalid user data")

    return GiveUserInfo(
        username=user_data["username"],
        role=user_data["role"]
    )


@app.get("/admin/dashboard", response_model=GiveAdminInfo)
def get_admin_dashboard(admin_payload: dict = Depends(get_current_admin_payload)):
    user_id = admin_payload["user_id"]
    user_data = fake_db.get(user_id)
    numbers_of_registered_users = len(fake_db)

    if not user_data:
        raise HTTPException(401, detail="Invalid admin data")

    return GiveAdminInfo(
        username=user_data["username"],
        role=user_data["role"],
        registered_users=numbers_of_registered_users,
    )
