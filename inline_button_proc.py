from telegram import (
    Update,
)
from telegram.ext import (
    ContextTypes,
)


from knz_game import knz_start
from knb_game import knb_start
from bac_game import bac_start


async def inline_button_proc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "knb":
        return await knb_start(update, context)

    if query.data == "bac":
        return await bac_start(update, context)

    if query.data == "knz":
        return await knz_start(update, context)
