from src.models.user import User
from src.repos.users_repo import UsersRepo


class UserService:
    @staticmethod
    async def get_or_create(tg_id: int, tg_login: str | None) -> User:
        return (await UsersRepo.get_user(tg_id)) or (await UsersRepo.create_user(tg_id, tg_login))
