from aiogram import Bot, Dispatcher, executor, types
# из блока работы с памятью
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

# Токен
api = ""
# Объект бота
bot = Bot(token = api)
#
dp = Dispatcher(bot, storage= MemoryStorage())

# Пишем в строке в тееге /start(Команда) тогда обрабатывается
@dp.message_handler(commands='start')
async def start_message(message):
    print('Привет! Я бот помогающий твоему здоровью.' )
# Выводится сообщение когда в телеге пришло
# сообщение обрабатывает все сообщения входящие
@dp.message_handler()
async def all_message(message):
    print( 'Введите команду /start, чтобы начать общение.')
# Запускаем
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates= True)