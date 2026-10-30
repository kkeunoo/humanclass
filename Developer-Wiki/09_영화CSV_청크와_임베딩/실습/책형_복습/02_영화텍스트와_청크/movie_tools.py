import pandas as pd


def parse_genre(value):
    text = str(value).strip()
    if text == '' or text == '(no genres listed)':
        return []
    return [genre.strip().lower() for genre in text.split('|')]


def make_content(movies, tags):
    result = movies[['movieId', 'title']].copy()
    result['title'] = result['title'].astype(str).str.strip()
    result['list_genre'] = movies['genres'].map(parse_genre)
    clean_tags = tags[['movieId', 'tag']].dropna(subset=['tag']).copy()
    clean_tags['tag'] = clean_tags['tag'].astype(str).str.strip().str.lower()
    clean_tags = clean_tags.drop_duplicates(['movieId', 'tag'])
    by_movie = clean_tags.groupby('movieId')['tag'].agg(list).to_dict()
    result['list_tag'] = result['movieId'].map(lambda movie_id: by_movie.get(movie_id, []))
    result['content_text'] = result.apply(
        lambda row: ' '.join([row['title']] + row['list_genre'] + row['list_tag']).strip(),
        axis=1,
    )
    return result.reset_index(drop=True)


def make_chunks(frame, size=50, overlap=15):
    if not 0 <= overlap < size:
        raise ValueError('겹침은 0 이상 크기 미만이어야 합니다.')
    chunks = []
    for row_index, row in enumerate(frame.to_dict(orient='records')):
        text = row['content_text'].strip()
        for chunk_index, start in enumerate(range(0, len(text), size - overlap)):
            chunks.append({
                'index': row_index, 'movieId': int(row['movieId']),
                'title': row['title'], 'genres': list(row['list_genre']),
                'tags': list(row['list_tag']), 'content': text[start:start + size],
                'chunk_index': chunk_index,
            })
    return chunks
