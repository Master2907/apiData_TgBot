from aiogram import Bot
from aiogram.types import CallbackQuery, URLInputFile
import requests

from .local_setting import API_HOST


async def getVideo(call: CallbackQuery, bot: Bot):
    id = call.data.split('_')[1]

    response = requests.get(f'{API_HOST}/api/getvideo/{id}')
    if response.status_code == 404:

        response = 'Not found 404'
        await call.message.answer(response)

    else:

        data = response.json()
        video = URLInputFile(
            url=API_HOST + data['video'],
        )
        await call.message.answer('Please wait. The file is being sent')
        await call.bot.send_chat_action(call.message.chat.id, action="upload_video")
        await call.message.answer_video(video=video)
        await call.answer()