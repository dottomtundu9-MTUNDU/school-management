from app.schemas.user import UserCreate
from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import Hash

def create(request:UserCreate,db:Session):
    existing=db.query(User).filter(User.email==request.email)
    if existing:
        raise HTTPException(status_code=status.HTTP_208_ALREADY_REPORTED,detail="the entered email already used,use another one")
    hash_password=Hash.password_hashing(request.password)
    user=User(email=request.email,password=hash_password,role=request.role)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
    
    