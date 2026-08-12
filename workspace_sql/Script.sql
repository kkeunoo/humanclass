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

-- where 조건식을 거짓으로 해서 column명만 볼 수도 있음
-- ctrl + 클릭으로 테이블명도 볼 수 있음
select *
from emp
where 1 != 1

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

select * from emp;

select * from emp
where comm = null;

select * from emp
where comm < 100;

-- Query에서 null상태는 'is null' 또는 'is not null'로 구분한다
select * from emp
where comm is null;

select * from emp
where comm is not null;

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

-- 집계 함수는 한 줄의 한 칸으로 나오며 group by와 잘 어울림
-- count는 특정 열 또는 행의 개수를 검색해줌, null은 빼고 세줌
select count(ename) from emp; 
select count(mgr) from emp;
select count(comm) from emp;
select count(*) from emp; -- *을 써서 모든 줄을 보는 경우가 많음

-- min, max는 각 최소값, 최대값이며 문자열에 사용해도 a-z순
select max(sal) from emp;
select min(sal) from emp;

-- 해당 컬럼의 합을 구할 때 사용
select sum(sal) from emp;

-- 해당 컬럼의 평균치를 구할 때 사용
select avg(sal) from emp;

-- 집계함수는 1줄로 셀 병합을 허용하지 않기 때문에 
-- 다른 여러 줄이 나오는 함수와 사용 시 원하는 결과를 얻기 어려움
select count(*), ename from emp;

-- length로 길이를 알 수 있음
select length(ename), ename from emp;

select * from emp
where length(ename) = 4;

-- substring(행/열, 시작, 개수)
-- 대상의 몇 번째부터 몇 개를 잘라오는게 substring
select substring(ename, 2, 3), ename from emp;
select substr(ename, 2, 3), ename from emp;

-- replace(행/열, 대상, 바꿀 문자열)
-- replace는 행/열 대상을 전부 바꿔줌
select replace(ename, 'A', '에이'), ename from emp;

-- lpad(행/열, 자릿수, 문자열)
-- 대상의 자릿수를 맞춰주고 남으면 채워주는 것이기 때문에 아래 3으로 하면 3글자로 줄어듦
select lpad(ename, 10, '#'), ename from emp; 
select lpad(ename, 3, '#'), ename from emp; 

select rpad(ename, 10, '#'), ename from emp; 

select lpad(sal, 10, '0'), ename from emp; 
select lpad(ename, 10, ' '), ename from emp; 

-- trim은 양쪽 공백을 제거해줌
select trim('  a b  c  ');

-- concat으로 column을 한 줄로 합칠 수 있음
-- Oracle에서는 ename || job으로 합치기 사용 할 수 있음
select concat(ename, job) from emp;
select concat(ename, ' ', job) from emp;
-- concat_ws(with seperator)로 구분자를 사용하여 합칠 수 있음
select concat_ws('-', ename, job, empno) from emp;

-- round는 반올림 할 수 있음, ','를 사용해서 소수점 범위도 지정할 수 있음
select round(3.14);
select round(3.145, 2);

-- ceil은 올림하는 것
select ceil(3.14);
select ceil(-3.14);

-- floor는 내림하는 것
select floor(3.14);
select floor(-3.14);

-- truncate는 두 번째 전달인자가 필수이며, 소수점 몇 자리인지 확인 후 버림
select truncate(-3.14, 0);

-- mod는 나머지를 구해줌
select mod(10, 3);

-- now(), sysdate()는 현재 시간을 알 수 있음
select now(); -- 서버시간
select sysdate();

-- date_format(시간, 양식) 으로 나오는 형식을 변경할 수 있음
select date_format(now(), '%Y년 %m월 %d일 %H시 %i분 %s초');

-- string의 일자를 date형태로 바꾸어 줌
select str_to_date('2026-08-07', '%Y-%m-%d');

-- ifnull(행/열, 기본값) 이면 null일 경우 기본값으로 바꿔줌
select ifnull(comm, 0), comm from emp;
select coalesce(comm, 0), comm from emp;

select sal * 12 + comm from emp;
select sal * 12 + ifnull(comm, 0) from emp;

-- 문제 _ ename의 앞 두 글자만 출력
select substr(ename, 1, 2), ename from emp;

