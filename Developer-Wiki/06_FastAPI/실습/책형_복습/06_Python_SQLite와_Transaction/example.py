import sqlite3
from dept_store import DB_FILE, prepare, find_dept, rename_dept

prepare()
print(find_dept(20))
print('수정 행', rename_dept(20, '복습 강의실'))
print(find_dept(20))
print('없는 번호', find_dept(99))

connection = sqlite3.connect(DB_FILE)
try:
    with connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE dept SET dname=? WHERE deptno=?', ('임시 이름', 10))
        raise ValueError('취소 실험')
except ValueError:
    print('미확정 변경 취소')
finally:
    connection.close()
print(find_dept(10))
