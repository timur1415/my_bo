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
                    knb_games INTEGER,
                    bac_recored INTEGER,
                    knz_win INTEGER
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
    cur.execute(f'SELECT id FROM users WHERE id={id}')
    user_data = cur.fetchone()#вернётся либо none  | (123) 
    if user_data == None:
        cur.execute(f'INSERT INTO users VALUES({id}, "{name}", 0, 0, 0, 0)')
        conn.commit()
    conn.close() 

def update_wins_knb(id,result):
    # Подлючаемся к бдхе
    conn = sqlite3.connect('game_bot.db')
    # Создать курсор
    cur = conn.cursor()
    if result == 'w':
        cur.execute(f'UPDATE users SET knb_win = knb_win + 1, knb_games = knb_games + 1 WHERE id = {id}')
    else:
        cur.execute(f'UPDATE users SET knb_games = knb_games + 1 WHERE id = {id}')
    conn.commit()
    # Подключение закрыть
    conn.close()


def get_knb_rate(name):
    lst = []
     # Подлючаемся к бдхе
    conn = sqlite3.connect('game_bot.db')
    # Создать курсор
    cur = conn.cursor()
    cur.execute(f'SELECT name, knb_wins, knb_games where name={name}')
    data = cur.fetchall()
    for user in data:
        name = user[0]
        wins = user[1]
        games = user[2]
        if wins > 0:
            proc = (wins / games) * 100
        else:
            proc = 0
    lst.append(proc, name)
    lst.sort(reverse = True)
    return lst



   
