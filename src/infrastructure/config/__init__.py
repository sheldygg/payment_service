from dataclasses import dataclass

from .db import DatabaseConfig


@dataclass
class Config:
    db: DatabaseConfig


def get_config(path: str | None = None) -> Config:
    return Config(
        db=DatabaseConfig(
            host="localhost",
            port=5432,
            username="postgres",
            password="postgres",
            database="payment_service",
        )
    )
