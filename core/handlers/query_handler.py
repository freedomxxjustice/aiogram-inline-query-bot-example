from secrets import token_hex
from aiogram.types import (
    InlineQuery,
    InlineQueryResultCachedVoice,
)
from aiogram import Router

from core.db.models.voice_and_user import AnyTypeOfMessage

router = Router()


@router.inline_query()
async def send_voice(query: InlineQuery):
    # result_id = token_hex(2)
    file_ids = await AnyTypeOfMessage.all().values_list("file_id", flat=True)
    file_titles = await AnyTypeOfMessage.all().values_list("title", flat=True)
    items = []
    for i in range(len(file_ids)):
        items.append(
            InlineQueryResultCachedVoice(
                title=file_titles[i], voice_file_id=file_ids[i], id=token_hex(2)
            )
        )
    await query.answer(items, cache_time=1, is_personal=False)
