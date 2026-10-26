# 20. SQL 종합실습 — 부서별 급여 차이 읽기

[SQL 목차](README.md) · [원본 문제와 내 실제 풀이](실습_SQL_원본문제_비교.md)

강사님 `Script.sql`의 7개 실제 문제와 내 풀이가 이 단원의 **원본 실습**이다. 이 장은 그중 [부서별 최고·최저 급여 차이](실습_SQL_원본문제_비교.md#section-2)를 바탕으로 SELECT·JOIN·GROUP BY를 다시 조합한 **새 복습**이다. 원본 문제의 문장이나 당시 제출 풀이로 표시하지 않는다.

## 풀 문제

학습용 `EMP`와 `DEPT`에서 부서 이름, 그 부서의 가장 높은 급여와 가장 낮은 급여의 차이를 조회한다. 먼저 `EMP.DEPTNO`와 `DEPT.DEPTNO`를 연결하고, 부서별로 묶는다. 결과 숫자는 현재 학습 DB의 행에 따라 달라지므로 특정 액수를 정답으로 외우지 않는다.

1. 두 표를 연결하지 않고 `FROM emp, dept`만 적으면 왜 행 수가 커지는가?
2. `MAX(sal) - MIN(sal)`을 부서별로 계산하려면 무엇을 `GROUP BY`에 적어야 하는가?
3. 강사님 풀이의 쉼표 조인과 내 풀이의 `JOIN ... USING(deptno)`에서 같은 관계를 만드는 조건은 무엇인가?

<details>
<summary>예시 풀이 — 먼저 직접 작성한 뒤 펼치기</summary>

```sql
-- 원본 발췌가 아닌 수업 내용의 재구성
SELECT d.dname, MAX(e.sal) - MIN(e.sal) AS salary_gap
FROM emp e
JOIN dept d ON e.deptno = d.deptno
GROUP BY d.deptno, d.dname;
```

두 표는 같은 `deptno`끼리 연결한다. `d.deptno, d.dname`으로 부서를 묶은 뒤 급여의 최고·최저를 계산한다. 내 실제 풀이의 `USING(deptno)`는 두 표의 같은 이름 열을 연결하는 다른 표기다. 강사님 원본의 쉼표 조인도 `WHERE emp.deptno = dept.deptno`가 있어야 같은 관계가 된다.

</details>

## 원본과 비교하기

[실제 문제 비교](실습_SQL_원본문제_비교.md#section-2)에서는 강사님 코드와 내 코드를 그대로 읽는다. 내 코드에는 **빈 부서까지 포함해 보기**라는 추가 시도가 있으며, 빈 부서를 포함할 때의 조인과 집계 결과는 기본 문제와 다르다. 먼저 위 기본 결과를 설명하고 [외부 조인](13_SQL_Outer_JOIN과_Self_JOIN.md)에서 범위를 넓힌다.

## 추가로 알면 좋은 것

대용량 조회 성능이나 운영 DB에 대한 변경 검토는 이 새 복습의 기본 목표가 아니다. 이전 Wiki가 만든 별도 8단계 프로젝트도 실제 강사님 문제와 혼동하지 않도록 [범위 분류](추가편_기존자료_학습범위_분류.md)에 남긴다.
