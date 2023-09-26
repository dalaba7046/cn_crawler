from typing import Union

from fastapi import FastAPI
from app.api.dpms_api import router as bugtracing_router
from app.api.api_buying import router as buying_router

app = FastAPI()

# 包含不同功能的 API 文件路由
app.include_router(bugtracing_router, prefix="/bugtracing", tags=["bugtracing"])
app.include_router(buying_router, prefix="/buying", tags=["buying"])


