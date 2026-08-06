-- 주석
/* 
여러 줄 주석

EMPNO : 사원번호
MGR : 상사의 EMPNO
HIREDATE : 고용일
SAL : 연봉
COMM : 보너스
DEPTNO : 부서번호

SQL에서는 []를 써도되고 생략도 가능

SELECT [DISTINCT|ALL] 열_리스트
FROM 테이블_리스트
WHERE 검색_조건식
GROUP BY 그룹_기준열_리스트
HAVING 그룹_조건식
ORDER BY { 정열_기준열 [ASC|DESC][.] }
6개의 절로 사용 가능

*/

-- 전체 사원
select * from emp;
-- 부서 별
select * from dept;
-- 연봉 등급표
select * from salgrade; 

select empno from emp;

select 
	empno, 
	ename
from 
	emp;

select job from emp;
-- distinct로 중복 결과를 하나만 보이게 할 수 있다
select distinct job from emp; 

-- as로 가져오는 열 리스트의 이름을 변경할 수 있음
select job as 직업 from emp;
-- as로 띄어쓰기가 포함되는 경우 ''는 필수로 사용해야 함
select job as '직업 이름' from emp;
-- as도 생략이 가능하다
select job '직업 이름' from emp;

-- select에서 사칙연산을 이용하면 해당 값도 볼 수 있음
select sal, sal*12 from emp;

-- select에 바로 대입해도 값은 나오게 할 수 있음
select 100*12;

-- 기존 NULL에는 더하거나 빼도 NULL로 유지됨
select sal, comm , sal + comm from emp;
-- select ename+sal from emp;

select * from emp;

-- where로 조건을 걸어 볼 수 있음
select * 
from emp
where deptno = 20;

-- where의 값일 땐 '대/소문자'를 구분 함, and로 여러가지의 조건
select * 
from emp
where deptno = 20 and job = 'CLERK';

-- job이 CLERK이거나, deptno이 20인 사람은 or로 출력
select * from emp
where deptno = 20 or job = 'CLERK';

-- and가 or보다 우선순위이기 때문에, 필요 시 괄호 활용
-- 아래는 deptno = 20 and job = 'CLERK' 가 먼저 필터링 됨
select * from emp
where deptno = 30 or deptno = 20 and job = 'CLERK';

select * from emp
where (deptno = 30 or deptno = 20) and job = 'CLERK';

select * from emp
where sal = 3000;

-- not은 != , <>도 사용할 수 있음
select * from emp
where sal != 3000;

select * from emp
where sal <> 3000;

select * from emp
where not (sal = 3000);

-- 문제1 _ 급여가 2,000이상이고 3,000미만인 사원
select * from emp
where SAL >= 2000 and SAL < 3000;

-- between을 쓰면 범위를 지정해서 볼 수 있음
-- between A and B 는 이상/이하만 가능
select * from emp
where sal between 2000 and 3000;

-- 문제2 _ job이 CLERK 이거나 급여가 2,000초과 이면서 부서번호가 10인 사원만 출력
select * from emp
where job = 'CLERK' or (SAL > 2000 and DEPTNO = 10);

-- where에서 컬럼이 같고 or일 때 줄일 수 있는 방법 (in)
-- select * from emp
-- where deptno = 20 or deptno = 30
select * from emp
where deptno in (20, 30)

select * from emp
where deptno not in (20, 30)

-- % 는 모든 글자를 뜻 함(심지어 글씨가 없더라도 포함)
-- '문자열%', '%문자열'로 문자열로 시작하거나 끝나는 값을 검색할 수 있음
select * from emp
-- where ename like 'SCOTT';
where ename like 'S%';

select * from emp
where ename like '%N';

-- '%문자열%'은 A로 시작하거나, 끝나거나, 포함한 검색 값
select * from emp
where ename like '%AM%';

-- '_' underscore는 한 글자 아무거나이고, 두번째 글자가 L인 값을 검색
select * from emp
where ename like '_L%';

-- 문제4 _ 이름이 5글자인 사람만 출력 (나중에 length가 따로 있음)
select * from emp
where ename like '_____';

select 'HUMAN';
select lower('Human');
select upper('Human');

-- 문제5 _ 사용자가 'Am'을 이용해서 am이 이름 중간에 들어가는 사람만 출력
-- MariaDB에서 대/소문자를 구분하지 않아 현재 출력값은 같음
select * from emp
where upper(ename) like upper('%Am%');
select * from emp
where lower(ename) like lower('%Am%');

-- 문제6 _ 부서 10 또는 20의 사원 중, 이름에 A가 들어가는 사원만 출력
select * from emp
where (deptno in (10,20)) and ename like '%A%'


-- order by로 정렬을 할 수 있음 
-- ASC:오름차순 → 생략 가능
select * from emp
order by sal asc;

-- DESC:내림차순 → 생략 가능
select * from emp
order by sal desc;

select * from emp
order by deptno;

-- column별 asc, desc를 부여할 수 있음
-- 앞의 desc를 먼저 적용하고 겹치는것이 나오면 뒤 asc 적용
select * from emp
order by deptno desc, job;

-- order by에 여러 칼럼인 경우 왼쪽부터 적용되고 동일한 값이 있는 경우 다음 조건 적용
-- deptno를 정렬하고, job을 정렬하고, empno를 정렬
select * from emp
order by deptno desc, job asc, empno;

-- 각 절의 순서를 지켜야 함, where이 order by 뒤에 갈 순 없음
select * from emp
where sal > 1000
order by deptno desc, job asc, empno;

-- limit에 인자가 1개일 경우 보여 줄 검색 결과의 rows를 제한할 수 있음
select * from emp
where sal > 1000
order by deptno desc, job asc, empno
limit 3;

-- limit [offset][rows]
-- limit에 인자를 2개 줄 경우, offset만큼 건너 뛴 rows만큼 보여줌
select * from emp
where sal > 1000
order by deptno desc, job asc, empno
limit 5, 3;

-- 문제3 _ 부서 번호가 20 또는 30인 사원 중에서
-- 연봉이 2,000 ~ 3,000 사이(포함)인 사원의
-- 연봉이 작은 순으로 출력하시오
-- 연봉이 같으면 이름을 내림차순으로 정렬
select * from emp
where (deptno = 20 or deptno = 30) and (sal between 2000 and 3000)
order by sal, ename desc;





