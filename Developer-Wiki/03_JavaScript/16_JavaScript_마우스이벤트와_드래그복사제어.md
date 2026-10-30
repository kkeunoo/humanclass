# 16. 마우스와 드래그 — 좌표의 기준과 상태를 함께 읽기

[JavaScript 목차](README.md) · [읽기 안내](00_JavaScript_V3_동작_백과_읽기법.md)

마우스가 움직였다는 사실만으로는 무엇을 움직일지 결정할 수 없다. 현재 누르고 있는지, 어디를 눌렀는지, 좌표의 기준이 어디인지가 필요하다. 이 장은 하나의 드래그 동작을 상태 저장과 좌표 계산으로 나누어 설명한다.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

누르기·놓기·클릭을 구분하고 네 가지 좌표 기준을 비교한다. 포인터 따라가기와 드래그의 차이, 누른 위치를 빼는 이유, 요소 밖에서 놓았을 때의 한계를 설명한다.

입력·현재 상태·실행 순서·결과를 분리해 설명한다. 실제 수업 원본은 아래에 표시하고, 원본에 없는 선택 학습은 9절 TIP에 둔다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

드래그는 대체로 누르기 → 누른 상태로 이동 → 놓기의 흐름이다. 이벤트 함수는 서로 다른 순간에 실행되므로 다음 이동 함수가 이전 누름을 알 수 있도록 상태를 변수에 보관한다. isDrag는 지금 이동을 허용할지, offsetX·offsetY는 요소 안의 어느 지점을 잡았는지를 기억한다.

| 관찰 정보 | 기준·의미 | 읽을 때의 주의점 |
| --- | --- | --- |
| offsetX·offsetY | 이벤트 대상의 padding 가장자리 | 자식 요소가 대상이면 기준도 달라질 수 있음 |
| pageX·pageY | 문서 | 스크롤한 문서 위치까지 반영 |
| clientX·clientY | 현재 보이는 뷰포트 | 문서 전체 좌표와 다름 |
| screenX·screenY | 화면 좌표계 | 브라우저 내용 영역의 좌표가 아님 |

일반적인 문서에서 세로 스크롤이 200이고 clientY가 50이면 pageY는 250으로 생각할 수 있다. “page는 문서 기준”이라는 말은 같은 포인터의 숫자가 스크롤과 무관하게 고정된다는 뜻이 아니다.

요소의 왼쪽에서 20px 떨어진 지점을 잡았다고 하자. 포인터가 문서의 x=150으로 이동했을 때 요소의 왼쪽을 150으로 놓으면 잡았던 지점이 아니라 모서리가 손 아래로 튄다. 150-20=130으로 놓아야 잡은 지점이 포인터를 따라간다. 다만 이 계산은 위치 기준이 문서와 맞고 테두리가 없는 아래 작은 예제의 조건이다.

