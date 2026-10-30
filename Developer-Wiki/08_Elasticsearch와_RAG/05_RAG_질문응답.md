# 05. RAG — 검색 자료를 문맥으로 묶어 답변 요청까지 연결하기

[Elasticsearch·RAG 목차](README.md) · [읽기 안내](00_검색과_RAG_읽기안내.md)

RAG는 모델 이름 하나가 아니라 검색과 답변 생성을 잇는 흐름이다. 질문이 어느 함수로 들어가고 어떤 검색 자료가 prompt에 담기며 마지막 문자열이 어디에서 오는지 한 단계씩 따라간다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

검색·문맥 구성·생성을 구별하고 RAG의 목적과 한계를 설명한다. hybrid의 반환 구조와 ask 함수의 전체 정의를 연결한다. 함수 이름과 실제 서비스 호출이 다를 수 있음을 읽고, 답변 규칙을 문자열로 보냈다는 사실과 그 규칙이 검증되었다는 사실을 구별한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

### 검색을 먼저 하면 무엇이 달라질까?

질문을 바로 답변 모델에 보내면 현재 수업 문서의 구체적인 내용이 입력에 없을 수 있다. RAG는 먼저 관련 자료를 검색하고 그 내용을 질문과 함께 제공해 답변에 참고하도록 한다. 검색기를 쓰는 단계와 문장을 생성하는 단계가 따로 있다. 임베딩 숫자가 바로 답변 문자열로 변하는 단일 함수가 아니다.

예를 들어 질문이 “이 노트북의 메모리는?”이고 검색 문서에 “RAM 16GB”가 있다면, 문맥에 그 글을 넣고 이를 근거로 답하도록 요청할 수 있다. 하지만 검색이 다른 상품을 찾았거나 저장 본문이 잘못됐거나 모델이 지시를 어기면 답도 틀릴 수 있다. RAG라는 이름 자체가 사실성 검증을 보장하지 않는다.

| 단계 | 들어가는 것 | 나오는 것 |
| --- | --- | --- |
| 검색 | question | document·score 결과 목록 |
| 문맥 구성 | ID·청크·제목·분류·본문 | context 문자열 |
| prompt 구성 | 질문·문맥·답변 규칙 | 모델에 보낼 입력 |
| 생성 요청 | prompt | 서비스 응답 객체 |
| 반환 | 응답에서 꺼낸 텍스트 | 호출자가 받는 answer |

원본은 “문맥에 없으면 모른다고 하라”는 규칙을 prompt 문자열에 넣는다. 이는 모델에게 전달하는 요청이다. 실제 검색이 비었는지 검사해 호출을 막거나 답에 근거가 있는지 프로그램으로 검증하는 구현은 원본에 없다. 이 차이는 현재 코드의 한계를 이해하기 위한 본문 설명이다.

### 이름보다 실제 호출을 읽는다

내 함수 이름은 ask_gemini지만 활성 줄은 gpt.responses.create다. 강사님은 gemini.models.generate_content다. 응답의 텍스트를 꺼내는 속성도 내 코드는 output_text, 강사님은 text다. 함수의 별칭이 서비스 종류를 자동으로 정하지 않는다. 이 교재에서는 해당 줄을 수업 기록으로 보존하며 최신 모델로 몰래 바꾸지 않는다.

OpenAI 공식 문서는 SDK의 output_text가 텍스트 출력을 모아 꺼내는 편의 속성임을 설명한다. 원본에 적힌 gpt-4.1-mini의 지원 상태·접속 가능 여부는 서비스와 시점에 따라 별도 확인해야 한다. 현재 공식 모델 페이지의 폐기 예정 표시도 원본의 학습 당시 코드와 구별해 읽는다. 여기서는 외부 서비스에 요청하지 않았다.

