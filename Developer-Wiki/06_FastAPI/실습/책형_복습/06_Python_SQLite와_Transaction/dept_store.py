import sqlite3

DB_FILE = 'book_dept.sqlite'

def prepare():
    connection = sqlite3.connect(DB_FILE)
    try:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS dept (deptno INTEGER PRIMARY KEY, dname TEXT NOT NULL, loc TEXT)')
        cursor.execute('SELECT COUNT(*) FROM dept')
        if cursor.fetchone()[0] == 0:
            for row in [(10, '1강의실', '천안'), (20, '2강의실', '수원'), (30, '3강의실', '서울')]:
                cursor.execute('INSERT INTO dept(deptno,dname,loc) VALUES(?,?,?)', row)
        connection.commit()
    finally:
        connection.close()

def find_dept(deptno):
    connection = sqlite3.connect(DB_FILE)
    connection.row_factory = sqlite3.Row
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT deptno,dname,loc FROM dept WHERE deptno=?', (deptno,))
        row = cursor.fetchone()
        return dict(row) if row is not None else None
    finally:
        connection.close()

def rename_dept(deptno, name):
    connection = sqlite3.connect(DB_FILE)
    try:
        with connection:
            cursor = connection.cursor()
            cursor.execute('UPDATE dept SET dname=? WHERE deptno=?', (name, deptno))
            changed = cursor.rowcount
        return changed
    finally:
        connection.close()
