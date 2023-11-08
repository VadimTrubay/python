from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
import uvicorn



app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Wellcome index"}


@app.get("/products")
async def products():
    return {"message": "Wellcome products"}


@app.get("/product/{product_id}")
async def get_product(product_id: int):
    return {"message": product_id}


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, reload=True)
