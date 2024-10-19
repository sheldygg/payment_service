from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter

from src.application.create_payment import CreatePayment, CreatePaymentDto
from src.core.models.payment import PaymentId

router = APIRouter(prefix="/payment")


@router.post("/create")
@inject
async def create_payment(
    payment: CreatePaymentDto, interactor: FromDishka[CreatePayment]
) -> PaymentId:
    return await interactor(payment)
