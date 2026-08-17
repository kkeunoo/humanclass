from pydantic import BaseModel

# pydantic BaseModel 사용해보기, 미리 자료형 선언
class Todo(BaseModel) :
    value1 : int
    value2 : str