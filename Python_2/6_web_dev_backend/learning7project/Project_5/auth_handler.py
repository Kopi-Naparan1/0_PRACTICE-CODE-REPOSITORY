# auth_handler.py


from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials, OAuth2PasswordRequestForm
from starlette.status import HTTP_403_FORBIDDEN
from datetime import datetime, timedelta
from jose import JWTError, jwt, ExpiredSignatureError
from fastapi.security import OAuth2PasswordBearer
from helper import TOKEN_EXPIRATION
from config import SECRET_KEY, ALGORITHM


def create_access_token(data: dict):
    to_encode = data.copy()
    expiry_time = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRATION)

    to_encode.update({"exp": expiry_time,
                      "iat": datetime.utcnow(),
                      "iss": "myapp",
                      "aud": "myapp_users"})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_access_token(token: str):

    try:
        decoded_jwt = jwt.decode(token,
                                 SECRET_KEY,
                                 algorithms=[ALGORITHM],
                                 audience="myapp_users",
                                 issuer="myapp")
        return decoded_jwt

    except ExpiredSignatureError:
        raise HTTPException(401, detail="Token expired")

    except JWTError:
        raise HTTPException(401, detail="Unauthorized")





