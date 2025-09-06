from sqlalchemy.orm import Session
from models.item_model import Item
from schemas.item_schema import ItemCreate, ItemUpdate

# Create a new item
def create_item(db: Session, item: ItemCreate, owner_id: int):
    db_item = Item(**item.dict(), owner_id=owner_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Get items belonging to a user
def get_items_by_owner(db: Session, owner_id: int):
    return db.query(Item).filter(Item.owner_id == owner_id).all()

# Get single item by ID
def get_item(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()

# Update an item
def update_item(db: Session, item_id: int, item: ItemUpdate):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item:
        for field, value in item.dict(exclude_unset=True).items():
            setattr(db_item, field, value)
        db.commit()
        db.refresh(db_item)
    return db_item

# Delete an item
def delete_item(db: Session, item_id: int):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item
