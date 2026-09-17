# DB처럼 표 형태의 데이터 파일을 읽어다 분석하고 다루는 lib
# 보통 머신러닝에서 데이터를 가져오고, 확인하고, 정리하는 용도로 주로 사용

# 데이터 구조
# Serial : 1차원 배열
# DataFrame : 2차원 테이블 (엑셀 시트, DB 테이블에 해당)

# 주요 기능
# 자료 입출력 : csv, xlsx, txt, json, sql
# 데이터 정제 : 중복 제거, 데이터 타입 변경, 결측치(null, NaN) 제거
# 가공 및 분석 : 필터링, 정렬, 그룹화, 병합
import pandas as pd 

# dataFrame은 2차원 배열을 뜻 함
dataFrame = pd.read_csv('wine+quality/winequality-red.csv', sep=';')

# head()로 기본 상위 5줄의 값을 출력하여 테스트 함, 전달인자 넣어서 3줄만 볼 수도 있음
# head의 경우 대충 hello world 느낌으로 로딩이 잘 되었는지 찍어보는 것
print(dataFrame.head(3))
print('-'*30)

# shape : 데이터프레임의 크기를 표시(행,열 의 개수)
# 보통 column을 변수라고 얘기하기도 함
print('dataFrame.shape : ', dataFrame.shape) 
print('-'*30)

# info : 데이터프레임의 요약 정보
# 출력결과 : 데이터 개수, 컬럼 이름, 결측치(null) 유/무, 타입, 메모리 사용량 
# 전체 column에 null이 없고 float, int로 되어있는 분석정보가 나옴
dataFrame.info() # memory usage: 150.0 KB 는 실제 메모리 사용량
print('-'*30)

# 정답 데이터 만들기 / (dataFrame['quality'] >= 7) 의 결과인 True는 1, False는 0으로 바꾸어 줌 (astype)
dataFrame['good'] = (dataFrame['quality'] >= 7).astype(int)
y = dataFrame['good'] # y는 정답
# quality는 점수로 되어있는데, 이를 단순화 시켜서 0과 1로 구분하기 위해 위 작업 진행
# 데이터 전처리(정제하는 과정 등), feature engineering
# 데이터 분석 전에 불순물, 이상치 제거

# 문제 데이터 만들기
X = dataFrame.drop(
    columns=['quality', 'good'] # 두 column을 지워서 X에 넣어라
)
# 깊은 복사 (얕은 복사와 다르게 원본 데이터를 복사, 원본이 지워지는게 아님)
# 문제지에서 정답을 지운 상태

# 데이터 쪼개기 : 학습 데이터와 테스트 데이터를 분리
# test는 모의고사, train 수업시간
# test_size등을 바꾸는 것을 '하이퍼 파라메터 튜닝' 이라고 함
# 정답만 넣은 y와 ['quality', 'good'] 을 제외한 문제만 넣은 X를 각 스플릿해서 20%를 X,y_test에서 사용 / 80%를 학습
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size = 0.2, # 문제와 정답을 준 뒤 20퍼센트만 가지고 테스트하라는 것, 80퍼센트 학습
    random_state = 42, # 다른 숫자를 사용해도 되지만, 같은 값을 사용해야 결과도 같다
    stratify = y # 80%의 학습용 데이터에서 7(좋음):3(나쁨) 이라면 y의 정답데이터도 해당 퍼센트로 잡아라
)
# random_state = 42 : 랜덤 표에서 42부터 시작하기 때문에 같은 결과를 낼 수 있는 재현성을 띄움
# 데이터를 나누는 과정을 고정하고, 값을 바꾸면 나누는 방법이 계속 바뀐다
# 난수표의 시작 값(seed)이라고 생각하면 편하다
# 동일한 설정으로 다시 실행했을 때 결과를 재현하기 쉽다

# stratify : 계층화(그룹별)한다
# y를 쓴 이유는 y, 즉 정답의 비율을 유지하면서 나누어라 라는 뜻
# 정답지의 0과 1의 비율로 학습/테스트 데이터도 비슷한 비율로 나눠라 라는 것

# 의사 결정 트리 Decision Tree
# 스무고개 하듯이 질문하면서 학습 - 여러 갈래로 나뉘어서 나무 모양이 됨
# 너무 나누면 과적합(over fitting)되어서 예측이 어렵게 된다
# 가지치기(Pruning) : 사용하지 않을 것 같은 루트를 잘라냄
# RandomForestClassifier(랜덤포레스트), 아키네이터같은걸 많이 만듦 
# 이러한 나무가 많을수록 통계를 낼 수 있으니, 그것이 숲과 같다 하여 'RandomForest'

