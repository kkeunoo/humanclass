# 14. SQL DDL과 제약조건

> Table 구조를 정의·변경·삭제하고 Database 수준에서 Data 무결성을 지키는 방법

---

## 이 문서에서 바로 찾기

- [학습 목표](#sql-14-section-2)
- [개념에서 실제 실행까지 — DDL과 제약조건이란? — 저장 구조에서 규칙을 지키기](#sql-14-section-3)
- [12. 내 코드와 강사님 코드 비교](#sql-14-section-15)
- [17. 종합실습](#sql-14-section-20)
- [18. 정답과 해설](#sql-14-section-21)
- [19. 최종 체크리스트](#sql-14-section-22)
- [20. 핵심 요약](#sql-14-section-23)

<details>
<summary>상세 목차 전체 펼치기</summary>

- [📌 문서 정보](#sql-14-section-1)
- [학습 목표](#sql-14-section-2)
- [개념에서 실제 실행까지 — DDL과 제약조건이란? — 저장 구조에서 규칙을 지키기](#sql-14-section-3)
- [1. DDL 기본 개념](#sql-14-section-4)
- [2. CREATE TABLE](#sql-14-section-5)
- [3. 자료형 선택](#sql-14-section-6)
- [4. NOT NULL](#sql-14-section-7)
- [5. DEFAULT](#sql-14-section-8)
- [6. PRIMARY KEY](#sql-14-section-9)
- [7. FOREIGN KEY](#sql-14-section-10)
- [8. 참조 동작](#sql-14-section-11)
- [9. ALTER TABLE](#sql-14-section-12)
- [10. DROP TABLE](#sql-14-section-13)
- [11. TRUNCATE TABLE](#sql-14-section-14)
- [12. 내 코드와 강사님 코드 비교](#sql-14-section-15)
- [13. 개선된 통합 예제](#sql-14-section-16)
- [14. 실무 변경 절차](#sql-14-section-17)
- [15. 자주 하는 실수](#sql-14-section-18)
- [16. 디버깅 방법](#sql-14-section-19)
- [17. 종합실습](#sql-14-section-20)
- [18. 정답과 해설](#sql-14-section-21)
- [19. 최종 체크리스트](#sql-14-section-22)
- [20. 핵심 요약](#sql-14-section-23)
- [📎 다음 문서](#sql-14-section-24)
- [🔬 V3 동작 백과 — Table 구조와 규칙은 어떻게 적용되는가?](#sql-14-section-25)

</details>

---

<a id="sql-14-section-1"></a>

## 📌 문서 정보

| 항목 | 내용 |
|---|---|
| 학습 주제 | `CREATE`, `ALTER`, `DROP`, `TRUNCATE`, `PRIMARY KEY`, `FOREIGN KEY`, `NOT NULL`, `DEFAULT` |
| 기준 DBMS | MariaDB, InnoDB |
| 실습 Table | `DEPT_TEST`, `EMP_TEST` |
| 선수 학습 | Table·Column·자료형, JOIN, NULL |
| 다음 학습 | DML: `INSERT`, `UPDATE`, `DELETE` |
| 문서 버전 | V3 Encyclopedia |

> 원본 `Script.sql`의 JOIN 다음 DDL과 제약조건 범위를 기준으로 구성했다. 실습용 기존 `EMP`, `DEPT`를 직접 변경하지 않고 별도의 `_TEST` Table을 사용한다.

---

<a id="sql-14-section-2"></a>

## 학습 목표

- 열 자료형·PK·FK·NULL·기본값의 역할을 이해한다.
- 실제 입력·중간 상태·결과와 실패 조건을 직접 확인한다.

---

<a id="sql-14-section-3"></a>

## 개념에서 실제 실행까지 — DDL과 제약조건이란? — 저장 구조에서 규칙을 지키기

### 무엇이며 왜 배워야 할까?

DDL은 테이블 같은 저장 구조를 정의·변경하는 언어다. CREATE가 구조를 만들고 ALTER가 구조를 바꾸며 DROP은 객체를 없앤다. SELECT 별칭은 결과 표시만 바꾸지만 ALTER RENAME COLUMN은 실제 구조 이름을 바꾼다. 그 뒤 예전 이름으로 접근하면 오류가 나는 이유다.

자료형은 저장 가능한 값의 형식을, 제약은 허용 관계를 정의한다. INT(4)의 4는 ‘네 자리 정수만’이라는 제한이 아니다. DECIMAL(7,2)는 총 정밀도와 소수 자릿수다. PK는 행 식별자로 유일하고 NULL 불가하며 FK는 비NULL 참조 값에 대해 부모 키 관계를 검사한다.

CREATE TABLE AS SELECT는 조회 결과로 구조와 데이터를 만들 수 있지만 원래 모든 PK·FK·인덱스·기본값이 그대로 복제된다고 보장하지 않는다. 구조 복사 목적과 데이터 복사 목적을 나누어 확인한다.

아래는 기존 EMP·DEPT 대신 새 이름의 InnoDB 학습 테이블을 만든다. 동일 이름이 이미 있으면 CREATE 오류를 확인하고 멈춘다. 편의를 위해 기존 테이블을 DROP하는 초기화 코드는 넣지 않았다. 일반 DDL은 암묵 커밋을 일으킬 수 있으므로 진행 중인 업무 트랜잭션과 섞지 않는다.

### 입력은 어디에서 오는가?

기존 EMP·DEPT를 변경하지 않는 새 wiki_demo_* 테이블을 사용한다. 이 이름이 이미 있으면 다른 새 이름으로 구분하고 기존 객체를 삭제·덮어쓰지 않는다. 일반 DDL은 진행 중인 트랜잭션과 분리한다. 아래 예제는 새 실습 테이블에서 한 번 실행하는 순서다.

### 실행 가능한 보충 SQL과 결과

아래는 원본의 개념을 작은 검증 범위로 정리한 보충 예제다. MariaDB 12.3.2, 일반 SQL 모드·InnoDB 기준에서 결과를 확인했다. 조회 SQL은 SQL 편집기의 Result Grid, 변경 SQL은 영향 행 표시와 사후 SELECT로 관찰한다. DBMS·모드·데이터 상태가 다르면 차이를 확인해야 한다.

```sql
CREATE TABLE wiki_demo_14_dept (
  deptno INT PRIMARY KEY,
  dname VARCHAR(30) NOT NULL
) ENGINE=InnoDB;
CREATE TABLE wiki_demo_14_emp (
  empno INT PRIMARY KEY,
  ename VARCHAR(30) NOT NULL,
  job VARCHAR(20) NOT NULL DEFAULT 'CLERK',
  deptno INT,
  CONSTRAINT wiki_fk_14_dept FOREIGN KEY (deptno)
    REFERENCES wiki_demo_14_dept(deptno)
) ENGINE=InnoDB;
INSERT INTO wiki_demo_14_dept VALUES (10, 'TRAINING');
INSERT INTO wiki_demo_14_emp (empno, ename, deptno)
VALUES (1, 'DEMO', 10);
SELECT e.empno, e.ename, e.job, d.dname
FROM wiki_demo_14_emp AS e
JOIN wiki_demo_14_dept AS d ON d.deptno = e.deptno;
```

Result Grid의 열·행 값:

```text
empno	ename	job	dname
1	DEMO	CLERK	TRAINING
```

여러 SELECT가 있으면 위 출력에 결과 헤더가 다시 나타난다. 숫자의 표시 자릿수와 NULL 표시 모양은 클라이언트별로 달라질 수 있지만 값과 행의 의미를 먼저 비교한다.

### 논리적 처리와 상태 변화 — 단계별로 따라가기

1. 부모 wiki_demo_14_dept에 유일한 부서 키를 정의한다.
2. 자식 wiki_demo_14_emp에 사원 PK와 부서 FK·이름 NOT NULL을 정의한다.
3. 부서 10을 먼저 입력하고 참조 사원을 입력한다.
4. SELECT가 부모·자식이 연결된 저장 결과를 확인한다. 기본값 job이 CLERK로 들어간다.

### 내 코드·강사님 코드의 어느 부분에 있었을까?


#### 내 코드: `workspace_sql/Script.sql` 683~692행

아래는 문맥을 확인하기 위한 발췌다. 주석에 적힌 설명이나 일부 SQL의 앞 상태까지 자동으로 정답이라고 간주하지 않는다. 발췌 조각 전체를 그대로 실행하라는 의미도 아니다.

```sql
as select * from dept where 1 != 1;
select * from dept3;

create table emp3 (
	empno int(4),
	ename varchar(10) not null,
	job varchar(9),
	mgr int(4),
	hiredate date,
	sal decimal(7,2),
```

#### 강사님 코드: `workspace_teacher/workspace_sql/Script.sql` 637~646행

아래는 문맥을 확인하기 위한 발췌다. 주석에 적힌 설명이나 일부 SQL의 앞 상태까지 자동으로 정답이라고 간주하지 않는다. 발췌 조각 전체를 그대로 실행하라는 의미도 아니다.

```sql
as select * from dept where 1 != 1;
select * from dept3;

create table emp3 (
	empno int(4),
	ename varchar(10) not null,
	job varchar(9),
	mgr int(4),
	hiredate date,
	sal decimal(7, 2), -- 총 7자리, 그 중 2자리 소수점
```

원본은 gender→gender2→gender3로 이름을 바꾼 뒤 DROP COLUMN gender를 시도한다. 전체를 이어 실행하면 이미 없는 이름 때문에 오류다. emp3→emp4 뒤 SELECT emp3도 마찬가지다. 순서에 따라 달라진 실제 객체 이름을 확인한다.

### 실무에서 사용하거나 디버깅할 때

표현식 결과와 저장 데이터 변경을 구분한다. 결과가 다르면 원본의 앞선 실행 상태, 입력 행 수, NULL·중복·경계값, 조인 후 행 수를 확인한다. 오류 없이 종료한 변경도 0행 대상일 수 있다. 실제 실행 순서·성능은 아래 본문의 논리 설명만으로 단정하지 말고 실행 계획·사후 조회로 검증한다.

### 이해 확인 실습

1. deptno=20인 자식을 바로 입력하거나 empno=1을 다시 입력하면?
2. gender를 gender2,gender3로 바꾼 뒤 DROP COLUMN gender가 성공하는가?

<details>
<summary>정답과 판단 근거 펼치기</summary>

1. 부서 20은 부모에 없어 FK 오류다. 사원번호 1 중복은 PK 오류다. 기존 행이 자동 덮어쓰기 되지 않는다.
2. 이미 존재하지 않는 이름이라 오류다. 실제 현재 구조와 순서를 확인한다.

</details>

### 이 개념을 다시 사용할 수 있는지 확인

- [ ] 개념·필요성·입력 컬럼과 자료형을 내 말로 설명한다.
- [ ] 중간 행·그룹·관계와 최종 결과를 구분한다.
- [ ] 원본 코드의 앞 상태와 보충 예제의 조건을 구분한다.
- [ ] NULL·0행·중복·경계값 또는 변경 실패를 재검토한다.

---

<a id="sql-14-section-4"></a>

## 1. DDL 기본 개념

### 1. DDL은 구조를 정의한다

```text
CREATE
→ Database Object 생성

ALTER
→ 기존 Object 구조 변경

DROP
→ Object 자체 삭제

TRUNCATE
→ Table 구조를 유지하며 전체 Row 제거
```

<a id="index-section-17"></a>

### 2. DML과 역할이 다르다

```text
DDL
→ Table·Column·Constraint 구조

DML
→ INSERT·UPDATE·DELETE로 Row Data 변경
```

### 3. DDL은 자동 Commit에 주의한다

MariaDB의 많은 DDL 문은 실행 전에 암시적 Commit을 발생시킬 수 있다. 일반 DML처럼 나중에 `ROLLBACK`하면 되겠다고 가정하지 않는다.

### 4. 실습 Table을 따로 만든다

```sql
CREATE TABLE dept_test (
    deptno INT NOT NULL,
    dname VARCHAR(50) NOT NULL,
    loc VARCHAR(50),
    PRIMARY KEY (deptno)
) ENGINE = InnoDB;
```

### 5. 구조를 먼저 확인한다

```sql
DESCRIBE dept_test;
SHOW CREATE TABLE dept_test;
```

---

<a id="sql-14-section-5"></a>

## 2. CREATE TABLE

### 6. 기본 문법

```sql
CREATE TABLE table_name (
    column_name data_type column_options,
    table_constraint
);
```

<a id="index-section-23"></a>

### 7. 부서 Table 생성

```sql
CREATE TABLE dept_test (
    deptno INT NOT NULL,
    dname VARCHAR(50) NOT NULL,
    loc VARCHAR(50),
    PRIMARY KEY (deptno)
) ENGINE = InnoDB;
```

### 8. 사원 Table 생성

```sql
CREATE TABLE emp_test (
    empno INT NOT NULL,
    ename VARCHAR(50) NOT NULL,
    job VARCHAR(30),
    mgr INT,
    hiredate DATE NOT NULL,
    sal DECIMAL(10, 2) NOT NULL DEFAULT 0,
    comm DECIMAL(10, 2),
    deptno INT,
    PRIMARY KEY (empno),
    CONSTRAINT fk_emp_test_dept
        FOREIGN KEY (deptno)
        REFERENCES dept_test (deptno)
) ENGINE = InnoDB;
```

### 9. Column 정의 순서

```text
Column명 → 자료형 → NULL 허용 → DEFAULT → 기타 속성
```

### 10. IF NOT EXISTS

```sql
CREATE TABLE IF NOT EXISTS dept_test (
    deptno INT PRIMARY KEY,
    dname VARCHAR(50) NOT NULL
);
```

이미 존재할 때 오류를 피할 수 있지만 기존 구조가 원하는 정의와 같은지는 보장하지 않는다.

### 11. Table명과 Column명을 의미 있게 작성한다

실습 목적이라도 `test1`, `col1`보다 업무 의미와 역할을 드러내는 이름을 사용한다.

---

<a id="sql-14-section-6"></a>

## 3. 자료형 선택

### 12. 숫자는 계산 목적에 맞게 선택한다

```sql
empno INT,
sal DECIMAL(10, 2)
```

금액처럼 정확한 소수 계산이 필요하면 부동소수점보다 `DECIMAL`을 우선 검토한다.

### 13. 문자열은 최대 길이를 설계한다

```sql
ename VARCHAR(50),
job VARCHAR(30)
```

무조건 큰 길이를 주지 말고 실제 업무 범위, Character Set, Index 사용을 고려한다.

### 14. 날짜는 날짜 자료형으로 저장한다

```sql
hiredate DATE,
created_at DATETIME
```

날짜를 임의 형식의 문자열로 저장하면 비교·정렬·날짜 계산이 어려워진다.

### 15. 정수의 크기와 부호를 맞춘다

Foreign Key의 자식 Column과 부모 Column은 정수 크기와 `UNSIGNED` 여부까지 호환되어야 한다.

### 16. NULL 허용 여부도 Schema의 일부다

자료형이 같아도 필수값과 선택값은 다른 업무 규칙을 가진다.

---

<a id="sql-14-section-7"></a>

## 4. NOT NULL

### 17. NULL 저장을 금지한다

```sql
ename VARCHAR(50) NOT NULL
```

### 18. 빈 문자열과 NULL은 다르다

`NOT NULL`은 `''` 같은 빈 문자열까지 금지하는 규칙이 아니다. 필요하면 Application Validation 또는 `CHECK` 등을 별도로 검토한다.

### 19. 모든 Column에 습관적으로 사용하지 않는다

값이 아직 알려지지 않을 수 있는지, 정말 필수인지 업무 의미로 결정한다.

### 20. 기존 Column을 NOT NULL로 변경하기

```sql
ALTER TABLE emp_test
MODIFY COLUMN job VARCHAR(30) NOT NULL;
```

기존 `NULL` Data가 있으면 변경이 실패할 수 있다.

### 21. 변경 전에 NULL을 확인한다

```sql
SELECT COUNT(*) AS null_job_count
FROM emp_test
WHERE job IS NULL;
```

---

<a id="sql-14-section-8"></a>

## 5. DEFAULT

### 22. 값을 생략했을 때 사용할 기본값

```sql
sal DECIMAL(10, 2) NOT NULL DEFAULT 0
```

### 23. DEFAULT는 기존 모든 NULL을 바꾸지 않는다

Column에 Default를 추가해도 이미 저장된 `NULL`이 자동으로 0으로 갱신되는 것은 아니다.

### 24. 명시적 NULL과 생략을 구분한다

Nullable Column에 명시적으로 `NULL`을 입력하면 Default 대신 NULL이 저장될 수 있다. Default는 주로 Column을 생략하거나 `DEFAULT`를 지정할 때 사용된다.

### 25. 날짜·시간 Default

```sql
created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
```

### 26. 업무상 안전한 값인지 확인한다

급여 미입력과 급여 0은 의미가 다를 수 있다. 단순히 오류를 피하려고 `DEFAULT 0`을 설정하지 않는다.

### 27. Default 확인

```sql
SHOW CREATE TABLE emp_test;
```

---

<a id="sql-14-section-9"></a>

## 6. PRIMARY KEY

### 28. Row를 유일하게 식별한다

```sql
PRIMARY KEY (empno)
```

### 29. 유일성과 NOT NULL을 함께 가진다

Primary Key 값은 중복될 수 없고 NULL도 허용하지 않는다.

### 30. Table당 하나의 Primary Key

하나의 PK 제약조건만 정의할 수 있지만 여러 Column을 묶은 복합 PK는 가능하다.

### 31. 복합 Primary Key

```sql
CREATE TABLE enrollment_test (
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    enrolled_at DATE NOT NULL,
    PRIMARY KEY (student_id, course_id)
);
```

### 32. 자연 Key와 대리 Key

업무 값 자체를 Key로 쓸지, 별도 숫자 ID를 둘지는 값의 안정성·길이·변경 가능성을 고려해 결정한다.

### 33. Primary Key 추가

```sql
ALTER TABLE dept_test
ADD CONSTRAINT pk_dept_test PRIMARY KEY (deptno);
```

이미 중복이나 NULL이 있으면 실패한다.

### 34. 중복 확인

```sql
SELECT deptno, COUNT(*) AS duplicate_count
FROM dept_test
GROUP BY deptno
HAVING COUNT(*) > 1;
```

---

<a id="sql-14-section-10"></a>

## 7. FOREIGN KEY

### 35. 부모와 자식 관계

```text
부모 Table
→ 참조되는 Key 보유: DEPT_TEST.DEPTNO

자식 Table
→ Foreign Key 보유: EMP_TEST.DEPTNO
```

### 36. 기본 정의

```sql
CONSTRAINT fk_emp_test_dept
    FOREIGN KEY (deptno)
    REFERENCES dept_test (deptno)
```

### 37. 존재하지 않는 부모 Key를 막는다

자식의 `DEPTNO`가 NULL이 아니라면 부모 `DEPT_TEST`에 일치하는 `DEPTNO`가 있어야 한다.

### 38. NULL Foreign Key는 허용될 수 있다

자식 Column이 Nullable이면 `NULL`은 “부모가 아직 지정되지 않음”으로 저장할 수 있다.

### 39. 부모 Key는 Index 조건을 만족해야 한다

참조 대상은 Index 또는 Index의 왼쪽 Prefix여야 한다. 일반적으로 Primary Key나 Unique Key를 참조한다.

### 40. 자식 Foreign Key에도 Index가 필요하다

InnoDB는 적합한 Index가 없으면 Foreign Key를 위해 자동 생성할 수 있다. 생성된 Index까지 `SHOW INDEX`로 확인한다.

### 41. 자료형을 맞춘다

```text
INT ↔ INT
INT UNSIGNED ↔ INT UNSIGNED
```

정수의 크기와 부호가 다르면 Foreign Key 생성이 실패할 수 있다.

### 42. Storage Engine을 맞춘다

부모와 자식 Table은 Foreign Key를 지원하는 같은 Engine을 사용해야 한다. 실습에서는 `InnoDB`를 사용한다.

### 43. 제약조건 이름을 직접 지정한다

`fk_emp_test_dept`처럼 관계가 드러나는 이름은 오류 분석과 삭제·변경에 유리하다.

---

<a id="sql-14-section-11"></a>

## 8. 참조 동작

### 44. 기본 동작은 보존을 우선한다

부모 Row를 참조하는 자식 Row가 있으면 부모의 삭제나 Key 변경이 제한될 수 있다.

### 45. ON DELETE RESTRICT

```sql
CONSTRAINT fk_emp_test_dept
    FOREIGN KEY (deptno)
    REFERENCES dept_test (deptno)
    ON DELETE RESTRICT
```

<a id="index-section-68"></a>

### 46. ON DELETE CASCADE

```sql
FOREIGN KEY (deptno)
REFERENCES dept_test (deptno)
ON DELETE CASCADE
```

부모 삭제가 자식 삭제로 전파되므로 업무상 정말 종속된 Data인지 신중히 판단한다.

### 47. ON DELETE SET NULL

```sql
FOREIGN KEY (deptno)
REFERENCES dept_test (deptno)
ON DELETE SET NULL
```

자식 Foreign Key Column이 Nullable이어야 한다.

### 48. ON UPDATE CASCADE

```sql
FOREIGN KEY (deptno)
REFERENCES dept_test (deptno)
ON UPDATE CASCADE
```

부모 Key 변경을 자식에 전파하지만 식별 Key를 자주 변경하는 설계 자체도 점검한다.

### 49. CASCADE를 편의 기능으로만 선택하지 않는다

대량 삭제와 예상하지 못한 전파 위험이 있으므로 Data 수명주기와 감사 요구사항을 먼저 확인한다.

### 50. MariaDB의 SET DEFAULT 참조 동작은 지원되지 않는다

Column의 `DEFAULT` 옵션과 Foreign Key의 `ON DELETE SET DEFAULT` 개념을 혼동하지 않는다.

---

<a id="sql-14-section-12"></a>

## 9. ALTER TABLE

### 51. Column 추가

```sql
ALTER TABLE dept_test
ADD COLUMN phone VARCHAR(30) NULL;
```

### 52. Column 자료형·속성 변경

```sql
ALTER TABLE dept_test
MODIFY COLUMN dname VARCHAR(100) NOT NULL;
```

`MODIFY`할 때 유지해야 할 `NOT NULL`, `DEFAULT` 속성을 빠뜨리지 않는다.

### 53. Column 이름 변경

```sql
ALTER TABLE dept_test
RENAME COLUMN phone TO contact_phone;
```

운영 MariaDB Version에서 지원 구문을 확인한다.

### 54. Column 삭제

```sql
ALTER TABLE dept_test
DROP COLUMN contact_phone;
```

Data가 함께 사라지므로 의존 Query, View, Application을 먼저 조사한다.

### 55. Foreign Key 추가

```sql
ALTER TABLE emp_test
ADD CONSTRAINT fk_emp_test_dept
FOREIGN KEY (deptno)
REFERENCES dept_test (deptno);
```

### 56. Foreign Key 삭제

```sql
ALTER TABLE emp_test
DROP FOREIGN KEY fk_emp_test_dept;
```

필요에 따라 별도로 남은 Index도 확인한다.

### 57. Primary Key 삭제

```sql
ALTER TABLE dept_test
DROP PRIMARY KEY;
```

다른 Foreign Key가 참조 중이면 먼저 의존 관계를 해결해야 한다.

### 58. Table 이름 변경

```sql
RENAME TABLE dept_test TO department_test;
```

Application Query와 Foreign Key Metadata를 포함한 영향 범위를 검토한다.

---

<a id="sql-14-section-13"></a>

## 10. DROP TABLE

### 59. Table 구조와 Data를 모두 삭제한다

```sql
DROP TABLE emp_test;
```

### 60. IF EXISTS

```sql
DROP TABLE IF EXISTS emp_test;
```

존재하지 않는 오류는 피하지만 잘못된 환경이나 이름을 자동으로 안전하게 만드는 것은 아니다.

### 61. 자식 Table부터 삭제한다

```sql
DROP TABLE IF EXISTS emp_test;
DROP TABLE IF EXISTS dept_test;
```

Foreign Key 의존 관계가 있으면 부모보다 자식을 먼저 처리한다.

<a id="index-section-86"></a>

### 62. DROP은 ROLLBACK을 기대하지 않는다

구조와 Data를 제거하는 파괴적 DDL이므로 Backup과 정확한 대상 확인이 먼저다.

### 63. 운영에서는 Fully Qualified Name을 검토한다

```sql
DROP TABLE IF EXISTS practice_db.emp_test;
```

Database 선택 실수의 위험을 줄이되 실행 전 환경을 다시 확인한다.

---

<a id="sql-14-section-14"></a>

## 11. TRUNCATE TABLE

### 64. 모든 Row를 빠르게 제거한다

```sql
TRUNCATE TABLE emp_test;
```

Table 구조는 남는다.

### 65. DELETE와 다르다

```text
DELETE FROM table
→ DML, WHERE 사용 가능, Transaction 범위 검토

TRUNCATE TABLE
→ 전체 Row 제거, DDL처럼 처리, WHERE 사용 불가
```

<a id="index-section-91"></a>

### 66. 암시적 Commit을 발생시킨다

`TRUNCATE` 후 일반적인 `ROLLBACK`으로 Row를 되살릴 수 있다고 가정하지 않는다.

<a id="index-section-92"></a>

### 67. AUTO_INCREMENT 값이 초기화된다

AUTO_INCREMENT를 사용하는 Table은 다음 번호가 처음부터 다시 시작할 수 있다.

### 68. 참조되는 부모 Table은 실패할 수 있다

다른 InnoDB Table의 Foreign Key가 참조하는 Table은 `TRUNCATE`할 수 없을 수 있다.

### 69. 전체 삭제 목적이 명확할 때만 사용한다

일부 Row만 제거하거나 감사 가능한 삭제가 필요하면 `DELETE`를 사용한다.

---

<a id="sql-14-section-15"></a>

## 12. 내 코드와 강사님 코드 비교

### 70. 제약조건 이름을 생략한 형태

```sql
CREATE TABLE emp_test (
    empno INT PRIMARY KEY,
    deptno INT,
    FOREIGN KEY (deptno) REFERENCES dept_test (deptno)
);
```

MariaDB가 이름을 생성할 수 있지만 이후 오류 확인과 삭제 시 직접 확인해야 한다.

<a id="index-section-97"></a>

### 71. 이름과 Engine을 명시한 형태

```sql
CREATE TABLE emp_test (
    empno INT NOT NULL,
    deptno INT,
    PRIMARY KEY (empno),
    CONSTRAINT fk_emp_test_dept
        FOREIGN KEY (deptno)
        REFERENCES dept_test (deptno)
) ENGINE = InnoDB;
```

### 72. ALTER 전에 바로 MODIFY한 형태

```sql
-- 기존 NULL 또는 너무 긴 값이 있으면 실패할 수 있다.
ALTER TABLE emp_test
MODIFY COLUMN job VARCHAR(10) NOT NULL;
```

### 73. Data를 먼저 진단하는 개선 흐름

```sql
SELECT
    SUM(job IS NULL) AS null_count,
    MAX(CHAR_LENGTH(job)) AS max_length
FROM emp_test;
```

진단 결과를 확인한 뒤 적절한 정리와 구조 변경을 수행한다.

### 74. 비교 결론

- 원본 실습은 DDL 문법 확인에 유효하다.
- 실제 변경은 Data와 의존 관계 진단을 먼저 한다.
- Constraint 이름, Engine, 자료형을 명시한다.
- `DROP`, `TRUNCATE`는 Rollback을 기대하지 않는다.
- Foreign Key 검사 비활성화를 일반 해결책으로 사용하지 않는다.

---

<a id="sql-14-section-16"></a>

## 13. 개선된 통합 예제

### 75. 안전한 부모·자식 Table 생성

```sql
CREATE TABLE dept_test (
    deptno INT NOT NULL,
    dname VARCHAR(50) NOT NULL,
    loc VARCHAR(50),
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT pk_dept_test PRIMARY KEY (deptno)
) ENGINE = InnoDB;

CREATE TABLE emp_test (
    empno INT NOT NULL,
    ename VARCHAR(50) NOT NULL,
    hiredate DATE NOT NULL,
    sal DECIMAL(10, 2) NOT NULL DEFAULT 0,
    deptno INT,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT pk_emp_test PRIMARY KEY (empno),
    CONSTRAINT fk_emp_test_dept
        FOREIGN KEY (deptno)
        REFERENCES dept_test (deptno)
        ON UPDATE CASCADE
        ON DELETE SET NULL
) ENGINE = InnoDB;
```

### 76. 생성 결과 검증

```sql
SHOW CREATE TABLE dept_test;
SHOW CREATE TABLE emp_test;
SHOW INDEX FROM dept_test;
SHOW INDEX FROM emp_test;
```

### 77. Information Schema로 제약조건 확인

```sql
SELECT
    table_name,
    constraint_name,
    constraint_type
FROM information_schema.table_constraints
WHERE table_schema = DATABASE()
  AND table_name IN ('dept_test', 'emp_test')
ORDER BY table_name, constraint_type;
```

---

<a id="sql-14-section-17"></a>

## 14. 실무 변경 절차

### 78. 변경 전 확인

```text
대상 Database와 Table
현재 CREATE 문
전체 Row 수와 위반 Data
Foreign Key·Index·View·Application 의존성
Backup과 복구 계획
```

### 79. 운영 Data 복사본에서 먼저 검증한다

DDL의 실행 시간, Lock, 변환 실패, Storage 증가를 Production과 유사한 환경에서 확인한다.

### 80. 한 번에 너무 많은 변경을 섞지 않는다

Column Rename, 자료형 축소, NOT NULL 추가를 한 문장에 모두 섞으면 실패 원인과 복구가 복잡해진다.

### 81. 변경 후 구조와 Data를 모두 검증한다

```sql
SHOW CREATE TABLE emp_test;
SELECT COUNT(*) AS row_count FROM emp_test;
```

### 82. 배포 순서를 부모·자식 관계에 맞춘다

생성은 부모 후 자식, 삭제는 자식 후 부모가 기본 흐름이다.

### 83. foreign_key_checks 비활성화는 최후 수단이다

검사를 끄면 잘못된 Data가 들어갈 수 있고 다시 켤 때 기존 위반 Data가 자동 정리되지 않는다. 일반 실습이나 운영 변경의 편의 기능으로 사용하지 않는다.

---

<a id="sql-14-section-18"></a>

## 15. 자주 하는 실수

### 84. 문자열 길이나 숫자 범위를 근거 없이 정한다

현재 Sample만 보지 말고 실제 업무 최대값과 향후 확장을 고려한다.

### 85. FK 양쪽 자료형이 다르다

`INT`와 `INT UNSIGNED`처럼 부호가 다르면 같은 정수처럼 보여도 호환되지 않을 수 있다.

### 86. 부모보다 자식을 먼저 생성한다

참조 대상 Table과 Key가 먼저 존재해야 한다.

### 87. 부모 Table을 먼저 DROP한다

참조하는 자식 제약조건 때문에 실패하거나 무결성 처리 절차가 필요하다.

### 88. ALTER MODIFY에서 기존 속성을 빠뜨린다

자료형만 바꾸려다 `NOT NULL` 또는 `DEFAULT` 의도가 달라지지 않는지 전체 Column 정의를 확인한다.

### 89. DEFAULT가 기존 Data를 정리한다고 생각한다

Default는 이후 입력의 생략값 규칙이다. 기존 Row 변경은 별도의 `UPDATE`가 필요하다.

### 90. TRUNCATE를 DELETE처럼 사용한다

WHERE가 없고 암시적 Commit과 AUTO_INCREMENT 초기화가 있다는 점을 확인한다.

### 91. IF EXISTS를 안전장치로 과신한다

존재 여부 오류만 줄일 뿐 잘못된 Database의 동명 Table 삭제를 막지 못한다.

---

<a id="sql-14-section-19"></a>

## 16. 디버깅 방법

### 92. 현재 정의를 그대로 확인한다

```sql
SHOW CREATE TABLE emp_test;
```

### 93. Engine과 Collation 확인

```sql
SHOW TABLE STATUS LIKE 'emp_test';
```

### 94. Foreign Key 위반 후보 찾기

```sql
SELECT e.empno, e.deptno
FROM emp_test AS e
LEFT JOIN dept_test AS d
    ON d.deptno = e.deptno
WHERE e.deptno IS NOT NULL
  AND d.deptno IS NULL;
```

### 95. PK 추가 전 중복·NULL 확인

```sql
SELECT empno, COUNT(*) AS duplicate_count
FROM emp_test
GROUP BY empno
HAVING empno IS NULL OR COUNT(*) > 1;
```

### 96. 자료형 축소 전 길이 확인

```sql
SELECT MAX(CHAR_LENGTH(ename)) AS max_name_length
FROM emp_test;
```

<a id="index-section-127"></a>

### 97. Constraint Metadata 확인

```sql
SELECT constraint_name, constraint_type
FROM information_schema.table_constraints
WHERE table_schema = DATABASE()
  AND table_name = 'emp_test';
```

### 98. 오류 메시지의 Constraint 이름을 추적한다

이름을 직접 지정하면 어떤 관계에서 실패했는지 `SHOW CREATE TABLE`과 Metadata로 빠르게 찾을 수 있다.

### 99. 재현 가능한 최소 DDL로 분리한다

부모 Table 생성 → 자식 Column 생성 → PK 확인 → FK 추가 순으로 나누어 어느 단계에서 실패하는지 확인한다.

---

<a id="sql-14-section-20"></a>

## 17. 종합실습

### 100. 문제 1 — 부서 Table 생성

부서 번호를 PK로 하고 부서명은 필수, 위치는 선택인 `dept_practice` Table을 만든다.

### 101. 문제 2 — 사원 Table 생성

사원 번호 PK, 사원명 필수, 급여 Default 0, 부서 번호 FK를 가진 `emp_practice` Table을 만든다.

### 102. 문제 3 — Column 추가와 변경

`emp_practice`에 `email VARCHAR(100)`을 추가하고 이후 `VARCHAR(200) NOT NULL`로 변경한다. 변경 전 기존 NULL 처리 필요성을 설명한다.

### 103. 문제 4 — 제약조건 확인

Information Schema에서 두 실습 Table의 PK와 FK를 조회한다.

### 104. 문제 5 — 안전한 삭제

Foreign Key 관계를 고려하여 두 실습 Table을 올바른 순서로 삭제한다.

---

<a id="sql-14-section-21"></a>

## 18. 정답과 해설

### 105. 문제 1 정답

```sql
CREATE TABLE dept_practice (
    deptno INT NOT NULL,
    dname VARCHAR(50) NOT NULL,
    loc VARCHAR(50),
    CONSTRAINT pk_dept_practice PRIMARY KEY (deptno)
) ENGINE = InnoDB;
```

### 106. 문제 2 정답

```sql
CREATE TABLE emp_practice (
    empno INT NOT NULL,
    ename VARCHAR(50) NOT NULL,
    sal DECIMAL(10, 2) NOT NULL DEFAULT 0,
    deptno INT,
    CONSTRAINT pk_emp_practice PRIMARY KEY (empno),
    CONSTRAINT fk_emp_practice_dept
        FOREIGN KEY (deptno)
        REFERENCES dept_practice (deptno)
) ENGINE = InnoDB;
```

### 107. 문제 3 정답

```sql
ALTER TABLE emp_practice
ADD COLUMN email VARCHAR(100) NULL;

SELECT COUNT(*) AS null_email_count
FROM emp_practice
WHERE email IS NULL;

-- 기존 NULL을 유효한 값으로 정리한 뒤 실행한다.
ALTER TABLE emp_practice
MODIFY COLUMN email VARCHAR(200) NOT NULL;
```

### 108. 문제 4 정답

```sql
SELECT table_name, constraint_name, constraint_type
FROM information_schema.table_constraints
WHERE table_schema = DATABASE()
  AND table_name IN ('dept_practice', 'emp_practice')
ORDER BY table_name, constraint_type;
```

### 109. 문제 5 정답

```sql
DROP TABLE IF EXISTS emp_practice;
DROP TABLE IF EXISTS dept_practice;
```

자식 Table의 Foreign Key 의존성을 먼저 제거한다.

---

<a id="sql-14-section-22"></a>

## 19. 최종 체크리스트

### 110. 설계 체크

- [ ] 각 Column의 자료형·길이·NULL 허용에 업무 근거가 있는가?
- [ ] Row를 안정적으로 식별하는 Primary Key가 있는가?
- [ ] Default가 “미입력”의 올바른 업무값인가?
- [ ] 부모와 자식의 자료형과 Engine이 호환되는가?

### 111. 변경 체크

- [ ] 현재 `SHOW CREATE TABLE`을 확인했는가?
- [ ] 기존 Data의 NULL·중복·길이·FK 위반을 검사했는가?
- [ ] 의존 Object와 Application 영향 범위를 확인했는가?
- [ ] DDL의 암시적 Commit과 Lock 가능성을 고려했는가?

### 112. 삭제·운영 체크

- [ ] `DROP`과 `TRUNCATE`의 정확한 대상을 재확인했는가?
- [ ] Backup과 복구 절차가 준비되어 있는가?
- [ ] 자식과 부모의 처리 순서가 올바른가?
- [ ] 변경 후 구조·Index·Constraint·Row 수를 검증했는가?

---

<a id="sql-14-section-23"></a>

## 20. 핵심 요약

### 113. DDL과 제약조건 핵심 문장

```text
CREATE
→ Table 구조 생성

ALTER
→ 기존 구조 변경, Data와 의존성 선검사

DROP
→ 구조와 Data 모두 삭제

TRUNCATE
→ 구조 유지, 전체 Row 제거, 암시적 Commit

PRIMARY KEY
→ Row의 유일한 식별자, UNIQUE + NOT NULL

FOREIGN KEY
→ 부모 Key와의 참조 무결성 보장

NOT NULL / DEFAULT
→ 필수값과 생략값 규칙
```

### 114. 최종 정리

DDL은 문법을 실행하는 순간 Database 구조와 Data 수명주기를 바꾼다. 따라서 `CREATE`보다 중요한 것은 적절한 자료형과 제약조건을 선택하는 것이고, `ALTER`보다 중요한 것은 기존 Data와 의존 관계를 먼저 진단하는 것이다. `DROP`과 `TRUNCATE`는 일반적인 Rollback을 기대하지 말고 정확한 대상·Backup·실행 순서를 확인한다.

---

<a id="sql-14-section-24"></a>

## 📎 다음 문서

다음 원본 흐름은 Row Data를 생성·수정·삭제하는 DML이다.

```text
15_SQL_DML.md
```

---

<a id="sql-14-section-25"></a>

## 🔬 V3 동작 백과 — Table 구조와 규칙은 어떻게 적용되는가?

DDL은 Data를 담는 그릇과 Database가 강제할 규칙을 정의한다.

```sql
CREATE TABLE todo (
    todo_id BIGINT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'READY',
    user_id BIGINT,
    CONSTRAINT fk_todo_user
        FOREIGN KEY (user_id) REFERENCES user_account(user_id)
);
```

```text
SQL 문법 확인
→ Table 이름 중복 확인
→ Column 이름·자료형·길이 등록
→ PRIMARY KEY Index와 중복 금지 규칙 생성
→ NOT NULL·DEFAULT 규칙 등록
→ FOREIGN KEY 대상 Table·Column 확인
→ Schema Metadata에 Table 생성
```

`title=NULL`을 입력하면 NOT NULL 검증에서 거부되고, 존재하지 않는 `user_id`를 입력하면 FOREIGN KEY 검증에서 거부된다. 제약조건은 Application 검증이 누락되어도 Database의 마지막 경계에서 잘못된 Data를 막는다.

DDL 뒤에는 성공 Message만 보지 않고 실제 구조를 확인한다.

```sql
SHOW CREATE TABLE todo;
DESCRIBE todo;
```

### 수업 원본에서 다시 찾기

| 개념 | 내 코드 Anchor | 강사님 코드 Anchor |
| --- | --- | --- |
| CREATE TABLE | `-- DDL의 시작`, `create table` | `create table emp2` |
| PK·FK | `primary key`, `foreign key` | 제약조건 구간 |
| ALTER | `alter table` | 같은 Query |
| DROP·TRUNCATE | `drop table`, `truncate` | 같은 DDL 구간 |

ALTER 전에는 기존 Data가 새 자료형과 제약조건을 만족하는지 먼저 조회한다.
