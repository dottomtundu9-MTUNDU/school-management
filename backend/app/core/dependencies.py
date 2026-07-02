from app.core.database import SessionLocal
import enum

class RoleEnum(str, enum.Enum):
    admin="admin"
    student="student"
    teacher="teacher"
    parents="parents"





def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()