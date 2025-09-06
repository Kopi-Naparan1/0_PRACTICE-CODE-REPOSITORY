from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


print('Running first_api.py')

app = FastAPI()


# the @app_api is called "path decoration operation"
@app.get('/blog')  # Base Url "/" called as "path"| .get called as "operations"
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):  # Called as "path operation function"
    if published:
        return {"data": f'{limit} published blogs from database'}
    else:
        return {"data": f'{limit} blogs from database'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'unpublished_blog'}


@app.get('/blog/{blog_id}')
def about(blog_id: int):
    return {'data': blog_id}


@app.get('/blog/{blog_id}/comments')
def comments(blog_id, limit=10):
    return {"data": {'1', '2'},
            "data_limit": {limit},
            "blog_id": {blog_id}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(blog: Blog):
    return {"data": f"Blog [{blog.title}] is created Body of [{blog.body}]",}