-- ename의 앞 두 글자만 원본 그대로 출력하고,
-- 4개의 *표를 붙여서 출력
select rpad(substr(ename, 1, 2), 6, '*'), ename from emp;

-- ename의 앞 두 글자만 원본 그대로 출력하고
-- 나머지 이름 만큼의 *를 출력 
select rpad(substr(ename, 1, 2), length(ename), '*'), ename from emp;

-- case문
select * from emp;

-- case문은 end로 무조건 닫아주어야 함
-- when과 then으로 조건을 줘서 바꿀 수 있음
select 
	job, sal, 
	case job
		when 'CLERK' then sal * 1.05
		when 'SALESMAN' then sal * 1.03
		else sal
	end as upsal
from emp;

-- case옆에 바로 쓰지 않으면 where조건 if처럼 진행할 수 있음
select 
	job, sal, 
	case 
		when job = 'CLERK' then sal * 1.05
		when job = 'SALESMAN' then sal * 1.03
		else sal
	end as upsal
from emp;

-- if, null로 아래처럼 null일 때 0으로 바꿀 수 있음
select 
	sal, comm,
	case 
		when comm is null then 0
		else comm
	end
from emp;

-- distinct와 비슷한 결과물을 검색할 수 있음
select deptno from emp
group by deptno;

-- group by와 집계함수를 같이 쓰면 '그룹별'이 가능
select 
	deptno, count(*), sum(sal) 
from emp
group by deptno;

-- 이렇게 쓰면 각 첫 번째것만 나오기 때문에 상위에 있는것은 group by에 넣어줘야 함
select deptno, job
from emp
group by deptno;

-- group by에 있는것을 select에 사용할 수 있음
select deptno, job, count(*)
from emp
group by deptno, job;

select deptno, job
from emp
where deptno = 10
group by deptno, job;

select deptno, job
from emp
where deptno = 10
group by deptno, job
order by job;

select avg(sal) from emp;

-- 집계함수는 'select'에서만 사용할 수 있어 Error
/*
select 
	ename, sal, avg(sal)
from emp
where sal >= avg(sal);
*/

-- 부서, 직업 별 sal평균이 2000이상인 조건 식
select
	 avg(sal), deptno, job
from emp
group by deptno, job, sal
having avg(sal) >= 2000;

-- having은 group by에 조건식을 걸 수 있지만 실무에서 주로 사용하진 않음
select
	 avg(sal), deptno, job
from emp
group by deptno, job
having deptno = 10; 
-- where 조건을 having에 적을 수 있지만,
-- 통상 group by와 관련 된 것만 적는것이 좋다

-- and에 cnt나 count를 써버리면, from부터 실행되기 때문에
-- 어떤 column인지 알 수 없어 having에 조건식을 줘서 조회해야 함
-- 직업 별로 연봉 1,000이상인 사람이 3명 이상인 경우 출력 조건식
select
	job, count(*) cnt
from emp
-- and cnt >= 3
-- and count(*) >= 3
where sal >= 1000
group by job
having count(*) >= 3

/* 5번 실행 */ select job, 1 as num
/* 1번 실행 */ from emp
/* 2번 실행 */ where sal > 1000
/* 3번 실행 */ group by job
/* 4번 실행 */ having count(*) >= 3
/* 6번 실행 */ order by job desc, num

-- union으로 겹치는것을 제외하고 합쳐서 한 번에 보여줄 수 있음
select * from emp where deptno = 10
union
select * from emp where deptno = 10;

-- union all은 겹치더라도 나오게 함, union보다 활용도가 높음
select * from emp where deptno = 10
union all
select * from emp where deptno = 10;

select * from emp
where sal > 1250;

select sal 
from emp
where ename = 'WARD'

-- 서브쿼리로 중첩해서 사용할 수 있음
select * from emp
where sal > (select sal 
			 from emp
			 where ename = 'WARD');

-- 서브쿼리에서 column이 두개이거나, 여러 줄이면 안 됨
select * from emp
where sal > (select avg(sal) from emp);

-- 부서 별 최고 연봉자
-- 1. 부서 별 최고 연봉을 뽑아라
select max(sal)
from emp
group by deptno;

