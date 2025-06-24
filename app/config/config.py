from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    TOKEN: str
    BASE_SITE: str
    ADMIN_ID: str
    model_config = SettingsConfigDict(env_file=".env", extra="allow")

    def get_webhook_url(self) -> str:
        return f"{self.BASE_SITE}/webhook"


settings = Settings()
