from dishka import Provider, make_async_container, AsyncContainer

from src.infrastructure.di.config import ConfigProvider
from src.infrastructure.di.db import DbProvider
from src.infrastructure.di.repositories import RepositoriesProvider
from src.infrastructure.di.interactors import InteractorsProvider

def get_common_providers() -> list[Provider]:
    return [
        ConfigProvider(),
        DbProvider(),
        RepositoriesProvider(),
        InteractorsProvider(),
    ]


def create_api_container() -> AsyncContainer:
    return make_async_container(*get_common_providers())