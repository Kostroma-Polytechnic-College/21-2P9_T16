from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from state.aStates import RegisterState
from keyboards.register_kb import IlKeyBoard, SpecKeyBoard

async def register_name(message: Message, state: FSMContext):
    if message.text:
        if len(message.text) <= 15: 
            await message.answer(text=f"Вас зовут, {message.text}?", reply_markup=IlKeyBoard())
            await state.update_data(name=message.text)
            await state.set_state(RegisterState.kbNameState)
        else:
            await message.answer(text="Имя не должно превышать 15 символов. Придумайте другое имя.")
            await state.set_state(RegisterState.regNameState)

async def select_name(call: CallbackQuery, state: FSMContext):
    await call.answer()
    if call.data == 'Да':
        await call.message.edit_reply_markup(reply_markup=None)
        data = await state.get_data()
        name = data.get("name")
        await call.message.answer(f"Привет, {name}!")
        await call.message.answer("На кого ты хочешь поступить?",reply_markup=SpecKeyBoard())
        await state.set_state(RegisterState.kbSpecState)
    elif call.data == 'Нет':
        await call.message.edit_reply_markup(reply_markup=None)
        await call.message.answer('Введите имя')
        await state.set_state(RegisterState.regNameState)
