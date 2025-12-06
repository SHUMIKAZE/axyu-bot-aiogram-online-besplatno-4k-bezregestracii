import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart

# 1. Вставь сюда свой токен
TOKEN = '7062578652:AAF7IvPhN6YYUAz4Kt6UDaYEjHtv7deo5ig'
TOKEN = '7062578652:AAGE0rZScE6mZYmXvxWuTjwL5yvGvdnRN_c'

# Включаем логирование, чтобы видеть в консоли, что происходит
logging.basicConfig(level=logging.INFO)

# 2. Создаем объекты бота и диспетчера
# Диспетчер (dp) - это "уши" бота, он слушает сообщения
bot = Bot(token=TOKEN)
dp = Dispatcher()

# 3. Обработчик команды /start
# Когда пользователь нажмет Start, сработает эта функция
@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    # message.from_user.first_name - это имя того, кто написал
    reply_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="выяснить"), KeyboardButton(text="милостыня")],
        ],
        resize_keyboard=True,
    )
    inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="выяснить", callback_data="info_btn"), InlineKeyboardButton(text="милостыня", callback_data="help_btn")],
    ])
    await message.answer(
        f"Привет, {message.from_user.first_name}!\n\n Ха, лох ебаный! Ты не {message.from_user.first_name}, ты долбаеб!",
        reply_markup=reply_keyboard,
    )
    await message.answer(
        "Или используй инлайн кнопки:",
        reply_markup=inline_keyboard,
    )

@dp.message(lambda message: message.text and message.text.lower() in ["выяснить", "неформация"])  # compatible filter
async def info_handler(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="негр", callback_data="help_btn")],
    ])
    await message.answer(
        "ща все поясню:\n- Автор: я\n- Версия: режиссерская\n\nклацни \"негр\" если нужна помощь.",
        reply_markup=keyboard,
    )

@dp.message(lambda message: message.text and message.text.lower() in ["милостыня", "негр"])  # compatible filter
async def help_handler(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="неформация", callback_data="info_btn")],
    ])
    await message.answer(
        "милостыня:\n- только попробуй клацнуть, нотесли клацнешь \"неформация\" то получишь неформацию.\n- написи любую хуйнб для эхо",
        reply_markup=keyboard,
    )

# Обработчики инлайн кнопок
@dp.callback_query(lambda c: c.data == "info_btn")
async def info_callback(callback_query: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="негр", callback_data="help_btn")],
    ])
    await callback_query.message.edit_text(
        "ща все поясню:\n- Автор: я\n- Версия: режиссерская\n\nклацни \"негр\" если нужна помощь.",
        reply_markup=keyboard,
    )
    await callback_query.answer()

@dp.callback_query(lambda c: c.data == "help_btn")
async def help_callback(callback_query: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="неформация", callback_data="info_btn")],
    ])
    await callback_query.message.edit_text(
        "милостыня:\n- только попробуй клацнуть, нотесли клацнешь \"неформация\" то получишь неформацию.\n- написи любую хуйнб для эхо",
        reply_markup=keyboard,
    )
    await callback_query.answer()

# 4. Обработчик любого текста (Эхо)
# Сработает, если это не команда, а просто текст
@dp.message()
async def echo_answer(message: types.Message):
    # Мы просто отправляем тот же текст обратно
    if message.text == "СУПЕР СЕКРЕТНЫЙ МАССАЖ":
        await message.answer("О, ты знаешь секретный пароль! Поздравляю, ты получил доступ к секретной информации:")
        await message.answer(f"<span class='tg-spoiler'>ХАХАХАХА ТЫ ПОПАЛ!!! ТЕПЕРЬ ТВОЙ АЙПИ У МЕНЯ!!!!!</span>", parse_mode="HTML")
        #await message.answer("<tg-spoiler>ХАХАХАХА ТЫ ПОПАЛ!!! ТЕПЕРЬ ТВОЙ АЙПИ У МЕНЯ!!!!!</tg-spoiler>")
    else:
        await message.answer(f"В смысле блять '{message.text}'? Ты охуел?")


# 5. Функция запуска
async def main():
    print("Бот запущен!")
    # start_polling - бот постоянно спрашивает у Telegram: "Есть новые сообщения?"
    await dp.start_polling(bot)

# Эта конструкция запускает код, только если мы запускаем файл напрямую
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")