from telegram import (
    Update,
)
from telegram.ext import (
    ContextTypes,
)




from states import (
    GET_NAME,
    GET_AGE,
)

async def take_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="как тебя зовут?"
    )
    return GET_NAME


async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_user = update.effective_message.text
    context.user_data["name"] = text_user
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="сколько тебе лет?"
    )
    return GET_AGE


async def get_age(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_user = update.effective_message.text
    context.user_data["age"] = text_user
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"ваше имя {context.user_data['name']}\nваш возраст {context.user_data['age']}",
    )