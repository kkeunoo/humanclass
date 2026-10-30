import pandas as pd
from cf_tools import recent_split, recommend

ratings = pd.DataFrame([
    [10, 1, 4.0, 100], [10, 2, 5.0, 110], [10, 3, 3.0, 120],
    [20, 1, 4.0, 100], [20, 3, 5.0, 110], [20, 4, 2.0, 120],
    [30, 2, 5.0, 100], [30, 4, 3.0, 110], [30, 3, 4.0, 120],
], columns=['userId', 'movieId', 'rating', 'timestamp'])
test, train = recent_split(ratings)
print('학습·시험 행:', len(train), len(test))
print('사용자 10의 시험 영화:', test[test['userId'] == 10]['movieId'].tolist())
result = recommend(train, 10)
print('추천 영화:', [row['movieId'] for row in result])
print('예측 평점:', [round(float(row['score']), 6) for row in result])
print('시험을 평가했는가:', False)
