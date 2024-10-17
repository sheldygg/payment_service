from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.db.models.wallet import Wallet
from src.core.models.wallet import WalletDto

class WalletRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_wallet_by_address(self, address: str) -> WalletDto:
        wallet = await self.session.get(Wallet, address)
        return wallet.to_dto() if wallet else None
