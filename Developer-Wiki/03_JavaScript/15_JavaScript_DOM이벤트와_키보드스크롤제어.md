# 15. DOM 이벤트 — 등록·호출·제거와 입력 검사

[JavaScript 목차](README.md) · [읽기 안내](00_JavaScript_V3_동작_백과_읽기법.md)

이벤트는 클릭이나 페이지 로드처럼 브라우저에서 일어난 동작·변화다. 함수는 미리 등록해 두고 해당 동작이 발생했을 때 실행한다. 등록 직후의 상태와 클릭한 뒤의 결과를 나누면 여러 처리 방식의 차이를 설명할 수 있다.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

onclick의 교체와 addEventListener의 여러 함수 등록을 비교한다. 등록할 때 사용한 함수 참조로 제거하는 이유, HTML과 외부 JavaScript의 연결, 입력 검사와 실제 인증의 차이를 설명한다.

입력·현재 상태·실행 순서·결과를 분리해 설명한다. 실제 수업 원본은 아래에 표시하고, 원본에 없는 선택 학습은 9절 TIP에 둔다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

이벤트는 사용자가 버튼을 누르거나 페이지 로드가 끝나는 등의 사건이다. 이벤트 처리 함수는 그 사건이 일어났을 때 실행할 작업이다. 리스너 등록은 브라우저에 “이 버튼에서 click이 발생하면 이 함수를 호출해 주세요”라고 연결해 두는 작업이다. 등록문을 실행한 순간과 사용자가 클릭한 순간은 다르다.

button.addEventListener('click', handler)에서 handler는 함수 자체를 가리키는 값이다. handler()라고 쓰면 먼저 함수를 실행하고 그 반환값을 전달한다. 함수 이름이 handler라서 자동 실행되는 것이 아니라, 등록 코드가 그 함수와 사건을 연결하기 때문에 나중에 실행된다.

| 작성 방법 | 저장하는 것 | 다시 작성하면 |
| --- | --- | --- |
| onclick = 함수 | 하나의 이벤트 처리 속성 값 | 뒤의 값이 앞의 값을 교체 |
| addEventListener('click', 함수) | 해당 이벤트의 리스너 등록 | 서로 다른 함수들을 함께 등록 가능 |
| removeEventListener('click', 함수) | 기존 등록을 찾아 제거 | 버튼 요소 자체는 남음 |

같은 내용의 익명 함수를 두 번 적어도 새로 만든 함수들은 서로 다른 값이다. 제거할 때는 등록했던 함수의 참조가 필요하다. 반대로 같은 대상에 같은 이벤트·함수·capture 조건으로 반복 등록하는 경우를 서로 다른 함수 등록과 혼동하지 않는다.

HTML의 head에서 외부 script를 읽을 때는 body의 버튼을 아직 만들지 않았을 수 있다. 이때 선택 결과는 null이다. 원본은 로드가 끝난 뒤 init에서 다시 선택한다. 앞에서 null을 받았던 변수가 저절로 버튼으로 바뀐 것이 아니라, 나중에 새로 선택한 결과를 사용하는 것이다.

