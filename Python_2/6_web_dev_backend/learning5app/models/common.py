# models/common.py

from sqlalchemy import Column, DateTime, Boolean
from datetime import datetime

# A base class you can inherit in other models
class TimestampMixin:
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class SoftDeleteMixin:
    is_deleted = Column(Boolean, default=False)
