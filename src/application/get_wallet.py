from src.application.common.interactor import Interactor
from src.core.enums import WalletStatus
from src.core.models.wallet import WalletAddress
from src.infrastructure.db.repositores.wallet import WalletRepository


class GetWallet(Interactor[WalletAddress, WalletStatus]):
    def __init__(self, wallet_repository: WalletRepository):
        self.wallet_repository = wallet_repository

    async def __call__(self, wallet_address: WalletAddress) -> WalletStatus:
        wallet = await self.wallet_repository.get_wallet_by_address(wallet_address)
        if wallet is None:
            return WalletStatus.UNKNOWN
        else:
            return WalletStatus.ACTIVE
