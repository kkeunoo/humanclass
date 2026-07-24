---
title: JS_DOM_내용과_속성_조작
version: v1.0
last_updated: 2026-07-22
status: completed
---

# 문서 정보

| 항목 | 내용 |
|------|------|
| 문서명 | JS_DOM_내용과_속성_조작 |
| 분야 | Frontend / JavaScript |
| 버전 | v1.0 |
| 작성일 | 2026-07-22 |

---

# 개요

DOM 요소를 선택했다면 다음 단계는 해당 요소의 내용을 읽거나 변경하는 것이다.

JavaScript에서는 텍스트 변경, HTML 변경, 입력값 읽기, 속성 변경 등을 통해 화면을 동적으로 제어할 수 있다.

이번 문서에서는 DOM 요소의 내용과 속성을 조작하는 가장 기본적인 방법을 학습한다.

---

# 핵심 개념

DOM 요소는 크게 다음과 같은 정보를 가지고 있다.

- 화면에 표시되는 텍스트
- 내부 HTML 구조
- 입력값(value)
- 속성(attribute)
- DOM 프로퍼티(property)

JavaScript는 이러한 정보를 읽거나 변경하여 화면을 동적으로 구성한다.

대표적으로 사용하는 속성은 다음과 같다.

| 기능 | 사용 방법 |
|------|-----------|
| 텍스트 변경 | innerText |
| 텍스트 읽기 | textContent |
| HTML 변경 | innerHTML |
| 입력값 읽기 | value |
| 체크 여부 | checked |
| 속성 읽기 | getAttribute() |
| 속성 변경 | setAttribute() |
| 속성 삭제 | removeAttribute() |

---

# DOM 조작 흐름

DOM 조작은 일반적으로 다음 순서로 진행된다.

```text
1. 요소 선택
        ↓
2. 값 읽기
        ↓
3. 값 변경
        ↓
4. 화면 반영
```

예를 들어 제목을 변경하는 과정은 다음과 같다.

```javascript
const title =
    document.querySelector("#title");

title.innerText =
    "JavaScript";
```

---

# 기본 문법

## 내용 변경

```javascript
element.innerText = "텍스트";
```

```javascript
element.textContent = "텍스트";
```

```javascript
element.innerHTML = "<b>텍스트</b>";
```

---

## 내용 읽기

```javascript
console.log(
    element.innerText
);
```

```javascript
console.log(
    element.textContent
);
```

```javascript
console.log(
    element.innerHTML
);
```

---

# 주요 개념

## innerText

`innerText`는 화면에 표시되는 텍스트를 읽거나 변경하는 프로퍼티이다.

```html
<h1 id="title">
안녕하세요
</h1>
```

```javascript
const title =
    document.querySelector("#title");

console.log(
    title.innerText
);
```

결과

```text
안녕하세요
```

---

## 텍스트 변경하기

```javascript
title.innerText =
    "JavaScript";
```

화면

```text
JavaScript
```

---

## HTML 예제

```html
<p id="message">
환영합니다.
</p>
```

```javascript
const message =
    document.querySelector(
        "#message"
    );

message.innerText =
    "로그인 성공";
```

실행 결과

```text
로그인 성공
```

---

## 버튼 글자 변경

```html
<button id="loginButton">
로그인
</button>
```

```javascript
const loginButton =
    document.querySelector(
        "#loginButton"
    );

loginButton.innerText =
    "로그인 완료";
```

---

## textContent

`textContent`도 텍스트를 읽고 변경할 수 있다.

```javascript
console.log(
    title.textContent
);
```

```javascript
title.textContent =
    "새로운 제목";
```

---

## innerText와 textContent의 공통점

둘 다 문자열을 읽고 변경할 수 있다.

```javascript
title.innerText =
    "HTML";
```

```javascript
title.textContent =
    "CSS";
```

---

## 차이점

### innerText

- 화면에 보이는 텍스트를 기준으로 동작한다.
- CSS의 영향을 받는다.

### textContent

- HTML 내부의 모든 텍스트를 가져온다.
- 화면 표시 여부와 관계없이 텍스트를 읽는다.

예를 들어 다음 HTML이 있다고 가정한다.

```html
<p id="sample">
HTML
<span style="display:none">
CSS
</span>
JavaScript
</p>
```

```javascript
const sample =
    document.querySelector(
        "#sample"
    );
```

```javascript
console.log(
    sample.innerText
);
```

결과

```text
HTML
JavaScript
```

숨겨진 요소는 제외된다.

반면

```javascript
console.log(
    sample.textContent
);
```

