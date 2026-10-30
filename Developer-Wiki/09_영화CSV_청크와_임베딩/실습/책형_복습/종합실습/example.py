import pandas as pd
from movie_tools import make_content, make_chunks
from vector_tools import attach_vectors
from cf_tools import recent_split, recommend
from evaluation_tools import recall_at_k

movies = pd.DataFrame([
    [1, 'Example Movie', 'Action|Comedy'],
    [2, 'Second Movie', 'Action'],
    [3, 'Third Movie', 'Drama'],
    [4, 'Fourth Movie', 'Comedy'],
], columns=['movieId', 'title', 'genres'])
tags = pd.DataFrame([[1, 'friendship'], [1, 'funny']], columns=['movieId', 'tag'])
content = make_content(movies, tags)
chunks = make_chunks(content)
fixed_response = [{'index': i, 'embedding': [0.1, 0.2]} for i in reversed(range(len(chunks)))]
actions = attach_vectors(chunks, fixed_response, 'practice_movies')
print(content.iloc[0]['content_text'])
print('영화·청크·작업:', len(content), len(chunks), len(actions))
print('외부 임베딩·적재:', False)

ratings = pd.DataFrame([
    [10, 1, 4.0, 100], [10, 2, 5.0, 110], [10, 3, 3.0, 120],
    [20, 1, 4.0, 100], [20, 3, 5.0, 110], [20, 4, 2.0, 120],
    [30, 2, 5.0, 100], [30, 4, 3.0, 110], [30, 3, 4.0, 120],
], columns=['userId', 'movieId', 'rating', 'timestamp'])
test, train = recent_split(ratings)
recommendations = recommend(train, 10, top_k=2)
print('학습·시험:', len(train), len(test))
print('추천:', [item['movieId'] for item in recommendations])
print('가상 자료 Recall@2:', recall_at_k(10, test, recommendations, threshold=3.0, k=2))
