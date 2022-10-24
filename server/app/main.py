from aiohttp import web
import aiohttp_cors
from .common.database import db
from .api.user import user_router
from .api.tree import tree_router


ROUTES = [
    *user_router,
    *tree_router
]


async def get_application():
    app = web.Application()

    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*"
        )
    })

    await db.open_connection()

    for route in ROUTES:
        app.router.add_route(*route)

    for route in list(app.router.routes()):
        cors.add(route)

    return app
