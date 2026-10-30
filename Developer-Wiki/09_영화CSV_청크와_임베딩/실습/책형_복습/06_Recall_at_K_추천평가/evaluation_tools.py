def recall_at_k(user_id, test, recommendations, threshold=4.0, k=10):
    if k <= 0:
        raise ValueError('k는 양수여야 합니다.')
    relevant = set(test.loc[
        (test['userId'] == user_id) & (test['rating'] >= threshold), 'movieId'
    ])
    if not relevant:
        return -1.0
    recommended = {item['movieId'] for item in recommendations[:k]}
    return len(relevant & recommended) / len(relevant)
