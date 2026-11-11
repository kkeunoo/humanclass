from collections import defaultdict

cbf_ids = [10, 30, 10]
cf_ids = [30, 20]
scores = defaultdict(float)
for ids in (cbf_ids, cf_ids):
    for rank, movie_id in enumerate(dict.fromkeys(ids), start=1):
        scores[movie_id] += 1 / (60 + rank)

ordered = sorted(scores.items(), key=lambda item: (-item[1], item[0]))
print([(movie_id, round(score, 5)) for movie_id, score in ordered])
