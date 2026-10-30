# SQL 실제 문제 — 요구 문장의 대상·범위·빈 그룹을 코드로 옮기기 — 연습문제

[본문](../../실습_SQL_원본문제_비교.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원래 퀴즈·내 풀이와 구별하며, 새 book_emp 가상 데이터와 원본 EMP 초기 자료를 혼동하지 않는다.

## 목표와 준비

연도 안팎 조건·부서별 급여차·기준 사원 조회·모든 등급 집계·등급과 부서 조건·자기 부서 평균의 실제 풀이를 설명한다. 강사님과 내 코드의 장단점을 요구 기준으로 판단한다.

[준비문 포함 전체 SQL](../책형_복습/실습_SQL_원본문제_비교.sql)을 제공한다. [본문 3절](../../실습_SQL_원본문제_비교.md#example)의 같은 연결·새 임시 표·입력 행을 확인한다. D 드라이브 원본 전체를 실행해 준비하는 문제가 아니다.

## 문제 1. 행·열·값 예상

```sql
SELECT ename FROM book_year WHERE sal=(
 SELECT MIN(sal) FROM book_year WHERE hiredate BETWEEN '1981-01-01' AND '1981-12-31'
) ORDER BY ename;
SELECT ename FROM book_year WHERE sal=(
 SELECT MIN(sal) FROM book_year WHERE hiredate BETWEEN '1981-01-01' AND '1981-12-31'
) AND hiredate BETWEEN '1981-01-01' AND '1981-12-31' ORDER BY ename;
SELECT g.grade,COUNT(*) AS joined_rows,COUNT(e.empno) AS people
FROM book_grade g LEFT JOIN book_emp e ON e.sal BETWEEN g.losal AND g.hisal
GROUP BY g.grade ORDER BY g.grade;
SELECT e.ename,e.sal FROM book_emp e
WHERE e.sal>(SELECT AVG(other.sal) FROM book_emp other WHERE other.deptno=e.deptno)
ORDER BY e.empno;
```

결과 행 수·열 의미·각 값을 적는다. 빈 결과 0행과 NULL 한 칸을 구별한다.

<details>
<summary>풀이</summary>

연도조건을 안쪽에만 쓰면 **A·B**, 바깥에도 쓰면 **A**다.

| 등급 | 조인 결과 행 수 COUNT(*) | 실제 인원 COUNT(e.empno) |
| --- | --- | --- |
| 1 | 1 | 1 |
| 2 | 3 | 3 |
| 3 | 2 | 2 |
| 4 | 1 | 0 |

자기 부서 평균 초과는 **BEN1600·CARA3000·ELLA3000**이다.

첫 반례의 B는 1980년 입사지만 1981년 최저 1000과 같아서 잘못 포함된다. 두 번째 쿼리가 바깥 연도를 더 검사해 제외한다. 빈 등급 4는 외부 조인으로 남은 한 행을 COUNT(*)가 1로 세지만 사원 키는 NULL이라 COUNT(e.empno)는 0이다. 마지막 쿼리는 현재 e의 deptno를 안쪽 other.deptno와 맞춰 각 부서 평균을 계산한다. 이들은 원본 초기 자료와 다른 새 반례다.

</details>

## 문제 2. 이유 설명

1. 1981년 최저를 안쪽에서만 구하면 충분한가?
2. 빈 외부 조인의 COUNT(*)는 왜 1인가?
3. COUNT(e.empno)가 0인 이유는?
4. 자기 부서 조건이 없으면 어떤 평균인가?

<details>
<summary>풀이</summary>

바깥 사원의 연도도 확인해야 한다. 보존된 빈 매칭 행 한 개를 센다. 오른쪽 사원 키가 NULL이기 때문이다. 전체 표 평균이 된다.

| 반례 | 빠진 확인 | 영향 |
| --- | --- | --- |
| 다른 연도 같은 최저 급여 | 바깥 연도 | 대상 아닌 사원 추가 |
| 빈 등급 | COUNT 대상 | 0명을 1명으로 표시 |
| 다른 부서 평균 | 상관 부서 키 | 개인의 기준 평균 변경 |

</details>

## 문제 3. 한 가지만 바꾸기

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| B 연도를 1981로 | 올바른 결과도 A·B | 대상 범위 내 동점 |
| 빈 등급에 사원 1명 추가 | 두 COUNT 모두 1 | 실제 매칭 생김 |
| 상관 부서 조건 제거 | 전체 평균 초과로 바뀜 | 그룹 대응 없음 |

한 행씩 골라 예상하고 실행한다. 다음 실험 전에 원래 준비 자료로 돌아간다.

<details>
<summary>막힐 때 확인</summary>

초기 자료에서 같은 결과면 조건 누락이 없다는 뜻은 아니다. 경계·빈 그룹·다른 그룹의 동점 반례를 생각한다. LEFT JOIN 뒤 COUNT(*)와 실제 사원 키 COUNT를 구별한다. 평균 표시와 조건 비교에 다른 반올림을 적용했는지도 본다.

</details>

## 채점과 복습

값만 맞히지 말고 대상·상태·조건·NULL·정렬을 설명한다. 원본 코드와 새 개선안을 구별한다. 이 예제의 공통 조회 결과는 SQLite 메모리 DB 교차 확인이며 MariaDB 서버 실행 확인은 아니다. 공식 문법과 DB별 설정의 차이를 본문에서 확인한다. TIP 선택 확장은 필수 정답이 아니다.
