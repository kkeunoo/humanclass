# 17. 폼 이벤트 — 입력을 관찰하고 제출을 판단하는 시점

[JavaScript 목차](README.md) · [읽기 안내](00_JavaScript_V3_동작_백과_읽기법.md)

검색 입력 칸에 글자를 쓰는 순간과 검색 버튼으로 제출하는 순간은 다르다. 입력 중의 반응과 제출 전 검사를 한 함수로 뭉치지 않고, 각 이벤트가 어느 시점의 값을 읽는지 따라가 보자.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

focus·blur·input·submit을 구분하고 trim한 검사값과 원래 value의 차이를 설명한다. 직접 제출 메서드와 submit 이벤트의 관계, 무작위 색의 범위, 입력 로그의 표시 방법을 읽는다.

입력·현재 상태·실행 순서·결과를 분리해 설명한다. 실제 수업 원본은 아래에 표시하고, 원본에 없는 선택 학습은 9절 TIP에 둔다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

폼은 사용자의 입력값을 묶어 제출할 수 있는 HTML 요소다. input은 값을 담고, name은 제출할 값의 이름, action은 보낼 주소, method는 제출 방식이다. JavaScript에서 input을 ID로 선택하는 것과 서버로 보낼 이름을 name으로 정하는 것은 역할이 다르다.

| 사건 | 실행 시점 | 원본의 처리 |
| --- | --- | --- |
| focus | 입력 칸에 초점이 옴 | 노란 배경 |
| blur | 입력 칸에서 초점이 떠남 | 지정한 인라인 배경 제거 |
| input | 사용자 동작으로 값이 바뀜 | 값 기록·무작위 색 지정 |
| submit | 폼 제출을 시도함 | 기본 제출 취소 후 길이 검사 |

input 이벤트는 키를 놓는 keyup과 다르다. 사용자 붙여넣기 같은 값 변경도 다룬다. 반대로 query.value='가나'처럼 프로그램에서 값을 대입했다고 input 리스너가 저절로 실행되지는 않는다.

query.value.trim().length에서 먼저 현재 문자열을 읽고, 앞뒤 공백을 없앤 새 문자열을 얻어 길이를 검사한다. 원래 query.value는 그대로다. 검사에 쓴 문자열과 제출하는 문자열이 자동으로 같아진다고 생각하면 안 된다.

