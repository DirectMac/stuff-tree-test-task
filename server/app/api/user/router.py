from aiohttp import web
from aiohttp_pydantic import PydanticView
from app.common.database import db
from app.common.models.user import User, CreateUser, UpdateUser


prefix = "/users"


class UserCollectionView(PydanticView):
    async def get(self) -> list[User]:
        users: list[User] = await db.get_all(User)
        if len(users) == 0:
            raise web.HTTPNotFound(text="Users does not exist")

        return web.json_response([user.dict() for user in users])

    async def post(self, payload: CreateUser):
        boss_id = payload.boss_id
        if boss_id:
            boss: User | None = await db.get(User, boss_id)
            if boss is None:
                raise web.HTTPBadRequest(text="The boss does not exist")

        result = await db.post(User, **payload.dict())

        return web.json_response(
            result.dict(),
            status=201
        )


class UserItemView(PydanticView):
    async def get(self, id: int, /):
        user: User | None = await db.get(User, id)
        if user is None:
            raise web.HTTPNotFound()

        return web.json_response(user.dict())

    async def put(self, id: int, /, payload: UpdateUser):
        user: User | None = await db.get(User, id)
        users: list[User] | None = await db.get_all(User)
        if user is None:
            raise web.HTTPNotFound()

        boss_id = payload.boss_id
        boss: User | None = await db.get(User, boss_id)
        payload = payload.dict(exclude_unset=True)
        if boss_id is None:
            pass
        elif boss is None:
            raise web.HTTPBadRequest()
        for employee in users:
            if employee.boss_id == user.id:
                await db.put(
                    employee,
                    **{'boss_id': user.boss_id if user.boss_id else None}
                )

        result = await db.put(user, **payload)
        return web.json_response(result.dict())

    async def delete(self, id: int, /):
        user: User | None = await db.get(User, id)
        users: list[User] | None = await db.get_all(User)

        if user is None or len(users) == 0 :
            raise web.HTTPNotFound()

        ex_boss = user.boss_id
        for employee in users:
            if employee.boss_id == user.id:
                await db.put(
                    employee,
                    **{'boss_id': ex_boss if ex_boss else None}
                )
        result = await db.delete(user)

        return web.json_response(result.dict())