결과

```text
HTML
CSS
JavaScript
```

숨겨진 텍스트도 함께 포함된다.

---

## 언제 사용하는가?

일반적으로 화면의 글자를 변경할 때는 `innerText`를 많이 사용한다.

```javascript
result.innerText =
    "회원가입 완료";
```

화면에 보이는 텍스트를 그대로 변경하기 때문이다.

반면 HTML 내부의 전체 텍스트를 그대로 가져와야 하는 경우에는 `textContent`를 사용한다.

---

# innerHTML

`innerHTML`은 요소 내부의 HTML 자체를 읽거나 변경하는 프로퍼티이다.

```html
<div id="box">
안녕하세요
</div>
```

```javascript
const box =
    document.querySelector(
        "#box"
    );
```

```javascript
console.log(
    box.innerHTML
);
```

결과

```text
안녕하세요
```

---

## HTML 추가하기

```javascript
box.innerHTML =
    "<h2>JavaScript</h2>";
```

실행 결과

```html
<h2>JavaScript</h2>
```

---

## 여러 요소 추가

```javascript
box.innerHTML =

`
<h2>HTML</h2>
<p>CSS</p>
<button>확인</button>
`;
```

화면에는 실제 HTML 요소가 생성된다.

---

## innerText와의 차이

```javascript
box.innerText =
    "<h2>JavaScript</h2>";
```

화면

```text
<h2>JavaScript</h2>
```

태그가 문자열로 출력된다.

---

반면

```javascript
box.innerHTML =
    "<h2>JavaScript</h2>";
```

화면

```html
JavaScript
```

`<h2>` 요소가 실제로 생성된다.

---

# 세 가지 프로퍼티 비교

| 프로퍼티 | HTML 적용 | 텍스트 변경 | 태그 생성 |
|-----------|-----------|------------|-----------|
| innerText | ❌ | ✅ | ❌ |
| textContent | ❌ | ✅ | ❌ |
| innerHTML | ✅ | ✅ | ✅ |

---

# 실무에서 많이 사용하는 예

## 알림 메시지 출력

```javascript
message.innerText =
    "로그인 성공";
```

---

## 에러 메시지 출력

```javascript
error.innerText =
    "비밀번호를 입력하세요.";
```

---

## 공지사항 출력

```javascript
notice.innerHTML =

`
<strong>공지</strong>

신규 이벤트가 시작되었습니다.
`;
```

---

# 문자열과 HTML의 차이

다음 코드를 비교해보자.

```javascript
result.innerText =
    "<b>Hello</b>";
```

출력 결과

```text
<b>Hello</b>
```

---

```javascript
result.innerHTML =
    "<b>Hello</b>";
```

출력 결과

```html
<b>Hello</b>
```

HTML 태그가 실제 DOM 요소로 생성된다.

---

# 주의사항

`innerHTML`은 매우 편리하지만 문자열을 그대로 HTML로 해석한다.

따라서 사용자 입력을 그대로 넣는 것은 보안상 문제가 될 수 있다.

```javascript
result.innerHTML =
    userInput;
```

실무에서는 사용자 입력을 그대로 `innerHTML`에 넣지 않는 것이 일반적이다.

기본적인 화면의 텍스트를 변경할 때는 `innerText`를 사용하는 것이 안전하다.

---

# 내용 변경 디버깅

텍스트가 변경되지 않는다면 다음 내용을 확인한다.

```text
1. 요소를 제대로 선택했는가?
2. null이 반환되지 않았는가?
3. JavaScript 실행 시점이 올바른가?
4. innerText와 innerHTML을 혼동하지 않았는가?
5. console.log()로 선택 결과를 확인했는가?
```

---

---

# value

`value`는 입력 요소(input, textarea, select 등)의 값을 읽거나 변경하는 프로퍼티이다.

사용자가 입력한 데이터를 JavaScript에서 가장 많이 가져오는 방법이다.

## HTML

```html
<input
    type="text"
    id="userName"
    value="홍길동"
>
```

## JavaScript

```javascript
const userName =
    document.querySelector(
        "#userName"
    );

console.log(
    userName.value
);
```

결과

```text
홍길동
```

---

## 입력값 변경하기

```javascript
userName.value =
    "김철수";
```

실행 후

```text
김철수
```

로 변경된다.

---

## 사용자가 입력한 값 가져오기

```html
<input
    type="text"
    id="email"
>

<button id="checkButton">
확인
</button>
```

