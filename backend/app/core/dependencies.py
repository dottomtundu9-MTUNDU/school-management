from app.core.database import AsyncSessionlocal


async def get_db():
    async with AsyncSessionlocal()as db:
        try:
            yield db
        finally:
            await db.close()    