# 06. Recall@K — 좋아한 시험 영화 중 상위 추천이 찾아낸 비율 읽기

[영화 자료·추천 목차](README.md) · [읽기 안내](00_영화자료와_추천_읽기안내.md)

사용자 확인상 이 함수부터의 후반부는 놓친 수업의 강사님 코드를 옮긴 복습 자료다. 직접 작성 여부를 평가하지 않고 정의·작은 계산·호출 순서·결과 해석을 차근차근 설명한다. 복사 시작 경계는 사용자 추정임을 남긴다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

관련 영화 집합·상위 K 추천 집합·교집합·분모를 설명한다. 기본 threshold와 실제 경로의 전달값을 구별하고 -1.0을 정상 Recall 점수와 섞지 않는다. 함수 구현과 현재 데이터의 추천 성능을 구별한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

### 어떤 영화를 정답으로 볼까?

추천 평가는 실제 평점을 그대로 점수 예측과 비교할 수도 있고, 좋아할 영화를 상위 목록에 얼마나 넣었는지 볼 수도 있다. 이 함수는 시험 자료에서 특정 사용자의 평점이 threshold 이상인 영화를 관련 영화로 정한다. threshold=4.0이면 4점 이상을 좋아한 것으로 보는 평가 규칙이다. 이 규칙은 데이터가 스스로 알려 준 절대 기준이 아니다.

상위 k개 추천의 movieId를 집합으로 만들고 관련 영화와의 교집합 크기를 센다. `Recall@K = 상위 K에서 찾은 관련 영화 수 / 시험의 관련 영화 수`다. 예를 들어 관련 영화가 {3,4}이고 추천 상위 두 영화가 {3,5}면 하나를 찾았으므로 1/2=0.5다.

| 자리 | 새 예제 | 의미 |
| --- | --- | --- |
| relevant | 3·4 | 시험 평점 기준을 통과한 영화 |
| recommend[:2] | 3·5 | 현재 상위 두 추천 |
| 교집합 | 3 | 찾은 정답 영화 |
| 분모 | 2 | 추천 수가 아닌 관련 영화 수 |

상위 두 개 중 맞힌 비율인 Precision@2와 여기의 분모는 다르다. 이 코드가 계산하는 것은 Recall이다. K를 키우면 같은 고정 추천 순위의 더 많은 부분을 보지만, 사용자 만족이나 다른 지표까지 자동으로 좋아졌다고 결론 내리지는 않는다.

### 관련 영화가 없으면 왜 -1.0일까?

분모가 0이면 비율을 계산할 수 없다. 원본은 이 경우 -1.0을 반환해 “평가할 관련 영화 없음”을 표시한다. Recall의 정상 범위 0~1 안의 성능 점수가 아니다. 여러 사용자 평균을 낼 때 이를 그대로 더하면 평가가 왜곡될 수 있어 제외·표시 정책이 필요하다.

집합은 같은 영화 ID를 한 번만 센다. 추천에 중복이 있더라도 먼저 상위 k개를 자르고 집합으로 바꾸기 때문에 중복 자리를 뒤 영화로 자동 보충하지 않는다. 원본은 k나 threshold의 입력 조건을 엄격히 검사하지 않는다. 아래 새 함수는 k가 양수인지 확인하는 개선을 추가했다.

