from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import SessionLocal
from services.jd.item_crud import *
from schemas.jd_schema import Items
from typing import Any
router = APIRouter()

# #新增item
# @router.post("/add_item", response_model=Items)
# def create_item(sku_id: str, db: Session):
#     """
#     建立一個新的Item記錄
#      Args:
#          sku_id (str): SKU_ID
#          db (Session, optional): 資料庫會話，預設從依賴中取得
#      Returns:
#          dict: 包含創建結果的回應字典
#     """
#     # 檢查是否已存在相同 SKU_ID 的 Item，如果存在則回傳錯誤
#     existing_item = db.query(Items).filter(Items.SKU_ID == sku_id).first()
#     if existing_item:
#         raise HTTPException(
#             status_code=400, detail="Item with this SKU_ID already exists")

#     # 建立新的 Item 記錄
#     # 設定預設的 COLLECT_STATUS 為 'NEW'
#     new_item = Items(SKU_ID=sku_id, COLLECT_STATUS='NEW')
#     db.add(new_item)
#     db.commit()
#     db.refresh(new_item)

#     return {"message": "Item created successfully", "sku_id": new_item.SKU_ID}

#查詢所有SKU
@router.get('/items',response_model=Items)
def get_all_item(db:Session):
    items = get_items(db)
    return items