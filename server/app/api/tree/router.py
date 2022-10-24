from aiohttp import web
from aiohttp_pydantic import PydanticView
from app.common.models.user import User
from app.common.database import db


prefix = "/tree"


class TreeItemView(PydanticView):
    async def get(self):
        users: list[User] = await db.get_all(User)
        bosses_filtered = filter(lambda employee : employee.boss_id is None, users)
        employees_filtered = filter(lambda employee : employee.boss_id is not None, users)

        bosses = list(bosses_filtered)
        users = list(employees_filtered)

        if len(bosses) == 0:
            raise web.HTTPNotFound(
                text="Key: 'bosses'. At least 1 user is required for tree modeling"
            )

        def create_tree(bosses: list[User]):
            return [
                {
                    **boss.dict(),
                    "employees": create_tree(
                        [employee for employee in users if employee.boss_id == boss.id]
                    ),
                }
                for boss in bosses
            ]

        return web.json_response(create_tree(bosses))
