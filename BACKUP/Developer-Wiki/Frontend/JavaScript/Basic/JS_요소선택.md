---
title: JavaScript DOM 요소 선택
version: v1.0
last_updated: 2026-07-22
status: Completed
---

# JavaScript DOM 요소 선택

## 문서 정보

| 항목 | 내용 |
|------|------|
| 문서명 | JavaScript DOM 요소 선택 |
| 분류 | Frontend / JavaScript / Basic |
| 난이도 | Beginner |
| 선수 지식 | DOM 기초, CSS 선택자, JavaScript 변수와 객체 |
| 핵심 주제 | getElementById, querySelector, querySelectorAll, NodeList |
| 버전 | v1.0 |
| 최종 수정일 | 2026-07-22 |

---

# 개요

JavaScript로 HTML 요소의 내용이나 스타일을 변경하려면 먼저 대상 요소를 선택해야 한다.

다음 HTML이 있다고 가정한다.

```html
<h1 id="title">JavaScript</h1>
<p class="message">DOM 요소 선택</p>
```

JavaScript에서는 다음과 같이 요소를 선택할 수 있다.

```javascript
const title = document.querySelector("#title");
const message = document.querySelector(".message");
```

선택한 요소는 JavaScript 객체로 반환되며 변수에 저장하여 사용할 수 있다.

```javascript
console.log(title);
console.log(message);
```

DOM 요소 선택은 다음과 같은 작업의 시작점이다.

- 글자 변경
- 입력값 가져오기
- 스타일 변경
- 클래스 추가와 삭제
- 속성 변경
- 이벤트 연결
- 요소 생성과 삭제

따라서 DOM을 학습할 때 요소 선택 방법과 반환 결과를 정확히 구분하는 것이 중요하다.

---

# DOM 요소 선택의 기본 흐름

DOM 요소를 조작할 때는 일반적으로 다음 순서로 작성한다.

```text
1. HTML 요소를 작성한다.
2. JavaScript에서 요소를 선택한다.
3. 선택 결과를 변수에 저장한다.
4. 선택 결과를 확인한다.
5. 프로퍼티 또는 메서드를 사용한다.
```

예제

```html
<h1 id="title">기존 제목</h1>
```

```javascript
const title = document.querySelector("#title");

console.log(title);

title.innerText = "변경된 제목";
```

코드 실행 흐름은 다음과 같다.

```text
document 객체에서
↓
id가 title인 요소를 찾고
↓
title 변수에 저장한 뒤
↓
innerText 값을 변경한다.
```

---

# 요소 선택 후 변수에 저장하는 이유

다음과 같이 선택과 조작을 한 줄로 작성할 수도 있다.

```javascript
document.querySelector("#title").innerText = "변경된 제목";
```

하지만 일반적으로는 선택 결과를 변수에 저장하여 사용하는 것이 좋다.

```javascript
const title = document.querySelector("#title");

title.innerText = "변경된 제목";
title.style.fontSize = "40px";
title.classList.add("active");
```

변수에 저장하면 다음과 같은 장점이 있다.

- 같은 요소를 여러 번 선택하지 않아도 된다.
- 코드의 의미를 이해하기 쉽다.
- 선택 결과를 `console.log()`로 확인할 수 있다.
- 여러 프로퍼티와 메서드를 연속해서 사용할 수 있다.
- 오류가 발생했을 때 원인을 찾기 쉽다.

---

# 주요 요소 선택 방법

기초 단계에서 자주 사용하는 요소 선택 방법은 다음과 같다.

| 메서드 | 선택 기준 | 반환 결과 |
|--------|-----------|-----------|
| `getElementById()` | id 속성 | 요소 하나 또는 `null` |
| `querySelector()` | CSS 선택자 | 첫 번째 요소 하나 또는 `null` |
| `querySelectorAll()` | CSS 선택자 | 여러 요소가 담긴 NodeList |

각 메서드는 선택 방식과 반환 결과가 다르다.

반환 결과가 요소 하나인지 여러 요소인지에 따라 이후 코드 작성 방식도 달라진다.

---

# getElementById()

`getElementById()`는 `id` 속성값을 기준으로 요소 하나를 선택하는 메서드이다.

기본 문법

```javascript
document.getElementById("id 이름");
```

`id` 이름 앞에 `#`을 작성하지 않는다.

---

# getElementById() 기본 예제

HTML

```html
<h1 id="title">JavaScript</h1>
```

JavaScript

```javascript
const title = document.getElementById("title");

console.log(title);
```

결과

```html
<h1 id="title">JavaScript</h1>
```

선택한 요소의 내용을 변경할 수 있다.

```javascript
title.innerText = "DOM 요소 선택";
```

---

# getElementById()에서 #을 사용하지 않는 이유

`getElementById()`에는 CSS 선택자가 아니라 `id` 속성의 값만 전달한다.

올바른 코드

```javascript
const title = document.getElementById("title");
```

잘못된 코드

```javascript
const title = document.getElementById("#title");
```

HTML에서 실제 `id` 값은 다음과 같다.

```html
<h1 id="title">제목</h1>
```

`id` 값은 `title`이며 `#title`이 아니다.

`#`은 CSS 선택자에서 해당 값이 `id`라는 것을 나타내는 기호이다.

---

# getElementById()로 요소를 찾지 못한 경우

HTML

```html
<h1 id="title">제목</h1>
```

JavaScript

```javascript
const message = document.getElementById("message");

console.log(message);
```

결과

```text
null
```

HTML 문서에 `id="message"`인 요소가 없기 때문에 `null`이 반환된다.

`null` 상태에서 프로퍼티를 사용하면 오류가 발생한다.

```javascript
message.innerText = "안녕하세요.";
```

오류 예시

```text
Cannot set properties of null
```

---

# querySelector()

