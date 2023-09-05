from dotenv import dotenv_values
from aiogram import Bot, Dispatcher, types, executor

from py_logger import get_logger
from repository.ddl import set_user, is_exist_user
from repository.ddl import get_procedures

"""Settings"""
config = dotenv_values(".env")
CLIENT_TOKEN = config['CLIENT_TOKEN']

logger = get_logger(__name__)

bot = Bot(CLIENT_TOKEN)
dp = Dispatcher(bot)

"""Клавиатури та кнопки"""
start_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
procedures = types.KeyboardButton('Процедуры')
prices = types.KeyboardButton('Цены')
consultation = types.KeyboardButton('Консультация')
record = types.KeyboardButton('Записаться на прием')
start_kb.add(procedures, consultation).add(prices, record)


@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    """Функція обробки команди /start"""
    if not is_exist_user(message.from_user.id):
        set_user(user_id=message.from_user.id, first_name=message.from_user.first_name,
                 last_name=message.from_user.last_name)
    info = f'Добро пожаловать, <b>{message.from_user.first_name}</b>\n' \
           f'Вы находитесь в чат-боте\n<em><b>Доктора Вороновского</b></em>\n'
    await message.answer(text=info, parse_mode='HTML', reply_markup=start_kb)
    await message.delete()


@dp.message_handler(commands=['procedures'])
@dp.message_handler(lambda message: 'Процедуры' in message.text)
async def procedures_cmd(message: types.Message):
    """Функція обробки команди /procedures"""
    all_procedures = get_procedures()
    for proced in all_procedures:
        await bot.send_photo(chat_id=message.from_user.id, photo=proced.image_url, caption=f'<b>{proced.title}</b>',
                             parse_mode='HTML', reply_markup=types.InlineKeyboardMarkup(row_width=3)
                             .add(types.InlineKeyboardButton(text='Подробнее', url=proced.desc_url)))


async def on_startup(_):
    """Функція запускається при старті бота"""
    logger.info('Client VSM Bot start polling...')


async def on_shutdown(_):
    """Функція запускається при завершенні роботи бота"""
    logger.info('Client VSM Bot end polling.')


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