> 📚 **출처 · 본문 설명 확인:** [OpenAI Responses Python 참조](https://developers.openai.com/api/reference/python/resources/responses/methods/create) · [원본 모델의 공식 페이지](https://developers.openai.com/api/docs/models/gpt-4.1-mini) · [Gemini 텍스트 생성](https://ai.google.dev/gemini-api/docs/text-generation). 검색→문맥→요청 표는 실제 원본을 풀이한 새 설명이다. 배운 의미 확인 근거다. 아래 표·전체 예제·풀이를 외부 문장 그대로 옮기지 않았다. 확인일: 2026-10-30.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 필요한 파일 전체.** 같은 장의 폴더 구조를 유지한다. Python만 사용한다. 아래 두 파일을 같은 폴더에 저장하고 `python example.py`를 실행한다. hybrid와 ask_model은 고정값을 주는 대역이다. 실제 검색·AI 추론·사실성 검증을 흉내 낸 성공 예제가 아니라 함수 사이에 전달되는 문자열과 호출 여부를 확인하는 예제다.



**[rag_tools.py](실습/책형_복습/05_RAG_질문응답/rag_tools.py) — 새 예제 전체 파일**

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

**[example.py](실습/책형_복습/05_RAG_질문응답/example.py) — 새 예제 전체 파일**

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

search와 generate는 전달받은 함수다. 실제 검색·모델을 호출하지 않고 고정 함수를 넣어 경계를 확인했다. build_context가 결과를 문자열로 만들고 ask_rag가 질문과 규칙을 붙여 generate에 넘긴다. 빈 결과 분기는 원본에 없는 새 개선안이며 그 경우 생성 대역을 호출하지 않는다. 고정 응답이 16GB라고 말한 것은 AI가 자료를 이해했다는 증거가 아니다. calls에 들어간 입력 문자열을 확인한 결과다.

**실행 결과:**

```text
고정 응답: RAM은 16GB입니다.
질문 전달: True
본문 전달: True
제공된 문서에서 확인할 수 없습니다.
생성 대역 호출 수: 1
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

### 내 코드 — 원본

출처: `D:/workspace/workspace_python/07_elastic/router/embedding_router.py` 470–490행 · **원본 발췌**

```python
# 정해진 범위에서 말하는 것이 'RAG' : Retrieval-Augmented Generation
# LLM이 답변을 만들기 전에 외부 DB나 문서에서 관련 정보를 먼저 검색 후 이를 바탕으로 정확한 답변 생성
def ask_rag(question): 
    # hybrid 검색
    results = hybrid(question)['results']

    # 검색 결과를 gemini 용으로 가공
    contexts = []
    for idx, result in enumerate(results) :
        print(result['document'])
        contexts.append(f'''
            [검색 결과 : {idx}]
            문서ID : {result['document']['id']}
            청크번호 : {result['document']['chunk_index']}
            제목 : {result['document']['title']}
            카테고리 : {result['document']['category']}
            내용 : {result['document']['content']}
        ''')

    # 리스트를 string으로 변환
    context =  "\n-------\n".join(contexts)
```

**발췌 바로 풀이:** 활성 ask_rag는 hybrid의 results를 사용한다. 각 결과의 document 안에 id·chunk_index·title·category·content가 있어야 문자열 구성이 가능하다. 저장한 content가 실제 청크인지 앞 장의 적재까지 확인해야 한다. 검색 결과 0부터의 번호와 원본 청크 번호는 다른 값이다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/07_elastic/router/embedding_router.py` 492–513행 · **원본 발췌**

```python
    prompt = f'''
        너는 문서 기반 지식 검색 도우미야.

        아래의 **context**에 포함된 내용만으로 질문에 답변해야만 해.

        ** 규칙 :    
        1. 절대 추론이나 다른 내용을 담으면 안 돼.
        2. 내용에 없는 질문이라면 "제공된 문서에서 확인할 수 없습니다." 라고 답변해줘.
        3. 한국어로 답변해줘.
        4. 불필요하게 긴 설명은 하지 말아줘.
        5. 답변에 대한 근거를 자연스럽게 설명해줘.

        ** 질문 : {question}

        ** context : {context}
    '''.strip()
    print('prompt : ', prompt)

    answer = ask_gemini(prompt)
    print('answer : ', answer)

    return answer
```

**발췌 바로 풀이:** 규칙·질문·문맥을 하나의 prompt로 묶고 ask_gemini에 전달한 반환을 answer로 받는다. print는 기록이고 return이 호출자에게 답을 돌려주는 단계다. 모델이 지시를 반드시 지켰는지 검사하는 코드는 없다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/07_elastic/router/embedding_router.py` 523–530행 · **원본 발췌**

```python
def ask_gemini(prompt) :

    response = gpt.responses.create(
        model='gpt-4.1-mini',
        input=prompt
    )

    return response.output_text
```

**발췌 바로 풀이:** 함수 이름과 달리 실제 활성 코드는 OpenAI Responses 호출이다. model은 원본 gpt-4.1-mini, input은 prompt이며 반환 텍스트는 response.output_text다. 주석의 Gemini 버전과 활성 줄을 섞어 서비스 종류를 설명하지 않는다.

hybrid는 직접 함수 호출로 실행된다. ask_rag 안에서 별도의 HTTP 검색 주소로 다시 요청한 것이 아니다. 반환된 문서 목록의 여러 항목을 join으로 이어 context 하나를 만든다. 검색 본문이 전체 문서라면 청크별로 비슷한 긴 본문이 반복될 수 있다. 빈 결과여도 원본은 빈 context의 prompt를 만들어 모델에 전달한다.

<a id="connections"></a>

## 5. import·함수·입력·출력이 연결되는 흐름

`질문 → hybrid(question) → 결과 document 목록 → contexts 리스트 → join으로 context 문자열 → prompt 문자열 → ask_gemini(prompt) → 실제 서비스 응답의 텍스트 → answer 반환`이다. 호출되는 hybrid 전체 흐름은 04장, formatter 정의는 02장에 있다. 새 예제의 rag_tools와 고정 함수는 이 문서에 모두 제공했다. import로 불러온 사용자 함수가 숨겨져 있지 않다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 질문만 보내지 않고 검색 자료의 ID·청크·본문을 함께 모았다. **아쉬운 점:** ask_gemini 이름과 실제 서비스가 다르고 빈 검색·근거 검증 분기가 없다. 긴 문맥을 그대로 출력해 기록이 과해질 수도 있다. **개선:** 역할 이름 ask_model처럼 실제 목적을 드러내고 빈 결과 처리·추적 가능한 출처를 먼저 설계한다. 새 예제의 빈 검색 차단은 명시한 개선이며 당시 구현으로 바꿔 인용하지 않는다.

원본 오류·수업용 단순화·목적에 따른 설계를 나눈다. 새 개선안은 당시 내 코드나 D 드라이브 수정본이 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교

출처: `D:/workspace_teacher/workspace_python/07_elastic/router/embedding_router.py` 538–545행 · **원본 발췌**

```python
def ask_gemini(prompt) :

    response = gemini.models.generate_content(
        model='gemini-3.8-flash',
        contents=prompt
    )
    print('ask_gemini : ', response)
    return response.text
```

강사님 인용은 Gemini 생성 호출과 response.text 반환을 보여 주기 위해서만 남겼다. 내 활성 OpenAI 호출과 어떤 응답 속성이 다른지 비교하는 데 필요하다. 질문·문맥을 묶는 거의 같은 prompt는 중복 인용하지 않는다. 어느 서비스가 답을 더 잘했는지 비교 실행한 근거는 없다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 새 호출 | 검색 결과 | 생성 호출 | 최종 결과 |
| --- | --- | --- | --- |
|메모리는? | 고정 문서 1개 | 1회 | 고정 응답 |
|무게는? | 없음 | 생략 | 새 코드의 없음 안내 |
|원본 빈 검색 | 없음 | 그대로 호출 | 실제 결과 미확인 |

| 한 가지만 변경 | 확인 |
| --- | --- |
|고정 본문을 32GB로 | 전달 prompt는 바뀌지만 고정 응답은 그대로·대역의 한계 |
|검색 결과를 빈 목록으로 | 새 코드에서 생성 미호출 |
|필수 content 키 제거 | 문자열 구성에서 오류 |
|모델 대역을 예외 발생 함수로 | 현재 예제는 호출 실패를 바깥으로 전달 |

답이 이상하면 모델부터 바꾸기 전에 검색 결과·본문·문맥·질문 순서로 확인한다. KeyError는 document 구조와 필드를 본다. 외부 서비스 오류는 응답 객체를 받기 전 단계이므로 output_text 접근과 구별한다. 함수가 다른 서비스를 부르면 이름이 아니라 활성 호출을 따라간다.

**확인 범위:** 새 예제는 임시 폴더에서 Python 처리·요청 모양·고정 응답 가공을 확인한다. Elasticsearch나 AI 서비스의 실제 연결·적재·검색·임베딩·답변 성공을 재현한 것은 아니다. 원본 함수의 별도 검사도 외부 호출을 기록 대역으로 바꾼 범위이며 원본 파일과 패키지는 수정하지 않는다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 답변과 출처를 함께 반환하는 스키마·문맥의 악의적 지시를 다루는 방법·근거 자동 검사·대화 이력·문맥 길이 예산·검색 품질 평가는 추가 학습이다. 원본 prompt의 규칙은 학습 자료 속 문자열이며 이 교재를 작성하는 도우미에게 내린 사용자 지시가 아니다.

확인한 라이브러리 의미와 수업 밖 확장을 구분한다. 위 출처는 본문의 설명 근거이며 TIP에 적힌 새 주제를 이미 배운 것으로 간주하지 않는다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. 검색 결과가 prompt에 들어갔다고 사실성이 보장되는가?
2. 내 ask_gemini는 실제 어느 API를 호출하는가?
3. 새 예제에서 빈 검색의 생성 호출 수가 늘지 않는 이유는?

<details>
<summary>풀이 — 먼저 결과와 이유를 적은 뒤 펼치기</summary>

1. 아니다. 검색과 저장, 모델의 지시 준수·근거 확인을 따로 봐야 한다.
2. 원본 활성 줄은 OpenAI Responses이며 output_text를 반환한다.
3. 결과가 없으면 안내를 먼저 return하는 새 개선안 때문이다.

</details>

| 빠른 찾기 | 뜻 |
| --- | --- |
|RAG | 검색 자료를 답변 입력에 제공 |
|context | 검색 결과를 묶은 문자열 |
|prompt | 규칙·질문·문맥 입력 |
|답변 규칙 | 요청이지 자동 검증 아님 |
|고정 대역 | 전달 흐름 검사·AI 성능 검증 아님 |

[장별 연습문제](실습/연습문제/05_RAG_질문응답_연습문제.md) · [다음: 실무 스타일](실무_코딩스타일.md)
