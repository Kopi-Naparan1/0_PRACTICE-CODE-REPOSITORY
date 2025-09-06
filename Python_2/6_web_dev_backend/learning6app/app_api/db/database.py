from sqlalchemy.ext.declarative import declarative_base  # declarative_base is a factory that returns base class
from sqlalchemy import create_engine  # create_engine sets up connection to the database (prepares only)
from sqlalchemy.orm import sessionmaker  # class factory that build `Session` objects

# Tells SQLAlchemy where my database is. This one uses lightweight db stored locally.
DATABASE_URL = "sqlite:///.auth_app.db"  # Great for testing.

# creates the actual engine or DB connector
# SQLite is not thread-safe, we bypass that through connect args
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Prepares session factory
# *commit changes manually *delay updates until needed *bind= connects to our engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# For creating models
Base = declarative_base()


# Creates db session everytime called, yield it to the caller, close it automatically
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
