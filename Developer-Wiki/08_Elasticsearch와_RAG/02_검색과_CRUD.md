# 02. 검색과 CRUD — 찾을 조건·응답 구조·문서 변경을 구별하기

[Elasticsearch·RAG 목차](README.md) · [읽기 안내](00_검색과_RAG_읽기안내.md)

검색어 하나를 보내도 어느 필드에 어떤 질문을 하는지에 따라 결과의 의미가 달라진다. 검색 요청의 dict와 검색 응답의 dict를 구별하고, 원본에서 만든 결과 목록이 실제 반환으로 이어지는지 확인한다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

match·multi_match·term·range·filter·정렬·집계의 역할을 설명한다. hits.hits와 _source를 읽고 formatter의 정의부터 반환까지 연결한다. index·get·update·delete가 어떤 ID의 무엇을 바꾸는지 구별한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

### 검색 방식은 필드와 목적을 함께 본다

`match`는 text에 맞춰 검색어를 분석하는 전문 검색이고 `multi_match`는 여러 필드를 대상으로 한다. `term`은 정확한 색인 용어를 찾는다. text가 분석된 뒤에는 원래 문장과 색인 용어가 다를 수 있으므로 term을 “문장 전체가 같은가” 또는 SQL LIKE와 같은 것으로 외우면 안 된다. 범주값을 그대로 찾는 category는 keyword로 매핑한 이유가 있다.

| 원하는 일 | 이 수업의 방식 | 구별할 것 |
| --- | --- | --- |
| 본문에 관련 단어 찾기 | match | 분석된 용어·관련도 |
| 제목·본문 함께 검색 | multi_match | fields의 대상 |
| 분류 정확히 찾기 | category의 term | 부분 문자열 아님 |
| 가격 범위 | range, gte/lte | 두 경계 포함 |
| 범주는 제한·본문은 관련 검색 | bool.filter + must | 통과 조건과 점수 기여 |
| 가격 오름차순 등 | sort | 관련도 순위와 다른 순서 |
| 범주별 문서 수 | terms aggregation | 문서 목록과 별도 집계 결과 |

filter는 조건을 만족하는지를 정하고 그 조건 자체로 관련도 점수를 올리는 용도가 아니다. 정렬을 price로 지정하면 상단이 가장 관련 있는 문서가 아니라 가격 조건의 앞 문서일 수 있다. 집계는 응답의 aggregations 안에 buckets로 나오지만 원본 select_all은 results와 total만 반환하므로 요청한 집계가 자동으로 API 반환에 포함되지는 않는다.

### 검색 응답에는 본문 이외의 정보가 있다

`hits` 바깥 묶음 안의 `hits`는 현재 반환된 검색 결과 목록이다. 목록의 한 hit에는 _id·_score·_source 등이 있다. _source만 꺼내면 본문만 남고, score도 담으면 관련도 숫자를 함께 읽을 수 있다. total은 현재 목록 길이와 다를 수 있다. 검색 조건에 맞는 전체 수와 이번 페이지의 반환 수는 다른 개념이기 때문이다.

원본 formatter는 total의 value만 남기고 relation은 버린다. 실제 서버에서 relation이 gte이면 그 값은 하한일 수 있어 무조건 정확한 전체 건수라고 일반화하면 안 된다. 아래 고정 응답은 relation=eq인 한 건으로 단순화했다.

### 문서 변경은 같은 검색 작업이 아니다

index는 지정한 ID의 본문을 색인하며 같은 ID에 기존 문서가 있으면 그 본문을 대체하는 방식이다. update의 doc은 전달한 필드의 부분 갱신이다. get은 ID로 문서를 읽고 delete는 지운다. Python dict의 `update()`와 Elasticsearch의 `es.update()`는 같은 함수가 아니며, 이 장의 로컬 dict 변경은 의미를 설명하는 작은 예제다.

