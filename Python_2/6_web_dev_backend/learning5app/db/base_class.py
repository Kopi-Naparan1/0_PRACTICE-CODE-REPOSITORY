from sqlalchemy.orm import DeclarativeBase

# ✅ Base class every model will inherit from
# Think of this like the “blueprint” for every table in your database.
class Base(DeclarativeBase):
    pass
