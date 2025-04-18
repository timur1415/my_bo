from telegram import (
    Update,
    ReplyKeyboardMarkup,
)
from telegram.ext import (
    ContextTypes,
)
import random

# from start import start
from db import update_wins_knb

from start import start


from states import (
    KNB,
)

async def knb_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["камень", "ножницы", "бумага", "выход"]]
    markup = ReplyKeyboardMarkup(keyboard)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="это игра камень ножницы бумага! тебе нужно выбрать камень ножницы или бумагу и игра начнётся!",
        reply_markup=markup,
    )
    return KNB

async def knb_game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_user = update.effective_message.text
    comp_hod = ["камень", "ножницы", "бумага"]
    print (comp_hod)
    n = random.randint(0, 2)
    print(comp_hod[n])
    if text_user == "камень" and comp_hod[n] == "бумага":
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="ты проиграл\n\nя выбрал бумагу",
        )
        update_wins_knb(update.effective_user.id, 'l')
    elif text_user == "бумага" and comp_hod[n] == "ножницы":
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="ты проиграл\n\nя выбрал ножницы",
        )
        update_wins_knb(update.effective_user.id, 'l')
    elif text_user == "ножницы" and comp_hod[n] == "камень":
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="ты проиграл\n\nя выбрал камень",
        )
        update_wins_knb(update.effective_user.id, 'l')
    elif text_user == "камень" and comp_hod[n] == "ножницы":
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="красава победа на твоей стороне!!!\n\nя выбрал ножницы",
        )
        update_wins_knb(update.effective_user.id, 'w')
        
    elif text_user == "ножницы" and comp_hod[n] == "бумага":
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="красава победа на твоей стороне!!!\n\nя выбрал бумагу",
        )
        update_wins_knb(update.effective_user.id, 'w')
    elif text_user == "бумага" and comp_hod[n] == "камень":
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="красава победа на твоей стороне!!!\n\nя выбрал камень",
        )
        update_wins_knb(update.effective_user.id, 'w')
    elif text_user == "лом":
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="против лома нет приёма!!!\n\nПОСХАЛКА!!!",
        )
        update_wins_knb(update.effective_user.id,'w')
        
    elif text_user == 'выход':
        return await start(update, context)

    else:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="победила дружба!",
        )
        update_wins_knb(update.effective_user.id,'d')