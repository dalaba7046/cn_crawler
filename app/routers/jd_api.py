from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from config.database import SessionLocal
from services.jd.item_crud import *
from schemas import jd_schema
from typing import Any

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
@router.post("/add_item/", response_model=jd_schema.ItemsBase, status_code=status.HTTP_201_CREATED)
def create_item(item_id: str,site_id: str, db: Session = Depends(get_db)):
#     """
#     建立一個新的Item記錄
#      Args:
#          sku_id (str): SKU_ID
#          db (Session, optional): 資料庫會話，預設從依賴中取得
#      Returns:
#          dict: 包含創建結果的回應字典
#     """
#     # 檢查是否已存在相同 SKU_ID 的 Item，如果存在則回傳錯誤
    existing_item = db.query(jd_schema.ItemsBase).filter(jd_schema.ItemsBase.SKU_ID == item_id).first()
    if existing_item:
        raise HTTPException(
            status_code=400, detail="Item with this SKU_ID already exists")
    create_item(db,item_id,site_id)
    
    