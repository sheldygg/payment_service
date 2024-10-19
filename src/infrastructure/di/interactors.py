from dishka import Provider, Scope, provide

from src.application.create_payment import CreatePayment
from src.application.generate_wallet import GenerateWallet
from src.application.get_wallet import GetWallet


class InteractorsProvider(Provider):
    scope = Scope.REQUEST

    get_wallet = provide(GetWallet)
    generate_wallet = provide(GenerateWallet)
    create_payment = provide(CreatePayment)
