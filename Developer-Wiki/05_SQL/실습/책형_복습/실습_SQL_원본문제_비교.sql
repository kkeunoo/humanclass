DROP TEMPORARY TABLE IF EXISTS book_emp;
CREATE TEMPORARY TABLE book_emp (
    empno INT PRIMARY KEY, ename VARCHAR(20), job VARCHAR(20),
    mgr INT, sal DECIMAL(8,2), comm DECIMAL(8,2), deptno INT
);
INSERT INTO book_emp VALUES
(1,'ADA','CLERK',3,1000,NULL,20),
(2,'BEN','SALESMAN',3,1600,300,30),
(3,'CARA','MANAGER',NULL,3000,NULL,20),
(4,'DAN','CLERK',3,1300,0,10),
(5,'ELLA','ANALYST',3,3000,NULL,20),
(6,'FINN','SALESMAN',3,1500,0,30);
DROP TEMPORARY TABLE IF EXISTS book_dept;
CREATE TEMPORARY TABLE book_dept (deptno INT PRIMARY KEY, dname VARCHAR(20));
INSERT INTO book_dept VALUES (10,'ALPHA'),(20,'BETA'),(30,'GAMMA'),(40,'EMPTY');
DROP TEMPORARY TABLE IF EXISTS book_grade;
CREATE TEMPORARY TABLE book_grade(grade INT PRIMARY KEY,losal INT,hisal INT);
INSERT INTO book_grade VALUES(1,0,1200),(2,1201,2000),(3,2001,4000),(4,4001,9999);
DROP TEMPORARY TABLE IF EXISTS book_year;
CREATE TEMPORARY TABLE book_year(ename VARCHAR(10),hiredate DATE,sal INT);
INSERT INTO book_year VALUES('A','1981-02-01',1000),('B','1980-02-01',1000),('C','1981-03-01',1500);

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
