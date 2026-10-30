# 21. 외부 AI 요청 — 요청 본문·응답 글·대화 배열의 연결

[JavaScript 목차](README.md) · [읽기 안내](00_JavaScript_V3_동작_백과_읽기법.md)

AI 서비스 예제에서도 핵심은 앞에서 배운 입력값·객체·JSON·비동기 처리다. 답변을 화면에 보여 주는 것과 다음 요청의 대화 기록에 넣는 것은 다른 작업이다. 이 두 경로를 구분하면 원본의 개선점이 보인다.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

POST의 headers·body와 JSON 문자열을 설명한다. 중첩 응답에서 답변을 읽고 배열에 기록하는 흐름, 부모 내용 재대입이 자식에 미치는 결과, 새로고침과 메모리 기록의 관계를 추적한다.

입력·현재 상태·실행 순서·결과를 분리해 설명한다. 실제 수업 원본은 아래에 표시하고, 원본에 없는 선택 학습은 9절 TIP에 둔다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

요청 본문은 서비스로 보낼 데이터다. 원본은 contents 배열 안에 대화 항목을 넣고 각 항목의 parts 배열 안에 text를 넣는다. role은 사용자 또는 모델 쪽 항목임을 구분한다. 이 자료구조는 해당 서비스의 형식이며 모든 AI 서비스가 똑같이 요구하는 보편 문법은 아니다.

| 표현 | 역할 | 혼동하지 않을 것 |
| --- | --- | --- |
| list | contents를 가진 객체 | 그 자체가 배열은 아님 |
| list.contents | 대화 항목 배열 | push를 적용하는 대상 |
| JSON.stringify(list) | 보낼 JSON 문자열 | 원본 배열 자체를 문자열로 바꾸지 않음 |
| headers | 본문 형식·요청 정보 | 화면 입력값과 다름 |
| body | 실제로 보낼 본문 | 원본에서는 JSON 문자열 |

Content-Type: application/json은 본문이 JSON 형식임을 알린다. JSON으로 보내면 안 된다는 내 주석은 “객체를 그대로 이 예제의 body로 넘기지 말고 JSON 문자열로 표현한다”로 고친다. JSON 형식 자체를 금지하는 뜻이 아니다. JavaScript의 fetch headers는 이 수업 원본에 있으므로 본문이다. 배우지 않았다고 확인한 FastAPI request.headers와는 별도 학습 근거다.

