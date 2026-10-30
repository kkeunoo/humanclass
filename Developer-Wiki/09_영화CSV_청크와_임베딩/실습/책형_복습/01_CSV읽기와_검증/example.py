from csv_tools import load_csv, inspect_ids

movies = load_csv('movies.csv')
tags = load_csv('tags.csv')
ratings = load_csv('ratings.csv')
result = inspect_ids(movies, tags, ratings)
print('행 수:', len(movies), len(tags), len(ratings))
print('미리보기:', movies.head(1).to_dict(orient='records')[0]['title'])
print('태그의 미등록 ID:', result['tag_unknown_ids'])
print('평점의 미등록 ID:', result['rating_unknown_ids'])
print('평점 범위:', result['rating_min'], result['rating_max'])
