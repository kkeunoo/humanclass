# 17-02. 이벤트 전파와 위임 — 자식 클릭을 부모가 처리하는 이유

[JavaScript 목차](README.md) · [읽기 안내](00_JavaScript_V3_동작_백과_읽기법.md)

버튼은 한 번 눌렀는데 같은 제목이 두 번 출력된다면 클릭 횟수부터 의심할 필요는 없다. 클릭이 지나가는 경로와 그 경로에 등록된 함수를 보면 한 사건이 여러 처리로 이어지는 이유를 찾을 수 있다.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

target·currentTarget을 구별하고 버블링 경로를 설명한다. 전파 중단과 기본 동작 취소를 나누며, 표와 행의 중복 처리·체크박스의 독립 처리를 추적한다.

입력·현재 상태·실행 순서·결과를 분리해 설명한다. 실제 수업 원본은 아래에 표시하고, 원본에 없는 선택 학습은 9절 TIP에 둔다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

클릭이 자식에서 발생하면 일반적인 버블링 리스너는 자식에서 상위 요소 쪽으로 처리될 수 있다. 반대로 캡처링은 상위에서 대상 쪽으로 내려오는 단계다. 내 원본 주석은 두 이름을 반대로 적었으므로 교정한다. 모든 이벤트가 같은 방식으로 버블링한다고 확대하지 않는다.

```text
상위 → 대상: 캡처링
대상에서 처리
대상 → 상위: 버블링
```

| 정보·호출 | 의미 | 자식 버튼을 누른 부모 리스너의 예 |
| --- | --- | --- |
| target | 실제 사건의 대상 | 자식 버튼 |
| currentTarget | 현재 실행 중인 리스너의 등록 대상 | 부모 |
| stopPropagation | 경로의 추가 전파 중단 | 부모로 올라가는 처리를 막음 |
| preventDefault | 기본 동작 취소 | 체크 전환·링크 이동 등과 관련 |

이벤트 위임은 부모에 처리 함수를 두고 target을 검사하여 자식의 일을 판단하는 방식이다. 자식마다 같은 리스너를 붙이는 대신 등록 지점을 모을 수 있다. 그러나 행에도 표에도 같은 처리를 남기면 클릭이 두 등록 지점을 지나 중복 결과가 생긴다.

> 📚 **출처 · 본문 설명 확인:** [MDN 이벤트 버블링](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Event_bubbling), [addEventListener의 this](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener). 배운 기능의 뜻을 확인한 근거다. 예제·표·풀이 흐름은 수업 코드를 바탕으로 새로 작성했으며 외부 문장을 직접 인용하지 않았다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 스크립트.** [HTML 실행 파일](실습/책형_복습/17-02_JavaScript_이벤트전파와_위임.html)과 같은 폴더의 [JS 파일](실습/책형_복습/17-02_JavaScript_이벤트전파와_위임.js)을 함께 내려받는다. HTML을 브라우저로 열고 Console에서 결과를 확인한다. script는 필요한 HTML 뒤에 연결한다. 콘솔 출력은 페이지 본문에 자동으로 쓰이지 않는다.

**먼저 준비할 HTML · body 안:**

```html
    <div id="parent">
        <button id="child1" type="button">전파 중단</button>
        <button id="child2" type="button">부모로 전달</button>
    </div>
    <table id="board"><tbody><tr>
        <td><input class="chk" type="checkbox" value="1" aria-label="첫 글 선택"></td>
        <td class="title">제목1</td><td writer="w1">작성자1</td>
    </tr></tbody></table>
```

```javascript
document.getElementById('parent').addEventListener('click', function (event) {
    console.log('부모', event.target.id, event.currentTarget.id);
});
document.getElementById('child1').addEventListener('click', function (event) {
    event.stopPropagation();
    console.log('자식1');
});
const board = document.getElementById('board');
board.addEventListener('click', function (event) {
    if (event.target.classList.contains('title')) {
        console.log('제목', event.target.textContent);
    }
    if (event.target.hasAttribute('writer')) {
        console.log('작성자', event.target.getAttribute('writer'));
    }
});
board.querySelector('input.chk').addEventListener('click', function (event) {
    event.stopPropagation();
    const row = this.parentNode.parentNode;
    console.log('체크', this.checked, row.querySelector('.title').textContent);
});
```

