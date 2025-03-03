import logging
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ConversationHandler,
    CallbackQueryHandler,
)


from knz_game import knz_hod

from rate import my_stat, knb_stat, bac_stat, knz_stat

from start import start

from knb_game import knb_start, knb_game

from inline_button_proc import inline_button_proc

from get_data import get_age, get_name, take_input

from bac_game import bac_game, bac_start



from states import (
    MAIN_MENU,
    KNB,
    BAC,
    GET_NAME,
    GET_AGE,
    KNZ,
    RATE,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

if __name__ == "__main__":
    application = (
        ApplicationBuilder()
        .token("7485420037:AAHorQ62XM3FtqB8UFMQU3vs-MbERKd8sfQ")
        .build()
    )
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            MAIN_MENU: [
                CommandHandler(
                    "knb",
                    knb_start,
                ),
                CommandHandler("bac", bac_start),
                CommandHandler("get_name", take_input),
                CallbackQueryHandler(my_stat, pattern="^rate$"),
                CallbackQueryHandler(inline_button_proc),
            ],
            KNB: [MessageHandler(filters.TEXT & ~filters.COMMAND, knb_game)],
            BAC: [MessageHandler(filters.TEXT & ~filters.COMMAND, bac_game)],
            GET_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
            GET_AGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_age)],
            KNZ: [MessageHandler(filters.TEXT & ~filters.COMMAND, knz_hod)],
            RATE: [
                CallbackQueryHandler(knb_stat, pattern="^knb_stat$"),
                CallbackQueryHandler(start, pattern="^back$"),
                CallbackQueryHandler(bac_stat, pattern="^bac_stat$"),
                CallbackQueryHandler(knz_stat, pattern="^knz_stat$")
            ],
        },
        fallbacks=[CommandHandler("start", start)],
    )

    application.add_handler(conv_handler)

    application.run_polling()
