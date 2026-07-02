import bcrypt
from datetime import datetime,timedelta
from jose import jwt,JWTError


SECRET_KEY="SMART SCHOOL MANAGEMENT"
ALGORITHM="HS256"
EXPIRE_ACCESS_TOKEN=30

class Hash():
    @staticmethod
    def password_hashing(password):
        pass_byte=password.encode("utf-8")
        salt_byte=bcrypt.gensalt()
        hashed=bcrypt.hashpw(pass_byte,salt_byte)
        return hashed.decode("utf-8")
    
    @staticmethod
    def verify_password(plain_password,hashed_password):
        plain_byte=plain_password.encode("utf-8")
        hashed_byte=hashed_password.encode("utf-8")
        return bcrypt.checkpw(plain_byte,hashed_byte)
    
    
    #=============create access token===========
    
def create_accese_token(data:dict):
    to_encode=data.copy()
    expire=datetime.now()+timedelta(minutes=EXPIRE_ACCESS_TOKEN)
    to_encode.update({"exp":expire})
    token=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return token
    
def decode_token(token:str):
    payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    email=payload.get("sub")
    if not email:
        raise JWTError("token has no information")
    return payload
        
        