import datetime

from pydantic import BaseModel

from src.models.timestamp_mixin import TimestampMixin


class User(BaseModel, TimestampMixin):
    tg_id: int
    tg_login: str | None
