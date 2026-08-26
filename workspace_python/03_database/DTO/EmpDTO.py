# model들이 들어있는 곳 DTO
from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import field_validator, model_validator

class Emp3(SQLModel, table=True):
    # tablename이 없다면 클래스명이 테이블명이 됨
    # __tablename__ = 'emp' 

    empno: int = Field(primary_key = True)
    ename: str
    job: str
    # mgr: int | None = None # null이 있다면 none으로 처리하는 필터
    mgr: Optional[int] = None
    hiredate: str
    sal: float
    # comm: float | None = None
    comm: Optional[float] = None
    deptno: int = Field(
        foreign_key='dept3.deptno'
    )

class Emp_pr(SQLModel, table=True):
    # 아래처럼 하면 Auto increment가 가능함
    empno: int | None = Field(
        default=None, 
        primary_key=True
    )
    ename: str
    job: str
    mgr: Optional[int] = None
    hiredate: str
    sal: float
    comm: Optional[float] = None
    deptno: int

class Emp_pr_input(SQLModel):
    # 아래처럼 하면 Auto increment가 가능함
    empno: int | None = Field(
        default=None, 
        primary_key=True
    )
    ename: str
    job: str
    mgr: Optional[int] = None
    hiredate: str
    sal: float
    comm: Optional[float] = None
    deptno: int

    # 값을 검증해주는 데코레이터
    # 'comm'에 값을 넣기 전(mode='before')에 def함수를 실행시켜라
    @field_validator('comm', 'mgr', mode='before')
    @classmethod
    def empty_to_None1(cls, value):
        if value == "":
            return None
        else :
            return value
        # return None if value == "" else value
        # return value if value != "" else None

    @model_validator(mode='before')
    @classmethod
    def empty_to_None2(cls, value):
        return value if value != "" else None