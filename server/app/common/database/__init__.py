from .postgresql_connector import PostgreSQLConnector
from .postgresql_service import PostgreSQLService
from ..config import config


class PostgresqlManager(PostgreSQLConnector, PostgreSQLService):
    def __init__(
        self,
        username: str,
        password: str,
        host: str,
        port: int,
        name: str
    ): super().__init__(username, password, host, port, name)


db = PostgresqlManager(
    username=config.postgres_user,
    password=config.postgres_password,
    host=config.postgres_host,
    port=config.postgres_port,
    name=config.postgres_db
)
