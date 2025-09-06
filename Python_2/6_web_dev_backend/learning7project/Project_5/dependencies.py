# dependencies.py

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from auth_handler import verify_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verify_access_token(token)
    username = payload.get('sub')

    if not username:
        raise HTTPException(status_code=401, detail="Invalid token payload")

    return username