> 📚 **출처 · 본문 설명 확인:** [MDN pageX](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/pageX), [offsetX](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/offsetX), [mouseenter](https://developer.mozilla.org/en-US/docs/Web/API/Element/mouseenter_event). 배운 기능의 뜻을 확인한 근거다. 예제·표·풀이 흐름은 수업 코드를 바탕으로 새로 작성했으며 외부 문장을 직접 인용하지 않았다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 스크립트.** [HTML 실행 파일](실습/책형_복습/16_JavaScript_마우스이벤트와_드래그복사제어.html)과 같은 폴더의 [JS 파일](실습/책형_복습/16_JavaScript_마우스이벤트와_드래그복사제어.js)을 함께 내려받는다. HTML을 브라우저로 열고 Console에서 결과를 확인한다. script는 필요한 HTML 뒤에 연결한다. 콘솔 출력은 페이지 본문에 자동으로 쓰이지 않는다.

**먼저 준비할 HTML · body 안:**

```html
    <div id="drag">여기를 잡고 이동</div>
    <p>상자의 왼쪽 위에서 20px·20px 지점을 누르고 이동해 보세요.</p>
```

**위 파일 head의 style:**

```css
body { min-height: 800px; } #drag { position: absolute; left: 100px; top: 220px; width: 120px; height: 80px; background: lightblue; user-select: none; }
```

```javascript
const drag = document.getElementById('drag');
let isDrag = false;
let offsetX = 0;
let offsetY = 0;
drag.addEventListener('mousedown', function (event) {
    isDrag = true;
    offsetX = event.offsetX;
    offsetY = event.offsetY;
    console.log('시작', offsetX, offsetY);
});
document.body.addEventListener('mousemove', function (event) {
    if (isDrag) {
        drag.style.left = event.pageX - offsetX + 'px';
        drag.style.top = event.pageY - offsetY + 'px';
    }
});
window.addEventListener('mouseup', function () {
    if (isDrag) {
        isDrag = false;
        console.log('끝', drag.style.left, drag.style.top);
    }
});
```

스크롤이 0인 상태에서 상자 안의 문서 좌표 (120, 240)을 누르고 (220, 300)까지 옮긴 뒤 놓는다. 상자는 처음 (100, 220)에 있으므로 누른 위치는 (20, 20)이다. 마지막 좌표에서 이를 빼 left 200px·top 280px가 된다. 놓은 뒤 포인터만 더 움직여도 상자는 그대로다. 새 예제는 원본의 mouseup 범위를 window로 넓힌 개선안이며, 원본을 그대로 실행한 결과로 표시하지 않는다.

**예상 출력 또는 관찰:**

```text
시작 20 20
끝 200px 280px
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본의 일부다. 원본에 의존하는 앞 선언·HTML·함수는 다음 절의 연결까지 읽는다. 주석의 잘못된 표현도 원문대로 보존하고 설명에서 교정한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/asset/js/16_event_mouse.js` 55–73행

```javascript
    // 아래 실행함수들의 경우 해당 영역 내에서 눌렀을때만 작동함
    area2.addEventListener('dblclick', function() {
        // 0.3초 이내에 클릭이 두 번 발생했을 때 dblclick으로 알 수 있음
        log('더블클릭발생')
    })

    area2.addEventListener('mousedown', function() {
        // mouse가 눌렸을 때 확인 할 수 있음
        log('mousedown')
    })

    area2.addEventListener('mouseup', function() {
        // mouse가 올라왔을 때 확인 할 수 있음
        log('mouseup')
    })

    area2.addEventListener('click', function(evt) {
        // mouse가 클릭되었을 때 때 확인 할 수 있음
        log('click')
```

**발췌 바로 풀이:** 위 발췌는 click 함수의 첫 줄까지만 담았다. 좌표 출력과 닫는 부분은 다음 절의 원본 흐름으로 이어진다. 양쪽은 같은 이벤트를 등록한다. 같은 영역에서 일반적인 왼쪽 클릭은 mousedown → mouseup → click 순서를 관찰할 수 있다. log가 prepend하므로 화면에는 나중 출력이 위에 보인다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/asset/js/16_event_mouse.js` 75–86행

```javascript
        // evt전달인자가 하나기 때문에 , 대신 + 를 사용함
        // offsetY는 돔 0,0(좌상단) 기준으로 마우스가 어디서 클릭이 되었는지 나옴 (상대값)
        // 만약, 돔 위치가 이동하더라도 돔 안에서의 0,0이 적용
        log('offsetY : '+ evt.offsetY)
        // pageY의 경우 스크롤 관계 없이 문서 에서 0,0(좌상단) 기준 (절대값)
        log('pageY : '+ evt.pageY)
        // 서버에 접속할 수 있는 도구(client)의 0,0 기준
        // client는 page와 다르게 지금 보고있는 브라우저의 좌상단 기준
        log('clientY : '+ evt.clientY)
        // screen은 내가 보고 있는 화면(실제 모니터 참고) 좌상단 기준
        log('screenY : '+ evt.screenY)
    })
```

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/asset/js/16_event_mouse.js` 88–104행

```javascript
    // mouseenter와 mouseover 동일한 기능, 마우스가 올라오면
    // area2.addEventListener('mouseenter', function(evt) {
    area2.addEventListener('mouseover', function(evt) {
        log('moseover')
        area2.style.backgroundColor = 'yellow'
    })

    // area2.addEventListener('mouseleave', function(evt) {
    area2.addEventListener('mouseout', function(evt) {
        log('mouseout')
        area2.style.backgroundColor = 'white'
    })

    area2.addEventListener('mousemove', function(evt) {
        log('mousemove')
        log(`offsetX : ${evt.offsetX}, offsetY : ${evt.offsetY}`)
    })
```

