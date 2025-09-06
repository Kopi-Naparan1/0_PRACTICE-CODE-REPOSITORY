from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from learning5app.routes import user_routes, auth_routes, post_routes
from learning5app.db.database import create_db_and_tables

app = FastAPI()

# Optional: Connect DB
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Middleware: Allow frontend apps to connect
learning5app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Later, restrict to your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
learning5app.include_router(auth_routes.router)
learning5app.include_router(user_routes.router)
learning5app.include_router(post_routes.router)

