# 📦 SQLAlchemy essentials
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ✅ 1. DB URL (connection string) — this tells SQLAlchemy where the DB is
# Example: SQLite for local dev, PostgreSQL for production
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # ← using local SQLite file
# For PostgreSQL: "postgresql://user:password@localhost/dbname"

# ✅ 2. Create the database engine
# This is like "connecting the gas line" to your stove
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # SQLite-specific requirement
)

# ✅ 3. Create a session factory
# Think of this like a "kitchen workspace" where one chef (user) prepares data
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ✅ 4. Base class all models will inherit from
# Think of this as the "DNA" that every dish in your restaurant shares
Base = declarative_base()
