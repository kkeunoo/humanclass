---
title: JS_DOM_생성_삭제
version: v1.0
last_updated: 2026-07-22
status: completed
---

# 문서 정보

| 항목 | 내용 |
|------|------|
| 문서명 | JS_DOM_생성_삭제 |
| 분야 | Frontend / JavaScript |
| 버전 | v1.0 |
| 작성일 | 2026-07-22 |

---

# 개요

HTML은 처음 페이지가 로드될 때 화면을 구성한다.

하지만 실제 웹 서비스에서는 사용자의 동작에 따라 새로운 요소를 추가하거나 기존 요소를 삭제해야 하는 경우가 매우 많다.

예를 들어 다음과 같은 기능들이 있다.

- 댓글 추가
- 게시글 작성
- TODO 리스트
- 장바구니 상품 추가
- 알림 생성
- 채팅 메시지 추가

이러한 기능은 JavaScript를 이용해 DOM 요소를 동적으로 생성하거나 삭제하여 구현한다.

이번 문서에서는 요소 생성과 삭제에 필요한 기본 메서드를 학습한다.

---

# 핵심 개념

JavaScript는 새로운 HTML 요소를 만들고, 원하는 위치에 추가하거나 삭제할 수 있다.

대표적으로 다음 메서드를 사용한다.

- createElement()
- append()
- appendChild()
- prepend()
- before()
- after()
- remove()
- removeChild()
- cloneNode()

---

# DOM 생성 과정

```text
요소 생성
        ↓
내용 설정
        ↓
속성 설정
        ↓
DOM에 추가
        ↓
브라우저 화면 출력
```

---

# createElement()

새로운 HTML 요소를 생성한다.

## 기본 문법

```javascript
const element =
    document.createElement(
        "div"
    );
```

아직 화면에는 보이지 않는다.

생성만 되었을 뿐 DOM에는 추가되지 않은 상태이다.

---

# createElement() 예제

```javascript
const p =
    document.createElement(
        "p"
    );

console.log(p);
```

결과

```html
<p></p>
```

빈 `<p>` 요소가 생성된다.

---

# 생성한 요소에 내용 추가

```javascript
const p =
    document.createElement(
        "p"
    );

p.innerText =
    "안녕하세요.";
```

---

# append()

생성한 요소를 부모 요소의 **마지막 자식**으로 추가한다.

## HTML

```html
<div id="box">

</div>
```

---

## JavaScript

```javascript
const box =
    document.querySelector(
        "#box"
    );

const p =
    document.createElement(
        "p"
    );

p.innerText =
    "새로운 문장";

box.append(p);
```

결과

```html
<div id="box">

<p>새로운 문장</p>

</div>
```

---

# appendChild()

`appendChild()`도 마지막 자식으로 요소를 추가한다.

```javascript
box.appendChild(
    p
);
```

`append()`와 거의 비슷하게 사용된다.

---

# append()와 appendChild()

| 메서드 | 특징 |
|---------|------|
| append() | 문자열과 요소 모두 추가 가능 |
| appendChild() | DOM 요소(Node)만 추가 가능 |

> **실무 팁**  
> 최신 브라우저 환경에서는 `append()`를 많이 사용하지만, 기존 프로젝트나 강의에서는 `appendChild()`도 매우 자주 등장한다. 두 메서드 모두 익혀두는 것이 좋다.

---

# prepend()

새로운 요소를 **첫 번째 자식**으로 추가한다.

```javascript
box.prepend(
    p
);
```

---

# prepend() 예제

기존 HTML

```html
<div id="box">

<p>기존 요소</p>

</div>
```

JavaScript

```javascript
const p =
    document.createElement(
        "p"
    );

p.innerText =
    "첫 번째 요소";

box.prepend(
    p
);
```

결과

```html
<div id="box">

<p>첫 번째 요소</p>

<p>기존 요소</p>

</div>
```

---

---

# before()

