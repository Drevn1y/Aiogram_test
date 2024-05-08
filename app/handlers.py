from aiogram import F, Router
from aiogram.filters.command import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keyboards as kb

router = Router()

class Reg(StatesGroup):
    name = State()
    number = State()


# Хэндлер на команду /start
@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(f"Привет {message.from_user.first_name}", reply_markup=kb.main)


# сравнивет
@router.message(F.text == 'Как дела?')
async def cmd_start(message: Message):
    await message.reply(f"Хорошо {message.from_user.first_name}", reply_markup=kb.settings)


# Отправляет фото
@router.message(Command('get_photo'))
async def cmd_start(message: Message):
    await message.reply_photo(photo='https://unsplash.com/photos/man-person-standing-between-tall-trees-F_-0BxGuVvo',
                              caption='This picture is very simple')


@router.callback_query(F.data == 'catalog')
async def cmd_catalog(callback: CallbackQuery):
    await callback.answer('Вы выбрали каталог', show_alert=True)
    await callback.message.answer('Ты че пёс?')


@router.message(Command('reg'))
async def cmd_reg_one(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer('Введите ваше имя')


@router.message(Reg.name)
async def cmd_reg_two(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.number)
    await message.answer('Введите ваш номер')


@router.message(Reg.number)
async def cmd_reg_three(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    data = await state.get_data()
    await message.answer(f'Регистрация пройдена успешно\nИмя:{data["name"]}\nНомер:{data["number"]}')
    await state.clear()