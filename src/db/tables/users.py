from sqlalchemy import Column, Integer, String

from src.db.model import Base, TimestampMixin


class Users(Base, TimestampMixin):
    __tablename__ = "users"

    tg_id = Column(Integer, primary_key=True)
    tg_login = Column(String, default=None, nullable=True)
