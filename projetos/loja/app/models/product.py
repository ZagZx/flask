from app import db

from sqlalchemy import (
    String,
    Integer,
    Numeric,
    Text
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)
from decimal import Decimal

class Product(db.Model):
    __tablename__ = 'products'

    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    name:Mapped[str] = mapped_column(String(255), nullable=False)
    price:Mapped[Decimal] = mapped_column(Numeric(10,2), nullable=False)
    description:Mapped[str] = mapped_column(Text, nullable=False)