import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('tiny_wine.csv', sep=';')
print('읽은 모양:', df.shape)
df['good'] = (df['quality'] >= 7).astype(int)
y = df['good']
X = df.drop(columns=['quality', 'good'])
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print('정답:', y.tolist())
print('입력 열:', X.columns.tolist())
print('원본 열:', df.columns.tolist())
print('분할 크기:', len(X_train), len(X_test), len(y_train), len(y_test))
print('학습 짝:', X_train.index.equals(y_train.index))
print('시험 짝:', X_test.index.equals(y_test.index))
print('시험 클래스:', sorted(y_test.tolist()))
