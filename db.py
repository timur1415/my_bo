import sqlite3


def create_table():
    # Подлючаемся к бдхе
    conn = sqlite3.connect("game_bot.db")
    # Создать курсор
    cur = conn.cursor()

    # Выполняем какую-то команду
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    knb_win INTEGER,
                    knb_games INTEGER,
                    bac_record INTEGER,
                    knz_win_x INTEGER,
                    knz_win_O
    )""")

    # Сохранить если было изменение
    conn.commit()
    # Подключение закрыть
    conn.close()


def create__user(id, name):
    # Подлючаемся к бдхе
    conn = sqlite3.connect("game_bot.db")
    # Создать курсор
    cur = conn.cursor()
    cur.execute(f"SELECT id FROM users WHERE id={id}")
    user_data = cur.fetchone()  # вернётся либо none  | (123)
    if user_data == None:
        cur.execute(
            f'INSERT INTO users VALUES({id}, "{name}", 0, 0, 0, 0, 10000000000000)'
        )
        conn.commit()
    conn.close()


def update_wins_knb(id, result):
    # Подлючаемся к бдхе
    conn = sqlite3.connect("game_bot.db")
    # Создать курсор
    cur = conn.cursor()
    if result == "w":
        cur.execute(
            f"UPDATE users SET knb_win = knb_win + 1, knb_games = knb_games + 1 WHERE id = {id}"
        )
    else:
        cur.execute(f"UPDATE users SET knb_games = knb_games + 1 WHERE id = {id}")

    conn.commit()
    # Подключение закрыть
    conn.close()


def get_knb_rate():
    lst = []
    # Подлючаемся к бдхе
    conn = sqlite3.connect("game_bot.db")
    # Создать курсор
    cur = conn.cursor()
    cur.execute("SELECT name, knb_win, knb_games FROM users")
    data = cur.fetchall()
    for user in data:
        name = user[0]
        wins = user[1]
        games = user[2]
        if wins > 0:
            proc = (wins / games) * 100
        else:
            proc = 0
        lst.append([name, proc])
    lst.sort(reverse=True)
    return lst


def update_bac_record(id, record):
    conn = sqlite3.connect("game_bot.db")
    cur = conn.cursor()
    cur.execute(f"SELECT id, bac_record from users WHERE id={id}")
    data = cur.fetchone()
    id = data[0]
    bac_record = data[1]
    if record < bac_record:
        cur.execute(f"UPDATE users SET bac_record = {record} WHERE id={id}")
    conn.commit()
    conn.close()
