# FastAPI와 MariaDB — PyMySQL·SQLModel·사원 CRUD

<a id="section-1"></a>

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 범위 | workspace_python/03_database, 00_CSS 제외 |
| 내 코드 | 01_pymysql.py, 02_sqlmodel.py, 03_emp.py, DTO/EmpDTO.py, DTO/DeptDTO.py, templates |
| 강사님 코드 | 같은 경로의 파일과 add/list/detail/update 템플릿 |
| DBMS | MariaDB; 연결 드라이버 PyMySQL |
| 추가 범위 | CryptContext·Argon2 수업 파일 |
| 주의 | 원본 로그인 정보는 재노출하지 않는다. 실제 수업 DB를 자동 실행·수정하지 않는다. |

<a id="section-2"></a>

## 학습 목표

- 요청 데이터가 SQL·DB 결과·HTML로 이어지는 순서를 이해한다.
- Connection·Engine·Session·입력 모델·테이블 모델을 구분한다.
- 변경 업무의 commit·rollback·실패 응답을 일관되게 처리한다.

<a id="section-3"></a>

## 1. 왜 메모리 Todo 다음에 DB를 배우는가?

todo_list는 서버 재시작 때 사라지고 여러 서버 프로세스 사이에 자동 공유되지 않는다. MariaDB는 별도 서버에 데이터를 저장하고 조회·제약 조건·트랜잭션을 처리한다. FastAPI는 HTTP를 담당하고 DB Driver는 DB 서버와 통신한다. Jinja는 조회된 값을 화면으로 만드는 마지막 단계다. DB 연결에 성공했다고 API 경로나 HTML까지 올바른 것은 아니다.

```text
GET /emp/deptno?deptno=20
→ Query 문자열 추출·int 검증
→ DB 연결 또는 Session 공급
→ 바인딩된 SELECT 실행
→ 조회 결과를 이름 기반 행으로 가져옴
→ context["emp_list"]로 전달
→ Jinja 반복문이 HTML 행 생성
→ 200 HTML 응답
```

<a id="section-4"></a>

## 2. PyMySQL: Connection·Cursor·%s는 각각 무엇인가?

양쪽 01_pymysql.py의 get_connect()는 host·port·database·user·password를 설정해 Connection을 만든다. cursorclass=DictCursor는 조회 행을 컬럼명 Key의 dict로 받게 한다. Connection은 접속과 transaction을 관리하고 Cursor는 SQL 실행·결과를 다룬다.

```python
# get_connect()로 연결한 뒤 실행하는 수업 핵심 조각

## 목차

- [문서 정보](#section-1)
- [학습 목표](#section-2)
- [1. 왜 메모리 Todo 다음에 DB를 배우는가?](#section-3)
- [2. PyMySQL: Connection·Cursor·%s는 각각 무엇인가?](#section-4)
- [3. 안전한 접속 설정과 실행 모듈](#section-5)
- [4. Engine·Session·text·mappings의 역할](#section-6)
- [5. table=True·입력 DTO·빈 문자열 검증](#section-7)
- [6. 원본 사원 CRUD를 요청별로 비교하기](#section-8)
- [7. Depends·yield·commit의 실제 순서](#section-9)
- [8. 비밀번호 수업 — 암호화가 아니라 해시 검증](#section-10)
- [9. 실무 지침·자주 하는 실수·디버깅](#section-11)
- [10. 종합실습](#section-12)
- [11. 정답과 해설](#section-13)
- [최종 체크리스트](#section-14)
- [핵심 요약](#section-15)

with connect.cursor() as cursor:
    sql = "SELECT * FROM emp WHERE deptno = %s"
    cursor.execute(sql, (deptno,))
    emp_list = cursor.fetchall()
```


SQLite의 ? 대신 PyMySQL의 %s를 사용한다. 문자열·숫자 모두 placeholder는 %s이며 Python의 % 문자열 연산자로 사용자 값을 미리 끼워 넣지 않는다. (20,)은 한 개짜리 tuple이다. cursor context 종료와 Connection.close()는 다른 자원 종료이므로 원본 finally: connect.close()도 필요하다.

예를 들어 SELECT empno, ename, deptno에서 (1001, '학생', 20)인 샘플 행이 있다면 DictCursor 결과는 [{"empno":1001,"ename":"학생","deptno":20}]과 같은 구조다. 이 값은 설명용 샘플이지 사용자의 현재 DB를 조회해 얻은 결과가 아니다. 빈 결과와 연결 실패를 둘 다 []로 숨기면 사용자는 DB 오류를 '사원 없음'으로 오해할 수 있다.

