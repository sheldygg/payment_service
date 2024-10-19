from dataclasses import dataclass
from typing import NewType

WalletAddress = NewType("WalletAddress", str)


@dataclass
class WalletDto:
    address: WalletAddress
    private_key: str

    def decrypt_private_key(self):
        return self.private_key
