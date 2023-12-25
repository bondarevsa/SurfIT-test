from datetime import datetime
from enum import Enum as PythonEnum

from sqlalchemy import TIMESTAMP, Boolean, Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database.database import Base


class AdvertisementType(str, PythonEnum):
    SALE = "продажа"
    PURCHASE = "покупка"
    SERVICE = "оказание услуг"


class SortColumnType(str, PythonEnum):
    id = "id"
    adv_type = "adv_type"
    header = "header"
    body = "body"
    created_at = "created_at"
    created_by = "created_by"


class SortDirectionType(str, PythonEnum):
    asc = "asc"
    desc = "desc"


# class ComplaintType(str, PythonEnum):
#     SALE = 'продажа'
#     PURCHASE = 'покупка'
#     SERVICE = 'оказание услуг'


class User(Base):
    __tablename__ = "user"
    id: int = Column(Integer, primary_key=True)
    email: str = Column(String, nullable=False, unique=True)
    username: str = Column(String, nullable=False, unique=True)
    hashed_password: str = Column(String(length=1024), nullable=False)
    is_admin: bool = Column(Boolean, default=False, nullable=False)
    is_banned: bool = Column(Boolean, default=False)

    advertisements = relationship("Advertisement", back_populates="author")


class Advertisement(Base):
    __tablename__ = "advertisement"

    id: int = Column(Integer, primary_key=True)
    body: str = Column(String)
    adv_type: str = Column(Enum(AdvertisementType))
    header: str = Column(String)
    created_at: datetime = Column(TIMESTAMP, default=datetime.utcnow)
    created_by: int = Column(Integer, ForeignKey("user.id"))

    comment = relationship("Review")
    author = relationship("User", back_populates="advertisements", lazy="joined")


class Review(Base):
    __tablename__ = "review"

    id: int = Column(Integer, primary_key=True)
    text: str = Column(String)
    created_at: datetime = Column(TIMESTAMP, default=datetime.utcnow)
    created_by: int = Column(Integer, ForeignKey("user.id"))
    rating: int = Column(Integer)
    advertisement_id: int = Column(Integer, ForeignKey("advertisement.id"))

    author = relationship("User", lazy="joined")


# class Complaint(Base):
#     __tablename__ = "complaint"
#
#     id: int = Column(Integer, primary_key=True)
#     text: str = Column(String)
#     created_at = Column(TIMESTAMP, default=datetime.utcnow)
#     user_id: int = Column(Integer, ForeignKey("user.id"))
#     advertisement_id: int = Column(Integer, ForeignKey("advertisement.id"))
#
#     author = relationship("User", lazy='joined')