# RandomForestClassifier는 분류 문제에 사용하는 머신러닝 알고리즘
# random forest는 여러 개의 decision tree를 만들어서 결과를 종합하는 방식
# 하나의 방법이 아닌, 여러 나무의 결과를 종합해서 안정적인 예측을 한다
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(
    n_estimators = 100, # 아키네이터를 100마리 가져오겠다는 뜻(비유)
    random_state = 42
)
# n_estimators = 100 은 decision tree를 100개 사용하겠다는 뜻
# 나무가 많아지면 안정적(비슷한 결과를 또 기대할 수 있음)
# 많아지면 안정적이지만 시간이 늘어남(안정적이나, 품질이 좋아지는 것은 아니다 / 재현성을 높이기 위함)

model.fit(X_train, y_train) # 문제지로 학습 시작
# fit() : 머신러닝 모델을 실제 데이터에 학습시키기 (X_train 문제), (y_train 정답) - 학습 데이터에 대한 문제와 정답
# X_train : 입력(변수 or 문제) 데이터 / y_train : 정답 데이터
# Value % 2 = 0 이 짝수라던지, 이 사 육 팔에서 ㅣ ㅏ가 들어가면 짝수라던지 등 확률을 학습
# 학습 한 train 데이터를 기준으로 test 데이터로 모의고사를 본 셈 
# 학습이 끝나게 되면 정제된 데이터를 통한 학습 결과가 model 안에 저장된다

# 실전 데이터
# 학습하지 않은 새로운 값으로 학습한 내용에 따른 예측 결과 확인용
wine = [[
    7.4,
    0.70,
    0.00,
    1.9,
    0.076,
    11.0,
    34.0,
    0.9978,
    3.51,
    0.8,
    12.4
]]

columns = [
    "fixed acidity",
    "volatile acidity",
    "citric acid",
    "residual sugar",
    "chlorides",
    "free sulfur dioxide",
    "total sulfur dioxide",
    "density",
    "pH",
    "sulphates",
    "alcohol"
]

# 모델 학습에 사용한 X와 같은 형태로 만들어주는 과정(2차원 배열)
wine_df = pd.DataFrame(wine, columns=columns)

# predict : 예측 (결과는 배열로 나옴)
# 만약 여러 개를 줄 경우 [1,0,0] 형태로 나옴
wine_pred = model.predict(wine_df)
print('예측 결과(pred) : ', wine_pred) # 예측 결과 :  [0]

# proba(probablity : 확률)는 나쁠 확률 좋을 확률 같이 보여줌
# 비교 할 가짓수를 클래스라고 한다(현재 0과 1뿐)
# 새로운 데이터가 각 클래스가 될 확률을 계산한다 (0이 될 확률 0.59 / 1이 될 확률 0.41)
wine_prob = model.predict_proba(wine_df)
print('예측 확률(prob) : ', wine_prob) # 예측 결과(prob) :  [[0.59 0.41]]

########################
# 모델 성능 평가
########################

from sklearn.metrics import f1_score, roc_auc_score
# 평가 지표 : 모델이 얼마나 잘 이해했는가? 를 숫자로 표현한다

# train 데이터로 학습한 모델에 모의고사 문제인 test 데이터를 예측하라고 한다
pred = model.predict(X_test)

# 실제 정답(y_test)과 예측 답(pred)으로 f1 점수를 낸다
f1 = f1_score(y_test, pred)
# f1은 정밀도와 재현율을 함께 고려하는 지표(기준)다
# 단지 답만 점검하는 것이 아니라, 실제 양성(참/좋은 와인[1]) 데이터를 잘 찾았는지도 고려한다
# 점수는 0~1까지 나오며 1이 좋은 것 (정답과 좋은 데이터가 나올 확률)
print('f1 평가 점수 : ', f1) # f1 평가 점수 :  0.75

proba = model.predict_proba(X_test)[:, 1]
# 슬라이싱 [:, 1] 은 전체 행에서 두 번째 컬럼(좋은 와인의 확률)만 추출

# 점수는 0~1까지 나오며 
# 1 : 완벽 / 0.5 : 랜덤 / 0.5 미만 : 좋지 않음
auc = roc_auc_score(y_test, proba)
print('rod_auc 평가 점수 : ', auc) # 정답에 가까운 지표 rod_auc 평가 점수 :  0.9554193602552262
# ROC-AUC 지표는 얼마나 잘 구분하는가?
# 0.5는 무작위로 굴려도 나오는 값
# 1에 가까울수록 두 클래스를 잘 구분하는 모델이다

# f1과 roc_auc는 서로 다른 것을 기준으로 측정하기 때문에 서로 비교하지는 말자  

########################
# 교차 검증
########################
from sklearn.model_selection import cross_val_score
# Cross Validation(교차 유효성 검증) 
# 데이터를 여러 부분으로 나눠서 모델(학습을 해야하는 것들)을 반복적으로 학습하고 평가한다
'''
예를 들어 [0,1,2,3,4] 5개의 세트가 있다고 했을 때 이 중에서
1. 학습 [0,1,2,3]와 연습문제 [4]로 학습
2. 학습 [0,1,2,4]와 연습문제 [3]로 학습
3. 학습 [0,1,4,3]와 연습문제 [2]로 학습
4. 학습 [0,4,2,3]와 연습문제 [1]로 학습
5. 학습 [4,1,2,3]와 연습문제 [0]로 학습
'''
# 데이터가 많지 않은 경우에는 분할에 따라서 성능이 달라질 수 있기 때문에 유용하다
# 즉, 한 번의 결과만으로 모델 성능을 판단하는 문제를 줄이기 위해 사용한다

scores = cross_val_score(
    # model, X, y,
    model, X_train, y_train, 
    cv=5, # 보통 cv는 5정도를 사용해야 평균이 잘 나옴 
    scoring='f1' # 점수는 'f1' 평가 지표를 사용해라
)
# 전체 X(문제)와 Y(답)으로 다섯 번 교차 검증(5-Fold Cross Validation)을 수행한다
# cv=5 : 는 데이터를 5개 부분으로 나눠서 교대로 검증한다
# 한 번에 4개의 부분을 학습에 사용하고 1개의 부분을 검증에 사용한다
# scoring='f1' : 각 검증에서 F1-Score를 계산하라
print('cross_val_score : ', scores) 
# model. X, y, cv=5 : [0.23529412 0.37777778 0.28571429 0.48275862 0.31034483]
# model, X_train, y_train, cv=5 : [0.6        0.43137255 0.48148148 0.53571429 0.50980392]
# model, X_train, y_train, cv=10 : [0.75       0.4        0.17391304 0.64285714 0.43478261 0.5 0.58064516 0.66666667 0.53846154 0.55172414]

print('scores 평균 : ', scores.mean()) # 평균내기
# model, X, y, cv=5 : 0.33837792588299687
# model, X_train, y_train, cv=3 : 0.4806999380855232
# model, X_train, y_train, cv=5 : 0.5116744475568005
# model, X_train, y_train, cv=10 : 0.5239050299380618

# 단순하게 어떤 것이 좋다/나쁘다가 아니고, 어떤 덩어리가 무조건 정답도 아니다. 확률을 낼 뿐

from sklearn.model_selection import GridSearchCV
params = {
    'n_estimators' : [50, 100], 
    'max_depth' : [5, 10, None] # 최대 깊이를 5개, 10개, 무제한
}
# 2 * 3 = 6개의 조합을 params 변수 안에 저장
# n_estimators : 의사 결정 나무 개수
# max_depth : 나무의 최대 깊이 (None : 제한하지 않는다)
# 개발자가 바꿀 수 있는 것(값)들을 '하이퍼파라미터' 라고 한다

grid = GridSearchCV(
    RandomForestClassifier(random_state=42),
    params, 
    # cv=3,
    cv=5,
    scoring='f1'
)
# GridSearchCV
# 첫 번째 전달인자 : 머신러닝 모델 (ex RandomForestClassifier)
# 두 번째 전달인자 : 시험 할 하이퍼파라미터 후보(조합)
# 세 번째 전달인자 : CV, 학습 데이터의 조합 수 (3-Fold Cross Validation)
# 네 번째 전달인자 : 평가 지표 (F1으로 평가는 하지만 지표의 점수가 가장 높은 조합을 찾는다)

grid.fit(X_train, y_train) 
# 지정한 6개의 하이퍼파라미터 조합을 각각 학습하고 평가함
# train, test를 모두 주면 모든것을 학습하기 때문에 다 맞추게 됨 (새 데이터가 있다면 그걸 주면 되지만)
# 그래서 학습 한 train을 기준으로 처음 보는 test 데이터를 맞춰보게 하는 것
print('최적의 조합법(grid.best_params_) : ', grid.best_params_) # {'max_depth': None, 'n_estimators': 50}
# 6개의 하이퍼파라미터 조합 중 가장 좋았던 조합을 출력한다

# print('최고의 점수(best_score_) cv=3 : ', grid.best_score_) # 0.48361474498607304
print('최고의 점수(best_score_) cv=5 : ', grid.best_score_) # 0.5234521802159902
# GridSearchCV가 선택 한 최적의 하이퍼파라미터 조합으로 교차 검증에서 얻은 평균 F1 점수를 출력

grid_model = grid.best_estimator_ 
# GridSearchCV가 찾은 각 하이퍼파라미터 조합 중에서 가장 좋은 조합으로 만들어진 모델을 가져옴
# 최적의 RandomForestClassifier 결과물

grid_pred = grid_model.predict(wine_df)
print('grid 와인 결과 예측(pred) : ', grid_pred)

grid_prob = grid_model.predict_proba(wine_df)
print('grid 와인 확률 예측(prob) : ', grid_prob)

from sklearn.model_selection import StratifiedKFold

skf = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)
# cross_val_score에서는 찢은 데이터를 따로 넣었지만, 이번 건은 찢는 것 까지 해줌
# StratifiedKFold : 분류할 때 클래스의 비율을 최대한 유지하면서 나누는 방법
# n_splits='쪼갤 개수' / n_splits=5 (5-Fold Cross Validation) 5개 구역으로 쪼개기
# shuffle='True/False' / shuffle=True 데이터를 섞은 다음에 Fold로 나눈다 

scores = cross_val_score(
    grid_model, X, y,
    cv=skf,
    scoring='f1'
)
# StratifiedKFold 방식을 사용해서 Cross Validation을 수행한다
# 위에서 배운 내용은 그냥 5개 구역(구분)으로 나눠서 진행했지만, 
# 지금 하는 것은 정답의 비율에 가까운 구성으로 진행한다(train_test_split과 비슷한 역할을 한다)

# 이전 결과
# model, X_train, y_train, cv=5 : [0.6        0.43137255 0.48148148 0.53571429 0.50980392]
# model, X_train, y_train, cv=10 : [0.75       0.4        0.17391304 0.64285714 0.43478261 0.5 0.58064516 0.66666667 0.53846154 0.55172414]
print('skf 방식의 교차 검증 결과 : ', scores)
# 현재 결과
# skf 방식의 교차 검증 결과 :  [0.57142857 0.62686567 0.62857143 0.55555556 0.61971831]

# 이전 결과(평균)
# model, X_train, y_train, cv=5 : 0.5116744475568005
# model, X_train, y_train, cv=10 : 0.5239050299380618
print('skf 방식의 교차 검증 결과(평균) : ', scores.mean())
# 현재 결과(평균)
# skf 방식의 교차 검증 결과(평균) :  0.6004279074113004









############
# 시험문제
############
# dataFrame = pd.read_csv('wine+quality/winequality-red.csv', sep=';')

# print(dataFrame.head(2))
# print('dataFrame.shape : ', dataFrame.shape) 

# dataFrame.info()

# dataFrame['good'] = (dataFrame['quality'] >= 7).astype(int)

# y = dataFrame['good']

# X = dataFrame.drop(
#     columns=['quality', 'good'] 
# )

# X_train, X_test, y_train, y_test = train_test_split(
#     X, y,
#     test_size = 0.2, 
#     random_state = 42, 
#     stratify = y 
# )

# model = RandomForestClassifier(
#     n_estimators = 100, # 아키네이터를 100마리 가져오겠다는 뜻(비유)
#     random_state = 42
# )

# model.fit(X_train, y_train) # 문제지로 학습 시작

# wine1 = [[
#     7.4,
#     0.70,
#     0.00,
#     1.9,
#     0.076,
#     11.0,
#     34.0,
#     0.9978,
#     3.51,
#     0.8,
#     12.4
# ]]
# wine2 = [[
#     7.4,
#     0.36,
#     0.3,
#     1.8,
#     0.074,
#     17,
#     24,
#     0.99419,
#     3.24,
#     0.7,
#     11.4
# ]]

# wine3 = [[
#     7.4,
#     0.70,
#     0.00,
#     1.9,
#     0.076,
#     11.0,
#     34.0,
#     0.9978,
#     3.51,
#     0.5,
#     16
# ]]

# wine_df_1 = pd.DataFrame(wine1)
# wine_df_2 = pd.DataFrame(wine2)
# wine_df_3 = pd.DataFrame(wine3)

# wine_pred_1 = model.predict(wine_df_1)
# wine_pred_2 = model.predict(wine_df_2)
# wine_pred_3 = model.predict(wine_df_3)
# print('예측 결과(pred) : ', wine_pred_1) 
# print('예측 결과(pred) : ', wine_pred_2) 
# print('예측 결과(pred) : ', wine_pred_3) 

# wine_prob_1 = model.predict_proba(wine_df_1)
# wine_prob_2 = model.predict_proba(wine_df_2)
# wine_prob_3 = model.predict_proba(wine_df_3)
# print('예측 결과(prob) : ', wine_prob_1) 
# print('예측 결과(prob) : ', wine_prob_2) 
# print('예측 결과(prob) : ', wine_prob_3)
