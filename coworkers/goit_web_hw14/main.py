import uvicorn
import redis.asyncio as redis

from fastapi import FastAPI, Depends, HTTPException
from fastapi_limiter import FastAPILimiter
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import text

from goit_web_hw13.database.db import get_db
from goit_web_hw13.routes import users, auth, users_avatar
from goit_web_hw13.conf.config import settings

app = FastAPI()

app.include_router(auth.router, prefix='/api')
app.include_router(users_avatar.router, prefix='/api')
app.include_router(users.router, prefix='/api')


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup() -> None:
    """
    connection of the Redis database
    """
    r = await redis.Redis(host=settings.redis_host, port=settings.redis_port, db=0, encoding="utf-8",
                          decode_responses=True)
    await FastAPILimiter.init(r)


@app.get("/")
def read_root() -> dict:
    """
    Creates the '/' root route and return message "This is Adressbook"

    :param: without parameters
    :return: The returns message: "This is Adressbook"
    """
    return {"message": "This is Adressbook"}


@app.get("/api/healthchecker")
def healthchecker(db: Session = Depends(get_db)) -> dict:
    """
    Creates the '/api/healthchecker' route to check the health 
    of the database.
    The healthchecker function receives a session with the 
    database using the installed Depends(get_db) dependency, 
    executes the 'SELECT 1' query, and processes the result. 
    If the result is not found, an exception is thrown with 
    code 500 and the message "Database is not configured correctly". 
    If an error occurs during the query, an exception is thrown 
    with code 500 and the message "Error connecting to the database"

    :param db: The database session.
    :type db: Session
    :return: The returns message: "Welcome to FastAPI!",
        if the connection to the database is established,
        or an exception otherwise is thrown with code 500
        and relevant message
    :rtype: str | HTTPException
    """
    try:
        # Make request
        result = db.execute(text("SELECT 1")).fetchone()
        if result is None:
            raise HTTPException(status_code=500, detail="Database is not configured correctly")
        return {"message": "Welcome to FastAPI!"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error connecting to the database")
    
if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, reload=True)
    