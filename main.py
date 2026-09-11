import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from app.user import user
from app.admin import admin

async def main() -> None:
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_routers(user, admin)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        print("Starting up...")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("EXIT")