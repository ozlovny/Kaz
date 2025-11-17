from bot.utils import cryptopay

import string, random, main

links = """<b><a href="https://t.me/">Основной Канал</a> | <a href="https://t.me/">Наш Чат</a> | <a href="https://t.me/">Техническая Поддержка</a></b>"""
async def get_admin_menu_text(): 
    return f"""Админское меню: 
CryptoBot 
USDT  
Доступно: {round(dict(await cryptopay.get_balance())['USDT'], 3)} 
В ожидании: {round(dict(await cryptopay.get_hold())['USDT'], 3)} 
TON 
Доступно: {round(dict(await cryptopay.get_balance())['TON'], 3)} 
В ожидании: {round(dict(await cryptopay.get_hold())['TON'], 3)}"""



def get_admin_given(amount, asset):
    return f"""<blockquote><b>Сумма в размере {amount} {asset}! будет зачислена администрацией вручную!</b></blockquote>
<blockquote><b>Играй заново и испытай свою удачу!</b></blockquote>"""

def get_button_given(amount, asset):
    return f"""<blockquote><b>Победитель выиграл {amount} {asset}! Заберите выигрыш по кнопке ниже!</b></blockquote>
<blockquote><b>Играй заново и испытай свою удачу!</b></blockquote>"""

def get_transfer_given(amount, asset):
    return f"""<blockquote><b>На баланс победителя была зачислена сумма в размере {amount} {asset}</b></blockquote>
<blockquote><b>Играй заново и испытай свою удачу!</b></blockquote>"""

def rnd_id():
    al = string.ascii_letters
    txt = ""
    for i in range(1, 10):
        txt += random.choice(al)
    return txt

def get_stake(amount, asset, comment, name):
    return f"""<b>[💎]Новая ставка</b>
    
<blockquote><b>Никнейм игрока: {name}</b></blockquote>
<blockquote><b>Сумма ставки: {round(amount, 3)} {asset}</b></blockquote>
<blockquote><b>Ставка игрока: {comment}</b></blockquote>

<b>Желаем удачи!</b>"""

def get_win_text(amount, asset, type, additional_comment = None, is_less_dol = False, is_less = False):
    if type != 'def':
        start = "<b>" + additional_comment + "</b>"
    else:
        start = f"<b>Победа! Ваша ставка оказалась выигрышной: {additional_comment}</b>"
    if is_less:
        return start + "\n\n" + get_admin_given(amount, asset) + f"\n\n{links}"
    
    if is_less_dol:
        return start + "\n\n" + get_button_given(amount, asset) + f"\n\n{links}"
    else:
        return start + "\n\n" + get_transfer_given(amount, asset) + f"\n\n{links}"
    
def get_lose_text(additional_comment, type):
    if type != 'def':
        start = "<b>" + additional_comment + "</b>" + "\n\n" + "<blockquote><b>Играй заново и испытай свою удачу!</b></blockquote>" + f"\n\n{links}" 
        return start
    return f"""<b>Проигрыш! Ваша ставка оказалась проигрышной: {additional_comment}.

<blockquote>Играй заново и испытай свою удачу!</blockquote></b>""" + f"\n\n{links}"

def get_invalid_text(name, type = 'default'):
    if type == 'admin': addiction = "Возврат денежных средств будет выполнен администрацией вручную."
    elif type == "button": addiction = "Заберите деньги по кнопке ниже."
    else: addiction = "Был совершён возврат денежных средств."
    return f"""<b>[❌] Ошибка!</b>

<b>{name} - Вы</b> <i>забыли дописать комментарий к оплате или ошиблись при его написании.</i>
<i><b><u>{addiction}</u></b></i>

<blockquote>Комиссия составляет: 10%.</blockquote>
"""

def get_bowling_text(v):
    if v == 6: return "боулинг страйк"
    elif v == 5: return "боулинг 1"
    elif v == 4: return "боулинг 2"
    elif v == 3: return "боулинг 3"
    elif v == 2: return "боулинг 5"
    elif v == 1: return "боулинг 6"

def get_profile(id, name):
    return f"""<b>👤 Личный кабинет</b>

<b>UN:</b> {name}
<b>ID:</b> <code>{id}</code>
<b>Всего игр</b>: {main.db.get_total(id)}

<a href="https://t.me/">ScamCasino</a> - лучшие в телеграм"""