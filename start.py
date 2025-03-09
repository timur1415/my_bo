from telegram import (
    Update,
    ReplyKeyboardRemove,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    ContextTypes,
)


from states import (
    MAIN_MENU,
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("камень ножницы бумага", callback_data="knb")],
        [InlineKeyboardButton("быки и коровы", callback_data="bac")],
        [InlineKeyboardButton("крестики нолики", callback_data="knz")],
        [InlineKeyboardButton("стата", callback_data="rate")],
    ]
    markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    if query:
        await query.edit_message_text(
            text="привет выбери игру в которую будем играть",
            reply_markup=markup,
        )
    else:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="привет выбери игру в которую будем играть",
            reply_markup=markup,
        )
        message = await context.bot.send_message(
            chat_id=update.effective_chat.id, text="f", reply_markup=ReplyKeyboardRemove()
        )
        await context.bot.delete_message(
            chat_id=update.effective_chat.id, message_id=message.id
        )

    return MAIN_MENU
