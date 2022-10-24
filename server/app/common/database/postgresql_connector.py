from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine
from sqlalchemy.orm import sessionmaker


class PostgreSQLConnector:
    def __init__(
        self,
        username: str,
        password: str,
        host: str,
        port: int,
        name: str
    ):
        self.path = f"postgresql+asyncpg://{username}:{password}@{host}:{port}/{name}"
        self._engine: AsyncEngine = create_async_engine(
            self.path,
            future=True,
            echo=False
        )
        self._session: AsyncSession = sessionmaker(
            self.engine,
            expire_on_commit=False,
            class_=AsyncSession
        )()

    @property
    def session(self):
        return self._session

    @property
    def engine(self):
        return self._engine

    async def open_connection(self) -> None:
        async with self.engine.begin() as connection:
            await connection.run_sync(SQLModel.metadata.create_all)