```javascript
const email =
    document.querySelector(
        "#email"
    );

const checkButton =
    document.querySelector(
        "#checkButton"
    );

checkButton.addEventListener(
    "click",
    function() {

        console.log(
            email.value
        );

    }
);
```

버튼을 누르는 시점의 입력값을 읽는다.

---

# value와 innerText의 차이

```html
<input
    id="user"
    value="홍길동"
>

<p id="message">
안녕하세요
</p>
```

입력 요소는

```javascript
user.value
```

를 사용한다.

일반 요소는

```javascript
message.innerText
```

를 사용한다.

| 요소 | 사용 프로퍼티 |
|------|--------------|
| input | value |
| textarea | value |
| select | value |
| p | innerText |
| h1 | innerText |
| div | innerText 또는 innerHTML |

---

# checked

`checked`는 체크박스와 라디오 버튼의 선택 여부를 나타내는 Boolean 프로퍼티이다.

---

## HTML

```html
<input
    type="checkbox"
    id="agree"
>
```

---

## JavaScript

```javascript
const agree =
    document.querySelector(
        "#agree"
    );

console.log(
    agree.checked
);
```

결과

```text
true
```

또는

```text
false
```

---

## 체크 여부 변경

```javascript
agree.checked = true;
```

```javascript
agree.checked = false;
```

---

## 체크 여부 확인

```javascript
if (agree.checked) {

    console.log("동의");

}
```

---

# 체크박스 실습

## HTML

```html
<label>

<input
    type="checkbox"
    id="marketing"
>

마케팅 수신 동의

</label>

<button id="btn">
확인
</button>

<p id="result"></p>
```

---

## JavaScript

```javascript
const marketing =
    document.querySelector(
        "#marketing"
    );

const result =
    document.querySelector(
        "#result"
    );

const btn =
    document.querySelector(
        "#btn"
    );

btn.addEventListener(
    "click",
    function() {

        if (
            marketing.checked
        ) {

            result.innerText =
                "동의했습니다.";

        } else {

            result.innerText =
                "동의하지 않았습니다.";

        }

    }
);
```

---

# selected

`selected`는 `<option>` 요소의 선택 여부를 나타내는 프로퍼티이다.

하지만 실제 실무에서는 대부분 `select.value`를 사용한다.

---

## HTML

```html
<select id="city">

<option value="서울">
서울
</option>

<option value="부산">
부산
</option>

<option value="대전">
대전
</option>

</select>
```

---

## JavaScript

```javascript
const city =
    document.querySelector(
        "#city"
    );

console.log(
    city.value
);
```

결과

```text
서울
```

선택이 변경되면 `value`도 함께 변경된다.

---

# Attribute란?

Attribute는 HTML 태그에 작성하는 속성이다.

예를 들어

```html
<img

src="cat.jpg"

alt="고양이"

width="300"

>
```

여기서

- src
- alt
- width

모두 Attribute이다.

---

# getAttribute()

HTML 속성값을 읽는다.

## HTML

```html
<img

id="photo"

src="cat.jpg"

alt="고양이"

>
```

---

## JavaScript

```javascript
const photo =
    document.querySelector(
        "#photo"
    );

console.log(

photo.getAttribute(
    "src"
)

);
```

결과

```text
cat.jpg
```

---

# setAttribute()

속성을 변경하거나 새로 만든다.

```javascript
photo.setAttribute(

"src",

"dog.jpg"

);
```

실행 후

```html
<img src="dog.jpg">
```

---

## alt 변경

```javascript
photo.setAttribute(

"alt",

"강아지"

);
```

---

# removeAttribute()

속성을 제거한다.

```javascript
photo.removeAttribute(
    "alt"
);
```

실행 후

```html
<img src="dog.jpg">
```

---

# hasAttribute()

속성이 존재하는지 확인한다.

```javascript
photo.hasAttribute(
    "src"
);
```

결과

```text
true
```

---

```javascript
photo.hasAttribute(
    "title"
);
```

결과

```text
false
```

---

# Property와 Attribute의 차이

HTML

```html
<input

type="text"

id="user"

value="홍길동"

>
```

Property

```javascript
user.value
```

Attribute

```javascript
user.getAttribute(
    "value"
);
```

둘 다 값을 읽을 수 있지만 의미가 다르다.

| Property | Attribute |
|-----------|-----------|
| DOM 객체의 값 | HTML 속성 |
| JavaScript 중심 | HTML 중심 |
| 실행 중 변경 가능 | 초기 HTML 기준 |

---

# 언제 무엇을 사용할까?