`querySelector()`는 CSS 선택자를 이용하여 조건에 맞는 첫 번째 요소 하나를 선택한다.

기본 문법

```javascript
document.querySelector("CSS 선택자");
```

CSS에서 사용하던 선택자를 문자열로 전달한다.

---

# querySelector()로 id 선택하기

HTML

```html
<h1 id="title">제목</h1>
```

JavaScript

```javascript
const title = document.querySelector("#title");

console.log(title);
```

`id` 선택자이므로 `#`을 사용한다.

```javascript
"#title"
```

---

# querySelector()로 class 선택하기

HTML

```html
<p class="message">안녕하세요.</p>
```

JavaScript

```javascript
const message = document.querySelector(".message");

console.log(message);
```

`class` 선택자이므로 `.`을 사용한다.

```javascript
".message"
```

---

# querySelector()로 태그 선택하기

HTML

```html
<h2>DOM 학습</h2>
```

JavaScript

```javascript
const heading = document.querySelector("h2");

console.log(heading);
```

태그 선택자는 태그 이름을 그대로 작성한다.

---

# querySelector()로 속성 선택하기

HTML

```html
<input type="text" name="userName">
```

JavaScript

```javascript
const userName = document.querySelector("[name=userName]");

console.log(userName);
```

속성 선택자도 CSS 선택자 문법을 그대로 사용한다.

따옴표를 포함하여 다음처럼 작성할 수도 있다.

```javascript
const userName = document.querySelector('[name="userName"]');
```

JavaScript 문자열에 큰따옴표가 포함되므로 바깥쪽에 작은따옴표를 사용하면 읽기 쉽다.

---

# 선택된 체크박스 찾기

속성 선택자와 상태 선택자를 함께 사용할 수 있다.

HTML

```html
<label>
    <input type="checkbox" name="agree">
    동의
</label>
```

JavaScript

```javascript
const agree = document.querySelector("[name=agree]:checked");

console.log(agree);
```

체크되어 있다면 해당 요소가 반환된다.

체크되어 있지 않다면 다음 값이 반환된다.

```text
null
```

따라서 선택 여부를 확인할 수 있다.

```javascript
if (agree !== null) {

    console.log("동의했습니다.");

}
```

---

# 선택된 라디오 버튼 찾기

HTML

```html
<label>
    <input type="radio" name="size" value="small">
    Small
</label>

<label>
    <input type="radio" name="size" value="large">
    Large
</label>
```

JavaScript

```javascript
const size = document.querySelector("[name=size]:checked");

console.log(size);
```

선택된 라디오 버튼이 있다면 해당 요소가 반환된다.

선택된 값은 `value` 프로퍼티로 확인한다.

```javascript
console.log(size.value);
```

단, 아무것도 선택되지 않았다면 `size`는 `null`이므로 바로 `value`를 사용하면 오류가 발생한다.

```javascript
const size = document.querySelector("[name=size]:checked");

if (size !== null) {

    console.log(size.value);

}
```

---

# 복합 선택자 사용

`querySelector()`에서는 여러 선택자를 조합할 수 있다.

HTML

```html
<section id="profile">
    <p class="name">홍길동</p>
</section>
```

JavaScript

```javascript
const name = document.querySelector("#profile .name");

console.log(name);
```

위 코드는 `id="profile"`인 요소 내부의 `class="name"`인 요소를 선택한다.

---

# 자식 선택자 사용

HTML

```html
<ul id="menu">
    <li>HTML</li>
    <li>CSS</li>
    <li>JavaScript</li>
</ul>
```

JavaScript

```javascript
const menuItem = document.querySelector("#menu > li");

console.log(menuItem);
```

조건에 맞는 첫 번째 `li` 요소만 반환된다.

결과

```html
<li>HTML</li>
```

---

# 여러 class를 가진 요소 선택하기

HTML

```html
<div class="card active">카드</div>
```

두 class를 모두 가진 요소를 선택하려면 class 선택자를 붙여 작성한다.

```javascript
const card = document.querySelector(".card.active");

console.log(card);
```

다음 선택자와 혼동하지 않도록 주의한다.

```javascript
".card .active"
```

`.card .active`는 `card` 요소 내부에 있는 `active` 요소를 의미한다.

```javascript
".card.active"
```

`.card.active`는 `card`와 `active` class를 모두 가진 하나의 요소를 의미한다.

---

# querySelector()는 첫 번째 요소만 반환한다

HTML

```html
<p class="item">첫 번째</p>
<p class="item">두 번째</p>
<p class="item">세 번째</p>
```

JavaScript

```javascript
const item = document.querySelector(".item");

console.log(item);
```

결과

```html
<p class="item">첫 번째</p>
```

조건에 맞는 요소가 여러 개 있어도 첫 번째 요소 하나만 반환한다.

모든 요소를 선택하려면 `querySelectorAll()`을 사용해야 한다.

---

# getElementById()와 querySelector() 비교

HTML

```html
<h1 id="title">제목</h1>
```

`getElementById()` 사용

```javascript
const title1 = document.getElementById("title");
```

`querySelector()` 사용

```javascript
const title2 = document.querySelector("#title");
```

두 코드 모두 같은 요소를 선택한다.

| 구분 | `getElementById()` | `querySelector()` |
|------|--------------------|-------------------|
| 선택 기준 | id 값 | CSS 선택자 |
| `#` 사용 | 사용하지 않음 | 사용함 |
| class 선택 | 불가능 | 가능 |
| 태그 선택 | 불가능 | 가능 |
| 복합 선택자 | 불가능 | 가능 |
| 반환 결과 | 요소 하나 또는 `null` | 첫 번째 요소 또는 `null` |

---

# 어떤 선택 방법을 사용해야 하는가?

특정 `id` 요소만 선택한다면 두 방법 모두 사용할 수 있다.