-- 아래처럼 서브쿼리로 넣어 한 번에 처리할 수 있음
select ename, sal
from emp
-- where sal = 3000 or sal = 2850 or sal = 5000;
where sal in (3000, 2850, 5000);

select ename, sal
from emp
where sal in (  select max(sal)
				from emp
			  	group by deptno);

select sal from emp where ename = 'SCOTT';
select * from salgrade;

select grade
from salgrade
where 3000 between losal and hisal

select * from dept;
-- select안에 select로 사용 할 수도 있다
select
	sal,
	ename,
	(	select grade
		from salgrade
		where (	select sal 
				from emp 
				where ename = 'SCOTT') 
		between losal and hisal) as grade
from emp where ename = 'SCOTT';

-- having 없이 서브쿼리로 해결
-- 1. 부서 별 평균 연보 출력
select avg(sal)
from emp
group by deptno;
-- 2. 부서 별 평균 연봉이 2000이상인 부서만 출력
select avg(sal) avg_sal
from emp
-- where avg_sal >= 2000 → 사용 불가하며, select 이후(group by)에 사용 가능
-- where avg(sal) >= 2000 → 집계함수는 사용 불가능
group by deptno
having avg(sal) >= 2000;

-- 서브쿼리 사용
-- from 에 서브쿼리를 넣었을 때 별칭 필요
-- 위에 having 사용한 것을 from에 넣어 사용할 수 있음
select *
from (
	select avg(sal) avg_sal
	from emp
	group by deptno
) a
where avg_sal >= 2000;


-- 이렇게 2개의 테이블을 이용하게 되면 곱연산(데카르트)되어 출력됨
select * 
from emp, dept;

-- 두 개의 테이블을 이용할 땐 아래와 같이 조건식에서 맞춰야 함
select * 
from emp, dept
where emp.deptno = dept.deptno;

-- 아래처럼 별칭을 주어서 사용할 수 있음
select * 
from emp e, dept d
where e.deptno = d.deptno;

-- Column 'deptno' in SELECT is ambiguous
-- 두 테이블에 이름이 같기 때문에 뭘 지칭하는건지 모르겠다는 Error 발생
/*
select ename, dname, deptno 
from emp e, dept d
where e.deptno = d.deptno;
*/

select e.ename, d.dname, e.deptno 
from emp e, dept d
where e.deptno = d.deptno;

select * from salgrade;

-- SMITH의 연봉 등급은? 정답 : 1
-- 이름, 월급, 등급, losal, hisal
select * from salgrade
where 800 >= losal and 800 <= hisal;

select sal from emp
where ename='SMITH'

select ename, sal, grade, hisal, losal
from emp e, salgrade s
-- where sal >= losal and sal <= hisal
where sal between losal and hisal
and ename='SMITH';

select * from emp;

select mgr 
from emp
where ename = 'SMITH';

select ename
from emp
where empno = (	select mgr 
				from emp
				where ename = 'SMITH');		
-- 위 코드를 같은 테이블을 동시 조인하여 결과값도 알 수 있다
-- mgr이 null인 것은 빠져서 결과값은 총 14개 중 13개만 나옴
select e2.ename, e1.ename
from emp e1, emp e2
where e1.mgr = e2.empno
and e1.ename = 'SMITH';

-- 문제 _ 
-- 모든 사람의 이름, 급여, 부서명, 급여 등급
select ename, sal, dname, grade
from emp e, dept d, salgrade s
where (e.deptno = d.deptno) 
and (e.sal between s.losal and s.hisal)
order by s.grade desc, sal desc;

-- ename, * 처럼 사용은 불가하고 다른 것과 같이 있다면 별칭으로 붙여줘야 함
select ename, ename from emp;
select ename, emp.* from emp;
select ename, e.* from emp e;

-- join을 쓸 때는 where가 아닌 on에 조건식 기재
select e.deptno
from emp e join dept d on(e.deptno = d.deptno);

-- using으로 같은 column을 합칠 수 있음
select deptno
from emp e join dept d using(deptno);

/*
select deptno
from emp e 
	join dept d 
	join salgrade s;  형태처럼 조인은 이어붙일 수 있음
*/

select e1.empno, e1.ename, e2.empno, e2.ename
from emp e1
	join emp e2 on e1.mgr = e2.empno;

