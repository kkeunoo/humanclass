# 20. AJAX와 fetch — 요청한 순간과 데이터를 받은 순간 나누기

[JavaScript 목차](README.md) · [읽기 안내](00_JavaScript_V3_동작_백과_읽기법.md)

요청을 보냈다는 것은 응답이 이미 변수에 들어왔다는 뜻이 아니다. 지금 실행하는 코드와 나중에 실행할 응답 처리 함수를 나눠 읽어야 통신 결과를 제대로 사용할 수 있다. 같은 로컬 JSON을 두 방식으로 읽어 차이를 관찰한다.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

XMLHttpRequest의 생성·준비·전송·응답 처리를 설명한다. fetch의 응답 객체와 본문 읽기를 나누고 then의 return이 다음 단계에 무엇을 전달하는지 추적한다. 동기 예외와 비동기 체인의 오류 처리도 구별한다.

입력·현재 상태·실행 순서·결과를 분리해 설명한다. 실제 수업 원본은 아래에 표시하고, 원본에 없는 선택 학습은 9절 TIP에 둔다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

AJAX는 현재 페이지 전체를 이동하지 않고 데이터를 요청하여 나중에 받은 결과로 화면을 갱신하는 방식이다. XMLHttpRequest와 fetch는 그 요청에 사용하는 API다. JSON은 데이터 표현 형식이지 요청 자체의 이름이 아니다.

| 단계 | XMLHttpRequest | fetch |
| --- | --- | --- |
| 준비 | new와 open | fetch에 주소·옵션 전달 |
| 요청 시작 | send() | fetch() 호출 |
| 응답 처리 연결 | onload 함수 | 첫 then 함수 |
| JSON 읽기 | responseText를 JSON.parse | response.json() |
| 읽은 값 활용 | 콜백 안의 값 | 다음 then의 data |

Promise는 비동기 작업의 완료·실패와 이후 처리를 연결하는 값이다. 지금 당장 완성된 데이터 배열이라고 생각하지 않는다. 첫 then이 받은 response는 응답 객체이고, response.json()도 본문을 읽는 비동기 작업이다. 이를 return해야 다음 then이 그 결과를 기다려 data를 받을 수 있다.

try...catch는 현재 실행 중에 발생한 예외를 잡는다. 원본의 undefined.push는 동기 예외이고 그 아래 fetch와 별도 실험이다. fetch 체인에서 발생한 거절이나 예외는 연결한 catch에서 처리한다. 오류를 잡았다고 실패한 push 작업 자체가 성공으로 바뀐 것은 아니다.

> 📚 **출처 · 본문 설명 확인:** [MDN XMLHttpRequest 사용](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest_API/Using_XMLHttpRequest), [Fetch 사용](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch). 배운 기능의 뜻을 확인한 근거다. 예제·표·풀이 흐름은 수업 코드를 바탕으로 새로 작성했으며 외부 문장을 직접 인용하지 않았다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 스크립트.** [HTML 실행 파일](실습/책형_복습/20_JavaScript_AJAX와_fetch.html)과 같은 폴더의 [JS 파일](실습/책형_복습/20_JavaScript_AJAX와_fetch.js)을 함께 내려받는다. 이 예제는 같은 폴더의 [가상 사용자 JSON](실습/책형_복습/book-users.json)도 필요하다. 파일을 직접 여는 대신 VS Code의 Live Server 등으로 이 폴더를 웹으로 제공한다. Python이 설치되어 있다면 책형_복습 폴더에서 `python -m http.server 8000 --bind 127.0.0.1`을 실행하고 `http://127.0.0.1:8000/`에서 이 장 HTML을 선택한다. 종료는 실행한 터미널에서 Ctrl+C다. 실행 준비용 명령이며 JavaScript 수업 문법으로 분류하지 않는다. script는 필요한 HTML 뒤에 연결한다. 콘솔 출력은 페이지 본문에 자동으로 쓰이지 않는다.

**먼저 준비할 HTML · body 안:**

```html
    <button id="xhr" type="button">XHR로 읽기</button>
    <button id="fetch" type="button">fetch로 읽기</button>
    <p id="result"></p>
```

