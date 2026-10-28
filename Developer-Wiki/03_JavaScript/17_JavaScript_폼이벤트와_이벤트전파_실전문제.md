# 17. 폼 이벤트 — 입력 변화와 제출 시점 구분하기

[JavaScript 목차](README.md) · [이전: 복사 이벤트](16-02_JavaScript_선택과_복사이벤트.md) · [다음: 이벤트 전파·위임](17-02_JavaScript_이벤트전파와_위임.md) · [주문·로그인·피자 실습](17-03_JavaScript_주문_로그인_피자실습.md) · [메뉴·Todo 실습](17-04_JavaScript_메뉴와_Todo실습.md)

양쪽 `17_event_form.html`과 `asset/js/17_event_form.js`를 기준으로 한다. 입력·제출의 기본 흐름을 이 장에서 읽고, 실제 수업 문제는 [주문·로그인·피자](17-03_JavaScript_주문_로그인_피자실습.md)와 [메뉴·Todo](17-04_JavaScript_메뉴와_Todo실습.md)에서 강사님·내 코드를 비교한다. 외부 전송 주소를 로컬 수신 페이지로 바꾼 검수본에서 양쪽 폼의 입력 길이 검사와 제출값을 확인했다.

**폼 이벤트란?** 입력 칸에 초점이 오거나 글자가 바뀌고, 사용자가 제출을 시도할 때 발생하는 일이다. 아래는 원본 발췌가 아닌 **설명용 작은 예제**다.

```html
<input id="query">
<script>
  const query = document.querySelector('#query');
  query.addEventListener('input', function () {
    console.log(query.value);
  });
</script>
```

사용자가 `가`를 입력하면 `가`, 이어 `나`를 입력하면 `가나`가 출력된다. 원본은 이 변화 기록에 더해 초점 변화와 제출 시 길이 검사를 다룬다.

<!-- chapter-toc -->

