from fastapi import FastAPI,Depends
from app.core.dependencies import get_db
from sqlalchemy.orm import Session

app=FastAPI(
    title="Smart School ERP",
    description="backend system for school managment",
    version="1.0.0"
)

    
@app.get("/test_db",tags=["db test"])
async def test_db(db:Session=Depends(get_db)):
    return{
        "message":"welcome in smart School ERP API"
    }
