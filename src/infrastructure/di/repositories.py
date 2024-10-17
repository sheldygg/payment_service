from dishka import Provider, provide, Scope

from src.infrastructure.db.repositores.wallet import WalletRepository
from src.infrastructure.db.repositores.payment import PaymentRepository

class RepositoriesProvider(Provider):
    scope = Scope.REQUEST

    wallet = provide(WalletRepository)
    payment = provide(PaymentRepository)

