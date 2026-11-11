from langchain_core.messages import AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda

hybrid = {30: {'title': '복습용 영화', 'score': 0.03252}}
prompt = ChatPromptTemplate.from_messages([
    ('system', '주어진 후보만 설명한다.'), ('human', '후보: {hybrid}'),
])


def fixed_model(messages):
    text = messages.to_messages()[-1].content
    assert '복습용 영화' in text and '0.03252' in text
    return AIMessage(content='복습용 영화 · RRF 점수 0.03252')


chain = prompt | RunnableLambda(fixed_model) | StrOutputParser()
print(chain.invoke({'hybrid': hybrid}))
