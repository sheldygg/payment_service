from tronpy import AsyncTron
from tronpy.keys import PrivateKey

from src.application.common.interactor import Interactor
from src.core.models.wallet import WalletAddress, WalletDto
from src.infrastructure.db.repositores.wallet import WalletRepository
from src.infrastructure.db.uow import UnitOfWork


class GenerateWallet(Interactor[WalletAddress, WalletDto]):
    def __init__(
        self, tron: AsyncTron, wallet_repository: WalletRepository, ouw: UnitOfWork
    ):
        self.tron = tron
        self.wallet_repository = wallet_repository
        self.ouw = ouw

    async def __call__(self, data) -> WalletDto:
        generated_wallet = self.tron.generate_address(PrivateKey.random())
        wallet = WalletDto(
            address=generated_wallet["base58check_address"],
            private_key=generated_wallet["private_key"],
        )
        async with self.ouw:
            await self.wallet_repository.add_wallet(wallet)
            await self.ouw.commit()
            return wallet
