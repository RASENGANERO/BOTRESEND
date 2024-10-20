from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

generate_more_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Генерировать еще", callback_data='generate_more')]
    ]
)