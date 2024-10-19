import os
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv


load_dotenv('.env')


bot = Bot(
    default=DefaultBotProperties(parse_mode='Markdown'),
    token=os.environ.get('BOT_TOKEN')
)
