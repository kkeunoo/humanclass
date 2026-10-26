# 데이터 분석과 기초 머신러닝 — 와인 품질 분류

[Developer-Wiki 첫 화면](../README.md) · [Python 목차](../04_Python/README.md)

이 단원은 강사님과 내 `workspace_python/06_scikit_learn/01_main.py`를 비교한다. 두 폴더의 빨간 와인 CSV도 같은 1,599행·12열이다. **코드와 CSV에 있는 실습만 본문**에 놓고, 라이브러리의 다른 모델이나 이론은 ‘추가로 알면 좋은 것’으로 둔다. 가상환경의 `Lib`, `Scripts`, `share`와 `requirements.txt`는 학습 코드로 세지 않았다.

## 읽는 순서

1. [01 pandas로 CSV 읽고 입력·정답 만들기](01_Pandas_와인데이터와_학습입력.md) — `good`, `X`, `y`, 학습·시험 분리
2. [02 RandomForest 학습과 새 와인 예측](02_RandomForest_학습과_예측.md) — `fit`, `predict`, `predict_proba`
3. [03 평가·교차 검증·조합 찾기](03_평가와_교차검증.md) — F1, ROC AUC, `cross_val_score`, `GridSearchCV`

각 장에서 **강사님 원본 → 내 원본 → 실제 동작과 차이 → 직접 확인할 질문** 순서로 읽는다. 원본 발췌는 전체 실행 파일이 아니다. 앞선 변수와 CSV 파일 경로가 있어야 실행된다. 코드의 주석과 실제 전달 인자가 다르면 실행되는 인자를 기준으로 설명한다. [SQL의 표와 행](../05_SQL/01_SQL_기초와_SELECT.md)을 떠올린 뒤 [Python의 리스트·딕셔너리](../04_Python/README.md)와 다른 pandas 객체를 비교해 보면 좋다.

외부 데이터 일반화, 다른 모델, 배포와 모델 저장은 이번 양쪽 실습의 본문 범위가 아니다. 실제 모델 결과는 코드·데이터·라이브러리 환경에 따라 달라질 수 있으므로 주석에 적힌 점수를 정답처럼 외우지 않는다.
