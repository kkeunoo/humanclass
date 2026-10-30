import sqlite3

DB_FILE = 'book_todo.sqlite'

def prepare():
    connection = sqlite3.connect(DB_FILE)
    try:
        connection.execute('CREATE TABLE IF NOT EXISTS todos(id INTEGER PRIMARY KEY,item TEXT NOT NULL)')
        connection.commit()
    finally:
        connection.close()

def read_rows(sql, parameters=()):
    connection = sqlite3.connect(DB_FILE)
    connection.row_factory = sqlite3.Row
    try:
        cursor = connection.execute(sql, parameters)
        return [dict(row) for row in cursor.fetchall()]
    finally:
        connection.close()

def find(todo_id):
    rows = read_rows('SELECT id,item FROM todos WHERE id=?', (todo_id,))
    return rows[0] if rows else None

def list_all():
    return read_rows('SELECT id,item FROM todos ORDER BY id')

def change(sql, parameters):
    connection = sqlite3.connect(DB_FILE)
    try:
        cursor = connection.execute(sql, parameters)
        connection.commit()
        return cursor.rowcount
    finally:
        connection.close()

def create(todo_id, item):
    return change('INSERT INTO todos(id,item) VALUES(?,?)', (todo_id,item))

def rename(todo_id, item):
    return change('UPDATE todos SET item=? WHERE id=?', (item,todo_id))

def delete(todo_id):
    return change('DELETE FROM todos WHERE id=?', (todo_id,))
