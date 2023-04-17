import asyncio
import logging
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

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="5499334014:AAFpV801u920C7IQm7HFw_aDIjWaORhva1s")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


# @dp.message(Command("dice"))
# async def cmd_dice(message: types.Message, bot: Bot):
#     await bot.send_dice(-100123456789, emoji=DiceEmoji.DICE)


@dp.message(Command("dice"))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎲")


# @dp.message(Command("special_buttons"))
# async def cmd_special_buttons(message: types.Message):
#     builder = ReplyKeyboardBuilder()
#     # метод row позволяет явным образом сформировать ряд
#     # из одной или нескольких кнопок. Например, первый ряд
#     # будет состоять из двух кнопок...
#     builder.row(
#         types.KeyboardButton(text="Запросить геолокацию", request_location=True),
#         types.KeyboardButton(text="Запросить контакт", request_contact=True),
#     )
#     # ... второй из одной ...
#     builder.row(
#         types.KeyboardButton(
#             text="Создать викторину",
#             request_poll=types.KeyboardButtonPollType(type="quiz"),
#         )
#     )
#     # ... а третий снова из двух
#     builder.row(
#         types.KeyboardButton(
#             text="Выбрать премиум пользователя",
#             request_user=types.KeyboardButtonRequestUser(
#                 request_id=1, user_is_premium=True
#             ),
#         ),
#         types.KeyboardButton(
#             text="Выбрать супергруппу с форумами",
#             request_chat=types.KeyboardButtonRequestChat(
#                 request_id=2, chat_is_channel=False, chat_is_forum=True
#             ),
#         ),
#     )
#     # WebApp-ов пока нет, сорри :(

#     await message.answer(
#         "Выберите действие:",
#         reply_markup=builder.as_markup(resize_keyboard=True),
#     )


@dp.message(Command("inline_url"))
async def cmd_inline_url(message: types.Message, bot: Bot):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="GitHub", url="https://github.com"))
    builder.row(
        types.InlineKeyboardButton(
            text="Оф. канал Telegram", url="tg://resolve?domain=telegram"
        )
    )

    # Чтобы иметь возможность показать ID-кнопку,
    # У юзера должен быть False флаг has_private_forwards
    user_id = 1234567890
    chat_info = await bot.get_chat(user_id)
    if not chat_info.has_private_forwards:
        builder.row(
            types.InlineKeyboardButton(
                text="Какой-то пользователь", url=f"tg://user?id={user_id}"
            )
        )

    await message.answer(
        "Выберите ссылку",
        reply_markup=builder.as_markup(),
    )


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

# import asyncio
# import logging

# from aiogram import Bot, Dispatcher, Router, types

# # from aiogram import *
# from aiogram.filters import Command
# from aiogram.types import Message

# # Bot token can be obtained via https://t.me/BotFahter
# TOKEN = "5499334014:AAFpV801u920C7IQm7HFw_aDIjWaORhva1s"

# # All handlers should be attached to the Router (or Dispatcher)
# router = Router()


# @router.message(Command(commands=["start"]))
# async def command_start_handler(message: Message) -> None:
#     """
#     This handler receive messages with `/start` command
#     """
#     # Most event objects have aliases for API methods that can be called in events' context
#     # For example if you want to answer to incoming message you can use `message.answer(...)` alias
#     # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
#     # method automatically or call API method directly via
#     # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
#     await message.answer(f"Hello, <b>{message.from_user.full_name}!</b>")


# @router.message()
# async def echo_handler(message: types.Message) -> None:
#     """
#     Handler will forward received message back to the sender

#     By default, message handler will handle all message types (like text, photo, sticker and etc.)
#     """
#     try:
#         # Send copy of the received message
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         # But not all the types is supported to be copied so need to handle it
#         await message.answer("Nice try!")


# async def main() -> None:
#     # Dispatcher is a root router
#     dp = Dispatcher()
#     # ... and all other routers should be attached to Dispatcher
#     dp.include_router(router)

#     # Initialize Bot instance with a default parse mode which will be passed to all API calls
#     bot = Bot(TOKEN, parse_mode="HTML")
#     # And the run events dispatching
#     await dp.start_polling(bot)


# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO)
#     asyncio.run(main())
