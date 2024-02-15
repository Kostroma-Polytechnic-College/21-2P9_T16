from aiogram import Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from state.aStates import RegisterState , State
from keyboards.register_kb import IlKeyBoard,SpecKeyBoard
import asyncio


async def speciality_confkb(call: CallbackQuery, state: FSMContext):
    await call.answer()

    if call.data == 'Да':
        await call.message.edit_reply_markup(reply_markup=None)
        await call.message.answer('Пока что конец!')
        await state.clear()
    elif call.data == 'Нет':
        await call.message.edit_reply_markup(reply_markup=None)
        await call.message.answer('Выберите другую специальность',reply_markup=SpecKeyBoard())
        await state.set_state(RegisterState.kbSpecState)
