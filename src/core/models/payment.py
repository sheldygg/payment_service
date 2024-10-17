from dataclasses import dataclass


@dataclass
class PaymentDto:
    id: str
    amount: float
    description: str
