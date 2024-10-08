from aiogram.types import Message
from aiogram import Router, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, StateFilter
from core.db.models.voice_and_user import AnyTypeOfMessage

from core.filters.is_admin import IsAdmin

router = Router()
router.message.filter(IsAdmin())


class UploadVoice(StatesGroup):
    file_id = State()
    title = State()
    description = State()


class DeleteVoice(StatesGroup):
    title = State()


@router.message(StateFilter(None), Command("addvoice"))
async def upload_voice_start(message: Message, state: FSMContext):
    await message.answer("Please, send your voice message.")
    await state.set_state(UploadVoice.file_id)


@router.message(UploadVoice.file_id, F.voice)
async def upload_voice_file(message: Message, state: FSMContext):
    await state.update_data(file_id=message.voice.file_id)
    await message.answer("Please, enter the title of the audio.")
    await state.set_state(UploadVoice.title)


@router.message(UploadVoice.title, F.text)
async def upload_voice_title(message: Message, state: FSMContext):
    await state.update_data(title=message.text)
    await message.answer("Please, enter the description of the audio.")
    await state.set_state(UploadVoice.description)


@router.message(UploadVoice.description, F.text)
async def upload_voice_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    data = await state.get_data()
    await message.answer(f"Audio '{data['title']}' has been successfully added!")
    await state.clear()
    await AnyTypeOfMessage.create(
        file_id=data["file_id"],
        title=data["title"],
        description=data["description"],
        plays=0,
    )


@router.message(StateFilter(None), F.text.startswith("/deletevoice"))
async def delete_voice_start(message: Message, state: FSMContext):
    await message.answer("Please, enter the title of audio to delete.")
    await state.set_state(DeleteVoice.title)


@router.message(DeleteVoice.title, F.text)
async def delete_voice(message: Message, state: FSMContext):
    await AnyTypeOfMessage.filter(title=message.text).delete()
    await message.answer(f"Audio '{message.text}' was successfully deleted.")
    await state.clear()