`before()`는 선택한 요소의 **바로 앞**에 새로운 요소를 추가한다.

## HTML

```html
<p id="target">
기존 문장
</p>
```

---

## JavaScript

```javascript
const target =
    document.querySelector(
        "#target"
    );

const newP =
    document.createElement(
        "p"
    );

newP.innerText =
    "새로운 문장";

target.before(
    newP
);
```

결과

```html
<p>새로운 문장</p>

<p id="target">
기존 문장
</p>
```

---

# after()

`after()`는 선택한 요소의 **바로 뒤**에 새로운 요소를 추가한다.

```javascript
target.after(
    newP
);
```

결과

```html
<p id="target">
기존 문장
</p>

<p>새로운 문장</p>
```

---

# before()와 after() 비교

| 메서드 | 추가 위치 |
|---------|-----------|
| before() | 선택한 요소의 앞 |
| after() | 선택한 요소의 뒤 |

---

# remove()

`remove()`는 현재 요소를 DOM에서 삭제한다.

## HTML

```html
<p id="text">
삭제할 문장
</p>
```

## JavaScript

```javascript
const text =
    document.querySelector(
        "#text"
    );

text.remove();
```

결과

```html
<!-- 요소 삭제 -->
```

---

# removeChild()

부모 요소를 이용하여 자식을 삭제하는 방법이다.

## HTML

```html
<div id="box">

<p id="item">
삭제 대상
</p>

</div>
```

---

## JavaScript

```javascript
const box =
    document.querySelector(
        "#box"
    );

const item =
    document.querySelector(
        "#item"
    );

box.removeChild(
    item
);
```

---

# remove()와 removeChild()

| 메서드 | 특징 |
|---------|------|
| remove() | 요소 자신을 삭제 |
| removeChild() | 부모 요소가 자식을 삭제 |

> **실무 팁**  
> 최신 프로젝트에서는 `remove()`를 사용하는 경우가 많지만, 기존 코드나 라이브러리에서는 `removeChild()`도 자주 등장한다.

---

# cloneNode()

`cloneNode()`는 기존 요소를 복사한다.

기본 문법

```javascript
element.cloneNode();
```

---

# 얕은 복사

```javascript
const copy =
    element.cloneNode();
```

태그만 복사되고 내부 내용은 복사되지 않는다.

---

# 깊은 복사

```javascript
const copy =
    element.cloneNode(true);
```

`true`를 전달하면 자식 요소까지 함께 복사된다.

---

# cloneNode() 예제

## HTML

```html
<div id="card">

<h3>
HTML
</h3>

<p>
기초 과정
</p>

</div>
```

---

## JavaScript

```javascript
const card =
    document.querySelector(
        "#card"
    );

const copy =
    card.cloneNode(true);

document.body.append(
    copy
);
```

동일한 카드가 하나 더 생성된다.

---

# 요소 이동

이미 DOM에 존재하는 요소를 다시 `append()`하면 복사되는 것이 아니라 **이동**한다.

```javascript
box2.append(
    item
);
```

결과

```text
box1
↓

item

↓

box2
```

동일한 요소가 두 곳에 존재하지는 않는다.

---

# append()는 복사가 아니다

다음 코드는

```javascript
box.append(
    item
);
```

요소를 새로 만드는 것이 아니라 기존 요소를 새로운 위치로 이동시키는 코드이다.

복사가 필요하다면 `cloneNode(true)`를 사용해야 한다.

---

# 동적으로 목록 추가하기

## HTML

```html
<ul id="list">

</ul>
```

---

## JavaScript

```javascript
const list =
    document.querySelector(
        "#list"
    );

const li =
    document.createElement(
        "li"
    );

li.innerText =
    "JavaScript";

list.append(
    li
);
```

결과

```html
<ul>

<li>
JavaScript
</li>

</ul>
```

---

# 버튼으로 요소 추가하기

## HTML

```html
<button id="add">

추가

</button>

<ul id="list">

</ul>
```

