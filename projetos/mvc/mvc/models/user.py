from flask_login import UserMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from typing import List
from werkzeug.security import check_password_hash

from mvc.extensions import Base
from .product import Product

class User(UserMixin, Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)

    sold_products = Mapped[List[Product]] = relationship(back_populates='seller')

    def check_password(self, password: str):
        return check_password_hash(self.password_hash, password)