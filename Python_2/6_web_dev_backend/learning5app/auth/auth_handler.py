#auth/auth_handler.py

from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import HTTPException, status

#  Purpose:
#  (1) create jwt token
#  (2) verify token
#  (3) adding expiration date


SECRET_KEY = 'mysecret'
ALGORITHM = 'HS256'


def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload

    except JWTError:
        return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid token",
        headers={"WWW-Authenticate": "Bearer"})


def create_access_token(data: dict,
                        expires_delta: timedelta = timedelta(minutes=30))
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

