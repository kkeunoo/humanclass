import math
import pandas as pd
from surprise import Dataset, Reader, KNNWithMeans


def recent_split(ratings, test_size=0.2):
    if not 0 < test_size < 1:
        raise ValueError('시험 비율은 0보다 크고 1보다 작아야 합니다.')
    data = ratings.copy()
    data['original_order'] = range(len(data))
    data['timestamp'] = pd.to_numeric(data['timestamp'], errors='coerce')
    if data['timestamp'].isna().any():
        raise ValueError('유효한 timestamp가 필요합니다.')
    test_indices = []
    for _, group in data.groupby('userId', sort=False):
        if len(group) <= 1:
            continue
        ordered = group.sort_values(['timestamp', 'original_order'], kind='stable')
        count = min(len(ordered) - 1, max(1, math.ceil(len(ordered) * test_size)))
        test_indices.extend(ordered.tail(count).index.tolist())
    test = data.loc[test_indices].sort_values('original_order').drop(columns='original_order')
    train = data.drop(index=test_indices).sort_values('original_order').drop(columns='original_order')
    return test.reset_index(drop=True), train.reset_index(drop=True)


def recommend(train, user_id, top_k=2):
    if user_id not in set(train['userId']):
        raise ValueError('학습 자료에 없는 사용자입니다.')
    if top_k <= 0:
        raise ValueError('추천 수는 양수여야 합니다.')
    reader = Reader(rating_scale=(0.5, 5.0))
    dataset = Dataset.load_from_df(train[['userId', 'movieId', 'rating']], reader)
    train_set = dataset.build_full_trainset()
    model = KNNWithMeans(k=30, sim_options={'name': 'cosine', 'user_based': True}, verbose=False)
    model.fit(train_set)
    inner_id = train_set.to_inner_uid(user_id)
    seen = {train_set.to_raw_iid(movie_id) for movie_id, _ in train_set.ur[inner_id]}
    candidates = [train_set.to_raw_iid(i) for i in range(train_set.n_items) if train_set.to_raw_iid(i) not in seen]
    result = [{'movieId': movie_id, 'score': model.predict(user_id, movie_id).est} for movie_id in candidates]
    result.sort(key=lambda row: row['score'], reverse=True)
    return result[:top_k]
