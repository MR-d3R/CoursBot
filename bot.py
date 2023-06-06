import asyncio
import logging
import some, os
import data_emoji

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import FSInputFile


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
    photo = FSInputFile(f"hello.jpg")
    await bot.send_photo(
        message.from_user.id,
        photo,
    )
    await message.answer(
        f"{data_emoji.emojDiamont}Привет!{data_emoji.emojDiamont}\n Напиши, что хочешь сгенерировать, и получи картинку!"
        f"\n\nНецензурные слова и слова 18+ бот не принимает."
    )


@dp.message()
async def send_answer(message: types.Message):
    try:
        user_input = message.text
        await bot.send_message(message.from_user.id, f"{data_emoji.emojiZont}Ожидайте...{data_emoji.emojiZont}")
        file_name = some.image_generator(user_input)
        photo = FSInputFile(f"{file_name}")
        await bot.send_photo(
            message.from_user.id,
            photo,
            caption=f"{data_emoji.emojMolnia}Результат изображения по запросу: {user_input} {data_emoji.emojMolnia}",

        )

        os.remove(file_name)

        await bot.send_message(
            message.from_user.id,
            f"Чтобы сгенерировать следующее изображение, пришлите следующий запрос)",
        )
    except:
        await bot.send_message(
            message.from_user.id,
            f"Запрос содержит нецензурные слова... Попробуй еще раз",
        )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())