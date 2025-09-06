# auth_handler.py

from fastapi import HTTPException
# from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials, OAuth2PasswordRequestForm
# from starlette.status import HTTP_403_FORBIDDEN
from datetime import datetime, timedelta
from jose import jwt, ExpiredSignatureError, JWTError
# from fastapi.security import OAuth2PasswordBearer
from config import SECRET_KEY, ALGORITHM, TOKEN_EXPIRATION_MINUTES


def create_access_token(data: dict):
    to_encode = data.copy()
    expiry_time = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRATION_MINUTES)

    to_encode.update({"exp": expiry_time,
                      "iat": datetime.utcnow(),
                      "iss": "myapp",
                      "aud": "myapp_users"})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str):
    try:
        decoded_jwt = jwt.decode(token,
                                 SECRET_KEY,
                                 algorithms=[ALGORITHM],
                                 audience="myapp_users",
                                 issuer="myapp",)
        return decoded_jwt

    except ExpiredSignatureError:
        raise HTTPException(401, detail="Expired token")

    except JWTError:
        raise HTTPException(401, detail='Invalid Token')
