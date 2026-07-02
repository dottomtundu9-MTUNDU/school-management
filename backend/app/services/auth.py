
from sqlalchemy.orm import Session
from fastapi import HTTPException,status
from app.models.user import User
from app.core.security import Hash,create_accese_token

def login(email:str,password:str,db:Session):
    user=db.query(User).filter(User.email==email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="check your email")
    hash_password=Hash.verify_password(password,user.password)
    if not hash_password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="check your password")
    if not user.is_active:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="account is expired")
    access_token=create_accese_token({"sub":email})
    return{
        "access_token":access_token,
        "token_type":"Bearer"
    }
    