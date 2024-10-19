from sqlalchemy.ext.asyncio import AsyncSession

from src.core.models.payment import PaymentDto
from src.infrastructure.db.models.payment import Payment


class PaymentRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_paymnet(self, payment: PaymentDto) -> None:
        db = Payment(
            id=payment.id,
            amount=payment.amount,
            description=payment.description,
        )
        self.session.add(db)
