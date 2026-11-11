# 하이브리드 추천에서 CBF와 CF의 순위를 합치기

[단원 목차](README.md) · [연습문제](실습/연습문제/07_CBF_CF와_RRF_하이브리드추천_연습문제.md) · [이전](06_Recall_at_K_추천평가.md) · [다음](../10_LangChain과_LangGraph/01_모델호출과_메시지.md)

<a id="learn"></a>

## 1. 이 장에서 배울 것

CBF와 CF가 각각 어떤 후보를 만들고, `candidate_size`와 `top_k`가 어디에 쓰이는지 설명한다. 영화 ID마다 순위 점수를 합산하고, 중복을 제거하면서 기존 순서를 보존한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

CBF는 좋아한 영화의 장르·태그를 이용해 비슷한 내용을 찾는다. CF는 여러 사용자의 평점 관계를 이용해 아직 평가하지 않은 영화의 점수를 예측한다. 두 후보 목록의 원래 점수는 단위가 다르다. RRF(Reciprocal Rank Fusion)는 각 목록에서의 **순위**를 `1 / (60 + 순위)`로 바꿔 영화 ID별로 더한다. 양쪽 목록에 있는 영화는 두 점수를 받는다.

| ID | CBF 순위 | CF 순위 | 합산 |
| --- | --- | --- | --- |
| 30 | 2 | 1 | `1/62 + 1/61` |
| 10 | 1 | 없음 | `1/61` |
| 20 | 없음 | 2 | `1/62` |

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**설명용 전체 예제.** [실행 파일](실습/책형_복습/07_CBF_CF와_RRF_하이브리드추천/example.py)을 해당 장의 Python 환경으로 실행한다. 모든 입력과 모델 대역은 복습용이며 외부 서비스에 요청하지 않는다.

```python
from collections import defaultdict

cbf_ids = [10, 30, 10]
cf_ids = [30, 20]
scores = defaultdict(float)
for ids in (cbf_ids, cf_ids):
    for rank, movie_id in enumerate(dict.fromkeys(ids), start=1):
        scores[movie_id] += 1 / (60 + rank)

ordered = sorted(scores.items(), key=lambda item: (-item[1], item[0]))
print([(movie_id, round(score, 5)) for movie_id, score in ordered])
```

**실행 결과**

```text
[(30, 0.03252), (10, 0.01639), (20, 0.01613)]
```

<a id="my-code"></a>

## 4. 내 폴더의 실제 코드 읽기

**원본 발췌 · D:/workspace/workspace_python/08_langgraph/router/es_router.py 744–806행**

```python
def hybrid_filtering(
    list_movieId: list[int],    # CBF에서 사용 할 영화 목록
    userId: int,                # CF에서 사용 할 사용자 id
    top_k:int = 10,             # 결과 개수
    candidate_size:int = 50     # 각각의 추천에의 후보 수
):
    pass
    # CBF 추천
    # def content_based_filtering(list_movieId: list):
    # response_cbf = content_based_filtering(list_movieId)
    response_cbf = content_based_filtering(list_movieId, candidate_size)
    # return response_cbf

    result_cbf = set()
    for hit in response_cbf['hits']['hits'] :
        # movieId가 int지만 혹시 모르니 다시 한 번 형변환
        movieId = int(hit['_source']['movieId'])
        # title = hit['_source']['title']

        # 내가 안 본 영화ID만 중복 없이 담는다
        if movieId not in list_movieId :
            result_cbf.add(movieId)
        # if movieId not in list_movieId :
        #     result_cbf.append({
        #         'movieId' : movieId,
        #         'title' : title
        #     })

    # CF 추천
    response_cf = collaborative_filtering(userId, candidate_size)
    # return response_cf

    result_cf = set()
    for hit in response_cf :
        movieId = int(hit.get('movieId'))

        if movieId not in list_movieId :
            result_cf.add(movieId)

    # RRF
    # 강사님 같이 진행
    rrf_score = {}
    # CBF의 RRF 점수 계산
    for index, movieId in enumerate(result_cbf, start=1) :
        if rrf_score.get(movieId) :
            rrf_score[movieId] += 1 / (60 + index)
        else :
            rrf_score[movieId] = 1 / (60 + index)

    # CF의 RRF 점수 계산
    for index, movieId in enumerate(result_cf, start=1) :
        if rrf_score.get(movieId) :
            rrf_score[movieId] += 1 / (60 + index)
        else :
            rrf_score[movieId] = 1 / (60 + index)
    # 점수 높은 순으로 정렬
    result = sorted(
        rrf_score.items(), 
        key=lambda x: x[1], 
        reverse=True
    )

    return result[:top_k]
```

