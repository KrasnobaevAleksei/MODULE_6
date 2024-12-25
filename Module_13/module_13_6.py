from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = '7653586252:AAFTKkRUCWhbcMvYqOuZh2VwxI9_TjFhdxI'
bot = Bot(token = api)
dp = Dispatcher(bot, storage= MemoryStorage())

# Создание клавиатуры
kb = ReplyKeyboardMarkup()
#кнопки клавиатуры обычные
button = KeyboardButton(text= "Рассчитать")
button2= KeyboardButton(text= "Информация", request_contact = True)
# подгонка клавиатуры под размер устройства
kb.resize_keyboard = True
kb.one_time_keyboard = True

kb.row(button,button2) #Добавляет построчно каждый add с новой строки
                # еще есть kb.row, kb.insert


#Создаем инлайн клавиатуру с двумя кнопками callback_data - по этой метке
kb1 = InlineKeyboardMarkup()
button = InlineKeyboardButton(text= 'Рассчитать норму калорий', callback_data ='calories')
#callback_data - это типа ID кнопки
button_2= InlineKeyboardButton(text= 'Формулы расчёта', callback_data ='formulas')
#callback_data - это типа ID кнопки
kb1.add(button, button_2)

@dp.message_handler(text="Рассчитать")
async def main_menu(message):
    await message.answer('Выберите опцию', reply_markup = kb1)#reply_markup = kb - показывает клавиатуру

@dp.callback_query_handler(text = 'formulas')# Реагирует на кнопку инлайн клавиатуры
# button2 где callback_data ='formulas'
async def get_formulas(call):# название может быть любое, но здесь специально, чтобы понимали, что идет вызов кнопки
    await call.message.answer("Калории =  10 * вес + 6.25 * рост - 5 * возраст + 5")
    # await call.answer()#нужно если после кнопки происходит еще один вызов какой-нибудь

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет', reply_markup = kb)#reply_markup = kb - показывает клавиатуру

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    #Считывает введённое сообщение если равно переменной text
    # тогда выводит сообщение из answer и считывает введённое значение(текст)
@dp.callback_query_handler(text="calories")
async def set_age(call):
    await call.message.answer('Введите свой возраст')
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
        itog =  10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5
    except ValueError as e:
        await message.answer("O, no")
        await state.finish()

    # Выводит текст в телегу
    await message.answer(itog)
    # Ожидает ввода данных от пользователя
    await state.finish()

@dp.message_handler()
async def all_message(message):
    await message.answer( 'Введите команду /start, чтобы начать общение.')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True )