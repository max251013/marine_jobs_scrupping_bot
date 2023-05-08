from dataclasses import dataclass

from environs import Env

@dataclass
class TgBot:
    token: str  # token to access telegram bot

@dataclass
class Config:
    tg_bot: TgBot

#Create function, which will read file .env and return
#an instance of the Config class with token filled.

def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')))

user_id = 989716149