> 📚 **출처 · 본문 설명 확인:** [MDN addEventListener](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener), [removeEventListener](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/removeEventListener), [HTML body의 onload 연결](https://html.spec.whatwg.org/multipage/sections.html#the-body-element). 배운 기능의 뜻을 확인한 근거다. 예제·표·풀이 흐름은 수업 코드를 바탕으로 새로 작성했으며 외부 문장을 직접 인용하지 않았다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 스크립트.** [HTML 실행 파일](실습/책형_복습/15_JavaScript_DOM이벤트와_키보드스크롤제어.html)과 같은 폴더의 [JS 파일](실습/책형_복습/15_JavaScript_DOM이벤트와_키보드스크롤제어.js)을 함께 내려받는다. HTML을 브라우저로 열고 Console에서 결과를 확인한다. script는 필요한 HTML 뒤에 연결한다. 콘솔 출력은 페이지 본문에 자동으로 쓰이지 않는다.

**먼저 준비할 HTML · body 안:**

```html
    <button id="first" type="button">속성 방식</button>
    <button id="second" type="button">여러 함수</button>
    <button id="removed" type="button">제거된 등록</button>
    <p><label for="user">연습 아이디</label><input id="user"></p>
    <p><label for="password">연습 비밀번호</label><input id="password" type="password"></p>
    <button id="check" type="button">입력 확인</button>
    <p id="warning"></p><div id="view"></div>
```

```javascript
function writeLog(message) {
    const p = document.createElement('p');
    p.textContent = message;
    document.getElementById('view').prepend(p);
    console.log(message);
}
const first = document.getElementById('first');
first.onclick = function () { console.log('교체 전'); };
first.onclick = function () { console.log('교체 후'); };
const second = document.getElementById('second');
second.addEventListener('click', function () { console.log('첫째'); });
second.addEventListener('click', function () { console.log('둘째'); });
function removedHandler() { console.log('제거한 함수'); }
const removed = document.getElementById('removed');
removed.addEventListener('click', removedHandler);
removed.removeEventListener('click', removedHandler);
function checkInput() {
    const user = document.getElementById('user');
    const password = document.getElementById('password');
    const warning = document.getElementById('warning');
    if (user.value.trim() === '') {
        warning.textContent = '아이디는 필수';
    } else if (password.value.trim() === '') {
        warning.textContent = '비밀번호는 필수';
    } else {
        warning.textContent = '';
    }
    writeLog(warning.textContent === '' ? '입력 확인' : warning.textContent);
}
document.getElementById('check').addEventListener('click', checkInput);
```

파일을 열기만 하면 아직 Console 출력은 없다. **속성 방식 → 여러 함수 → 제거된 등록 → 빈 입력 확인 → 아이디에 student만 넣고 확인 → 비밀번호에 practice도 넣고 확인** 순서로 조작한다. 속성 방식은 뒤에 대입한 함수만 실행하고, 여러 함수 버튼은 등록한 두 함수를 차례로 실행한다. 제거된 등록 버튼은 아무것도 출력하지 않는다. 입력 확인을 세 번 마치면 현재 경고는 비어 있지만 view에는 과거 메시지 세 개가 남는다. 현재 경고와 과거 기록은 서로 다른 요소이기 때문이다. 두 입력값은 임의의 연습값이며 서버로 보내지 않는다.

**예상 출력 또는 관찰:**

```text
교체 후
첫째
둘째
아이디는 필수
비밀번호는 필수
입력 확인
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본의 일부다. 원본에 의존하는 앞 선언·HTML·함수는 다음 절의 연결까지 읽는다. 주석의 잘못된 표현도 원문대로 보존하고 설명에서 교정한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/asset/js/15_event.js` 17–29행

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

**발췌 바로 풀이:** init은 요소를 준비하고 bind를 호출한다. bind는 이벤트 등록 코드를 묶은 **우리가 만든 함수 이름**이며 브라우저가 자동 호출하는 특별한 이름이 아니다. 함수 안의 btn1은 맨 위 btn1과 별도의 지역 변수다. 처음 null이었던 변수가 저절로 버튼으로 바뀐 것이 아니다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/asset/js/15_event.js` 39–55행

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

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/asset/js/15_event.js` 57–63행

```javascript
    const btn4 = document.querySelector('#btn4')
    // btn4click() 으로 하면 실행이 되어버리는데, 실행이 되었을 때
    // 아래 btn4click 지역에 return이 없으므로 btn4click()가 'undefined'가 됨
    // 익명함수는 쓸 수 있지만 함수 자체를 넣으면 실행이 됨
    // remove는 event를 제거해주지만, 익명함수는 쉽게 제거할 수 없음
    btn4.addEventListener('click', btn4click)
    btn4.removeEventListener('click', btn4click)
```

**발췌 바로 풀이:** btn4click을 등록하고 같은 함수를 제거하므로 클릭해도 그 함수가 실행되지 않는다. 제거하는 것은 버튼이나 click 이벤트 자체가 아니라 **등록한 리스너**다. 강사님 주석의 ‘익명함수는 제거 못함’은 ‘참조를 보관하지 않고 등록하면 나중에 같은 함수를 지정하기 어렵다’로 고쳐 읽는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/asset/js/15_event.js` 87–104행

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

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/asset/js/15_event.js` 194–201행

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

**발췌 바로 풀이:** 양쪽은 같은 방식이다. log(message)는 div를 만들고 log 클래스를 붙여 #view의 첫 자식으로 넣는다. 나중 메시지가 위에 있으므로 **화면 위에서 아래로 읽는 순서가 시간순과 반대**다. 문자열 메시지 출력 목적이라면 div.innerHTML 대신 div.textContent = message를 쓰는 교정이 가능하다. 차이는 [12 콘텐츠](12_JavaScript_DOM_콘텐츠생성과_스타일조작.md)에서 읽는다.

내 init은 game의 시작 좌표를 left 10px·top 20px로 정한 뒤 bind를 호출한다. bind는 우리가 만든 함수 이름이며 브라우저 내장 기능이 아니다. 그 안의 버튼 1은 onclick을 두 번 대입하므로 두 번째 함수만 남는다. 버튼 2는 서로 다른 리스너 두 개를 등록하므로 클릭하면 두 출력이 나온다. 버튼 4는 등록 직후 같은 함수 참조로 제거하므로 해당 함수가 실행되지 않는다. 입력 검사에서는 비밀번호가 빈 조건인데 화면에 아이디 안내를 쓰는 복사 오류가 있다. 조건이 맞는지와 문구가 맞는지를 따로 읽어야 찾을 수 있다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

15_event.html의 script 경로 → asset/js/15_event.js 읽기 → load 시 init 호출 → 시작 좌표 준비 → bind에서 리스너 등록 → 사용자 클릭 → 콜백에서 현재 입력 읽기 → log(message) 호출 순서다. 아래 원본 log 정의는 div를 만들고 log 클래스를 붙인 뒤 메시지를 넣어 view.prepend로 추가한다. prepend는 맨 앞에 넣으므로 화면 위쪽이 최신 기록이다. Console의 시간순과 화면의 위아래 순서를 같은 것으로 읽지 않는다. 새 예제의 writeLog도 정의와 호출을 모두 보여 주며, 경고 메시지를 만드는 checkInput과 표시하는 writeLog의 역할을 나눴다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 등록·제거와 메시지 표시를 함수로 분리하여 같은 작업을 다시 사용할 수 있게 했다. **실제 오류:** 비밀번호가 빈 갈래의 아이디 안내를 비밀번호 안내로 바꿔야 한다. **설명 교정:** 익명 함수는 무조건 제거할 수 없는 것이 아니다. 같은 함수 참조를 보관하지 않고 새 익명 함수를 넘기면 기존 등록을 찾을 수 없다는 뜻이다. **공통 한계와 개선:** 양쪽 활성 코드에는 두 입력이 채워졌을 때 현재 경고를 비우는 else가 없다. 새 예제는 이 상태 처리를 보완한다. 경고를 비우는 것은 과거 로그 삭제나 실제 로그인 성공을 뜻하지 않는다.

개선안은 원본을 수정한 결과가 아니다. 실제 오류, 수업용 단순화, 목적에 따른 선택을 구별해 판단한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교

출처: `D:/workspace_teacher/workspace_html/javascript/asset/js/15_event.js` 65–76행

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

위 강사님 입력조건은 비밀번호가 비면 비밀번호문구를 써 내 복사 오류를 찾는 데 도움이 된다. 등록·로그함수는 같아 중복 인용하지 않는다. 두 HTML의 body onload와 window.onload를 독립 리스너 두 개로 계산하지 않는다. 같은 처리 속성과 연결되므로 정리할 때 한 곳을 유지하는 개선을 제안한다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 원본에 주는 입력 | 내 화면의 경고 | 해석 |
| --- | --- | --- |
| 둘 다 비움 | 아이디 필수 | 첫 번째 조건에서 처리 |
| 아이디만 입력 | 아이디 필수라는 잘못된 문구 | 비밀번호 조건 안의 복사 오류 |
| 둘 다 입력 | 이전 경고 유지 | else가 없어 기존 표시를 바꾸지 않음 |
| 버튼 4 클릭 | 새 출력 없음 | 리스너가 제거된 상태 |

trim()은 앞뒤 공백을 제거한 새 문자열을 반환한다. 원래 input.value를 자동으로 고치지는 않는다. 공백만 입력한 값을 검사할 때 도움이 되지만, 검사와 입력값 수정은 별도 작업이다.

**개인 학습 메모 연결:** 첨부 메모에서 적은 개발자 도구의 Event Listeners 패널은 등록 상태를 살펴볼 때 활용한다. 패널 확인과 실제 클릭 결과를 함께 관찰한다. 메모를 원본 코드의 일부나 인증 구현의 증거로 취급하지 않는다.

| 한 가지만 변경 | 예상 결과 | 확인하는 개념 |
| --- | --- | --- |
| first의 두 번째 대입 제거 | 교체 전 출력 | 첫 번째 속성 값이 유지됨 |
| removeEventListener 호출 제거 | 제거 버튼에서도 출력 | 등록이 남아 있음 |
| 성공 시 warning을 비우는 대입 제거 | 이전 경고가 남을 수 있음 | 등록 문제가 아닌 상태 갱신 문제 |

클릭 전부터 함수가 실행되면 등록 인수에 handler()처럼 괄호를 붙였는지 확인한다. 제거가 안 되면 등록했던 함수와 같은 참조를 넘기는지 본다. 요소가 null이면 선택자뿐 아니라 head에서의 실행 시점과 load 이후의 재선택도 확인한다. 문구가 틀리면 화면만 보지 말고 그 문구에 도달한 입력 조건부터 추적한다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** DOMContentLoaded·defer의 별도 로딩 전략·AbortController 리스너 관리·서버 인증은 추가 학습이다. 현재는 load·onclick·리스너등록/제거·입력 검사까지가 기본이다.



이 절의 확장은 기본 문제의 필수 조건이 아니다. 📚 출처가 있다는 것과 수업 밖 기능이라는 것은 다른 구분이다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. onclick에 두 번 대입하면 두 함수가 모두 쌓이는가?
2. 등록했던 함수를 제거하려면 어떤 값을 보관해야 하는가?
3. 현재 경고를 비우면 과거 메시지도 자동으로 없어지는가?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

같은 처리 속성은 뒤의 값으로 교체된다. 제거하려면 등록했던 함수 참조가 필요하다. warning과 view의 과거 자식 요소들은 다른 상태이므로 하나를 비운다고 다른 쪽이 자동으로 삭제되지 않는다.

</details>

| 단계 | 질문 |
| --- | --- |
| 등록 |함수값인가 |
| 제거 |같은참조인가 |
| 호출 |언제클릭했나 |
| 입력검사 |인증과구분했나 |

[장별 연습문제](실습/연습문제/15_JavaScript_DOM이벤트와_키보드스크롤제어_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [키보드·스크롤](15-02_JavaScript_키보드와_스크롤.md)이다.

<!-- 이전 색인 이동 주소 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
<a id="section-6"></a>
<a id="section-7"></a>

[이 장의 목차](#chapter-toc)에서 현재 설명을 찾는다.
