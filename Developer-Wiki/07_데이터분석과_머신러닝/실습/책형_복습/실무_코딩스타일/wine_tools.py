from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


def prepare(df):
    y = (df['quality'] >= 7).astype(int)
    X = df.drop(columns=['quality'])
    return train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )


def train(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model
