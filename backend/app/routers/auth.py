from fastapi import APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.services.auth import login

router=APIRouter(tags=["authentication"])

@router.post("/")
def login_user(data:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    return login(data.username,data.password,db)