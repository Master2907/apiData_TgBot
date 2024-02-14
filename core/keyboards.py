from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def getVideoBtn(id):
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="Get Video", callback_data=f'getvideo_{id}')
    keyboard.adjust(1)

    return keyboard.as_markup()