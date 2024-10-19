from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.core.models.wallet import WalletDto, WalletAddress
from src.infrastructure.db.models.base import Base


class Wallet(Base):
    __tablename__ = "wallet"

    address: Mapped[str] = mapped_column(String, primary_key=True)
    private_key: Mapped[str] = mapped_column(String)

    def to_dto(self) -> WalletDto:
        return WalletDto(
            address=WalletAddress(self.address),
            private_key=self.private_key,
        )
