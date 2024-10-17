import asyncio

from fastapi import FastAPI
from dishka.integrations.fastapi import setup_dishka

from src.main.di import create_api_container
from src.presentation.api.routes import wallet

def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(wallet.router)

    container = create_api_container()

    setup_dishka(container, app)

    return app

app = create_app()