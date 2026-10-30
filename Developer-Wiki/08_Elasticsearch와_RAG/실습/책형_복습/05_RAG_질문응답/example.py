from rag_tools import ask_rag

calls = []


def fixed_search(question):
    if question != '메모리는?':
        return {'results': []}
    return {'results': [{'document': {
        'id': 1, 'chunk_index': 0, 'title': '노트북 A', 'content': 'RAM은 16GB입니다.',
    }, 'score': 0.03}]}


def fixed_generate(prompt):
    calls.append(prompt)
    return '고정 응답: RAM은 16GB입니다.'


print(ask_rag('메모리는?', fixed_search, fixed_generate))
print('질문 전달:', '메모리는?' in calls[0])
print('본문 전달:', 'RAM은 16GB입니다.' in calls[0])
print(ask_rag('무게는?', fixed_search, fixed_generate))
print('생성 대역 호출 수:', len(calls))
