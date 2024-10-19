from dataclasses import dataclass
from uuid import uuid4

from src.application.common.interactor import Interactor
from src.core.models.payment import PaymentDto, PaymentId
from src.infrastructure.db.repositores.payment import PaymentRepository
from src.infrastructure.db.uow import UnitOfWork


@dataclass
class CreatePaymentDto:
    amount: float
    description: str


class CreatePayment(Interactor[CreatePaymentDto, PaymentId]):
    def __init__(self, payment_repository: PaymentRepository, uow: UnitOfWork):
        self.payment_repository = payment_repository
        self.uow = uow

    async def __call__(self, create_payment: CreatePaymentDto) -> PaymentId:
        payment = PaymentDto(
            id=PaymentId(str(uuid4())),
            amount=create_payment.amount,
            description=create_payment.description,
        )
        async with self.uow:
            await self.payment_repository.add_paymnet(payment)
            await self.uow.commit()
            return payment.id
