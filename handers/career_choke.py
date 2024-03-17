from aiogram import types, F, Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from less3.keybors.prof_kiborg import make_row_keyboard



router = Router()


available_prof_names = ["Разработчик", "Аналитик", "Тестировщик"]
available_prof_grades = ["Junior", "Middle", "Senior"]

#Хэндлер на команду /prof
@router.message(Command('prof'))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f"Привет, {name}, выбери свою профессию", reply_markup=make_row_keyboard(available_prof_names))

