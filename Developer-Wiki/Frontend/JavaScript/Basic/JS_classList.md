---
title: JS_classList
version: v1.0
last_updated: 2026-07-22
status: completed
---

# 문서 정보

| 항목 | 내용 |
|------|------|
| 문서명 | JS_classList |
| 분야 | Frontend / JavaScript |
| 버전 | v1.0 |
| 작성일 | 2026-07-22 |

---

# 개요

HTML 요소의 class는 CSS 스타일을 적용하는 가장 기본적인 방법이다.

JavaScript에서는 class를 추가하거나 제거하여 화면을 동적으로 변경할 수 있다.

예를 들어

- 메뉴 활성화
- 다크모드
- 모달창 열기
- FAQ 펼치기
- 버튼 선택 상태

등 대부분의 UI는 class를 변경하여 구현한다.

이번 문서에서는 `classList` 객체를 이용한 class 조작 방법을 학습한다.

---

# 핵심 개념

HTML 요소는 여러 개의 class를 가질 수 있다.

JavaScript에서는 `classList`를 이용하여 class를 자유롭게 추가, 삭제, 확인할 수 있다.

대표 메서드는 다음과 같다.

- add()
- remove()
- toggle()
- contains()

---

# classList 구조

```text
요소 선택
      ↓
classList 접근
      ↓
add()
remove()
toggle()
contains()
      ↓
CSS 변경
      ↓
화면 변경
```

---

# classList란?

요소의 class 목록을 관리하는 객체이다.

```javascript
const box =
    document.querySelector(
        ".box"
    );

console.log(
    box.classList
);
```

브라우저 개발자 도구에서 현재 적용된 class 목록을 확인할 수 있다.

---

# 기본 문법

```javascript
element.classList.메서드();
```

예시

```javascript
box.classList.add(
    "active"
);
```

---

# 주요 메서드

## classList.add()

새로운 class를 추가한다.

```javascript
box.classList.add(
    "active"
);
```

HTML

```html
<div class="box active">

</div>
```

---

# add() 예제

```css
.active{

background:red;

}
```

```javascript
const box =
    document.querySelector(
        ".box"
    );

box.classList.add(
    "active"
);
```

빨간색 스타일이 적용된다.

---

# classList.remove()

class를 제거한다.

```javascript
box.classList.remove(
    "active"
);
```

제거된 class의 스타일도 함께 사라진다.

---

# add()와 remove()

| 메서드 | 기능 |
|---------|------|
| add() | class 추가 |
| remove() | class 제거 |

---

# classList.contains()

특정 class가 존재하는지 확인한다.

반환값은 Boolean이다.

```javascript
const result =
    box.classList.contains(
        "active"
    );

console.log(result);
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

# contains() 활용

```javascript
if(
    box.classList.contains(
        "active"
    )
){

    console.log(
        "활성화 상태"
    );

}
```

---

---

# classList.toggle()

`toggle()`은 class가 있으면 제거하고, 없으면 추가한다.

가장 많이 사용하는 `classList` 메서드이다.

## 기본 문법

```javascript
element.classList.toggle(
    "active"
);
```

---

# toggle() 동작

초기 상태

```html
<div class="box">

</div>
```

JavaScript

```javascript
box.classList.toggle(
    "active"
);
```

결과

```html
<div class="box active">

</div>
```

다시 실행하면

```html
<div class="box">

</div>
```

로 돌아온다.

---

# toggle() 예제

## HTML

```html
<button id="btn">

클릭

</button>

<div class="box">

내용

</div>
```

---

## CSS

```css
.box{

display:none;

}

.box.active{

display:block;

}
```

---

## JavaScript

```javascript
const btn =
    document.querySelector(
        "#btn"
    );

const box =
    document.querySelector(
        ".box"
    );

btn.addEventListener(
    "click",
    function(){

        box.classList.toggle(
            "active"
        );

    }
);
```

버튼을 누를 때마다 내용이 나타났다가 사라진다.

---

# className과 classList

JavaScript에는 `className`도 존재한다.

```javascript
box.className =
    "active";
```

하지만 기존 class가 모두 덮어쓰기 된다.

예를 들어

```html
<div class="box card">

</div>
```

에서

```javascript
box.className =
    "active";
```

를 실행하면

```html
<div class="active">

