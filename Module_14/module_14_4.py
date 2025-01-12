from aiogram import Bot, Dispatcher,executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State,StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
import asyncio
import config
from crud_functions import *

#initiate_db()
products=get_all_products()

api=config.API

bot=Bot(token=api)

dp=Dispatcher(bot,storage=MemoryStorage())

kb=ReplyKeyboardMarkup(resize_keyboard=True)
buttton_r=KeyboardButton(text="Рассчитать")
buttton_i=KeyboardButton(text="Информация")
buttton_b=KeyboardButton(text="Купить")
kb.add(buttton_r,buttton_i)
kb.add(buttton_b)

inline_kb=InlineKeyboardMarkup()
inline_button_r=InlineKeyboardButton(text="Рассчитать норму калорий", callback_data='calories')
inline_button_f=InlineKeyboardButton(text="Формулы расчёта", callback_data='formulas')
inline_kb.add(inline_button_r,inline_button_f)

inline_kb_b=InlineKeyboardMarkup()
inline_button_1=InlineKeyboardButton(text="Product1", callback_data='product_buying')
inline_button_2=InlineKeyboardButton(text="Product2", callback_data='product_buying')
inline_button_3=InlineKeyboardButton(text="Product3", callback_data='product_buying')
inline_button_4=InlineKeyboardButton(text="Product4", callback_data='product_buying')
inline_kb_b.add(inline_button_1,inline_button_2,inline_button_3,inline_button_4)


class UserState(StatesGroup):
    age=State()
    growth=State()
    weight=State()

@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.",reply_markup=kb)

@dp.message_handler(text=["Рассчитать"])
async def main_menu(message):
    await message.answer("Выберите опцию:",reply_markup=inline_kb)

@dp.message_handler(text=["Купить"])
async def get_buying_list(message):
    for product in products:
        await message.answer(f"Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}")
        with open(f"{product[0]}.jpeg",'rb') as img:
            await message.answer_photo(img) 
    await message.answer("Выберите продукт для покупки:",reply_markup=inline_kb_b)

@dp.callback_query_handler(text=["product_buying"])
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()

@dp.callback_query_handler(text=["formulas"])
async def get_formulas(call):
    await call.message.answer("10 х вес (кг) + 6,25 х рост (cм) – 5 х возраст (г) – 161")
    await call.answer()

@dp.callback_query_handler(text=["calories"])
async def set_age(call):
    await call.message.answer("Введите свой возраст:")
    await call.answer()
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data=await state.get_data()
    c=10*float(data['weight'])+6.25*float(data['growth'])-5*float(data['age'])-161
    await message.answer(f"Ваша норма калорий: {c}")
    await state.finish()

@dp.message_handler()
async def all_massages(message):
    await message.answer("Введите команду /start, чтобы начать общение.")

if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True)