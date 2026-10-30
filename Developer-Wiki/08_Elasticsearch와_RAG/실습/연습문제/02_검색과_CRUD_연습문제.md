# 02. 검색과 CRUD — 찾을 조건·응답 구조·문서 변경을 구별하기 — 연습문제

[본문](../../02_검색과_CRUD.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원본·당시 내 코드·새 개선안을 구별한다. 예상 → 이유 → 한 가지 변경 순서로 푼다.

## 목표와 준비

match·multi_match·term·range·filter·정렬·집계의 역할을 설명한다. hits.hits와 _source를 읽고 formatter의 정의부터 반환까지 연결한다. index·get·update·delete가 어떤 ID의 무엇을 바꾸는지 구별한다.

[본문 3절](../../02_검색과_CRUD.md#example)의 폴더·설치·입력·실행 조건부터 확인한다. 아래 필요한 파일 전체를 같은 구조로 저장한다. 가져오는 함수·모델 정의도 빠뜨리지 않는다.

## 문제 1. 실행 결과 예상

**search_tools.py**

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

**example.py**

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

실행 전에 결과를 먼저 적는다. 자료의 모양·분류 결과·확률·점수·현재 변수의 대상을 구별한다.

<details>
<summary>풀이</summary>

```text
필터: {'category': 'laptop'}
총수·반환수: 1 1
제목·점수: 메모리 안내 2.0
잘못된 키: -1
문자열 키: 1
부분 변경 뒤: 메모리 안내 120
```

formatter는 응답 한 건마다 document와 score를 묶어 results에 담는다. 바깥 함수가 그 반환을 받은 뒤 제목과 점수에 접근한다. id에 따옴표를 붙이지 않으면 Python의 내장 함수 객체가 키 자리에 들어가 보통 -1이 나온다. 마지막은 Python dict의 가격만 바꾸어 나머지 제목이 남는 모습을 확인한다. 실제 es.update의 전송·응답 검증과는 구별한다.

| 표현 | 자료 | 이 장의 값 |
| --- | --- | --- |
|query | 전송 조건 | category 필터·content 검색 |
|response.hits.hits | 고정 hit 목록 | 1건 |
|hit._source | 본문 dict | 제목·가격 |
|formatter 결과 | document·score 목록 | 제목과 2.0 |
|total | 고정 응답의 eq 값 | 1 |

</details>

## 문제 2. 이유 설명

1. term을 SQL LIKE라고 설명하면 안 되는 이유는?
2. results를 만들고 response를 반환하면 무엇이 달라지는가?
3. index와 update의 doc은 같은 변경 방식인가?

<details>
<summary>풀이</summary>

1. 부분 문자열이 아니라 정확한 색인 용어를 찾기 때문이다.
2. 단순 본문 목록 대신 원본 검색 응답 구조가 반환된다.
3. 같은 ID의 본문 대체와 전달한 필드의 부분 갱신을 구별한다.

</details>

## 문제 3. 한 가지만 바꾸기

| 한 가지만 변경 | 예상 |
| --- | --- |
|고정 hits를 빈 목록으로 | 결과 목록이 비어짐 |
|total만 30으로 | 반환수 1과 총수 30은 다름 |
|_score 생략 | get 때문에 None |
|본문에서 id 제거 | 현재 get의 기본 -1 |
|range의 lte를 lt로 | 실제 서버에서는 상한 제외·로컬 예제로 검색하지 않음 |

<details>
<summary>막힐 때 확인</summary>

검색어가 안 나오면 먼저 필드의 매핑·분석·검색 방식을 확인한다. total과 목록 길이가 다르다고 즉시 오류로 단정하지 않는다. formatter의 KeyError는 응답이 search의 예상 구조인지 본다. 수정 뒤 다른 필드가 남아 있다면 부분 갱신의 목적을 확인한다.

</details>

## 채점과 복습

정상 출력뿐 아니라 입력 열·정답·분할·평가 대상의 차이도 설명한다. 새 예제는 독립 실행이며 실제 검색·AI 서비스 성공과 구별한다. TIP 확장은 필수 조건이 아니다. 정의→입력→호출→반환→다음 평가의 흐름을 연결한다.
