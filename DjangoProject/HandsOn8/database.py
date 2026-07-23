from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite+aiosqlite:///./coursemanager.db"

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()


async def get_db(): # its a dependency function 
    async with SessionLocal() as session:
        yield session   # yield tells that this func is a generator and doesnt act like a return function, 
                        #it will return the session object to the caller and then close the session after the request is completed.