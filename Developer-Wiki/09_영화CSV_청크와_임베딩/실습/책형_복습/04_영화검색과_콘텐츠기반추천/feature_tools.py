from collections import Counter


def build_query(selected_sources, top_n=5):
    genre_counter = Counter()
    tag_counter = Counter()
    for source in selected_sources:
        genre_counter.update(source.get('genres', []))
        tag_counter.update(source.get('tags', []))
    terms = [term for term, _ in genre_counter.most_common(top_n)]
    terms.extend([term for term, _ in tag_counter.most_common(top_n)])
    return ' '.join(dict.fromkeys(terms))
