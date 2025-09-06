from fastapi import FastAPI, Header, HTTPException, Depends
from pydantic import BaseModel, Field


def authenticator(api_key: str = Header(...)):
    if api_key != "secret":
        raise HTTPException(401, detail="Invalid API key")


app = FastAPI()

fake_db = {}


class TaskIn(BaseModel):
    task: str = Field(min_length=1, max_length=150)


class TaskOut(BaseModel):
    id: int = Field(ge=1, le=9999)
    task: str = Field(min_length=1, max_length=150)


@app.post("/tasks/{task_id}", response_model=TaskOut, status_code=201, dependencies=[Depends(authenticator)],
          tags=["Tasks"], summary="Add a new task")
def add_task(task_id: int, task: TaskIn) -> TaskOut:
    if task_id in fake_db:
        raise HTTPException(409, detail="Task ID already exist")

    fake_db[task_id] = task

    return TaskOut(id=task_id,
                   task=task.task)


@app.get("/tasks/{task_id}", status_code=200, dependencies=[Depends(authenticator)])
def get_task(task_id: int) -> dict:
    if task_id not in fake_db:
        raise HTTPException(404, detail="Task not found")

    return {"id": task_id,
            "task": fake_db[task_id].task}


@app.delete("/tasks/{task_id}", status_code=200, dependencies=[Depends(authenticator)])
def delete_task(task_id: int) -> dict:
    if task_id not in fake_db:
        raise HTTPException(404, detail="Task not found")

    del fake_db[task_id]

    return {"message": f"Task ID {task_id} deleted"}
