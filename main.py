import asyncio
import logging

import aiogram
from aiogram.fsm.storage.memory import MemoryStorage

from bot import bot
from src.router import router


async def main():
    dp = aiogram.Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)

    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        pass


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
