from sqlalchemy import Column, Integer

from src.db.model import Base


class Users(Base):
    __tablename__ = "users"

    tg_id = Column(Integer, primary_key=True)
