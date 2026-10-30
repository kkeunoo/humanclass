from pathlib import Path
import pandas as pd


def load_csv(name):
    path = Path(__file__).resolve().parent / name
    return pd.read_csv(path)


def inspect_ids(movies, tags, ratings):
    movie_ids = set(movies['movieId'].dropna())
    tag_ids = set(tags['movieId'].dropna())
    rating_ids = set(ratings['movieId'].dropna())
    return {
        'tag_unknown_ids': sorted(tag_ids - movie_ids),
        'rating_unknown_ids': sorted(rating_ids - movie_ids),
        'rating_min': float(ratings['rating'].min()),
        'rating_max': float(ratings['rating'].max()),
    }
