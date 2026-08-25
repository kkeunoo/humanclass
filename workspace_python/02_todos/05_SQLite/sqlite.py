import sqlite3

# # SQLite DB접속부
# def connect() :
#     # sqlite3.connect('DB파일명') , 없으면 만들어주고 있으면 읽어옴
#     connect = sqlite3.connect('sqlite.db')
#     cursor = connect.cursor()

#     return cursor

def create_dept() :
    connect = sqlite3.connect('sqlite.db')
    cursor = connect.cursor() # cursor는 위에 connect한 실제 연결 객체를 가져오는 것

    # cursor에 있는 SQL문을 실행
    # 보통 DDL은 autocommit이 되지만, 별도로 commit 해줘야 함
    # if not exists를 넣어주면 만약 없다면 실행하기에 중복생성 오류 방지 (Oracle은 없음)
    cursor.execute('''
        create table if not exists dept (
            deptno integer primary key,
            dname text not null,
            loc text
        )
    ''')
    # commit해주고 나면 연결 끊어주는 것 필요
    connect.commit()
    connect.close()

def insert_dept() :
    connect = sqlite3.connect('sqlite.db')
    cursor = connect.cursor()

    # execute '?'의 경우 이 자리에 다른 것을 받아 넣으라는 것
    # SQL injection을 방지하기 위해 '?'를 쓰고 tuple로 값을 별도로 넣는 것이며,
    # '?'은 int면 int..등등 문자와 숫자 자료형을 한 번 걸러 변환해 줌
    cursor.execute('''
        insert into dept (deptno, dname, loc)
        values (?, ?, ?)
    ''', (10, '1강의실', '천안'))

    cursor.execute('''
        insert into dept (deptno, dname, loc)
        values (?, ?, ?)
    ''', (20, '2강의실', '수원'))

    cursor.execute('''
        insert into dept (deptno, dname, loc)
        values (?, ?, ?)
    ''', (30, '3강의실', '서울'))

    # cursor rowcount로 영향을 미친 열의 수를 알 수 있음
    # 가장 최근의 cursor가 영향을 끼친 줄의 수 만 나옴(3으로 나오지 않음)
    print('수정 개수:', cursor.rowcount)

    connect.commit()
    connect.close()

# select는 실행 후 결과를 다시 가져와야 함
def select_dept() :
    connect = sqlite3.connect('sqlite.db')
    cursor = connect.cursor()

    cursor.execute('''
        select deptno, dname, loc
        from dept
    ''')

    rows = cursor.fetchall()
    print('fetchall 결과')
    print(rows)

    connect.close()

def select_dept_20() :
    connect = sqlite3.connect('sqlite.db')
    cursor = connect.cursor()

    cursor.execute('''
        select deptno, dname, loc
        from dept
        where deptno = ?
    ''',(20,)) # where에 20을 바로 넣어도 좋지만 py에서 진행 시 ','후 튜플로 값 넣기 연습

    # cursor.execute('''
    #     select deptno, dname, loc
    #     from dept
    # ''')

    # fetchall 대신 fetchone으로 하면 원하는 값 하나만 튜플로 받아볼 수 있음 (fetchall은 리스트 안에 튜플)
    # 결과 하나만 구할 때 사용하며 where 조건이 없을 경우 제일 첫 번째 데이터값이 나옴 (에러 없으니 조심)
    rows = cursor.fetchone()
    print('fetchall 결과')
    print(rows)

    connect.close()

def select_dict() :
    connect = sqlite3.connect('sqlite.db')
    connect.row_factory = sqlite3.Row
    cursor = connect.cursor()

    cursor.execute('''
        select deptno, dname, loc
        from dept
        where deptno = ?
    ''',(20,))

    rows = cursor.fetchone()
    print('fetchall 결과')
    print(rows)
    # connect.row_factory = sqlite3.Row 를 사용하면 dict로 형변환하여 받아볼 수 있음
    print( dict(rows) )

    connect.close()

def select_all_dict() :
    connect = sqlite3.connect('sqlite.db')
    connect.row_factory = sqlite3.Row
    cursor = connect.cursor()

    cursor.execute('''
        select deptno, dname, loc
        from dept
    ''')

    rows = cursor.fetchall()
    print('fetchall 결과')
    # for i in range(len(rows)) :
    #     print(dict(rows[i]))

    result = []
    for row in rows :
        result.append(dict(row))
    print(result)

    result2 = [ dict(row) for row in rows]
    print(result2)

    connect.close()

from pydantic import BaseModel
# DTO = Data Transfer Object 데이터 변경 바구니 Java식 표현
class DeptDTO(BaseModel) :
# class DeptSchema(BaseModel) : # Python 식 표현
# class DeptModel(BaseModel) : # Python 식 표현
    deptno : int
    dname : str
    loc : str

def select_all_class() :
    connect = sqlite3.connect('sqlite.db')
    connect.row_factory = sqlite3.Row
    cursor = connect.cursor()

    cursor.execute('''
        select deptno, dname, loc
        from dept
    ''')

    rows = cursor.fetchall()

    # 아래처럼 **로 DeptDTO에 넣을 때 딕셔너리로 분열하여 넣으면 Key=Value가 들어감
    # DeptDTO Pydantic에 형태에 맞게 넣을 때 사용 (고정 된 형태를 가지기 위해 Pydantic 사용)
    result2 = [ DeptDTO(**dict(row)) for row in rows]
    print(result2)

    connect.close()

def update_dept() :
    connect = sqlite3.connect('sqlite.db')
    cursor = connect.cursor()

    # cursor.execute('''
    #     update dept
    #     set dname = ?
    #     where deptno = ?
    # ''', ('좋은 강의실', 10))

    cursor.execute('''
        update dept
        set dname = ?
    ''', ('좋은 강의실',))

    # where 값을 주지 않으면 dept에 있는 dname을 모두 바꾸기 때문에 줄의 수 3개가 나옴
    print('수정 개수:', cursor.rowcount)

    connect.commit()
    connect.close()

def update_with() :
    # connect = sqlite3.connect('sqlite.db')
    # 성공하면 commit, 실패하면 rollback을 진행 함(file처럼 with를 사용해서)
    # close()까지 자동으로 해주기 때문에 'with'를 사용하면 더욱 편리함
    with sqlite3.connect('sqlite.db') as connect:
        cursor = connect.cursor()

        cursor.execute('''
            update dept
            set dname = ?
        ''', ('좋은 강의실',))

        print('수정 개수:', cursor.rowcount)

        # connect.commit()
        # connect.close()

# create_dept()
# insert_dept()
# select_dept()
select_dept_20()
select_dict()
select_all_dict()
select_all_class()
update_dept()
update_with()
select_all_class()