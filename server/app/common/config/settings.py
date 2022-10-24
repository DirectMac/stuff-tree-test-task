from pydantic import BaseSettings
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class PostgreSQLSettings(BaseSettings):
    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_port: str
    postgres_db: str


class AppSettings(BaseSettings):
    server_port: int


class Settings(
    PostgreSQLSettings,
    AppSettings
):
    pass