```javascript
document.getElementById('xhr').addEventListener('click', function () {
    const xhr = new XMLHttpRequest();
    xhr.open('GET', 'book-users.json');
    xhr.onload = function () {
        const users = JSON.parse(xhr.responseText);
        console.log('XHR 응답', users[1].name);
        document.getElementById('result').textContent = users[1].name;
    };
    xhr.send();
    console.log('XHR 요청 뒤');
});
document.getElementById('fetch').addEventListener('click', function () {
    fetch('book-users.json', { method: 'GET' })
        .then(function (response) {
            return response.json();
        })
        .then(function (users) {
            console.log('fetch 응답', users[2].address.geo.lat);
            document.getElementById('result').textContent = users[2].address.geo.lat;
        })
        .catch(function (error) {
            document.getElementById('result').textContent = '읽기 실패';
            console.error(error);
        });
    console.log('fetch 요청 뒤');
});
```

XHR로 읽기를 누르고 응답까지 확인한 다음 fetch로 읽기를 누른다. 각 버튼의 요청 뒤 로그가 먼저 나오고 응답 처리는 나중에 나온다. 가상 JSON의 배열 인덱스 1은 준호, 인덱스 2의 address.geo.lat는 문자열 35.3이다. 외부 사용자 서비스의 현재 데이터가 아니라 함께 제공한 연습 파일의 값이다. 두 버튼을 빠르게 연달아 누르면 요청들 사이의 응답 순서는 이 예시와 달라질 수 있으므로 조작 조건도 함께 지킨다.

**예상 출력 또는 관찰:**

```text
XHR 요청 뒤
XHR 응답 준호
fetch 요청 뒤
fetch 응답 35.3
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본의 일부다. 원본에 의존하는 앞 선언·HTML·함수는 다음 절의 연결까지 읽는다. 주석의 잘못된 표현도 원문대로 보존하고 설명에서 교정한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/asset/js/20_ajax.js` 7–38행

```javascript
    const btn1 = document.querySelector('#btn1')
    btn1.addEventListener('click', function() {

        // AJAX는 4단계로 구성되어 있음(url도 가능하고, 파일도 가능함)
        // 1_ajax 객체 생성 
        const xhr = new XMLHttpRequest()

        // 2_보낼 준비 방식(method), 주소(url)
        xhr.open('GET', 'https://jsonplaceholder.typicode.com/users')

        // 3_보내기
        xhr.send()

        // 4_결과 받기 및 활용, 갔다 오면~이기 때문에 콜백함수 이용
        xhr.onload = function() {
            console.log('다녀왔어')
            console.log( xhr.responseText )

            // 깜짝퀴즈, 두번째 사람의 이름을 출력하기 (Ervin)
            // 세번째 사람의 lat(좌표)를 출력하기
            const xhrData = JSON.parse(xhr.responseText)
            console.log(xhrData)
            // 첫번째 방법
            console.log(xhrData[1]['name'])
            console.log(xhrData[2]['address']['geo']['lat'])
            // 두번째 방법
            console.log(xhrData[1].name)
            console.log(xhrData[2].address.geo.lat)
        
        }

    })
```

**발췌 바로 풀이:** 객체를 만들고 `open('GET', 주소)`로 요청을 준비하고 `send()`로 보낸다. 응답이 오면 `onload`에서 `responseText`를 읽는다. 응답이 JSON 문자열이라는 전제에서 `JSON.parse`로 배열을 만든 뒤 두 번째 사람은 인덱스 `1`, 세 번째 사람은 인덱스 `2`로 접근한다. 내 코드는 대괄호와 점 표기를 둘 다 확인한다. 강사님 주석의 사람 이름·좌표 값은 당시 예시 데이터에 관한 것이므로 항상 고정된 결과라고 외우지 않는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/asset/js/20_ajax.js` 40–58행

```javascript
    const btn2 = document.querySelector('#btn2')
    btn2.addEventListener('click', function() {

        const xhr = new XMLHttpRequest()
    
        // 상대주소로 하지 않아도 갔다 오는 이유는, html에서 자바스크립트를
        // 연결했기 때문에 head영역 자바스크립트 안에 들어갔기 때문에
        // 20_ajax.html의 폴더 경로와 동일함 (주소경로를 참고한다는 말이 더 정확)
        xhr.open('GET', '19_json.html')
        xhr.send()
        
        xhr.onload = function() {
            console.log( xhr.responseText )
        }

        // 아래에 들어가있어도, 비동기기 때문에 값을 받지 않고 로그상 위에 먼저 나오게 됨
        console.log( '['+ xhr.responseText +']' )
        
    })
