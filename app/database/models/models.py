from datetime import datetime
from sqlalchemy import Integer, String, TIMESTAMP, Column, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.database.database import Base


class User(Base):
    __tablename__ = "user"
    id: int = Column(Integer, primary_key=True)
    email: str = Column(String, nullable=False)
    username: str = Column(String, nullable=False)
    hashed_password: str = Column(String(length=1024), nullable=False)
    is_admin: bool = Column(Boolean, default=False, nullable=False)

    advertisements = relationship("Advertisement", back_populates="author")


class Advertisement(Base):
    __tablename__ = "advertisement"

    id: int = Column(Integer, primary_key=True)
    body: str = Column(String)
    adv_type: str = Column(String)
    header: str = Column(String)
    timestamp = Column(TIMESTAMP, default=datetime.utcnow)
    user_id: int = Column(Integer, ForeignKey('user.id'))

    comment = relationship('Comment')
    author = relationship("User", back_populates="advertisements", lazy='joined')


class Comment(Base):
    __tablename__ = "comment"

    id: int = Column(Integer, primary_key=True)
    text: str = Column(String)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    user_id: int = Column(Integer, ForeignKey("user.id"))
    post_id: int = Column(Integer, ForeignKey("advertisement.id"))

    author = relationship("User", lazy='joined')
