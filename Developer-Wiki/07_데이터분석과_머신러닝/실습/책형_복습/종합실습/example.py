from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.metrics import f1_score, roc_auc_score
from wine_tools import load_split

X_train, X_test, y_train, y_test = load_split('winequality-red.csv')
base_model = RandomForestClassifier(n_estimators=100, random_state=42)
base_model.fit(X_train, y_train)
base_test_pred = base_model.predict(X_test)
base_test_scores = base_model.predict_proba(X_test)[:, 1]
train_cv_scores = cross_val_score(
    base_model, X_train, y_train, cv=5, scoring='f1'
)
params = {'n_estimators': [50, 100], 'max_depth': [5, 10, None]}
grid = GridSearchCV(
    RandomForestClassifier(random_state=42), params, cv=5, scoring='f1'
)
grid.fit(X_train, y_train)
selected_model = grid.best_estimator_
selected_test_pred = selected_model.predict(X_test)
selected_test_scores = selected_model.predict_proba(X_test)[:, 1]
print('학습/시험 행:', len(X_train), len(X_test))
print('기본 시험 F1:', round(f1_score(y_test, base_test_pred), 6))
print('기본 시험 AUC:', round(roc_auc_score(y_test, base_test_scores), 6))
print('학습 부분 CV 평균:', round(train_cv_scores.mean(), 6))
print('선택 설정:', grid.best_params_)
print('선택 과정 CV 평균:', round(grid.best_score_, 6))
print('선택 모델 시험 F1:', round(f1_score(y_test, selected_test_pred), 6))
print('선택 모델 시험 AUC:', round(roc_auc_score(y_test, selected_test_scores), 6))
