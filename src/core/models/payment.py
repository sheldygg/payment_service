from dataclasses import dataclass
from typing import NewType

PaymentId = NewType("PaymentId", str)


@dataclass
class PaymentDto:
    id: PaymentId
    amount: float
    description: str
