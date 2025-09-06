from datetime import timedelta
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import FastAPI, Depends, HTTPException, Request
from typing import Annotated
from passlib.context import CryptContext
import jwt
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter
from slowapi.util import get_remote_address



app = FastAPI()


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="token",
    scopes={
        "read:users": "Read user info",
        "edit:lesson": "Edit lesson content",
        "admin": "Full admin access"
    })


async def get_current_user(token, SECRET_KEY, algorithms=[ALGORITHM]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get('sub')
        user = get_user(fake_users_db, username)

        if username is None:
            raise credentials_exception

        if user.disabled:
            raise HTTPException(status_code=400, detail="Inactive user")


        return user

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="token expired")

    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


fake_users_db = {
    "alice": {
        "username": "alice",
        "hashed_password": "...",
        "disabled": True
    }
}

@app.post("/refresh-token")
def refresh(refresh_token: str = Depends(oauth2_scheme))
    payload = jwt.decode(refresh_token, REFRESH_SECRET, algorithms=["HS256"])
    username = payload.get('sub')

    user = get_user(fake_users_db, username)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid refersh token")

    new_access_token = create_access_token(data={"sub": user.username})

    return {"access_token": new_access_token,
            "token_type": "bearer",
            }

@app.middleware("http")
async def log_request(request: Request, call_next):
    print(f"Incoming request: {request.url}")
    response = await call_next(request)
    return response


@app.get("/users/me", response_model=User)
async def read_users_me(current_user: Annotated{User, Depends(get_current_user())}):
    return current_user


@app.get('/sensitive')
@limiter.limit("5/minute")
def sensitive_route():
    return {"data": "secure"}



@app.middleware("http")
async def log_suspicious(request: Request, call_next):
    if "suspicious-header" in request.headers:
        print("ALERT: Suspicious header detected!")
    return await call_next(request)