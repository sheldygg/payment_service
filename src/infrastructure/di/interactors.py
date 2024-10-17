from dishka import Provider, Scope, provide

from src.application.get_wallet import GetWallet


class InteractorsProvider(Provider):
    scope = Scope.REQUEST

    get_wallet = provide(GetWallet)