```javascript
document.getElementById("title");
```

```javascript
document.querySelector("#title");
```

다양한 CSS 선택자를 사용하거나 선택 방식의 통일성을 유지하려면 `querySelector()`가 편리하다.

```javascript
document.querySelector(".message");
document.querySelector("[name=size]:checked");
document.querySelector("#menu > li");
```

프로젝트나 팀의 코드 작성 방식에 따라 선택 방법은 달라질 수 있다.

중요한 것은 메서드마다 선택자 작성 방법이 다르다는 점이다.

---

# querySelectorAll()

`querySelectorAll()`은 CSS 선택자와 일치하는 모든 요소를 선택한다.

기본 문법

```javascript
document.querySelectorAll("CSS 선택자");
```

반환 결과는 요소 하나가 아니라 여러 요소가 들어 있는 `NodeList`이다.

---

# querySelectorAll() 기본 예제

HTML

```html
<p class="item">HTML</p>
<p class="item">CSS</p>
<p class="item">JavaScript</p>
```

JavaScript

```javascript
const items = document.querySelectorAll(".item");

console.log(items);
```

출력 결과는 브라우저에 따라 다음과 비슷하게 표시된다.

```text
NodeList(3)
```

NodeList 안에는 선택된 세 개의 요소가 저장되어 있다.

```text
0: p.item
1: p.item
2: p.item
length: 3
```

---

# querySelector()와 querySelectorAll() 비교

HTML

```html
<div class="box">첫 번째</div>
<div class="box">두 번째</div>
<div class="box">세 번째</div>
```

`querySelector()` 사용

```javascript
const box = document.querySelector(".box");

console.log(box);
```

첫 번째 요소 하나가 반환된다.

`querySelectorAll()` 사용

```javascript
const boxes = document.querySelectorAll(".box");

console.log(boxes);
```

모든 `.box` 요소가 NodeList에 담겨 반환된다.

| 구분 | `querySelector()` | `querySelectorAll()` |
|------|-------------------|----------------------|
| 선택 개수 | 첫 번째 요소 하나 | 조건에 맞는 모든 요소 |
| 반환 결과 | Element 또는 `null` | NodeList |
| 프로퍼티 직접 사용 | 가능 | 일반적으로 불가능 |
| 반복 처리 | 필요하지 않음 | 여러 요소 조작 시 필요 |

---

# NodeList란?

NodeList는 여러 개의 DOM 노드를 모아놓은 목록 형태의 객체이다.

```javascript
const items = document.querySelectorAll(".item");
```

`items`는 하나의 HTML 요소가 아니다.

여러 요소를 담고 있는 NodeList이다.

```javascript
console.log(items);
console.log(typeof items);
```

`typeof` 결과는 다음과 같다.

```text
object
```

NodeList도 JavaScript에서 객체로 다뤄진다.

---

# NodeList의 인덱스

NodeList는 배열처럼 인덱스를 이용하여 각 요소에 접근할 수 있다.

```javascript
const items = document.querySelectorAll(".item");

console.log(items[0]);
console.log(items[1]);
console.log(items[2]);
```

인덱스는 `0`부터 시작한다.

```text
items[0] → 첫 번째 요소
items[1] → 두 번째 요소
items[2] → 세 번째 요소
```

---

# NodeList의 length

선택된 요소의 개수는 `length` 프로퍼티로 확인할 수 있다.

```javascript
const items = document.querySelectorAll(".item");

console.log(items.length);
```

요소가 세 개라면 결과는 다음과 같다.

```text
3
```

---

# 여러 요소를 찾지 못한 경우

`querySelectorAll()`은 조건에 맞는 요소가 없어도 `null`을 반환하지 않는다.

HTML에 `.item` 요소가 없다고 가정한다.

```javascript
const items = document.querySelectorAll(".item");

console.log(items);
console.log(items.length);
```

결과

```text
NodeList(0)
0
```

빈 NodeList가 반환된다.

이는 `querySelector()`와 중요한 차이이다.

```javascript
const item = document.querySelector(".item");
```

결과

```text
null
```

```javascript
const items = document.querySelectorAll(".item");
```

결과

```text
NodeList(0)
```

---

# 요소 하나와 여러 요소의 차이

HTML

```html
<div class="quiz q1">문제 1</div>
<div class="quiz q2">문제 2</div>
```

요소 하나 선택

```javascript
const quiz = document.querySelector(".quiz");

console.log(quiz);
```

`quiz`에는 첫 번째 `div` 요소 하나가 저장된다.

따라서 다음과 같이 `classList`를 사용할 수 있다.

```javascript
const result = quiz.classList.contains("q1");

console.log(result);
```

결과

```text
true
```

---

# querySelectorAll() 결과에 classList를 사용할 수 없는 이유

다음 코드를 살펴보자.

```javascript
const quizzes = document.querySelectorAll("div.quiz");

const result = quizzes.classList.contains("q2");
```

이 코드는 오류가 발생한다.

`quizzes`는 하나의 요소가 아니라 NodeList이기 때문이다.

NodeList 자체에는 요소의 `classList` 프로퍼티가 없다.

```text
quizzes
└── 여러 개의 div 요소가 들어 있는 NodeList
```

각 요소의 `classList`를 사용하려면 인덱스로 하나를 꺼내야 한다.

```javascript
const quizzes = document.querySelectorAll("div.quiz");

const result = quizzes[1].classList.contains("q2");

console.log(result);
```

결과

```text
true
```

---

# 선택 결과의 형태 확인하기

DOM 요소 관련 오류가 발생하면 먼저 선택 결과를 출력한다.

```javascript
const quizzes = document.querySelectorAll("div.quiz");

console.log(quizzes);
console.log(typeof quizzes);
console.log(quizzes.length);
```

그리고 첫 번째 요소도 확인한다.

