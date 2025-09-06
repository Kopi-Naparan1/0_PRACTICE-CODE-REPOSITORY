# core/security.py

from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from typing import Union, Any
from core.config import get_settings

# ✅ 1. Load global settings like SECRET_KEY, algorithm, token expiration
settings = get_settings()

# ✅ 2. Create password hashing context using bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ✅ 3. Hash a plain-text password
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# ✅ 4. Verify if a plain password matches its hashed version
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# ✅ 5. Create JWT token from data
def create_access_token(subject: Union[str, Any], expires_delta: timedelta = None) -> str:
    # ⏳ Set token expiry time
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    # 👤 Payload includes subject (user id or username), expiry time
    to_encode = {"exp": expire, "sub": str(subject)}

    # 🔐 Encode the payload with the secret key and algorithm
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

# ✅ 6. Decode token & return subject (e.g. user_id or email)
def decode_access_token(token: str) -> Union[str, None]:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload.get("sub")
    except JWTError:
        return None
