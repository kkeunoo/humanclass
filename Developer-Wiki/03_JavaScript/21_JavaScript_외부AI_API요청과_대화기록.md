# 21. 외부 AI API 요청과 대화 기록

[JavaScript 목차](README.md) · [이전: 날씨 응답](20-02_JavaScript_날씨응답_필터와_표시.md)

양쪽 `21_gemini.html`은 앞 장의 `fetch`를 이용해 **입력 글을 요청 본문에 넣어 보내고 결과를 읽는 구조**를 연습한다. 원본의 API 키는 빈 문자열이고, 실제 서비스 응답을 검증한 파일은 아니다. URL의 모델 이름이나 현재 사용 가능 여부를 학습 결론으로 삼지 않는다.

<!-- chapter-toc -->

- [1. 한 번 질문 보내기](21_JavaScript_외부AI_API요청과_대화기록.md#section-1)
- [2. 여러 번 질문한 내용 보관하기](21_JavaScript_외부AI_API요청과_대화기록.md#section-2)
- [3. 결과를 읽을 때 구분할 것](21_JavaScript_외부AI_API요청과_대화기록.md#section-3)
- [직접 확인할 질문](21_JavaScript_외부AI_API요청과_대화기록.md#section-4)
- [추가로 알면 좋은 것](21_JavaScript_외부AI_API요청과_대화기록.md#section-5)

<a id="section-1"></a>

## 1. 한 번 질문 보내기

### 강사님 코드

출처: `teacher/workspace_html/javascript/21_gemini.html` 17~45행 · **원본 발췌**

```javascript
        const ask = document.querySelector('#ask')
        ask.addEventListener('click', function(){
            const key = ''
            const prompt = document.querySelector('#prompt').value
            const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent'

            const data = {
                contents: [{
                    parts:[{
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
                body: JSON.stringify(data)
            }).then( function(response){
                return response.json()
            }).then( function(result){
                console.log(result)
            }).catch( function(error){
                console.error('요청 중 에러', error)
            })
        })
```

### 내 코드

출처: `me/workspace_html/javascript/21_gemini.html` 17~49행 · **원본 발췌**

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

`#prompt.value`를 읽어 `contents → parts → text`에 넣는다. `fetch`에는 `POST`, JSON 형식 헤더, `JSON.stringify(data)`로 만든 문자열 본문을 전달한다. 응답을 `response.json()`으로 읽고 다음 `then`에서 사용한다. 내 코드는 후보의 텍스트를 찾아 화면에 표시하려 했다. 그러나 `askResult.append(divAdd)` 직후 `askResult.innerText = ...`가 부모의 내용을 다시 써서 방금 만든 `divAdd`가 사라진다. 한 줄 결과만 표시하려면 빈 `div`를 만들 필요가 없다.

<a id="section-2"></a>

## 2. 여러 번 질문한 내용 보관하기

### 강사님 코드

출처: `teacher/workspace_html/javascript/21_gemini.html` 7~10행 · **원본 발췌**

```javascript
<script>
    const list = {
        contents: []
    }
```

출처: `teacher/workspace_html/javascript/21_gemini.html` 46~80행 · **원본 발췌**

```javascript
        const ask2 = document.querySelector('#ask2')
        ask2.addEventListener('click', function(){
            const key = ''
            const prompt = document.querySelector('#prompt').value
            const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent'

            list.contents.push({
                role: 'user',
                parts:[{
                    text: prompt
                }]
            })

            fetch(url, {
                method: 'POST',
                headers: {
                    'x-goog-api-key': key,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(list)
            }).then( function(response){
                return response.json()
            }).then( function(result){
                console.log(result)

                list.contents.push({
                    role: 'model',
                    parts:[{
                        text: JSON.stringify(result)
                    }]
                })
            }).catch( function(error){
                console.error('요청 중 에러', error)
            })
        })
```

### 내 코드

출처: `me/workspace_html/javascript/21_gemini.html` 7~10행 · **원본 발췌**

```javascript
<script>
    const list = {
        contents: []
    }
```

출처: `me/workspace_html/javascript/21_gemini.html` 54~97행 · **원본 발췌**

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

`list.contents`는 **이 페이지가 열려 있는 동안** 보낼 대화 항목을 배열에 모은다. `ask2`를 누르면 사용자 글을 `push`하고 전체 `list`를 요청한다. 응답 뒤에는 모델 항목도 `push`한다. 브라우저 저장소나 서버에 기록하는 코드는 없어서 새로고침하면 이 배열은 처음부터 시작한다.

양쪽 코드 모두 모델 항목의 `text`에 **응답 전체를 `JSON.stringify(result)`로 넣는다**. 다음 요청에서 사람이 읽을 답변만 보내는 구조와 다르며, 원본 의도인 자연스러운 대화 기록과 어긋날 수 있다. 내 코드가 따로 화면에 읽어낸 `result['candidates']['0']['content']['parts']['0']['text']`가 있다면 그 글을 모델 항목의 `text`로 저장하는 편이 의도에 맞다. 다만 응답에 해당 경로가 없을 수도 있으므로 실제 응답을 확인해야 한다.

<a id="section-3"></a>

## 3. 결과를 읽을 때 구분할 것

- **요청을 만드는 단계:** 원본만으로 확인 가능하다.
- **외부 서비스가 성공 응답을 주는지:** 키가 빈 문자열이므로 확인되지 않았다.
- **`catch`의 범위:** 네트워크 거절이나 `then` 안 오류는 받지만, HTTP 오류 응답을 JSON으로 읽은 뒤 성공처럼 처리할 수도 있다. 현재 코드는 응답 상태를 검사하지 않는다.

내 HTML의 버튼은 `type="buttn"`으로 적혀 있다. 유효한 값인 `button`으로 고치는 편이 좋다. 현재는 폼 밖에 있어서 클릭 리스너 학습을 막는 핵심 원인은 아니다.

<a id="section-4"></a>

## 직접 확인할 질문

1. 첫 버튼은 어느 객체를 보내고, 두 번째 버튼은 어느 객체를 보낼까?
2. `list.contents`는 새로고침 뒤에도 남을까?
3. 응답 전체를 다음 대화의 `text`로 넣으면 어떤 글이 전달될까?

<a id="section-5"></a>

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/21_JavaScript_외부AI_API요청과_대화기록_연습문제.md)

## 추가로 알면 좋은 것

외부 API를 실제 서비스에 붙일 때는 키를 브라우저 문서에 직접 넣지 않고 서버 쪽에서 관리하는 구성을 검토한다. 이 수업 원본은 요청 형식과 Promise 흐름을 연습하는 수준이다.

