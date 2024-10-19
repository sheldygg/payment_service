from sqlalchemy import Float, String
from sqlalchemy.orm import Mapped, mapped_column

from src.core.models.payment import PaymentDto, PaymentId
from src.infrastructure.db.models.base import Base


class Payment(Base):
    __tablename__ = "payment"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    amount: Mapped[float] = mapped_column(Float)
    description: Mapped[str] = mapped_column(String)

    def to_dto(self) -> PaymentDto:
        return PaymentDto(
            id=PaymentId(self.id),
            amount=self.amount,
            description=self.description,
        )
