# 20. SQL 종합실습 — 빈 부서까지 포함한 급여 보고서

[SQL 목차](README.md) · [실무 스타일](19_SQL_실무_코딩스타일.md)

## 1. 목적과 자료

원래 부서별 급여 차이 문제에서 출발해 여러 장을 연결하는 **새 종합실습**이다. 원본 EMP 초기 자료와 다른 book_emp 6명·book_dept 4개를 쓴다. 개념·별칭·관계·빈 그룹·NULL을 설명하는 것이 목표다.

## 2. 요구사항과 예상

모든 부서의 번호·이름·실제 사원 수·최고급여−최저급여를 부서번호순으로 보여 준다. 사원이 없는 부서도 남긴다. 사원 수는0으로, 계산할 급여가 없는 차이는NULL로 둔다. 0을 무조건 채워 표시하지 않는다.

| 부서 | 사원 급여 | 예상 인원·차이 |
| --- | --- | --- |
| ALPHA | 1300 | 1·0 |
| BETA | 1000·3000·3000 | 3·2000 |
| GAMMA | 1600·1500 | 2·100 |
| EMPTY | 없음 | 0·NULL |

## 3. 직접 작성할 순서

1. 한 결과 행의 단위를 부서라고 적는다.
2. 빠지면 안 되는 부서를 왼쪽에 놓는다.
3. 같은 부서번호로 사원을 연결한다.
4. 부서번호·이름으로 묶고 실제 사원키를 센다.
5. 최대−최소를 계산하고 결과 순서를 지정한다.

## 4. 전체 풀이와 실행

[준비문 포함 전체 SQL](실습/책형_복습/20_SQL_종합실습.sql)을 제공한다. 가상 자료 준비는 [스타일 장3절](19_SQL_실무_코딩스타일.md#example)에 전부 있다. 같은 연습 연결에서 준비한 뒤 아래 조회를 실행한다.

<details>
<summary>풀이 — 먼저 자신의 SQL을 적은 뒤 펼치기</summary>

```sql
SELECT
    d.deptno,
    d.dname,
    COUNT(e.empno) AS people,
    MAX(e.sal) - MIN(e.sal) AS sal_gap
FROM book_dept d
LEFT JOIN book_emp e ON e.deptno = d.deptno
GROUP BY d.deptno, d.dname
ORDER BY d.deptno;
```

| 번호 | 부서 | 인원 | 급여 차이 |
| --- | --- | --- | --- |
| 10 | ALPHA | 1 | 0 |
| 20 | BETA | 3 | 2000 |
| 30 | GAMMA | 2 | 100 |
| 40 | EMPTY | 0 | NULL |

한 명인 ALPHA의 최고·최저는 같은1300이므로 차이0이다. BETA는3000−1000=2000, GAMMA는1600−1500=100이다. EMPTY는 사원이 없어 인원0이지만 급여 차이는NULL이다. 0명과 차이0원을 자동으로 같은 뜻으로 만들지 않는다. 결과의 한 행은 사원이 아니라 부서다.

</details>

## 5. 자료가 결과가 되는 과정

FROM의 부서 → LEFT JOIN으로 사원 연결 → 같은 부서 그룹 → 실제 사원키 COUNT·최대와 최소 → 결과 열 → 부서번호 정렬이다. EMPTY는 사원열이NULL인 한 조합행으로 남는다. COUNT(*)라면 그 한 행을1로 세므로 실제 인원과 다르다. COUNT(e.empno)는NULL을 제외해0이다.

ALPHA의 차이0은 한 명의 급여가 같아서 나온 계산값이다. EMPTY의NULL은 계산에 넣을 급여가 없다는 상태다. 둘을 같은 뜻으로 표시할지는 별도 업무 정책이다.

## 6. 한 가지 변경 실험

| 변경 | 예상 | 설명 |
| --- | --- | --- |
| 내부 JOIN으로 | EMPTY 사라짐 | 보존 요구 불충족 |
| COUNT(*)로 | EMPTY 인원1 | 빈 조합행을 셈 |
| HAVING COUNT(e.empno)>=2 | BETA·GAMMA | 집계 후 그룹 제한 |
| WHERE e.sal>=1500 | ALPHA·EMPTY 빠짐 | 입력행 제한·외부조인 영향 |
| 별칭만 변경 | 값 동일 | 표현 변경 |

각 실험은 기본 상태로 돌아가 하나씩 한다. 정답 숫자뿐 아니라 어느 단계에서 행·그룹이 빠졌는지 적는다.

## 7. 원본과 비교하고 채점

실제 초기 원본 데이터에서는 ACCOUNTING 차이 3700, RESEARCH 2200, SALES 1900이다. 내 원본에는 빈 부서까지 보는 LEFT 추가 풀이가 있다. 새 book_ 자료와 숫자가 다른 이유는 입력이 다르기 때문이다. 강사님·내 원본의 같은 조건과 차이는 [실제 문제 비교](실습_SQL_원본문제_비교.md)에서 읽는다.

채점은 부서 보존·정확한 집계 키·NULL 정책·그룹 기준·정렬·설명으로 나눈다. 예쁘게 줄을 맞췄지만 WHERE에서 빈 부서를 제외했다면 요구를 만족하지 못한다. 짧은 SQL이라고 항상 더 좋은 것도 아니다.

## 8. 출처·추가 학습·검증 범위

📚 [MariaDB JOIN](https://mariadb.com/docs/server/reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/joins/join-syntax)·[COUNT](https://mariadb.com/docs/server/reference/sql-functions/aggregate-functions/count) 의미를 확인했다. 새 자료·풀이·설명은 수업 문법으로 구성했다.

💡 **TIP · 수업 범위 밖:** 보고서 성능 측정·상세 인덱스 설계·동시성·장기 집계 정책은 선택 학습이다. 기본 목표를 그 기능들로 대체하지 않는다.

결과·변경 시나리오는 SQLite 메모리 DB에서 교차 확인하고 MariaDB 문법과 대조했다. MariaDB 서버 실행·성능을 확인한 것은 아니다. [SQL 목차](README.md) · [다음: FastAPI](../06_FastAPI/README.md)
