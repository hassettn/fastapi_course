# main.py
# course here: https://realpython.com/fastapi-python-web-apis

from fastapi import FastAPI

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
