from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from auth_handler import decode_access_token


oauth2scheme = OAuth2PasswordBearer(tokenUrl="/login")


def get_current_user_payload(token: str = Depends(oauth2scheme)):
    payload = decode_access_token(token)
    user_id = payload.get("user_id")
    role = payload.get("role")

    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token payload")

    if role != 'user' or role != "admin":
        raise HTTPException(status_code=401, detail="Invalid token payload - role is not valid")
    return payload


def get_current_admin_payload(token: str = Depends(oauth2scheme)):
    payload = decode_access_token(token)
    user_id = payload.get("user_id")
    role = payload.get("role")

    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token payload")

    if role != 'admin':
        raise HTTPException(status_code=401, detail="Invalid token payload. Only Admin allowed")
    return payload
