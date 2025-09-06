from fastapi import FastAPI, Depends
print('Running routes_test.py')

app = FastAPI()

# ✅ Dependency (you’ll inject this into an endpoint)


def get_fake_user():
    return {"username": "student01", "role": "admin"}


@app.get("/")
def read_root():
    return {"message": "Hallo Welcome to routing practice"}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}


@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}


@app.get("/profile")
def read_profile(user: dict = Depends(get_fake_user)):
    return {"user": user}
