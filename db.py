import sqlite3

def create_table():
    # Подлючаемся к бдхе
    conn = sqlite3.connect('game_bot.db')
    # Создать курсор
    cur = conn.cursor()

    # Выполняем какую-то команду
    cur.execute('''CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    knb_win INTEGER,
                    knb_games INTEGER
    )''')

    # Сохранить если было изменение
    conn.commit()
    # Подключение закрыть
    conn.close()

def create__user(id, name):
     # Подлючаемся к бдхе
    conn = sqlite3.connect('game_bot.db')
    # Создать курсор
    cur = conn.cursor()
    cur.execute(f'INSERT INTO users VALUES({id}, "{name}", 0, 0)')
    conn.commit()
    conn.commit()

def update_wins_knb(id):
    # Подлючаемся к бдхе
    conn = sqlite3.connect('game_bot.db')
    # Создать курсор
    cur = conn.cursor()
    cur.execute(f'UPDATE users SET knb_win = knb_win + 1, knb_games = knb_games + 1 WHERE id = {id}')
    conn.commit()
    # Подключение закрыть
    conn.close()