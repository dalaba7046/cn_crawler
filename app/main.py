from typing import Union
from fastapi import FastAPI
from app.routers.item_api import router as item_router


app = FastAPI()

@app.get('/')
def root():
    return {"message": "Hello World"}

# 包含不同功能的 API 文件路由
app.include_router(item_router, prefix="/v1/item", tags=["jd_item"])