| 목적 | 사용 |
|------|------|
| 입력값 읽기 | value |
| 체크 여부 | checked |
| 화면 글자 변경 | innerText |
| HTML 추가 | innerHTML |
| 속성 읽기 | getAttribute() |
| 속성 변경 | setAttribute() |
| 속성 삭제 | removeAttribute() |

---

# 실무 예제 ① 로그인

## HTML

```html
<input
    id="id"
>

<input
    id="pw"
    type="password"
>

<button id="login">
로그인
</button>
```

---

## JavaScript

```javascript
const id =
    document.querySelector("#id");

const pw =
    document.querySelector("#pw");

const login =
    document.querySelector("#login");

login.addEventListener(
    "click",
    function() {

        console.log(id.value);
        console.log(pw.value);

    }
);
```

---

# 실무 예제 ② 이미지 변경

```html
<img

id="profile"

src="user.png"

>
```

```javascript
const profile =
    document.querySelector(
        "#profile"
    );

profile.setAttribute(

"src",

"admin.png"

);
```

---

# 실무 예제 ③ 버튼 비활성화

```html
<button id="submit">
가입하기
</button>
```

```javascript
const submit =
    document.querySelector(
        "#submit"
    );

submit.disabled = true;
```

버튼을 다시 사용할 수 있도록 하려면

```javascript
submit.disabled = false;
```

를 사용한다.

---

# 내용과 속성 조작 디버깅

문제가 발생하면 다음 순서대로 확인한다.

```text
1. 요소를 제대로 선택했는가?
2. value와 innerText를 혼동하지 않았는가?
3. checked는 checkbox/radio에서만 사용하는가?
4. setAttribute()의 속성명을 올바르게 작성했는가?
5. getAttribute()가 null을 반환하지 않았는가?
6. console.log()로 값을 확인했는가?
```

---

---

# 실무 활용

DOM 요소의 내용과 속성을 변경하는 기능은 거의 모든 웹 서비스에서 사용된다.

대표적인 활용 사례는 다음과 같다.

- 로그인 입력값 확인
- 회원가입 폼 검증
- 장바구니 수량 변경
- 상품 이미지 변경
- 버튼 활성화 및 비활성화
- 에러 메시지 출력
- 프로필 정보 수정
- 공지사항 및 알림 출력

사용자가 화면에서 보는 대부분의 내용은 이러한 DOM 조작을 통해 변경된다.

---

# 실무 예제 프로젝트

이번 예제에서는 회원가입 화면을 간단하게 구현한다.

## HTML

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>회원가입</title>
    <script src="main.js" defer></script>
</head>
<body>

<h1>회원가입</h1>

<input
    type="text"
    id="userName"
    placeholder="이름 입력"
>

<br><br>

<input
    type="email"
    id="email"
    placeholder="이메일 입력"
>

<br><br>

<label>

<input
    type="checkbox"
    id="agree"
>

개인정보 수집 동의

</label>

<br><br>

<button id="joinButton">

가입하기

</button>

<p id="result"></p>

</body>
</html>
```

---

## JavaScript

```javascript
const userName =
    document.querySelector(
        "#userName"
    );

const email =
    document.querySelector(
        "#email"
    );

const agree =
    document.querySelector(
        "#agree"
    );

const joinButton =
    document.querySelector(
        "#joinButton"
    );

const result =
    document.querySelector(
        "#result"
    );
```

---

## 가입 버튼 이벤트

```javascript
joinButton.addEventListener(
    "click",
    function() {

        if (
            userName.value === ""
        ) {

            result.innerText =
                "이름을 입력해주세요.";

            return;

        }

        if (
            email.value === ""
        ) {

            result.innerText =
                "이메일을 입력해주세요.";

            return;

        }

        if (
            agree.checked === false
        ) {

            result.innerText =
                "개인정보 수집에 동의해주세요.";

            return;

        }

        result.innerHTML =

        `
        <strong>
        회원가입이 완료되었습니다.
        </strong>
        `;

    }
);
```

---

# 예제 코드 흐름

```text
1. 입력 요소를 선택한다.
2. 버튼 요소를 선택한다.
3. 결과를 출력할 요소를 선택한다.
4. 버튼을 클릭한다.
5. 이름 입력 여부를 확인한다.
6. 이메일 입력 여부를 확인한다.
7. 체크박스 선택 여부를 확인한다.
8. 조건을 모두 만족하면 완료 메시지를 출력한다.
```

---

# 내용과 속성 조작 오류 분석

## 오류 1

```javascript
title.value = "Hello";
```

`h1`, `p`, `div`와 같은 일반 요소는 `value`를 사용하지 않는다.

올바른 코드

```javascript
title.innerText =
    "Hello";
