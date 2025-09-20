from flask_login import UserMixin
from app import db

from sqlalchemy import (
    String,
    Integer,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    name:Mapped[str] = mapped_column(String(255), nullable=False)
    email:Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    password_hash:Mapped[str] = mapped_column(String(255), nullable=False)