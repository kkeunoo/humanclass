# 🗄️ SQL Developer-Wiki

> **Learn • Compare • Improve • Archive**
>
> 관계형 Database의 조회·집계·관계·변경·Transaction 기초  
> 실제 MariaDB 수업·실습 코드를 기반으로 SQL의 동작 원리, 코드 비교, 오류 분석, 안전한 작성 방식을 하나의 학습 흐름으로 정리합니다.

---

## 📌 학습 목표

- `SELECT`부터 조건·정렬·집계까지 SQL 조회의 기본 흐름을 이해합니다.
- 함수, `CASE`, Subquery, 집합연산을 활용해 요구사항을 Query로 변환합니다.
- `INNER JOIN`, Outer Join, Self Join으로 Table 관계를 정확히 연결합니다.
- DDL과 제약조건으로 Table 구조와 Data 무결성을 설계합니다.
- DML과 Transaction으로 Data를 안전하게 생성·수정·삭제합니다.
- Index와 실행 계획을 사용해 Query 성능을 측정하고 개선합니다.
- Recursive CTE로 조직도와 같은 계층형 Data를 탐색합니다.
- 내 코드와 강사 코드의 실제 차이를 비교하고 더 명확한 SQL로 개선합니다.

---

## 🗺️ 학습 흐름

```text
SELECT와 조건식
    ↓
정렬·집계·함수
    ↓
CASE와 집합연산
    ↓
Subquery와 JOIN
    ↓
DDL·제약조건·DML
    ↓
Transaction
    ↓
Index·AUTO_INCREMENT
    ↓
Recursive CTE
    ↓
실무 코딩 스타일
    ↓
종합실습
```

---

## 📚 Documentation

| No | Document | 분류 |
|:--:|---|:--:|
| 01 | [01 SQL 기초와 SELECT](./01_SQL_기초와_SELECT.md) | 학습 |
| 02 | [02 SQL WHERE와 조건연산자](./02_SQL_WHERE와_조건연산자.md) | 학습 |
| 03 | [03 SQL LIKE와 NULL](./03_SQL_LIKE와_NULL.md) | 학습 |
| 04 | [04 SQL 정렬과 LIMIT](./04_SQL_정렬과_LIMIT.md) | 학습 |
| 05 | [05 SQL 집계함수](./05_SQL_집계함수.md) | 학습 |
| 06 | [06 SQL GROUP BY와 HAVING](./06_SQL_GROUP_BY와_HAVING.md) | 학습 |
| 07 | [07 SQL 문자열함수](./07_SQL_문자열함수.md) | 학습 |
| 08 | [08 SQL 숫자·날짜·NULL함수](./08_SQL_숫자_날짜_NULL함수.md) | 학습 |
| 09 | [09 SQL CASE 조건식](./09_SQL_CASE_조건식.md) | 학습 |
| 10 | [10 SQL UNION과 UNION ALL](./10_SQL_UNION과_UNION_ALL.md) | 학습 |
| 11 | [11 SQL 서브쿼리](./11_SQL_서브쿼리.md) | 학습 |
| 12 | [12 SQL JOIN](./12_SQL_JOIN.md) | 학습 |
| 13 | [13 SQL Outer JOIN과 Self JOIN](./13_SQL_Outer_JOIN과_Self_JOIN.md) | 학습 |
| 14 | [14 SQL DDL과 제약조건](./14_SQL_DDL과_제약조건.md) | 학습 |
| 15 | [15 SQL DML](./15_SQL_DML.md) | 학습 |
| 16 | [16 SQL Transaction](./16_SQL_Transaction.md) | 학습 |
| 17 | [17 SQL Index와 AUTO_INCREMENT](./17_SQL_Index와_AUTO_INCREMENT.md) | 학습 |
| 18 | [18 SQL Recursive CTE](./18_SQL_Recursive_CTE.md) | 학습 |
| 19 | [19 SQL 실무 코딩스타일](./19_SQL_실무_코딩스타일.md) | 실무 |
| 20 | [20 SQL 종합실습](./20_SQL_종합실습.md) | 실습 |

