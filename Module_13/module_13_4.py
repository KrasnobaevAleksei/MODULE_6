
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Bot, Dispatcher, executor, types
# из блока работы с памятью
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = '7653586252:AAFTKkRUCWhbcMvYqOuZh2VwxI9_TjFhdxI'
bot = Bot(token = api)
dp = Dispatcher(bot, storage= MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    #Считывает введённое сообщение если равно переменной text
    # тогда выводит сообщение из answer и считывает введённое значение(текст)
@dp.message_handler(text="Calories")
async def set_age(message):
    await message.answer('Введите свой возраст')
    #Просим пользователя ввести возраст и
    # ожидаем ввода возраста в
    # объект age класса UserState
    await UserState.age.set()

@dp.message_handler(state= UserState.age)
async def set_growth(message, state):
    # обновляет данные в состоянии age
    # на написанное юзером сообщение
    await state.update_data(age= message.text)
    # Выводит текст в телегу
    await message.answer('Введите свой рост')
    # Ожидает ввода данных от пользователя
    await UserState.growth.set()

@dp.message_handler(state= UserState.growth)
async def set_growth(message, state):
    # обновляет данные в состоянии age
    # на написанное юзером сообщение
    await state.update_data(growth= message.text)
    # Выводит текст в телегу
    await message.answer('Введите свой вес')
    # Ожидает ввода данных от пользователя
    await UserState.weight.set()

@dp.message_handler(state= UserState.weight)
async def send_calories(message, state):
    # обновляет данные в состоянии age
    # на написанное юзером сообщение
    await state.update_data(weight= message.text)
    #запоминаем все ранне введенные состояния
    data = await state.get_data()
    try:
        itog =  10 * int(data['weight']) + 6.25 * int(data['growth']) + 5 * int(data['age']) + 5
    except ValueError as e:
        await message.answer("O, NO")
        await state.finish()

    # Выводит текст в телегу
    await message.answer(itog)
    # Ожидает ввода данных от пользователя
    await state.finish()


# Запускаем
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates= True)