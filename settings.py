from pydantic import BaseSettings


class Settings(BaseSettings):
    API_TELEGRAM_TOKEN: str
    LINK_BOT: str
    CHANNEL_LINK: str
    CHANNEL_ID: str
    ANSWER_NOT_SUB: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