```javascript
console.log(quizzes[0]);
```

다음 차이를 구분해야 한다.

```javascript
quizzes.classList
```

NodeList에 `classList`를 사용하려는 코드이다.

```javascript
quizzes[0].classList
```

NodeList 안의 첫 번째 요소에 `classList`를 사용하는 코드이다.

---

# 반환 결과 구분하기

DOM 요소 선택 메서드를 사용할 때는 다음 질문을 먼저 확인해야 한다.

```text
선택 결과가 요소 하나인가?
또는 여러 요소가 들어 있는 목록인가?
```

요소 하나라면 다음처럼 직접 프로퍼티를 사용할 수 있다.

```javascript
const title = document.querySelector("#title");

title.innerText = "제목";
title.classList.add("active");
```

여러 요소라면 각 요소에 접근해야 한다.

```javascript
const items = document.querySelectorAll(".item");

items[0].classList.add("active");
items[1].classList.add("active");
```

또는 반복문을 사용한다.

```javascript
for (let i = 0; i < items.length; i++) {

    items[i].classList.add("active");

}
```

반복문을 이용한 여러 요소 처리는 다음 Part에서 자세히 다룬다.

---

# 요소 선택 시 변수 이름 작성

선택 결과가 하나인지 여러 개인지 변수 이름으로 구분하면 코드를 이해하기 쉽다.

요소 하나

```javascript
const item = document.querySelector(".item");
```

여러 요소

```javascript
const items = document.querySelectorAll(".item");
```

요소 하나

```javascript
const quiz = document.querySelector(".quiz");
```

여러 요소

```javascript
const quizzes = document.querySelectorAll(".quiz");
```

일반적으로 여러 요소를 저장한 변수는 복수형 이름을 사용하는 것이 좋다.

---

---

# NodeList와 배열(Array)의 차이

`querySelectorAll()`의 반환 결과는 배열(Array)이 아니라 **NodeList**이다.

```javascript
const items = document.querySelectorAll(".item");

console.log(items);
```

결과

```text
NodeList(3)
```

NodeList는 여러 개의 DOM 요소를 저장하는 객체이다.

배열과 비슷하게 사용할 수 있지만 완전히 같은 자료형은 아니다.

---

# NodeList의 특징

NodeList는 다음과 같은 특징을 가진다.

- 여러 요소를 저장한다.
- 인덱스로 접근할 수 있다.
- `length`를 사용할 수 있다.
- 반복문으로 순회할 수 있다.
- DOM 요소(Element)를 저장한다.

예제

```javascript
const items = document.querySelectorAll(".item");

console.log(items[0]);
console.log(items.length);
```

---

# NodeList와 배열 비교

| 구분 | Array | NodeList |
|------|-------|----------|
| 여러 값 저장 | O | O |
| 인덱스 사용 | O | O |
| length | O | O |
| DOM 요소 저장 | X | O |
| querySelectorAll() 반환 | X | O |

기초 단계에서는 NodeList를 **"DOM 요소가 들어있는 배열처럼 생긴 객체"**라고 이해하면 충분하다.

---

# NodeList 반복하기

HTML

```html
<p class="item">HTML</p>
<p class="item">CSS</p>
<p class="item">JavaScript</p>
```

JavaScript

```javascript
const items = document.querySelectorAll(".item");

for (let i = 0; i < items.length; i++) {

    console.log(items[i]);

}
```

결과

```text
<p class="item">HTML</p>
<p class="item">CSS</p>
<p class="item">JavaScript</p>
```

---

# 요소의 글자 출력하기

NodeList 안에는 DOM 요소가 저장되어 있다.

따라서 인덱스로 접근한 뒤 `innerText`를 사용할 수 있다.

```javascript
const items = document.querySelectorAll(".item");

for (let i = 0; i < items.length; i++) {

    console.log(items[i].innerText);

}
```

결과

```text
HTML
CSS
JavaScript
```

---

# 여러 요소의 내용 변경하기

HTML

```html
<p class="item">HTML</p>
<p class="item">CSS</p>
<p class="item">JavaScript</p>
```

JavaScript

```javascript
const items = document.querySelectorAll(".item");

for (let i = 0; i < items.length; i++) {

    items[i].innerText = "변경 완료";

}
```

실행 결과

```text
변경 완료
변경 완료
변경 완료
```

---

# 여러 요소의 스타일 변경

HTML

```html
<p class="item">HTML</p>
<p class="item">CSS</p>
<p class="item">JavaScript</p>
```

JavaScript

```javascript
const items = document.querySelectorAll(".item");

for (let i = 0; i < items.length; i++) {

    items[i].style.color = "red";

}
```

모든 요소의 글자색이 빨간색으로 변경된다.

---

# 여러 요소의 클래스 추가

HTML

```html
<p class="item">HTML</p>
<p class="item">CSS</p>
<p class="item">JavaScript</p>
```

JavaScript

```javascript
const items = document.querySelectorAll(".item");

for (let i = 0; i < items.length; i++) {

    items[i].classList.add("active");

}
```

모든 요소에 `active` 클래스가 추가된다.

---

# forEach()

NodeList는 `forEach()`를 사용할 수도 있다.

```javascript
const items = document.querySelectorAll(".item");

items.forEach(function(item) {

    console.log(item.innerText);

});
```

결과

```text
HTML
CSS
JavaScript
```

---

# for문과 forEach() 비교

## for문

```javascript
for (let i = 0; i < items.length; i++) {

    console.log(items[i].innerText);

}
```

## forEach()

```javascript
items.forEach(function(item) {

    console.log(item.innerText);

});
```

두 방법 모두 같은 결과를 얻을 수 있다.

현재 국비교육 과정에서는 `for`문을 먼저 충분히 익힌 후 `forEach()`를 사용하는 것을 추천한다.

---

# classList

