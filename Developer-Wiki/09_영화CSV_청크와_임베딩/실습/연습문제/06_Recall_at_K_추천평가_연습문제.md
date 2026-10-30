# 06. Recall@K — 좋아한 시험 영화 중 상위 추천이 찾아낸 비율 읽기 — 연습문제

[본문](../../06_Recall_at_K_추천평가.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원본·당시 내 코드·새 개선안을 구별한다. 예상 → 이유 → 한 가지 변경 순서로 푼다.

## 목표와 준비

관련 영화 집합·상위 K 추천 집합·교집합·분모를 설명한다. 기본 threshold와 실제 경로의 전달값을 구별하고 -1.0을 정상 Recall 점수와 섞지 않는다. 함수 구현과 현재 데이터의 추천 성능을 구별한다.

[본문 3절](../../06_Recall_at_K_추천평가.md#example)의 폴더·설치·입력·실행 조건부터 확인한다. 아래 필요한 파일 전체를 같은 구조로 저장한다. 가져오는 함수·모델 정의도 빠뜨리지 않는다.

## 문제 1. 실행 결과 예상

**evaluation_tools.py**

```python
def recall_at_k(user_id, test, recommendations, threshold=4.0, k=10):
    if k <= 0:
        raise ValueError('k는 양수여야 합니다.')
    relevant = set(test.loc[
        (test['userId'] == user_id) & (test['rating'] >= threshold), 'movieId'
    ])
    if not relevant:
        return -1.0
    recommended = {item['movieId'] for item in recommendations[:k]}
    return len(relevant & recommended) / len(relevant)
```

**example.py**

```python
import pandas as pd
from evaluation_tools import recall_at_k

test = pd.DataFrame([
    {'userId': 10, 'movieId': 3, 'rating': 4.5},
    {'userId': 10, 'movieId': 4, 'rating': 5.0},
    {'userId': 10, 'movieId': 9, 'rating': 3.0},
])
recommendations = [{'movieId': 3}, {'movieId': 5}, {'movieId': 4}]
print('Recall@1:', recall_at_k(10, test, recommendations, k=1))
print('Recall@2:', recall_at_k(10, test, recommendations, k=2))
print('Recall@3:', recall_at_k(10, test, recommendations, k=3))
print('관련 영화 없음:', recall_at_k(99, test, recommendations, k=2))
```

실행 전에 결과를 먼저 적는다. 자료의 모양·분류 결과·확률·점수·현재 변수의 대상을 구별한다.

<details>
<summary>풀이</summary>

```text
Recall@1: 0.5
Recall@2: 0.5
Recall@3: 1.0
관련 영화 없음: -1.0
```

시험의 3·4번 영화가 4점 이상이고 9번은 기준 미만이다. 첫 추천은 3이므로 절반을 찾는다. 두 번째 5는 관련 영화가 아니어서 @2도 절반이다. 세 번째에 4가 들어오므로 @3은 1.0이다. 사용자 99는 관련 영화가 없어 원본과 같은 표식 -1.0을 돌려준다. 전체 함수 정의를 함께 제공해 import 대상이 숨겨져 있지 않다.

| K | 잘라 본 추천 | 찾은 관련 영화 | Recall |
| --- | --- | --- | ---: |
|1 | 3 | 3 하나 | 0.5 |
|2 | 3·5 | 3 하나 | 0.5 |
|3 | 3·5·4 | 3·4 | 1.0 |
|관련 없음 | 비교 분모 없음 | 해당 없음 | 표식 -1.0 |

</details>

## 문제 2. 이유 설명

1. 새 예제 Recall@2의 분모는 왜 2인가?
2. 원본 경로의 실제 기준은 기본 4.0·10인가?
3. -1.0을 사용자 평균에 그대로 넣어도 되는가?

<details>
<summary>풀이</summary>

1. 기준 이상인 시험 영화가 3·4 두 개이기 때문이다.
2. 경로가 직접 2.0·50을 전달한다.
3. 정상 Recall 점수가 아닌 평가 불가 표식이므로 별도 정책이 필요하다.

</details>

## 문제 3. 한 가지만 바꾸기

| 한 가지만 변경 | 예상 |
| --- | --- |
|threshold를 5.0으로 | 관련 영화는 4 하나 |
|추천을 [3,3,4]로 | @2는 3 하나만 찾음·중복을 뒤 영화로 보충 안 함 |
|빈 추천·관련 영화 있음 | 0.0 |
|관련 영화 없음 | -1.0·정상 0점과 구별 |

<details>
<summary>막힐 때 확인</summary>

항상 -1이면 사용자와 시험 선호 기준을 확인한다. 점수가 낮으면 모델뿐 아니라 후보에 들어올 수 있는 영화 범위도 본다. 0.5가 왜 나왔는지 모르면 분자와 분모의 실제 ID 집합을 적는다. 기본값과 경로에서 직접 전달한 값이 다른지도 확인한다.

</details>

## 채점과 복습

정상 출력뿐 아니라 입력 열·정답·분할·평가 대상의 차이도 설명한다. 새 예제는 독립 실행이며 실제 검색·AI 서비스 성공과 구별한다. TIP 확장은 필수 조건이 아니다. 정의→입력→호출→반환→다음 평가의 흐름을 연결한다.
