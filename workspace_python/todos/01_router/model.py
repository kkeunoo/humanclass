from pydantic import BaseModel, Field

# pydantic BaseModel 사용해보기, 미리 자료형 선언
class Todo(BaseModel) :
    value1 : int
    value2 : str

# POST에서 Body영역으로 들어오는것을 잡아주는것들 Field로 쓸 수 있다
class Todo2(BaseModel) :
    id : int = Field(ge=1, le=100)
    item : str = Field(min_length=2, max_length=20)

class TodoItems(BaseModel) :
    todoID : int
    todoITEM : str