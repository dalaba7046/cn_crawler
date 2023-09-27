# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 11:40:32 2023

@author: a2793
"""
from sqlalchemy.orm import Session
from models.jd_model import *
from sqlalchemy import text
import pandas as pd
import logging
logger = logging.getLogger()


def create_item(db: Session, item_data):
    """
    創建一个新的Item紀錄
    """
    item = Items(**item_data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def get_item(db: Session, sku_id: str):
    """
    根據SKU_ID獲取Item紀錄
    """
    return db.query(Items).filter(Items.SKU_ID == sku_id).first()


def get_items(db: Session):
    """
    獲取所有Item紀錄
    """
    return db.query(Items).all()


def update_item(db: Session, sku_id: str, item_data):
    """
    更新Item的COLLECT_STATUS
    Args:
        db (Session): 連線
        sku_id (str): SKU_ID，用於確定要更新哪個Item
        status (str): 更新後的COLLECT_STATUS，可以是 'SUCCESS', 'NEW', 'ERROR', 'PENDING'
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
        elif status == 'PENDING':
            item.COLLECT_STATUS = 'PENDING'
        else:
            return False  

        db.commit()
        db.refresh(item)
        return True
    return False  


#設計錯誤,需新增欄位
def delete_item(db: Session, sku_id: str):
    """
    使用軟删除方式删除Item紀錄，更新COLLECT_STATUS為'N'
    """
    item = get_item(db, sku_id)
    if item:
        item.IF_COLLECT = 'SUCCESS'  
        db.commit()
        db.refresh(item)
        return item
    return None
