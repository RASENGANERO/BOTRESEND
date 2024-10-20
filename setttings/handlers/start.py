from aiogram import types, F
from aiogram.types import FSInputFile
from aiogram.filters import Command

from main import dp, bot, db
from other.generate_image import generate_image, phrases
from keyboards import generate_more_btn
from other import set_commands_user, set_commands_admin
from other import ADMIN_ID

import random
import string
import os


@dp.message(Command('start', 'restart'))
async def start(msg: types.Message):
    if not await db.user_exists(msg.from_user.id):  # if the user is not registered
        await db.add_user(msg.from_user.id)

    if msg.from_user.id in ADMIN_ID:
        await set_commands_admin(bot)
    else:
        await set_commands_user(bot)

    letters = string.ascii_lowercase
    rand_name = ''.join(random.choice(letters) for _ in range(5))
    await generate_image(phrases, img=rand_name)
    try:
        card = FSInputFile(f"img/{rand_name}.png")
        await bot.send_photo(msg.from_user.id,
                             photo=card, caption="<i>Твоя бинго карточка, получите-распишитесь. Зачеркивать секторы "
                                                 "можно в режиме редактирования фото на телефоне или при отправке "
                                                 "фото в телеграме.\n\n"
                                                 "Левел-1: закрыть горизонтальную или вертикальную линию.\n"
                                                 "Левел-2: закрыть диагональ.\n"
                                                 "Левел-3: собрать полный бинго.</i>", reply_markup=generate_more_btn)
        os.remove(f"img/{rand_name}.png")
    except:
        await msg.answer("Извини, произошла ошибка\nПопробуй позже")


@dp.callback_query(F.data.startswith('generate_more'))
async def generate(call: types.CallbackQuery):
    letters = string.ascii_lowercase
    rand_name = ''.join(random.choice(letters) for _ in range(5))
    await generate_image(phrases, img=rand_name)
    try:
        card = FSInputFile(f"img/{rand_name}.png")
        await bot.send_photo(call.from_user.id,
                             photo=card,
                             caption="<i>Твоя бинго карточка, получите-распишитесь. Зачеркивать секторы "
                                     "можно в режиме редактирования фото на телефоне или при отправке "
                                     "фото в телеграме.\n\n"
                                     "Левел-1: закрыть горизонтальную или вертикальную линию.\n"
                                     "Левел-2: закрыть диагональ.\n"
                                     "Левел-3: собрать полный бинго.</i>", reply_markup=generate_more_btn)
        os.remove(f"img/{rand_name}.png")
    except:
        await call.message.answer("Извини, произошла ошибка\nПопробуй позже")


@dp.message(Command('count_users'))
async def count_users(msg: types.Message):
    await msg.answer(f"Количество пользователей: <b>{await db.all_users()}</b>")