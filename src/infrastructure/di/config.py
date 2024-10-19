from dishka import Provider, Scope, provide

from src.infrastructure.config import Config, DatabaseConfig, get_config


class ConfigProvider(Provider):
    scope = Scope.APP

    @provide
    def get_config(self) -> Config:
        return get_config()

    @provide
    def get_db_config(self, config: Config) -> DatabaseConfig:
        return config.db
