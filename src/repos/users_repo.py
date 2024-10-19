from typing import Union

from sqlalchemy import insert, select

from src.db.session import get_base_repository
from src.db.tables.users import Users
from src.models.user import User


class UsersRepo:
    @staticmethod
    async def get_user(tg_id: int) -> Union[User, None]:
        async with get_base_repository().session() as session:
            query = select(Users.__table__).where(Users.tg_id == tg_id)
            query_result = await session.execute(query)
            if not (user := query_result.mappings().one_or_none()):
                return None
            return User(**user)

    @staticmethod
    async def create_user(tg_id: int, tg_login: str | None) -> User:
        async with get_base_repository().session() as session:
            query = insert(Users).returning(Users.__table__).values(tg_id=tg_id)
            query_result = await session.execute(query)
            user = query_result.mappings().one_or_none()
            return User(**user)
