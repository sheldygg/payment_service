from dishka import Provider, Scope, provide
from tronpy import AsyncTron


class TronProvider(Provider):
    scope = Scope.APP

    @provide
    def get_tron(self) -> AsyncTron:
        return AsyncTron()