---

## 🧩 학습 영역

| 영역 | 문서 | 핵심 내용 |
|---|:---:|---|
| 조회 기초 | 01–04 | `SELECT`, `WHERE`, `LIKE`, `NULL`, `ORDER BY`, `LIMIT` |
| 집계·함수 | 05–09 | 집계함수, Grouping, 문자열·숫자·날짜 함수, `CASE` |
| 결과 결합 | 10–13 | `UNION`, Subquery, Inner·Outer·Self Join |
| 구조·Data 변경 | 14–16 | DDL, 제약조건, DML, Transaction |
| 성능·계층 | 17–18 | Index, `AUTO_INCREMENT`, Recursive CTE |
| 실무 통합 | 19–20 | Coding Style, Code Review, 종합실습 |

---

## 🧭 추천 학습 방법

1. README에서 전체 학습 범위와 문서 순서를 확인합니다.
2. 번호 순서대로 문서를 읽고 SQL 예제를 직접 실행합니다.
3. 실행 전 예상 Result의 Column, Row 수, NULL과 중복 여부를 작성합니다.
4. 내 코드와 강사 코드의 실제 차이를 확인하고 결과와 작성 의도를 비교합니다.
5. 원본 설명의 오류·과도한 일반화와 개선 내용을 구분해서 이해합니다.
6. 대표 오류와 Debugging 과정을 같은 Sample Data로 다시 재현합니다.
7. DDL·DML 실습은 원본 `EMP`, `DEPT`가 아닌 별도 실습 Table에서 진행합니다.
8. 실무 코딩 스타일에서 안전성과 Code Review 기준을 정리합니다.
9. 종합실습에서 조회부터 Transaction·Index까지 하나의 흐름으로 연결합니다.

---

## 🗃️ 실습 Database

SQL 문서는 MariaDB의 학습용 Sample Schema를 기준으로 합니다.

```text
EMP
→ 사원 정보

DEPT
→ 부서 정보

SALGRADE
→ 급여 범위와 등급

BONUS
→ Bonus 정보
```

주요 관계는 다음과 같습니다.

```text
EMP.DEPTNO → DEPT.DEPTNO
→ 사원과 부서 관계

EMP.MGR → EMP.EMPNO
→ 사원과 관리자 Self Join 관계

EMP.SAL BETWEEN SALGRADE.LOSAL AND SALGRADE.HISAL
→ 급여 등급 Non-Equi Join
```

> `EMP.MGR`과 `SALGRADE` 관계는 학습 Query에서 논리적으로 연결하는 구조이며 실제 Foreign Key 정의 여부와는 구분합니다.

---

## 🔍 원본 비교 기준

SQL V2 문서는 사용자 `workspace_sql/Script.sql`과 강사님 `workspace_sql/Script.sql`을 함께 검토하여 구성했습니다.

- 실제로 존재하는 코드 차이만 비교합니다.
- 단순 Formatting 차이와 결과가 달라지는 Logic 차이를 구분합니다.
- 수업 중 시행착오는 최종 정답과 분리해 설명합니다.
- MariaDB의 실제 동작과 다른 설명은 교정 근거와 함께 보완합니다.
- 원본에 없는 비교 내용을 임의로 만들지 않습니다.
- 문서 분리는 단순 줄 번호가 아니라 실제 학습 흐름을 기준으로 합니다.

---

## 💼 실무 코딩 스타일

[19 SQL 실무 코딩스타일](./19_SQL_실무_코딩스타일.md)

앞에서 학습한 문법을 반복하기보다 실제 Project에서 SQL을 어떻게 작성·검증·Review할지에 집중합니다.

```text
Naming & Formatting
→ Query Structure
→ NULL & Boundary Safety
→ Safe DML
→ Transaction
→ Execution Plan
→ Code Review
```

---

## 🚀 종합실습

[20 SQL 종합실습](./20_SQL_종합실습.md)

SQL 01~19의 내용을 단계별 문제와 하나의 실무 Scenario로 연결합니다.