---

## JavaScript

```javascript
const add =
    document.querySelector(
        "#add"
    );

const list =
    document.querySelector(
        "#list"
    );

add.addEventListener(
    "click",
    function(){

        const li =
            document.createElement(
                "li"
            );

        li.innerText =
            "새로운 항목";

        list.append(
            li
        );

    }
);
```

버튼을 누를 때마다 새로운 `<li>`가 생성된다.

---

# 실무 활용

DOM 생성과 삭제는 다음과 같은 기능에서 자주 사용된다.

- TODO 리스트
- 게시글 작성
- 댓글 추가
- 댓글 삭제
- 장바구니 상품 추가
- 알림 목록
- 채팅 메시지 출력
- FAQ 목록 생성

사용자의 동작에 따라 화면을 실시간으로 변경해야 하는 대부분의 기능에서 사용된다.

---

# DOM 생성/삭제 디버깅

문제가 발생하면 다음 사항을 확인한다.

```text
1. createElement()로 요소를 생성했는가?
2. append() 또는 appendChild()를 호출했는가?
3. 부모 요소를 올바르게 선택했는가?
4. remove() 대상이 존재하는가?
5. cloneNode(true)가 필요한 상황은 아닌가?
6. console.log()로 생성된 요소를 확인했는가?
```

---

---

# 실무 활용

DOM 생성과 삭제는 화면을 사용자와 상호작용하는 형태로 만드는 핵심 기술이다.

정적인 HTML만으로는 구현하기 어려운 기능들을 JavaScript를 이용해 실시간으로 처리할 수 있다.

대표적인 활용 사례는 다음과 같다.

- TODO 리스트
- 게시판
- 댓글 시스템
- 장바구니
- 쇼핑몰 상품 목록
- 알림(Notification)
- 채팅 프로그램
- FAQ 아코디언

---

# 실무 예제 프로젝트

이번 예제에서는 버튼을 눌러 할 일을 추가하고 삭제하는 간단한 TODO 리스트를 구현한다.

## HTML

```html
<input
    type="text"
    id="todoInput"
    placeholder="할 일을 입력하세요."
>

<button id="addBtn">

추가

</button>

<ul id="todoList">

</ul>
```

---

## JavaScript

```javascript
const input =
    document.querySelector(
        "#todoInput"
    );

const addBtn =
    document.querySelector(
        "#addBtn"
    );

const todoList =
    document.querySelector(
        "#todoList"
    );

addBtn.addEventListener(
    "click",
    function(){

        if(
            input.value.trim() === ""
        ){

            return;

        }

        const li =
            document.createElement(
                "li"
            );

        li.innerText =
            input.value;

        li.addEventListener(
            "click",
            function(){

                li.remove();

            }
        );

        todoList.append(
            li
        );

        input.value = "";

        input.focus();

    }
);
```

---

# 예제 코드 흐름

```text
사용자 입력
        ↓
추가 버튼 클릭
        ↓
공백 검사
        ↓
li 생성
        ↓
텍스트 입력
        ↓
ul에 추가
        ↓
입력창 초기화
        ↓
focus 이동
        ↓
항목 클릭 시 삭제
```

---

# CRUD와 DOM

DOM 생성과 삭제는 CRUD 중 Create와 Delete에 해당한다.

| CRUD | DOM 예시 |
|------|----------|
| Create | createElement(), append() |
| Read | querySelector() |
| Update | innerText, innerHTML, value |
| Delete | remove(), removeChild() |

> **실무 팁**  
> 게시판, 회원 관리, 상품 관리 화면은 대부분 CRUD 기능을 기반으로 만들어진다. DOM 조작은 이러한 화면을 구현하는 첫걸음이다.

---

# 오류 분석

## 오류 1

```javascript
const li =
    document.createElement("li");

li.innerText = "HTML";
```

생성만 했기 때문에 화면에는 나타나지 않는다.

올바른 코드

```javascript
list.append(
    li
);
```

