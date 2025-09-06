#auth/utils.py

from jose import jwt, JWTError
from datetime import datetime

# Purpose:
# (1) Check whether a JWT token is already expired — without raising an error.
# (2)  Pull out the "sub" field from a token (often the user email or ID).


def is_token_expired(token: str,
                     secret: str,
                     algorithm:str = "HS256") -> bool:
    """Returns True if the token is expired or invalid; False otherwise."""

    try:
        payload = jwt.decode(token, secret, algorithms=[algorithm])
        exp = payload.get("exp")

        if exp:
            return datetime.utcfromtimestamp(exp) < datetime.utcnow()
        return True
    except JWTError:
        return True


def get_token_subject(token: str,
                      secret: str,
                      algorithm: str = "HS256",) -> str | None:
    try:
        payload = jwt.decode(token, secret, algorithms=[algorithm])
        return payload.get("sub")
    except JWTError:
        return None



