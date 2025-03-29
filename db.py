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
                    knb_proc INTEGER,
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
        cur.execute(f'INSERT INTO users VALUES({id}, "{name}", 0, 0, 0, 0, 0)')
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

def update_proc_knb(id,proc):
    # подключение к бд
    conn = sqlite3.connect('game_bot.db')
    # создать курсор
    cur = conn.cursor()
    result = cur.fetchone() 
    wins = result[2]
    games = result[3]
    proc = wins / games
    proc *= 100
    if proc != 0:
        proc = wins / games
        proc *= 100
        # proc = wins / games * 100
        cur.execute(f'UPDATE users SET knb_proc = {proc} WHERE id = {id}')
    else:
        proc = None 
    conn.commit()
    conn.close()

    
   

   
