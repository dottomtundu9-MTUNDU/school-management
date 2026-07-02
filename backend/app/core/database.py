# from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,AsyncSession
# from sqlalchemy.orm import declarative_base
# from app.core.config import settings

# #create engine that useurl from settings
# engine=create_async_engine(settings.DATABASE_URL,echo=True)
# AsyncSessionlocal=async_sessionmaker(
#     bind=engine,
#     class_=AsyncSession,
#     expire_on_commit=False,
# )
# Base=declarative_base()
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./note.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()