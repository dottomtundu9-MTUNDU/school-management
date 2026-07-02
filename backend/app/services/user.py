from app.schemas.user import UserCreate
from sqlalchemy.orm import Session
from app.models.user import User

def create(request:UserCreate,db:Session):
    user=User(email=request.email,password=request.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
    
    