from aiogram import Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from state.aStates import RegisterState , State
from keyboards.register_kb import SpecConfKeyBoard
import asyncio

async def speciality_kb(call: CallbackQuery, state: FSMContext):
    await call.answer()
    if call.data == 'Ar':
        await state.update_data(spec=call.data)
        await call.message.answer(f"Описание специальности Архитектура...",reply_markup= SpecConfKeyBoard())
        await call.message.edit_reply_markup(reply_markup=None)
        await state.set_state(RegisterState.cnfKbSpecState)

    elif call.data == 'Gu':
        await state.update_data(spec=call.data)
        await call.message.answer(f"Описание специальности Гидрогеология...",reply_markup= SpecConfKeyBoard())
        await call.message.edit_reply_markup(reply_markup=None)
        await state.set_state(RegisterState.cnfKbSpecState)
        
    elif call.data == 'Pr':
        await state.update_data(spec=call.data)
        await call.message.edit_reply_markup(reply_markup=None)
        await call.message.answer(f"Описание специальности программист ..",reply_markup= SpecConfKeyBoard())
        await state.set_state(RegisterState.cnfKbSpecState)
                
    elif call.data == 'El':
        await state.update_data(spec=call.data)
        await call.message.answer(f"Описание специальности Электронные ...",reply_markup= SpecConfKeyBoard())
        await call.message.edit_reply_markup(reply_markup=None)
        await state.set_state(RegisterState.cnfKbSpecState)
                        
    elif call.data == 'Ra':
        await state.update_data(spec=call.data)
        await call.message.answer(f"Описание специальности Радиоэлектр...",reply_markup= SpecConfKeyBoard())
        await call.message.edit_reply_markup(reply_markup=None)
        await state.set_state(RegisterState.cnfKbSpecState)
                        
    elif call.data == 'ER':
        await state.update_data(spec=call.data)
        await call.message.answer(f"Описание специальности Разработка элект...",reply_markup= SpecConfKeyBoard())
        await call.message.edit_reply_markup(reply_markup=None)
        await state.set_state(RegisterState.cnfKbSpecState)
                        
    elif call.data == 'MR':
        await state.update_data(spec=call.data)
        await call.message.answer(f"Описание специальности Монтажник...",reply_markup= SpecConfKeyBoard())
        await call.message.edit_reply_markup(reply_markup=None)
        await state.set_state(RegisterState.cnfKbSpecState)
                        
    elif call.data == 'CK':
        await state.update_data(spec=call.data)
        await call.message.answer(f"Описание специальности Консультант...",reply_markup= SpecConfKeyBoard())
        await call.message.edit_reply_markup(reply_markup=None)
        await state.set_state(RegisterState.cnfKbSpecState)