# 15-02. 키보드와 스크롤 — 키의 정보에서 위치 변경까지

[JavaScript 목차](README.md) · [읽기 안내](00_JavaScript_V3_동작_백과_읽기법.md)

브라우저는 키를 누르거나 화면을 움직일 때 이벤트 객체로 상황을 전달한다. 키 식별값을 검사하고 좌표 문자열을 계산하면 작은 이동 실습을 만들 수 있다. 키 입력·포커스·페이지 스크롤은 서로 영향을 줄 수 있어 조건을 따로 적는다.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

keydown·keyup·이벤트 객체를 구별한다. Enter로 포커스와 클릭 처리를 연결하고, 좌표를 10px씩 바꾸는 계산을 설명한다. 스크롤할 공간과 현재 위치, scrollTo 요청의 완료 시점을 구분한다.

입력·현재 상태·실행 순서·결과를 분리해 설명한다. 실제 수업 원본은 아래에 표시하고, 원본에 없는 선택 학습은 9절 TIP에 둔다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

keydown은 키를 누를 때, keyup은 놓을 때 발생한다. 브라우저는 처리 함수에 이벤트 객체를 전달한다. 함수의 매개변수 이름을 event에서 evt로 바꿔도 그 객체의 역할은 같다. 이벤트 객체는 “어떤 키였는가, 보조 키가 함께 눌렸는가” 같은 정보를 담는다.

원본의 keyCode는 숫자로 키를 식별한다. key는 Enter 같은 의미 문자열을 제공한다. keyCode를 모든 키의 ASCII 값이라고 외우면 안 된다. 현재는 권장되지 않는 오래된 API이지만, 수업 원본을 해석할 때는 그대로 읽고 원본 주석에도 있는 key와 비교한다.

| 정보·호출 | 역할 | 예 |
| --- | --- | --- |
| keyCode | 원본의 숫자 식별값 | Enter 13, 오른쪽 39 |
| key | 키의 의미 문자열 | 'Enter', 'ArrowRight' |
| ctrlKey·shiftKey·altKey | 보조 키 상태 | Ctrl이 함께 눌렸는지 |
| focus() | 입력 포커스 이동 | 아이디에서 비밀번호로 |
| click() | 요소의 클릭 처리 호출 | 버튼 처리 함수 실행 |

style.left는 인라인 스타일의 문자열이다. 원본은 먼저 '10px'를 대입해 시작값을 준비한다. parseInt('10px')로 숫자 10을 읽고, 10을 더한 뒤 'px'를 붙이면 '20px'가 된다. 문자열 '10px'에 숫자 10을 그대로 더해 만든 '10px10'은 원하는 좌표가 아니다.

scrollY는 현재 세로 스크롤 위치이고 scrollTo는 위치 변경 요청이다. behavior가 smooth이면 여러 순간에 걸쳐 이동하므로 호출 직후 이미 0에 도착했다고 단정하지 않는다. 내용이 화면보다 길어 움직일 여지가 있는지도 먼저 확인한다.

