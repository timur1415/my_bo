from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    ContextTypes,
)

from db import get_knb_rate, get_knb_wins_games, get_bac_record, get_bac_rate
from states import (
    RATE,
)


async def my_stat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton(
                "топ игроков по проценту в камень ножницы бумага",
                callback_data="knb_stat",
            )
        ],
        [InlineKeyboardButton("рекорд в быки и коровы", callback_data="bac_stat")],
        [InlineKeyboardButton("стата крестики нолики", callback_data="knz_stat")],
        [InlineKeyboardButton("назад", callback_data="back")],
    ]

    markup = InlineKeyboardMarkup(keyboard)
    id = update.effective_chat.id
    record = get_bac_record(id)
    procent = get_knb_rate()
    wins_games = get_knb_wins_games(id)
    for nums in wins_games:
        wins = nums[0]
        games = nums[1]
    for user in procent:
        numbers = round(user[1])
    await query.edit_message_text(
        f"привет, {update.effective_user.first_name}, ваша статистика:\n\nкамень ножницы бумага:\n  {wins} побед из {games} игр - {numbers}% побед\n\nбыки и коровы:\n  ваш рекорд: {record} ходов",
        reply_markup=markup,
    )

    return RATE


async def knb_stat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    keyboard = [[InlineKeyboardButton("назад", callback_data="back")]]
    markup = InlineKeyboardMarkup(keyboard)

    procent = get_knb_rate()
    text = ""
    for user in procent:
        numbers = round(user[1], 1)
        text += f"{user[0]} -- {numbers}%\n\n"

    await query.edit_message_text(f"{text}", reply_markup=markup)


async def bac_stat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    keyboard = [[InlineKeyboardButton("назад", callback_data="back")]]
    markup = InlineKeyboardMarkup(keyboard)

    record = get_bac_rate()
    text = ''
    for rec in record:
        text += f'{rec[0]} -- {rec[1]}ходов'

    await query.edit_message_text(f"{text}", reply_markup=markup)


async def knz_stat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    keyboard = [[InlineKeyboardButton("назад", callback_data="back")]]

    markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text("ваша стата в быки и коровы", reply_markup=markup)