```text
기초 조회
    ↓
함수·CASE·집계
    ↓
JOIN·Subquery·계층
    ↓
Schema 설계
    ↓
안전한 DML·Transaction
    ↓
Index·실행 계획
    ↓
최종 Code Review
```

---

## 🛡️ 안전한 실습 원칙

- `UPDATE`, `DELETE` 전에 같은 조건의 `SELECT`로 대상 Row를 확인합니다.
- 원본 `EMP`, `DEPT`를 변경하지 않고 `_PRACTICE`, `_TEST` Table을 사용합니다.
- DML은 예상 영향 Row와 변경 후 Data를 함께 검증합니다.
- 여러 변경은 `START TRANSACTION`으로 묶고 성공 시 `COMMIT`, 문제 발생 시 `ROLLBACK`합니다.
- `DROP`, `TRUNCATE`, 주요 `ALTER`는 일반적인 Rollback을 기대하지 않습니다.
- `FORCE INDEX`는 실행 계획과 실제 측정 근거가 있을 때만 사용합니다.
- Recursive CTE는 종료 조건, 최대 깊이, Cycle 가능성을 확인합니다.

---

## ⭐ Documentation Features

- ✅ 실제 MariaDB 수업·실습 코드 기반
- ✅ 사용자 코드와 강사 코드 비교
- ✅ 존재하지 않는 차이는 임의로 만들지 않음
- ✅ 원본 오류와 개선 방향 구분
- ✅ Query 결과뿐 아니라 동작 원리와 실무 활용 설명
- ✅ NULL·경계값·중복·동점 Test 보완
- ✅ 대표 오류와 단계별 Debugging 정리
- ✅ 안전한 DDL·DML·Transaction 절차 제공
- ✅ Index와 실행 계획 검증 포함
- ✅ 실무 코딩 스타일과 종합실습 제공
- ✅ GitHub 상대 경로 Navigation 통일

---

## 📖 Documentation Structure

```text
Document Information
        ↓
Learning Objectives
        ↓
Core Concepts
        ↓
Syntax & Examples
        ↓
Practical Usage
        ↓
Code Comparison
        ↓
Corrections & Improvements
        ↓
Common Mistakes & Debugging
        ↓
Comprehensive Exercises
        ↓
Answers & Explanations
        ↓
Final Checklist
        ↓
Key Summary
```

> 실제 원본이나 비교 대상이 없는 항목은 존재하지 않는 차이를 만들지 않고 해당 주제의 동작 원리와 검수 내용을 중심으로 구성합니다.

---

## 🎯 Learning Outcome

SQL 문서를 완료하면 다음 흐름으로 Database 문제를 설명하고 해결하는 것을 목표로 합니다.

```text
요구사항 분석
→ Result 한 Row의 의미 정의
→ Query 작성
→ NULL·중복·경계값 검증
→ 안전한 Data 변경
→ 실행 계획과 성능 확인
→ 유지보수 가능한 문서화
```

---

## 📂 Folder Policy

- 학습 문서는 `01`부터 `20`까지 번호 순서를 유지합니다.
- `README.md`는 SQL 문서의 목차와 학습 가이드 역할을 담당합니다.
- 같은 폴더 문서는 `./파일명.md`로 연결합니다.
- Developer-Wiki Home은 `../README.md`로 연결합니다.
- 이전 Subject는 `../04_Python/README.md`로 연결합니다.
- 실무 코딩 스타일과 종합실습은 정규 학습 마지막 단계에 배치합니다.
- SQL 원본 실습 파일은 `workspace_sql`에서 관리하고 Wiki 문서와 역할을 구분합니다.
- 모든 내부 Link는 GitHub 상대 경로를 사용합니다.

---

## 📎 Navigation

| Previous | Home | Next |
|:---:|:---:|:---:|
| [🐍 Python](../04_Python/README.md) | [🏠 Developer-Wiki](../README.md) | [🏠 Developer-Wiki](../README.md) |

---

## 📚 Developer-Wiki

> **Learn • Compare • Improve • Archive**

실행한 Query와 해결한 Database 문제를 다시 사용할 수 있는 개발 지식으로 축적하는 것을 목표로 합니다.