**발췌 바로 풀이:** 활성 코드는 mouseover/mouseout이다. 들어오면 노랑, 나가면 흰색이고 이동할 때 좌표를 출력한다. 내 'moseover'는 로그 글자의 오타이며 이벤트 이름 자체는 올바른 mouseover다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/asset/js/16_event_mouse.js` 106–115행

```javascript
    document.querySelector('body').addEventListener('mousemove', function(evt) {
        const game = document.querySelector('#game')

        // 마우스 좌상단에 붙여놓았기 때문에, 1px정도 떨어뜨려놓아야 클릭이 됨
        // 그렇지 않고 붙여놓았을 때는 그림이 클릭하게 되는 효과이기 때문
        game.style.top = evt.pageY + 10 + 'px'
        game.style.left = evt.pageX + 10 + 'px'

        // log(`offsetX : ${evt.offsetX}, offsetY : ${evt.offsetY}`)
    })
```

**발췌 바로 풀이:** 양쪽 모두 #game의 위치를 page 좌표보다 오른쪽·아래 10px로 설정한다. pageX=100, pageY=200이면 left='110px', top='210px'다. 버튼을 누르는 조건이 없으므로 이 코드는 **드래그가 아니라 포인터 따라가기**다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/asset/js/16_event_mouse.js` 117–136행

```javascript
    // drag and drop 만들기
    document.querySelector('#img').addEventListener('mousedown', function(evt) {
        _isDrag = true
        // 눌렀을 때 X, Y값을 저장해두어야 하기 때문에 전역변수를 선언해서 저장
        _offsetX = evt.offsetX
        _offsetY = evt.offsetY
    })
    document.querySelector('#img').addEventListener('mouseup', function(evt) {
        // 마우스를 뗀다면 drag 하고있는것을 중단하기 위해 false로 변환
        _isDrag = false
    })

    document.querySelector('body').addEventListener('mousemove', function(evt) {
        const img = document.querySelector('#img')

        if(_isDrag) {
            img.style.top = (evt.pageY - _offsetY) + 'px'
            img.style.left = (evt.pageX - _offsetX) + 'px'
        }
    })
```

**발췌 바로 풀이:** 1. #img에서 mousedown: _isDrag를 true로 바꾸고 누른 위치를 저장한다.
2. body에서 mousemove: true인 동안에만 새 위치를 계산한다.
3. #img에서 mouseup: false로 바꾸어 이동을 멈춘다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/asset/js/16_event_mouse.js` 1–12행

```javascript
// 전역변수는 언더바처럼 따로 지정해주어도 좋음
let _isDrag = false
let _offsetX = 0
let _offsetY = 0

function log(message) {
    const div = document.createElement('div')
    div.classList.add('log')
    div.innerHTML = message
    const view = document.querySelector('#view')
    view.prepend(div)
}
```

원본은 두 이동 기능을 동시에 등록한다. game은 body의 mousemove 때마다 page 좌표에 10을 더해 따라오며, 버튼을 누르는 조건이 없다. 반면 img는 _isDrag가 true일 때만 움직인다. HTML의 img라는 ID는 실제로 div에 붙어 있다. 변수 이름만 보고 이미지 요소라고 판단하지 않는다. _offsetX와 _offsetY는 mousedown 때 저장하고 이후 mousemove에서 사용하므로 이벤트가 바뀌어도 유지되는 범위에 선언했다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

16_event_mouse.html의 외부 script → window.onload → bind 등록 → mousedown에서 상태와 누른 위치 저장 → body mousemove에서 조건 검사와 계산 → mouseup에서 상태 해제 순서다. 아래 함께 실은 log(message)는 div 생성·클래스 지정·innerHTML 대입·prepend를 수행한다. 원본의 화면 로그는 최신 항목이 위에 온다. 새 예제는 계산에 집중하려고 Console을 쓰며 외부 이미지 요청도 필요하지 않도록 색 상자로 구성했다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 누름 순간의 위치를 별도 변수로 저장한 주석은 상태가 왜 필요한지 드러낸다. **주석 교정:** dblclick의 간격을 모든 환경에서 0.3초로 고정하지 않는다. mouseenter와 mouseover도 완전히 같은 API는 아니다. **공통 한계:** 양쪽은 img에만 mouseup을 등록하여 밖에서 놓으면 상태가 남을 수 있다. 테두리와 부모의 위치 기준도 있으므로 범용 드래그 구현이라고 설명하지 않는다. **개선:** 배운 window의 mouseup으로 같은 페이지에서 놓는 범위를 넓혀 볼 수 있다. 창 밖에서 놓기와 터치까지 모두 해결한 것은 아니다.

