from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.services.user import create
from app.schemas.user import UserCreate

router=APIRouter(prefix="/User",tags=["user management"])

@router.post("")
def create_user(data:UserCreate,db:Session=Depends(get_db)):
    return create(data,db)