from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from sqlalchemy import text
import uvicorn


app = FastAPI()

# staticfiles = StaticFiles(directory="static/css")
# app.mount("/static", staticfiles, name="static")
# templates = Jinja2Templates(directory="templates")


# @app.get("/", response_class=HTMLResponse)
# async def index(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request, "title": "Kaustubh Demo", "body_content": "This is the demo for using FastAPI with Jinja templates"})


@app.get("/")
async def index():
    return {"message": "Wellcome index"}


@app.get("/products")
async def products():
    return {"message": "Wellcome products"}


@app.get("/product/{product_id}")
async def get_product(product_id: int):
    return {"message": product_id}


# if __name__ == '__main__':
#     uvicorn.run('main:app', host=localhost, port=5000, reload=True)