> 📚 **출처 · 본문 설명 확인:** [Google GenerateContent 공식 요청·응답 구조](https://ai.google.dev/api/generate-content), [MDN Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch). 배운 기능의 뜻을 확인한 근거다. 예제·표·풀이 흐름은 수업 코드를 바탕으로 새로 작성했으며 외부 문장을 직접 인용하지 않았다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 스크립트.** [HTML 실행 파일](실습/책형_복습/21_JavaScript_외부AI_API요청과_대화기록.html)과 같은 폴더의 [JS 파일](실습/책형_복습/21_JavaScript_외부AI_API요청과_대화기록.js)을 함께 내려받는다. HTML을 브라우저로 열고 Console에서 결과를 확인한다. script는 필요한 HTML 뒤에 연결한다. 콘솔 출력은 페이지 본문에 자동으로 쓰이지 않는다.

**먼저 준비할 HTML · body 안:**

```html
    <label>질문 <input id="prompt"></label>
    <button id="add" type="button">가상 답변으로 기록 연습</button>
    <div id="result"></div>
```

```javascript
const list = { contents: [] };
function appendLine(role, text) {
    const line = document.createElement('p');
    line.textContent = role + ': ' + text;
    document.getElementById('result').append(line);
}
document.getElementById('add').addEventListener('click', function () {
    const prompt = document.getElementById('prompt').value;
    list.contents.push({ role: 'user', parts: [{ text: prompt }] });
    const body = JSON.stringify(list);
    console.log('요청 직전 항목', list.contents.length);
    console.log(typeof body);
    // 실제 AI 응답이 아닌, 구조 풀이용 가상 응답
    const result = { candidates: [{ content: { parts: [{ text: '연습 답변' }] } }] };
    const answer = result.candidates[0].content.parts[0].text;
    list.contents.push({ role: 'model', parts: [{ text: answer }] });
    appendLine('user', prompt);
    appendLine('model', answer);
    console.log('답변 기록 뒤 항목', list.contents.length);
});
```

안녕을 넣고 누른 뒤 다음 질문으로 바꿔 다시 누른다. 첫 질문을 넣으면 요청 본문을 만드는 순간 항목 수는 1, 가상 모델 답변을 기록하면 2다. 다음 클릭은 기존 두 항목 뒤에 사용자 글을 추가하여 3개를 본문으로 만들고 답변 뒤에는 4개다. appendLine의 정의는 role·text를 받아 p를 만들고 글자로 넣어 결과 영역 끝에 붙인다. 이 예제는 네트워크 요청이 전혀 없으며 가상 응답 구조를 읽는 연습이다. 실제 API 성공·AI 생성·대화 기억 기능으로 소개하지 않는다.

**예상 출력 또는 관찰:**

```text
요청 직전 항목 1
string
답변 기록 뒤 항목 2
요청 직전 항목 3
string
답변 기록 뒤 항목 4
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본의 일부다. 원본에 의존하는 앞 선언·HTML·함수는 다음 절의 연결까지 읽는다. 주석의 잘못된 표현도 원문대로 보존하고 설명에서 교정한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/21_gemini.html` 17–49행

```javascript
        const ask = document.querySelector('#ask')
        ask.addEventListener('click', function() {
            const key = ''
            const prompt = document.querySelector('#prompt').value
            const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent'
        
            const data = {
                contents: [{
                    parts: [{
                        text: prompt
                    }]
                }]
            }

            fetch(url, {
                method: 'POST',
                headers: {
                    'x-goog-api-key': key,
                    'Content-Type': 'application/json'
                },
                // JSON으로 날아가면 안되기 때문에, 문자열로 변경해서 전달
                body: JSON.stringify(data)
            }).then( function(response){
                return response.json()
            }).then( function(result){
                console.log(result['candidates']['0']['content']['parts']['0']['text'])
                const divAdd = document.createElement('div')
                const askResult = document.querySelector('#askResult')
                askResult.append(divAdd)
                askResult.innerText = result['candidates']['0']['content']['parts']['0']['text']
            }).catch( function(error){
                console.error('요청 중 에러', error)
            })
```

**발췌 바로 풀이:** `#prompt.value`를 읽어 `contents → parts → text`에 넣는다. `fetch`에는 `POST`, JSON 형식 헤더, `JSON.stringify(data)`로 만든 문자열 본문을 전달한다. 응답을 `response.json()`으로 읽고 다음 `then`에서 사용한다. 내 코드는 후보의 텍스트를 찾아 화면에 표시하려 했다. 그러나 `askResult.append(divAdd)` 직후 `askResult.innerText = ...`가 부모의 내용을 다시 써서 방금 만든 `divAdd`가 사라진다. 한 줄 결과만 표시하려면 빈 `div`를 만들 필요가 없다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/21_gemini.html` 7–10행

```html
<script>
    const list = {
        contents: []
    }
```

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/21_gemini.html` 54–97행

```javascript
        const ask2 = document.querySelector('#ask2')
        ask2.addEventListener('click', function() {
            const key = ''
            const prompt = document.querySelector('#prompt').value
            const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent'
        
            // push로 list라는 배열에 내가 보낸 것, gemini가 보내준 것을
            // json으로 저장해서 gemini가 기억을 하는 것 처럼 구현할 수 있음
            list.contents.push({
                role: 'user',
                parts: [{
                    text: prompt
                }]
            })

            fetch(url, {
                method: 'POST',
                headers: {
                    'x-goog-api-key': key,
                    'Content-Type': 'application/json'
                },
                // JSON으로 날아가면 안되기 때문에, 문자열로 변경해서 전달
                body: JSON.stringify(list)
            }).then( function(response){
                return response.json()
            }).then( function(result){
                console.log(result['candidates']['0']['content']['parts']['0']['text'])
                
                list.contents.push({
                    role: 'model',
                    parts: [{
                        text: JSON.stringify(result)
                    }]
                })
                
                const divAdd = document.createElement('div')
                const askResult = document.querySelector('#askResult')
                askResult.append(divAdd)
                askResult.innerText = result['candidates']['0']['content']['parts']['0']['text']
            }).catch( function(error){
                console.error('요청 중 에러', error)
            })

        })
```

**발췌 바로 풀이:** `list.contents`는 **이 페이지가 열려 있는 동안** 보낼 대화 항목을 배열에 모은다. `ask2`를 누르면 사용자 글을 `push`하고 전체 `list`를 요청한다. 응답 뒤에는 모델 항목도 `push`한다. 브라우저 저장소나 서버에 기록하는 코드는 없어서 새로고침하면 이 배열은 처음부터 시작한다.

내 첫 버튼은 prompt를 객체에 넣어 POST하고 response.json 뒤 candidates[0].content.parts[0].text를 읽는다. 그 경로의 문자열을 화면에 넣지만 divAdd를 append한 직후 부모 askResult.innerText를 대입하여 방금 붙인 자식을 다시 없앤다. 둘째 버튼은 list.contents에 사용자 항목을 넣고 전체 list를 보낸다. 결과 뒤 모델 항목에도 push하지만 text에는 답변만이 아니라 응답 객체 전체를 JSON.stringify한 문자열을 넣는다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

load에서 버튼 연결 → 클릭 때 prompt.value 읽기 → 사용자 항목 push → JSON.stringify → fetch의 POST·headers·body → 첫 then에서 JSON 읽기 → 다음 then에서 답변 경로 읽기 → 모델 항목 push와 DOM 표시 순서다. list는 클릭 콜백 바깥에 있어 다음 클릭에도 남는다. 반면 새로고침하면 스크립트를 다시 실행하여 contents는 빈 배열로 시작한다. 브라우저 저장소나 서버에 대화 기록을 저장한 코드는 없다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 내 코드는 중첩 응답에서 답변을 찾아 화면까지 연결하고 사용자·모델 항목을 구분했다. **실제 DOM 문제:** 부모 innerText 대입은 자식을 유지하며 글자만 덧붙이는 작업이 아니다. 한 결과만 표시할지 기록을 쌓을지 정한 뒤 둘 중 한 방식을 택한다. **공통 개선:** 모델 기록에는 화면에서 읽은 답변 문자열을 넣는 편이 대화 의도에 맞다. 응답 전체를 stringify한 것을 사람이 읽은 답변과 같은 것으로 다루지 않는다. **수업용 한계:** 빈 키·미검증 응답 구조이므로 실행 성공을 보장하지 않는다.

개선안은 원본을 수정한 결과가 아니다. 실제 오류, 수업용 단순화, 목적에 따른 선택을 구별해 판단한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



강사님과 내 요청 구조는 같아서 중복 인용하지 않는다. 양쪽 모델 기록의 JSON.stringify(result)도 같은 개선 대상이다. 내 화면 추출 코드는 답변만 저장하는 방향의 단서가 된다. 버튼 type=buttn은 유효한 button으로 고치는 것이 맞다. 현재 폼 밖 배치에서 이 오타가 모든 요청 실패의 원인이라고 단정하지는 않는다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 순간 | contents 개수 | 담긴 것 |
| --- | --- | --- |
| 처음 | 0 | 빈 배열 |
| 첫 질문 직후 | 1 | user |
| 첫 답변 기록 뒤 | 2 | user, model |
| 둘째 질문 직후 | 3 | 이전 두 항목, 새 user |
| 둘째 답변 뒤 | 4 | 이전 세 항목, 새 model |
| 새로고침 | 0 | 초기화 |

원본의 모델명 문자열은 당시 파일의 값으로 보존한다. 현재 지원 모델이나 키를 확인한 실행 예제로 간주하지 않는다. 실제 응답에는 후보나 해당 경로가 없을 수도 있으므로 경로가 항상 존재한다고 외우지 않는다. 이번 자동 검수는 가상 값과 DOM 기록만 확인했다.

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| list를 클릭 함수 안으로 이동 | 클릭마다 이전 기록 사라짐 | 매번 새 객체 생성 |
| answer 대신 JSON.stringify(result) 기록 | 응답 구조 전체가 text에 들어감 | 답변 글과 응답 객체 차이 |
| appendLine 대신 부모 textContent 대입 | 이전 자식 기록이 사라짐 | 부모 내용 교체 |
| 새로고침 | 기록 초기화 | 별도 저장 없음 |

기록이 한 줄만 남으면 부모 전체 내용을 다시 대입하는지 본다. 다음 요청 항목이 이상하면 model의 text에 무엇을 넣었는지 확인한다. undefined 경로 오류는 실제 응답 구조를 먼저 확인한다. catch가 있다고 모든 HTTP 오류를 자동 실패로 판단하는 것은 아니므로 성공 상태 확인은 별도 확장으로 둔다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** API 키를 서버에서 관리하는 구성, 상태 코드와 응답 형태 검사, 중복 요청·실패한 사용자 항목 복구, 영구 대화 저장은 추가 학습이다. 이 원본은 요청 형식과 then 흐름을 연습한 자료다.



이 절의 확장은 기본 문제의 필수 조건이 아니다. 📚 출처가 있다는 것과 수업 밖 기능이라는 것은 다른 구분이다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. list와 list.contents 중 배열은 어느 쪽인가?
2. 둘째 질문 직후 본문에는 항목 몇 개가 있는가?
3. 응답 전체 문자열과 답변 문자열은 같은가?
4. 화면에 append한 뒤 부모 내용을 대입하면 자식은 유지되는가?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

contents가 배열이다. 가상 예제에서는 3개다. 응답 전체는 메타 구조까지 담아 답변만과 다르다. 부모 내용을 교체하면 기존 자식은 유지되지 않는다.

</details>

| 단계 | 읽을 대상 |
| --- | --- |
| 요청 | contents·parts·text |
| 응답 | candidates 안의 실제 글 |
| 기록 | model의 text |
| 화면 | 자식 추가와 부모 교체 구분 |

[장별 연습문제](실습/연습문제/21_JavaScript_외부AI_API요청과_대화기록_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [웹훅 POST](22_JavaScript_웹훅_POST요청.md)다.

<!-- 이전 색인 이동 주소 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>

[이 장의 목차](#chapter-toc)에서 현재 설명을 찾는다.
