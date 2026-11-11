hits = [
    {'_source': {'movieId': 7, 'title': 'A'}, '_score': 2.0},
    {'_source': {'movieId': 7, 'title': 'A'}, '_score': 1.9},
    {'_source': {'movieId': 5, 'title': 'B'}, '_score': 1.5},
]
seen = set()
recommends = []
for hit in hits:
    source = hit['_source']
    movie_id = source['movieId']
    if movie_id in seen:
        continue
    seen.add(movie_id)
    recommends.append((movie_id, source['title'], hit['_score']))

print(recommends)
print(recommends[:1])
