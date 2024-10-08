from aiogram import Router


def setup_routers():
    from . import voice_upload_handler, query_handler

    router = Router()
    router.include_router(voice_upload_handler.router)
    router.include_router(query_handler.router)
    return router