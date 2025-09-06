#auth/hashing.py
from passlib.context import CryptContext


# Purpose:
# (1) Hash a password before storing it in a database
# (2) Verify password and compare it to the hashed one

pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)