from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from users import users_db
from errores import error_401


security = HTTPBearer()

def get_current_users(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token  not in users_db:
        