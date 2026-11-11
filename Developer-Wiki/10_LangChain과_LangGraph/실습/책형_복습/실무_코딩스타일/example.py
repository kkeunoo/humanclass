from pydantic import BaseModel, ConfigDict, Field, ValidationError


class RecommendationState(BaseModel):
    model_config = ConfigDict(extra='forbid')
    question: str
    recommends: list[dict] = Field(default_factory=list)


print(RecommendationState(question='영화 추천').recommends)
try:
    RecommendationState.model_validate({'question': '영화 추천', 'recommedns': []})
except ValidationError as error:
    print(error.errors()[0]['loc'][0], error.errors()[0]['type'])
