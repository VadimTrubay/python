import uvicorn
import redis.asyncio as redis
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from fastapi_limiter import FastAPILimiter
from fastapi.middleware.cors import CORSMiddleware

from contacts.database.db import get_db
from contacts.routes import contacts, auth, users_avatar
from contacts.conf.config import settings

app = FastAPI()

app.include_router(contacts.router, prefix='/api')
app.include_router(auth.router, prefix='/api')
app.include_router(users_avatar.router, prefix='/api')


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    r = await redis.Redis(host=settings.redis_host, port=settings.redis_port, db=0, encoding="utf-8",
                          decode_responses=True)
    await FastAPILimiter.init(r)


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


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, reload=True)