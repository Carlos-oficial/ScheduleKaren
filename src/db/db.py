import sqlite3
from sqlite3 import Error
from os import path


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    finally:
        return conn

def init_db(db):
    with open("schema.sql",'r') as f:
        db.executescript(f.read())

def post_event(name,time,remind=None,db=None):
    if not db:
        db = create_connection("bot.db")
        init_db(db)
    db.execute("INSERT INTO event VALUES(?,?,?,?)",(None,name,time,remind))

def get_queue(db=None):
    if not db:
        db = create_connection("bot.db")
        init_db(db)
    row = conn.execute("SELECT * FROM event ORDER BY time").fetchall()
    return row

def test_db():
    conn = create_connection("bot.db")
    init_db(conn)
    from datetime import datetime
    dt = datetime.now()
    ts = datetime.timestamp(dt)
    conn.execute("INSERT INTO event VALUES(?,?,?,?)",(None,"NOME1",ts,"10"))
    row = conn.execute("SELECT * FROM event ORDER BY id")
    row = row.fetchall()
    print(row)

if __name__ == '__main__':
    conn = create_connection("bot.db")
    init_db(conn)
    test_db()