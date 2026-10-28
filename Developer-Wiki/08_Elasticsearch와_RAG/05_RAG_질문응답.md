# 05. 검색한 문맥으로 질문에 답하기

[이전: 하이브리드 검색](04_벡터와_하이브리드검색.md) · [목차](README.md) · [Developer-Wiki 첫 화면](../README.md)

RAG의 이 실습은 **질문으로 검색 → 검색 결과에서 문맥 작성 → 그 문맥과 질문을 AI에 전달 → 답변 반환** 순서다. 외부 모델이 반드시 문맥만 따른다고 보장하는 검증 기능은 코드에 없다.

## 먼저: RAG는 어디에 검색을 끼워 넣나?

RAG는 **검색으로 찾은 자료를 답변 생성에 함께 제공**하는 흐름이다. 이 장의 함수는 질문을 바로 답변 모델에 보내지 않고, 04장의 `hybrid()`로 관련 문서를 먼저 찾는다.

| 단계 | 이 수업의 함수 | 다음 단계로 넘어가는 값 |
| --- | --- | --- |
| 1. 검색 | `hybrid(question)` | 결과 문서 목록 |
| 2. 문맥 만들기 | 결과의 ID·제목·분류·내용을 문자열로 묶기 | `context` |
| 3. 질문과 문맥 전달 | `ask_gemini(prompt)` | 외부 모델의 답변 문자열 |

이 표는 **실제 코드 흐름을 새로 요약한 것**이다. 함수 이름 `ask_gemini`가 곧 호출 서비스라는 뜻은 아니다. 아래 원본을 비교하면 강사님은 Gemini, 나는 GPT 호출을 사용한다.

## 질문으로 문서를 먼저 검색

검색 결과 한 건을 `contexts`의 한 항목으로 만들고, 여러 항목을 구분선으로 이어 `context` 문자열을 만든다. 문맥에 넣은 `content`가 청크인지 원래 전체 본문인지는 03장의 적재 방식을 함께 봐야 한다.

### 강사님 코드 — 원본 발췌

출처: `D:/workspace_teacher/workspace_python/07_elastic/router/embedding_router.py` 492–511행

```python
@router.get('/embed/ask')
def ask_rag(question):
    # 하이브리드 검색
    results = hybrid(question)['results']

    # 검색 결과를 gemini 용으로 가공
    contexts = []
    for idx, result in enumerate(results) :
        print('>>>>>>>>>>', result)
        contexts.append(f'''
            [검색 결과 : {idx}]
            문서ID : {result['document']['id']}
            청크번호 : {result['document']['chunk_index']}
            제목 : {result['document']['title']}
            카테고리 : {result['document']['category']}
            내용 : {result['document']['content']}
        ''')

    # 리스트를 string으로 변환
    context = "\n-------\n".join(contexts)
```

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/07_elastic/router/embedding_router.py` 470–490행

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

`hybrid(question)['results']`가 반환한 각 결과에서 문서 ID, 청크번호, 제목, 카테고리, 내용을 `contexts`에 넣는다. 이 결과의 `document['content']`가 실제 청크 내용인지 확인해야 한다. 03장에서 본 것처럼 적재 코드는 청크별 임베딩을 만들지만 원본 본문을 `_source`에 계속 둘 수 있다.

## 문맥과 질문을 묶어 답변 요청

프롬프트에는 **역할, 답변 규칙, 질문, 검색 문맥**이 함께 들어간다. ‘문서에 없으면 모른다고 답하라’는 규칙은 답변 모델에 보내는 지시다. 검색 결과가 없거나 모델이 규칙을 어겼을 때 자동으로 검사하는 코드는 아래 발췌에 없다.

### 강사님 코드 — 원본 발췌

출처: `D:/workspace_teacher/workspace_python/07_elastic/router/embedding_router.py` 513–534행

```python
    prompt = f'''
        너는 문서 기반 지식 검색 도우미야.

        아래의 **context**에 포함된 내용만으로 질문에 답변해야만해.

        ** 규칙 :
        1 절대 추론이나 다른 내용을 담으면 안돼.
        2 내용에 없는 질문이라면 "문서에서 확인할 수 없는 질문입니다"라고 답변해줘
        3 한국어로 답변해줘
        4 불필요하게 긴 설명을 하지 말아줘
        5 답변에 대한 근거를 자연스럽게 설명해줘

        ** 질문 : {question}

        ** context : {context}
    '''.strip()
    print('prompt : ', prompt)

    answer = ask_gemini(prompt)
    print('answer : ', answer)

    return answer
```

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/07_elastic/router/embedding_router.py` 492–513행

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

프롬프트는 제공된 문맥만 사용하고 없으면 모른다고 답하도록 지시한다. 두 파일의 문구는 조금 다르지만 의도는 같다. 코드에는 검색 결과가 비었을 때 별도 분기, 출처의 자동 검증, 답변의 사실성 검증은 없다. 따라서 이 문구는 **요청**이며 실제 답의 신뢰성을 보장하는 장치는 아니다.

### 강사님 코드 — 원본 발췌

출처: `D:/workspace_teacher/workspace_python/07_elastic/router/embedding_router.py` 538–545행

```python
def ask_gemini(prompt) :

    response = gemini.models.generate_content(
        model='gemini-3.8-flash',
        contents=prompt
    )
    print('ask_gemini : ', response)
    return response.text
```

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/07_elastic/router/embedding_router.py` 523–530행

```python
def ask_gemini(prompt) :

    response = gpt.responses.create(
        model='gpt-4.1-mini',
        input=prompt
    )

    return response.output_text
```

여기에는 눈에 띄는 차이가 있다. 강사님은 `gemini.models.generate_content`를 호출하고 내 현재 실행 코드는 `gpt.responses.create`를 호출한다. 내 파일의 Gemini 버전은 주석 처리돼 있다. 그러므로 함수 이름 `ask_gemini`만 보고 사용 모델을 판단하면 안 된다. 응답을 꺼내는 속성도 강사님은 `response.text`, 나는 `response.output_text`다. **실제 서비스 호출 성공과 모델 응답은 확인하지 않았다.**

## 직접 확인할 질문

1. 질문만 외부 모델에 보내는 것과 검색 문맥을 함께 보내는 것의 차이는?
2. 내 `ask_gemini` 함수의 현재 실행 코드는 어느 서비스를 호출하는가?
3. 청크별 임베딩을 만들었어도 `_source['content']`를 확인해야 하는 이유는?

## 추가로 알면 좋은 것

> 💡 **TIP · 수업 범위 밖:** 답변과 검색 문서의 출처를 함께 돌려주고, 문맥이 없을 때 답을 중단하는 설계는 유용하다. 아직 두 실습 함수에는 적용되지 않았다.

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/05_RAG_질문응답_연습문제.md) → [단원 종합실습](종합실습.md)
