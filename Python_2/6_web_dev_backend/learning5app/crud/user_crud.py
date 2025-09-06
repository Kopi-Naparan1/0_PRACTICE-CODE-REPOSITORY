from sqlalchemy.orm import Session
from models.user_model import User
from schemas.user_schema import UserCreate
from utils.hashing import Hasher

# Create a new user
def create_user(db: Session, user: UserCreate):
    hashed_password = Hasher.get_password_hash(user.password)  # Hash the password
    db_user = User(email=user.email, password=hashed_password)  # Create user instance
    db.add(db_user)  # Add to session
    db.commit()  # Commit transaction
    db.refresh(db_user)  # Refresh to get ID and other DB-generated fields
    return db_user

# Get a user by email
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

# Get user by ID
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()
