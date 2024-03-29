from pathlib import Path

from environs import Env
from fastapi_mail import ConnectionConfig

env_path = Path(__file__).resolve().parents[2].joinpath(".env")

env = Env()
env.read_env(str(env_path))


class AppConfig:
    POSTGRES_HOST = env.str("POSTGRES_HOST")
    POSTGRES_PORT = env.int("POSTGRES_PORT")
    POSTGRES_USER = env.str("POSTGRES_USER")
    POSTGRES_DB = env.str("POSTGRES_DB")
    POSTGRES_PASSWORD = env.str("POSTGRES_PASSWORD")

    MAIL_USERNAME = env.str("MAIL_USERNAME")
    MAIL_PASSWORD = env.str("MAIL_PASSWORD")
    MAIL_FROM = env.str("MAIL_FROM")
    MAIL_PORT = env.int("MAIL_PORT")
    MAIL_SERVER = env.str("MAIL_SERVER")
    MAIL_STARTTLS = env.bool("MAIL_STARTTLS")
    MAIL_SSL_TLS = env.bool("MAIL_SSL_TLS")

    JWT_SECRET_KEY = env.str("JWT_SECRET_KEY")

    def get_db_url(self):
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    def get_smtp_config(self):
        return ConnectionConfig(
            MAIL_USERNAME=self.MAIL_USERNAME,
            MAIL_PASSWORD=self.MAIL_PASSWORD,
            MAIL_FROM=self.MAIL_FROM,
            MAIL_PORT=self.MAIL_PORT,
            MAIL_SERVER=self.MAIL_SERVER,
            MAIL_STARTTLS=self.MAIL_STARTTLS,
            MAIL_SSL_TLS=self.MAIL_SSL_TLS,
        )


app_config = AppConfig()
connection_config = app_config.get_smtp_config()
