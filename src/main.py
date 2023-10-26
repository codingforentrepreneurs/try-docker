import os # python-decouple
from typing import Union

from fastapi import FastAPI
# gunicorn src.main:app --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000

app = FastAPI()


@app.get("/")
def read_root():
    my_pw = os.environ.get("MY_PW")
    return {"Hello": "World", "my_pw": my_pw}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
