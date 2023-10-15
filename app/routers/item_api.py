from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.config.database import SessionLocal
from app.services.jd.item_crud import *
from app.schemas import jd_schema
from typing import Any
from fastapi.responses import JSONResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#查詢所有SKU
@router.get('/items', response_model=list[jd_schema.ItemsBase], status_code=status.HTTP_200_OK)
def get_all_item( db: Session = Depends(get_db)):
    items = get_items(db)
    return items

#查詢SKU
@router.get('/item/{item_id}',response_model=jd_schema.ItemsBase, status_code=status.HTTP_200_OK,response_model_exclude_unset=True)
def get_item_review(item_id:str,db: Session = Depends(get_db)):
    item = get_item(db,item_id)
    return item
    
#新增item
@router.post("/item", response_model=dict, status_code=status.HTTP_201_CREATED)
def create_new_item(item_data: ItemCreate, db: Session = Depends(get_db)):
    return create_item(db, item_data)

#刪除item
@router.put("/item/{item_id}", status_code=status.HTTP_200_OK)
def delete(item_id:str,db: Session = Depends(get_db)):
    return delete_item(db, item_id)
