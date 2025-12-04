import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

# 1. Вставь сюда свой токен
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
    await message.answer(f"Привет, {message.from_user.first_name}!\n\n Ха, лох ебаный! Ты не {message.from_user.first_name}, ты долбаеб!")

# 4. Обработчик любого текста (Эхо)
# Сработает, если это не команда, а просто текст
@dp.message()
async def echo_answer(message: types.Message):
    # Мы просто отправляем тот же текст обратно
    await message.reply(f"В смысле блять '{message.text}'? Ты охуел?")

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