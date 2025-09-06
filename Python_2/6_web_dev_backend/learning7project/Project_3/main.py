from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field


app = FastAPI()


class ArticleIn(BaseModel):
    article: str = Field(min_length=1, max_length=500)


class ArticleOut(BaseModel):
    article_number: int = Field(ge=1, le=9999)
    article: str = Field(min_length=1, max_length=500)


fake_db_articles = {}


def article_number():
    return len(fake_db_articles)


@app.post("/articles/analyze", response_model=ArticleOut, status_code=201)
def send_article(article_in: ArticleIn, article_num: int = Depends(article_number)) -> ArticleOut:
    article_num += 1
    fake_db_articles[article_num] = article_in.article

    return ArticleOut(
        article_number=article_num,
        article=article_in.article,
    )


@app.get("/articles/stats")
def get_article(article_num: int = Depends(counter)):
    return {"Article Published": article_num}
