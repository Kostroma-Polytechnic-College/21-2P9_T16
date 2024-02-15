from aiogram import Dispatcher, Bot, F
from dotenv import load_dotenv
from state.aStates import RegisterState
from aiogram.filters import Command
from utils.commands import set_commands
from handlers.start import get_start
from handlers.register import register_name, select_name
from handlers.spec import speciality_kb
from handlers.confirm_spec import speciality_confkb
from aiogram.fsm.context import FSMContext


import os
import asyncio

load_dotenv()


token = os.getenv('TOKEN')
admin_id = os.getenv('ADMIN_ID')

bot = Bot(token=token, parse_mode='HTML')
dp = Dispatcher()


async def start_bot(bot: Bot):
    await bot.send_message(admin_id, text='Бот за работой)')


dp.startup.register(start_bot)

dp.message.register(get_start, Command(commands='start'))

dp.message.register(register_name, RegisterState.regNameState)

dp.callback_query.register(select_name, RegisterState.kbNameState)

#dp.message.register(speciality_choise, RegisterState.regSpecState)

dp.callback_query.register(speciality_kb, RegisterState.kbSpecState)

#dp.message.register(speciality_conf, RegisterState.cnfSpecState)

dp.callback_query.register(speciality_confkb, RegisterState.cnfKbSpecState)
async def start():
    await set_commands(bot)
    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
