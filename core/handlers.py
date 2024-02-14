from aiogram.types import Message, URLInputFile
from aiogram import Bot
import requests

from .local_setting import API_HOST

async def getMovie(message: Message):
    id = message.text

    response = requests.get(f'{API_HOST}/api/getmovie/{id}')
    if response.status_code == 404:

        response = 'Not found 404'
        await message.answer(response)

    else:
        
        data = response.json()
        image = URLInputFile(
            url=API_HOST + data['poster'],
            filename='poster.png'
        )
        
        caption = f"Title : {data['title']}\nGenres : {data['genres']}\nYear : {data['year']}\n\nDescription :\n{data['description']}"
        
        await message.answer_photo(photo=image, caption=caption)