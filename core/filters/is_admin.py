from aiogram import Bot
from aiogram.types import Message
from aiogram.filters import Filter


class IsAdmin(Filter):
    def __init__(self) -> None:
        pass

    async def __call__(self, message: Message, bot: Bot) -> bool:
        return message.from_user.id in bot.my_admin_list
