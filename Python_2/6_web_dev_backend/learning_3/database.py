# from database.py

# First, import these
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Second, define database URL (the path of your database)
SQLALCHEMY_DATABASE_URL = 'sqlite:///blog.db'

# Third, Create the engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Fourth, Create the session local
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Lastly, the declarative base
Base = declarative_base()
