from db.handlers import query, setup, mutation

@setup
def users(con):
    con.execute('''create table if not exists users (
    id integer primary key autoincrement,
    name text not null,
    last_name text,
    telegram_id text not null unique,
    profile_picture text
    );''')
    return
    
@query
def get_user(id, con = None):
    res = con.execute('select * from users where id=?', id)
    return res.fetchone()

@query
def get_user_with_telegram_id(telegram_id, con = None):
    res = con.execute('select * from users where telegram_id=?', telegram_id)
    return res.fetchone()

@query
def get_all_users(con):
    res = con.execute('select * from users')
    return res.fetchall()

@mutation
def add_user(telegram_id, name, last_name, con):
    res = con.execute('insert into users (telegram_id, name, last_name) values (?, ?, ?)', [telegram_id, name, last_name])
    return res.lastrowid
