from typing import TypedDict
from langgraph.graph import END, START, StateGraph


class State(TypedDict, total=False):
    movie_ids: list[int]
    route: str
    result: str


def select(_state):
    return {'route': 'CBF'}


def validate(state):
    return 'CBF' if state.get('movie_ids') else 'ERROR'


graph = StateGraph(State)
graph.add_node('select', select)
graph.add_node('cbf', lambda state: {'result': f"후보 입력 {state['movie_ids']}"})
graph.add_node('error', lambda _state: {'result': '영화 ID가 필요합니다'})
graph.add_edge(START, 'select')
graph.add_conditional_edges('select', validate, {'CBF': 'cbf', 'ERROR': 'error'})
graph.add_edge('cbf', END)
graph.add_edge('error', END)
app = graph.compile()
for input_state in ({'movie_ids': [10]}, {}):
    print(app.invoke(input_state)['result'])
