from sqlalchemy import String, Float
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.db.models.base import Base
from src.core.models.payment import PaymentDto

class Payment(Base):
    __tablename__ = "payment"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    amount: Mapped[float] = mapped_column(Float)
    description: Mapped[str] = mapped_column(String)

    def to_dto(self) -> PaymentDto:
        return PaymentDto(
            id=self.id,
            amount=self.amount,
            description=self.description,
        )