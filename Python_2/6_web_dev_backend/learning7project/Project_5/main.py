# main.py
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import FastAPI, HTTPException, Depends
from helper import UserData, UserLoginInfo, GiveToken, ArticleInfoIn, ArticleInfoOut
from hashing import hash_password, verify_hashed_password
from auth_handler import create_access_token, verify_access_token
from dependencies import get_current_user

app = FastAPI()

articles_db = {}
fake_user_db = {}


@app.post("/register")
def register_user(user_data: UserData):
    if user_data.username in fake_user_db:
        raise HTTPException(400, "User already exist")

    hashed_password = hash_password(user_data.password)
    fake_user_db[user_data.username] = hashed_password

    articles_db[user_data.username] = []
    return {"message": "User is now registered"}


@app.post("/login", response_model=GiveToken)
def login_user(user_info: OAuth2PasswordRequestForm = Depends()):
    username = user_info.username
    password = user_info.password

    stored_password_hashed = fake_user_db.get(username)

    if not stored_password_hashed:
        raise HTTPException(404, "Username not found")

    if not verify_hashed_password(password, stored_password_hashed):
        raise HTTPException(401, "Wrong username or password")

    token = create_access_token({"sub": username})

    return GiveToken(
        access_token=token,
        token_type="bearer"
    ).dict()


@app.post("/posts")
def create_post(article_no_id: ArticleInfoIn, username: str = Depends(get_current_user)):

    articles = articles_db.setdefault(username, [])

    article_with_id = ArticleInfoOut(
        id=len(articles) + 1,
        posts=article_no_id)

    articles_db[username].append(article_with_id)
    return {"message": "Article is posted",
            "article": article_with_id}


def notes():
    top_topic_errors = """
    1. 
    """

    notes = """
    1. This is still not done. The posts don't get saved into the object. In other words, it won't persist
    Also, it increment it which is good but the posts doesnt store previous posts"""


