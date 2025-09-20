from app import db

from sqlalchemy import (
    String,
    Integer,
    DECIMAL,
    TEXT
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)


class Product(db.Model):
    __tablename__ = 'products'

    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    name:Mapped[str] = mapped_column(String(255), nullable=False)
    price:Mapped[float] = mapped_column(DECIMAL(10,2), nullable=False)
    description:Mapped[str] = mapped_column(TEXT, nullable=False)