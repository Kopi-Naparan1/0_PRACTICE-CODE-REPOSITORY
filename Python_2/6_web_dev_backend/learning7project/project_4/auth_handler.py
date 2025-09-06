# auth_handler.py

from config import SECRET_KEY, ALGORITHM
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from starlette.status import HTTP_403_FORBIDDEN
from datetime import datetime, timedelta
from jose import JWTError, jwt, ExpiredSignatureError
from fastapi.security import OAuth2PasswordBearer


oauth2scheme = OAuth2PasswordBearer(tokenUrl="/token")


TOKEN_EXPIRATION = 30


def create_access_token(
        data: dict):
    to_encode = data.copy()
    expiry_time = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRATION)
    to_encode.update({"exp": expiry_time})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return encoded_jwt


def verify_access_token(
  token: str,
):

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload

    except ExpiredSignatureError:
        raise HTTPException(401, detail="Token expired")

    except JWTError:
        raise HTTPException(401, detail="Unauthorized")


class JWTBearer(HTTPBearer):
    """ensures that credentials are valid"""
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)

        if credentials:
            if credentials.scheme != "Bearer":
                raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Invalid Authorization Scheme")

            return verify_access_token(credentials.credentials)

        else:
            raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Invalid authorization code")
