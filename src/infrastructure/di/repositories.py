from dishka import Provider, Scope, provide

from src.infrastructure.db.repositores.payment import PaymentRepository
from src.infrastructure.db.repositores.wallet import WalletRepository


class RepositoriesProvider(Provider):
    scope = Scope.REQUEST

    wallet = provide(WalletRepository)
    payment = provide(PaymentRepository)
