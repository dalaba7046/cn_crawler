from typing import Union

from fastapi import FastAPI
from db.client import DatabaseConnector
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/v1/items/")
def read_items(item_id: int, q: Union[str, None] = None):
    
    
    return {"item_id": item_id, "q": q}
