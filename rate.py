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
        [InlineKeyboardButton("стата камень ножницы бумага", callback_data="knb_stat")],
        [InlineKeyboardButton("стата быки и коровы", callback_data="bac_stat")],
        [InlineKeyboardButton("стата крестики нолики", callback_data="knz_stat")],
        [InlineKeyboardButton("назад", callback_data="back")],
    ]

    markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text("ваша стата", reply_markup=markup)

    return RATE


async def knb_stat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    procent = get_knb_rate()
    query = update.callback_query
    keyboard = [[InlineKeyboardButton("назад", callback_data="back")]]

    markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(f'{procent[1]} - {procent[0]}%', reply_markup=markup)

async def bac_stat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    keyboard = [[InlineKeyboardButton("назад", callback_data="back")]]

    markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text('ваша стата в быки и коровы', reply_markup=markup)

async def knz_stat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    keyboard = [[InlineKeyboardButton("назад", callback_data="back")]]

    markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text('ваша стата в быки и коровы', reply_markup=markup)