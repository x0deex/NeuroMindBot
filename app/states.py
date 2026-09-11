from aiogram.fsm.state import State, StatesGroup

class Chating(StatesGroup):
    model = State()
    text = State()
    