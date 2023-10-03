# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 11:40:32 2023

@author: a2793
"""
from sqlalchemy.orm import Session
from models.jd_model import Items
from schemas.jd_schema import ItemCreate
import logging
from fastapi import HTTPException
logger = logging.getLogger()


def create_item(db: Session, item_data: ItemCreate):
    """
    建立一個新的Item記錄
      Args:
          sku_id (str): SKU_ID
          site_id (str): SITE_ID
          db (Session, optional): 資料庫會話，預設從依賴中取得
      Returns:
          dict: 包含創建結果的回應字典
    """
    existing_item = db.query(Items).filter(
        Items.SKU_ID == item_data.SKU_ID).first()
    if existing_item:
        raise HTTPException(status_code=400, detail="SKU_ID already exists")

    # 建立新的 Item 記錄
    new_item = Items(**item_data.dict())
    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
        return {"message": "Item created successfully", "sku_id": new_item.SKU_ID}
    except Exception as e:
        db.rollback()  # 回滚事务以避免数据损坏
        logger.error(f'{e}')
        raise HTTPException(status_code=500, detail="Internal Server Error")



def get_item(db: Session, sku_id: str):
    """
    根據SKU_ID獲取Item紀錄
    """
    item = db.query(Items).filter(Items.SKU_ID == sku_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


def get_items(db: Session):
    return db.query(Items).all()


def update_item(db: Session, sku_id: str, status):
    """
    更新Item的COLLECT_STATUS
    Args:
        db (Session): 連線
        sku_id (str): SKU_ID，用於確定要更新哪個Item
        status (str): 更新後的IF_COLLECT，可以是 'SUCCESS', 'NEW', 'ERROR', 'PENDING'
    Returns:
        bool: 如果成功更新返回True，否則返回False
    """
    item = db.query(Items).filter(Items.SKU_ID == sku_id).first()
    if item:
        # 根据不同的逻辑设置COLLECT_STATUS
        if status == 'SUCCESS':
            item.COLLECT_STATUS = 'SUCCESS'
        elif status == 'NEW':
            item.COLLECT_STATUS = 'NEW'
        elif status == 'ERROR':
            item.COLLECT_STATUS = 'ERROR'
        elif status == 'GOING':
            item.COLLECT_STATUS = 'GOING'
        elif status == 'PENDING':
            item.COLLECT_STATUS = 'PENDING'
        else:
            return False  

        db.commit()
        db.refresh(item)
        return True
    return False  


def delete_item(db: Session, sku_id: str):
    """
    使用軟删除方式删除Item紀錄，更新COLLECT_STATUS為'N'
    """
    item = db.query(Items).filter(Items.SKU_ID == sku_id).first()
    if item.IF_COLLECT=='Y':

        item.IF_COLLECT = 'N'
        db.commit()
        return {"message": "Item marked as deleted", "sku_id": sku_id}
    else:

        raise HTTPException(status_code=404, detail=f"Item with SKU_ID {sku_id} not found")
