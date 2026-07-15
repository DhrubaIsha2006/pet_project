from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="APP_",
    )

    MONGO_DB_URL: str
    MONGO_DB_DB: str


settings = AppSettings()  # type: ignore[call-arg]