DOM 요소에는 클래스를 관리하기 위한 `classList` 프로퍼티가 있다.

HTML

```html
<div id="box" class="card"></div>
```

JavaScript

```javascript
const box = document.querySelector("#box");

console.log(box.classList);
```

`classList`를 이용하면 클래스를 추가하거나 삭제할 수 있다.

---

# classList.add()

클래스를 추가한다.

```javascript
box.classList.add("active");
```

결과

```html
<div id="box" class="card active"></div>
```

---

# classList.remove()

클래스를 제거한다.

```javascript
box.classList.remove("active");
```

결과

```html
<div id="box" class="card"></div>
```

---

# classList.toggle()

클래스가 없으면 추가하고, 있으면 제거한다.

```javascript
box.classList.toggle("active");
```

한 번 실행

```html
<div class="card active"></div>
```

다시 실행

```html
<div class="card"></div>
```

버튼 메뉴, 아코디언, 다크모드 등에서 자주 사용된다.

---

# classList.contains()

특정 클래스가 있는지 확인한다.

HTML

```html
<div class="quiz q2"></div>
```

JavaScript

```javascript
const quiz = document.querySelector(".quiz");

const result = quiz.classList.contains("q2");

console.log(result);
```

결과

```text
true
```

없는 클래스라면

```javascript
console.log(
    quiz.classList.contains("q3")
);
```

결과

```text
false
```

---

# contains() 오류가 발생하는 이유

다음 코드를 살펴보자.

```javascript
const quiz = document.querySelectorAll(".quiz");

quiz.classList.contains("q2");
```

오류가 발생한다.

이유는 `quiz`가 Element가 아니라 NodeList이기 때문이다.

NodeList에는 `classList`가 없다.

---

# 올바른 코드

첫 번째 요소

```javascript
const quiz = document.querySelectorAll(".quiz");

console.log(
    quiz[0].classList.contains("q1")
);
```

두 번째 요소

```javascript
console.log(
    quiz[1].classList.contains("q2")
);
```

또는 반복문을 사용한다.

```javascript
for (let i = 0; i < quiz.length; i++) {

    console.log(
        quiz[i].classList.contains("q2")
    );

}
```

---

# 실제 오류 분석

다음 코드를 살펴보자.

```javascript
let quiz2 = document.querySelectorAll("div.quiz");

let isQ2 = quiz2.classList.contains("q2");
```

다음과 같은 오류가 발생한다.

```text
Cannot read properties of undefined
```

또는

```text
Cannot read properties of NodeList
```

원인은 `quiz2`가 NodeList이기 때문이다.

`classList`는 각 요소(Element)에 존재한다.

---

# 해결 방법

첫 번째 방법

```javascript
let quiz2 = document.querySelectorAll("div.quiz");

let isQ2 =
quiz2[0].classList.contains("q2");
```

두 번째 방법

```javascript
for (let i = 0; i < quiz2.length; i++) {

    console.log(
        quiz2[i].classList.contains("q2")
    );

}
```

반드시 **NodeList → 요소(Element) → classList** 순서로 접근해야 한다.

```text
NodeList
 ↓
Element
 ↓
classList
```

---

# checked 요소 선택

체크된 체크박스

```javascript
const checked =
document.querySelector(
"[name=hobby]:checked"
);
```

체크된 라디오 버튼

```javascript
const size =
document.querySelector(
"[name=size]:checked"
);
```

선택된 요소가 있다면 Element를 반환한다.

선택되지 않았다면

```text
null
```

이 반환된다.

따라서 다음처럼 확인하는 것이 좋다.

```javascript
if (size !== null) {

    console.log(size.value);

}
```

---

# NodeList를 사용할 때 확인해야 할 사항

다음 내용을 항상 확인하면 많은 오류를 예방할 수 있다.

- 반환 결과가 Element인가?
- 반환 결과가 NodeList인가?
- `console.log()`로 결과를 확인했는가?
- `length`가 0은 아닌가?
- 인덱스를 올바르게 사용했는가?
- `classList`를 NodeList에 사용하지 않았는가?

---

# DOM 요소 선택 디버깅 순서

DOM 관련 오류가 발생하면 다음 순서대로 확인한다.

```text
1. console.log() 출력
        ↓
2. Element인가 NodeList인가?
        ↓
3. null인가?
        ↓
4. length 확인
        ↓
5. 선택자 확인
        ↓
6. script 실행 위치 확인
```

---

---

# 요소 선택 종합 실습

이번 실습에서는 하나의 요소와 여러 요소를 선택하고, 선택 결과에 따라 서로 다른 방식으로 DOM을 조작한다.

## HTML

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>DOM 요소 선택 실습</title>
    <script src="main.js" defer></script>
</head>
<body>

    <h1 id="title">프론트엔드 학습 목록</h1>

    <ul id="studyList">
        <li class="study-item html">HTML</li>
        <li class="study-item css">CSS</li>
        <li class="study-item javascript">JavaScript</li>
    </ul>

    <p id="result"></p>

</body>
</html>
```

## JavaScript

```javascript
const title = document.querySelector("#title");
const studyItems = document.querySelectorAll(".study-item");
const result = document.querySelector("#result");

