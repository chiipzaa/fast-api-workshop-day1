from datetime import timedelta, datetime
from typing import Optional

from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer

from jose import JWTError, jwt
from decople import config


SECRET_KEY = config("SECRET_KEY")
ALGORITHM = config("ALGORITHM")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_token(data:dict, expire_delta: Optional[timedelta]=None):
    to_encode = data.copy
    expire = generate_expire_date(expire_delta)

def generate_expire_date(expire_delta:Optional[timedelta]=None):
    if expire_delta:
        expire = datetime.utcnow()+expire_delta
    else:
        expire = datetime.utcnow()+timedelta(days=1)