from sqlalchemy.orm import Session
from models.token_model import Token
from schemas.token_schema import TokenCreate

# Save token to DB (optional — only if you're tracking or blacklisting tokens)
def store_token(db: Session, token_data: TokenCreate):
    db_token = Token(**token_data.dict())  # Convert schema to model
    db.add(db_token)
    db.commit()
    db.refresh(db_token)
    return db_token

# Retrieve token (e.g., for blacklisting check)
def get_token(db: Session, token_str: str):
    return db.query(Token).filter(Token.token == token_str).first()
