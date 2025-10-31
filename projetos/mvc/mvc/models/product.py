from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Numeric, ForeignKey, Boolean

from mvc.extensions import Base

class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    price: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    avaliable: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    seller_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    purchaser_id: Mapped[int] = mapped_column(ForeignKey('user.id'))

    seller: Mapped["User"] = relationship(back_populates='sold_products')
    purchaser: Mapped["User"] = relationship(back_populates='purchased_products')