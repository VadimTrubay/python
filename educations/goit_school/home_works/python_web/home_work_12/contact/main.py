from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text

from contacts.database.db import get_db
from contacts.routes import contacts, auth

app = FastAPI()

app.include_router(contacts.router, prefix='/api')
app.include_router(auth.router, prefix='/api')


@app.get("/")
def read_root():
    return {"message": "My contacts book"}


@app.get("/api/healthchecker")
def healthchecker(db: Session = Depends(get_db)):
    try:
        result = db.execute(text("SELECT")).fetchone()
        if result is None:
            raise HTTPException(status_code=500, detail="Database is not configured correctly")
        return {"message": "Welcome to FastAPI!"}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, detail="Error connecting to the database")
    