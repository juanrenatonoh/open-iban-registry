from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    app_version: str

    iban_registry_config_header: list[str]
    iban_registry_config_encoding: list[str]

    mongo_url: str
    mongo_db: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


settings = Settings()
