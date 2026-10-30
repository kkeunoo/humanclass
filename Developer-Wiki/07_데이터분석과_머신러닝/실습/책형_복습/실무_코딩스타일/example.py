import pandas as pd
from sklearn.metrics import f1_score, roc_auc_score
from wine_tools import prepare, train

df = pd.DataFrame({
    'alcohol': [8] * 10 + [13] * 10,
    'quality': [5] * 10 + [7] * 10,
})
X_train, X_test, y_train, y_test = prepare(df)
model = train(X_train, y_train)
test_pred = model.predict(X_test)
positive_scores = model.predict_proba(X_test)[:, 1]
test_f1 = f1_score(y_test, test_pred)
test_auc = roc_auc_score(y_test, positive_scores)
print('학습·시험 행:', len(X_train), len(X_test))
print('클래스:', model.classes_.tolist())
print('시험 F1:', test_f1)
print('시험 AUC:', test_auc)
