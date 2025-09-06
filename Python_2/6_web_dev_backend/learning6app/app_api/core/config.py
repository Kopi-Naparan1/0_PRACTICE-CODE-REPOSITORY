import os  # A module that helps me interact with the operating system


SECRET_KEY = os.getenv("SECRET_KEY")  # Look for a value "SECRET_KEY", assign it to SECRET_KEY
ALGORITHM = os.getenv("ALGORITHM") # Look for a value "ALGORITHM", assign it to ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))  # Fallback to 30 if missing
DATABASE_URL = os.getenv("DATABASE_URL")
