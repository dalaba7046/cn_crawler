# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 11:40:32 2023

@author: a2793
"""
from db.client import DatabaseConnector
from sqlalchemy import text
import pandas as pd
import logging
logger = logging.getLogger()


def search_by_sql(table,wheremap=None):
    
    sql = f"""
    select * from {table}
    """

    if wheremap is not None:
        sql = f"""
        {sql} where {wheremap}
        """
    
    
    res_raw = con.execute(text(sql)).all()
    
    
    return res_raw


def search_str_by_pandas(con,table,wheremap=None):
    
    sql = f"""
    select * from {table}
    """

    if wheremap is not None:
        sql = f"""{sql} where {wheremap}
        """
    
    res_raw = pd.read_sql(sql,con)
    
    return res_raw

def insert_data(df,con,table):
    try:
        df.to_sql(table,con,index=False,if_exists='append')
    except Exception as e:
        logger.error(f'{e}')
