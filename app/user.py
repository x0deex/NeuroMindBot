from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, CommandObject, Command
from aiogram.fsm.context import FSMContext


import app.keyboards as kb
from app.states import Chating
from app.generators import gpt_text

user = Router()

@user.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Добро пожаловать!", reply_markup=kb.reply_menu)

@user.message(F.text == "Каталог")
async def catalog(message: Message):
    await message.answer("Выберите какую нейросеть хотите использовать:", 
                         reply_markup=kb.inline_catalog)

@user.callback_query(F.data == "back_to_catalog")
async def back_to_catalog(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.edit_text("Выберите какую нейросеть хотите использовать:",
                                     reply_markup=kb.inline_catalog)

@user.callback_query(F.data.startswith("gpt_"))
async def gpt_model(callback: CallbackQuery, state: FSMContext):
    await callback.answer("")
    await state.set_state(Chating.model)
    if callback.data == "gpt_chatgpt":
        gpt_name = "ChatGPT"
        await callback.message.edit_text(f"Теперь выберите какую модель {gpt_name} хотите использовать: ", 
                                      reply_markup=await kb.cmd_chatgpt())

    if callback.data == "gpt_claude":
        gpt_name = "Claude"
        await callback.message.edit_text(f"Теперь выберите какую модель {gpt_name} хотите использовать: ", 
                                      reply_markup=await kb.cmd_claude())

    if callback.data == "gpt_gemini":
        gpt_name = "Gemini"
        await callback.message.edit_text(f"Теперь выберите какую модель {gpt_name} хотите использовать: ", 
                                      reply_markup=await kb.cmd_gemini())
        
    if callback.data == "gpt_grok":
        gpt_name = "Grok"
        await callback.message.edit_text(f"Теперь выберите какую модель {gpt_name} хотите использовать: ", 
                                      reply_markup=await kb.cmd_grok())
        
    if callback.data == "gpt_deepseek":
        gpt_name = "Deepseek"
        await callback.message.edit_text(f"Теперь выберите какую модель {gpt_name} хотите использовать: ", 
                                      reply_markup=await kb.cmd_deepseek())
        
    if callback.data == "gpt_chinese":
        gpt_name = "Chinese(Китайские)"
        await callback.message.edit_text(f"Теперь выберите какую модель {gpt_name} хотите использовать: ", 
                                      reply_markup=await kb.cmd_chinese())
    await state.update_data(gpt_name=gpt_name)

@user.callback_query(Chating.model)
async def gpt_start_answer(callback: CallbackQuery, state: FSMContext, ):
    await callback.answer("")

    data = await state.get_data()
    gpt_name = data.get("gpt_name", "нейросеть")

    model = callback.data
    await state.update_data(model=model)
    await state.set_state(Chating.text)
    await callback.message.edit_text(f"Модель: {gpt_name}\nМодель Версии: {model}\nВведите запрос:")

@user.message(Chating.text)
async def gpt_answer(message: Message, state: FSMContext):
    await state.set_state(Chating.wait)
    data = await state.get_data()
    model = data.get("model")
    response = await gpt_text(message.text, model)
    await message.answer(response)
    await state.clear()

@user.message(Chating.wait)
async def wait_wait(message: Message):
    await message.answer("Ваше сообщение генерируется, подождите")