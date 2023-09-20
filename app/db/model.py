# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 16:26:41 2023

@author: a2793
"""
from sqlalchemy import Date,VARCHAR, Column, Integer, String, DateTime, Text, Index
from db.client import DatabaseConnector
Base = DatabaseConnector().Base

class Rating(Base):
    __tablename__='cn_rating_raw_4_imp'
    RAW_ID = Column(Integer,nullable=False,primary_key=True)
    PRODUCT_SIN = Column(VARCHAR(100),nullable=False)
    goodRateShow = Column(VARCHAR(100),nullable=True)
    score1Count = Column(VARCHAR(100),nullable=True)
    score2Count = Column(VARCHAR(100),nullable=True)
    score3Count = Column(VARCHAR(100),nullable=True)
    score4Count = Column(VARCHAR(100),nullable=True)
    score5Count = Column(VARCHAR(100),nullable=True)
    SCRAPY_DT_STR = Column(VARCHAR(30),nullable=False)
    SITE_ID = Column(VARCHAR(100),nullable=False)
    # BRAND_NAME
    def __str__(self):
        return f"object:<SITE_NAME: {self.SITE_NAME} PRODUCT_SIN: {self.PRODUCT_SIN}> "


class Review(Base):
    __tablename__='cn_review_raw_4_imp'
    PRODUCT_SIN = Column(VARCHAR(256),nullable=False)
    SITE_REVIEW_ID = Column(VARCHAR(1024),nullable=False)
    SITE_REVIEW_URL = Column(VARCHAR(1024),nullable=False)
    SITE_REVIEW_DATE_STR = Column(VARCHAR(30),nullable=False)
    SITE_REVIEW_TITLE = Column(VARCHAR(1024),nullable=False)
    SITE_REVIEW_MESSAGE_HTML = Column(Text,nullable=False)
    SITE_REVIEW_MESSAGE = Column(Text,nullable=False)
    SITE_REVIEW_RATING = Column(VARCHAR(10),nullable=False)
    SCRAPY_DT_STR = Column(VARCHAR(30),nullable=False)
    USER_NAME = Column(VARCHAR(30),nullable=False)
    RATING = Column(VARCHAR(30),nullable=False)
    REVIEW_DATE = Column(VARCHAR(30),nullable=False)
    AFTER_REVIEW_MESSAGE = Column(Text,nullable=False)
    
    
    def __str__(self):
        return f"Review Object:<PRODUCT_SIN: {self.PRODUCT_SIN} SITE_REVIEW_ID: {self.SITE_REVIEW_ID}>"


class Items(Base):
    __tablename__='df_sku_list'
    pass