> 📚 **출처 · 본문 설명 확인:** [MDN KeyboardEvent.keyCode](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/keyCode), [KeyboardEvent.key](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key), [scrollTo](https://developer.mozilla.org/en-US/docs/Web/API/Window/scrollTo). 배운 기능의 뜻을 확인한 근거다. 예제·표·풀이 흐름은 수업 코드를 바탕으로 새로 작성했으며 외부 문장을 직접 인용하지 않았다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 스크립트.** [HTML 실행 파일](실습/책형_복습/15-02_JavaScript_키보드와_스크롤.html)과 같은 폴더의 [JS 파일](실습/책형_복습/15-02_JavaScript_키보드와_스크롤.js)을 함께 내려받는다. HTML을 브라우저로 열고 Console에서 결과를 확인한다. script는 필요한 HTML 뒤에 연결한다. 콘솔 출력은 페이지 본문에 자동으로 쓰이지 않는다.

**먼저 준비할 HTML · body 안:**

```html
    <p><label for="user">아이디 연습</label><input id="user"></p>
    <p><label for="pw">비밀번호 연습</label><input id="pw" type="password"></p>
    <button id="check" type="button">연습 확인</button>
    <div id="game">이동 상자</div>
    <p>스크롤 위치: <span id="position">0</span></p>
    <button id="top" type="button">맨 위로</button>
```

**위 파일 head의 style:**

```css
body { min-height: 250vh; } #game { position: relative; width: 100px; height: 40px; background: lightblue; } #top { position: fixed; right: 10px; bottom: 10px; }
```

```javascript
const game = document.getElementById('game');
game.style.left = '10px';
game.style.top = '20px';
document.body.addEventListener('keydown', function (event) {
    let changed = true;
    if (event.keyCode === 39) game.style.left = parseInt(game.style.left) + 10 + 'px';
    else if (event.keyCode === 37) game.style.left = parseInt(game.style.left) - 10 + 'px';
    else if (event.keyCode === 40) game.style.top = parseInt(game.style.top) + 10 + 'px';
    else if (event.keyCode === 38) game.style.top = parseInt(game.style.top) - 10 + 'px';
    else changed = false;
    if (changed) console.log(game.style.left, game.style.top);
});
document.getElementById('user').addEventListener('keyup', function (event) {
    if (event.keyCode === 13) document.getElementById('pw').focus();
});
document.getElementById('pw').addEventListener('keyup', function (event) {
    if (event.keyCode === 13) document.getElementById('check').click();
});
document.getElementById('check').addEventListener('click', function () {
    console.log('연습 확인');
});
window.addEventListener('scroll', function () {
    document.getElementById('position').textContent = window.scrollY;
});
document.getElementById('top').addEventListener('click', function () {
    window.scrollTo({ top: 0, behavior: 'smooth' });
});
```

페이지의 빈 곳에서 **오른쪽 → 아래 → 왼쪽 → 위**를 한 번씩 누른다. 좌표가 바뀌다가 시작값인 left 10px·top 20px로 돌아온다. 아이디 칸에서 Enter를 누르면 비밀번호 칸으로 포커스가 옮겨지고, 비밀번호 칸에서 Enter를 누르면 연습 확인 버튼의 클릭 처리를 호출한다. 아래로 스크롤한 뒤 맨 위로 버튼을 누르면 최종 위치가 0으로 돌아온다. 아래 Console 출력은 이 조작 순서의 결과다. 원본과 구별한 새 전체 예제이며 실제 로그인 기능은 아니다.

**예상 출력 또는 관찰:**

```text
20px 20px
20px 30px
10px 30px
10px 20px
연습 확인
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본의 일부다. 원본에 의존하는 앞 선언·HTML·함수는 다음 절의 연결까지 읽는다. 주석의 잘못된 표현도 원문대로 보존하고 설명에서 교정한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/asset/js/15_event.js` 124–142행

```javascript
        // id에서 enter를 했을 때 pw창으로 focus가 가도록 지정
        if(event.keyCode == 13) { // enter keyCode
            log('엔터 빵')
            const pw = document.querySelector('#pw')
            pw.focus()
        }

        if(event.ctrlKey && event.keyCode == 67) {// ctrl + c 복사방지
            alert('ctrl+c')
        }
    })

    document.querySelector('#pw').addEventListener('keyup', function(event) {
        if(event.keyCode == 13) {
            const login = document.querySelector('#login')
            // pw에서 enter를 칠 경우 login 버튼이 click되도록 설정
            login.click()
        }
    })
```

**발췌 바로 풀이:** id에서 Enter를 놓으면 pw.focus()로 입력할 위치를 옮긴다. pw에서 Enter를 놓으면 login.click()으로 앞 장의 클릭 처리 함수를 실행한다. id의 Enter 한 번으로 두 단계가 자동 완료되는 것으로 읽지 않는다. 비밀번호 칸에서 다시 Enter를 입력하는 흐름이다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/asset/js/15_event.js` 163–181행

```javascript
    document.querySelector('body').addEventListener('keydown', function(event) {
        // log(event.keyCode)
        const game = document.querySelector('#game')
        
        // const left = parseInt(game.style.top)
        // console.log(top)

        // style로 값을 바꿀 땐 항상 설정한 값만 가져올 수 있기 때문에
        // js에서 init에 한 번 더 선언한 뒤에 가져옴
        if(event.keyCode == 39) { // 오른쪽 키를 눌렀을 때 이미지가 10px 이동하도록 변경
            game.style.left = parseInt(game.style.left) + 10 + 'px'
        } else if(event.keyCode == 37) { // 왼쪽방향키
            game.style.left = parseInt(game.style.left) - 10 + 'px'
        } else if(event.keyCode == 40) { // 아랫방향키
            game.style.top = parseInt(game.style.top) + 10 + 'px'
        } else if(event.keyCode == 38) { // 윗방향키
            game.style.top = parseInt(game.style.top) - 10 + 'px'
        } 
    })
```

**발췌 바로 풀이:** 내 코드는 오른쪽뿐 아니라 왼쪽·아래·위도 처리한다. 배운 조건문과 px 문자열 변환을 적용한 확장이므로 이 풀이를 본문 기준으로 함께 남긴다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/asset/js/15_event.js` 144–161행

```javascript
    document.querySelector('#top').addEventListener('click', function(event) {
        // 현재 스크롤의 위치를 알 수 있는 document 커맨드
        // 스크롤바의 길이는 전체 길이에서 그만큼만 보고있다는 뜻
        console.log(document.documentElement.scrollTop)
        // document.documentElement.scrollTop = 0

        // window.scrollTo는 smooth 외에도 여러가지가 있음, 나중에 배울 제이슨?이라는 것
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        })
    })

    // window 자체에서 scroll이 움직일 때 마다 Y값을 알 수 있음
    // 스크롤이 더 없다가 내렸을 때 추가적으로 화면을 로딩하는 등 그때 사용해도 좋음
    window.addEventListener('scroll', function() {
        console.log('window.scrollY', window.scrollY)
    })
```

**발췌 바로 풀이:** document.documentElement.scrollTop은 이 표준 모드 문서의 루트 스크롤 위치, window.scrollY는 창의 세로 스크롤 위치를 읽는 데 쓴다. 맨 위에서는 보통 0이다. scrollTo에 top:0을 주어 위쪽으로 이동시키고 behavior:'smooth'로 부드럽게 이동하도록 요청한다. 최종 위치가 호출 즉시 0이라고 가정하지 않는다.

내 원본은 init에서 left 10px·top 20px로 시작하여 네 방향을 처리한다. 강사님은 left 20px·top 10px에서 시작하고 오른쪽만 처리한다. 나는 같은 조건문 방식을 다른 방향으로 확장한 것이다. 원본에서 Ctrl+C일 때 띄우는 alert는 안내창이다. 안내창을 띄웠다는 사실만으로 브라우저의 복사 기본 동작까지 취소했다고 설명하지 않는다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

HTML의 외부 script 연결 → load 때 init으로 좌표 준비 → bind에서 키 이벤트 등록 → 브라우저가 이벤트 객체 전달 → keyCode 검사 → 숫자 좌표 계산 → px 문자열 대입 순서다. 앞 장에서 정의를 확인한 log(message)는 DOM에 메시지를 쌓는 함수다. document.documentElement.scrollTop은 이 표준 모드 문서의 루트 스크롤 위치를, window.scrollY는 창의 현재 세로 위치를 관찰한다. scrollTo에 넘기는 중괄호는 JavaScript 객체 인수이며 JSON 문자열이 아니다. 객체 자체는 19장에서 다시 설명한다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 강사님의 오른쪽 이동을 네 방향 조건문으로 확장하여 입력과 결과를 연결했다. **설명 교정:** style에서 읽은 값이 외부 CSS까지 계산한 최종 스타일 전체라고 보지 않는다. **원본의 한계:** body에서 키 이벤트를 받으므로 입력 칸의 방향키도 상자를 움직일 수 있다. 방향키의 기본 스크롤과 화면 경계 제한도 별도로 처리하지 않았다. **개선 방향:** 우선 한 번에 10px 이동하는 조건과 계산을 이해한다. 지금 예제를 완성된 게임 조작기로 설명하지 않는다.

개선안은 원본을 수정한 결과가 아니다. 실제 오류, 수업용 단순화, 목적에 따른 선택을 구별해 판단한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



강사님 HTML은 높이가 300vh여서 스크롤할 영역이 있다. 내 파일의 해당 높이 규칙은 주석이다. 같은 동작을 비교할 때에는 원본을 고치는 대신 검수용 복사본에 긴 영역을 준비했다는 조건을 기록한다. 시작 좌표가 다른 것은 오류가 아니라 입력 조건 차이다. Enter와 스크롤의 핵심 코드는 같으므로 두 코드를 모두 반복 인용하지 않는다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 원본 비교 조건 | 강사님 | 내 코드 |
| --- | --- | --- |
| 시작 left / top | 20px / 10px | 10px / 20px |
| 오른쪽 한 번 후 | 30px / 10px | 20px / 20px |
| 구현한 방향 | 오른쪽 | 네 방향 |
| 긴 스크롤 영역 | 300vh | 관련 규칙이 주석 |

keyup만으로 붙여넣기를 포함한 모든 입력 변화를 감지한다고 일반화하지 않는다. Ctrl+C 안내가 뜬 사실과 복사 이벤트의 기본 동작을 취소한 것도 별개다. 스크롤 위치를 표시하는 글자와 실제로 스크롤할 수 있는 문서 높이 역시 구분한다.

| 한 가지만 변경 | 예상 결과 | 이유 |
| --- | --- | --- |
| 시작 left만 20px | 오른쪽 한 번 후 30px | 초기값만 바뀜 |
| body의 긴 높이 제거 | 내용이 짧으면 스크롤이 안 보임 | 움직일 공간이 없음 |
| 오른쪽 증가량만 5로 변경 | 한 번에 5px 이동 | 입력 횟수는 같고 이동량만 바뀜 |

parseInt 결과가 NaN이면 인라인 시작값을 준비했는지 확인한다. 입력 중에도 상자가 움직이면 이벤트가 body까지 전달되는 현재 처리 범위를 살핀다. 맨 위로 버튼을 눌러도 화면이 움직이지 않으면 코드 오류를 단정하기 전에 현재 위치와 스크롤할 여지가 있는지 확인한다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** requestAnimationFrame, 키 상태를 관리하는 게임 루프, 화면 경계와 입력 포커스를 함께 다루는 완성된 조작기는 추가 학습이다. keyCode 원본 해석은 보존하되, 새 코드의 API 선택은 지원 여부와 목적을 확인하여 결정한다.



이 절의 확장은 기본 문제의 필수 조건이 아니다. 📚 출처가 있다는 것과 수업 밖 기능이라는 것은 다른 구분이다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. 내 시작 좌표에서 오른쪽과 아래를 한 번씩 누르면 어디인가?
2. scrollTo의 객체 인수는 JSON 문자열인가?
3. Ctrl+C 안내창만으로 복사를 차단했다고 할 수 있는가?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

left 20px·top 30px다. scrollTo에는 문자열이 아닌 객체를 전달했다. 안내창과 기본 동작 취소는 별개이므로 복사 차단으로 단정할 수 없다.

</details>

| 확인 단계 | 질문 |
| --- | --- |
| 키 입력 | 어떤 식별값을 읽었나? |
| 좌표 계산 | 숫자 계산 후 단위를 붙였나? |
| 포커스 | focus와 click 중 무엇을 호출했나? |
| 스크롤 | 이동할 영역과 최종 위치가 있는가? |

[장별 연습문제](실습/연습문제/15-02_JavaScript_키보드와_스크롤_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [마우스](16_JavaScript_마우스이벤트와_드래그복사제어.md)다.

<!-- 이전 색인 이동 주소 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
<a id="section-6"></a>

[이 장의 목차](#chapter-toc)에서 현재 설명을 찾는다.
