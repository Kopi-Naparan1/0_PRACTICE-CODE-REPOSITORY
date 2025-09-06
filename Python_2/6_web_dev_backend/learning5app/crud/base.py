from sqlalchemy.orm import Session
from typing import Type, TypeVar, Generic, List
from models.base_model import Base  # Assuming you have a shared base
from pydantic import BaseModel

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)

# Generic base class for CRUD operations
class CRUDBase(Generic[ModelType, CreateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self, db: Session, id: int) -> ModelType:
        return db.query(self.model).filter(self.model.id == id).first()

    def get_all(self, db: Session) -> List[ModelType]:
        return db.query(self.model).all()

    def create(self, db: Session, obj_in: CreateSchemaType) -> ModelType:
        obj_data = obj_in.dict()
        db_obj = self.model(**obj_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, id: int) -> None:
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