</div>
```

가 된다.

기존의 `box`, `card` 클래스는 모두 사라진다.

---

# className과 classList 비교

| 항목 | className | classList |
|------|-----------|-----------|
| 기존 class 유지 | ❌ | ✅ |
| class 추가 | 불편 | 쉬움 |
| class 제거 | 직접 처리 | remove() |
| 실무 사용 빈도 | 낮음 | 매우 높음 |

> **실무 팁**  
> 특별한 이유가 없다면 `className`보다 `classList`를 사용하는 것이 안전하다. 기존 클래스를 유지한 채 필요한 클래스만 추가하거나 제거할 수 있기 때문이다.

---

# 메뉴 활성화

## HTML

```html
<button class="menu">
HTML
</button>

<button class="menu">
CSS
</button>

<button class="menu">
JavaScript
</button>
```

---

## JavaScript

```javascript
const menus =
    document.querySelectorAll(
        ".menu"
    );

menus.forEach(function(menu){

    menu.addEventListener(
        "click",
        function(){

            menu.classList.add(
                "active"
            );

        }
    );

});
```

클릭한 버튼에 `active` 클래스가 추가된다.

> **참고**  
> 이 예제는 클릭한 버튼에 `active`를 추가하는 기본 예제이다. 실제 탭 메뉴처럼 하나만 활성화하려면 기존 `active`를 먼저 제거하는 과정이 필요하며, 이후 실전 프로젝트에서 다룬다.

---

# 다크 모드 만들기

## HTML

```html
<button id="mode">

다크모드

</button>

<body>

...
```

---

## CSS

```css
.dark{

background:#222;

color:white;

}
```

---

## JavaScript

```javascript
const mode =
    document.querySelector(
        "#mode"
    );

mode.addEventListener(
    "click",
    function(){

        document.body.classList.toggle(
            "dark"
        );

    }
);
```

버튼을 누를 때마다 다크모드가 적용되고 해제된다.

---

# contains()와 toggle() 함께 사용하기

```javascript
if(
    box.classList.contains(
        "active"
    )
){

    console.log(
        "현재 활성화"
    );

}
else{

    console.log(
        "비활성화"
    );

}
```

현재 상태를 확인한 뒤 필요한 처리를 할 수 있다.

---

# 아코디언 메뉴 예제

```javascript
question.addEventListener(
    "click",
    function(){

        answer.classList.toggle(
            "open"
        );

    }
);
```

CSS에서 `.open` 클래스에 높이나 표시 여부를 지정하면 FAQ 형태의 아코디언 메뉴를 구현할 수 있다.

---

# 실무 활용

`classList`는 다음과 같은 UI에서 매우 자주 사용된다.

- 햄버거 메뉴
- 다크모드
- 탭 메뉴
- FAQ 아코디언
- 모달창
- 슬라이드 메뉴
- 드롭다운 메뉴
- 선택된 버튼 표시
- 현재 페이지 메뉴 강조

---

# classList 디버깅

문제가 발생하면 다음 사항을 확인한다.

```text
1. 요소를 올바르게 선택했는가?
2. CSS 클래스 이름이 정확한가?
3. classList.add()와 remove()를 올바르게 사용했는가?
4. toggle()가 의도한 위치에서 호출되는가?
5. contains()의 반환값을 확인했는가?
6. 개발자 도구에서 class가 실제로 추가되는지 확인했는가?
```

---

---

# 실무 활용

`classList`는 JavaScript와 CSS를 연결하는 가장 중요한 기능 중 하나이다.

HTML 구조를 변경하지 않고도 CSS 클래스만 추가하거나 제거하여 다양한 UI를 구현할 수 있다.

대표적인 활용 사례는 다음과 같다.

- 다크 모드
- 햄버거 메뉴
- FAQ 아코디언
- 탭 메뉴
- 모달창 열기/닫기
- 드롭다운 메뉴
- 슬라이드 메뉴
- 선택된 버튼 강조
- 현재 페이지 메뉴 표시

---

# 실무 예제 프로젝트

이번 예제에서는 클릭한 메뉴만 활성화되는 간단한 탭 메뉴를 구현한다.

## HTML

```html
<div class="menu-container">

<button class="menu active">
HTML
</button>

<button class="menu">
CSS
</button>

<button class="menu">
JavaScript
</button>

</div>
```

---

## CSS

```css
.menu{

background:white;

color:black;

}

.menu.active{

background:#4f46e5;

color:white;

}
```

---

## JavaScript

```javascript
const menus =
    document.querySelectorAll(
        ".menu"
    );

menus.forEach(function(menu){

    menu.addEventListener(
        "click",
        function(){

            menus.forEach(function(item){

                item.classList.remove(
                    "active"
                );

            });

            menu.classList.add(
                "active"
            );

        }
    );

});
```

---

# 예제 코드 흐름

```text
메뉴 클릭
      ↓
모든 active 제거
      ↓
클릭한 메뉴 선택
      ↓
active 추가
      ↓
