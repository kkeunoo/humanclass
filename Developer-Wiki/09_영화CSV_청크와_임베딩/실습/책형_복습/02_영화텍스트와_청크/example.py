import pandas as pd
from movie_tools import make_content, make_chunks

movies = pd.DataFrame([{'movieId': 1, 'title': 'Example Movie', 'genres': 'Action|Comedy'}])
tags = pd.DataFrame([
    {'movieId': 1, 'tag': 'friendship'},
    {'movieId': 1, 'tag': 'funny'},
    {'movieId': 1, 'tag': ' FUNNY '},
])
frame = make_content(movies, tags)
chunks = make_chunks(frame)
print(frame.iloc[0]['content_text'])
print('태그:', frame.iloc[0]['list_tag'])
print('문자 수:', len(frame.iloc[0]['content_text']))
print('청크 길이:', [len(c['content']) for c in chunks])
print('둘째 내용:', chunks[1]['content'])
print('행 위치·영화 ID:', chunks[0]['index'], chunks[0]['movieId'])
