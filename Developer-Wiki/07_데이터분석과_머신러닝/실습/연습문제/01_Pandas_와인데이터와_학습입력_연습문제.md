# 01. pandas — 와인 표를 읽고 문제와 정답을 따로 준비하기 — 연습문제

[본문](../../01_Pandas_와인데이터와_학습입력.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원본·당시 내 코드·새 개선안을 구별한다. 예상 → 이유 → 한 가지 변경 순서로 푼다.

## 목표와 준비

DataFrame·Series·행·열·특성·정답을 구별한다. 세미콜론 CSV를 확인하고 good을 만든 이유, quality와 good을 입력에서 뺀 이유, 네 분할 변수의 관계를 설명한다. 수업의 실제 와인 표와 아래 작은 가상 표의 숫자를 혼동하지 않는다.

[본문 3절](../../01_Pandas_와인데이터와_학습입력.md#example)의 폴더·설치·입력·실행 조건부터 확인한다. 아래 필요한 파일 전체를 같은 구조로 저장한다. 가져오는 함수·모델 정의도 빠뜨리지 않는다.

## 문제 1. 실행 결과 예상

**tiny_wine.csv**

```csv
alcohol;acidity;quality
8.0;6.0;5
8.5;6.1;6
9.0;6.2;5
9.5;6.3;6
10.0;6.4;5
11.0;6.5;7
11.5;6.6;8
12.0;6.7;7
12.5;6.8;8
13.0;6.9;7
```

**example.py**

```python
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
```

실행 전에 결과를 먼저 적는다. 자료의 모양·분류 결과·확률·점수·현재 변수의 대상을 구별한다.

<details>
<summary>풀이</summary>

```text
읽은 모양: (10, 3)
정답: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
입력 열: ['alcohol', 'acidity']
원본 열: ['alcohol', 'acidity', 'quality', 'good']
분할 크기: 8 2 8 2
학습 짝: True
시험 짝: True
시험 클래스: [0, 1]
```

첫 줄은 CSV를 읽은 직후이므로 3열이다. good을 추가하면 df는 4열이 된다. X는 두 정답 관련 열을 뺀 2열이고, 원본 df는 여전히 quality와 good을 가지고 있다. 마지막 검사는 값을 맞혔다는 평가가 아니라 **입력과 정답의 인덱스가 같은 순서인지** 보는 것이다.

`tolist()`·`columns`·`index.equals()`는 이 새 예제의 확인을 돕는 표기다. 당시 원본에 사용한 것처럼 인용하지 않는다. 8행을 학습, 2행을 시험으로 나누고 두 시험 행에는 0과 1이 하나씩 있다. 수업 CSV의 실제 비율은 이 가상 자료의 5:5와 다르다.

| 지점 | 원본 CSV 기준 모양 | 다음에 쓸 곳 |
| --- | --- | --- |
| 읽기 직후 | 1,599 × 12 | 요약 확인 |
| good 추가 | 1,599 × 13 | 입력·정답 분리 |
| X / y | 1,599 × 11 / 1,599개 | 짝인 분할 |
| X_train / y_train | 1,279 × 11 / 1,279개 | fit |
| X_test / y_test | 320 × 11 / 320개 | predict와 평가 |

정답이 있다는 말은 모든 측정값이 정확하다는 품질 보장이 아니다. 이 장에서는 우선 실제 파일의 모양과 정답 기준을 분명히 확인한다.

실제 분할에서 정답 0은 학습 1,105개·시험 277개, 정답 1은 학습 174개·시험 43개다. 정확히 같은 비율의 소수 행을 나눌 수는 없으므로 가까운 정수 개수로 나뉜다. 학생 CSV는 LF, 강사님 CSV는 CRLF여서 파일 바이트 크기와 해시는 다르지만 정규화한 텍스트와 읽은 표는 같다. 이는 모델 자료가 달랐다는 뜻이 아니다.

</details>

## 문제 2. 이유 설명

1. good을 만들고도 quality를 X에서 빼는 이유는?
2. stratify와 random_state는 각각 무엇을 정하는가?
3. 실제 CSV의 분할 크기와 가상 CSV의 분할 크기는?

<details>
<summary>풀이</summary>

1. quality로 good을 바로 계산할 수 있어 정답의 근거가 입력에 남기 때문이다.
2. 정답 클래스의 비율과 무작위 분할의 재현 조건이다.
3. 실제는 1,279/320, 가상은 8/2다. 각각의 입력과 정답은 같은 행을 가리킨다.

</details>

## 문제 3. 한 가지만 바꾸기

| 한 가지만 변경 | 확인할 결과 | 해석 |
| --- | --- | --- |
| 새 CSV에서 sep 생략 | 보통 한 열로 읽힘 | 파일 구분자와 맞지 않음 |
| good 기준을 8로 변경 | 7점 행은 0으로 바뀜 | 문제 정의가 달라짐 |
| X에서 good을 빼지 않음 | 정답 열이 입력에 남음 | 분류 시험의 의미가 달라짐 |
| random_state만 변경 | 같은 크기라도 선택 행이 바뀔 수 있음 | 분할과 크기는 다른 개념 |

<details>
<summary>막힐 때 확인</summary>

파일을 못 찾으면 Python 파일 위치와 현재 작업 폴더를 구별한다. quality 열을 못 찾으면 먼저 columns와 구분자를 본다. stratify 오류가 나면 작은 자료의 클래스 개수와 시험 크기가 충분한지 확인한다. info를 print로 다시 감싸면 요약 뒤 None이 보일 수 있는데, info가 요약을 출력하고 반환한 값 때문이다.

</details>

## 채점과 복습

정상 출력뿐 아니라 입력 열·정답·분할·평가 대상의 차이도 설명한다. 새 예제는 독립 실행이며 실제 와인 점수와 구별한다. TIP 확장은 필수 조건이 아니다. 정의→입력→호출→반환→다음 평가의 흐름을 연결한다.