- [1. 어떤 시점에 실행할까](17_JavaScript_폼이벤트와_이벤트전파_실전문제.md#section-1)
- [2. submit 이벤트와 form.submit()은 다르다](17_JavaScript_폼이벤트와_이벤트전파_실전문제.md#section-2)
- [3. 검사한 문자열과 제출한 문자열](17_JavaScript_폼이벤트와_이벤트전파_실전문제.md#section-3)
- [4. 입력 로그는 글자 출력으로 교정할 수 있다](17_JavaScript_폼이벤트와_이벤트전파_실전문제.md#section-4)
- [5. 복습](17_JavaScript_폼이벤트와_이벤트전파_실전문제.md#section-5)
- [추가로 알면 좋은 것](17_JavaScript_폼이벤트와_이벤트전파_실전문제.md#section-6)

<a id="section-1"></a>

## 1. 어떤 시점에 실행할까

| 이벤트 | 이 원본에서 맡은 일 |
| --- | --- |
| focus | 검색 입력 칸에 초점이 오면 노란 배경 |
| blur | 초점을 잃으면 지정했던 배경 제거 |
| input | 사용자가 내용을 바꾸면 현재 값 기록·무작위 색 |
| submit | 검색 폼을 제출하려 할 때 길이 검사 |

### 강사님 코드

출처: `teacher/workspace_html/javascript/asset/js/17_event_form.js` 14–31행 · **원본 발췌**

```javascript
    const query = document.querySelector('#query')
    query.addEventListener('focus', function(){
        query.style.background = 'yellow'
    })
    query.addEventListener('blur', function(){
        query.style.background = ''
    })
    // input: 값이 변경될 때
    query.addEventListener('input', function(){
        log(query.value)

        const r = parseInt(Math.random() * 256)
        const g = parseInt(Math.random() * 256)
        const b = parseInt(Math.random() * 256)
        const a = Math.random()

        query.style.backgroundColor = `rgba(${r}, ${g}, ${b}, ${a})`
    })
```

### 내 코드

출처: `me/workspace_html/javascript/asset/js/17_event_form.js` 13–34행 · **원본 발췌**

```javascript
    const query = document.querySelector('#query')
    // focus는 초점이 가있을 때, blue는 초점을 잃었을 때
    // 아래와 같은 부분은 textbox를 클릭했을 때와 밖으로 나왔을 때
    query.addEventListener('focus', function() {
        query.style.backgroundColor = 'yellow'
    })
    query.addEventListener('blur', function() {
        query.style.backgroundColor = ''
    })
    // input은 텍스트 자체가 바뀌는걸 감지하기 때문에, 마우스 우클릭으로
    // 붙여넣기 해도 값이 들어가면 감지하는 이벤트
    query.addEventListener('input', function() {
        log(query.value)

        const r = parseInt(Math.random() * 256)
        const g = parseInt(Math.random() * 256)
        const b = parseInt(Math.random() * 256)
        const a = Math.random()

        query.style.backgroundColor = `rgba(${r}, ${g}, ${b}, ${a})`

    })
```

강사님은 focus/blur에서 background, 나는 backgroundColor를 쓴다. background는 배경 관련 값을 묶는 속성이고 backgroundColor는 색상 속성이다. 별도 배경 이미지가 없는 이 원본에서는 초점 시 노랑, 잃으면 지정값 제거라는 결과가 같다. 내 주석의 'blue'는 **blur**의 오타다.

input은 keyup과 다르다. 사용자가 입력 내용을 바꾸는 동작을 다루므로 키보드 입력뿐 아니라 붙여넣기 같은 변경에도 연결된다. 반대로 JavaScript로 query.value를 대입했다는 이유만으로 input 이벤트가 자동 발생하지는 않는다. [MDN input 이벤트](https://developer.mozilla.org/en-US/docs/Web/API/Element/input_event)

색상 r·g·b는 각각 0–255 정수, a는 0 이상 1 미만의 수다. 입력할 때마다 다시 뽑으므로 특정 색이 정답은 아니다. focus의 노란색은 input의 새 색상으로 덮일 수 있다. blur에서 빈 문자열을 넣으면 해당 인라인 배경 지정을 지우는 것이며, 모든 상황에서 반드시 흰색을 지정한다는 뜻은 아니다.

<a id="section-2"></a>

## 2. submit 이벤트와 form.submit()은 다르다

HTML은 method="get", action에 검색 주소, target="_blank"를 지정하고 검색 input의 name을 query로 둔다. 유효한 입력은 원본 동작상 새 창 또는 탭의 검색 요청에 사용된다. 검수에서는 외부 검색 전송 대신 action을 로컬 수신 페이지로, target을 로컬 iframe으로 바꾸어 확인했다.

### 강사님 코드

출처: `teacher/workspace_html/javascript/asset/js/17_event_form.js` 33–44행 · **원본 발췌**

```javascript
    const form = document.querySelector('#form')
    form.addEventListener('submit', function(event){

        // 태그의 기본(고유) 기능을 막아준다
        event.preventDefault()

        if(query.value.trim().length < 2){
            alert('검색어는 두 글자 이상입니다')
        } else {
            form.submit()
        }
    })
```

### 내 코드

출처: `me/workspace_html/javascript/asset/js/17_event_form.js` 37–48행 · **원본 발췌**

```javascript
    const form = document.querySelector('#form')
    form.addEventListener('submit', function(event){
        
        // prevent는 태그의 기본 고유 기능을 막는다는 함수 (submit 등)
        event.preventDefault()

        if(query.value.trim().length < 2) {
            alert('검색어는 두 글자 이상입니다.')
        } else {
            form.submit()
        }
    })
```

두 로직은 같고 alert 문구의 마침표만 다르다. 먼저 기본 제출을 취소한다. trim한 문자열 길이가 2 미만이면 안내창을 띄우고, 조건을 통과하면 form.submit()으로 직접 제출한다.

**로컬 화면 확인:** 강사님·내 코드 모두 `a` 한 글자 입력 시 안내창이 뜨고 수신 페이지는 바뀌지 않았다. `  ab  ` 입력 시 수신 페이지 주소의 `query=++ab++`로 앞뒤 공백이 전달됐다. 이는 `trim()`이 원래 입력값을 수정하지 않는다는 설명과 일치한다. 검수 페이지의 주소와 대상만 바꿨으며 실제 외부 검색 서비스로는 전송하지 않았다.

```text
사용자가 제출
  → submit 이벤트 함수
  → 기본 제출 취소
  → 검사 실패: 안내창 / 검사 성공: form.submit()
```

form.submit()은 submit 이벤트 함수를 다시 실행하지 않으므로 이 원본이 계속 자기 자신을 부르는 구조는 아니다. 브라우저의 기본 제약 검증도 거치지 않는 직접 제출 메서드라는 점을 함께 기억한다. [MDN form.submit](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/submit)

<a id="section-3"></a>

## 3. 검사한 문자열과 제출한 문자열

| 입력 예 | trim 후 길이 | 원본 판단 |
| --- | --- | --- |
| 빈 값·공백만 | 0 | 안내창, 제출 안 함 |
| '가' | 1 | 안내창, 제출 안 함 |
| '  가  ' | 1 | 안내창, 제출 안 함 |
| '가나' | 2 | 직접 제출 |
| '  가나  ' | 2 | 직접 제출, 앞뒤 공백은 value에 남음 |

trim은 검사에 쓴 반환값만 만든다. 원본에 query.value를 바꾸는 대입은 없으므로 실제 제출값에서 공백도 자동 제거되었다고 설명하지 않는다. 또한 문자열 length는 모든 문자의 눈에 보이는 개수를 항상 뜻하지는 않는다. 이 실습의 일반 한글·영문 입력 기준과 이모지 등의 세부 문자 처리 구현을 구분한다.

<a id="section-4"></a>

## 4. 입력 로그는 글자 출력으로 교정할 수 있다

log(query.value)는 입력된 문자열을 원본 log 함수의 innerHTML에 넣는다. 사용자가 태그 모양의 문자열을 넣으면 HTML로 해석될 수 있다. 값 관찰 목적이라면 [15장의 log 교정](15_JavaScript_DOM이벤트와_키보드스크롤제어.md)을 따라 div.textContent = message로 바꾼다. 같은 위험 설명을 이 장에서 새 보안 도구 구현으로 늘리지 않는다.

<a id="section-5"></a>

## 5. 복습

1. focus로 노란 배경이 되었는데 입력 후 색이 달라지는 이유는?
2. query.value = '가나'만 실행하면 input 함수도 자동 실행되는가?
3. form.submit()이 현재 submit 이벤트 함수를 다시 부르는가?
4. '  가나  '를 검사한 뒤 제출하면 공백이 자동 제거되는가?

<details>
<summary>정답</summary>

1. input 함수가 새 rgba 색상으로 지정하기 때문이다.
2. 아니다. 프로그램에 의한 value 대입과 사용자 입력 이벤트를 구분한다.
3. 아니다. 직접 제출 메서드다.
4. 아니다. 원본은 trim 결과로 길이만 검사하고 value는 바꾸지 않는다.

</details>

<a id="section-6"></a>

## 추가로 알면 좋은 것

requestSubmit, validity API로 구성한 전체 검증 도구, 세밀한 유니코드 글자 수 계산은 추가 학습이다. 본문은 원본의 focus·blur·input·submit, trim·length 검사 범위에 둔다.

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/17_JavaScript_폼이벤트와_이벤트전파_실전문제_연습문제.md) → [다음: 이벤트 전파와 위임](17-02_JavaScript_이벤트전파와_위임.md)

