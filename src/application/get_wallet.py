from src.application.common.interactor import Interactor
from src.infrastructure.db.repositores.wallet import WalletRepository
from src.core.models.wallet import WalletAddress

class GetWallet(Interactor):
    def __init__(self, wallet_repository: WalletRepository):
        self.wallet_repository = wallet_repository

    async def __call__(self, wallet_address: WalletAddress):
        r = await self.wallet_repository.get_wallet_by_address(wallet_address)
        return r