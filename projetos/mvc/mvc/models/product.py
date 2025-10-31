from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Numeric, ForeignKey

from mvc.extensions import Base
from .user import User

class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    price: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    seller_id = Mapped[int] = mapped_column(ForeignKey(User.id))

    seller = Mapped[User] = mapped_column(relationship(back_populates='sold_products'))
