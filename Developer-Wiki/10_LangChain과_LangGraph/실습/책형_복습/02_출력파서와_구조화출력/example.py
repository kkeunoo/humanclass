from langchain_core.messages import AIMessage
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from pydantic import BaseModel


class Recipe(BaseModel):
    food: list[str]
    steps: list[str]


parser = PydanticOutputParser(pydantic_object=Recipe)
prompt = ChatPromptTemplate.from_messages([
    ('system', '{format_instructions}'), ('human', '{dish}'),
]).partial(format_instructions=parser.get_format_instructions())


def fixed_model(_prompt):
    return AIMessage(content='{"food":["계란"],"steps":["삶기"]}')


model = RunnableLambda(fixed_model)
value = (prompt | model | parser).invoke({'dish': '삶은 계란'})
print(type(value).__name__, value.food, value.steps)
text = (prompt | model | StrOutputParser()).invoke({'dish': '삶은 계란'})
print('문자열로 사용:', isinstance(text, str))
