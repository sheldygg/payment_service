from dishka import Provider, provide, Scope

from src.infrastructure.config import Config, get_config, DatabaseConfig

class ConfigProvider(Provider):
    scope = Scope.APP

    @provide
    def get_config(self) -> Config:
        return get_config()

    @provide
    def get_db_config(self, config: Config) -> DatabaseConfig:
        return config.db