console.log(title);
console.log(studyItems);
console.log(result);
```

각 변수의 선택 결과는 다음과 같다.

| 변수 | 선택 결과 |
|------|-----------|
| `title` | `h1` 요소 하나 |
| `studyItems` | 여러 `li` 요소가 들어 있는 NodeList |
| `result` | `p` 요소 하나 |

---

# 하나의 요소 변경하기

`title`은 요소 하나이므로 직접 `innerText`를 사용할 수 있다.

```javascript
title.innerText = "웹 개발 학습 목록";
```

다음과 같이 클래스를 추가할 수도 있다.

```javascript
title.classList.add("main-title");
```

요소 하나를 선택한 경우에는 해당 요소의 프로퍼티와 메서드를 직접 사용한다.

---

# 여러 요소 변경하기

`studyItems`는 NodeList이므로 반복문을 사용해야 한다.

```javascript
for (let i = 0; i < studyItems.length; i++) {

    studyItems[i].classList.add("active");

}
```

모든 `.study-item` 요소에 `active` 클래스가 추가된다.

---

# 특정 요소 확인하기

각 요소가 특정 클래스를 가지고 있는지 확인할 수 있다.

```javascript
for (let i = 0; i < studyItems.length; i++) {

    const isJavaScript =
        studyItems[i].classList.contains("javascript");

    console.log(isJavaScript);

}
```

결과

```text
false
false
true
```

세 번째 요소만 `javascript` 클래스를 가지고 있기 때문이다.

---

# 조건에 맞는 요소의 내용 변경하기

```javascript
for (let i = 0; i < studyItems.length; i++) {

    if (
        studyItems[i]
            .classList
            .contains("javascript")
    ) {

        studyItems[i].innerText =
            "JavaScript DOM";

    }

}
```

실행 결과

```text
HTML
CSS
JavaScript DOM
```

---

# 조건에 맞는 요소 개수 구하기

```javascript
let activeCount = 0;

for (let i = 0; i < studyItems.length; i++) {

    if (
        studyItems[i]
            .classList
            .contains("active")
    ) {

        activeCount++;

    }

}

result.innerText =
    `활성화된 항목: ${activeCount}개`;
```

객체 하나를 선택할 때와 NodeList를 선택할 때의 차이를 이해하면 여러 요소를 조건에 따라 처리할 수 있다.

---

# 체크박스 선택 실습

## HTML

```html
<h2>관심 분야</h2>

<label>
    <input
        type="checkbox"
        name="interest"
        value="HTML"
    >
    HTML
</label>

<label>
    <input
        type="checkbox"
        name="interest"
        value="CSS"
    >
    CSS
</label>

<label>
    <input
        type="checkbox"
        name="interest"
        value="JavaScript"
    >
    JavaScript
</label>

<button id="checkButton">선택 확인</button>

<p id="interestResult"></p>
```

---

## JavaScript

```javascript
const checkButton =
    document.querySelector("#checkButton");

const interests =
    document.querySelectorAll(
        "[name=interest]"
    );

const interestResult =
    document.querySelector(
        "#interestResult"
    );
```

`interests`에는 모든 관심 분야 체크박스가 들어 있는 NodeList가 저장된다.

---

# checked 프로퍼티 사용하기

체크박스가 선택되어 있는지는 `checked` 프로퍼티로 확인할 수 있다.

```javascript
console.log(interests[0].checked);
```

선택되어 있으면

```text
true
```

선택되어 있지 않으면

```text
false
```

가 반환된다.

---

# 선택된 체크박스 출력하기

```javascript
checkButton.addEventListener(
    "click",
    function() {

        let selectedResult = "";

        for (
            let i = 0;
            i < interests.length;
            i++
        ) {

            if (
                interests[i].checked
                === true
            ) {

                selectedResult +=
                    interests[i].value
                    + " ";

            }

        }

        interestResult.innerText =
            selectedResult;

    }
);
```

체크된 요소만 확인하여 해당 요소의 `value`를 출력한다.

---

# :checked 선택자 사용하기

버튼을 클릭한 시점에 선택된 체크박스만 다시 찾을 수도 있다.

```javascript
checkButton.addEventListener(
    "click",
    function() {

        const checkedInterests =
            document.querySelectorAll(
                "[name=interest]:checked"
            );

        let selectedResult = "";

        for (
            let i = 0;
            i < checkedInterests.length;
            i++
        ) {

            selectedResult +=
                checkedInterests[i].value
                + " ";

        }

        interestResult.innerText =
            selectedResult;

    }
);
```

`querySelectorAll()`을 사용했으므로 선택된 체크박스가 없어도 `null`이 반환되지 않는다.

선택된 요소가 없다면 빈 NodeList가 반환된다.

```text
NodeList(0)
```

---

# 라디오 버튼 선택 실습

## HTML

```html
<h2>사이즈 선택</h2>

<label>
    <input
        type="radio"
        name="size"
        value="Small"
    >
    Small
</label>

<label>
    <input
        type="radio"
        name="size"
        value="Medium"
    >
    Medium
</label>

<label>
    <input
        type="radio"
        name="size"
        value="Large"
    >
    Large
</label>

<button id="sizeButton">
    사이즈 확인
</button>

<p id="sizeResult"></p>
```

---

## JavaScript

```javascript
const sizeButton =
    document.querySelector(
        "#sizeButton"
    );

const sizeResult =
    document.querySelector(
        "#sizeResult"
    );
```

버튼을 클릭했을 때 선택된 라디오 버튼을 찾는다.

```javascript
sizeButton.addEventListener(
    "click",
    function() {

        const size =
            document.querySelector(
                "[name=size]:checked"
            );

        console.log(size);

    }
);
```

---

# 선택 여부 검사하기

선택된 라디오 버튼이 없다면 `size`에는 `null`이 저장된다.

따라서 `value`를 사용하기 전에 확인해야 한다.

```javascript
sizeButton.addEventListener(
    "click",
    function() {

        const size =
            document.querySelector(
                "[name=size]:checked"
            );

        if (size === null) {

            sizeResult.innerText =
                "사이즈를 선택해주세요.";

        } else {

            sizeResult.innerText =
                `선택한 사이즈: ${size.value}`;

        }

    }
);
```

---

# 실무 예제 프로젝트

## 상품 선택 결과 출력

사용자가 상품 옵션을 선택하면 선택된 값을 화면에 출력하는 예제이다.

### HTML

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>상품 옵션 선택</title>
    <script src="main.js" defer></script>
</head>
<body>

    <h1 id="productTitle">
        상품 주문
    </h1>

    <h2>사이즈</h2>

    <label>
        <input
            type="radio"
            name="size"
            value="Small"
        >
        Small
    </label>

    <label>
        <input
            type="radio"
            name="size"
            value="Large"
        >
        Large
    </label>

    <h2>추가 옵션</h2>

    <label>
        <input
            type="checkbox"
            class="option"
            value="치즈"
        >
        치즈
    </label>

    <label>
        <input
            type="checkbox"
            class="option"
            value="베이컨"
        >
        베이컨
    </label>

    <label>
        <input
            type="checkbox"
            class="option"
            value="소스"
        >
        소스
    </label>

    <button id="orderButton">
        주문 확인
    </button>

    <div id="orderResult"></div>

</body>
</html>
```

