from chunk_tools import split_text, build_actions


def fixed_embedding(title, content):
    return [0.1, 0.2]


text = 'A' * 20 + '. ' + 'B' * 20 + '. ' + 'C' * 20 + '.'
doc = {'id': 7, 'title': '구조 예제', 'content': text}
chunks = split_text(text)
actions = build_actions(doc, fixed_embedding)
print('청크 수:', len(chunks))
print('청크 길이:', [len(c) for c in chunks])
print('둘째 앞 겹침:', chunks[1][:6])
print('ID:', [a['_id'] for a in actions])
print('본문 독립:', actions[0]['_source'] is not actions[1]['_source'])
print('원본 유지:', doc['content'] == text and 'embedding' not in doc)
print('가상 차원:', len(actions[0]['_source']['embedding']))
