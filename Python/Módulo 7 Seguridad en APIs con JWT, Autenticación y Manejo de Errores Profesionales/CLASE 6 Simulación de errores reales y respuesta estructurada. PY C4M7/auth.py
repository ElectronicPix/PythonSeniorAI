# python -m pip install fastapi uvicorn python-jose sqlalchemy passlib[bcrypt]


# Instalación de dependencias: python -m pip install fastapi uvicorn python-jose sqlalchemy passlib[bcrypt]


from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


SECRET_KEY = "SECRET123"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

security = HTTPBearer()

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=401, 
            detail= "Token inválido o expirado"
        )

def get_current_user(
    credemtials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credemtials.credentials
    return verify_token(token)

def require_rol(role: str):
    def role_check(user=Depends(get_current_user)):
        if user.get("role") != role:
            raise HTTPException(
                status_code=403,
                detail="Acceso denegado para este rol"
            )
        return user
    return role_check