DOM에 추가해야 화면에 출력된다.

---

## 오류 2

```javascript
document.querySelector(
    "#list"
).append(
    "<li>HTML</li>"
);
```

문자열은 그대로 텍스트로 처리된다.

요소를 추가하려면 `createElement()`를 사용하거나, 문자열을 추가할 목적이라면 `insertAdjacentHTML()`처럼 적절한 메서드를 사용한다.

---

## 오류 3

```javascript
const copy =
    card.cloneNode();
```

내부 내용까지 복사되지 않는다.

필요한 경우

```javascript
card.cloneNode(true);
```

를 사용한다.

---

## 오류 4

```javascript
box.append(
    item
);

anotherBox.append(
    item
);
```

요소가 복사되는 것이 아니라 마지막 위치로 이동한다.

동일한 요소를 여러 곳에서 사용하려면 복사본을 만들어야 한다.

---

# DOM 생성/삭제 디버깅 체크리스트

```text
1. createElement()를 호출했는가?
2. 생성한 요소를 append() 했는가?
3. 부모 요소를 올바르게 선택했는가?
4. remove()를 호출한 요소가 존재하는가?
5. cloneNode(true)가 필요한 상황은 아닌가?
6. 요소가 이동한 것인지 복사된 것인지 확인했는가?
7. console.log()로 생성된 요소를 확인했는가?
```

---

# 이번 문서에서 새롭게 배운 내용

- createElement()
- append()
- appendChild()
- prepend()
- before()
- after()
- remove()
- removeChild()
- cloneNode()
- 요소 이동
- 동적 요소 생성
- TODO 리스트 구현
- CRUD와 DOM의 관계

---

# 자주 하는 실수

- createElement()만 호출하고 DOM에 추가하지 않는 경우
- append()와 appendChild()의 차이를 이해하지 못하는 경우
- append()가 요소를 복사한다고 생각하는 경우
- cloneNode()에 `true`를 전달하지 않아 자식 요소가 복사되지 않는 경우
- remove()와 removeChild()를 혼동하는 경우
- 부모 요소를 잘못 선택하여 append()가 실패하는 경우

---

# 면접 포인트

### createElement()란 무엇인가?

새로운 HTML 요소(Node)를 생성하는 메서드이다.

생성만 할 뿐 화면에는 아직 추가되지 않는다.

---

### append()와 appendChild()의 차이는?

둘 다 마지막 자식으로 요소를 추가한다.

`append()`는 문자열과 요소를 모두 추가할 수 있지만, `appendChild()`는 Node만 추가할 수 있다.

---

### remove()와 removeChild()의 차이는?

`remove()`는 자기 자신을 삭제한다.

`removeChild()`는 부모 요소가 특정 자식 요소를 삭제한다.

---

### cloneNode(true)는 무엇인가?

기존 요소를 자식 요소까지 포함하여 깊은 복사하는 메서드이다.

---

### append()를 두 번 호출하면 복사되는가?

아니다.

기존 요소가 새로운 위치로 이동한다.

복사가 필요하면 `cloneNode(true)`를 사용한다.

---

# 핵심 정리

- `createElement()`는 새로운 요소를 생성한다.
- 생성한 요소는 `append()`, `appendChild()`, `prepend()` 등을 이용해 DOM에 추가해야 화면에 표시된다.
- `before()`와 `after()`는 선택한 요소의 앞뒤에 요소를 삽입한다.
- `remove()`와 `removeChild()`는 요소를 삭제한다.
- `cloneNode(true)`는 요소와 자식 요소를 함께 복사한다.
- `append()`는 요소를 복사하지 않고 이동시킨다.
- DOM 생성과 삭제는 대부분의 동적 웹 애플리케이션에서 핵심적으로 사용된다.

---

# 변경 이력

| Version | 날짜 | 변경 내용 |
|---------|------|-----------|
| v1.0 | 2026-07-22 | 최초 작성 |