```

**발췌 바로 풀이:** `19_json.html`은 요청을 시작한 페이지 `20_ajax.html`의 주소를 기준으로 해석되는 상대 경로다. `xhr.responseText`를 `send()` 바로 다음에 찍는 코드와 `onload` 안에서 찍는 코드를 비교하면 응답을 **기다린 뒤 읽어야 한다**는 뜻이 분명해진다. 정상적인 비동기 요청에서 바로 다음 줄의 값은 응답 전 빈 문자열일 수 있다. HTML 응답을 JSON이라고 생각해 `JSON.parse`하면 오류가 나므로 이 예제에서는 텍스트 그대로 기록한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/asset/js/20_ajax.js` 310–354행

```javascript
    const btn5 = document.querySelector('#btn5')
    btn5.addEventListener('click', function() {

        let a = undefined
        // try를 실행하고 오류가 나면 catch로 넘어감
        // catch는 전달인자가 있음
        // javascipt는 하나 오류나면 안 넘어가기 때문에, try catch로 잡음
        // 잡게되면 오류 다음에 있는 것은 실행이 됨
        try {
            a.push(1)
        }catch( e ){
            // console.log로 확인해봐야 err메세지를 확인할 수 있음
            console.log(e)
        }

        const url = 'https://jsonplaceholder.typicode.com/users'
        
        // 원래 방식
        // // 1_ajax 객체 생성 
        // const xhr = new XMLHttpRequest()
        // // 2_보낼 준비 방식(method), 주소(url)
        // xhr.open('GET', 'https://jsonplaceholder.typicode.com/users')
        // // 3_보내기
        // xhr.send()
        // // 4_결과 받기 및 활용, 갔다 오면~이기 때문에 콜백함수 이용
        // xhr.onload = function() {
        //     console.log('다녀왔어')
        //     console.log( xhr.responseText )
        // }

        // fetch(주소, 옵션json), 3번까지가 한 번에 끝남
        // ~하면(then), fetch의 get이 다 끝나면
        fetch(url, {
            method: 'GET'
            // then은 앞에 있는것이 동작 끝나면 진행 됨
        }).then(function(response) {
            console.log(response)
            // 아래는 JSON.parse(a.responseText) 역할 
            return response.json()
        }).then(function (data) {
            console.log(data)
        }).catch(function (error) {
            console.error( error )
        })
    })
```

**발췌 바로 풀이:** `fetch`는 요청을 시작하고 Promise를 돌려준다. 첫 `then`은 응답 객체를 받고 `response.json()`의 결과를 반환한다. 다음 `then`은 변환된 데이터를 받는다. `catch`는 체인에서 발생한 거절이나 오류를 기록한다. `response.json()`은 응답을 JSON으로 읽는 단계이지 모든 `responseText`를 자동으로 JSON으로 바꾸는 일반 명령이 아니다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/asset/js/20_ajax.js` 357–371행

```javascript
    const btn6 = document.querySelector('#btn6')
    btn6.addEventListener('click', function() {
        debugger

        console.log('btn6 클릭')
        debug()
        console.log('끝')
    })
}

