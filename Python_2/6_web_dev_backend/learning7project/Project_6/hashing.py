from passlib.context import CryptContext


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def hash_plain_password(plain_password: str):
    return pwd_context.hash(plain_password)


def verify_plain_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
