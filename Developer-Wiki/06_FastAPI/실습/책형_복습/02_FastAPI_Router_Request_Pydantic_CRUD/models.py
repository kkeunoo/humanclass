from pydantic import BaseModel, Field

class Todo(BaseModel):
    id: int = Field(ge=1, le=100)
    item: str = Field(min_length=2, max_length=20)
