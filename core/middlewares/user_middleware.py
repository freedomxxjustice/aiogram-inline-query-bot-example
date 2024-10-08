from typing import Dict, Any, Callable, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Update

from core.db.models.voice_and_user import User


class UserMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: Dict[str, Any],
    ) -> Any:
        current_event = (
            event.message
            or event.callback_query
            or event.inline_query
            or event.chosen_inline_result
        )
        user = await User.get_or_create(
            id=current_event.from_user.id, username=current_event.from_user.username
        )

        data["user"] = user[0]
        return await handler(event, data)
