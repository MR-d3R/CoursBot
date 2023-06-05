import asyncio
import logging
import some, os
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.types import (
    ReplyKeyboardRemove,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


with open(os.path.dirname(os.path.realpath(__file__)) + "/token_here.txt") as file:
    TOKEN = file.readline().strip()

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота

bot = Bot(token=f"{TOKEN}")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Привет! Напиши, что хочешь сгенерировать, и получи картинку!\nНецензурные слова и слова 18+ бот не принимает."
    )


@dp.message()
async def send_answer(message: types.Message):
    user_input = message.text
    await bot.send_message(message.from_user.id, f"Ожидайте...")
    link = some.image_generator(user_input)
    await bot.send_message(message.from_user.id, f"Вот ваш {user_input}, {link}")
    await bot.send_message(
        message.from_user.id,
        f"Чтобы сгенерировать слюдующее изображение, пришлите слюдующий запрос)",
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