select e1.empno, e1.ename, e2.empno, e2.ename
from emp e1
	left outer join emp e2 on e1.mgr = e2.empno;
	-- left outer는 왼쪽에 있는 column 대상이 한 번은 무조건 나오게 해주는 것

select e1.empno, e1.ename, e2.empno, e2.ename
from emp e1
	right outer join emp e2 on e1.mgr = e2.empno;
	-- SMITH ~ MILLER는 한 번 이상 다 나와야 하기 때문에 출력된 것이고, 부하가 없음

select * from dept;

-- 문제 
-- deptno, dname, empno, ename 출력
-- 모든 부서가 다 나오게 해야 함
-- 부서 번호 별 오름차순, 같다면 이름 오름차순
select d.deptno, dname, empno, ename
from dept d
	left outer join emp e on (d.deptno = e.deptno)
order by deptno asc, ename asc;

-- DDL의 시작 _ CREATE TABLE
-- desc TABLE은 구조를 알려주는 디스크립션 명령어
desc emp;

-- foreign key는 참조 할 테이블이 있어야 가능하기 때문에, PK만 먼저 쓴 것
-- 만약, dept2에 deptno가 10~40일 때 emp2에 값을 넣을 때 그 외의 것은 넣지 못하도록
-- unique + not null = primary key
create table emp2(
	empno int(4) primary key,
	ename varchar(10) not null,
	job varchar(9),
	mgr int(4),
	hiredate date,
	sal decimal(7,2), -- 총 7자리 중, 소수점 2자리
	comm decimal(7,2),
	deptno int(2)
);
select * from emp2;
desc emp2;

desc dept;
create table dept2(
	deptno int(2) primary key,
	dname varchar(14),
	loc varchar(13)
);
select * from dept2;
desc dept2;

-- 테이블 구조 복사 (as로 모든것을 가져올 수 있음)
create table emp_copy 
as select * from emp;

select * from emp_copy;
desc emp_copy;

-- 아래처럼 내용물 없이 False를 줘서 껍데기만 들고올 수 있음
create table emp_copy2
as select * from emp where 1 <> 1;

select * from emp_copy2;

create table dept3
as select * from dept where 1 != 1;
select * from dept3;

create table emp3 (
	empno int(4),
	ename varchar(10) not null,
	job varchar(9),
	mgr int(4),
	hiredate date,
	sal decimal(7,2),
	comm decimal(7,2),
	deptno int(2),
	primary key (empno), -- 여러 개가 필요할 때 직접적으로 안 주고 하단에 별도 작성 가능
	foreign key (deptno) references dept3(deptno) -- foreign key는 primary key만 잡힘
);

desc dept3;
-- 테이블 삭제
drop table dept3;

create table dept3(
	deptno int(2) primary key,
	dname varchar(14),
	loc varchar(13)
);
desc dept3;
desc emp3;
-- 이렇게 한 번 참조해두고 나면, dept3을 먼저 지울 수 없고
-- 지우게 된다면 emp3를 먼저 지우과서 dept3을 지워야 함 (emp3 → dept3를 바라보고 있기 때문)

-- ALTER TABLE (테이블 수정)
-- 열 추가 및 열 삭제
alter table emp3 
add gender varchar(10) not null default '남';
select * from emp3;

-- 열을 바꿀 때 자료형은 다시 써줘야 함
alter table emp3
change gender gender2 varchar(10);
select * from emp3;

-- 최신 Oracle방식은 자료형을 쓰지 않아도 됨
-- 단, 실무에서 먹히지 않는 곳도 있기 때문에 유의해야 함
alter table emp3
rename column gender2 to gender3;
select * from emp3;

alter table emp3
drop column gender;
select * from emp3;

-- rename to로 테이블명도 변경할 수 있다
alter table emp3
rename to emp4;
select * from emp3;
select * from emp4;

drop table emp4;
select * from emp4;
-- emp4를 먼저 지웠기 때문에, 참조되는 부모 dept3을 지울 수 있음
drop table dept3;
select * from dept3;

-- truncate 버림으로 테이블의 내용도 버릴 수 있음
-- 이후 배우는 delete는 롤백이 되지만, truncate는 롤백이 불가능
select * from emp_copy;
truncate table emp_copy;

