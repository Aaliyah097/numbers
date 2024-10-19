import aiogram
from aiogram.filters import Command
from aiogram.types import Message

router = aiogram.Router()


@router.message(Command("start"))
async def start(msg: Message) -> None:
    await msg.reply("OK")
