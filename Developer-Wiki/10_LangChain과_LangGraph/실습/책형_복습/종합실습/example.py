from typing import TypedDict

from langchain_core.messages import AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from langgraph.graph import END, START, StateGraph


class State(TypedDict, total=False):
    question: str
    movie_ids: list[int]
    recommends: list[str]
    explain: str
    error: str


def find_candidates(_state):
    return {'recommends': ['복습용 액션 영화']}


def validate(state):
    return 'find' if state.get('movie_ids') else 'error'


def fixed_model(prompt):
    assert '복습용 액션 영화' in prompt.to_messages()[-1].content
    return AIMessage(content='복습용 액션 영화를 추천합니다.')


prompt = ChatPromptTemplate.from_messages([('human', '{question} 후보: {recommends}')])
chain = prompt | RunnableLambda(fixed_model) | StrOutputParser()


def explain(state):
    return {'explain': chain.invoke(state)}


graph = StateGraph(State)
graph.add_node('find', find_candidates)
graph.add_node('explain', explain)
graph.add_node('error', lambda _state: {'error': '영화 ID가 필요합니다.'})
graph.add_conditional_edges(START, validate, {'find': 'find', 'error': 'error'})
graph.add_edge('find', 'explain')
graph.add_edge('explain', END)
graph.add_edge('error', END)

app = graph.compile()
for ids in ([10], []):
    final = app.invoke({'question': '비슷한 영화?', 'movie_ids': ids})
    print(final.get('explain') or final.get('error'))