select * from dept2;
drop table dept2;

select * from emp2;
drop table emp2;

create table dept2 (
	deptno int(2) primary key,
	dname varchar(14),
	loc varchar(13)
);
select * from dept2;

create table emp2 (
	empno int(4),
	ename varchar(10) not null,
	job varchar(9) default 'CLERK',
	mgr int(4),
	hiredate date default now(),
	sal decimal(7,2),
	comm decimal(7,2),
	deptno int(2),
	primary key (empno), 
	foreign key (deptno) references dept2(deptno)
);
select * from emp2;

insert into dept2
values (
	10,
	'휴먼',
	'천안'
);
select * from dept2;

-- column을 지정하지 않았을 경우에는 values에 모두 적어야 함
insert into emp2
values (
	1000, 
	'정근욱', 
	'MANAGER', 
	2000, 
	'2026-08-09', 
	4000,
	100,
	10
);
select * from emp2;

-- 기존에 default가 되어있거나, NOT NULL이 아닌 경우 넣고 싶은 column 값만 넣을 수 있음
insert into emp2 (empno, ename, sal, comm, deptno)
values (1001, '홍길동', 4100, 150, 10);
select * from emp2;

-- ename은 insert 누락 시 NULL이 들어가나 NOT NULL 제한이 있기에 에러 발생
-- SQL Error [1364] [HY000]: (conn=5) Field 'ename' doesn't have a default value
-- insert into emp2 (empno, sal, comm, deptno)
-- values (1001, 4100, 150, 10);

-- Primaty key이며 unique와 not null 형태이기 때문에 중복값이 들어갈 수 없는 오류(Duplicate) 발생
-- SQL Error [1062] [23000]: (conn=5) Duplicate entry '1001' for key 'PRIMARY'
-- insert into emp2 (empno, ename, sal, comm, deptno)
-- values (1001, '홍길동', 4100, 150, 10);

-- dept 테이블에 deptno '20'값이 없기 때문에 발생되는 에러
-- SQL Error [1452] [23000]: (conn=5) Cannot add or update a child row: 
-- a foreign key constraint fails (`human`.`emp2`, CONSTRAINT `1` FOREIGN KEY (`deptno`) REFERENCES `dept2` (`deptno`))
-- insert into emp2 (empno, ename, sal, comm, deptno)
-- values (1002, '홍길동', 4100, 150, 20);

insert into emp2 (empno, ename, sal, comm, deptno)
values 
(1012, '홍길동2', 4100, 150, 10),
(1013, '홍길동3', 4100, 150, 10),
(1014, '홍길동4', 4100, 150, 10);
select * from emp2;

-- UPDATE
-- where문을 사용하지 않았을 땐 모든 값이 바뀌기 때문에 조심해야 함
update emp2
set 
	sal = 1000,
	comm = 200;
select * from emp2;

update emp2
set 
	sal = sal * 1.1,
	comm = comm * 1.2
where empno = 1002;
select * from emp2;

-- dept 테이블에서도 서로 참조를 하고 있기 때문에 변경할 수 없음
-- SQL Error [1451] [23000]: (conn=5) Cannot delete or update a parent row: 
-- a foreign key constraint fails (`human`.`emp2`, CONSTRAINT `1` FOREIGN KEY (`deptno`) REFERENCES `dept2` (`deptno`))
select * from dept2;
update dept2
set deptno = 20
where deptno = 10;

-- DELETE
-- delete from table로 원하는 대상만 제거할 수 있음 (from은 필수)
delete from emp2
where empno = 1002;
select * from emp2;

delete from emp2;
select * from emp2;

-- DDL은 자동 commit이기 때문에 그 시점 전으로는 되돌릴 수 없음
-- rollback은 마지막 DDL(CREATE, ALTER, DROP)을 실행하기 전으로 롤백해줌
rollback;
select * from emp2;
select * from dept2;

commit;
rollback;

delete from emp2
where empno = 1012;

rollback;
select * from emp2;

select * 
from emp e
	left outer join emp e2 on (e.mgr = e2.empno)
	left outer join dept d on (e.deptno = d.deptno)
order by e.ename desc;

select * from emp
where deptno = 10;

-- index 생성
create index idx_emp_empno_desc
on emp(empno desc);