---

## JavaScript

```javascript
const orderButton =
    document.querySelector(
        "#orderButton"
    );

const options =
    document.querySelectorAll(
        ".option"
    );

const orderResult =
    document.querySelector(
        "#orderResult"
    );
```

---

## 주문 버튼 이벤트

```javascript
orderButton.addEventListener(
    "click",
    function() {

        const size =
            document.querySelector(
                "[name=size]:checked"
            );

        if (size === null) {

            orderResult.innerText =
                "사이즈를 선택해주세요.";

            return;

        }

        let optionResult = "";

        for (
            let i = 0;
            i < options.length;
            i++
        ) {

            if (
                options[i].checked
                === true
            ) {

                optionResult +=
                    options[i].value
                    + " ";

            }

        }

        if (optionResult === "") {

            optionResult = "선택 없음";

        }

        orderResult.innerText =
            `사이즈: ${size.value}
추가 옵션: ${optionResult}`;

    }
);
```

---

# 예제 코드 흐름

```text
1. 주문 버튼 요소를 선택한다.
2. 추가 옵션 전체를 NodeList로 선택한다.
3. 결과를 출력할 요소를 선택한다.
4. 버튼 클릭 시 선택된 라디오 버튼을 찾는다.
5. 라디오 버튼을 선택하지 않았다면 안내 문구를 출력한다.
6. NodeList를 반복하며 체크된 옵션을 찾는다.
7. 선택 결과를 문자열로 만든다.
8. 결과 요소의 innerText를 변경한다.
```

---

# 요소 선택 관련 오류 분석

## 오류 1: null에서 프로퍼티 사용

```javascript
const result =
    document.querySelector(
        "#orderResult"
    );

result.innerText = "주문 완료";
```

HTML에 `id="orderResult"`인 요소가 없다면 다음 오류가 발생한다.

```text
Cannot set properties of null
```

해결 방법은 선택 결과를 먼저 확인하는 것이다.

```javascript
console.log(result);
```

---

## 오류 2: NodeList에 classList 사용

```javascript
const items =
    document.querySelectorAll(
        ".item"
    );

items.classList.add("active");
```

`items`는 요소 하나가 아니라 NodeList이므로 오류가 발생한다.

올바른 코드

```javascript
for (
    let i = 0;
    i < items.length;
    i++
) {

    items[i]
        .classList
        .add("active");

}
```

---

## 오류 3: 존재하지 않는 인덱스 사용

```javascript
const items =
    document.querySelectorAll(
        ".item"
    );

console.log(items[5]);
```

선택된 요소가 세 개뿐이라면 `items[5]`의 결과는 다음과 같다.

```text
undefined
```

이 상태에서 `classList`를 사용하면 오류가 발생한다.

```javascript
items[5].classList.add("active");
```

오류 예시

```text
Cannot read properties of undefined
```

---

## 오류 4: 선택되지 않은 라디오 버튼의 value 사용

```javascript
const size =
    document.querySelector(
        "[name=size]:checked"
    );

console.log(size.value);
```

선택된 라디오 버튼이 없다면 `size`는 `null`이다.

따라서 다음처럼 검사해야 한다.

```javascript
if (size !== null) {

    console.log(size.value);

}
```

---

## 오류 5: getElementById()에 # 작성

잘못된 코드

```javascript
const title =
    document.getElementById(
        "#title"
    );
```

올바른 코드

```javascript
const title =
    document.getElementById(
        "title"
    );
```

`getElementById()`에는 실제 `id` 값만 전달한다.

---

## 오류 6: querySelector()의 class 선택자에서 . 생략

HTML

```html
<p class="message">
    안내 메시지
</p>
```

잘못된 코드

```javascript
const message =
    document.querySelector(
        "message"
    );
```

위 코드는 `message`라는 이름의 태그를 찾는다.

올바른 코드

```javascript
const message =
    document.querySelector(
        ".message"
    );
```

---

# 선택 메서드 결정하기

요소를 선택하기 전에 필요한 결과가 하나인지 여러 개인지 먼저 확인한다.

## 하나의 요소가 필요한 경우

```javascript
document.getElementById("title");
```

```javascript
document.querySelector("#title");
```

```javascript
document.querySelector(
    "[name=size]:checked"
);
```

---

## 여러 요소가 필요한 경우

```javascript
document.querySelectorAll(".item");
```

```javascript
document.querySelectorAll(
    "[name=interest]"
);
```

```javascript
document.querySelectorAll(
    "[name=interest]:checked"
);
```

---

# 반환 결과에 따른 처리 방법

| 반환 결과 | 처리 방법 |
|-----------|-----------|
| Element | 프로퍼티와 메서드를 직접 사용 |
| `null` | 선택자와 실행 시점 확인 |
| NodeList | 인덱스 또는 반복문 사용 |
| 빈 NodeList | `length`가 `0`인지 확인 |
| `undefined` | 사용한 인덱스가 존재하는지 확인 |

---

