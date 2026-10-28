# 16. 마우스 이벤트 — 좌표를 읽고 드래그 상태 유지하기

[JavaScript 목차](README.md) · [이전: 키보드·스크롤](15-02_JavaScript_키보드와_스크롤.md) · [다음: 선택·복사·화면 크기](16-02_JavaScript_선택과_복사이벤트.md)

기준은 양쪽 `16_event_mouse.html`과 `asset/js/16_event_mouse.js`다. 이벤트 등록과 log 함수는 [15장](15_JavaScript_DOM이벤트와_키보드스크롤제어.md)에 설명했다. 여기서는 같은 마우스 동작에서도 **좌표 기준과 현재 드래그 상태**에 따라 처리 결과가 달라지는 부분을 읽는다.

**마우스 좌표와 상태란?** 마우스가 움직인 위치를 숫자로 읽고, 버튼을 누르고 있는지 변수에 기억해 동작을 나누는 것이다. 아래는 원본 발췌가 아닌 **설명용 작은 예제**다.

```javascript
let isDrag = false;
document.addEventListener('mousedown', function () { isDrag = true; });
document.addEventListener('mouseup', function () { isDrag = false; });
document.addEventListener('mousemove', function (event) {
    if (isDrag) console.log(event.pageX);
});
```

누르지 않고 움직일 때는 출력되지 않고, 누른 채 움직일 때 문서 기준 가로 좌표가 출력된다. 원본은 이 상태와 누른 지점의 차이까지 이용해 요소의 위치를 계산한다.

<!-- chapter-toc -->

