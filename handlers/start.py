from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from state.aStates import RegisterState , State
import asyncio


async def get_start(message: Message, bot: Bot, state: FSMContext):
    

    sout = """Голос: Кхм-кхм
Вы слышите неуверенное покашливание девушки напротив
Голос: Ваше имя
Вы начинаете потихоньку вспоминать что происходит
Вы закончили 9 классов, и перед вами встал выбор от которого зависит, кем вы будете в жизни, ясно лишь одно, поступать надо в Политех.
Голос: Ваше имя?
Ещё более неуверенная интонация прозвучала в её голосе
Вы: Да, кхм, меня зовут"""
    
    for lite in sout.split('\n'):
        
        await bot.send_message(message.from_user.id, text=lite)
        
        await asyncio.sleep(2/3)

    await state.set_state(RegisterState.regNameState)
    await message.answer(text="Придумайте Имя")