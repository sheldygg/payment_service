from pydantic import BaseModel

from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter

from src.core.models.wallet import WalletAddress
from src.application.get_wallet import GetWallet

router = APIRouter(prefix="/wallet")


class WalletResponse(BaseModel):
    wallet: str

@router.get("/{address}/info", response_model=WalletResponse)
@inject
async def get_wallet_info(
    address: WalletAddress,
    interactor: FromDishka[GetWallet],
) -> WalletResponse:
    wallet = await interactor(wallet_address=address)
    if wallet:
        return WalletResponse(wallet=wallet.address)

    return WalletResponse(wallet="Wallet not found")
