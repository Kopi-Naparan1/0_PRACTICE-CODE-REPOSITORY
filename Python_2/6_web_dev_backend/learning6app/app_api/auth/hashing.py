from passlib.context import CryptContext  # CryptContext define how the password should be hashed and verified.

# schemes: the argument will be the hashing algorithm.
# deprecated: this will warn me incase the hash is old and needs rehashing.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hasher:

    # static method allows calling the method directly via Hasher.method_name() without instantiation
    @staticmethod  # call the method without creating an object of hasher.
    def get_password_hash(password: str) -> str:  # Input: a raw password str ->  hashed ver (bcrypt).
        return pwd_context.hash(password)  # This is where hashing happens

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:

        # checks if the plain pwd matches with the stored pwd in db
        return pwd_context.verify(plain_password, hashed_password)
