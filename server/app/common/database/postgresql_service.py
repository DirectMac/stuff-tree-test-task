from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from sqlalchemy.exc import DatabaseError


class PostgreSQLService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self, model):
        query = select(model)
        records = await self.session.execute(query)
        result = records.scalars().all()
        return result

    async def get(self, model, id: int):
        query = select(model).where(model.id == id)
        record = await self.session.execute(query)
        result = record.scalars().first()
        return result

    async def post(self, model, **kwargs):
        record = model(**kwargs)
        self.session.add(record)
        try:
            await self.session.commit()
        except DatabaseError:
            await self.session.rollback()
        return record

    async def put(self, record, **kwargs):
        Model = record.__class__
        await self.session.execute(
            update(Model)
            .where(Model.id == record.id)
            .values(**kwargs)
        )
        try:
            await self.session.commit()
        except DatabaseError:
            await self.session.rollback()

        return record

    async def delete(self, record):
        await self.session.delete(record)
        try:
            await self.session.commit()
        except DatabaseError:
            await self.session.rollback()

        return record
