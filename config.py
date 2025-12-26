from pydantic_settings import BaseSettings, SettingsConfigDict
from openai import AsyncOpenAI


class Settings(BaseSettings):

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    RABBITMQ_HOST: str
    RABBITMQ_PORT: int
    RABBITMQ_USER: str
    RABBITMQ_PASSWORD: str

    DS_API_KEY: str

    @property
    def rabbitmq_url(self) -> str:
        return (
            f'amqp://{self.RABBITMQ_USER}:{self.RABBITMQ_PASSWORD}@'
            f'{self.RABBITMQ_HOST}:{self.RABBITMQ_PORT}'
        )

    @property
    def get_ds_api_key(self) -> str:
        return self.DS_API_KEY


settings = Settings()
