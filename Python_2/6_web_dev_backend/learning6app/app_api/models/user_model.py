
# Importing data types and column constructor.
from sqlalchemy import Column, String, Boolean, Integer

# The `Base` is the model from DB. Used for creating models.
from learning6app.app_api.db.database import Base


# Class User - like a form template -> Makes a user
class User(Base):
    # The tablename is the name of the table. It is like a tag for the table.
    __tablename__ = 'users'

    # A unique ID to identify each row. `primary_key` main identifier. `index` speed up lookups.
    # Ex: id = 1 -> first user
    #     id = 2 -> second user
    id = Column(Integer, primary_key=True, index=True)

    # `unique` No two users can have the same email.
    # `nullable` required to be filled or not. # If False = required. If True = Optional
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=True)

    # Used for authorization
    role = Column(String, default='users')  # user/admin

    # Flag a user -> True = active , False = Deactivated or Banned
    is_active = Column(Boolean, default=True)
