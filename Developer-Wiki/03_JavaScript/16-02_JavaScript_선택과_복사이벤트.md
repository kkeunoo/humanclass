# 16-02. 선택·복사·화면 크기 — 기본 동작과 이벤트 처리 구분하기

[JavaScript 목차](README.md) · [이전: 마우스·드래그](16_JavaScript_마우스이벤트와_드래그복사제어.md)

양쪽 `asset/js/16_event_mouse.js`의 선택·복사 처리와 resize 예제다. 이벤트 발생을 관찰하는 것과 브라우저의 기본 동작을 바꾸는 것을 구분한다.

<!-- chapter-toc -->

- [1. 우클릭 메뉴와 글자 선택](16-02_JavaScript_선택과_복사이벤트.md#section-1)
- [2. 선택한 글자 뒤에 출처 문구 붙이기](16-02_JavaScript_선택과_복사이벤트.md#section-2)
- [3. return과 preventDefault는 역할이 다르다](16-02_JavaScript_선택과_복사이벤트.md#section-3)
- [4. 창 안쪽 크기를 읽는 resize](16-02_JavaScript_선택과_복사이벤트.md#section-4)
- [5. 복습](16-02_JavaScript_선택과_복사이벤트.md#section-5)
- [추가로 알면 좋은 것](16-02_JavaScript_선택과_복사이벤트.md#section-6)

<a id="section-1"></a>

## 1. 우클릭 메뉴와 글자 선택

### 강사님 코드

출처: `teacher/workspace_html/javascript/asset/js/16_event_mouse.js` 20–27행 · **원본 발췌**

```javascript
    const area = document.querySelector('#area')
    area.oncontextmenu = () =>{
        alert('오른쪽 버튼 금지입니다')
        return false
    }
    area.onselectstart = function(){
        return false
    }
```

### 내 코드

출처: `me/workspace_html/javascript/asset/js/16_event_mouse.js` 21–32행 · **원본 발췌**

```javascript
    // 우클릭 하는 메뉴를 컨텍스트 메뉴라고 함
    const area = document.querySelector('#area')
    // contextmenu를 false로 주게되면 해당 영역은 우클릭 메뉴를 사용할 수 없음
    area.oncontextmenu = () => {
        alert('오른쪽 버튼 금지입니다')
        return false;
    }

    // selectstart로 해당 영역 드래그를 막을 수 있음
    area.onselectstart = function() {
        return false;
    }
```

oncontextmenu 함수는 안내창을 띄운 뒤 false를 반환하여 해당 메뉴의 기본 동작을 취소한다. onselectstart의 false는 글자 선택이 시작되는 기본 동작을 막는다. 내 주석의 ‘드래그 막기’는 여기서 **글자 선택 시작을 막기**로 정확히 읽는다. 앞 장에서 구현한 모든 요소 이동 기능을 금지하는 것은 아니다.

이 방식은 이벤트 처리 속성(on...)에 지정한 함수의 반환값을 사용한 것이다. addEventListener 콜백에서 return false만 쓰는 경우에도 똑같이 기본 동작이 취소된다고 외우지 않는다. 다음 절의 addEventListener 코드는 event.preventDefault()를 사용한다. 화면의 메뉴나 선택을 제한하는 실습이지 문서 내용을 복제할 수 없게 보호하는 장치는 아니다.

<a id="section-2"></a>

## 2. 선택한 글자 뒤에 출처 문구 붙이기

### 강사님 코드

출처: `teacher/workspace_html/javascript/asset/js/16_event_mouse.js` 29–43행 · **원본 발췌**

```javascript
    const area2 = document.querySelector('#area2')
    area2.addEventListener('copy', function(event){
        event.preventDefault()

        const selection = window.getSelection().toString()
        console.log(selection)
        if(selection.length == 0){
            return
        }

        const str = '[출처] www.naver.com'
        const result = selection + str

        event.clipboardData.setData('text/plain', result)
    })
```

### 내 코드

출처: `me/workspace_html/javascript/asset/js/16_event_mouse.js` 34–53행 · **원본 발췌**

```javascript
    const area2 = document.querySelector('#area2')
    // oncopy는 ctrl+c 등 복사할 때 발생하는 이벤트 (클립보드에 저장되는 것)
    area2.addEventListener('copy', function(event) {
        // preventDefault는 ctrl+c 등이 하는 기본을 막아주는 것
        event.preventDefault()
        
        // selection은 드래그를 했을 때 영역을 알려줌
        const selection = window.getSelection().toString()
        console.log(selection)
        if(selection.length == 0) {
            return
        }

        // 아래처럼 clipboard 영역에 str로 추가해주면, 출처가 붙어서 나옴
        const str = '[출처] www.naver.com'
        const result = selection + str

        // plain은 텍스트에 순수한 글씨, 거기에 result를 추가
        event.clipboardData.setData('text/plain', result)
    })
```

양쪽 로직은 같다. #area2에서 copy 이벤트가 발생하면 기본 복사를 취소하고 현재 선택된 글자를 문자열로 읽는다. 비어 있으면 함수를 끝내고, 글자가 있으면 정해 둔 출처 문구를 이어 붙여 복사 데이터를 지정한다.

```text
선택 글자 '복사 연습'
  + '[출처] www.naver.com'
  → '복사 연습[출처] www.naver.com'
```

원본에는 사이를 띄우거나 줄바꿈하는 문자가 없다. 결과를 보기 좋게 설명하려고 임의의 공백을 원본 결과에 넣지 않는다. www.naver.com은 원본의 고정 연습 문구이며 실제 출처를 자동으로 알아내는 코드가 아니다. 문자열을 붙인다고 그 사이트에 요청을 보내는 것도 아니다.

| 문장 | 역할 |
| --- | --- |
| event.preventDefault() | 브라우저의 기본 복사 동작 취소 |
| window.getSelection().toString() | 현재 문서에서 선택한 글자 읽기 |
| selection.length == 0 | 비어 있는 문자열 확인 |
| event.clipboardData.setData('text/plain', result) | 이번 복사 이벤트의 일반 텍스트 데이터 지정 |

preventDefault가 빈 선택 검사보다 먼저 실행된다. 따라서 빈 문자열이면 **기본 동작은 이미 취소했고 새 데이터는 쓰지 않은 채 종료**한다. 실행 순서를 바꾸어 설명하지 않는다. 이 API는 copy 이벤트가 전달한 데이터를 다루며, 별도의 navigator.clipboard API를 사용한 예제가 아니다. [MDN copy 이벤트](https://developer.mozilla.org/en-US/docs/Web/API/Element/copy_event)

<a id="section-3"></a>

## 3. return과 preventDefault는 역할이 다르다

return은 현재 함수 실행을 끝낸다. preventDefault는 취소 가능한 이벤트의 기본 동작을 취소한다. 원본의 return은 빈 선택일 때 아래 문자열 연결·setData를 실행하지 않도록 한다. 이벤트의 전파를 멈춘다는 뜻도 아니다. 전파 제어는 다음 17장 원본에서 별도로 읽는다.

15장의 Ctrl+C alert와 이 copy 처리의 차이도 여기서 정리할 수 있다. 전자는 키 조합을 보고 안내창만 띄우며, 후자는 copy 이벤트 안에서 기본 동작을 취소하고 복사할 데이터를 바꾼다.

<a id="section-4"></a>

## 4. 창 안쪽 크기를 읽는 resize

### 강사님 코드

출처: `teacher/workspace_html/javascript/asset/js/16_event_mouse.js` 113–118행 · **원본 발췌**

```javascript
    window.addEventListener('resize', function(evt){
        const w = window.innerWidth
        const h = window.innerHeight

        log(`w:${w}, h:${h}`)
    })
```

### 내 코드

출처: `me/workspace_html/javascript/asset/js/16_event_mouse.js` 138–145행 · **원본 발췌**

```javascript
    window.addEventListener('resize', function(evt) {
        // 아래와 같이 입력하면, w와 h에 브라우저 안쪽 width, height를 알 수 있음
        // 단, 스크롤 영역을 제외한 부분이기 때문에 그 부분까지면 아우터를 써야 함
        const w = window.innerWidth
        const h = window.innerHeight

        log(`화면w:${w}, 높이h:${h}`)
    })
```

창 크기가 바뀌면 가로·세로 값을 읽어 log에 표시한다. 숫자는 현재 환경에 따라 달라지므로 고정 정답으로 적지 않는다. 이벤트를 등록했다는 이유만으로 최초 한 번 자동 출력되는 것도 아니다.

innerWidth/innerHeight는 창 안쪽 뷰포트 크기이며, 표시되는 스크롤바 너비·높이를 포함할 수 있다. 내 주석의 ‘스크롤 영역을 제외하므로 포함하려면 outer’는 잘못된 설명이다. outerWidth/outerHeight는 브라우저 창의 바깥 크기로, 문서 전체 크기를 뜻하지 않는다. [MDN innerWidth](https://developer.mozilla.org/en-US/docs/Web/API/Window/innerWidth)

<a id="section-5"></a>

## 5. 복습

1. 원본에서 선택한 글자가 없을 때 setData가 실행되는가?
2. 문자열 '연습'을 복사할 때 원본이 설정하는 텍스트는?
3. getSelection과 clipboardData는 같은 정보인가?
4. innerHeight가 문서 전체 콘텐츠 높이인가?

<details>
<summary>정답</summary>

1. 아니다. preventDefault 뒤 return으로 끝난다.
2. '연습[출처] www.naver.com'이다.
3. 아니다. 전자는 선택 내용, 후자는 이번 이벤트의 복사 데이터를 다룬다.
4. 아니다. 창 안쪽 뷰포트 높이다.

</details>

<a id="section-6"></a>

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/16-02_JavaScript_선택과_복사이벤트_연습문제.md)

## 추가로 알면 좋은 것

navigator.clipboard의 읽기·쓰기와 권한 처리, 모바일 선택 UI까지 다루는 복사 도구는 추가 학습이다. 본문은 수업에서 쓴 copy 이벤트와 clipboardData 범위에 둔다.

