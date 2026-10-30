import pandas as pd
from evaluation_tools import recall_at_k

test = pd.DataFrame([
    {'userId': 10, 'movieId': 3, 'rating': 4.5},
    {'userId': 10, 'movieId': 4, 'rating': 5.0},
    {'userId': 10, 'movieId': 9, 'rating': 3.0},
])
recommendations = [{'movieId': 3}, {'movieId': 5}, {'movieId': 4}]
print('Recall@1:', recall_at_k(10, test, recommendations, k=1))
print('Recall@2:', recall_at_k(10, test, recommendations, k=2))
print('Recall@3:', recall_at_k(10, test, recommendations, k=3))
print('관련 영화 없음:', recall_at_k(99, test, recommendations, k=2))
