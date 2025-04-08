import random
from telegram import (
    Update,
)
from telegram.ext import (
    ContextTypes,
)
from start import start

from db import update_bac_record

from states import (
    BAC,
)


def guess_number():
    comp_number = random.randint(1000, 9999)
    otvet = check_num(comp_number)
    if otvet == None:
        return guess_number()
    else:
        return otvet


def check_num(num):
    lst = []
    for simvol in str(num):
        lst.append(int(simvol))
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return None

    return lst


def take_input():
    hod = int(input("введите число"))
    otvet = check_num(hod)
    if otvet == None:
        print("ты не прав")
        return take_input()
    else:
        return otvet


def count_bulls_and_cows(g_sp, u_sp):
    bulls = 0
    cows = 0
    for i in range(len(g_sp)):
        if g_sp[i] == u_sp[i]:
            bulls += 1
    for j in range(len(u_sp)):
        if u_sp[j] in g_sp:
            cows += 1
    return bulls, cows


if __name__ == "__main__":
    g_sp = guess_number()
    print(g_sp)
    bulls = 0
    while bulls < 4:
        u_sp = take_input()
        bulls, cows = count_bulls_and_cows(g_sp, u_sp)
        print(f"Быков {bulls}\nКоров {cows}")


async def bac_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['n_hod'] = 0
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Суть игры заключается в том, что компьютер загадывает одно четырехзначное число цифры, которого должны быть различны. Затем пользователь должен это число отгадать.\n\nпримеры игры:\n\nкомпьютер загадывает 1234 и не говорит от этом человеку\n\nВведите число: 4739\n\nБыки: 1\n\nКоровы: 1\n\nПояснение: Компьютер сказал 1 бык потому, что в догадке человека есть число 3 и оно совпадает с 3 в загаданном числе по номеру. 1 корова потому, что в догадке человека, есть число 4, но в его числе 4 на 1м месте, а у компьютера 4 на 4м месте.Введите число: 4231\n\nБыки: 2\n\nКоровы: 2\n\nПояснение: 2 быка потому, что в догадке человека есть числа 2 и 3, которые совпадают по номеру с 2 и 3 из загаданного компьютером числа.\n\nВведите число: 1234\n\nБыки: 4\n\nКоровы: 0\n\nВы победили",
    )
    g_sp = guess_number()
    print(g_sp)
    context.user_data["g_sp"] = g_sp
    return BAC


async def bac_game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    g_sp = context.user_data["g_sp"]
    num = int(update.effective_message.text)
    context.user_data['n_hod'] += 1
    u_sp = check_num(num)
    if u_sp == None:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="ты ошибаешся.цифры должны быть уникальны",
        )
        return BAC
    buls, cows = count_bulls_and_cows(g_sp, u_sp)
    if buls == 4:
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text="ты угадал"
        )
        update_bac_record(update.effective_user.id, context.user_data['n_hod'])
        return await start(update, context)
    else:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"быков у тебя: {buls}\nкоров у тебя: {cows}:",
        )
    
    
