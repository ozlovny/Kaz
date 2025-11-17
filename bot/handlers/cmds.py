from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.utils.deep_linking import decode_payload

from bot import keyboards
from bot.utils import text
from bot.utils.cryptopay import crypto
import main

async def cmd_start(message: Message):
    """Обработчик команды start"""
    if not main.db.users_exists(message.from_user.id):
        main.db.add_user(message.from_user.id)
    main.db.set_active(message.from_user.id)
    args = message.get_args()  # получаем некие args с сообщения
    if args is not None and args != "":  # проверяем есть ли они вообще
        id = decode_payload(args)  # расшифровываем айди
        if int(id) == message.from_user.id:  # сравниваем
            if main.db.have_check(message.from_user.id):
                check_id = main.db.get_check_id(message.from_user.id)
                check = await crypto.get_checks(check_ids=check_id)
                await message.answer("Получите ваши средства", reply_markup=keyboards.functional.create_url_button(check.bot_check_url))
                main.db.remove_check(check_id)
        else:
            await message.answer("Это не для вас")
    else:
        await message.answer(text.get_profile(message.from_user.id, message.from_user.username),
                             parse_mode='html', reply_markup=keyboards.start_keyboards.profile_keyboard)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=['start'])
