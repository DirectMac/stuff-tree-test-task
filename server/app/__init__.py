from aiohttp import web
from .main import get_application
from .common.config import config


def start_app():
    app = get_application()
    web.run_app(app, port=config.server_port)