CSS 변경
      ↓
활성 메뉴 표시
```

---

# 오류 분석

## 오류 1

```javascript
const menus =
    document.querySelectorAll(
        ".menu"
    );

menus.classList.add(
    "active"
);
```

`querySelectorAll()`은 `NodeList`를 반환하므로 `classList`를 사용할 수 없다.

올바른 코드

```javascript
menus.forEach(function(menu){

    menu.classList.add(
        "active"
    );

});
```

또는 하나의 요소만 선택하려면

```javascript
const menu =
    document.querySelector(
        ".menu"
    );

menu.classList.add(
    "active"
);
```

---

## 오류 2

```javascript
box.className =
    "active";
```

기존 클래스가 모두 사라진다.

올바른 코드

```javascript
box.classList.add(
    "active"
);
```

---

## 오류 3

```javascript
box.classList.contains(
    "active"
);
```

반환값을 사용하지 않는 경우

```javascript
const isActive =
    box.classList.contains(
        "active"
    );

if(isActive){

    console.log(
        "활성화"
    );

}
```

Boolean 값을 변수에 저장하거나 조건문에서 활용하는 것이 좋다.

---

## 오류 4

```javascript
box.classList.toggle(
    "active"
);

box.classList.toggle(
    "active"
);
```

같은 코드가 연속으로 실행되면 첫 번째는 클래스를 추가하고 두 번째는 바로 제거하므로 결과적으로 변화가 없는 것처럼 보일 수 있다.

---

# classList 디버깅 체크리스트

```text
1. querySelector()와 querySelectorAll()를 구분했는가?
2. NodeList에 classList를 사용하지 않았는가?
3. CSS 클래스 이름이 정확한가?
4. className과 classList를 혼동하지 않았는가?
5. toggle()가 중복 호출되고 있지 않은가?
6. contains()의 반환값을 확인했는가?
7. 개발자 도구에서 class가 실제로 추가되는지 확인했는가?
```

---

# 이번 문서에서 새롭게 배운 내용

- classList 객체
- classList.add()
- classList.remove()
- classList.toggle()
- classList.contains()
- className과 classList의 차이
- 메뉴 활성화 구현
- 다크 모드 구현
- 아코디언 구현 원리
- NodeList와 Element의 차이

---

# 자주 하는 실수

- `querySelectorAll()`의 결과에 `classList`를 사용하는 경우
- `className`으로 기존 클래스를 모두 덮어쓰는 경우
- `toggle()`를 연속 호출하여 상태가 바로 원래대로 돌아가는 경우
- CSS 클래스 이름과 JavaScript 문자열이 일치하지 않는 경우
- `contains()`의 반환값을 활용하지 않는 경우

---

# 면접 포인트

### classList란 무엇인가?

HTML 요소의 클래스를 관리하는 객체이다.

클래스를 추가, 제거, 확인, 토글하는 기능을 제공한다.

---

### add()와 remove()의 역할은?

- `add()`는 클래스를 추가한다.
- `remove()`는 클래스를 제거한다.

---

### toggle()은 언제 사용하는가?

클래스가 있으면 제거하고, 없으면 추가한다.

메뉴, 다크 모드, 아코디언처럼 상태를 전환하는 UI에서 많이 사용한다.

---

### contains()는 무엇을 반환하는가?

특정 클래스의 존재 여부를 `true` 또는 `false`로 반환한다.

---

### className과 classList의 차이는?

`className`은 클래스 문자열 전체를 변경한다.

`classList`는 기존 클래스를 유지하면서 필요한 클래스만 추가하거나 제거할 수 있다.

---

### querySelectorAll()에서 classList를 사용할 수 없는 이유는?

`querySelectorAll()`은 하나의 요소가 아니라 `NodeList`를 반환하기 때문이다.

`classList`는 각각의 HTML 요소(Element)에 존재한다.

---

# 핵심 정리

- `classList`는 HTML 요소의 클래스를 관리하는 객체이다.
- `add()`는 클래스를 추가한다.
- `remove()`는 클래스를 제거한다.
- `toggle()`은 클래스의 추가와 제거를 자동으로 전환한다.
- `contains()`는 클래스 존재 여부를 확인한다.
- `className`은 기존 클래스를 덮어쓰므로 주의해야 한다.
- `querySelectorAll()`의 반환값에는 직접 `classList`를 사용할 수 없다.
- `classList`는 대부분의 동적인 UI 구현에서 핵심적으로 사용된다.

---

# 변경 이력

| Version | 날짜 | 변경 내용 |
|---------|------|-----------|
| v1.0 | 2026-07-22 | 최초 작성 |
