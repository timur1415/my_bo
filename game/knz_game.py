from telegram import Update
from telegram.ext import (
    ContextTypes,
)
from telegram.constants import ParseMode

from states import KNZ

from db import update_knz_record

from start import start

def get_board_st(board):
    st = "-" * 13
    for i in range(0, 7, 3):
        st += f"\n| {board[i]} | {board[i + 1]} | {board[i + 2]} |\n"
        st += "-" * 13
    return f"`{st}`"


async def knz_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    context.user_data["board"] = board
    hod = 1
    context.user_data["db_hod"] = 0
    context.user_data["hod"] = hod
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="ты попал в игру крестики нолики!\n\nПРАВИЛА ИГРЫ\n\nвам отпровляется игровое поле с номерами в каждой клетке и вам нужно выбрать куда вы поставите крестик или нолик,выбрали, на клетке которую вы выбрали ставится крестик или нолик а дальше всё как в обычных крестиках и ноликах. кто первый поставит свои фигуры 3 в ряд тот и победил!\n\n удачи!",
    )
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=get_board_st(board),
        parse_mode=ParseMode.MARKDOWN_V2,
    )
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="куда вы хотите поставить нолик?"
    )

    return KNZ


async def knz_hod(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["db_hod"] += 1
    context.user_data["hod"] += 1
    text_user = int(update.effective_message.text)
    if text_user > 9 or text_user < 1:
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text="ты выбрал плохое число"
        )
        return KNZ

    if context.user_data["hod"] % 2 == 0:
        figure = "O"
    else:
        figure = "X"

    if context.user_data["board"][text_user - 1] in "XO":
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text="выбери заново пж"
        )
        return KNZ

    context.user_data["board"][text_user - 1] = figure
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=get_board_st(context.user_data["board"]),
        parse_mode=ParseMode.MARKDOWN_V2,
    )
    ress = check_win(context.user_data["board"])
    context.user_data["db_hod"] += 1
    if ress and ress in "XO":
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"победил {ress}", 
        )

        update_knz_record(update.effective_chat.id, context.user_data["db_hod"])
        return await start(update, context)
        
    
    elif context.user_data["hod"] == 9 and ress == None:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="нечья",
        )
        return await start(update, context)

def check_win(board):
    if board[0] == board[1] == board[2]:
        return board[0]
    elif board[3] == board[4] == board[5]:
        return board[3]
    elif board[6] == board[7] == board[8]:
        return board[6]
    elif board[0] == board[3] == board[6]:
        return board[0]
    elif board[1] == board[4] == board[7]:
        return board[1]
    elif board[2] == board[5] == board[8]:
        return board[2]
    elif board[0] == board[4] == board[8]:
        return board[0]
    elif board[2] == board[4] == board[6]:
        return board[2]
    else:
        return None
