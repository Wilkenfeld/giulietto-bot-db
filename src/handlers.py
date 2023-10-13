from dotenv import dotenv_values
from sqlite3 import connect
from functools import wraps
from typing import Optional, Callable

#? TODO: save abs location in env variable
def get_real_conf_path():
    """Returns the real absolute path for .env file"""
    import os
    from pathlib import Path

    real_file_location = os.path.realpath(__file__)
    conf_path = os.path.join(Path(real_file_location).parent.parent, '.env')
    print(conf_path)
    return conf_path

conf = dotenv_values(get_real_conf_path())

def query(callback, name: Optional[str] = None):
    """Decorator for handling a connection to DB"""
    name = name if name else callback.__name__

    @wraps(callback)
    def wrapper(*args, **kwargs):
        print(f'Executing query ({name})')
        con = connect(conf['SQLITE_DB'])
        kwargs['con'] = con
        res = callback(*args, **kwargs)
        con.close()
        return res

    return wrapper

def mutation(callback, name: Optional[str] = None):
    """Decorator for handling a connection to DB"""
    name = name if name else callback.__name__

    @wraps(callback)
    def wrapper(*args, **kwargs):
        print(f'Executing mutation ({name})')
        con = connect(conf['SQLITE_DB'])
        kwargs['con'] = con
        res = callback(*args, **kwargs)
        con.commit()
        con.close()
        return res

    return wrapper
    

def setup(callback, name: Optional[str] = None):
    """Decorator to init a service (create tables and similar stuff)"""
    name = name if name else callback.__name__
    print(f"Setup {name}")
    con = connect(conf['SQLITE_DB'])
    callback(con)
    con.close()
    return callback


if __name__ == "__main__":
    from services.users import get_user, add_user, get_all_users
    print(add_user('2', 'Roberto', ''))
    print(get_user('1'))
    print(get_all_users())

    from services.absences import create_absence, get_absence, get_all_absences, delete_absence
    print(create_absence(1, '2023-10-10', '2023-10-12'))
    print(get_absence(1))
    print(get_all_absences())
    print(get_all_absences(1))
    delete_absence(14)
    print(get_all_absences())