전파 중단 버튼, 부모로 전달 버튼, 제목, 작성자를 차례로 누르고 체크박스를 두 번 누른다. 자식1은 부모 출력을 만들지 않는다. 자식2의 클릭은 부모가 받지만 target은 child2이고 currentTarget은 parent다. 체크박스의 전파만 막았으므로 체크와 해제는 계속 일어나며 두 번 모두 제목을 출력한다. 새 예제는 표 한 곳에 위임을 모으고 checked 관찰을 추가한 설명 예제다. 원본의 이중 등록을 그대로 둔 결과와 다르다.

**예상 출력 또는 관찰:**

```text
자식1
부모 child2 parent
제목 제목1
작성자 w1
체크 true 제목1
체크 false 제목1
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본의 일부다. 원본에 의존하는 앞 선언·HTML·함수는 다음 절의 연결까지 읽는다. 주석의 잘못된 표현도 원문대로 보존하고 설명에서 교정한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/asset/js/17_event_form.js` 54–72행

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

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/asset/js/17_event_form.js` 74–82행

```javascript
    const child1 = document.querySelector('#child1')
    child1.addEventListener('click', function(event) {

        // preventDefault랑 비슷하지만 부모로 올라가는 내 이벤트를 stop
        // 부모에게 전달하는 것(캡쳐링) 방지
        event.stopPropagation()

        log('자식1 클릭')
    })
