from app.core.database import Base
from sqlalchemy import Column,Integer,String,DateTime,Boolean
from datetime import datetime

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True)
    email=Column(String,unique=False)
    password=Column(String,nullable=False)
    is_active=Column(Boolean,default=True)
    created_at=Column(DateTime,default=datetime.now())
    updated_at=Column(DateTime,onupdate=datetime.now())    