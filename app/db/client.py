# -*- coding: utf-8 -*-
"""
Created on Wed May 18 18:34:54 2022

@author: Johnny.Liu
"""

import configparser
import os
import logging
from sqlalchemy import types, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from sqlalchemy.ext.declarative import declarative_base
logger = logging.getLogger()

# DB連線class    
class DatabaseConnector:
    def __init__(self, env):
        path_root = f"{os.getcwd().split('src')[0]}\\cfg"
        path_db = f'{path_root}\database.cfg'
        self.config = configparser.ConfigParser()
        self.config.read(path_db)

        if env not in self.config:
            raise ValueError(f"Invalid environment '{env}'")

        self.db_user = self.config[env]['MYSQL_DATA_USER']
        self.db_password = self.config[env]['MYSQL_DATA_PASSWORD']
        self.db_host = self.config[env]['MYSQL_DATA_HOST']
        self.db_port = self.config[env]['MYSQL_DATA_PORT']
        self.db_database = self.config[env]['MYSQL_DATA_DATABASE']

        self.engine = create_engine(f"mysql+pymysql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_database}")
        self.Session = sessionmaker(bind=self.engine)
        self.Base = declarative_base()
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        
    def connect(self):
        try:
            # session = self.Session()
            return self.engine.connect()
        except Exception as e:
            logger.error(f"Error connecting to the database: {e}")
            return None
    def close_connection(self):
        try:
            if self.engine.connect().close():
                self.engine.connect().close()
        except Exception as e:
            logger.error(f"Error closing the database connection: {e}")
            
            
            
if __name__ == "__main__":
    env='DEV'
    db_connector = DatabaseConnector(env)
    con = db_connector.connect()
    con.execute(text('select * from def_sku_list')).all()
    con.close()
