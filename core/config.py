from pydantic import BaseSettings


class CommonSettings(BaseSettings):
    APP_NAME: str = "FastAPI BoilerPlate"
    DEBUG_MODE: bool = True


class ServerSettings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000


class Settings(CommonSettings, ServerSettings):

    class Config:
        env_file = "./.env"