from fastapi import FastAPI  # Imports the main class to create the FastAPI app.
from learning6app.app_api.routes import auth_routes, admin_routes  # Imports the router that handles authentication routes like /login, /register.

# Base: the declarative base class used by SQLAlchemy to define models
# engine: the connection to your actual database (SQLite, PostgreSQL, etc.)
from learning6app.app_api.db.database import Base, engine

# Imports the tool to define how your app will extract tokens from requests.
from fastapi.security import OAuth2PasswordBearer


# Take all the models defined using Base, and create the corresponding tables in the database.
# Create DB tables on startup
# This will only create missing tables. It won’t update existing ones — for that, you use migrations (Alembic)
Base.metadata.create_all(bind=engine)

app = FastAPI()


# Adds all endpoints from auth_routes into the main app.
app.include_router(auth_routes.router,
                   prefix="/auth",
                   tags=["Authentication"])


# for admin routes.
app.include_router(admin_routes.router)