# 요소 선택 디버깅 체크리스트

DOM 요소 선택 코드에서 오류가 발생하면 다음 순서로 확인한다.

```text
1. JavaScript 파일이 연결되었는가?
2. JavaScript가 DOM 생성 후 실행되는가?
3. HTML에 대상 요소가 존재하는가?
4. id와 class의 철자가 같은가?
5. #과 .을 올바르게 사용했는가?
6. 선택 결과가 Element인가?
7. 선택 결과가 NodeList인가?
8. NodeList의 length는 몇 개인가?
9. 사용한 인덱스가 실제로 존재하는가?
10. null 또는 undefined 상태에서 프로퍼티를 사용하지 않았는가?
```

다음 코드를 먼저 작성하면 원인을 찾기 쉽다.

```javascript
console.log(target);
console.log(typeof target);
```

NodeList라면 다음 내용도 확인한다.

```javascript
console.log(target.length);
console.log(target[0]);
```

---

# 이번 문서에서 새롭게 배운 내용

- DOM 요소를 조작하려면 먼저 대상 요소를 선택해야 한다.
- `getElementById()`는 `id` 값을 이용하여 요소 하나를 선택한다.
- `querySelector()`는 CSS 선택자로 첫 번째 요소 하나를 선택한다.
- `querySelectorAll()`은 조건에 맞는 모든 요소를 NodeList로 반환한다.
- 요소 하나에는 `classList`, `innerText` 등을 직접 사용할 수 있다.
- NodeList에는 요소의 `classList`를 직접 사용할 수 없다.
- NodeList의 각 요소는 인덱스 또는 반복문으로 접근한다.
- `querySelector()`가 요소를 찾지 못하면 `null`을 반환한다.
- `querySelectorAll()`이 요소를 찾지 못하면 빈 NodeList를 반환한다.
- 선택된 체크박스와 라디오 버튼은 `:checked` 선택자로 찾을 수 있다.
- 체크박스의 선택 여부는 `checked` 프로퍼티로 확인할 수 있다.

---

# 자주 하는 실수

- `getElementById()`의 인수에 `#`을 작성한다.
- `querySelector()`에서 `id`와 `class` 선택자를 혼동한다.
- `querySelector()`가 여러 요소를 모두 반환한다고 생각한다.
- `querySelectorAll()`의 결과를 일반 Element로 생각한다.
- NodeList에 직접 `classList`를 사용한다.
- NodeList의 존재하지 않는 인덱스에 접근한다.
- 선택 결과를 확인하지 않고 바로 프로퍼티를 사용한다.
- 선택되지 않은 라디오 버튼의 `value`를 바로 사용한다.
- `querySelectorAll()`의 결과가 없으면 `null`이라고 생각한다.
- 단수형과 복수형 변수 이름을 구분하지 않는다.

---

# 면접 포인트

### getElementById()란?

HTML 요소의 `id` 값을 기준으로 요소 하나를 반환하는 메서드이다.

인수에는 `#`을 작성하지 않고 실제 `id` 값만 전달한다.

---

### querySelector()란?

CSS 선택자를 이용하여 조건에 맞는 첫 번째 요소 하나를 반환하는 메서드이다.

요소를 찾지 못하면 `null`을 반환한다.

---

### querySelectorAll()이란?

CSS 선택자와 일치하는 모든 요소를 NodeList 형태로 반환하는 메서드이다.

조건에 맞는 요소가 없어도 `null`이 아닌 빈 NodeList를 반환한다.

---

### querySelector()와 querySelectorAll()의 차이는?

`querySelector()`는 첫 번째 요소 하나를 반환한다.

`querySelectorAll()`은 조건에 맞는 모든 요소를 NodeList로 반환한다.

---

### NodeList란?

여러 DOM 노드를 저장하는 목록 형태의 객체이다.

배열처럼 인덱스와 `length`를 사용할 수 있지만 배열과 완전히 같은 자료형은 아니다.

---

### NodeList에 classList를 직접 사용할 수 없는 이유는?

`classList`는 개별 Element가 가지고 있는 프로퍼티이다.

NodeList는 여러 요소를 담은 목록이므로 인덱스나 반복문으로 개별 요소에 접근해야 한다.

---

### querySelector()와 querySelectorAll()이 요소를 찾지 못하면 어떻게 되는가?

`querySelector()`는 `null`을 반환한다.

`querySelectorAll()`은 길이가 `0`인 빈 NodeList를 반환한다.

---

### 체크된 라디오 버튼은 어떻게 선택하는가?

```javascript
document.querySelector(
    "[name=size]:checked"
);
```

선택된 요소가 없다면 `null`이 반환되므로 사용 전에 확인해야 한다.

---

# 핵심 정리

- DOM 조작은 요소 선택에서 시작한다.
- `getElementById()`는 `id` 값으로 요소 하나를 선택한다.
- `querySelector()`는 CSS 선택자로 첫 번째 요소를 선택한다.
- `querySelectorAll()`은 모든 일치 요소를 NodeList로 반환한다.
- Element와 NodeList는 서로 다른 방식으로 다뤄야 한다.
- Element에는 프로퍼티와 메서드를 직접 사용할 수 있다.
- NodeList는 인덱스 또는 반복문으로 각 요소에 접근한다.
- `classList`는 NodeList가 아닌 개별 Element에 사용한다.
- 단일 선택 결과가 없으면 `null`이 반환될 수 있다.
- 다중 선택 결과가 없으면 빈 NodeList가 반환된다.
- 선택 결과를 `console.log()`로 확인하는 습관이 중요하다.
- 변수 이름을 단수형과 복수형으로 구분하면 오류를 줄일 수 있다.

---

# 변경 이력

| Version | 날짜 | 변경 내용 |
|---------|------|-----------|
| v1.0 | 2026-07-22 | 최초 작성 |