```

---

## 오류 2

```javascript
input.innerText
```

입력 요소는 `innerText`가 아니라 `value`를 사용한다.

```javascript
input.value
```

---

## 오류 3

```javascript
result.innerHTML =
    "<strong>Hello";
```

태그가 제대로 닫히지 않으면 의도하지 않은 결과가 나타날 수 있다.

올바른 코드

```javascript
result.innerHTML =
    "<strong>Hello</strong>";
```

---

## 오류 4

```javascript
checkbox.value
```

체크 여부를 확인하려면

```javascript
checkbox.checked
```

를 사용해야 한다.

---

## 오류 5

```javascript
image.src =
    "dog.jpg";
```

동작은 가능하지만,

```javascript
image.setAttribute(
    "src",
    "dog.jpg"
);
```

처럼 작성하면 HTML 속성을 직접 조작한다는 의미가 더 명확해진다.

---

## 오류 6

```javascript
photo.getAttribute(
    "SRC"
);
```

속성명은 HTML에서 작성한 이름과 동일하게 사용하는 것이 좋다.

```javascript
photo.getAttribute(
    "src"
);
```

---

# 내용 변경과 속성 변경 비교

| 작업 | 사용 방법 |
|------|-----------|
| 글자 변경 | innerText |
| HTML 추가 | innerHTML |
| 전체 텍스트 읽기 | textContent |
| 입력값 읽기 | value |
| 체크 여부 | checked |
| 속성 읽기 | getAttribute() |
| 속성 변경 | setAttribute() |
| 속성 삭제 | removeAttribute() |

---

# 이번 문서에서 새롭게 배운 내용

- DOM 요소의 내용을 변경하는 방법
- `innerText`와 `textContent`의 차이
- `innerHTML`을 이용한 HTML 생성
- 입력 요소의 `value` 사용법
- 체크박스와 라디오 버튼의 `checked`
- `selected`와 `select.value`
- HTML Attribute의 개념
- `getAttribute()`
- `setAttribute()`
- `removeAttribute()`
- `hasAttribute()`
- Property와 Attribute의 차이

---

# 자주 하는 실수

- 일반 요소에서 `value`를 사용한다.
- input 요소에서 `innerText`를 사용한다.
- `innerHTML`과 `innerText`를 혼동한다.
- `checked` 대신 `value`를 사용한다.
- HTML 태그를 문자열처럼 출력하려 한다.
- `setAttribute()`의 속성명을 잘못 작성한다.
- 사용자 입력을 그대로 `innerHTML`에 넣는다.
- Property와 Attribute를 같은 개념으로 생각한다.

---

# 면접 포인트

### innerText와 textContent의 차이

`innerText`는 화면에 표시되는 텍스트를 기준으로 동작한다.

`textContent`는 화면에 보이지 않는 텍스트까지 포함하여 읽는다.

---

### innerHTML은 언제 사용하는가?

HTML 요소 자체를 동적으로 생성하거나 변경할 때 사용한다.

단, 사용자 입력을 그대로 넣는 것은 보안상 주의해야 한다.

---

### value는 언제 사용하는가?

`input`, `textarea`, `select`와 같은 입력 요소의 값을 읽거나 변경할 때 사용한다.

---

### checked는 언제 사용하는가?

체크박스와 라디오 버튼의 선택 여부를 확인하거나 변경할 때 사용한다.

---

### Property와 Attribute의 차이는?

Property는 DOM 객체의 현재 상태를 의미한다.

Attribute는 HTML 태그에 작성된 속성을 의미한다.

실행 중에는 Property가 변경될 수 있으며, Attribute는 초기 HTML 속성을 기준으로 한다.

---

# 핵심 정리

- DOM 요소는 내용과 속성을 모두 변경할 수 있다.
- 화면의 글자를 변경할 때는 `innerText`를 가장 많이 사용한다.
- HTML을 생성할 때는 `innerHTML`을 사용한다.
- 입력 요소는 `value`로 값을 읽는다.
- 체크 여부는 `checked`로 확인한다.
- HTML 속성은 `getAttribute()`와 `setAttribute()`로 조작할 수 있다.
- Property와 Attribute는 서로 다른 개념이다.
- 요소의 종류에 맞는 프로퍼티를 사용하는 것이 중요하다.

---

# 변경 이력

| Version | 날짜 | 변경 내용 |
|---------|------|-----------|
| v1.0 | 2026-07-22 | 최초 작성 |
