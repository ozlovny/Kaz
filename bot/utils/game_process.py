from aiogram.types import Message
from settings import coefs
from bot.utils import func, text
from settings.constants import knb
import asyncio, random

class GameProcess:
    def __init__(self, amount, asset, coef, user_id, username) -> None:
        self.amount = amount
        self.asset = asset
        self.coef = coef
        self.id = user_id
        self.username = username

    async def basketball_process(self, message: Message, type="goal"):
        msg = await message.answer_dice('🏀')
        await asyncio.sleep(4)
        v = msg.dice.value
        if type == "goal":
            if v == 4 or v == 5:
                self.coef += coefs.BASKET
                await func.winner(message, self.amount, self.asset, self.coef, self.id, self.username, "баскетбол попал")
            else:
                await func.looser(message, "баскетбол не попал")
        else:
            self.coef += coefs.BASKET_MISS
            if v == 3 or v == 1 or v == 2:
                await func.winner(message, self.amount, self.asset, self.coef, self.id, self.username, "баскетбол не попал")
            else:
                await func.looser(message, "баскетбол попал")

    async def footaball_process(self, message: Message, type="goal"):
        msg = await message.answer_dice('⚽')
        await asyncio.sleep(5)
        v = msg.dice.value
        if type == "goal":
            self.coef += coefs.FOOTBALL
            if v == 4 or v == 5 or v == 3:
                await func.winner(message, self.amount, self.asset, self.coef, self.id, self.username, "футбол попал")
            else:
                await func.looser(message, "футбол не попал")
        else:
            self.coef += coefs.FOOTBALL_MISS
            if v == 1 or v == 2:
                await func.winner(message, self.amount, self.asset, self.coef, self.id, self.username, "футбол попал")
            else:
                await func.looser(message, "футбол не попал")

    async def darts_procces(self, message: Message, type='center'):
        msg = await message.answer_dice('🎯')
        await asyncio.sleep(4)
        v = msg.dice.value
        if type == "w":
            self.coef += coefs.DARTS_COLOR
            if v == 3 or v == 5:
                await func.winner(message, self.amount, self.asset, self.coef, self.id, self.username, "дартс белое")
            elif v == 6:
                await func.looser(message, "дартс центр")
            elif v == 1:
                await func.looser(message, "дартс мимо")
            else:
                await func.looser(message, "дартс красное")
        elif type == "r":
            self.coef += coefs.DARTS_COLOR
            if v == 4 or v == 2:
                await func.winner(message, self.amount, self.asset, self.coef, self.id, self.username, "дартс красное")
            elif v == 6:
                await func.looser(message, "дартс центр")
            elif v == 1:
                await func.looser(message, "дартс мимо")
            else:
                await func.looser(message, "дартс белое")
        elif type == "miss":
            self.coef += coefs.DARTS
            if v == 1:
                await func.winner(message, self.amount, self.asset, self.coef, self.id, self.username, "дартс мимо")
            elif v == 3 or v == 5:
                await func.looser(message, "дартс белое")
            elif v == 4 or v == 2:
                await func.looser(message, "дартс красное")
            else:
                await func.looser(message, "дартс центр")
        else:
            self.coef += coefs.DARTS
            if v == 6:
                await func.winner(message, self.amount, self.asset, self.coef, self.id, self.username, "дартс центр")
            elif v == 3 or v == 5:
                await func.looser(message, "дартс белое")
            elif v == 4 or v == 2:
                await func.looser(message, "дартс красное")
            elif v == 1:
                await func.looser(message, "дартс мимо")

    async def dice_procces(self, message: Message, type, n=None):
        msg = await message.answer_dice('🎲')
        await asyncio.sleep(4)
        v = msg.dice.value
        if type == "number":
            self.coef += coefs.DICE_NUMBER
            if n == v:
                await func.winner(message, self.amount, self.asset, self.coef, self.id, self.username, f"Победа! Выпало число {v}.")
            else:
                await func.looser(message, f"Проигрыш! Выпало число {v}. Вы не угадали!")
        elif type == "even":
            self.coef += coefs.DICE
            if v == 2 or v == 4 or v == 6:
                await func.winner(message, self.amount, self.asset, self.coef, self.id, self.username, f"Победа! Выпало число {v}.")
            else:
                await func.looser(message, f"Проигрыш! Выпало число {v}.")
        elif type == "odd":
            self.coef += coefs.DICE
            v = msg.dice.value
            if v == 1 or v == 3 or v == 5:
                await func.winner(message, self.amount, self.asset, self.coef, self.id, self.username, f"Победа! Выпало число {v}.")
            else:
                await func.looser(message, f"Проигрыш! Выпало число {v}.")
        elif type == "more":
            self.coef += coefs.DICE_MORE_LESS
            v = msg.dice.value
            v = msg.dice.value
            if v == 4 or v == 5 or v == 6:
                await func.winner(message, self.amount, self.asset, self.coef, self.id, self.username, f"Победа! Выпало число {v}.")
            else:
                await func.looser(message, f"Проигрыш! Выпало число {v}.")
        elif type == "less":
            self.coef += coefs.DICE_MORE_LESS
            v = msg.dice.value
            v = msg.dice.value
            if v == 1 or v == 2 or v == 3:
                await func.winner(message, self.amount, self.asset, self.coef, self.id, self.username, f"Победа! Выпало число {v}.")
            else:
                await func.looser(message, f"Проигрыш! Выпало число {v}.")

    async def duel_number_process(self, message: Message, num, game='🎲', textes=["первого кубика", "второго кубика"]):
        self.coef += coefs.DUEL
        while True:
            cub1 = await message.answer_dice(game)
            cub2 = await message.answer_dice(game)
            if num == 1:
                msguser = cub1
                msgbot = cub2
            else:
                msguser = cub2
                msgbot = cub1
            await asyncio.sleep(4)
            if msguser.dice.value > msgbot.dice.value:
                if num == 1:
                    await func.winner(message, self.amount, self.asset, self.coef, self.id, self.username, f"Победа! Игра прошла со счётом [{msguser.dice.value}:{msgbot.dice.value}] в пользу {textes[0]}.")
                else:
                    await func.winner(message, self.amount, self.asset, self.coef, self.id, self.username, f"Победа! Игра прошла со счётом [{msgbot.dice.value}:{msguser.dice.value}] в пользу {textes[1]}.")
                break
            elif msguser.dice.value == msgbot.dice.value:
                await message.reply("*⚡Ничья! Играем ещё раз!*", 'markdown')
                await asyncio.sleep(2)
            elif msguser.dice.value < msgbot.dice.value:
                if num == 1:
                    await func.looser(message, f"Проигрыш! Игра прошла со счётом [{msguser.dice.value}:{msgbot.dice.value}] в пользу {textes[1]}.")
                else:
                    await func.looser(message, f"Проигрыш! Игра прошла со счётом [{msgbot.dice.value}:{msguser.dice.value}] в пользу {textes[0]}.")
                break

    async def duel_proccess(self, message: Message, game='🎲', textes=["первого кубика", "второго кубика"]):
        self.coef += coefs.DUEL
        while True:
            msgbot = await message.answer_dice(game)
            msguser = await message.answer_dice(game)
            await asyncio.sleep(4)
            if msguser.dice.value > msgbot.dice.value:
                await func.winner(message, self.amount, self.asset, self.coef, self.id, self.username, f"Победа! Игра прошла со счётом [{msgbot.dice.value}:{msguser.dice.value}] в пользу {textes[1]}.")
                break
            elif msguser.dice.value == msgbot.dice.value:
                await message.reply("*⚡Ничья! Играем ещё раз!*", 'markdown')
                await asyncio.sleep(2)
            elif msguser.dice.value < msgbot.dice.value:
                await func.looser(message, f"Проигрыш! Игра прошла со счётом [{msgbot.dice.value}:{msguser.dice.value}] в пользу {textes[0]}.")
                break

    async def bowling_process(self, message: Message, stake):
        msg = await message.answer_dice('🎳')
        v = msg.dice.value
        self.coef += coefs.BOWLING
        await asyncio.sleep(5)
        if stake == 0:
            if v == 6:
                await func.winner(message, self.amount, self.asset, self.coef, self.id, self.username, "боулинг 0")
            else:
                await func.looser(message, text.get_bowling_text(v))
        elif stake == 1:
            if v == 5:
                await func.winner(message, self.amount, self.asset, self.coef, self.id, self.username, "боулинг 1")
            else:
                await func.looser(message, text.get_bowling_text(v))
        elif stake == 2:
            if v == 4:
                await func.winner(message, self.amount, self.asset, self.coef, self.id, self.username, "боулинг 2")
            else:
                await func.looser(message, text.get_bowling_text(v))
        elif stake == 3:
            if v == 3:
                await func.winner(message, self.amount, self.asset, self.coef, self.id, self.username, "боулинг 3")
            else:
                await func.looser(message, text.get_bowling_text(v))
        elif stake == 5:
            if v == 2:
                await func.winner(message, self.amount, self.asset, self.coef, self.id, self.username, "боулинг 5")
            else:
                await func.looser(message, text.get_bowling_text(v))
        elif stake == 6:
            if v == 1:
                await func.winner(message, self.amount, self.asset, self.coef, self.id, self.username, "боулинг страйк")
            else:
                await func.looser(message, text.get_bowling_text(v))

    async def knb_procces(self, message: Message, stake):
        if stake == "камень":
            hand = '✊🏻'
        elif stake == "бумага":
            hand = '👋🏻'
        elif stake == "ножницы":
            hand = '✌🏻'
        await message.answer(hand)
        await asyncio.sleep(2)
        while True:
            bothand = random.choice(knb)
            await message.answer(bothand)
            if (bothand == '✊🏻' and hand == '👋🏻') or (bothand == '👋🏻' and hand == '✌🏻') or (bothand == '✌🏻' and hand == '✊🏻'):
                await func.winner(message, self.amount, self.asset, self.coef, self.id, self.username, stake)
                break
            elif bothand == hand:
                await message.reply("*⚡Ничья! Бот снова ходит!*", 'markdown')
            else:
                await func.looser(message, "Проигрыш! Соперник переиграл вас в камень, ножницы, бумага!")
                break
