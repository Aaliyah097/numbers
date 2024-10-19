import aiogram
from aiogram.filters import Command
from aiogram.types import Message

from src.services.user_service import UserService

router = aiogram.Router()


@router.message(Command("start"))
async def start(msg: Message) -> None:
    # если юзера нет в бд, то зарегать его
    # показать приветственное сообщение
    # показать меню
    if not msg.from_user:
        await msg.reply("Не человек")
        return

    user = await UserService.get_or_create(msg.from_user.id, msg.from_user.username)
    print(user)
    await msg.reply("OK")
