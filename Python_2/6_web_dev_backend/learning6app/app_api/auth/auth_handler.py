from datetime import datetime, timedelta  # timedelta lets me add/sub time.
from jose import JWTError, jwt  # jwt has .encode and .decode: it handles the token.
# JWTError will do something if the token is not valid.


from fastapi import Depends, HTTPException, status

# OA2PB looks for the "Authorization: Bearer <token>". extracts it automatically.
from fastapi.security import OAuth2PasswordBearer

# "User" is the sqlalchemy model
from learning6app.app_api.models.user_model import User

# "Session" handles the DB transaction.
from sqlalchemy.orm import Session

# "get_db" injects the current database into the function
from learning6app.app_api.db.database import get_db


# tokenUrl is the endpoint (You can depend on this to get the token)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


# Define secret and algorithm
SECRET_KEY = "your-secret-key"  # Used to sign JWT tokens
ALGORITHM = "HS256"  # determines how the token is signed
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # how long the token should last


def create_access_token(data: dict,  # contains key value pair (dict)
                        expires_delta: timedelta = None):  # this lets me customize the expiry date of the token

    to_encode = data.copy()  # copy the input data to avoid unnecessary changes in the original dict.
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))  # Default will be to add 15 minutes if empty
    to_encode.update({"exp": expire})  # Needed to update the expiry "exp"  in the dict
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)  # This encodes the token using the 3 needed.
    return encode_jwt  # function gets called, it will return a token. Just needs data and optionally expiry date


# takes a token and exception to raise incase something is wrong.
def verify_token(token: str,  # the token that was sent
                 credentials_exception):

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])  # if the token is invalid/expired -> JWTError

        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception

        return username

    except JWTError:  # Its main job is to raise error when the JWT is invalid.
        raise credentials_exception


def get_current_user(
        token: str = Depends(oauth2_scheme),  # token is the encoded data sent to the `create_access_token`
        db: Session = Depends(get_db)  # any database passed into the getdb will be used.
):

    # If the token is invalid, this will be raised
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )

    # This will get the username if the token is valid. If not, then the credentials_exception will show
    username = verify_token(token, credentials_exception)

    user = db.query(User).filter(User.username == username).first()  # In here, you will make a user using the modle
    # db.query(User) start a database query on the User model
    # .filter to username) a condition; to include User.username == username
    # ".first" returns first result.

    # If user is none, raise the credential exception. If user is not empty, return the user
    if user is None:
        raise credentials_exception
    return user


