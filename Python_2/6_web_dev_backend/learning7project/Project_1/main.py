from fastapi import FastAPI, Depends, Header, HTTPException
from pydantic import BaseModel, Field
from typing import Annotated


def check_api_key(api_key: str = Header(...)):
    if api_key != "secret":
        raise HTTPException(403, detail="Invalid API key")


app = FastAPI(dependencies=[Depends(check_api_key)])


fake_db = {}


class MakeNote(BaseModel):
    title: str = Field(min_length=1, max_length=50)
    content: str = Field(min_length=1, max_length=500)


@app.post("/notes", status_code=201)
def make_notes(note: MakeNote):
    if note.title in fake_db:
        raise HTTPException(409, detail="Note title already exists")

    fake_db[note.title] = note.content
    return {"message": "-- Note added --"}


@app.get("/notes")
def view_notes():
    return fake_db
