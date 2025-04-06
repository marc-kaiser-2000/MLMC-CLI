from typing import Optional
from dataclasses import dataclass


@dataclass
class AppConfig:
    pass


@dataclass
class LoggerConfig:
    pass


class Config:
    app: Optional[AppConfig] = None
    logger: Optional[LoggerConfig] = None



def defaultConfig() -> Config:
    return Config()

    