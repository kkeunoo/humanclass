# 01. CSV에서 학습 입력과 정답 만들기

[이 단원 목차](README.md) · [다음: 모델 학습과 예측](02_RandomForest_학습과_예측.md)

`winequality-red.csv`의 한 행은 와인 한 개, 열은 측정값과 `quality` 점수다. 두 원본은 같은 파일을 세미콜론 구분자로 읽는다. CSV를 직접 세면 1,599행·12열이다. 먼저 표를 확인한 다음 예측할 정답과 모델에 줄 입력을 나눈다.

## 1. 파일을 읽고 표의 모양 확인

### 강사님 코드 — 원본 발췌

출처: `D:/workspace_teacher/workspace_python/06_scikit_learn/01_main.py` 12–28행

```python
import pandas as pd

dataFrame = pd.read_csv('wine+quality/winequality-red.csv', sep=';')

# 기본 상위 5줄의 값을 가져온다
# print(dataFrame.head())
# 가져오고 싶은 줄(행)을 지정할 수 있다
# 하는 이유는 대충 hello world 느낌으로 로딩이 잘 됐는지 확인 용도
print(dataFrame.head(3))
print('-'* 30)
# shape : 데이타프레임의 크기 (행의 개수, 열의 개수)
print('dataFrame.shape: ', dataFrame.shape)
print('-'* 30)

# info : 요약 정보
# 출력 결과 : 데이터 개수, 컬럼 이름들, 타입, 결측치 유무, 메모리 사용량
dataFrame.info()
```

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/06_scikit_learn/01_main.py` 12–30행

```python
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
```

`pd.read_csv(..., sep=';')`는 쉼표가 아닌 세미콜론을 열 구분자로 사용한다. `head(3)`은 앞의 3행을 보여 주고, `shape`는 `(행 수, 열 수)`, `info()`는 열 이름·자료형·비어 있지 않은 값의 수 등을 보여 준다. 내 코드가 설명을 더 적었지만 실행 흐름은 같다. 양쪽 주석의 **Serial**은 pandas 객체 이름 **Series**와 혼동하지 말자. DataFrame은 행과 열을 가진 표다.

## 2. 0·1 정답과 입력 열 나누기

### 강사님 코드 — 원본 발췌

출처: `D:/workspace_teacher/workspace_python/06_scikit_learn/01_main.py` 31–42행

```python
# 정답 데이터 만들기
# True:1, False:0
dataFrame['good'] = (dataFrame['quality'] >= 7).astype(int)
y = dataFrame['good']
# quality는 점수로 되어있는데 이를 단순하게 0과 1로 구분한다
# 데이터 전처리, feature engineering
# 전처리 : 분석 전에 불순물 제거

# 문제 데이터 만들기
X = dataFrame.drop(
    columns=['quality', 'good']
)
```

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/06_scikit_learn/01_main.py` 33–43행

```python
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
```

`quality >= 7`이 참이면 `good=1`, 아니면 `good=0`이다. `y`는 이 정답 열이고, `X`는 `quality`와 `good`을 제외한 11개 측정 열이다. 정답을 입력 열에 그대로 두면 모델이 답을 보고 맞히는 셈이므로 두 열을 제외한다. CSV에서 직접 세면 `good=1`은 217행이다.

내 주석의 ‘깊은 복사’는 이 한 줄의 핵심을 설명하기에 부정확하다. 여기서는 `drop(columns=...)`의 **반환값을 새 변수 `X`에 받았고 원본 `dataFrame`을 제자리에서 수정하지 않았다**고 읽는다. pandas 객체의 내부 복사 방식 전체를 이 주석으로 일반화하지 않는다.

## 3. 학습용과 시험용 분리

### 강사님 코드 — 원본 발췌

출처: `D:/workspace_teacher/workspace_python/06_scikit_learn/01_main.py` 48–54행

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
```

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/06_scikit_learn/01_main.py` 51–57행

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size = 0.2, # 문제와 정답을 준 뒤 20퍼센트만 가지고 테스트하라는 것, 80퍼센트 학습
    random_state = 42, # 다른 숫자를 사용해도 되지만, 같은 값을 사용해야 결과도 같다
    stratify = y # 80%의 학습용 데이터에서 7(좋음):3(나쁨) 이라면 y의 정답데이터도 해당 퍼센트로 잡아라
)
```

`X_train`과 `y_train`은 같은 행의 입력·정답 쌍이고, `X_test`와 `y_test`는 나중에 평가할 쌍이다. `test_size=0.2`는 약 20%를 시험용으로 둔다. `random_state=42`는 이 분할의 난수 상태를 고정해 같은 환경에서 다시 비교하기 쉽게 한다. `stratify=y`는 0·1의 비율을 학습용과 시험용에서 가깝게 유지한다. 내 주석의 ‘7:3’은 설명용 예시이며 이 CSV의 실제 0·1 비율이 아니다.

## 직접 확인할 질문

1. `quality`를 `X`에 그대로 남기면 무엇이 문제인가?
2. `dataFrame.shape`의 두 숫자는 각각 무엇인가?
3. `stratify=y`는 어떤 비율을 지키려는가?

## 추가로 알면 좋은 것

결측치 대체·범주형 인코딩·특성 선택을 체계적으로 묶는 방법은 이번 코드의 중심이 아니다. 이 단계에서는 **실제로 만든 `X`, `y`와 분리 결과**를 먼저 읽는다.
