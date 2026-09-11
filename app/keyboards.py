from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

# ------------------------- КНОПКИ ------------------------
reply_menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Каталог"), KeyboardButton(text="Корзина")],
    [KeyboardButton(text="Поддержка")]
], resize_keyboard=True, input_field_placeholder="выберите из пункта ниже")

inline_catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="ChatGPT", callback_data="gpt_chatgpt")],
    [InlineKeyboardButton(text="Claude (Anthropic)", callback_data="gpt_claude")],
    [InlineKeyboardButton(text="Gemini (Google)", callback_data="gpt_gemini")],
    [InlineKeyboardButton(text="Grok (xAI)", callback_data="gpt_grok")],
    [InlineKeyboardButton(text="Deepseek", callback_data="gpt_deepseek")],
    [InlineKeyboardButton(text="Chinese (Китайские)", callback_data="gpt_chinese")]
])

# -----------------------------------------------------------------

# -------------------- МОДЕЛИ НЕЙРОНОК --------------------

async def cmd_chatgpt():
    chatgpt = ["gpt-5.5", "gpt-5.6-luna", "gpt-5.6-terra", "gpt-5.6-sol", "gpt-6-astra"]
    keyboard = InlineKeyboardBuilder()
    for gpt in chatgpt:
        keyboard.add(InlineKeyboardButton(text=gpt.upper(), callback_data=gpt))
    keyboard.add(InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_catalog"))
    return keyboard.adjust(2).as_markup()

async def cmd_claude():
    cloude = ["claude-haiku-4-5", "claude-sonnet-4-6", "claude-sonnet-5", "claude-opus-4-6", "claude-opus-4-7", "claude-opus-4-8", "claude-opus-5", "claude-fable-5", "claude-fable-5.1"]
    keyboard = InlineKeyboardBuilder()
    for gpt in cloude:
        keyboard.add(InlineKeyboardButton(text=gpt.upper(), callback_data=gpt))
    keyboard.add(InlineKeyboardButton(text="⬅️ ⬅️ Назад", callback_data="back_to_catalog"))
    return keyboard.adjust(2).as_markup()

async def cmd_gemini():
    gemini = ["gemini-3.1-pro", "gemini-3.5-flash", "gemini-3.6-flash", "gemini-3.7-flash", "gemini-3.8-flash"]
    keyboard = InlineKeyboardBuilder()
    for gpt in gemini:
        keyboard.add(InlineKeyboardButton(text=gpt.upper(), callback_data=gpt))
    keyboard.add(InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_catalog"))
    return keyboard.adjust(2).as_markup()

async def cmd_grok():
    grok = ["grok-4.5", "grok-4.6"]
    keyboard = InlineKeyboardBuilder()
    for gpt in grok:
        keyboard.add(InlineKeyboardButton(text=gpt.upper(), callback_data=gpt))
    keyboard.add(InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_catalog"))
    return keyboard.adjust(2).as_markup()

async def cmd_deepseek():
    deepseek = ["deepseek-v4-flash", "deepseek-v4-pro"]
    keyboard = InlineKeyboardBuilder()
    for gpt in deepseek:
        keyboard.add(InlineKeyboardButton(text=gpt.upper(), callback_data=gpt))
    keyboard.add(InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_catalog"))
    return keyboard.adjust(2).as_markup()

async def cmd_chinese():
    chinese = ["mimo-v2.5", "mimo-v2.5-pro", "kimi-k2.7-code", "minimax-m3", "glm-5-turbo", "glm-5.2", "glm-5.3-flash", "glm-5.3", "hy4-preview", "qwen3.8-flash", "qwen3.8-max", "kimi-k3"]
    keyboard = InlineKeyboardBuilder()
    for gpt in chinese:
        keyboard.add(InlineKeyboardButton(text=gpt.upper(), callback_data=gpt))
    keyboard.add(InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_catalog"))
    return keyboard.adjust(2).as_markup()

# -----------------------------------------------------------------------------------------------------