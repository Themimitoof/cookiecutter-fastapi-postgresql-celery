import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, AnyUrl, BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    """
    Configuration model for {{cookiecutter.package_dir}}.
    """

    # -- App settings section
    PROJECT_NAME: str
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = (
        60 * 24 * 8
    )  # 60 minutes * 24 hours * 8 days = 8 days
    # SERVER_NAME: str
    # SERVER_HOST: AnyHttpUrl

    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    # -- Database settings section

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v

        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB')}",
        )

    # -- Celery settings section

    CELERY_SERVER: str
    CELERY_USER: str
    CELERY_PASSWORD: Optional[str]
    CELERY_VHOST: str
    CELERY_BROKER_DSN: Optional[AnyUrl] = None

    @validator("CELERY_BROKER_DSN", pre=True)
    def assemble_celery_dsn(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v

        return AnyUrl.build(
            scheme="amqp",
            user=values.get("CELERY_USER"),
            password=values.get("CELERY_PASSWORD"),
            host=values.get("CELERY_SERVER"),
            path=f"/{values.get('CELERY_VHOST')}",
        )

    class Config:
        case_sensitive = True


settings = Settings()
