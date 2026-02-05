from fastapi import FastAPI, Depends, Request, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import session
import logging
import hashlib

from database import SessionLocal, engine, Base
from models import User
from auth import create_access_token, get_current_user, require_rol

Base.metadata.create_all(bing=engine)

app=FastAPI()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def hash_password(password: str):
    return hashlib.sha256(password.encode()).hexdigest()

def very_password(password: str, hashed: str):
    return hash_password(password) == hashed

# Dependencia de la base de datos

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

@app.middleware("http")

async def auth_middleware(request: Request, call_next):
    logging.info(f"Request a {request.url.path}")
    
    if request.url.path in ["/login", "/docs", "/openapi.json"]:
        return await call_next(request)
    token = request.headers.get("Authorization")
    if not token:
        return JSONResponse(
            status_code= 401, 
            content={"detail": "Token requerido"}
        )
    
    response = await call_next(request)
    return response

@app.on_event("startup")
def startup():
    db = SessionLocal()
    if not db.query(User). first():
        admin = User(
            username = "admin",
            password = hash_password("admin123"),
            role= "admin"
        )
        db.add(admin)
        db.commit()
    db.close()
    