<a id="section-5"></a>

## 3. 안전한 접속 설정과 실행 모듈

💡 다음은 운영 습관 보강이며 원본 설정을 그대로 복사한 코드가 아니다.

```python
import os
import pymysql

def get_connect():
    return pymysql.connect(
        host=os.getenv("DB_HOST", "127.0.0.1"),
        port=int(os.getenv("DB_PORT", "3306")),
        database=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        cursorclass=pymysql.cursors.DictCursor,
    )
```


설정 누락 KeyError, 인증 실패, 서버 접속 실패, DB명 오류는 원인이 다르다. 오류를 상세히 터미널에 남기되 응답에 비밀번호·접속 URL을 보내지 않는다. root 대신 필요한 권한의 별도 계정을 사용하는 편이 안전하다. 원본 01_pymysql.py의 __main__에는 uvicorn.run('api:app', ...)이 있지만 해당 파일명과 맞지 않는다. 직접 실행 대신 파일 경로가 있는 폴더에서 python -m uvicorn 01_pymysql:app으로 정확한 모듈을 지정하거나 api.py로 이름을 정리한다.

<a id="section-6"></a>

## 4. Engine·Session·text·mappings의 역할

Engine은 연결 URL·Driver·연결 풀 등을 관리하는 DB 진입점이다. create_engine()을 했다고 모든 SQL이 이미 실행된 것이 아니다. Session은 작업과 transaction, ORM 객체 상태를 관리하며 Cursor와 완전히 같은 객체는 아니다. text()는 SQL 문자열을 SQLAlchemy의 실행 가능한 SQL 표현으로 만든다. '미리 서버 컴파일하여 무조건 더 빠르고 %s보다 안전'이라는 내 주석은 과장이다. 두 방식 모두 제대로 바인딩해야 안전하다.

```python
from sqlalchemy import text
sql = text("SELECT * FROM emp3 WHERE deptno = :deptno")
result = session.execute(sql, {"deptno": deptno})
emp_list = result.mappings().fetchall()
```


:deptno는 바인딩 이름이고 dict의 Key가 맞아야 한다. execute의 Result 객체는 결과 데이터 List 자체가 아니다. mappings()는 컬럼명으로 접근하는 RowMapping 결과를 제공한다. fetchall()/all()로 남은 행을 소비하고 Jinja가 emp.ename 같은 표현으로 접근한다.

SQLAlchemy mysql+pymysql:// URL은 MariaDB 서버에 MySQL 호환 Driver로 연결하는 형태다. SQLite의 check_same_thread=False는 같은 연결 사용에 관한 스레드 검사 옵션이지 '여러 연결이 불가능하니 해제'하는 기능이 아니다. 잠금·동시 쓰기 문제와도 별개다.

<a id="section-7"></a>

## 5. table=True·입력 DTO·빈 문자열 검증

내 DTO/EmpDTO.py의 Emp3와 Emp_pr는 table=True이고 Emp_pr_input은 일반 입력 모델이다. 반면 최신 강사님 Emp3 선언에는 table=True가 없다. 이름이 Emp3라도 자동으로 테이블 모델이 된다고 단정하면 안 된다. Field(primary_key=True)만 있다고 create_all이 무조건 테이블을 생성하지 않는다. 테이블 모델을 import해 metadata에 등록한 뒤 create_all을 해야 한다. create_all은 존재하는 테이블의 컬럼을 마음대로 변경하는 migration 도구도 아니다.

Form 입력은 텍스트다. 빈 mgr/comm은 ""이고 DB의 NULL과 다르다. 내 입력 모델과 강사님 모델은 before field validator로 두 필드의 ""를 None으로 바꾼다.

```python
# 실제 수업 방식의 핵심
@field_validator("comm", "mgr", mode="before")
@classmethod
def empty_to_none(cls, value):
    return None if value == "" else value
```


"100"은 이후 int/float 검증을 받고 ""는 None으로 허용된다. 내 empty_to_None2 model_validator는 전달받은 전체 값이 ""인지 비교할 뿐 dict 안 각 필드를 순회하지 않는다. '모든 빈 필드를 처리한다'고 해설하면 틀리다. ename·job 같은 필수 텍스트까지 None으로 바꾸는 것도 올바른 업무 검증이 아니다. 입력용 모델에서 공백 제거·길이·급여 범위·날짜 타입을 명확히 정하고 DB 모델은 저장 스키마에 맞춘다.

