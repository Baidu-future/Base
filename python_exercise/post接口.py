# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2019/11/12 21:27
# @author  : Mo
# @function: post service of fastapi
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    a: int = 12
    b: int = 23


@app.post('/test')
def calculate(request_data: Item):
    a = request_data.a
    b = request_data.b
    c = a + b
    res = {"res": c}
    return res


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app=app,
                host="192.168.0.12",
                port=8082,
                workers=1)