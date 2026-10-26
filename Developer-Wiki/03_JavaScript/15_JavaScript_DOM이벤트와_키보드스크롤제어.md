# 15. DOM 이벤트 — 함수를 등록하고 사용자 동작에 반응하기

[JavaScript 목차](README.md) · [이전: 동기·비동기](14_JavaScript_동기비동기와_이벤트루프.md) · [다음: 키보드·스크롤](15-02_JavaScript_키보드와_스크롤.md)

기준은 양쪽 `15_event.html`과 `asset/js/15_event.js`다. 이벤트는 클릭·키 입력·페이지 로드처럼 브라우저에서 일어난 동작이나 상태 변화다. 이벤트가 발생했을 때 실행할 함수를 **미리 등록**한다. 이 장은 등록·제거와 로그인 입력 검사, 다음 장은 키보드·이동·스크롤을 다룬다.

<!-- chapter-toc -->

- [1. 처음에는 null인데 로드 뒤에는 버튼인 이유](15_JavaScript_DOM이벤트와_키보드스크롤제어.md#section-1)
- [2. onclick 대입과 addEventListener 등록](15_JavaScript_DOM이벤트와_키보드스크롤제어.md#section-2)
- [3. 제거하려면 등록한 함수 참조를 사용한다](15_JavaScript_DOM이벤트와_키보드스크롤제어.md#section-3)
- [4. 로그인 버튼은 입력 검사 실습이다](15_JavaScript_DOM이벤트와_키보드스크롤제어.md#section-4)
- [5. log는 새 메시지를 맨 위에 붙인다](15_JavaScript_DOM이벤트와_키보드스크롤제어.md#section-5)
- [6. 복습](15_JavaScript_DOM이벤트와_키보드스크롤제어.md#section-6)
- [추가로 알면 좋은 것](15_JavaScript_DOM이벤트와_키보드스크롤제어.md#section-7)

<a id="section-1"></a>

## 1. 처음에는 null인데 로드 뒤에는 버튼인 이유

양쪽 HTML은 head에서 외부 JavaScript를 읽는다. 그 시점에는 아래 body의 버튼을 아직 읽지 않았다. 파일 맨 위의 btn1은 null이고 init 안에서 다시 선택한 btn1은 버튼 요소다.

### 강사님 코드

출처: `teacher/workspace_html/javascript/asset/js/15_event.js` 15–25행 · **원본 발췌**

```javascript
function init(){
    const btn1 = document.querySelector('#btn1')
    console.log(2, 'btn1', btn1)

    const game = document.querySelector('#game')
    game.style.top = '10px'
    game.style.left = '20px'

    bind()
}
window.onload = init
```

### 내 코드

출처: `me/workspace_html/javascript/asset/js/15_event.js` 17–29행 · **원본 발췌**

```javascript
function init() {
    const btn1 = document.querySelector('#btn1')
    console.log(2, 'btn1', btn1)

    const game = document.querySelector('#game')
    game.style.left = '10px'
    game.style.top = '20px'

    bind()
}

// 이렇게 js에 주지 않아도 body에도 쓸 수 있음, 단 변수기때문에 한 번만 적용
window.onload = init
```

init은 요소를 준비하고 bind를 호출한다. bind는 이벤트 등록 코드를 묶은 **우리가 만든 함수 이름**이며 브라우저가 자동 호출하는 특별한 이름이 아니다. 함수 안의 btn1은 맨 위 btn1과 별도의 지역 변수다. 처음 null이었던 변수가 저절로 버튼으로 바뀐 것이 아니다.

window.onload = init은 함수를 등록한다. init()을 대입하면 그 자리에서 호출한 반환값을 넣게 된다. 이 차이는 [함수 참조·콜백](08-02_JavaScript_함수참조와_콜백.md)과 연결된다.

두 HTML에는 `<body onload="init();">`도 있다. body의 onload는 Window의 같은 이벤트 처리 속성과 연결되므로 두 독립 리스너가 더해지는 예로 읽지 않는다. 원본 실행의 init 횟수도 확인한다. 정리해서 쓸 때는 HTML onload를 빼고 JavaScript의 window.onload 등록 한곳을 유지하면 찾기 쉽다. 반면 addEventListener로 별도 등록까지 추가하면 호출 횟수가 달라질 수 있다. [HTML 표준: body의 이벤트 처리](https://html.spec.whatwg.org/multipage/sections.html#the-body-element)

<a id="section-2"></a>

## 2. onclick 대입과 addEventListener 등록

### 강사님 코드

출처: `teacher/workspace_html/javascript/asset/js/15_event.js` 30–46행 · **원본 발췌**

```javascript
    const btn1 = document.querySelector('#btn1')
    
    btn1.onclick = function(){
        console.log('btn1 클릭')
    }
    btn1.onclick = function(){
        console.log('btn1 click')
    }

    // addEventListener : 동일한 이벤트에 여러 함수를 추가할 수 있다
    const btn2 = document.querySelector('#btn2')
    btn2.addEventListener('click', function(){
        console.log('btn2 클릭')
    })
    btn2.addEventListener('click', function(){
        console.log('btn2 click')
    })
```

### 내 코드

출처: `me/workspace_html/javascript/asset/js/15_event.js` 39–55행 · **원본 발췌**

```javascript
    const btn1 = document.querySelector('#btn1')
    // 아래처럼 동일한 2개의 함수를 주어도, 변수이기 때문에 덮어씌워짐
    btn1.onclick = function() {
        console.log('btn1 클릭')
    }
    btn1.onclick = function() {
        console.log('btn1 click')
    }

    const btn2 = document.querySelector('#btn2')
    // onclick function에 담은 것과 다르게, 동일한 이벤트에 여러 함수 추가 할 수 있음
    btn2.addEventListener('click', function() {
        console.log('btn2 클릭')
    })
    btn2.addEventListener('click', function() {
        console.log('btn2 click')
    })
```

| 한 번 클릭 | 원본의 출력 | 이유 |
| --- | --- | --- |
| 버튼1 | btn1 click | 같은 onclick 속성에 두 번째 함수를 대입하여 교체 |
| 버튼2 | btn2 클릭 → btn2 click | 서로 다른 함수 두 개를 등록 |
| 버튼3 | btn3 click | HTML의 onclick="btn3click()"가 호출 |
| 버튼4 | 해당 클릭 출력 없음 | 등록 직후 제거했기 때문 |

내 코드와 강사님 코드는 같다. 두 익명함수의 글자가 같아 보여도 새로 작성한 함수 표현식은 서로 다른 함수다. 같은 대상·이벤트·등록 조건에서 **같은 함수 참조**를 addEventListener에 반복 전달한 경우와 구별한다. 원본의 주석 처리된 load 등록은 실행되지 않는다. [MDN addEventListener](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener)

**개인 학습 메모 — 코드 발췌 아님.** 첨부 메모에는 브라우저 개발자도구에서 버튼을 검사하고 **Event Listeners** 패널을 보면 연결된 이벤트를 확인할 수 있다고 적혀 있다. 위 원본의 버튼1과 버튼2를 각각 선택해 `click` 항목을 비교해 보자. 이 패널은 등록 상태를 살피는 보조 도구다. 실제로 어떤 함수가 실행되는지는 클릭 후 출력도 함께 확인한다.

<a id="section-3"></a>

## 3. 제거하려면 등록한 함수 참조를 사용한다

### 강사님 코드

출처: `teacher/workspace_html/javascript/asset/js/15_event.js` 48–53행 · **원본 발췌**

```javascript
    const btn4 = document.querySelector('#btn4')
    btn4.addEventListener('click', btn4click)
    // removeEventListener
    // 이벤트 제거
    // 단, 익명함수는 제거 못함
    btn4.removeEventListener('click', btn4click)
```

### 내 코드

출처: `me/workspace_html/javascript/asset/js/15_event.js` 57–63행 · **원본 발췌**

```javascript
    const btn4 = document.querySelector('#btn4')
    // btn4click() 으로 하면 실행이 되어버리는데, 실행이 되었을 때
    // 아래 btn4click 지역에 return이 없으므로 btn4click()가 'undefined'가 됨
    // 익명함수는 쓸 수 있지만 함수 자체를 넣으면 실행이 됨
    // remove는 event를 제거해주지만, 익명함수는 쉽게 제거할 수 없음
    btn4.addEventListener('click', btn4click)
    btn4.removeEventListener('click', btn4click)
```

btn4click을 등록하고 같은 함수를 제거하므로 클릭해도 그 함수가 실행되지 않는다. 제거하는 것은 버튼이나 click 이벤트 자체가 아니라 **등록한 리스너**다. 강사님 주석의 ‘익명함수는 제거 못함’은 ‘참조를 보관하지 않고 등록하면 나중에 같은 함수를 지정하기 어렵다’로 고쳐 읽는다.

**배운 함수 참조로 재구성한 예제 — 원본 발췌 아님**

```javascript
const handler = function () {
    console.log('버튼 클릭')
}
btn4.addEventListener('click', handler)
btn4.removeEventListener('click', handler)
```

이름 없는 함수 표현식도 변수에 참조를 보관하면 제거할 수 있다. 새 function을 똑같이 작성해서 전달하는 것은 같은 참조가 아니다. [MDN removeEventListener](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/removeEventListener)

<a id="section-4"></a>

## 4. 로그인 버튼은 입력 검사 실습이다

서버에 요청하거나 계정을 인증하는 코드가 아니다. 클릭할 때 #id와 #pw의 현재 value를 읽고 비었는지 검사한다. 테스트에는 임의의 연습 문자열을 사용한다.

### 강사님 코드

출처: `teacher/workspace_html/javascript/asset/js/15_event.js` 65–76행 · **원본 발췌**

```javascript
        // id를 적었는지 판단
        if(id.value.trim() == ''){
            console.log('아이디는 필수입니다')
            warning.innerText = '아이디는 필수입니다'

            log('아이디는 필수입니다')
        }
        else if(pw.value.trim() == ''){
            warning.innerText = '비밀번호는 필수입니다'

            log('비밀번호는 필수입니다')
        }
```

### 내 코드

출처: `me/workspace_html/javascript/asset/js/15_event.js` 87–104행 · **원본 발췌**

```javascript
        if(id.value.trim() == '') {
            console.log('아이디는 필수입니다.')
            warning.innerText = '아이디는 필수입니다.'

            // <!-- <div class="log">글씨 출력</div> -->
            // const div = document.createElement('div')
            // div.classList.add('log')
            // div.innerHTML = '아이디는 필수입니다.'
            // const view = document.querySelector('#view')
            // view.prepend(div)

            log('아이디는 필수입니다.')
        } else if(pw.value.trim() == '') {
            console.log('아이디는 필수입니다.')
            warning.innerText = '아이디는 필수입니다.'

            log('비밀번호는 필수입니다.')
        } 
```

| 입력 | 강사님 warning | 내 warning | 내 화면 로그 |
| --- | --- | --- | --- |
| 둘 다 빈 값 | 아이디는 필수입니다 | 아이디는 필수입니다. | 아이디는 필수입니다. |
| id만 입력 | 비밀번호는 필수입니다 | **아이디는 필수입니다.** | 비밀번호는 필수입니다. |
| 둘 다 입력 | 기존 경고 유지 | 기존 경고 유지 | 새 경고 로그 없음 |

내 else if의 화면 경고와 console 출력이 아이디 문구로 남아 있다. 여기서는 강사님 코드처럼 비밀번호 문구를 써야 조건과 안내가 일치한다. 두 원본 모두 마지막 else가 없어 앞선 실패 경고가 남는다. 내 파일 앞쪽의 주석 처리된 연습에는 else로 지우는 시도가 있지만 현재 활성 코드에는 없다.

trim()은 검사에 쓰는 새 문자열을 반환한다. 사용자가 입력한 원래 value 자체를 지우거나 자동 수정하는 기능은 아니다. `'   ' == ''`는 false이므로 trim 뒤에 비교한다. 내 주석의 ‘== 빈 문자열은 스페이스바도 포함’이라는 설명은 이 의미로 바로잡는다.

**양쪽 원본을 바탕으로 교정한 조건 부분 — 클릭 함수 안에서 사용**

```javascript
if (id.value.trim() == '') {
    warning.innerText = '아이디는 필수입니다.'
    log('아이디는 필수입니다.')
} else if (pw.value.trim() == '') {
    warning.innerText = '비밀번호는 필수입니다.'
    log('비밀번호는 필수입니다.')
} else {
    warning.innerText = ''
}
```

둘 다 입력하면 현재 warning만 비운다. 과거 로그까지 삭제하는 코드는 아니다. 원본의 비밀번호 console 출력은 연습용 값 관찰이며 실제 로그인 기능에 그대로 남겨 두는 방식으로 안내하지 않는다.

<a id="section-5"></a>

## 5. log는 새 메시지를 맨 위에 붙인다

### 강사님 코드

출처: `teacher/workspace_html/javascript/asset/js/15_event.js` 142–149행 · **원본 발췌**

```javascript
function log(message){
    //  <div class="log">글씨 출력</div>
    const div = document.createElement('div')
    div.classList.add('log')
    div.innerHTML = message
    const view = document.querySelector('#view')
    view.prepend(div)
}
```

### 내 코드

출처: `me/workspace_html/javascript/asset/js/15_event.js` 194–201행 · **원본 발췌**

```javascript
function log(message) {
    // <!-- <div class="log">글씨 출력</div> -->
    const div = document.createElement('div')
    div.classList.add('log')
    div.innerHTML = message
    const view = document.querySelector('#view')
    view.prepend(div)
}
```

양쪽은 같은 방식이다. log(message)는 div를 만들고 log 클래스를 붙여 #view의 첫 자식으로 넣는다. 나중 메시지가 위에 있으므로 **화면 위에서 아래로 읽는 순서가 시간순과 반대**다. 문자열 메시지 출력 목적이라면 div.innerHTML 대신 div.textContent = message를 쓰는 교정이 가능하다. 차이는 [12 콘텐츠](12_JavaScript_DOM_콘텐츠생성과_스타일조작.md)에서 읽는다.

<a id="section-6"></a>

## 6. 복습

1. onclick에 두 번 대입하면 함수 두 개가 쌓이는가?
2. addEventListener에 btn4click()을 넘기면 무엇이 달라지는가?
3. 내 코드에서 id만 입력한 경우 화면 안내가 잘못된 이유는?
4. 교정 후 모두 입력해도 #view의 과거 메시지가 남는 이유는?

<details>
<summary>정답</summary>

1. 아니다. 같은 속성의 값이 교체된다.
2. 함수를 즉시 호출하고 반환값을 넘긴다. 원본은 함수 참조를 등록해야 한다.
3. 비밀번호 조건 안에서 warning에 아이디 문구를 넣었기 때문이다.
4. 교정 코드는 현재 warning만 비운다. #view의 자식은 제거하지 않았다.

</details>

<a id="section-7"></a>

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/15_JavaScript_DOM이벤트와_키보드스크롤제어_연습문제.md)

## 추가로 알면 좋은 것

defer·DOMContentLoaded를 이용한 별도 로딩 전략, AbortController로 여러 리스너 관리하기, 서버 인증 구현은 추가 학습이다. 이 장에서는 원본 load·onclick·addEventListener·removeEventListener와 배운 입력 검사까지만 기본 범위로 둔다.

