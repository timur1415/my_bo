from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    ContextTypes,
)

from db import get_knb_rate
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
    procent = get_knb_rate()
    for user in procent:
        numbers = round(user[1])
    await query.edit_message_text(
        f"привет, {update.effective_user.first_name}, ваша статистика:\n\nкамень ножницы бумага:\nваш процент побед состовляет {numbers}% ",
        reply_markup=markup,
    )

    return RATE


async def knb_stat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    procent = get_knb_rate()
    text = ""
    for user in procent:
        numbers = round(user[1], 1)
        text += f"{user[0]} -- {numbers}%\n\n"
    query = update.callback_query
    keyboard = [[InlineKeyboardButton("назад", callback_data="back")]]

    markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(f"{text}", reply_markup=markup)


async def bac_stat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    keyboard = [[InlineKeyboardButton("назад", callback_data="back")]]

    markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text("ваша стата в быки и коровы", reply_markup=markup)


async def knz_stat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    keyboard = [[InlineKeyboardButton("назад", callback_data="back")]]

    markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text("ваша стата в быки и коровы", reply_markup=markup)
