from rank_tools import fuse

text_hits = [
    {'_id': 'A', '_source': {'title': 'A 안내'}},
    {'_id': 'B', '_source': {'title': 'B 안내'}},
]
vector_hits = [
    {'_id': 'B', '_source': {'title': 'B 안내'}},
    {'_id': 'C', '_source': {'title': 'C 안내'}},
]
result = fuse(text_hits, vector_hits)
print('순서:', [row['id'] for row in result['results']])
print('점수:', [round(row['score'], 6) for row in result['results']])
print('고유 결과:', result['total'])
short = fuse(text_hits, vector_hits, size=1)
print('상위 1개·총수:', len(short['results']), short['total'])
print('빈 입력:', fuse([], []))
