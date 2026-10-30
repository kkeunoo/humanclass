import pandas as pd
from sklearn.model_selection import train_test_split


def load_split(path):
    df = pd.read_csv(path, sep=';')
    df['good'] = (df['quality'] >= 7).astype(int)
    y = df['good']
    X = df.drop(columns=['quality', 'good'])
    return train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
