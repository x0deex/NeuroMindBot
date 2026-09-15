import asyncio

from aiogram import Bot, Dispatcher
from config import BOT_TOKEN

from app.user import user
from app.admin import admin
from app.database.models import async_main

async def main() -> None:
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.startup.register(async_main)
    dp.include_routers(user, admin)
    await dp.start_polling(bot)

async def on_startup(dispatcher):
    await async_main()

if __name__ == "__main__":
    try:
        print("Starting up...")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("EXIT")