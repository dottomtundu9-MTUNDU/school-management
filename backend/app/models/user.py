from app.core.database import Base
from sqlalchemy import Column,Integer,String,DateTime,Boolean,Enum
from datetime import datetime
from app.core.dependencies import RoleEnum

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True)
    email=Column(String,unique=True)
    password=Column(String,nullable=False)
    role=Column(Enum(RoleEnum),default=RoleEnum.student)
    is_active=Column(Boolean,default=True)
    created_at=Column(DateTime,default=datetime.now())
    updated_at=Column(DateTime,default=datetime.now(),onupdate=datetime.now())  