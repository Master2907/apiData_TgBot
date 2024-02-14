from aiogram.types import Message, URLInputFile
from aiogram import Bot
import requests

from .local_setting import API_HOST

async def getMovie(message: Message):
    id = message.text
    response = requests.get(f'{API_HOST}/api/getmovie/{id}').json()
    image = URLInputFile(
        url=API_HOST + response['poster'],
        filename='poster.png'
    )
    video = URLInputFile(
        url=API_HOST + response['video'],
    )
    print(response['id'])
    print(API_HOST + response['poster'])
    await message.answer_photo(photo=image)
    await message.answer_video(video=video)
    await message.answer(message.text)