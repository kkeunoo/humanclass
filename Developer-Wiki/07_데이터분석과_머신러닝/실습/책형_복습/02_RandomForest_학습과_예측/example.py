import pandas as pd
from sklearn.ensemble import RandomForestClassifier

X_train = pd.DataFrame({'alcohol': [8, 8, 8, 8, 13, 13, 13, 13]})
y_train = [0, 0, 0, 0, 1, 1, 1, 1]
model = RandomForestClassifier(n_estimators=100, random_state=42)
learned = model.fit(X_train, y_train)
new_wines = pd.DataFrame({'alcohol': [8, 13]})
pred = model.predict(new_wines)
proba = model.predict_proba(new_wines)
print('같은 모델:', learned is model)
print('클래스:', model.classes_.tolist())
print('입력 모양:', new_wines.shape)
print('분류:', pred.tolist())
print('확률 모양:', proba.shape)
print('각 행 합:', proba.sum(axis=1).round(6).tolist())
