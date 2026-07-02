from fastapi import FastAPI,Depends
from app.core.dependencies import get_db
from sqlalchemy.orm import Session
from app.routers.user import router as user_router
from app.routers.auth import router as auth_router
from app.core.database import engine,Base

Base.metadata.create_all(engine)

app=FastAPI(
    title="Smart School ERP",
    description="backend system for school managment",
    version="1.0.0"
)
app.include_router(user_router)
app.include_router(auth_router)

    
@app.get("/test_db",tags=["db test"])
async def test_db(db:Session=Depends(get_db)):
    return{
        "message":"welcome in smart School ERP API"
    }