- [1. 누르기·놓기·클릭을 구분한다](16_JavaScript_마우스이벤트와_드래그복사제어.md#section-1)
- [2. 좌표 숫자보다 기준점을 먼저 본다](16_JavaScript_마우스이벤트와_드래그복사제어.md#section-2)
- [3. 들어오고 나갈 때 배경 바꾸기](16_JavaScript_마우스이벤트와_드래그복사제어.md#section-3)
- [4. 포인터를 따라오는 그림](16_JavaScript_마우스이벤트와_드래그복사제어.md#section-4)
- [5. 눌렀을 때만 움직이는 드래그](16_JavaScript_마우스이벤트와_드래그복사제어.md#section-5)
- [6. 요소 밖에서 놓는 경우의 한계](16_JavaScript_마우스이벤트와_드래그복사제어.md#section-6)
- [7. 복습](16_JavaScript_마우스이벤트와_드래그복사제어.md#section-7)
- [추가로 알면 좋은 것](16_JavaScript_마우스이벤트와_드래그복사제어.md#section-8)

<a id="section-1"></a>

## 1. 누르기·놓기·클릭을 구분한다

| 이벤트 | 원본에서 확인하는 동작 |
| --- | --- |
| mousedown | 마우스 버튼 누르기 |
| mouseup | 누른 버튼 놓기 |
| click | 클릭 성립 |
| dblclick | 빠른 두 번 클릭 성립 |
| mousemove | 포인터 이동 |

### 강사님 코드

출처: `teacher/workspace_html/javascript/asset/js/16_event_mouse.js` 45–56행 · **원본 발췌**

```javascript
    area2.addEventListener('dblclick', function(){
        log('더블클릭 발생')
    })

    area2.addEventListener('mousedown', function(){
        log('mousedown')
    })
    area2.addEventListener('mouseup', function(){
        log('mouseup')
    })
    area2.addEventListener('click', function(evt){
        log('click')
```

### 내 코드

출처: `me/workspace_html/javascript/asset/js/16_event_mouse.js` 55–73행 · **원본 발췌**

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

위 발췌는 click 함수의 첫 줄까지만 담았다. 좌표 출력과 닫는 부분은 다음 절의 원본 흐름으로 이어진다. 양쪽은 같은 이벤트를 등록한다. 같은 영역에서 일반적인 왼쪽 클릭은 mousedown → mouseup → click 순서를 관찰할 수 있다. log가 prepend하므로 화면에는 나중 출력이 위에 보인다.

내 주석의 dblclick ‘0.3초 이내’는 모든 환경의 고정 기준이 아니다. 더블클릭 판정 간격은 사용 환경에 영향을 받는다. 두 번 클릭할 때 개별 click도 발생하므로 dblclick만 발생한다고 읽지 않는다.

<a id="section-2"></a>

## 2. 좌표 숫자보다 기준점을 먼저 본다

### 강사님 코드

출처: `teacher/workspace_html/javascript/asset/js/16_event_mouse.js` 65–69행 · **원본 발췌**

```javascript
        log('offsetY : '+ evt.offsetY)
        log('pageY : '+ evt.pageY)
        log('clientY : '+ evt.clientY)
        log('screenY : '+ evt.screenY)
    })
```

### 내 코드

출처: `me/workspace_html/javascript/asset/js/16_event_mouse.js` 75–86행 · **원본 발췌**

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

| 좌표 | 기준 | 예제를 읽는 방법 |
| --- | --- | --- |
| offsetX / offsetY | 이벤트 대상 요소의 padding 가장자리 | 요소 안에서 누른 위치 |
| pageX / pageY | 문서 | 문서 전체 안의 위치 |
| clientX / clientY | 현재 보이는 뷰포트 | 스크롤로 바뀐 화면 안의 위치 |
| screenX / screenY | 화면 좌표계 | 창 바깥 화면 기준의 위치 |

예를 들어 세로 스크롤이 200이고 clientY가 50이면 일반적인 문서에서 pageY는 250이다. ‘page는 스크롤과 관계없다’는 말은 **기준이 문서라는 뜻**이지, 스크롤해도 현재 포인터의 pageY가 무조건 같은 숫자라는 뜻이 아니다.

원본 #area2에는 자식 요소가 없어 offset을 그 영역 안의 위치로 보기 쉽다. 자식이 생기면 이벤트 대상도 달라질 수 있으므로 무조건 리스너를 등록한 부모 기준이라고 일반화하지 않는다. 내 주석의 ‘evt 전달인자가 하나라 + 사용’도 구분한다. 여기서는 한 문자열 메시지를 받는 **log(message)**에 전달할 글자를 연결하려고 +를 쓴다. 이벤트 객체의 인수 개수 때문에 문자열 연결이 필요한 것은 아니다.

<a id="section-3"></a>

## 3. 들어오고 나갈 때 배경 바꾸기

### 강사님 코드

출처: `teacher/workspace_html/javascript/asset/js/16_event_mouse.js` 71–85행 · **원본 발췌**

```javascript
    // area2.addEventListener('mouseenter', function(evt){
    area2.addEventListener('mouseover', function(evt){
        log('mouseover')
        area2.style.backgroundColor = 'yellow'
    })
    // area2.addEventListener('mouseleave', function(evt){
    area2.addEventListener('mouseout', function(evt){
        log('mouseout')
        area2.style.backgroundColor = 'white'
    })

    area2.addEventListener('mousemove', function(evt){
        log('mousemove')
        log(`offsetX:${evt.offsetX}, offsetY:${evt.offsetY}`)
    })
```

### 내 코드

출처: `me/workspace_html/javascript/asset/js/16_event_mouse.js` 88–104행 · **원본 발췌**

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

활성 코드는 mouseover/mouseout이다. 들어오면 노랑, 나가면 흰색이고 이동할 때 좌표를 출력한다. 내 'moseover'는 로그 글자의 오타이며 이벤트 이름 자체는 올바른 mouseover다.

주석 처리된 mouseenter/mouseleave와 완전히 같은 기능은 아니다. mouseover/mouseout은 자식 사이 이동과 이벤트 전파의 영향을 받으며, mouseenter/mouseleave는 전파 방식이 다르다. 원본처럼 자식이 없는 영역에서 비슷해 보이는 결과와 API가 같다는 주장을 구분한다. [MDN mouseenter](https://developer.mozilla.org/en-US/docs/Web/API/Element/mouseenter_event)

<a id="section-4"></a>

## 4. 포인터를 따라오는 그림

### 강사님 코드

출처: `teacher/workspace_html/javascript/asset/js/16_event_mouse.js` 87–94행 · **원본 발췌**

```javascript
    document.querySelector('body').addEventListener('mousemove', function(evt){
        const game = document.querySelector('#game')

        game.style.top = evt.pageY+10 +'px'
        game.style.left = evt.pageX+10 +'px'

        // log(`Y:${evt.clientY}, X:${evt.clientX}`)
    })
```

### 내 코드

출처: `me/workspace_html/javascript/asset/js/16_event_mouse.js` 106–115행 · **원본 발췌**

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

양쪽 모두 #game의 위치를 page 좌표보다 오른쪽·아래 10px로 설정한다. pageX=100, pageY=200이면 left='110px', top='210px'다. 버튼을 누르는 조건이 없으므로 이 코드는 **드래그가 아니라 포인터 따라가기**다.

원본 CSS는 position:absolute이며 위치 기준을 새로 만드는 조상이 없다. 부모 배치가 달라지면 page 좌표를 그대로 left/top으로 쓰는 계산도 다시 확인해야 한다. 10px 간격은 이 실습에서 포인터 바로 아래를 그림이 가리지 않도록 둔 것이지 모든 겹침 문제를 해결하는 일반 규칙은 아니다.

<a id="section-5"></a>

## 5. 눌렀을 때만 움직이는 드래그

HTML의 #img는 이름과 달리 **div 요소**다. 내 HTML에 실제 이미지 태그를 넣는 줄은 주석 처리되어 있다. 원본이 무엇을 움직이는지부터 구분한다.

| 변수 | 최초 값 | 역할 |
| --- | --- | --- |
| _isDrag | false | 지금 드래그 중인지 |
| _offsetX | 0 | 눌렀던 가로 위치 |
| _offsetY | 0 | 눌렀던 세로 위치 |

언더바는 이름을 구분하려고 붙인 관례이며 자동으로 전역이나 비공개 변수가 되게 하는 문법이 아니다.

### 강사님 코드

출처: `teacher/workspace_html/javascript/asset/js/16_event_mouse.js` 96–111행 · **원본 발췌**

```javascript
    document.querySelector('#img').addEventListener('mousedown', function(evt){
        _isDrag = true
        _offsetX = evt.offsetX
        _offsetY = evt.offsetY
    })
    document.querySelector('#img').addEventListener('mouseup', function(evt){
        _isDrag = false
    })
    document.querySelector('body').addEventListener('mousemove', function(evt){
        const img = document.querySelector('#img')

        if(_isDrag){
            img.style.top = (evt.pageY - _offsetY) +'px'
            img.style.left = (evt.pageX - _offsetX) +'px'
        }
    })
```

### 내 코드

출처: `me/workspace_html/javascript/asset/js/16_event_mouse.js` 117–136행 · **원본 발췌**

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

1. #img에서 mousedown: _isDrag를 true로 바꾸고 누른 위치를 저장한다.
2. body에서 mousemove: true인 동안에만 새 위치를 계산한다.
3. #img에서 mouseup: false로 바꾸어 이동을 멈춘다.

예를 들어 누른 offsetX가 20이고 이동한 pageX가 150이면 원본 계산의 left는 130px이다. offset을 빼지 않으면 누른 지점과 상관없이 요소의 모서리가 포인터로 달라붙는다. 양쪽은 같은 계산이고, 내 저장 시점 주석은 변수의 필요성을 이해하기 좋다.

offset 기준과 left/top 기준은 테두리 등에서 미세한 차이가 날 수 있다. 원본 #img에는 1px 테두리가 있으므로 이 계산을 모든 CSS 구조에서 정확히 픽셀 일치하는 범용 드래그라고 설명하지 않는다.

<a id="section-6"></a>

## 6. 요소 밖에서 놓는 경우의 한계

양쪽은 mouseup을 #img에만 등록했다. 포인터가 그 요소를 벗어나 다른 곳에서 놓이면 _isDrag가 true로 남을 가능성이 있다. 강사님 코드도 같은 한계가 있으므로 학생만 잘못된 것으로 분류하지 않는다. 또 버튼 종류를 확인하지 않아 오른쪽 버튼으로 눌러도 상태를 켤 수 있다.

**배운 mouseup과 window 등록으로 교정한 부분 — 기존 #img mouseup 등록을 대신함**

```javascript
window.addEventListener('mouseup', function () {
    _isDrag = false
})
```

같은 페이지의 다른 요소에서 놓는 상황까지 받도록 범위를 넓힌다. 창 밖에서 놓기, 터치, 부모 좌표 변환까지 모두 해결한 코드는 아니다. 기본 학습에서는 원본 상태의 흐름과 이 한계를 구분한다.

<a id="section-7"></a>

## 7. 복습

1. #game과 #img는 각각 언제 움직이는가?
2. _offsetX=15, pageX=110일 때 원본 계산의 left는?
3. _isDrag가 false인 동안 body mousemove는 #img를 바꾸는가?
4. 내 코드가 출력하는 'moseover'는 이벤트 이름 오류인가?

<details>
<summary>정답</summary>

1. #game은 body의 포인터 이동 때, #img는 _isDrag가 true인 이동 때다.
2. '95px'다.
3. 아니다. #game의 별도 함수는 여전히 실행될 수 있다.
4. 아니다. 로그 문구 오타이며 등록 이벤트 이름은 mouseover다.

</details>

<a id="section-8"></a>

## 추가로 알면 좋은 것

Pointer Events, setPointerCapture, requestAnimationFrame 최적화와 터치까지 지원하는 드래그 구현은 추가편이다. 위 기본 문제를 풀기 위한 필수 기능으로 넣지 않는다.

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/16_JavaScript_마우스이벤트와_드래그복사제어_연습문제.md) → [다음: 선택과 복사](16-02_JavaScript_선택과_복사이벤트.md)

