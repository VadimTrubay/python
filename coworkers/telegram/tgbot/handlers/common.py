from aiogram import Dispatcher, types
from aiogram.dispatcher import filters, FSMContext
from aiogram.types.reply_keyboard import ReplyKeyboardRemove

from tgbot.database.models.fields import Client
from tgbot.keyboards import reply_kb
from tgbot.texts import texts
from tgbot.filters.create_order_filters import ListStateFilter
from tgbot.FSMStates.client_st import FSMRegistration
from tgbot.middlewares.common_mw import AdminsIDs
import tgbot.utils.helpers_for_hendlers as hfh

async def back(message: types.Message, state: FSMContext, db_worker):
    data = await state.get_data()
    state_group, return_hendlers = data.get('hendlers_dct', (None, {}))
    previous_name = None
    if state_group:
        await hfh.delete_state_value(state)
        previous_name = await state_group.previous()
        await hfh.delete_state_value(state)
    back_hendler = return_hendlers.get(previous_name, no_command if previous_name else no_state)
    # print(await state.get_data())
    await back_hendler(message, state=state, db_worker=db_worker)

def get_full_name(first_name, last_name):
    return f'{first_name} {last_name}' if last_name else first_name

async def known_start(message: types.Message):
    await message.answer('Hello')
    # id_con = message.from_user.id
    # contact = contacts[id_con]
    # await message.answer(f'Hello {contact.firstname} {contact.lastname}')

async def registration(message:types.Message, state:FSMContext):
    if await filters.IsSenderContact(True).check(message):
        client = Client(
            message.from_user.id,
            message.from_user.first_name,
            message.from_user.last_name,
            message.from_user.username,
            message.contact.phone_number
        )
        client.insert_to_db()
        # contacts[client.id] = client
        name = get_full_name(client.first_name, client.last_name)
        await message.answer(f'{name}, Вас зареєстровано успішно', reply_markup=reply_kb.make_main_kb())
        await state.finish()
    else:
        await message.answer('Вибачте, це не ваш контакт')

async def wrong_command(update: types.Message|types.CallbackQuery, *args):
    await update.answer('Неправильна команда')

async def no_state(update: types.Message|types.CallbackQuery, *args):
    await update.answer('Скористайтесь меню', reply_markup=reply_kb.make_main_kb())

@hfh.need_admin()
async def send_link_to_admin(message: types.Message, admin):
    await message.answer(
        f'Щоб написати адміну перейдіть за посиланням:\n{texts.TG_LINK}{admin}'
        )
    
def hendlers_registration(dp: Dispatcher):
    # dp.register_message_handler(back, filters.Text('Назад'), state='*')
    dp.register_message_handler(known_start, commands='start')
    dp.register_message_handler(registration,content_types='contact', state=FSMRegistration.contact)
    dp.register_message_handler(send_link_to_admin, filters.Text(equals='Написати адміну'))
    # dp.register_message_handler(no_command)
    
    dp.register_message_handler(no_state, state=None)
    dp.register_callback_query_handler(wrong_command, state='*')
    dp.register_message_handler(wrong_command, state='*')

