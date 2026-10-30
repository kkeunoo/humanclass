# 05. RAG — 검색 자료를 문맥으로 묶어 답변 요청까지 연결하기 — 연습문제

[본문](../../05_RAG_질문응답.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원본·당시 내 코드·새 개선안을 구별한다. 예상 → 이유 → 한 가지 변경 순서로 푼다.

## 목표와 준비

검색·문맥 구성·생성을 구별하고 RAG의 목적과 한계를 설명한다. hybrid의 반환 구조와 ask 함수의 전체 정의를 연결한다. 함수 이름과 실제 서비스 호출이 다를 수 있음을 읽고, 답변 규칙을 문자열로 보냈다는 사실과 그 규칙이 검증되었다는 사실을 구별한다.

[본문 3절](../../05_RAG_질문응답.md#example)의 폴더·설치·입력·실행 조건부터 확인한다. 아래 필요한 파일 전체를 같은 구조로 저장한다. 가져오는 함수·모델 정의도 빠뜨리지 않는다.

## 문제 1. 실행 결과 예상

**rag_tools.py**

```python
def build_context(results):
    contexts = []
    for index, result in enumerate(results):
        doc = result['document']
        contexts.append(
            f"[검색 결과 {index}] 문서ID={doc['id']} 청크={doc['chunk_index']}\n"
            f"제목={doc['title']}\n내용={doc['content']}"
        )
    return '\n-------\n'.join(contexts)


def ask_rag(question, search, generate):
    results = search(question)['results']
    if not results:
        return '제공된 문서에서 확인할 수 없습니다.'
    context = build_context(results)
    prompt = f'문맥에 있는 내용으로만 한국어로 답하세요.\n질문: {question}\n문맥:\n{context}'
    return generate(prompt)
```

**example.py**

```python
from rag_tools import ask_rag

calls = []


def fixed_search(question):
    if question != '메모리는?':
        return {'results': []}
    return {'results': [{'document': {
        'id': 1, 'chunk_index': 0, 'title': '노트북 A', 'content': 'RAM은 16GB입니다.',
    }, 'score': 0.03}]}


def fixed_generate(prompt):
    calls.append(prompt)
    return '고정 응답: RAM은 16GB입니다.'


print(ask_rag('메모리는?', fixed_search, fixed_generate))
print('질문 전달:', '메모리는?' in calls[0])
print('본문 전달:', 'RAM은 16GB입니다.' in calls[0])
print(ask_rag('무게는?', fixed_search, fixed_generate))
print('생성 대역 호출 수:', len(calls))
```

실행 전에 결과를 먼저 적는다. 자료의 모양·분류 결과·확률·점수·현재 변수의 대상을 구별한다.

<details>
<summary>풀이</summary>

```text
고정 응답: RAM은 16GB입니다.
질문 전달: True
본문 전달: True
제공된 문서에서 확인할 수 없습니다.
생성 대역 호출 수: 1
```

search와 generate는 전달받은 함수다. 실제 검색·모델을 호출하지 않고 고정 함수를 넣어 경계를 확인했다. build_context가 결과를 문자열로 만들고 ask_rag가 질문과 규칙을 붙여 generate에 넘긴다. 빈 결과 분기는 원본에 없는 새 개선안이며 그 경우 생성 대역을 호출하지 않는다. 고정 응답이 16GB라고 말한 것은 AI가 자료를 이해했다는 증거가 아니다. calls에 들어간 입력 문자열을 확인한 결과다.

| 새 호출 | 검색 결과 | 생성 호출 | 최종 결과 |
| --- | --- | --- | --- |
|메모리는? | 고정 문서 1개 | 1회 | 고정 응답 |
|무게는? | 없음 | 생략 | 새 코드의 없음 안내 |
|원본 빈 검색 | 없음 | 그대로 호출 | 실제 결과 미확인 |

</details>

## 문제 2. 이유 설명

1. 검색 결과가 prompt에 들어갔다고 사실성이 보장되는가?
2. 내 ask_gemini는 실제 어느 API를 호출하는가?
3. 새 예제에서 빈 검색의 생성 호출 수가 늘지 않는 이유는?

<details>
<summary>풀이</summary>

1. 아니다. 검색과 저장, 모델의 지시 준수·근거 확인을 따로 봐야 한다.
2. 원본 활성 줄은 OpenAI Responses이며 output_text를 반환한다.
3. 결과가 없으면 안내를 먼저 return하는 새 개선안 때문이다.

</details>

## 문제 3. 한 가지만 바꾸기

| 한 가지만 변경 | 확인 |
| --- | --- |
|고정 본문을 32GB로 | 전달 prompt는 바뀌지만 고정 응답은 그대로·대역의 한계 |
|검색 결과를 빈 목록으로 | 새 코드에서 생성 미호출 |
|필수 content 키 제거 | 문자열 구성에서 오류 |
|모델 대역을 예외 발생 함수로 | 현재 예제는 호출 실패를 바깥으로 전달 |

<details>
<summary>막힐 때 확인</summary>

답이 이상하면 모델부터 바꾸기 전에 검색 결과·본문·문맥·질문 순서로 확인한다. KeyError는 document 구조와 필드를 본다. 외부 서비스 오류는 응답 객체를 받기 전 단계이므로 output_text 접근과 구별한다. 함수가 다른 서비스를 부르면 이름이 아니라 활성 호출을 따라간다.

</details>

## 채점과 복습

정상 출력뿐 아니라 입력 열·정답·분할·평가 대상의 차이도 설명한다. 새 예제는 독립 실행이며 실제 검색·AI 서비스 성공과 구별한다. TIP 확장은 필수 조건이 아니다. 정의→입력→호출→반환→다음 평가의 흐름을 연결한다.
