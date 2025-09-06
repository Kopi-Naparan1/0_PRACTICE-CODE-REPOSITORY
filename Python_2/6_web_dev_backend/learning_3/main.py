# from main.py


from fastapi import FastAPI, Depends
from schemas import Blog
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()


@app.post('/blog')
def create(request: Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog
