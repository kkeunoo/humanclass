# 02. 모델을 학습시키고 새 와인 예측하기

[이 단원 목차](README.md) · [이전: 입력·정답 분리](01_Pandas_와인데이터와_학습입력.md) · [다음: 평가·교차 검증](03_평가와_교차검증.md)

앞 장의 `X_train`, `y_train`을 모델에 주고, 두 원본이 직접 적은 **서로 다른 새 와인**을 예측한다. 주석에 적힌 예전 출력값은 현재 실행 결과를 보장하지 않는다.

## 1. 같은 종류의 모델을 만들고 학습

### 강사님 코드 — 원본 발췌

출처: `D:/workspace_teacher/workspace_python/06_scikit_learn/01_main.py` 77–88행

```python
from sklearn.ensemble import RandomForestClassifier

# 어떻게 할지 선언
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
# n_estimators=100 : decision tree 100개를 사용해라
# 나무가 많아지면 안정적인데 시간이 늘어난다 (안정적이지만 품질이 좋아지는건 별개다)


model.fit(X_train, y_train) # 학습
```

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/06_scikit_learn/01_main.py` 77–87행

```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(
    n_estimators = 100, # 아키네이터를 100마리 가져오겠다는 뜻(비유)
    random_state = 42
)
# n_estimators = 100 은 decision tree를 100개 사용하겠다는 뜻
# 나무가 많아지면 안정적(비슷한 결과를 또 기대할 수 있음)
# 많아지면 안정적이지만 시간이 늘어남(안정적이나, 품질이 좋아지는 것은 아니다 / 재현성을 높이기 위함)

model.fit(X_train, y_train) # 문제지로 학습 시작
```

양쪽 모두 `RandomForestClassifier`에 나무 100개와 `random_state=42`를 설정한 뒤 `fit(X_train, y_train)`을 호출한다. `fit`은 학습용 입력과 정답의 관계를 모델에 맞춘다. 내 주석의 ‘나무가 많아지면 안정적’이라는 비유는 개념 이해에는 도움이 되지만, 나무 수만 늘리면 항상 점수가 좋아진다는 뜻은 아니다. 강사님 주석도 시간 증가와 품질 개선은 별개라고 구분한다.

## 2. 새 입력값은 열 이름과 순서를 맞춘다

### 강사님 코드 — 원본 발췌

출처: `D:/workspace_teacher/workspace_python/06_scikit_learn/01_main.py` 95–109행

```python
# 실전 데이타
# 학습하지 않은 새로운 값으로 학습한 내용에 따른 예측 결과 확인용
wine = [[
    12.6,
    0.31,
    0.72,
    2.2,
    0.072,
    6.0,
    29.0,
    0.9978,
    2.88,
    0.82,
    29.8
]]
```

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/06_scikit_learn/01_main.py` 94–108행

```python
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
```

강사님과 내 `wine` 숫자는 서로 다르다. 따라서 같은 모델 설정이어도 **두 새 와인의 예측 결과가 같아야 할 이유는 없다**. 두 원본은 바로 아래에서 11개 열 이름을 `columns`로 만들고, 2차원 `DataFrame` 한 행으로 바꾼다. 학습에 쓴 `X`와 열 이름·순서가 맞아야 한다.

### 강사님 코드 — 원본 발췌

출처: `D:/workspace_teacher/workspace_python/06_scikit_learn/01_main.py` 110–139행

```python
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


# 모델 학습에 사용한 X와 같은 형태로 만들기
wine_df = pd.DataFrame(wine, columns=columns)

# predict : 예측 결과
# 결과는 배열로 나온다
# 만약에 여러 개를 주면 [1,0,1]
wine_pred = model.predict(wine_df)
print("예측 결과:", wine_pred)

# predict_proba : 예측 확률
# proba -> probability 확률
# 비교할 가짓수를 클래스라고 한다(현재 0과 1)
# 새로운 데이터가 각 클래스가 될 확률을 계산한다
wine_prob = model.predict_proba(wine_df)
print("예측 결과:", wine_prob)
```

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/06_scikit_learn/01_main.py` 110–136행

```python
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
```

`predict(wine_df)`는 0 또는 1로 분류한 결과를 배열로 반환한다. `predict_proba(wine_df)`는 각 클래스의 확률을 **클래스 순서대로** 담은 2차원 배열을 반환한다. 학생 주석의 `[0]`, `[[0.59 0.41]]`은 기록 당시 출력 예시다. 실제 값을 확인하려면 같은 CSV와 실행 환경으로 현재 코드를 실행해야 한다.

## 직접 확인할 질문

1. `fit`에 왜 `X_test`, `y_test` 대신 학습용 데이터를 주는가?
2. `wine` 한 개도 왜 `[[...]]`처럼 2차원으로 적는가?
3. `predict`와 `predict_proba`의 결과 모양은 어떻게 다른가?

## 추가로 알면 좋은 것

다른 분류기 선택, 모델 파일로 저장하기, 실제 서비스 배포는 양쪽 `01_main.py`에서 다루지 않았다. 모델을 비교하거나 배포할 때 별도 주제로 공부한다.
