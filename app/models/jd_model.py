# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 16:26:41 2023

@author: a2793
"""
from sqlalchemy import Date,VARCHAR, Column, Integer, String, DateTime, Text, Index
from db.database import Base
from datetime import datetime

class Rating(Base):
    __tablename__='cn_rating_raw_4_imp'
    RAW_ID = Column(Integer,nullable=False,primary_key=True)
    PRODUCT_SIN = Column(VARCHAR(100),nullable=False)
    goodRateShow = Column(VARCHAR(100))
    score1Count = Column(VARCHAR(100))
    score2Count = Column(VARCHAR(100))
    score3Count = Column(VARCHAR(100))
    score4Count = Column(VARCHAR(100))
    score5Count = Column(VARCHAR(100))
    SCRAPY_DT_STR = Column(VARCHAR(30),nullable=False)
    SITE_ID = Column(VARCHAR(100),nullable=False)
    # BRAND_NAME
    def __str__(self):
        return f"object:<SITE_NAME: {self.SITE_NAME} PRODUCT_SIN: {self.PRODUCT_SIN}> "


class Review(Base):
    __tablename__='cn_review_raw_4_imp'
    PRODUCT_SIN = Column(VARCHAR(256))
    SITE_REVIEW_ID = Column(VARCHAR(1024), nullable=False)
    SITE_REVIEW_URL = Column(VARCHAR(1024))
    SITE_REVIEW_DATE_STR = Column(VARCHAR(30))
    SITE_REVIEW_TITLE = Column(VARCHAR(1024))
    SITE_REVIEW_MESSAGE_HTML = Column(Text)
    SITE_REVIEW_MESSAGE = Column(Text)
    SITE_REVIEW_RATING = Column(VARCHAR(10))
    SCRAPY_DT_STR = Column(VARCHAR(30))
    USER_NAME = Column(VARCHAR(30))
    RATING = Column(VARCHAR(30))
    REVIEW_DATE = Column(DateTime, default=datetime.utcnow)
    AFTER_REVIEW_MESSAGE = Column(Text)
    
    
    def __str__(self):
        return f"Review Object:<PRODUCT_SIN: {self.PRODUCT_SIN} SITE_REVIEW_ID: {self.SITE_REVIEW_ID}>"


class Items(Base):
    __tablename__='df_sku_list'
    SKU_ID = Column(VARCHAR(100))
    SITE_ID = Column(VARCHAR(100))
    COLLECT_STATUS = Column(VARCHAR(100))

    def __str__(self):
        return f"Item Object:<SKU_ID: {self.SKU_ID} SITE_ID: {self.SITE_ID}>"


class ReviewId(Base):
    SITE_ID = Column(VARCHAR(100))
    SITE_REVIEW_ID = Column(VARCHAR(100))
    IMPORT_DATE = Column(DateTime, default=datetime.utcnow,
                         onupdate=datetime.utcnow)

    def __str__(self):
        return f"ReviewId Object:<SITE_REVIEW_ID: {self.SITE_REVIEW_ID} SITE_ID: {self.SITE_ID}>"
