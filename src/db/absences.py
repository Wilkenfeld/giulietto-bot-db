from db.handlers import query, setup, mutation

@setup
def create_absences_table(con=None):
    con.execute('''create table if not exists absences (
    id integer primary key autoincrement,
    user_id integer not null,
    from_date text(10) not null,
    to_date text(10) not null,
    foreign key (user_id) references users(id)
    )''')
    return

@mutation
def create_absence(user_id, from_date, to_date, con=None):
    res = con.execute('insert into absences (user_id, from_date, to_date) values (?, ?, ?)', [user_id, from_date, to_date])
    return res.lastrowid

@query
def get_absence(absence_id, con=None):
    res = con.execute('select * from absences where id = ?', [absence_id])
    return res.fetchone()

@query
def get_all_absences(user_id=None, con=None):
    res = None
    if user_id:
        res = con.execute('select * from absences where user_id = ?', [user_id])
    else:
        res = con.execute('select * from absences')
    return res.fetchall()

@mutation
def delete_absence(absence_id, con=None):
    con.execute('delete from absences where id = ?', [absence_id]) 
