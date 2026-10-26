# 20. AJAX와 fetch — 화면 이동 없이 응답 받기

[JavaScript 목차](README.md) · [이전: 객체와 JSON](19_JavaScript_객체와_JSON.md) · [다음: 날씨 응답 가공](20-02_JavaScript_날씨응답_필터와_표시.md)

양쪽 `20_ajax.html`과 `asset/js/20_ajax.js`에서 실제 다룬 것은 `XMLHttpRequest`, 응답의 JSON 변환, `fetch`의 `then`·`catch`다. 네트워크 예제는 외부 사이트의 상태와 브라우저 실행 환경에 따라 결과가 바뀔 수 있다. 아래는 **코드 흐름**을 기준으로 설명한다.

<!-- chapter-toc -->

- [1. XMLHttpRequest의 네 단계](#section-1)
- [2. 로컬 HTML을 받아보며 실행 순서 관찰](#section-2)
- [3. fetch와 Promise 연결](#section-3)
- [4. 디버거 연습](#section-4)
- [직접 확인할 질문](#section-5)
- [추가로 알면 좋은 것](#section-6)

<a id="section-1"></a>

## 1. XMLHttpRequest의 네 단계

### 강사님 코드

출처: `teacher/workspace_html/javascript/asset/js/20_ajax.js` 5~35행 · **원본 발췌**

```javascript
    const btn1 = document.querySelector('#btn1')
    btn1.addEventListener('click', function(){

        // 1. ajax 객체 생성
        const xhr = new XMLHttpRequest()

        // 2. 보낼 준비
        // 방식method, 주소
        xhr.open('GET', 'https://jsonplaceholder.typicode.com/users')

        // 3. 보내기
        xhr.send()

        // 4. 결과 활용
        xhr.onload = function(){
            console.log('다녀왔어')
            // xhr.responseText : 응답받은 글씨가 들어가 있는 변수
            console.log( xhr.responseText )

            // 깜짝 퀴즈
            // 두 번째 사람의 이름을 출력
            //      Ervin Howell
            // 세 번째 사람의 lat를 출력
            //      -68.6102
            const member = JSON.parse(xhr.responseText)
            console.log(member[1])
            console.log(member[1].name)
            console.log(member[1]['name'])
            console.log(member[2].address.geo.lat)
        }
    })
```

### 내 코드

출처: `me/workspace_html/javascript/asset/js/20_ajax.js` 7~38행 · **원본 발췌**

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

객체를 만들고 `open('GET', 주소)`로 요청을 준비하고 `send()`로 보낸다. 응답이 오면 `onload`에서 `responseText`를 읽는다. 응답이 JSON 문자열이라는 전제에서 `JSON.parse`로 배열을 만든 뒤 두 번째 사람은 인덱스 `1`, 세 번째 사람은 인덱스 `2`로 접근한다. 내 코드는 대괄호와 점 표기를 둘 다 확인한다. 강사님 주석의 사람 이름·좌표 값은 당시 예시 데이터에 관한 것이므로 항상 고정된 결과라고 외우지 않는다.

<a id="section-2"></a>

## 2. 로컬 HTML을 받아보며 실행 순서 관찰

### 강사님 코드

출처: `teacher/workspace_html/javascript/asset/js/20_ajax.js` 37~57행 · **원본 발췌**

```javascript
    const btn2 = document.querySelector('#btn2')
    btn2.addEventListener('click', function(){

        // 1. ajax 객체 생성
        const xhr = new XMLHttpRequest()

        // 2. 보낼 준비
        // 방식method, 주소
        xhr.open('GET', '19_json.html')

        // 3. 보내기
        xhr.send()

        // 4. 결과 활용
        xhr.onload = function(){
            console.log('다녀왔어')
            console.log( xhr.responseText )
        }

        console.log( '['+ xhr.responseText +']')
    })
```

### 내 코드

출처: `me/workspace_html/javascript/asset/js/20_ajax.js` 40~58행 · **원본 발췌**

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

`19_json.html`은 요청을 시작한 페이지 `20_ajax.html`의 주소를 기준으로 해석되는 상대 경로다. `xhr.responseText`를 `send()` 바로 다음에 찍는 코드와 `onload` 안에서 찍는 코드를 비교하면 응답을 **기다린 뒤 읽어야 한다**는 뜻이 분명해진다. 정상적인 비동기 요청에서 바로 다음 줄의 값은 응답 전 빈 문자열일 수 있다. HTML 응답을 JSON이라고 생각해 `JSON.parse`하면 오류가 나므로 이 예제에서는 텍스트 그대로 기록한다.

<a id="section-3"></a>

## 3. fetch와 Promise 연결

### 강사님 코드

출처: `teacher/workspace_html/javascript/asset/js/20_ajax.js` 189~227행 · **원본 발췌**

```javascript
    const btn5 = document.querySelector('#btn5')
    btn5.addEventListener('click', function(){

        let a = undefined
        try{
            a.push(1)
        }catch( e ){
            console.log(e)
        }

        const url = 'https://jsonplaceholder.typicode.com/users'

        // // 1. ajax 객체 생성
        // const xhr = new XMLHttpRequest()
        // // 2. 보낼 준비
        // // 방식method, 주소
        // xhr.open('GET', 'https://jsonplaceholder.typicode.com/users')
        // // 3. 보내기
        // xhr.send()
        // // 4. 결과 활용
        // xhr.onload = function(){ 
            // console.log( xhr.responseText )
            // const member = JSON.parse(xhr.responseText)

        // fetch(주소, 옵션json)
        let option = {
            method: 'GET'
        }
        fetch(url, {
            method: 'GET'
        }).then(function (response){
            console.log(response)
            return response.json()
        }).then(function (data){
            console.log(data)
        }).catch(function (error){
            console.error( error )
        })
    })
```

### 내 코드

출처: `me/workspace_html/javascript/asset/js/20_ajax.js` 310~354행 · **원본 발췌**

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

`fetch`는 요청을 시작하고 Promise를 돌려준다. 첫 `then`은 응답 객체를 받고 `response.json()`의 결과를 반환한다. 다음 `then`은 변환된 데이터를 받는다. `catch`는 체인에서 발생한 거절이나 오류를 기록한다. `response.json()`은 응답을 JSON으로 읽는 단계이지 모든 `responseText`를 자동으로 JSON으로 바꾸는 일반 명령이 아니다.

양쪽 코드에는 먼저 `undefined`에 `push`하여 오류를 발생시키고 `try...catch`로 잡는 별도 실습이 있다. 그 오류를 처리했기 때문에 아래 `fetch` 코드로 계속 진행한다. 강사님 코드의 `option` 변수는 만들어 두었지만 실제 `fetch` 호출에는 별도 객체가 전달된다.

<a id="section-4"></a>

## 4. 디버거 연습

### 강사님 코드

출처: `teacher/workspace_html/javascript/asset/js/20_ajax.js` 230~246행 · **원본 발췌**

```javascript
    const btn6 = document.querySelector('#btn6')
    btn6.addEventListener('click', function(){
        debugger
    
        console.log('btn6 클릭')
        debug()
        console.log('끝')
    })

}

function debug(){

    let a = 1
    
    console.log(a)
}
```

### 내 코드

출처: `me/workspace_html/javascript/asset/js/20_ajax.js` 357~371행 · **원본 발췌**

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

`debugger`는 개발자 도구가 열려 있을 때 실행을 멈춰 변수와 순서를 살펴보는 연습이다. 두 코드 모두 버튼을 누르면 `debug()`를 부른다.

<a id="section-5"></a>

## 직접 확인할 질문

1. `responseText`를 읽는 줄은 `send()` 바로 뒤와 `onload` 안 중 어디가 응답 도착을 보장할까?
2. `fetch`의 두 번째 `then`은 응답 객체를 받을까, 파싱된 데이터를 받을까?
3. `19_json.html`을 받아온 문자열을 바로 JSON으로 파싱하면 어떻게 될까?

<a id="section-6"></a>

## 추가로 알면 좋은 것

원본 예제에는 응답 상태 코드 검사와 요청 실패 시 사용자 화면 안내가 없다. 실제 서비스에서는 성공 응답인지 확인하고 실패를 화면에서도 설명해야 한다.

