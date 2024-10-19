import datetime

from pydantic import BaseModel


class TimestampMixin:
    created_at: datetime.datetime | None = None
    updated_at: datetime.datetime | None = None