개선안은 원본을 수정한 결과가 아니다. 실제 오류, 수업용 단순화, 목적에 따른 선택을 구별해 판단한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



두 원본의 드래그 계산과 해제 범위는 같아서 강사님 코드를 다시 싣지 않는다. 공통 한계를 학생만의 오류로 평가하지 않는다. 내 로그의 moseover는 출력 글자의 오타이며 등록한 이벤트 이름 mouseover는 맞다. mouseenter·mouseleave는 자식 사이 이동과 전파에서 mouseover·mouseout과 차이가 있다. 자식 없는 상자에서 비슷해 보였다는 관찰과 API가 같다는 결론을 나눈다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 순간 | isDrag | 저장·변경 내용 |
| --- | --- | --- |
| 처음 | false | 이동해도 좌표를 바꾸지 않음 |
| (120, 240)에서 누름 | true | offset (20, 20) 저장 |
| (220, 300)으로 이동 | true | left 200px, top 280px |
| 놓음 | false | 현재 위치 유지 |
| 이후 포인터만 이동 | false | 상자 위치 변화 없음 |

일반적인 왼쪽 클릭에서는 mousedown → mouseup → click을 관찰한다. 더블클릭에는 개별 click도 생기므로 dblclick만 발생한다고 생각하지 않는다. 원본에서 log에 문자열을 이어 붙이는 이유는 log(message)가 한 메시지를 받기 때문이며, 이벤트 매개변수가 하나여서 +를 써야 하는 것은 아니다.

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| offset을 빼지 않음 | 요소 모서리가 포인터로 이동 | 잡은 지점 보정이 사라짐 |
| if 조건 제거 | 누르지 않아도 따라옴 | 상태에 따른 제한이 사라짐 |
| window 대신 drag에 mouseup | 밖에서 놓을 때 해제를 놓칠 수 있음 | 이벤트 수신 범위가 좁아짐 |

움직일 때 튀면 좌표 기준과 offset 저장 시점을 확인한다. CSS에서 위치를 바꿀 수 있게 position을 지정했는지도 본다. 놓았는데 계속 움직이면 isDrag가 false로 바뀌었는지와 mouseup 등록 대상을 살핀다. 이름에 언더바를 붙였다고 자동으로 전역·비공개가 되는 것은 아니다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** Pointer Events, setPointerCapture, requestAnimationFrame 최적화와 터치 지원은 추가 학습이다. 이 장의 필수 설명은 수업에서 사용한 마우스 이벤트·상태 변수·좌표 계산으로 구성했다.



이 절의 확장은 기본 문제의 필수 조건이 아니다. 📚 출처가 있다는 것과 수업 밖 기능이라는 것은 다른 구분이다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. game의 따라가기와 img의 드래그는 언제 움직이는가?
2. offsetX가 15이고 pageX가 110이면 left는?
3. mouseup을 요소 밖에서 놓치면 어떤 상태가 남는가?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

game은 이동할 때마다, img는 드래그 상태가 true인 이동 때 움직인다. left는 95px다. 해제되지 않은 true가 남아 이후 이동에도 상자가 움직일 수 있다.

</details>

| 질문 | 확인 대상 |
| --- | --- |
| 언제 움직이나? | isDrag 조건 |
| 어디를 잡았나? | offset 저장 |
| 어디로 옮기나? | page 좌표에서 offset 빼기 |
| 언제 멈추나? | mouseup 범위 |

[장별 연습문제](실습/연습문제/16_JavaScript_마우스이벤트와_드래그복사제어_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [선택·복사](16-02_JavaScript_선택과_복사이벤트.md)다.

<!-- 이전 색인 이동 주소 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
<a id="section-6"></a>
<a id="section-7"></a>
<a id="section-8"></a>

[이 장의 목차](#chapter-toc)에서 현재 설명을 찾는다.
