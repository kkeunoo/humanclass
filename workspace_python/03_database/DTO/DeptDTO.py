from sqlmodel import SQLModel, Field
from typing import Optional

class Dept3(SQLModel, table=True):
    deptno: int = Field(primary_key=True)
    dname: str
    loc: str
    
# class Dept_pr(SQLModel, table=True):
#     deptno: int = Field(primary_key=True)
#     dname: str
#     loc: str