> 📚 **출처 · 본문 설명 확인:** [Elastic term](https://www.elastic.co/docs/reference/query-languages/query-dsl/query-dsl-term-query) · [Match query](https://www.elastic.co/docs/reference/query-languages/query-dsl/query-dsl-match-query) · [Update API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-update) · [검색 API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-search). 배운 의미 확인 근거다. 아래 표·전체 예제·풀이를 외부 문장 그대로 옮기지 않았다. 확인일: 2026-10-30.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 필요한 파일 전체.** 같은 장의 폴더 구조를 유지한다. Python만으로 실행한다. 두 파일을 같은 폴더에 저장하고 `python example.py`를 실행한다. query는 전송하지 않은 요청 조건이고 response는 미리 만든 고정 응답이다. 문자열 분석·점수 계산·실제 검색 결과를 Python으로 재현한 예제가 아니다.



**[search_tools.py](실습/책형_복습/02_검색과_CRUD/search_tools.py) — 새 예제 전체 파일**

```python
def formatter(resp):
    results = []
    for hit in resp['hits']['hits']:
        results.append({
            'document': hit.get('_source', {}),
            'score': hit.get('_score'),
        })
    return {'results': results, 'total': resp['hits']['total']['value']}
```

**[example.py](실습/책형_복습/02_검색과_CRUD/example.py) — 새 예제 전체 파일**

```python
from search_tools import formatter

query = {'bool': {
    'filter': [{'term': {'category': 'laptop'}}],
    'must': [{'match': {'content': '메모리'}}],
}}
response = {'hits': {
    'total': {'value': 1, 'relation': 'eq'},
    'hits': [{'_id': '1', '_score': 2.0, '_source': {
        'id': 1, 'title': '메모리 안내', 'price': 100,
    }}],
}}
result = formatter(response)
print('필터:', query['bool']['filter'][0]['term'])
print('총수·반환수:', result['total'], len(result['results']))
print('제목·점수:', result['results'][0]['document']['title'], result['results'][0]['score'])
document = {'id': 1, 'title': '메모리 안내', 'price': 100}
print('잘못된 키:', document.get(id, -1))
print('문자열 키:', document.get('id', -1))
document.update({'price': 120})
print('부분 변경 뒤:', document['title'], document['price'])
```

formatter는 응답 한 건마다 document와 score를 묶어 results에 담는다. 바깥 함수가 그 반환을 받은 뒤 제목과 점수에 접근한다. id에 따옴표를 붙이지 않으면 Python의 내장 함수 객체가 키 자리에 들어가 보통 -1이 나온다. 마지막은 Python dict의 가격만 바꾸어 나머지 제목이 남는 모습을 확인한다. 실제 es.update의 전송·응답 검증과는 구별한다.

**실행 결과:**

```text
필터: {'category': 'laptop'}
총수·반환수: 1 1
제목·점수: 메모리 안내 2.0
잘못된 키: -1
문자열 키: 1
부분 변경 뒤: 메모리 안내 120
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

### 내 코드 — 원본

출처: `D:/workspace/workspace_python/07_elastic/router/es_router.py` 256–267행 · **원본 발췌**

```python
# select의 like처럼 정확히 일치하는 값을 검색
@router.get('/es/select/term')
def term(keyword:str):
    response = es.search(
        index='computer',
        query={'term' : {
            # 'category' : keyword 
            'content' : keyword 
        }} 
    )

    return {"msg" : formatter(response)}
```

**발췌 바로 풀이:** 실제 term 대상은 content다. 주석 처리한 category를 실행 대상으로 읽지 않는다. text 필드의 정확한 색인 용어 검색을 문장 전체 일치나 부분 문자열 검색으로 설명하지 않는다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/07_elastic/router/es_router.py` 270–281행 · **원본 발췌**

```python
def range_(max:int, min:int = 0):
    response = es.search(
        index='computer',
        query={'range' : {
            'price' : {
                'gte' : min,
                'lte' : max
            } 
        }} 
    )

    return {"msg" : formatter(response)}
```

**발췌 바로 풀이:** min 기본값은 0이고 max는 호출에서 받는다. price에 gte와 lte를 사용해 경계를 포함한다. min이 max보다 큰 경우를 자동으로 바꾸는 코드는 없다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/07_elastic/router/es_router.py` 203–213행 · **원본 발췌**

```python
    results = []
    for hit in response['hits']['hits'] :
        document = hit.get('_source', {})
        results.append(document)

    return {
        'msg' : {
            'results' : results,
            'total' : response['hits']['total']['value']
        }
    }
```

**발췌 바로 풀이:** 만든 results를 실제 반환에 사용했다. 이 반환에는 원본 hit의 _id·_score가 없고 본문만 있다. 강사님은 같은 목록을 만들고도 response를 반환하므로 둘의 응답 구조가 다르다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/07_elastic/router/es_router.py` 324–335행 · **원본 발췌**

```python
@router.post('/es/crud/insert')
def insert_document(document : dict): # 데이터가 이미 있으면 update가 됨
    response = es.index(
        index='computer',
        id=document.get('id', -1),
        document=document
    )

    return {
        'response' : response,
        "msg" : 'document 추가 완료'
    }
```

**발췌 바로 풀이:** 내 코드는 문자열 id 키를 읽는다. 강사님 원문의 따옴표 없는 id는 내장 함수여서 다른 키다. 내 구현도 누락 때 -1을 사용하므로 여러 문서가 같은 ID로 덮어써질 수 있다. 올바른 키 읽기와 필수 입력 검증은 별개의 문제다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/07_elastic/util.py` 48–60행 · **원본 발췌**

```python
def formatter(resp):
    results = []
    for hit in resp['hits']['hits'] :
        # document = hit.get('_source', {})
        results.append({
            'document' : hit.get('_source', {}),
            'score' : hit.get('_score')
        })

    return {
        'results' : results,
        'total' : resp['hits']['total']['value']
    }
```

**발췌 바로 풀이:** 다른 라우터들이 import하는 실제 formatter 정의다. 본문은 document, 점수는 score로 담고 total의 value를 꺼낸다. 이 함수는 검색을 수행하지 않으며 들어온 응답의 정해진 구조를 가공한다. 키가 없는 임의 dict까지 자동으로 복구하는 함수도 아니다.

원본 select_all은 match_all과 category 집계를 요청한다. 그 뒤 _source 목록을 만들어 반환한다. 다른 검색 경로들은 공통 formatter로 응답을 바꾼다. bool 필터와 정렬, update·get·delete도 같은 es 클라이언트를 사용하지만 읽기와 변경을 구분해야 한다. 일부 변경 함수는 예외를 print한 뒤 빈 dict를 반환하므로 호출자는 빈 결과와 실패를 구분하기 어렵다.

<a id="connections"></a>

## 5. import·함수·입력·출력이 연결되는 흐름

`경로 인자 → query dict → es.search → 검색 응답 → util.formatter → results/total → HTTP 반환`이다. es.search의 입력 dict와 응답 dict는 모양과 목적이 다르다. select_all은 formatter 대신 본문 목록을 직접 만든다. CRUD에서는 주소의 id 또는 입력 dict의 문자열 id를 es 메서드에 전달하므로 값이 어디서 온 것인지까지 추적한다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 내 select_all은 만든 목록을 그대로 반환해 이름과 결과가 맞고, 삽입에서 문자열 id 키를 읽었다. **아쉬운 점:** -1 기본값은 누락 문서들을 같은 대상으로 만들 수 있고 예외를 출력만 하면 API의 실패가 흐려진다. **개선:** 응답에 무엇을 보존할지 결정하고 필수 ID·허용 정렬 필드를 확인한다. 부분 갱신과 전체 본문 대체를 주석에 정확히 적는다. 이 개선은 당시 적용 코드와 구별한다.

원본 오류·수업용 단순화·목적에 따른 설계를 나눈다. 새 개선안은 당시 내 코드나 D 드라이브 수정본이 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교

출처: `D:/workspace_teacher/workspace_python/07_elastic/router/es_router.py` 180–190행 · **원본 발췌**

```python
    results = []
    for hit in response["hits"]["hits"]:
        document = hit.get("_source", {})
        results.append(document)

    return {
        "msg": {
            "results": response, 
            "total": response["hits"]["total"]["value"]
        }
    }
```

출처: `D:/workspace_teacher/workspace_python/07_elastic/router/es_router.py` 307–318행 · **원본 발췌**

```python
@router.post('/es/crud/insert')
def insert_document(document : dict) :
    response = es.index(
        index='computer',
        id=document.get(id, -1),
        document=document
    )

    return { 
        'response': response,
        "msg": 'document 추가 완료'
    }
```

첫 인용은 강사님이 results를 만들어 놓고 response를 반환한 부분이고, 둘째는 document.get(id, -1)이다. 내 코드는 이 두 지점에서 의도한 반환·문자열 키 사용이 더 명확하다. 다만 원점수·메타데이터가 필요해 전체 response를 의도적으로 반환하는 설계도 가능하다. 같은 동작의 range·formatter는 중복 인용하지 않는다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 표현 | 자료 | 이 장의 값 |
| --- | --- | --- |
|query | 전송 조건 | category 필터·content 검색 |
|response.hits.hits | 고정 hit 목록 | 1건 |
|hit._source | 본문 dict | 제목·가격 |
|formatter 결과 | document·score 목록 | 제목과 2.0 |
|total | 고정 응답의 eq 값 | 1 |

| 한 가지만 변경 | 예상 |
| --- | --- |
|고정 hits를 빈 목록으로 | 결과 목록이 비어짐 |
|total만 30으로 | 반환수 1과 총수 30은 다름 |
|_score 생략 | get 때문에 None |
|본문에서 id 제거 | 현재 get의 기본 -1 |
|range의 lte를 lt로 | 실제 서버에서는 상한 제외·로컬 예제로 검색하지 않음 |

검색어가 안 나오면 먼저 필드의 매핑·분석·검색 방식을 확인한다. total과 목록 길이가 다르다고 즉시 오류로 단정하지 않는다. formatter의 KeyError는 응답이 search의 예상 구조인지 본다. 수정 뒤 다른 필드가 남아 있다면 부분 갱신의 목적을 확인한다.

**확인 범위:** 새 예제는 임시 폴더에서 Python 처리·요청 모양·고정 응답 가공을 확인한다. Elasticsearch나 AI 서비스의 실제 연결·적재·검색·임베딩·답변 성공을 재현한 것은 아니다. 원본 함수의 별도 검사도 외부 호출을 기록 대역으로 바꾼 범위이며 원본 파일과 패키지는 수정하지 않는다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 입력 스키마 강화·실패를 HTTP 상태로 구분하는 정책·페이지 처리·집계 오차·refresh 시점의 상세 동작은 추가 학습이다. 현재는 요청 조건과 응답 모양, 실제 ID·변경 대상을 먼저 설명한다.

확인한 라이브러리 의미와 수업 밖 확장을 구분한다. 위 출처는 본문의 설명 근거이며 TIP에 적힌 새 주제를 이미 배운 것으로 간주하지 않는다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. term을 SQL LIKE라고 설명하면 안 되는 이유는?
2. results를 만들고 response를 반환하면 무엇이 달라지는가?
3. index와 update의 doc은 같은 변경 방식인가?

<details>
<summary>풀이 — 먼저 결과와 이유를 적은 뒤 펼치기</summary>

1. 부분 문자열이 아니라 정확한 색인 용어를 찾기 때문이다.
2. 단순 본문 목록 대신 원본 검색 응답 구조가 반환된다.
3. 같은 ID의 본문 대체와 전달한 필드의 부분 갱신을 구별한다.

</details>

| 빠른 찾기 | 핵심 |
| --- | --- |
|term | 정확한 색인 용어 |
|gte/lte | 경계 포함 |
|formatter | 응답 가공·검색 아님 |
|id / 문자열 id | 내장 함수 / dict의 이름 키 |
|doc | 부분 갱신 내용 |

[장별 연습문제](실습/연습문제/02_검색과_CRUD_연습문제.md) · [다음: 청크와 임베딩](03_청크와_임베딩.md)
