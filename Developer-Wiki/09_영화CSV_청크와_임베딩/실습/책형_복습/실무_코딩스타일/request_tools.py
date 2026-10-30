def validate_request(user_id, top_k, train_user_ids):
    if user_id not in set(train_user_ids):
        raise ValueError('학습 자료에 없는 사용자입니다.')
    if not isinstance(top_k, int) or top_k <= 0:
        raise ValueError('추천 수는 양의 정수여야 합니다.')
    return user_id, top_k
