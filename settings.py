import os

from dotenv import load_dotenv

load_dotenv(".env")


class Settings:
    BOT_TOKEN: str = os.environ.get("BOT_TOKEN", "")

    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN не указан")

    PG_USER = os.environ.get("POSTGRES_USER")
    PG_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
    PG_DB = os.environ.get("POSTGRES_DB")
    PG_PORT = os.environ.get("POSTGRES_PORT")
    PG_HOST = os.environ.get("POSTGRES_HOST")

    @classmethod
    def get_async_pg_url(cls) -> str:
        return (
            f"postgresql+asyncpg://:@?dsn=postgresql://:@{cls.PG_HOST}/"
            f"{cls.PG_DB}&port={cls.PG_PORT}&user={cls.PG_USER}&password={cls.PG_PASSWORD}"
        )

    @classmethod
    def get_pg_url(cls) -> str:
        return (
            f"postgresql://{Settings.PG_USER}:{Settings.PG_PASSWORD}@"
            f"{Settings.PG_HOST}:{Settings.PG_PORT}/{Settings.PG_DB}"
        )