<a id="section-8"></a>

## 6. 원본 사원 CRUD를 요청별로 비교하기

| 업무 | 내 03_emp.py | 강사님 03_emp.py | 중요한 차이 |
| --- | --- | --- | --- |
| 목록 | GET /emp/select, emp_pr | GET /list, emp3 | 테이블·URI가 실제로 다름 |
| 추가 화면/처리 | GET·POST /emp/insert | GET /add, POST /api/add | 입력 모델과 Form 연결 |
| 상세 | GET /emp/detail?empno=... | GET /detail/{empno} | Query vs Path |
| 수정 화면/처리 | GET·POST /emp/update | GET /modify, POST /api/modify | 서버에서 사원번호로 재조회 |
| 삭제 | POST /emp/delete, 직접 Form 읽기 | POST /api/delete, empno: int = Form() | 내 원본은 문자열·누락 직접 처리 |

내 상세는 fetchall() 후 for 안에서 첫 결과를 반환한다. 없는 사원은 반복이 실행되지 않아 None 응답이 될 수 있다. 내 수정 화면은 emp_list[0]을 바로 읽어 빈 결과이면 IndexError가 날 수 있다. 강사님 fetchone()도 None을 검사하지 않고 템플릿에 넘기므로 404가 자동 보장되지 않는다.

```python
# 조회 후 처리하는 개선 조각
emp = session.execute(
    text("SELECT * FROM emp_pr WHERE empno = :empno"),
    {"empno": empno},
).mappings().first()
if emp is None:
    raise HTTPException(status_code=404, detail="없는 사원")
```


급여 변경 GET /emp/update/sal?per=10은 수업 실험이지만 조회 method로 DB를 수정한다. 재방문으로 급여가 다시 1.1배가 될 수 있으므로 개선 API에서는 POST/PATCH와 명확한 권한·범위를 사용한다. 한번 1000→1100이면 반복 시 1210이 된다. HTTP method가 SQL 작업 의미를 자동 강제하지는 않는다.

<a id="section-9"></a>

## 7. Depends·yield·commit의 실제 순서

