from tortoise import Tortoise
from aiogram import Bot, Dispatcher
from core.handlers import setup_routers
import asyncio, logging

from config_reader import config

bot = Bot(token=config.BOT_TOKEN.get_secret_value())
bot.my_admin_list = [938450625]
dp = Dispatcher()


async def on_startup():
    await Tortoise.init(
        db_url=config.DB_URL.get_secret_value(),
        modules={"models": ["core.db.models.voice_and_user"]},
    )
    await Tortoise.generate_schemas()


async def on_shutdown():
    await Tortoise.close_connections()


async def bot_start():
    dp.startup.register(on_startup)
    dp.startup.register(on_shutdown)
    dp.include_router(setup_routers())
    # dp.update.middleware(UserMiddleware)
    await bot.delete_webhook(True)
    await dp.start_polling(bot)


async def bot_stop():
    await dp.stop_polling()


if __name__ == "__main__":
    try:
        logging.basicConfig(level=20)
        asyncio.run(bot_start())
    except KeyboardInterrupt:
        asyncio.run(bot_stop())