-- index를 타면 emp (index) 형식으로 표시된다
-- 보통 데이터가 많았을 때 검색 속도가 빨라짐, 최신순은 역순(desc)로 검색하기도 함
select * from emp
order by empno desc;

create index idx_emp_deptno
on emp(deptno);

select * from emp
where deptno = 10;

-- 강제로 index를 타게 할 수 있음
select * 
from emp force index (idx_emp_deptno)
where deptno = 10
order by deptno;

-- length로 확인하게 되면 문자열의 Byte가 나옴(한글은 3Byte)
select length('한구');
select length('ab');

select char_length('한구');

select max(empno)+1 from emp;

-- increment는 Primary Key일때만 가능
-- 아래처럼 함수형태로 만들어서 사용할 수 있다
create table emp_auto (
	empno int auto_increment, -- increment를 사용하면 자동증가 시킬 수 있음
	ename varchar(50),
	
	primary key(empno)
);

insert into emp_auto(ename)
values('근욱');
select * from emp_auto;

insert into emp_auto(ename)
values('근욱2');
select * from emp_auto;

-- 무한 대댓글
select 
	empno, ename, mgr, 1 as Level
from emp
where mgr is null
union all
select 
	empno, ename, mgr, 2 as Level
from emp
where mgr = 7839;

-- 아래처럼 재귀함수로 각 Level을 부여할 수 있다
with recursive emp_recu as (
	select 
		empno, ename, mgr, 
		lpad(ename, length(ename), ' '),
		1 as level,
		cast(ename as char(200)) as sort_key
	from emp
	where mgr is null
	union all
	select
		e.empno, e.ename, e.mgr, 
		lpad(e.ename, er.level*4+length(e.ename), ' '),
		er.Level+1 as level,
		concat(er.sort_key, '-', cast(e.ename as char(200))) as sort_key
	from emp e
		join emp_recu er on (e.mgr = er.empno)
)
select * from emp_recu
order by sort_key;

select * from emp;
select * from dept;
select * from salgrade;

-- 문제1 _ 1981년에 입사한 사원 중에서 급여가 가장 낮은 사원을 조회하시오.
select * from emp;
desc emp;

select * from emp
where substr(HIREDATE, 1, 4) = '1981'
order by sal asc;

-- 문제1 최종풀이
select ename, sal, hiredate 
from emp
where sal = (	select min(sal)
				from emp
				where substr(HIREDATE, 1, 4) = '1981');

-- 문제1 개선풀이
select ename, sal, hiredate 
from emp
where sal = (	select min(sal)
				from emp
				where hiredate 
					between date '1981-01-01' and date '1981-12-31');

-- 문제2 _ 각 부서별 급여가 가장 높은 사원과, 가장 낮은 사원의 차이를 조회하시오.
-- 부서명, 차이 금액 출력
select * from emp e;
select * from dept;

-- 문제2 최종풀이
select d.dname, max(e.sal) - min(e.sal) as salCalc
from emp e join dept d using(deptno)
group by d.deptno, d.dname;

-- 문제2 각 부서별? 빈 부서도 포함해보기
select d.dname, max(e.sal) - min(e.sal) as salCalc
from dept d 
	left outer join emp e using(deptno)
group by d.deptno, d.dname;

/* -- 값 확인용
select *
from emp
where sal = (
	select min(sal)
	from emp
	where deptno = 10
)

select *
from emp
where sal = (
	select max(sal)
	from emp
	where deptno = 10
)
*/

-- 문제3 _ BLAKE보다 높은 연봉을 받는 사람들 출력
select * from emp;

select sal from emp
where ename = 'BLAKE';

-- 문제3 최종풀이
select ename, sal from emp
where sal > (	select sal from emp
				where ename = 'BLAKE');

-- 문제4 _ JONES와 같은 JOB을 가진 사람들을 출력
select * from emp;

select job from emp
where ename = 'JONES';

-- 문제4 최종풀이
select ename, job from emp
where job = (	select job from emp
				where ename = 'JONES');

-- 문제5 _ 급여 등급 별 사원 수를 등급 오름차순으로 정렬
-- 단, 모든 등급을 표시한다 (몇 등급에 몇 명)
select * from emp;
select * from salgrade;

