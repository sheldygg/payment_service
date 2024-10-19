from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter

from src.application.generate_wallet import GenerateWallet
from src.application.get_wallet import GetWallet
from src.core.models.wallet import WalletAddress, WalletDto
from src.core.enums import WalletStatus

router = APIRouter(prefix="/wallet")


@router.get("/{address}/status", response_model=WalletStatus)
@inject
async def get_wallet_status(
    address: WalletAddress,
    interactor: FromDishka[GetWallet],
) -> WalletStatus:
    wallet_status = await interactor(wallet_address=address)
    return wallet_status


@router.get("/generate", response_model=WalletDto)
@inject
async def generate_wallet(
    interactor: FromDishka[GenerateWallet],
) -> WalletDto:
    wallet = await interactor(1)
    return wallet
