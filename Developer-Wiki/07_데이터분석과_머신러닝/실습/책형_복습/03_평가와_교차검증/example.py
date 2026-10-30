from sklearn.metrics import f1_score, roc_auc_score

y_true = [0, 0, 1, 1]
pred = [0, 1, 1, 0]
positive_scores = [0.1, 0.8, 0.9, 0.4]
print('F1:', f1_score(y_true, pred))
print('AUC:', roc_auc_score(y_true, positive_scores))
print('모두 0의 F1:', f1_score(y_true, [0, 0, 0, 0]))
print('동점 점수의 AUC:', roc_auc_score(y_true, [0.5, 0.5, 0.5, 0.5]))
