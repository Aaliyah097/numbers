from contextlib import asynccontextmanager
from logging import getLogger
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from settings import Settings


class BaseRepository:
    def __init__(self, db: AsyncEngine, **kwargs) -> None:
        self._session_maker = sessionmaker(
            db, expire_on_commit=False, class_=AsyncSession)
        self._logger = getLogger(self.__class__.__name__)
        super().__init__(**kwargs)

    @asynccontextmanager
    async def session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self._session_maker() as session:
            async with session.begin():
                yield session


def get_base_repository() -> BaseRepository:
    pg_engine: AsyncEngine = create_async_engine(
        Settings.get_async_pg_url(), echo=False)
    return BaseRepository(pg_engine)