function debug() {
    let a = 1

    console.log(a)
}
```

**발췌 바로 풀이:** `debugger`는 개발자 도구가 열려 있을 때 실행을 멈춰 변수와 순서를 살펴보는 연습이다. 두 코드 모두 버튼을 누르면 `debug()`를 부른다.

내 첫 버튼은 외부 사용자 API에 GET 요청을 보내고 onload에서 JSON.parse 뒤 두 번째 이름·세 번째 좌표를 점 표기와 대괄호 표기로 각각 읽는다. 두 번째 버튼은 19_json.html을 텍스트로 받아온다. 상대 주소는 외부 JS 파일의 디렉터리 자체가 아니라 문서의 기준 URL을 따라 해석된다. 응답이 HTML이면 JSON.parse 대상이 아니다. fetch 예제의 첫 then은 response.json()을 return하고 다음 then이 데이터 값을 받는다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

20_ajax.html → asset/js/20_ajax.js → load 때 버튼 등록 → 클릭에서 요청 → 브라우저가 응답 처리 예약 → onload 또는 then → JSON 읽기 → 배열·중첩 속성 접근 순서다. 원본 디버거 버튼은 debugger → btn6 클릭 출력 → debug() 호출 → 함수 안의 a=1 출력 → 끝 출력이다. debug의 정의도 원본 발췌에 함께 실었다. 개발자 도구로 멈췄을 때 다음 줄과 함수 진입을 따라가며 관찰한다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 내 코드는 같은 중첩 데이터를 두 표기법으로 읽고 요청 직후와 응답 콜백의 시점을 비교한다. **설명 교정:** 예외가 나면 JavaScript 전체가 영원히 멈춘다는 뜻은 아니다. 처리하지 않은 예외는 해당 실행 흐름을 중단시킬 수 있고, 원본은 이를 catch하여 아래 코드로 이어 간다. **공통 한계:** 응답이 왔다고 모든 HTTP 상태가 성공은 아니다. 원본은 상태 검사와 사용자 실패 안내가 충분하지 않다. 상태 검사 확장은 TIP에서 구분한다.

개선안은 원본을 수정한 결과가 아니다. 실제 오류, 수업용 단순화, 목적에 따른 선택을 구별해 판단한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



양쪽 핵심 요청 흐름이 같아 강사님 코드를 반복하지 않는다. 강사님이 option 변수를 만들어 놓았지만 실제 fetch에는 다른 객체 리터럴을 넘기므로 그 변수가 호출에 사용된 것으로 해설하지 않는다. 새 예제는 onload를 send보다 먼저 연결하여 응답 처리 준비와 요청 시작의 순서를 읽기 쉽게 했다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 표현 | 그 순간 얻는 것 | 바로 데이터 배열인가? |
| --- | --- | --- |
| new XMLHttpRequest | 요청 객체 | 아님 |
| send 직후 responseText | 아직 빈 문자열일 수 있음 | 아님 |
| onload의 responseText | 응답 본문 문자열 | parse가 별도 필요 |
| fetch 반환 | Promise | 아님 |
| 첫 then의 response | 응답 객체 | 아님 |
| json을 반환한 다음 then | 해석한 값 | 이 연습 파일은 배열 |

연습 파일을 웹 서버에서 받아오는 것은 실제 로컬 HTTP 요청이다. 외부 서비스의 성공을 확인한 것은 아니다. 상대 주소가 잘못되어 HTML 오류 페이지를 받은 경우 JSON 해석 실패가 날 수 있으므로 “통신이 됐다”와 “원하는 데이터 형식이다”를 나누어 확인한다.

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| users[1]을 users[0]으로 | 민지 출력 | 배열 인덱스 차이 |
| 첫 then의 return 제거 | 다음 then은 undefined를 받을 수 있음 | 비동기 결과를 넘기지 않음 |
| JSON 파일 대신 HTML 요청 | JSON 읽기 실패 | 응답 형식 차이 |
| 요청 주소 오타 | 원하는 데이터 대신 오류·다른 응답 | 요청과 내용 확인 필요 |

파일 직접 열기에서 실패하면 먼저 웹으로 제공하는 실행 조건을 맞춘다. 응답은 왔는데 JSON 오류면 실제 응답 본문을 확인한다. 다음 then의 값이 없으면 return 위치를 본다. 고정 사용자 이름과 좌표는 원본 주석의 당시 예시이며 외부 API의 영구 정답으로 외우지 않는다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** response.ok·status 검사, XHR의 오류·시간 초과 처리, 취소·중복 요청 관리와 async/await의 체계적 사용은 추가 학습이다. 본문은 실제 작성한 onload·then·catch 흐름으로 먼저 이해한다.



이 절의 확장은 기본 문제의 필수 조건이 아니다. 📚 출처가 있다는 것과 수업 밖 기능이라는 것은 다른 구분이다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. 요청 직후 출력과 onload 중 어디에서 응답을 읽는가?
2. 첫 then의 response와 다음 users는 같은 값인가?
3. HTML을 JSON으로 읽으면 왜 실패하는가?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

응답이 도착한 뒤 onload에서 읽는다. response는 응답 객체이고 users는 JSON 본문을 읽은 결과다. HTML은 JSON 문법이 아니어서 해석할 수 없다.

</details>

| 단계 | 확인 |
| --- | --- |
| 요청 | 주소·방식 |
| 응답 | 도착 시점·본문 형식 |
| 해석 | 문자열에서 값으로 |
| 연결 | return과 다음 then |

[장별 연습문제](실습/연습문제/20_JavaScript_AJAX와_fetch_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [날씨 응답 필터·표시](20-02_JavaScript_날씨응답_필터와_표시.md)다.

<!-- 이전 색인 이동 주소 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
<a id="section-6"></a>

[이 장의 목차](#chapter-toc)에서 현재 설명을 찾는다.
