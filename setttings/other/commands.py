from aiogram import Bot
from aiogram.types import BotCommand


async def set_commands_user(bot: Bot):
    commands = [
        BotCommand(
            command='restart',
            description='Перезагрузка'
        )
    ]
    await bot.set_my_commands(commands)


async def set_commands_admin(bot: Bot):
    commands = [
        BotCommand(
            command='restart',
            description='Перезагрузка'
        ),
        BotCommand(
            command='count_users',
            description='Перезагрузка'
        )
    ]
    await bot.set_my_commands(commands)