# 17-02. 이벤트 전파·위임 — 자식을 눌렀는데 부모가 반응하는 이유

[JavaScript 목차](README.md) · [이전: 폼 이벤트](17_JavaScript_폼이벤트와_이벤트전파_실전문제.md)

양쪽 `asset/js/17_event_form.js`의 parent/child와 게시판 실습이다. 강사님과 내 코드에서 **실행 중인 리스너의 위치**를 비교한다. 주문·로그인·피자는 [17-03](17-03_JavaScript_주문_로그인_피자실습.md), 메뉴·Todo는 [17-04](17-04_JavaScript_메뉴와_Todo실습.md)에 정리했다.

<!-- chapter-toc -->

- [1. 캡처링과 버블링 방향](17-02_JavaScript_이벤트전파와_위임.md#section-1)
- [2. target과 currentTarget](17-02_JavaScript_이벤트전파와_위임.md#section-2)
- [3. 자식1은 위로 전달하지 않는다](17-02_JavaScript_이벤트전파와_위임.md#section-3)
- [4. 게시판에 이벤트를 위임한다](17-02_JavaScript_이벤트전파와_위임.md#section-4)
- [5. 체크박스 클릭은 별도 처리한다](17-02_JavaScript_이벤트전파와_위임.md#section-5)
- [6. 복습](17-02_JavaScript_이벤트전파와_위임.md#section-6)
- [추가로 알면 좋은 것](17-02_JavaScript_이벤트전파와_위임.md#section-7)

<a id="section-1"></a>

## 1. 캡처링과 버블링 방향

```text
상위에서 대상 쪽으로 내려오는 단계: 캡처링
대상에서 이벤트 처리
대상에서 상위 쪽으로 올라가는 단계: 버블링
```

내 원본 주석은 두 이름을 반대로 적었다. 기본 addEventListener('click', 함수)는 별도 캡처 옵션을 주지 않았으므로, 자식에서 발생한 click이 올라올 때 부모 리스너가 반응하는 예제다. 모든 이벤트가 똑같이 버블링한다고 확대하지 않는다. [MDN 이벤트 버블링](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Event_bubbling)

<a id="section-2"></a>

## 2. target과 currentTarget

### 강사님 코드

출처: `teacher/workspace_html/javascript/asset/js/17_event_form.js` 46–63행 · **원본 발췌**

```javascript
    const parent = document.querySelector('#parent')
    parent.addEventListener('click', function(event){
        log('부모 클릭')

        // target : 실제 이벤트가 발생한 DOM
        console.log('event.target', event.target)

        // currentTarget : 이벤트가 적용되어 있는 DOM
        console.log('event.currentTarget', event.currentTarget)
        
        // this
        //      addEventListener 안에서는 event.currentTarget
        //      대부분의 경우 window를 가지고 있다
        //      그래서 현재 this에 어떤 값이 있는지 알고 있을 때만 쓴다
        //      arrow 함수의 경우 this === window
        console.log('this', this)
        console.log(  this === event.currentTarget  )
    })
```

### 내 코드

출처: `me/workspace_html/javascript/asset/js/17_event_form.js` 54–72행 · **원본 발췌**

```javascript
    const parent = document.querySelector('#parent')
    // 이벤트는 부모에게 주었지만, 자식을 클릭할 때 마다 target으로 작동(위임)
    parent.addEventListener('click', function(event) {
        log('부모 클릭')

        // target은 실제 이벤트가 발생 한 DOM을 가르키게 됨
        console.log('event.target', event.target)

        // currentTarget은 이벤트가 걸려있는 DOM이 나옴(현재 부모에게 적용되어있음)
        console.log('event.currenttarget', event.currentTarget)

        // this는 currentTarget과 동일하지만, 쉽게 쓸 수 있도록 만들어준 것
        // addEventListener 안에서는 event.currentTarget 를 의미
        // 기본적으로 this객체에는 'window'가 들어가있음
        // 편하지만, 지금 this가 뭔지 알 수 있을때만 사용해야 함 (arrow도 불가)
        console.log('this', this)
        console.log( this === event.currentTarget) // true

    })
```

| 부모 리스너에서 확인 | 부모 자체 클릭 | 자식2 클릭 |
| --- | --- | --- |
| event.target | parent | child2 |
| event.currentTarget | parent | parent |
| 일반 function의 this | parent | parent |

target은 이벤트가 발생한 대상이고 currentTarget은 **지금 실행 중인 리스너가 등록된 대상**이다. 자식2를 클릭해도 currentTarget이 자식2가 되는 것이 아니다. 양쪽의 일반 function에서는 this === event.currentTarget이 true다.

화살표 함수는 주변의 this를 사용한다. 양쪽 주석의 ‘화살표 함수는 무조건 window’나 ‘arrow 불가’는 일반 규칙이 아니다. 이 예제를 둘러싼 일반 load 함수의 this는 Window라, 그 안에서 화살표 리스너로 바꾸면 이 경우에는 Window를 이어받는다. 원본처럼 리스너 등록 대상을 명확히 읽으려면 event.currentTarget을 확인하면 된다. [MDN addEventListener의 this](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener)

<a id="section-3"></a>

## 3. 자식1은 위로 전달하지 않는다

### 강사님 코드

출처: `teacher/workspace_html/javascript/asset/js/17_event_form.js` 65–72행 · **원본 발췌**

```javascript
    const child1 = document.querySelector('#child1')
    child1.addEventListener('click', function(event){
        // 전달 방지
        // 부모로 전달되는 이벤트 중지
        event.stopPropagation()

        log('자식1 클릭')
    })
```

### 내 코드

출처: `me/workspace_html/javascript/asset/js/17_event_form.js` 74–82행 · **원본 발췌**

```javascript
    const child1 = document.querySelector('#child1')
    child1.addEventListener('click', function(event) {

        // preventDefault랑 비슷하지만 부모로 올라가는 내 이벤트를 stop
        // 부모에게 전달하는 것(캡쳐링) 방지
        event.stopPropagation()

        log('자식1 클릭')
    })
```

자식1을 클릭하면 '자식1 클릭'이 기록되고, 원본 parent의 click 함수로 올라가지 않는다. 자식2에는 이 중단 코드가 없으므로 '부모 클릭'이 기록된다.

| 호출 | 목적 | 원본 사례 |
| --- | --- | --- |
| preventDefault() | 기본 동작 취소 | 검색 제출을 먼저 멈춤 |
| stopPropagation() | 이벤트 경로의 전파 중단 | 자식 click이 부모 리스너로 올라가는 것 중단 |

stopPropagation이 target을 '나'로 바꾸는 것은 아니다. target은 원래 발생 대상이고 이 메서드는 전파를 제어한다. 이미 실행된 상위 캡처 리스너를 되돌리는 것도 아니다. 같은 요소의 다른 리스너를 모두 지우는 기능과도 구분한다.

<a id="section-4"></a>

## 4. 게시판에 이벤트를 위임한다

각 셀마다 같은 함수를 붙이는 대신 행 또는 표에 click 함수를 두고 event.target을 검사한다. 제목 셀이면 글자를, writer 속성이 있으면 그 값을 출력한다. 이것이 이 원본의 이벤트 위임이다.

### 강사님 코드 — 행에 등록

출처: `teacher/workspace_html/javascript/asset/js/17_event_form.js` 98–114행 · **원본 발췌**

```javascript
    const trs = document.querySelectorAll('#board tr')
    for( let tr of trs ){
        tr.addEventListener('click', function(event){
            console.log(event.target)
    
            if(event.target.classList.contains('chk')){
                log(event.target.value)
            }
    
            if(event.target.classList.contains('title')){
                log(event.target.textContent)
            }
    
            if(event.target.hasAttribute('writer')){
                log(event.target.getAttribute('writer'))
            }
        })
```

### 내 코드 — 표에도 등록

출처: `me/workspace_html/javascript/asset/js/17_event_form.js` 90–109행 · **원본 발췌**

```javascript
    const board = document.querySelector('#board')
    board.addEventListener('click', function(event) {
        console.log(event.target)
        // log(event.target)

       if(event.target.classList.contains('chk')) {
            // console.log(event.target.value)
            log(event.target.value)
       }

       if(event.target.classList.contains('title')) {
            log(event.target.innerText)
       }

       // 원래라면 class가 들어가 있어야 하지만, writer로 들어가 있기 때문에
       // hasAttribute로 있는지 확인하고 getAttribute로 값을 가져오기
       if(event.target.hasAttribute('writer')) {
            log(event.target.getAttribute('writer'))
       }
    })
```

### 내 코드 — 행 등록도 활성 상태

출처: `me/workspace_html/javascript/asset/js/17_event_form.js` 112–137행 · **원본 발췌**

```javascript
    const trs = document.querySelectorAll('#board tr')
    // all을 쓰게되면 배열로 가져오기에 for문을 쓰는게 좋고, of로 배열의 처음부터 끝까지
    for( let tr of trs ) {
        tr.addEventListener('click', function(event) {
            console.log(event.target)
            // log(event.target)
    
            // tr안에 있는 chk라는 class를 가진 것을 true값 반환하고
            // true일 때 value 출력
            if(event.target.classList.contains('chk')) {
                // console.log(event.target.value)
                log(event.target.value)
            }
            
            // tr안에 있는 title이라는 class를 가진 것을 true값 반환하고
            // true일 때 text 출력
           if(event.target.classList.contains('title')) {
                log(event.target.innerText)
           }
    
           // 원래라면 class가 들어가 있어야 하지만, writer로 들어가 있기 때문에
           // hasAttribute로 있는지 확인하고 getAttribute로 값을 가져오기
           if(event.target.hasAttribute('writer')) {
                log(event.target.getAttribute('writer'))
           }
        })
```

강사님은 표 등록을 주석 처리하고 행 등록만 남겼다. 나는 **표와 행 두 곳 모두 활성 상태**다. 제목1을 한 번 누르면 내 코드에서는 행에서 한 번, 표에서 한 번 실행되어 같은 제목이 두 번 기록된다. 작성자1을 눌러도 w1이 두 번 기록된다. 같은 함수가 자동 중복 등록된 문제가 아니라, 경로상의 서로 다른 두 요소에 처리 코드를 둔 결과다.

이 실습의 요구처럼 행 위임으로 정리하려면 내 90–109행의 표 등록 부분을 제거하거나 주석 처리하고 행 등록을 유지한다. 강사님 코드의 이 구분이 더 명확하다. closest 같은 새로운 API로 원본 전체를 다시 설계할 필요는 없다.

<a id="section-5"></a>

## 5. 체크박스 클릭은 별도 처리한다

### 강사님 코드

출처: `teacher/workspace_html/javascript/asset/js/17_event_form.js` 116–124행 · **원본 발췌**

```javascript
        tr.querySelector('input.chk').addEventListener('click', function(event){
            event.stopPropagation()

            // console.log(this.parentNode)

            console.log(
                this.parentNode.parentNode.querySelector('.title').innerText
            )
        })
```

### 내 코드

출처: `me/workspace_html/javascript/asset/js/17_event_form.js` 139–151행 · **원본 발췌**

```javascript
        // input 태그이고 chk라는 class를 가진 것을 가져온 뒤 click 이벤트 설정
        tr.querySelector('input.chk').addEventListener('click', function(event) {
            // 부모에게 올라가는걸 막았기 때문에 target은 '나' 임
            event.stopPropagation()

            // 이렇게 쓰면 tr상위인 td로 올라갈 수 있음
            // console.log(this.parentNode)

            // parentNode를 사용해서 상위 부모까지 올라갈 수 있음 (형제 등 있을 때)
            console.log(
                this.parentNode.parentNode.querySelector('.title').innerText
            )
        })
```

```text
this: input.chk
  → parentNode: td
  → parentNode: tr
  → querySelector('.title'): 같은 행의 제목 셀
```

양쪽은 같은 동작이다. 체크박스에서 전파를 멈추므로 위 행·표의 value 출력 분기는 이 클릭에서 실행되지 않고 **console에 제목**을 출력한다. #view의 log에 제목을 넣는 것과 혼동하지 않는다. stopPropagation만 호출했으므로 체크 자체의 기본 동작은 그대로다.

또한 원본은 checked를 검사하지 않는다. 체크할 때뿐 아니라 **체크 해제할 때도** 제목을 출력한다. 문제 주석의 ‘체크하면’만 보고 활성 코드를 선택 시에만 실행되는 것으로 해석하지 않는다. 체크된 때만 출력하려면 같은 콜백 안에서 이미 배운 this.checked 조건을 추가하는 별도 교정으로 표시한다.

parentNode 두 번은 이 HTML의 input → td → tr 구조에 맞춘 경로다. 중간에 다른 요소를 끼우면 달라질 수 있다. 행 안에 제목 자식 태그를 추가했을 때도 target의 class가 title인지 직접 검사하는 원본 분기는 원하는 대로 작동하지 않을 수 있다. 현재 단순 표 구조의 학습 범위를 분명히 한다.

<a id="section-6"></a>

## 6. 복습

1. 자식2를 클릭할 때 부모 리스너의 target/currentTarget은?
2. 내 제목 셀 클릭이 두 번 출력되는 이유는?
3. 체크박스 클릭의 stopPropagation이 체크 전환도 막는가?
4. 원본은 체크를 해제할 때도 console에 제목을 출력하는가?

<details>
<summary>정답</summary>

1. child2 / parent다.
2. tr과 table 양쪽에서 같은 종류의 click을 처리한다.
3. 아니다. 원본은 기본 체크 동작을 취소하지 않았다.
4. 그렇다. checked를 검사하는 조건이 없다.

</details>

<a id="section-7"></a>

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/17-02_JavaScript_이벤트전파와_위임_연습문제.md)

## 추가로 알면 좋은 것

closest를 이용한 대상 찾기, stopImmediatePropagation, 복잡한 동적 컴포넌트의 위임 설계는 추가편이다. 수업의 parentNode·classList·getAttribute와 전파 차이를 먼저 익힌다.

