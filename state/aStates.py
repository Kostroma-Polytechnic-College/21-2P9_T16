from aiogram.fsm.state import StatesGroup, State

class RegisterState(StatesGroup):

    regNameState = State()
    kbNameState = State()
    regSpecState = State()
    kbSpecState = State()
    cnfSpecState = State()
    cnfKbSpecState = State()