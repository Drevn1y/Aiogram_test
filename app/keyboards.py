from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=
                           [
                               [KeyboardButton(text='Каталог')],
                               [KeyboardButton(text='Корзина'), KeyboardButton(text='Контакты')]
                           ], resize_keyboard=True, input_field_placeholder='Выберите пункт меню')

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Каталог', callback_data='catalog')],
    [InlineKeyboardButton(text='Корзина', callback_data='basket')],
    [InlineKeyboardButton(text='Контакты', callback_data='contact')]
])


# cars = ['Tesla', 'BMW', 'Honda']
#
# async def inline_cars():
#     keyboard = InlineKeyboardBuilder()
#     for car in cars:
#         keyboard.add(InlineKeyboardButton(text=car, url='https://google.com/'))
#     return keyboard.adjust(2).as_markup()
#
# async def reply_cars():
#     keyboard = ReplyKeyboardBuilder()
#     for car in cars:
#         keyboard.add(KeyboardButton(text=car))
#     return keyboard.adjust(2).as_markup()
