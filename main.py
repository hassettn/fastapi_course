# main.py
# course here: https://realpython.com/fastapi-python-web-apis

from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class my_Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
# defines a structure like this:
"""
{
    "name": "Foo",
    "description": "An optional description",
    "price": 45.2,
    "tax": 3.5
}
"""


my_app = FastAPI()


@my_app.get("/")
# what to do in case of GET
async def root():
    return {"message": "Hello World"}


@my_app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


@my_app.get("/numbers/{number}")
async def read_item(number: int):
    # data parsing and validation as integer
    return {"item_id": number}


@my_app.post("/request/")
async def create_item(request: my_Item):
    return request
