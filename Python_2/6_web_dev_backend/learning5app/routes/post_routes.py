# routes/post_routes.py

from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from app.schemas.post_schema import PostRequest, PostResponse
from app.models.post_model import posts_db  # This is a fake in-memory database
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import decode_access_token

router = APIRouter(
    prefix="/posts",
    tags=["Posts"],
    dependencies=[Depends(JWTBearer())]  # ✅ All routes require a valid token
)

# Simulated auto-incrementing ID
post_id_counter = len(posts_db) + 1


@router.post("/", response_model=PostResponse, status_code=201)
def create_post(post: PostRequest):
    """
    📝 Create a new post
    Requires valid JWT token (handled by JWTBearer).
    """
    global post_id_counter
    new_post = {
        "id": post_id_counter,
        "title": post.title,
        "content": post.content,
        "author": post.author
    }
    posts_db.append(new_post)
    post_id_counter += 1
    return new_post


@router.get("/", response_model=List[PostResponse])
def get_all_posts():
    """
    🔍 Get all posts.
    """
    return posts_db


@router.get("/{post_id}", response_model=PostResponse)
def get_post(post_id: int):
    """
    🔍 Get a specific post by ID.
    """
    for post in posts_db:
        if post["id"] == post_id:
            return post
    raise HTTPException(status_code=404, detail="Post not found")


@router.delete("/{post_id}", status_code=204)
def delete_post(post_id: int):
    """
    ❌ Delete a post by ID.
    """
    for i, post in enumerate(posts_db):
        if post["id"] == post_id:
            posts_db.pop(i)
            return
    raise HTTPException(status_code=404, detail="Post not found")
