# 02. 검색 결과를 읽고 문서를 고치기

[이전: 연결·적재](01_연결과_문서적재.md) · [목차](README.md) · [다음: 청크와 임베딩](03_청크와_임베딩.md)

`match`는 분석된 텍스트 필드의 검색어를 찾고, `multi_match`는 여러 필드를 검색한다. `term`은 색인된 **정확한 용어**를 찾는다. 범위 검색과 필터도 양쪽 원본에 있다.

## 먼저: 어떤 질문에 어떤 검색을 쓸까?

앞 장에서 `title`·`content`는 `text`, `category`는 `keyword`, `price`는 숫자로 정했다. 따라서 검색 방식은 **찾을 필드와 원하는 결과**에 맞춰 읽는다.

| 이해용 질문 | 수업 코드에서 살필 방식 | 핵심 |
| --- | --- | --- |
| 제목 또는 본문에 검색어가 있는가? | `match`, `multi_match` | 분석된 텍스트 검색 |
| 분류값이 정확히 같은가? | `term`과 `keyword` 필드 | 정확한 용어 검색 |
| 가격이 0~100 사이인가? | `range`의 `gte`, `lte` | 양쪽 경계 포함 |

이 표의 질문은 **설명용 예시**다. 실제 응답 건수는 인덱스에 들어 있는 문서와 검색 요청을 실행해야 알 수 있다. 검색은 읽기이고, 뒤의 `index`·`update`·`delete`는 문서를 바꾸는 동작이다.

## 같은 검색을 다른 필드에 적용

`term`을 `text` 필드에 써도 ‘문장 전체가 정확히 같은가?’를 검사한다고 단순화하면 안 된다. 실제 실행 대상은 두 원본 모두 `content`이며, 주석에 남은 `category`는 실행되지 않는다.

### 강사님 코드 — 원본 발췌

출처: `D:/workspace_teacher/workspace_python/07_elastic/router/es_router.py` 225–237행

```python
# term
# select의 like 처럼 정확히 일치하는 값
@router.get('/es/select/term')
def term(keyword: str):
    response = es.search(
        index="computer",
        query={"term": {
            # 'category': keyword
            'content': keyword
        }}
    )

    return { "msg": formatter(response) }
```

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/07_elastic/router/es_router.py` 256–267행

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

두 코드 모두 `term`의 실제 대상은 `content`다. 바로 위에서 `category` 검색을 주석 처리했다. `content`는 `text`라 문장 전체의 정확한 일치를 기대하면 안 된다. **범주값의 정확한 일치**를 확인하려면 이 실습의 `category`처럼 `keyword` 필드를 대상으로 삼는 편이 알맞다. 주석의 “SQL LIKE처럼”도 부정확하다. `term`은 부분 문자열 검색이 아니다.

### 강사님 코드 — 원본 발췌

출처: `D:/workspace_teacher/workspace_python/07_elastic/router/es_router.py` 243–255행

```python
@router.get('/es/select/range')
def range_(max:int, min:int = 0):
    response = es.search(
        index="computer",
        query={"range": {
            'price': {
                'gte': min,
                'lte': max
            }
        }}
    )

    return { "msg": formatter(response) }
```

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/07_elastic/router/es_router.py` 270–281행

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

`range`는 `price`를 `min` 이상·`max` 이하로 제한한다. 이 외에 양쪽은 `match`, `multi_match`, `bool.filter`, 정렬, 범주별 집계도 실습한다. 처음에는 필드가 `text`인지 `keyword`인지, 결과가 점수 순인지 조건만 통과했는지를 구별해 읽는다.

## 반환값에서는 내 코드가 더 일관적

검색 응답의 `hits.hits`는 각 결과와 `_source` 같은 내부 정보를 담는다. 호출자에게 문서 본문만 보여 주려면 `_source`를 꺼낸 `results`를 반환해야 한다. 아래 두 코드는 같은 목록을 만들지만 **마지막 반환 변수**가 다르다.

### 강사님 코드 — 원본 발췌

출처: `D:/workspace_teacher/workspace_python/07_elastic/router/es_router.py` 180–190행

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

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/07_elastic/router/es_router.py` 203–213행

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

두 함수 모두 검색 응답의 `hits.hits`에서 `_source`를 꺼내 `results` 목록을 만든다. 하지만 강사님 코드는 만든 목록 대신 원본 `response`를 반환한다. 내 코드는 **`results`를 반환**하므로 `total`과 나란히 간단한 문서 목록을 받는다. 원본 점수와 메타데이터까지 필요하면 원본 응답을 선택할 수 있지만, 변수명과 반환 형태는 일치시켜야 읽기 쉽다.

## 새 문서의 ID와 부분 수정

`es.index`는 지정한 ID에 문서를 넣고, `es.update(..., doc=...)`는 전달한 필드를 갱신한다. ID를 잘못 읽으면 의도하지 않은 문서를 바꿀 수 있으므로 아래의 `id`와 `'id'` 차이를 코드 그대로 비교한다.

### 강사님 코드 — 원본 발췌

출처: `D:/workspace_teacher/workspace_python/07_elastic/router/es_router.py` 307–318행

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

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/07_elastic/router/es_router.py` 324–335행

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

강사님 `document.get(id, -1)`의 `id`는 문자열 키가 아니라 Python 내장 함수다. 보통 입력 딕셔너리에 그 키가 없으므로 `-1`이 선택된다. 내 `document.get('id', -1)`은 실제 `'id'` 키를 읽는다. 다만 내 코드도 ID가 없으면 모든 누락 문서에 `-1`을 쓰므로, 입력을 확인하지 않고 여러 번 호출하면 같은 ID에 덮어쓸 수 있다.

양쪽 `update_document`는 `es.update(..., doc=document)`를 사용한다. 주석에 “전체 덮어쓰기”라고 쓰여도 `doc`은 **전달한 필드의 부분 갱신**으로 읽어야 한다. 조회는 `es.get`, 삭제는 `es.delete`를 호출한다. 실제 서버에 쓰는 동작이라 문서 읽기 검증에서는 호출하지 않았다.

## 직접 확인할 질문

1. `document.get(id, -1)`과 `document.get('id', -1)`의 차이는?
2. `results`를 만들고 `response`를 돌려주면 호출자는 어떤 자료형을 받는가?
3. 가격 범위의 `gte`, `lte`는 경계값을 포함하는가?

## 추가로 알면 좋은 것

> 💡 **TIP · 수업 범위 밖:** 없는 ID에 대한 예외를 HTTP 상태 코드로 바꾸는 설계나 엄격한 입력 스키마는 이 함수들의 현재 실습 중심이 아니다.

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/02_검색과_CRUD_연습문제.md) → [다음 장에서 청크 만들기](03_청크와_임베딩.md)
