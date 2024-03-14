from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyword = ReplyKeyboardMarkup(
    keyboard=[

        [KeyboardButton(text="Button 1"), KeyboardButton(text="Button 2")],
        [KeyboardButton(text="Button 3"), KeyboardButton(text="Button")],
    ], resize_keyboard=True
)b