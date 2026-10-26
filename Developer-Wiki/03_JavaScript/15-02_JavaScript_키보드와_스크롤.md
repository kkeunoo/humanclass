# 15-02. 키보드·스크롤 — 입력된 키와 화면 위치 연결하기

[JavaScript 목차](README.md) · [이전: 이벤트 등록](15_JavaScript_DOM이벤트와_키보드스크롤제어.md)

양쪽 `asset/js/15_event.js` 후반과 `15_event.html`의 스타일을 함께 읽는다. 등록 방식은 앞 장에 두고 여기서는 **어떤 이벤트에서 어떤 값을 바꾸는지** 살핀다.

<!-- chapter-toc -->

- [1. keydown과 keyup](#section-1)
- [2. Enter로 포커스 이동과 클릭 실행](#section-2)
- [3. 방향키로 위치를 10px 바꾸기](#section-3)
- [4. 스크롤 위치와 맨 위로 이동](#section-4)
- [5. 복습](#section-5)
- [추가로 알면 좋은 것](#section-6)

<a id="section-1"></a>

## 1. keydown과 keyup

keydown은 키를 누를 때, keyup은 키를 놓을 때 발생한다. 원본의 event는 브라우저가 콜백에 전달하는 이벤트 객체다. 변수 이름을 event나 evt로 바꿔도 같은 역할이다.

| 원본에서 보는 정보 | 의미 |
| --- | --- |
| event.keyCode | 원본이 사용한 키 식별 숫자 |
| event.key | 키의 의미를 나타내는 문자열; 원본에 출력 주석 있음 |
| event.ctrlKey | Ctrl 키가 눌린 상태인지 |
| event.shiftKey / altKey | Shift / Alt 상태; 원본에 출력 주석 있음 |

keyCode를 모든 키의 ASCII 값이라고 외우면 부정확하다. 환경 의존적인 오래된 API이며 현재는 권장되지 않는다. **수업 원본 해석은 keyCode로 유지**하고, 원본 주석에도 있는 key를 짧게 비교한다. 예를 들어 Enter 키는 event.key === 'Enter'로 판단할 수 있다. [MDN keyCode](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/keyCode)

<a id="section-2"></a>

## 2. Enter로 포커스 이동과 클릭 실행

### 강사님 코드

출처: `teacher/workspace_html/javascript/asset/js/15_event.js` 92–107행 · **원본 발췌**

```javascript
        if(event.keyCode == 13){    // 엔터
            log('엔터 빵')
            const pw = document.querySelector('#pw')
            pw.focus()
        }

        if(event.ctrlKey && event.keyCode == 67) { // ctrl + c
            alert('ctrl + c')
        }
    })
    document.querySelector('#pw').addEventListener('keyup', function(event){
        if(event.keyCode == 13){    // 엔터
            const login = document.querySelector('#login')
            login.click()
        }
    })
```

### 내 코드

출처: `me/workspace_html/javascript/asset/js/15_event.js` 124–142행 · **원본 발췌**

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

id에서 Enter를 놓으면 pw.focus()로 입력할 위치를 옮긴다. pw에서 Enter를 놓으면 login.click()으로 앞 장의 클릭 처리 함수를 실행한다. id의 Enter 한 번으로 두 단계가 자동 완료되는 것으로 읽지 않는다. 비밀번호 칸에서 다시 Enter를 입력하는 흐름이다.

Ctrl+C 조건은 alert를 띄우는 코드다. 내 주석처럼 **복사를 막는 구현은 아니다.** 실제 copy 이벤트 처리와 기본 동작 취소는 다음 마우스·복사 장에서 비교한다. 입력 확인도 keyup만으로 모든 변경을 감지한다고 확장하지 않는다. 붙여넣기 등 입력 변화는 이후 input 이벤트와 구분해 배운다.

<a id="section-3"></a>

## 3. 방향키로 위치를 10px 바꾸기

### 강사님 코드

출처: `teacher/workspace_html/javascript/asset/js/15_event.js` 121–133행 · **원본 발췌**

```javascript
    document.querySelector('body').addEventListener('keydown', function(event){

        log(event.keyCode)

        const game = document.querySelector('#game')
        log(game.style.left)

        if(event.keyCode == 39){ // 오른쪽
            // 20px + 10px : 20px10px
            game.style.left = (parseInt(game.style.left) + 10)+'px'
        }

    })
```

### 내 코드

출처: `me/workspace_html/javascript/asset/js/15_event.js` 163–181행 · **원본 발췌**

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

내 코드는 오른쪽뿐 아니라 왼쪽·아래·위도 처리한다. 배운 조건문과 px 문자열 변환을 적용한 확장이므로 이 풀이를 본문 기준으로 함께 남긴다.

| 항목 | 강사님 | 내 코드 |
| --- | --- | --- |
| init 직후 left / top | 20px / 10px | 10px / 20px |
| 오른쪽 한 번 | left 30px | left 20px |
| 왼쪽·위·아래 분기 | 없음 | 각 방향으로 10px씩 이동 |
| 화면 밖 이동 제한 | 없음 | 없음 |

양쪽 CSS에는 position:absolute가 있다. JavaScript의 init은 인라인 left·top을 다시 설정한다. CSS 규칙의 left가 element.style.left에 자동으로 복사되지는 않기 때문에, 원본은 계산할 인라인 값을 먼저 준비한 것이다. 내 코드의 최종 시작 위치는 CSS의 20px/10px가 아니라 init이 설정한 10px/20px다.

`'20px' + 10`은 '20px10'이므로 parseInt로 숫자를 얻어 더한 후 'px'를 붙인다. 자세한 변환 비교는 [12-03 스타일](12-03_JavaScript_DOM_스타일과_퀴즈.md)에 있다.

이벤트를 body에 등록했기 때문에 입력 칸에서 누른 방향키도 body까지 전달되어 그림이 움직일 수 있다. 원본에는 입력 중 이동 제외나 기본 스크롤 취소가 없다. 의도한 게임 전용 조작으로 완성되었다고 설명하지 않는다. 이벤트 전파는 17장에서 해당 수업 코드와 함께 다룬다.

<a id="section-4"></a>

## 4. 스크롤 위치와 맨 위로 이동

### 강사님 코드

출처: `teacher/workspace_html/javascript/asset/js/15_event.js` 109–119행 · **원본 발췌**

```javascript
    document.querySelector('#top').addEventListener('click', function(event){
        console.log( document.documentElement.scrollTop )
        // document.documentElement.scrollTop = 0
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        })
    })
    window.addEventListener('scroll', function(){
        console.log('window.scrollY', window.scrollY)
    })
```

### 내 코드

출처: `me/workspace_html/javascript/asset/js/15_event.js` 144–161행 · **원본 발췌**

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

document.documentElement.scrollTop은 이 표준 모드 문서의 루트 스크롤 위치, window.scrollY는 창의 세로 스크롤 위치를 읽는 데 쓴다. 맨 위에서는 보통 0이다. scrollTo에 top:0을 주어 위쪽으로 이동시키고 behavior:'smooth'로 부드럽게 이동하도록 요청한다. 최종 위치가 호출 즉시 0이라고 가정하지 않는다.

`{ top: 0, behavior: 'smooth' }`는 JavaScript 객체를 인수로 전달한 것이다. 내 주석의 JSON 추측과 구분한다. 객체와 JSON 문자열은 이후 19장에서 자세히 비교한다.

강사님 HTML의 body는 height:300vh라 스크롤을 관찰하기 쉽다. 내 HTML에서는 이 규칙이 주석 처리되어 있다. 내용이 화면보다 짧으면 내려갈 여지가 없어 스크롤 코드가 있어도 눈에 띄는 이동이 없을 수 있다. 같은 조건에서 비교하려면 내 검수 복사본에만 해당 수업 CSS를 다시 적용했다고 표시한다.

<a id="section-5"></a>

## 5. 복습

1. 내 원본에서 오른쪽·아래를 한 번씩 누르면 left/top은?
2. body의 keydown은 입력 칸에서 발생한 키도 받을 수 있는가?
3. scrollTo의 중괄호 부분은 JSON 문자열인가?
4. Ctrl+C 때 alert가 뜨면 복사가 차단되었다고 볼 수 있는가?

<details>
<summary>정답</summary>

1. 시작 10px/20px에서 20px/30px다. 위치는 각각 left/top 순서다.
2. 원본에서는 그렇다. 전파되어 body의 함수도 실행될 수 있다.
3. 아니다. JavaScript 객체다.
4. 아니다. 원본은 안내창을 띄울 뿐 copy 기본 동작을 취소하지 않는다.

</details>

<a id="section-6"></a>

## 추가로 알면 좋은 것

requestAnimationFrame을 이용한 부드러운 이동, 키 누름 상태를 계속 관리하는 게임 루프, 화면 경계·입력 포커스까지 다루는 완성형 컨트롤러는 추가 학습이다. 원본의 한 번 입력에 10px 이동하는 코드와 구분한다.

