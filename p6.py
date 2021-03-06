from typing import Optional

from fastapi import FastAPI, Request

from pydantic import BaseModel
from 


app = FastAPI()



class Item(BaseModel):

    name: str

    price: float

    is_offer: Optional[bool] = None



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int,item_price: int, q: Optional[str] = None, flavour: Optional[str] = None):
    return {"item_id": item_id, "item_price":item_price, "q": q, "flavour":flavour,}



@app.put("/items/{item_id}")

def update_item(item_id: int, item: Item):

    return {"item_name": item.name, "item_id": item_id}

@app.post("/item")
async def create_item(item: Item):
    return { "item_name":item_name }

@app.delete("/item")
def delete_item(item_id: int):
    return item
