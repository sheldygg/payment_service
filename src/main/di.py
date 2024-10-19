from dishka import AsyncContainer, Provider, make_async_container

from src.infrastructure.di.config import ConfigProvider
from src.infrastructure.di.db import DbProvider
from src.infrastructure.di.interactors import InteractorsProvider
from src.infrastructure.di.repositories import RepositoriesProvider
from src.infrastructure.di.tron import TronProvider


def get_common_providers() -> list[Provider]:
    return [
        ConfigProvider(),
        DbProvider(),
        RepositoriesProvider(),
        InteractorsProvider(),
        TronProvider(),
    ]


def create_api_container() -> AsyncContainer:
    return make_async_container(*get_common_providers())
