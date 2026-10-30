from collections import Counter
from feature_tools import build_query

selected = [
    {'movieId': 1, 'genres': ['comedy'], 'tags': ['fun', 'friendship']},
    {'movieId': 2, 'genres': ['comedy', 'action'], 'tags': ['fun']},
]
print('검색문:', build_query(selected))
print('문자열:', dict(Counter('김밥김밥')))
print('단어 목록:', dict(Counter(['김밥', '김밥'])))
print('빈 선택:', repr(build_query([])))