-- 문제5 최종풀이
select s.grade, count(e.ENAME) as gradeCount
from salgrade s left outer join emp e
on (e.sal between s.losal and s.hisal)
group by s.grade
order by s.grade asc;

-- 문제6 _ 이름, 급여, 급여 등급, 부서 이름 조회
-- 단, 급여 등급이 3 이상만 조회 (급여 등급 내림차순, 같은 경우 급여 내림차순)
-- 급여가 같은 경우 이름 내림차순
-- 문제6 최종풀이
select * from emp;
select * from salgrade;
select * from dept;

select e.ename, e.sal, s.grade, d.dname
from emp e join salgrade s join dept d on (e.deptno = d.deptno) and (e.sal between s.losal and s.hisal)
where s.grade >= 3
-- group by e.ename
order by s.grade desc, e.sal desc, e.ename desc; 

-- 문제6 개선
select e.ename, e.sal, s.grade, d.dname
from emp e 
	join dept d
		on (e.deptno = d.deptno)
	join salgrade s
		on (e.sal between s.losal and s.hisal)
where s.grade >= 3
order by 
	s.grade desc, 
	e.sal desc, 
	e.ename desc; 

-- 문제7 _ 부서명이 SALES인 사원 중, 급여 등급이 2또는 3인 사원을 급여 내림차순으로 정렬
select * from emp;
select * from dept;

-- 문제7 최종풀이
select e.ename, e.sal, s.grade, d.dname
from emp e join dept d join salgrade s on (e.deptno = d.deptno) and (e.sal between s.losal and s.hisal)
where d.dname = 'SALES' and (s.grade = 2 or s.grade = 3)
order by e.sal desc;

-- 문제7 개선
select e.ename, e.sal, s.grade, d.dname
from emp e 
	join dept d 
		on (e.deptno = d.deptno)
	join salgrade s
		on (e.sal between s.losal and s.hisal)
where d.dname = 'SALES' 
	and (s.grade = 2 or s.grade = 3)
order by e.sal desc;




-- 시험문제 ------------------------------------------------------
select e.ename, e.sal, d.dname
from emp e
join dept d on e.deptno = d.deptno
where e.sal > 2000
order by sal;

select e.ename, e.sal, s.grade
from emp e
join dept d on e.deptno = d.deptno
join salgrade s on e.sal between s.losal  and s.hisal
where e.sal between 1000 and 3000
order by sal;

select e.ename, e.hiredate, d.dname
from emp e
join dept d on e.deptno = d.deptno
order by hiredate;

select e.ename, d.dname, e.sal, s.grade
from emp e
join dept d on e.deptno = d.deptno
join salgrade s on e.sal between s.losal and s.hisal
where s.grade >= 3
order by e.sal desc;

select e.ename, d.dname, e.sal, (
	select round(avg(e2.sal),0)
	from emp e2
	where e2.deptno = e.deptno
) as salAvg
from dept d
join emp e on e.deptno = d.deptno
where e.sal > (
	select avg(e2.sal)
	from emp e2
	where e2.deptno = e.deptno
)
order by d.dname, e.sal desc;
-- 시험문제 ------------------------------------------------------
-- 위는 최종본

select d.dname, avg(e.sal) as salCalc
from emp e join dept d using(deptno)
group by d.deptno, d.dname;

select ename,dname,sal,a.avgsal
from emp e1, (
	select deptno, avg(sal) as avgSAl
	from emp e2
	group by deptno
) a
join dept d using(deptno)
where e1.sal > a.avgSal
and e1.deptno = a.deptno
order by dname, sal desc;


/*
 select e.ename, d.dname, e.sal
from emp e
join dept d on e.deptno = d.deptno
where e.sal > (
	select avg(e.sal)
	from emp e
	join dept d on e.deptno = d.deptno
	where e.deptno = (
		select deptno
		from emp e
		join dept d using(deptno)
		group by deptno
	)
)
group by e.ename;

select e.ename, d.dname, e.sal
from emp e
join dept d on e.deptno = d.deptno
where e.deptno = 10 and e.sal > (
	select avg(e.sal)
	from emp e
	group by e.deptno
);
*/



select * from emp;
desc emp;
desc dept;
desc salgrade;

commit;