```

**발췌 바로 풀이:** 자식1을 클릭하면 '자식1 클릭'이 기록되고, 원본 parent의 click 함수로 올라가지 않는다. 자식2에는 이 중단 코드가 없으므로 '부모 클릭'이 기록된다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/asset/js/17_event_form.js` 90–109행

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

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/asset/js/17_event_form.js` 112–137행

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

**발췌 바로 풀이:** 강사님은 표 등록을 주석 처리하고 행 등록만 남겼다. 나는 **표와 행 두 곳 모두 활성 상태**다. 제목1을 한 번 누르면 내 코드에서는 행에서 한 번, 표에서 한 번 실행되어 같은 제목이 두 번 기록된다. 작성자1을 눌러도 w1이 두 번 기록된다. 같은 함수가 자동 중복 등록된 문제가 아니라, 경로상의 서로 다른 두 요소에 처리 코드를 둔 결과다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/asset/js/17_event_form.js` 139–151행

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

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/asset/js/17_event_form.js` 1–7행

```javascript
function log(message) {
    const div = document.createElement('div')
    div.classList.add('log')
    div.innerHTML = message
    const view = document.querySelector('#view')
    view.prepend(div)
}
```

내 parent 리스너는 자식2 클릭도 받아 target과 currentTarget을 출력한다. child1은 stopPropagation 뒤 자기 메시지만 출력한다. 게시판에서는 내 table과 각 tr에 처리 리스너가 모두 활성 상태다. 제목을 한 번 누르면 tr에서 한 번, table에서 한 번 같은 제목을 기록한다. 체크박스는 자체 리스너에서 전파를 중단하므로 위 행·표의 분기로 올라가지 않고 Console에 같은 행의 제목을 출력한다. checked 조건이 없어 해제할 때도 출력한다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

input.chk의 this → parentNode로 td → 다시 parentNode로 tr → querySelector로 같은 행의 title을 찾는다. 이 경로는 현재 HTML 구조에 의존한다. 중간 래퍼를 끼우면 부모 두 번의 도착점도 달라진다. 원본 log(message)는 아래 정의대로 화면에 메시지를 쌓고, 체크박스 분기의 console.log는 개발자 도구로 보낸다. 출력 위치가 다르므로 화면 로그에 없다는 이유로 함수가 실행되지 않았다고 판단하지 않는다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** target과 currentTarget을 함께 관찰하고 체크박스 처리를 나눠 위임을 실험했다. **실제 중복 처리:** 내 표·행 리스너가 함께 활성이라 한 클릭을 두 곳에서 처리한다. 한 위임 지점만 남기는 개선이 필요하다. **주석 교정:** stopPropagation이 target을 자기 자신으로 바꾸는 것은 아니다. 일반 function 리스너의 this는 여기서 currentTarget과 같지만, 화살표 함수는 주변 this를 이어받는다. 무조건 window이거나 사용할 수 없다는 일반 규칙으로 외우지 않는다.

개선안은 원본을 수정한 결과가 아니다. 실제 오류, 수업용 단순화, 목적에 따른 선택을 구별해 판단한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교

출처: `D:/workspace_teacher/workspace_html/javascript/asset/js/17_event_form.js` 98–114행

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

강사님은 표 등록을 주석 처리하고 행 등록만 남겨 중복 처리가 없다. 아래 강사님 발췌는 이 차이를 판단할 때 필요하여 인용한다. 다만 행마다 등록하는 방식과 표에 한 번 등록하는 방식 중 어느 쪽이 언제나 우수하다고 결론 내리지 않는다. 현재 개선의 핵심은 같은 일을 중복하는 등록을 정리하는 것이다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 클릭 | 내 원본에서 실행 | 구별할 것 |
| --- | --- | --- |
| 자식1 | 자식1 리스너 | 부모로 전파 중단 |
| 자식2 | 부모 리스너 | target은 자식2로 유지 |
| 제목 | 행 → 표 | 같은 제목이 두 번 기록 |
| 체크박스 | 체크박스 리스너 | 기본 체크 전환은 유지 |

전파 중단은 이미 실행한 상위 캡처 리스너의 일을 되돌리지 않는다. 같은 요소의 다른 리스너를 모두 지우는 호출도 아니다. title 안에 별도 자식 태그가 생기면 실제 target의 클래스가 title이 아닐 수 있으므로 단순한 현재 표에서 관찰한 결과를 복잡한 구조까지 확대하지 않는다.

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| 자식1의 stopPropagation 제거 | 자식1 다음 부모 출력 | 버블링 경로 유지 |
| 원본 table 등록만 제거 | 제목 중복이 한 번으로 줄음 | tr 등록은 남아 있음 |
| 체크 콜백에 this.checked 조건 추가 | 체크할 때만 제목 출력 | 해제 상태를 제외 |

한 번 눌렀는데 두 번 나오면 경로의 등록 대상을 확인한다. 제목이 안 잡히면 target이 실제로 어떤 요소인지 본다. this가 기대와 다르면 일반 함수인지 화살표 함수인지와 주변 this를 확인한다. 체크가 계속 바뀌는 것은 stopPropagation의 실패가 아니라 기본 동작을 취소하지 않은 결과다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** closest로 대상 찾기, stopImmediatePropagation, 복잡한 동적 컴포넌트의 위임 설계는 추가 학습이다. 먼저 배운 parentNode·classList·getAttribute와 전파의 역할을 연결한다.



이 절의 확장은 기본 문제의 필수 조건이 아니다. 📚 출처가 있다는 것과 수업 밖 기능이라는 것은 다른 구분이다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. 자식2를 누른 부모 리스너의 target과 currentTarget은?
2. 내 원본에서 제목이 두 번 출력되는 이유는?
3. 체크박스의 전파 중단은 체크 전환도 막는가?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

child2와 parent다. tr과 table의 두 리스너가 같은 클릭 경로에서 처리하기 때문이다. stopPropagation은 기본 체크 전환을 취소하지 않는다.

</details>

| 질문 | 먼저 볼 것 |
| --- | --- |
| 어디서 발생했나? | target |
| 누가 처리하나? | currentTarget |
| 왜 두 번인가? | 경로의 등록 지점 |
| 무엇을 막나? | 기본 동작과 전파 구별 |

[장별 연습문제](실습/연습문제/17-02_JavaScript_이벤트전파와_위임_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [주문·로그인·피자 실습](17-03_JavaScript_주문_로그인_피자실습.md)이다.

<!-- 이전 색인 이동 주소 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
<a id="section-6"></a>
<a id="section-7"></a>

[이 장의 목차](#chapter-toc)에서 현재 설명을 찾는다.
