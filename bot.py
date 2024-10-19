from aiogram import Bot
from aiogram.client.default import DefaultBotProperties

from settings import Settings

bot = Bot(default=DefaultBotProperties(parse_mode="Markdown"), token=Settings.BOT_TOKEN)
