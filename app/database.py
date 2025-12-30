from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, DeclarativeBase

bd_host = "localhost"
bd_port = 5432
bd_user = "postgres"
bd_password = "postgres"
bd_name = "postgres"

DATABASE_URL = f"postgresql+asyncpg://{bd_user}:{bd_password}@{bd_host}:{bd_port}/{bd_name}"

engine = create_async_engine(DATABASE_URL)

async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    pass