원본 get_session()은 with Session(engine) as session: yield session; session.commit()이다. FastAPI가 generator를 진행해 Session을 얻고 endpoint에 넘긴 후 의존성 정리 단계에서 뒤 코드를 실행한다. endpoint의 'return 직전'과 commit 성공 시점은 반드시 같지 않다. 응답을 만들었다고 변경이 확정되었다고 단정하면 안 된다. 최신 권장 lifecycle 방식은 lifespan이며 수업 on_event 코드는 학습 기록으로 남긴다. [공식 Session 의존성 예제](https://sqlmodel.tiangolo.com/tutorial/fastapi/session-with-dependency/)

💡 성공 응답 전에 commit을 확인하도록 변경 업무가 transaction을 소유하는 개선 방식:

```python
def get_session():
    with Session(engine) as session:
        yield session

def modify_emp(session, empno, ename):
    try:
        result = session.execute(
            text("UPDATE emp_pr SET ename=:ename WHERE empno=:empno"),
            {"ename": ename, "empno": empno},
        )
        # 존재 확인·업무 검증은 이 앞에서 별도로 수행
        session.commit()
    except Exception:
        session.rollback()
        raise
    return result.rowcount
```


commit의 실패도 try 내부에서 처리한다. 같은 rowcount가 MariaDB Driver 설정과 '동일값 수정'에서 어떤 의미인지 확인해야 하며 무조건 0=SQL실패로 해석하지 않는다. 사원 존재 여부는 별도로 SELECT해 판단한다. 원본 INSERT는 endpoint와 dependency 양쪽 commit이 있어 소유권이 섞여 있다. 어느 한 위치에서 업무 단위를 정해 관리하는 편이 읽기 쉽다.

강사님 delete()는 except 뒤 count가 설정되지 않은 채 if count를 읽을 수 있다. 실패를 catch했다고 정상 응답을 만들 수 있는 것은 아니다. except에서 rollback 후 raise하거나 count 초기화와 실패 분기를 명시한다. 입력 오류 422, 없는 행 404, 중복 PK 409, 내부 DB 오류 500을 구분한다.

<a id="section-10"></a>

## 8. 비밀번호 수업 — 암호화가 아니라 해시 검증

양쪽 03_database의 번호 04 파일은 CryptContext(schemes=['argon2'])를 만들고 hash·verify를 연습한다. 파일명은 ZIP 해석 과정에서 깨져 있으므로 의미를 임의 원본 파일명으로 확정하지 않는다. 내용은 확인했다.

```python
from passlib.context import CryptContext
ctx_pw = CryptContext(schemes=["argon2"], deprecated="auto")
hashed = ctx_pw.hash("연습용 비밀번호")
print(ctx_pw.verify("연습용 비밀번호", hashed))
print(ctx_pw.verify("틀린 입력", hashed))
```

```text
True
False
```


Argon2 비밀번호 해시는 원문을 복호화하는 암호화와 다르다. Salt 때문에 동일한 원문도 hash 문자열이 달라질 수 있으므로 문자열 equality가 아니라 verify로 확인한다. 해시를 로그에 지속 출력하거나 평문 비밀번호를 DB에 저장하지 않는다. 이 파일만으로 회원가입·로그인 기능이 완성된 것은 아니다.

<a id="section-11"></a>

## 9. 실무 지침·자주 하는 실수·디버깅

| 증상 | 확인 순서 |
| --- | --- |
| import 실패 | 올바른 Interpreter, sqlmodel·pymysql 설치, DTO 경로 |
| Access denied | 계정·권한·설정값, 비밀정보 로그 노출 금지 |
| table 없음 | human/emp3/emp_pr 구분, table=True·metadata·초기 SQL |
| 정상처럼 보이는데 저장 안 됨 | execute→commit 성공→새 SELECT 순서 |
| ""에서 숫자 오류 | 선택 필드의 before validator와 실제 Form Key |
| 상세 null/수정 500 | 조회 결과 None/빈 List 검사 |
| HTML 빈 행 | context Key와 템플릿의 필드명 |

async def 안에서 동기 DB Driver를 직접 오래 실행하면 event loop를 막을 수 있다. 💡 동기 endpoint·작업 분리·비동기 DB 설계는 해당 Driver에 맞춰 선택한다. 비동기 함수라는 이름만으로 SQL이 비동기화되지 않는다.

<a id="section-12"></a>

## 10. 종합실습

샘플 emp_pr에 사원번호 1001, 이름 학생, 급여 1000인 한 행을 넣은 별도 연습 DB를 준비한다. 목록→상세→이름 수정→재조회→삭제를 연결한다. 수정 입력 빈 mgr/comm을 NULL로 처리하고 없는 사원·중복 사원·연결 실패를 각각 분기한다. 변경 성공은 commit 뒤 303으로 목록에 연결한다. 실제 수업 human DB의 급여 변경 endpoint를 자동 호출하지 않는다.

<a id="section-13"></a>

## 11. 정답과 해설

<details><summary>정상·실패 흐름을 풀어보기</summary>

GET /emp/detail?empno=1001 → int 검증 → Session → 이름 기반 SELECT → 존재 검사 → HTML. 수정 Form → 입력 모델 검증 → 대상 존재 검사 → 바인딩 UPDATE → commit 성공 → 303 목록 → 새 GET 재조회. 없는 사원은 UPDATE 전에 404. 중복 PK INSERT는 transaction rollback 후 409 등 명확한 응답. DB 오류는 로그를 남기고 rollback 후 숨기지 않는다. 예외를 catch하고 return 없이 끝내면 null이 될 수 있으므로 실패 응답도 설계해야 한다.

</details>

<a id="section-14"></a>

## 최종 체크리스트

- [ ] Engine·Session·Cursor의 책임을 구분한다.
- [ ] %s·:name·?를 Driver에 맞게 사용한다.
- [ ] table=True와 입력 모델을 구분한다.
- [ ] 빈 문자열·NULL·필수 값의 차이를 설명한다.
- [ ] commit 실패 이전에 성공 응답을 확정하지 않는다.
- [ ] 실제 계정·비밀번호를 문서와 저장소에 복사하지 않는다.
- [ ] 없는 조회를 404로 처리하고 변경 method를 구분한다.

<a id="section-15"></a>

## 핵심 요약

HTTP 입력 검증 → Session → 바인딩 SQL → 결과 소비 → 업무 상태 확인 → commit/rollback → HTML/Redirect. 해시는 복호화가 아니라 verify로 확인한다.