> 📚 **출처 · 본문 설명 확인:** [MDN input 이벤트](https://developer.mozilla.org/en-US/docs/Web/API/Element/input_event), [form.submit](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/submit). 배운 기능의 뜻을 확인한 근거다. 예제·표·풀이 흐름은 수업 코드를 바탕으로 새로 작성했으며 외부 문장을 직접 인용하지 않았다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 스크립트.** [HTML 실행 파일](실습/책형_복습/17_JavaScript_폼이벤트와_이벤트전파_실전문제.html)과 같은 폴더의 [JS 파일](실습/책형_복습/17_JavaScript_폼이벤트와_이벤트전파_실전문제.js)을 함께 내려받는다. HTML을 브라우저로 열고 Console에서 결과를 확인한다. script는 필요한 HTML 뒤에 연결한다. 콘솔 출력은 페이지 본문에 자동으로 쓰이지 않는다.

**먼저 준비할 HTML · body 안:**

```html
    <form id="form">
        <label for="query">검색어 연습</label><input id="query" name="query">
        <button type="submit">검사</button>
    </form>
    <p id="message"></p>
```

```javascript
const form = document.getElementById('form');
const query = document.getElementById('query');
const message = document.getElementById('message');
query.addEventListener('focus', function () {
    query.style.backgroundColor = 'yellow';
});
query.addEventListener('blur', function () {
    query.style.backgroundColor = '';
});
query.addEventListener('input', function () {
    console.log('입력', query.value);
});
form.addEventListener('submit', function (event) {
    event.preventDefault();
    const checked = query.value.trim();
    if (checked.length < 2) {
        message.textContent = '두 글자 이상 입력';
    } else {
        message.textContent = '검사 통과, 원래 값: [' + query.value + ']';
    }
    console.log(message.textContent);
});
```

가를 입력하고 검사 버튼을 누른 뒤, 앞뒤 공백 두 칸씩 있는 가나로 바꾸고 다시 누른다. 아래 입력 로그는 각 문자열로 한 번에 교체한 경우다. 직접 한 글자씩 타이핑하면 input이 여러 번 발생하므로 중간 로그도 더 생긴다. 새 예제는 외부 전송 대신 화면에 검사 결과만 표시한다. 원본의 form.submit()까지 그대로 실행한 예제가 아님을 구분한다. 마지막 대괄호 안의 공백은 원래 value가 남았다는 관찰 표시다.

**예상 출력 또는 관찰:**

```text
입력 가
두 글자 이상 입력
입력   가나  
검사 통과, 원래 값: [  가나  ]
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본의 일부다. 원본에 의존하는 앞 선언·HTML·함수는 다음 절의 연결까지 읽는다. 주석의 잘못된 표현도 원문대로 보존하고 설명에서 교정한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/asset/js/17_event_form.js` 13–34행

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

**발췌 바로 풀이:** 강사님은 focus/blur에서 background, 나는 backgroundColor를 쓴다. background는 배경 관련 값을 묶는 속성이고 backgroundColor는 색상 속성이다. 별도 배경 이미지가 없는 이 원본에서는 초점 시 노랑, 잃으면 지정값 제거라는 결과가 같다. 내 주석의 'blue'는 **blur**의 오타다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/asset/js/17_event_form.js` 37–48행

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

**발췌 바로 풀이:** 두 로직은 같고 alert 문구의 마침표만 다르다. 먼저 기본 제출을 취소한다. trim한 문자열 길이가 2 미만이면 안내창을 띄우고, 조건을 통과하면 form.submit()으로 직접 제출한다.

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

내 코드는 초점이 오면 backgroundColor를 노랑으로, 떠나면 빈 문자열로 바꾼다. 주석의 blue는 blur의 오타다. input 안에서는 0~255 정수 r·g·b와 0 이상 1 미만의 a를 새로 뽑아 rgba 색을 만든다. 따라서 focus의 노랑이 입력 중 다른 색으로 바뀔 수 있으며 특정 색을 고정 정답으로 삼지 않는다. submit에서는 먼저 기본 제출을 취소한 뒤 trim한 길이가 2 미만이면 안내하고, 통과하면 form.submit()으로 직접 제출한다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

17_event_form.html의 form·query·제출 버튼 → load 뒤 리스너 등록 → 사용자 입력 때 input → 제출 시도 때 submit → preventDefault → 길이 판단 → 원본의 직접 제출 또는 실패 안내 순서다. 원본 log(query.value)는 아래 log 정의로 이어져 입력을 innerHTML에 넣는다. 값 관찰 목적이면 이미 배운 textContent로 바꾸는 개선이 적절하다. 새 예제는 message.textContent를 사용하며 별도 파일의 정의를 숨기지 않는다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 사용자의 값 변경과 제출 검사를 이벤트로 분리했고 공백만 입력한 경우도 검사했다. **설명 교정:** blur의 빈 문자열은 인라인 배경 지정을 지우는 것이며 항상 흰색을 지정한다는 뜻은 아니다. **공통 한계:** trim 결과로 길이만 검사하므로 원래 제출값의 앞뒤 공백은 남는다. 이를 바꾸려면 query.value에 별도로 대입하는 개선을 명시해야 한다. **표시 개선:** 태그 모양 입력도 글자로 관찰하려면 log의 innerHTML 대신 textContent를 쓴다.

개선안은 원본을 수정한 결과가 아니다. 실제 오류, 수업용 단순화, 목적에 따른 선택을 구별해 판단한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



양쪽 제출 로직은 같고 안내창 문구의 마침표만 다르므로 강사님 코드를 반복하지 않는다. 강사님의 background는 배경 속성을 묶고 내 backgroundColor는 색만 다룬다. 배경 이미지가 없는 현재 원본에서 비슷한 결과를 봤다고 두 속성의 역할 전체가 같다고 설명하지 않는다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 입력 | trim 결과 길이 | 원본의 분기 | 원래 value |
| --- | --- | --- | --- |
| 빈 값·공백만 | 0 | 안내 | 그대로 |
| '가' | 1 | 안내 | 그대로 |
| '  가  ' | 1 | 안내 | 공백 포함 |
| '가나' | 2 | 직접 제출 | 그대로 |
| '  가나  ' | 2 | 직접 제출 | 공백 포함 |

form.submit()은 submit 이벤트 함수를 다시 부르지 않는 직접 제출 메서드이므로 이 원본이 무한히 자기 자신을 부르는 것은 아니다. 브라우저의 기본 제약 검증도 거치지 않는다. 이전 개편의 로컬 수신 검수에서는 공백이 전달되는 것을 확인했지만, 이번 작은 예제는 전송을 수행하지 않고 문자열 상태만 관찰했다. 확인 시점과 검수 범위를 혼동하지 않는다.

| 한 가지만 변경 | 예상 | 해석 |
| --- | --- | --- |
| trim 제거 | 공백 두 칸도 길이 2로 통과 | 실제 의미 있는 글자 검사와 달라짐 |
| 검사 전 query.value에 trim 결과 대입 | 앞뒤 공백이 입력에서도 사라짐 | 검사와 수정의 차이 |
| input 로그를 keyup으로 변경 | 붙여넣기 등에서 관찰 차이 | 키 사건과 값 변경의 차이 |

검사 통과 뒤 화면이 이동한다면 기본 제출을 취소했는지 본다. 공백이 남아 있으면 trim의 반환값만 검사했는지 확인한다. 초점 색이 입력 후 바뀌면 input의 색상 대입 순서를 읽는다. 무작위 색이 예시와 달라도 범위를 만족하면 같은 로직이다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** requestSubmit, validity API를 묶은 검증 도구와 유니코드 글자 수의 상세 처리는 추가 학습이다. 이 실습의 length를 모든 이모지의 눈에 보이는 글자 수와 같다고 확대하지 않는다.



이 절의 확장은 기본 문제의 필수 조건이 아니다. 📚 출처가 있다는 것과 수업 밖 기능이라는 것은 다른 구분이다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. value에 대입하면 input 리스너가 자동 실행되는가?
2. 검사에 trim을 쓰면 실제 value도 바뀌는가?
3. form.submit()은 이 submit 리스너를 다시 호출하는가?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

세 가지 모두 아니다. 프로그램 대입과 사용자 input 이벤트, 새 문자열 반환과 원본 수정, 직접 제출 메서드와 submit 이벤트를 각각 구별한다.

</details>

| 읽을 단계 | 확인 |
| --- | --- |
| 입력 | 언제 값이 바뀌었나? |
| 검사 | 어떤 문자열의 길이인가? |
| 표시 | HTML인가, 글자인가? |
| 제출 | 기본 동작·직접 호출 중 어느 쪽인가? |

[장별 연습문제](실습/연습문제/17_JavaScript_폼이벤트와_이벤트전파_실전문제_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [이벤트 전파와 위임](17-02_JavaScript_이벤트전파와_위임.md)이다.

<!-- 이전 색인 이동 주소 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
<a id="section-6"></a>

[이 장의 목차](#chapter-toc)에서 현재 설명을 찾는다.
