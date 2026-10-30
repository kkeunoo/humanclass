from vector_tools import attach_vectors

chunks = [
    {'movieId': 1, 'chunk_index': 0, 'content': '첫 조각'},
    {'movieId': 1, 'chunk_index': 1, 'content': '둘째 조각'},
]
response_rows = [
    {'index': 1, 'embedding': [0.3, 0.4]},
    {'index': 0, 'embedding': [0.1, 0.2]},
]
actions = attach_vectors(chunks, response_rows, 'practice_movies')
print('ID:', [a['_id'] for a in actions])
print('첫 벡터:', actions[0]['_source']['embedding'])
print('둘째 벡터:', actions[1]['_source']['embedding'])
print('원본 유지:', 'embedding' not in chunks[0])
try:
    attach_vectors(chunks, response_rows[:1], 'practice_movies')
except ValueError as error:
    print(error)
print('외부 전송:', False)
