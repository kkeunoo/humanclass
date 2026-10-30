from typing import Optional
from sqlmodel import SQLModel, Field
from pydantic import field_validator

class BookEmp(SQLModel, table=True):
    empno: int = Field(primary_key=True)
    ename: str
    deptno: int
    sal: float
    comm: Optional[float] = None

class EmpInput(SQLModel):
    empno: int
    ename: str
    deptno: int
    sal: float
    comm: Optional[float] = None

    @field_validator('comm', mode='before')
    @classmethod
    def empty_to_none(cls, value):
        return None if value == '' else value