**풀이:** CBF의 청크 응답에서는 `_source.movieId`, CF의 추천 목록에서는 `movieId`를 꺼낸다. `list_movieId`에 있는 영화는 후보에서 제외한다. 두 집합에 각각 순위를 붙여 같은 점수표에 더하고 상위 `top_k`개의 `(영화 ID, 점수)`를 반환한다.

<a id="connections"></a>

## 5. import·함수·입력·출력이 연결되는 흐름

`/recommend/hybrid` → `hybrid()` → `hybrid_filtering()` → [CBF](04_영화검색과_콘텐츠기반추천.md)와 [CF](05_시간분할과_협업필터링.md) → 순위 점수 → `movies.csv`에서 제목 조회 → 영화 ID별 제목과 점수. `candidate_size`는 두 검색에 넘기는 후보 크기이며 청크 중복과 제외 조건 때문에 실제 후보 영화 수가 줄 수 있다.

**원본 발췌 · D:/workspace/workspace_python/08_langgraph/router/es_router.py 857–887행**

```python
@router.get('/recommend/hybrid')
def hybrid(
    userId: int,                # CF에서 사용 할 사용자 id
    top_k:int = 10,             # 결과 개수
    candidate_size:int = 50,     # 각각의 추천에의 후보 수
    list_movieId: list[int] = Query(...)    # CBF에서 사용 할 영화 목록
):  
    result_hybrid = hybrid_filtering(list_movieId, userId, top_k, candidate_size)
    df_movies = util.load_csv('movies.csv')

    result = {}
    for i in result_hybrid :
        movieId = i[0]
        score = i[1]
        title = df_movies.loc[
            # loc에 3을 쓰면 세 번째 컬럼일 수 있음
            df_movies['movieId'] == movieId,
            'title'
        ].iloc[0] # loc는 조건에 따라 가는데, iloc는 행의 순서를 가져옴 integer location
        '''
        iloc : 결과 중 몇 번째 줄
            224 Star Wars: Episode IV - A New Hope (1977).
            Name: title, dtype: object
        '''

        result[movieId] = {
            'title' : title,
            'score' : score
        }

    return result
```

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점.** 서로 다른 추천 방식을 함수로 나누고 최종 정렬에서 점수의 기준을 하나로 맞췄다.

**아쉬운 점.** `set` 순회 순서는 검색 결과 순위를 담지 않는다. CBF와 CF의 기존 순위를 살리려면 순서 있는 목록에 추가하면서 별도 `seen`으로 중복을 검사하거나, 이 예제처럼 `dict.fromkeys()`로 첫 등장 순서를 유지한다. 제목 조회의 `.iloc[0]`는 해당 영화가 CSV에 없을 때 실패할 수 있다. 후보 ID와 제목의 매칭 실패도 결과에서 구분할 수 있다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교

양쪽 구현은 후보를 집합에 넣은 뒤 같은 방식으로 점수를 합한다. 강사님 코드도 순위 보존은 별도로 개선할 부분이다. 내 코드는 CF 후보 ID를 `int()`로 맞추고, 강사님 코드는 받은 값을 그대로 사용한다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

CBF의 `[10, 30, 10]`이 `[10, 30]`으로 줄어드는 순서를 적는다. CF에 있는 30이 양쪽 점수를 받는 것을 확인한다. CBF 순서를 `[30, 10, 10]`으로 바꿔 각 영화 점수의 변화를 비교한다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **추가로 알면 좋은 것:** 동점 처리와 후보 수에 따른 품질 변화는 같은 평가 자료에서 비교한다. 이 장은 Python에서 영화 ID의 순위를 합친다. Elasticsearch 요청에 검색기 두 개를 넣는 실습은 [08 단원의 검색 RRF](../08_Elasticsearch와_RAG/04_벡터와_하이브리드검색.md)에서 읽는다.

📚 [Elastic RRF의 순위 점수 식](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/reciprocal-rank-fusion)

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. 영화 30이 1위를 차지하는 이유를 설명한다.
2. 중복 제거에 `set()`을 쓰면 어떤 정보가 사라지는가?
3. `candidate_size=50`, `top_k=10`의 역할을 구별한다.

[풀이를 접어 둔 연습문제](실습/연습문제/07_CBF_CF와_RRF_하이브리드추천_연습문제.md)에서 확인한다.

[단원 목차](README.md) · [연습문제](실습/연습문제/07_CBF_CF와_RRF_하이브리드추천_연습문제.md) · [이전](06_Recall_at_K_추천평가.md) · [다음](../10_LangChain과_LangGraph/01_모델호출과_메시지.md)