> 📚 **출처 · 본문 설명 확인:** 실제 수업의 recall_at_k와 /recommend/recall 정의를 직접 풀이했다. [Python 집합](https://docs.python.org/ko/3/library/stdtypes.html#set-types-set-frozenset)의 교집합 의미를 확인했으며 예제의 점수·표는 새로 구성했다. 배운 의미 확인 근거다. 아래 표·전체 예제·풀이를 외부 문장 그대로 옮기지 않았다. 확인일: 2026-10-30.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 필요한 파일 전체.** 같은 장의 폴더 구조를 유지한다. pandas가 필요하다. 아래 두 파일을 같은 폴더에 저장하고 `python example.py`를 실행한다. 입력은 가상 시험 평점과 미리 정한 추천 목록이다. 실제 추천 모델의 품질을 측정한 결과와 구별한다.



**[evaluation_tools.py](실습/책형_복습/06_Recall_at_K_추천평가/evaluation_tools.py) — 새 예제 전체 파일**

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

**[example.py](실습/책형_복습/06_Recall_at_K_추천평가/example.py) — 새 예제 전체 파일**

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

시험의 3·4번 영화가 4점 이상이고 9번은 기준 미만이다. 첫 추천은 3이므로 절반을 찾는다. 두 번째 5는 관련 영화가 아니어서 @2도 절반이다. 세 번째에 4가 들어오므로 @3은 1.0이다. 사용자 99는 관련 영화가 없어 원본과 같은 표식 -1.0을 돌려준다. 전체 함수 정의를 함께 제공해 import 대상이 숨겨져 있지 않다.

**실행 결과:**

```text
Recall@1: 0.5
Recall@2: 0.5
Recall@3: 1.0
관련 영화 없음: -1.0
```

<a id="my-code"></a>

## 4. 옮겨 둔 강사님 수업 코드를 따라 읽기

### 내 폴더에 옮긴 강사님 코드 — 원본

출처: `D:/workspace/workspace_python/08_langgraph/router/es_router.py` 641–683행 · **원본 발췌**

```python
def recall_at_k(
    userId:int, 
    test:pd.DataFrame,   # 정답 데이터
    recommend:list[dict], # 추천 목록
    threshold: float = 4.0, # 경계선에 대한 범위
    k:int=10
):
    # loc[]는 where조건처럼 사용할 수 있음
    # 내가 평점을 threshold 이상을 준 정답만 뽑자
    # 첫 번째 전달인자 : 조건
    # 두 번째 전달인자 : 특정 컬럼만 가져오기
    # relevant_movies  relevant(관련된)
    # 나와 관련된 영화 목록
    # pandas.Series 객체는 set으로 자동 형변환이 안된다
    # 그래서 set()으로 명시적 형변환
    relevant_movies = set(test.loc[ 
        # 첫 번째
        (test['userId'] == userId)
        & (test['rating'] >= threshold),

        # 두 번째
        'movieId'
    ])
    # 정답 데이터에 조건이 맞는 영화가 없어서 Recall 계산할 수 없다
    if len(relevant_movies) == 0 :
        return -1.0

    # 암시적, 묵시적 형변환
    recommend_moives = {
        item['movieId'] for item in recommend[:k]
    }

    # 추천 목록 중에서 내가 좋아하는 영화의 개수
    # 추천 중 정답 개수
    # & : 교집합
    hit_count = len(relevant_movies & recommend_moives)

    print('hit_count', hit_count)
    print('len(relevant_movies)', len(relevant_movies))

    # Recall@K = 맞힌 개수 / 전체 정답
    result = hit_count / len(relevant_movies)
    return result
```

**발췌 바로 풀이:** 이 후반부는 사용자 확인상 강사님 코드를 옮긴 학습 자료다. test에서 사용자·평점 기준을 함께 적용하고 상위 k개 추천의 ID 집합과 교집합을 구한다. recommend_moives는 변수 철자일 뿐 결과를 바꾸지는 않지만 의미가 분명한 이름이 읽기 쉽다.
### 내 폴더에 옮긴 강사님 코드 — 원본

출처: `D:/workspace/workspace_python/08_langgraph/router/es_router.py` 686–692행 · **원본 발췌**

```python
def recall(userId:int):
    test,_ = split_train_test()
    recommend = collaborative_filtering(userId, 50)
    threshold = 2.0
    k = 50

    return recall_at_k(userId, test, recommend, threshold, k)
```

**발췌 바로 풀이:** 경로는 함수 기본값과 달리 threshold=2.0·k=50을 직접 전달한다. 추천도 50개를 요청한다. 따라서 기본 threshold=4.0·k=10으로 평가했다고 설명하면 틀리다. 분할을 여기서 한 번, collaborative_filtering 안에서 다시 한 번 수행한다.

recall 경로는 test를 준비하고 collaborative_filtering(userId,50)으로 추천을 만든 뒤 recall_at_k에 시험 자료와 추천을 함께 준다. 실제 전달 기준은 2.0·50이다. 양쪽 사본의 현재 함수·경로는 같은 계산이므로 한 번 인용하고 풀이를 확장한다. 외부 서버는 필요 없지만 전체 경로에는 실제 CSV와 모델 학습이 있으므로 그 실행과 작은 계산 예제를 구별한다.

<a id="connections"></a>

## 5. import·함수·입력·출력이 연결되는 흐름

`/recommend/recall의 userId → 시간 분할의 test → 협업 필터링의 추천 50개 → recall_at_k(userId,test,recommend,2.0,50) → 관련 집합·추천 집합 → 교집합 비율 또는 -1.0`이다. 협업 함수는 05장에 전체 정의가 있다. 새 evaluation_tools는 이 마지막 계산만 분리한다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**코드에서 배울 점:** 분모가 없는 경우를 구분하고 집합으로 영화 ID를 비교한다. **검토할 한계:** 시험에만 있고 학습 카탈로그에 없는 영화도 분모에 포함될 수 있으며 현재 추천기는 그 영화를 후보로 만들지 못할 수 있다. K·선호 기준·후보 범위를 함께 기록해야 한다. **개선 방향:** 중복 추천·평가 제외 사용자·호출별 반복 분할 정책을 명시한다. 이 평가는 복사한 코드의 학습 포인트이며 학생 직접 구현 성과 평가가 아니다.

원본 오류·수업용 단순화·목적에 따른 설계를 나눈다. 새 개선안은 당시 내 코드나 D 드라이브 수정본이 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



사용자 확인상 강사님 코드를 옮긴 부분이다. 확보한 양쪽 함수와 경로는 같은 계산·전달값이므로 강사님 원문을 다시 붙이지 않는다. 정확한 복사 시작점은 사용자 추정임을 기록한다. 앞의 직접 작성 부분과 같은 출처로 묶어 평가하지 않는다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| K | 잘라 본 추천 | 찾은 관련 영화 | Recall |
| --- | --- | --- | ---: |
|1 | 3 | 3 하나 | 0.5 |
|2 | 3·5 | 3 하나 | 0.5 |
|3 | 3·5·4 | 3·4 | 1.0 |
|관련 없음 | 비교 분모 없음 | 해당 없음 | 표식 -1.0 |

| 한 가지만 변경 | 예상 |
| --- | --- |
|threshold를 5.0으로 | 관련 영화는 4 하나 |
|추천을 [3,3,4]로 | @2는 3 하나만 찾음·중복을 뒤 영화로 보충 안 함 |
|빈 추천·관련 영화 있음 | 0.0 |
|관련 영화 없음 | -1.0·정상 0점과 구별 |

항상 -1이면 사용자와 시험 선호 기준을 확인한다. 점수가 낮으면 모델뿐 아니라 후보에 들어올 수 있는 영화 범위도 본다. 0.5가 왜 나왔는지 모르면 분자와 분모의 실제 ID 집합을 적는다. 기본값과 경로에서 직접 전달한 값이 다른지도 확인한다.

**확인 범위:** 새 예제는 임시 폴더에서 Python 처리·요청 모양·고정 응답 가공을 확인한다. Elasticsearch나 AI 서비스의 실제 연결·적재·검색·임베딩·답변 성공을 재현한 것은 아니다. 원본 함수의 별도 검사도 외부 호출을 기록 대역으로 바꾼 범위이며 원본 파일과 패키지는 수정하지 않는다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 사용자별 평균 정책·다른 랭킹 지표·평가 후보를 제한하는 여러 방식·시간에 따른 반복 평가는 추가 학습이다. 현재 수업 코드의 Recall 계산은 본문에 두고 아직 구현하지 않은 고급 평가로 확대하지 않는다.



09 소스는 작업 중 변경을 감지해 2026-10-30 확보한 사본을 기준으로 집필했다. 이후 변경은 별도 재검토 대상이다. 확인한 라이브러리 의미와 수업 밖 확장을 구분한다. 위 출처는 본문의 설명 근거이며 TIP에 적힌 새 주제를 이미 배운 것으로 간주하지 않는다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. 새 예제 Recall@2의 분모는 왜 2인가?
2. 원본 경로의 실제 기준은 기본 4.0·10인가?
3. -1.0을 사용자 평균에 그대로 넣어도 되는가?

<details>
<summary>풀이 — 먼저 결과와 이유를 적은 뒤 펼치기</summary>

1. 기준 이상인 시험 영화가 3·4 두 개이기 때문이다.
2. 경로가 직접 2.0·50을 전달한다.
3. 정상 Recall 점수가 아닌 평가 불가 표식이므로 별도 정책이 필요하다.

</details>

| 빠른 찾기 | 핵심 |
| --- | --- |
|분자 | 상위 K가 찾은 관련 영화 수 |
|분모 | 시험의 관련 영화 수 |
|-1.0 | 분모 없음 표식 |
|실제 경로 | threshold 2.0·K 50 |

[장별 연습문제](실습/연습문제/06_Recall_at_K_추천평가_연습문제.md) · [다음: 실무 스타일](실무_코딩스타일.md)
