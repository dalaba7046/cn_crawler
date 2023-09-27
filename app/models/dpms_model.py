from sqlalchemy import Date,VARCHAR, Column, Integer, String, DateTime, Text, Index
from config.database import Base
from datetime import datetime


class Task(Base):
    __tablename__ = 'task'
    
    TASK_ID = Column(VARCHAR(100), nullable=False, primary_key=True)
    SKU_NUM = Column(VARCHAR(100))
    HOST_NAME = Column(VARCHAR(100))
    JOB_ID = Column(VARCHAR(100))
    TASK_ITEM_COUNT = Column(VARCHAR(100))
    TASK_STATUS = Column(VARCHAR(100))
    TASK_START = Column(DateTime)
    CREATE_USER = Column(VARCHAR(100))
    CREATE_DATE = Column(DateTime, default=datetime.utcnow)
    UPDATE_USER = Column(VARCHAR(100))
    UPDATE_DATE = Column(DateTime, default=datetime.utcnow,
                         onupdate=datetime.utcnow)

class Item(Base):
    __tablename__ = "task_item"  

    ITEM_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    TASK_ID = Column(Integer, index=True)
    REF_ID = Column(Integer, index=True)
    ITEM_STATUS = Column(String)
    ITEM_START = Column(DateTime)
    CREATE_USER = Column(String)
    CREATE_DATE = Column(DateTime, default=datetime.utcnow)
    UPDATE_USER = Column(String)
    UPDATE_DATE = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    
class Log(Base):
    __table__name = "api_log_in"
    ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    FROM_IP = Column(String)
    ENDPOINT_URL = Column(String)
    METHOD_TYPE = Column(String)
    RESP = Column(VARCHAR(100))
    ERROR_MSG = Column(String)
    CREATE_DATE = Column(DateTime, default=datetime.utcnow)
