# from typing import Union

# from fastapi import FastAPI

# #pydentic is inbulit in fastapi to validate the data
# from pydantic import BaseModel
# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int , q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

# @app.put("/items/{item_id}")
# def update_item(item_id: int , item: Item):
#     return {"item_name": item.name, "item_id": item_id}

# @app.post("/items/")
# def create_item(item: Item):
#     return item

import uvicorn
from decouple import config

PORT= config("PORT")

if __name__ == "__main__":
    uvicorn.run("server.app:app", host="0.0.0.0", port=PORT, reload=True)