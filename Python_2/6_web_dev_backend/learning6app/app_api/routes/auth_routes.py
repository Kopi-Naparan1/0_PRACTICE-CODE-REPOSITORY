from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session  # This is my  short-lived database session. Allows me to talk to my DB.
from fastapi.security import OAuth2PasswordRequestForm  # Automatically expects: username + password
from auth.auth_bearer import JWTBearer  # Forces JWT token validation. Blocks unauthenticated access.

# UserCreate is input schema; UserOut hides sensitive info in output
from learning6app.app_api.schemas.user_schema import UserCreate, UserOut 
from learning6app.app_api.models.user_model import User  # The User model. Used for creating users.
from learning6app.app_api.db.database import get_db  # Gets the working/chosen DB
from learning6app.app_api.auth.hashing import Hasher  # A static class that can hash or verify pwd.
from learning6app. app_api.auth.auth_handler import create_access_token, get_current_user  # encode and decodes JWT


router = APIRouter(
    prefix="/auth",  # Think of this as the start of the route.
    tags=["auth"]  # helps grouping in SwaggerUI.
)


# GET /auth/me – Get info of the currently authenticated user (from JWT)
@router.get("/me", response_model=UserOut, dependencies=[Depends(JWTBearer)])
def read_current_user(
    current_user: UserOut = Depends(get_current_user)
):
    return current_user


# auth/register route : user sign-up
@router.post("/register", response_model=UserOut)
def register_user(user: UserCreate,  # create user
                  db: Session = Depends(get_db)):

    # 1 Check if username or email already exist

    # Queries DB: “Is there anyone with this username OR email?”
    existing_user = db.query(User).filter(
        (User.username == user.username) | (User.email == user.email)
    ).first()
    if existing_user:
        raise HTTPException(status_code=400,
                            detail="Username or email already registered.")

    # 2 Hash the password before saving
    hashed_password = Hasher.get_password_hash(user.password)

    # 3 Create new user instance. The password now is hashed.
    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
    )

    # 4 Add to DB and commit
    db.add(new_user)  # stage the user for saving.
    db.commit() # writes something to the DB
    db.refresh(new_user)  # gets auto-generated fields like id, created_at

    return new_user


# auth/login route : for logging in.
@router.post("/login")
def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(), # username and password
        db: Session = Depends(get_db)
):

    # fetch username
    user = db.query(User).filter(User.username == form_data.username).first()

    if not user:
        raise HTTPException(status_code=401,
                            detail="Invalid credentials")

    if not Hasher.verify_password(form_data.password, user.hashed_password): #  match the pwd and hashed pwd
        raise HTTPException(status_code=401, detail="Incorrect password")

    access_token = create_access_token(data={"sub": user.username}) # "sub" = subject (token standard)

    return {
        "access_token": access_token,  # creates access token if pwd is valid.
        "token_type": "bearer"
    }
