---
title: JS_style_조작
version: v1.0
last_updated: 2026-07-22
status: completed
---

# 문서 정보

| 항목 | 내용 |
|------|------|
| 문서명 | JS_style_조작 |
| 분야 | Frontend / JavaScript |
| 버전 | v1.0 |
| 작성일 | 2026-07-22 |

---

# 개요

CSS는 웹 페이지의 디자인을 담당한다.

JavaScript에서는 `style` 객체를 이용하여 CSS 속성을 직접 변경할 수 있다.

예를 들어

- 글자색 변경
- 배경색 변경
- 요소 숨기기
- 크기 변경
- 위치 이동

등을 JavaScript에서 실시간으로 제어할 수 있다.

이번 문서에서는 `style` 객체를 이용한 스타일 변경 방법과 `classList`와의 차이를 학습한다.

---

# 핵심 개념

HTML 요소는 `style` 객체를 가지고 있다.

JavaScript에서는 이 객체를 이용하여 CSS 속성을 직접 변경할 수 있다.

대표적으로 다음과 같은 속성을 많이 사용한다.

- color
- backgroundColor
- fontSize
- width
- height
- display
- visibility
- opacity

---

# style 구조

```text
요소 선택
      ↓
style 접근
      ↓
CSS 속성 변경
      ↓
브라우저 화면 변경
```

---

# style 객체

HTML 요소의 인라인 스타일을 관리하는 객체이다.

```javascript
const box =
    document.querySelector(
        ".box"
    );

console.log(
    box.style
);
```

브라우저 개발자 도구에서 `CSSStyleDeclaration` 객체를 확인할 수 있다.

---

# 기본 문법

```javascript
element.style.속성 =
    "값";
```

예시

```javascript
box.style.color =
    "red";
```

---

# CSS와 JavaScript 속성명 차이

CSS에서는 속성명을 `-`(하이픈)으로 작성한다.

```css
background-color
```

JavaScript에서는 **camelCase**를 사용한다.

```javascript
backgroundColor
```

대표적인 예시는 다음과 같다.

| CSS | JavaScript |
|------|------------|
| background-color | backgroundColor |
| font-size | fontSize |
| margin-top | marginTop |
| border-radius | borderRadius |

---

# 글자색 변경

## HTML

```html
<p id="text">
안녕하세요.
</p>
```

---

## JavaScript

```javascript
const text =
    document.querySelector(
        "#text"
    );

text.style.color =
    "red";
```

글자색이 빨간색으로 변경된다.

---

# 배경색 변경

```javascript
text.style.backgroundColor =
    "yellow";
```

배경색이 노란색으로 변경된다.

---

# 글자 크기 변경

```javascript
text.style.fontSize =
    "30px";
```

단위를 함께 작성해야 한다.

---

# width와 height

```javascript
box.style.width =
    "300px";

box.style.height =
    "150px";
```

요소의 크기가 변경된다.

---

# display

`display`는 요소를 화면에 표시하거나 숨길 때 사용한다.

```javascript
box.style.display =
    "none";
```

요소가 화면에서 사라진다.

다시 보이게 하려면

```javascript
box.style.display =
    "block";
```

을 사용한다.

> **실무 팁**  
> `display`는 요소 자체를 화면에서 제거한 것처럼 동작한다. 레이아웃도 함께 변경되므로, 단순히 보이기/숨기기 기능에서 자주 사용된다.

---

---

# visibility

`visibility`는 요소를 화면에서 보이지 않게 만들거나 다시 표시할 때 사용한다.

## 기본 문법

```javascript
element.style.visibility =
    "hidden";
```

다시 표시하려면

```javascript
element.style.visibility =
    "visible";
```

을 사용한다.

---

# display와 visibility의 차이

| 속성 | 화면 표시 | 공간 유지 |
|------|-----------|-----------|
| display: none | ❌ | ❌ |
| visibility: hidden | ❌ | ✅ |

예를 들어

```html
<div>A</div>

<div>B</div>

<div>C</div>
```

에서 B에

```javascript
style.visibility =
    "hidden";
```

을 적용하면

```text
A

(빈 공간)

C
```

처럼 공간은 그대로 유지된다.

반면

```javascript
style.display =
    "none";
```

을 적용하면

```text
A

C
```

처럼 공간도 함께 사라진다.

> **실무 팁**  
> 레이아웃을 유지하면서 잠시 숨겨야 하는 경우에는 `visibility`를, 레이아웃까지 함께 변경해야 하는 경우에는 `display`를 사용한다.

---

# opacity

`opacity`는 요소의 투명도를 조절한다.

값은 **0부터 1까지** 사용할 수 있다.

```javascript
box.style.opacity =
    "0";
```

완전히 투명하다.

```javascript
box.style.opacity =
    "0.5";
```

반투명 상태이다.

```javascript
box.style.opacity =
    "1";
```

완전히 보이는 상태이다.

---

# opacity 예제

```javascript
const image =
    document.querySelector(
        "#image"
    );

image.style.opacity =
    "0.3";
```

이미지가 흐리게 표시된다.

---

# 버튼으로 요소 숨기기

## HTML

```html
<button id="hide">

숨기기

</button>

<div id="box">

내용

</div>
```

---

## JavaScript

```javascript
const hide =
    document.querySelector(
        "#hide"
    );

const box =
    document.querySelector(
        "#box"
    );

hide.addEventListener(
    "click",
    function(){

        box.style.display =
            "none";

    }
);
```

버튼을 클릭하면 요소가 사라진다.

---

# 버튼으로 요소 보이기

```javascript
show.addEventListener(
    "click",
    function(){

        box.style.display =
            "block";

    }
);
```

---

# style과 classList 비교

두 방법 모두 화면을 변경할 수 있지만 목적이 다르다.

| style | classList |
|--------|-----------|
| 인라인 스타일 변경 | CSS 클래스 변경 |
| 한두 개 속성 변경에 적합 | 여러 스타일 변경에 적합 |
| 재사용성 낮음 | 재사용성 높음 |
| CSS와 분리 어려움 | CSS와 역할 분리 가능 |

---

# 언제 style을 사용할까?

다음과 같은 경우에 적합하다.

- width 변경
- height 변경
- 위치 이동
- 투명도 변경
- 색상 변경
- 계산된 값 적용

예시

```javascript
box.style.width =
    "350px";
```

---

# 언제 classList를 사용할까?

다음과 같은 경우에 적합하다.

- 다크 모드
- 메뉴 활성화
- 모달창 열기
- FAQ
- 슬라이드
- 애니메이션 적용

예시

```javascript
box.classList.add(
    "active"
);
```

---

# 모달창 예제

## HTML

```html
<button id="open">

열기

</button>

<div id="modal">

모달창

</div>
```

---

## CSS

```css
#modal{

display:none;

}
```

---

## JavaScript

```javascript
const open =
    document.querySelector(
        "#open"
    );

const modal =
    document.querySelector(
        "#modal"
    );

open.addEventListener(
    "click",
    function(){

        modal.style.display =
            "block";

    }
);
```

실무에서는 여기에 닫기 버튼을 추가하여 `display = "none"`으로 다시 숨기는 경우가 많다.

> **실무 팁**  
> 간단한 예제에서는 `style.display`를 사용해도 되지만, 실제 프로젝트에서는 `.open`, `.active` 같은 클래스를 추가·제거하는 방식이 유지보수에 더 유리하다.

---

# 실무 활용

`style`은 다음과 같은 기능에서 자주 사용된다.

- 진행률 표시
- 로딩 바
- 드래그 이동
- 크기 변경
- 위치 변경
- 투명도 조절
- 애니메이션 시작 값 설정

---

# style 디버깅

문제가 발생하면 다음 사항을 확인한다.

```text
1. 요소를 올바르게 선택했는가?
2. CSS 속성명을 camelCase로 작성했는가?
3. 단위(px, %, rem 등)를 함께 작성했는가?
4. display와 visibility를 혼동하지 않았는가?
5. 개발자 도구에서 style 속성이 적용되었는가?
6. classList와 style 중 어떤 방식이 적절한지 확인했는가?
```

---

---

# 실무 활용

`style` 객체는 요소의 CSS 속성을 직접 변경할 수 있기 때문에 사용자의 동작에 따라 화면을 즉시 변경해야 하는 기능에서 자주 사용된다.

대표적인 활용 사례는 다음과 같다.

- 진행률(Progress Bar)
- 로딩 화면
- 이미지 확대/축소
- 드래그 앤 드롭
- 요소 이동
- 크기 조절
- 투명도 변경
- 간단한 애니메이션

---

# 실무 예제 프로젝트

이번 예제에서는 버튼을 클릭하여 안내 패널을 열고 닫는 기능을 구현한다.

## HTML

```html
<button id="toggleBtn">

패널 열기

</button>

<div id="panel">

공지사항입니다.

</div>
```

---

## CSS

```css
#panel{

display:none;

padding:20px;

background:#eeeeee;

}
```

---

## JavaScript

```javascript
const toggleBtn =
    document.querySelector(
        "#toggleBtn"
    );

const panel =
    document.querySelector(
        "#panel"
    );

toggleBtn.addEventListener(
    "click",
    function(){

        if(
            panel.style.display ===
            "block"
        ){

            panel.style.display =
                "none";

            toggleBtn.innerText =
                "패널 열기";

        }
        else{

            panel.style.display =
                "block";

            toggleBtn.innerText =
                "패널 닫기";

        }

    }
);
```

---

# 예제 코드 흐름

```text
버튼 클릭
      ↓
display 값 확인
      ↓
block인가?
      ↓
예 → none 변경
아니오 → block 변경
      ↓
버튼 글자 변경
```

---

# style보다 classList를 사용하는 경우

다음과 같은 코드는 가능하다.

```javascript
modal.style.display =
    "block";

modal.style.backgroundColor =
    "#ffffff";

modal.style.border =
    "1px solid #cccccc";

modal.style.padding =
    "20px";

modal.style.borderRadius =
    "10px";
```

하지만 스타일 속성이 많아질수록 JavaScript 코드가 복잡해진다.

이럴 때는 CSS에 클래스를 미리 정의한 뒤 `classList`를 사용하는 것이 좋다.

```css
.modal-open{

display:block;

background:#ffffff;

border:1px solid #cccccc;

padding:20px;

border-radius:10px;

}
```

```javascript
modal.classList.add(
    "modal-open"
);
```

이처럼 **디자인은 CSS**, **동작은 JavaScript**가 담당하도록 역할을 분리하면 유지보수가 쉬워진다.

---

# 오류 분석

## 오류 1

```javascript
box.style.background-color =
    "red";
```

JavaScript에서는 하이픈(`-`)을 사용할 수 없다.

올바른 코드

```javascript
box.style.backgroundColor =
    "red";
```

---

## 오류 2

```javascript
box.style.width =
    300;
```

단위를 작성하지 않아 원하는 크기가 적용되지 않을 수 있다.

올바른 코드

```javascript
box.style.width =
    "300px";
```

---

## 오류 3

```javascript
box.style.display =
    "hidden";
```

`display`에는 `"hidden"`이라는 값이 없다.

올바른 코드

```javascript
box.style.display =
    "none";
```

또는

```javascript
box.style.visibility =
    "hidden";
```

상황에 따라 적절한 속성을 선택해야 한다.

---

## 오류 4

```javascript
box.style.opacity =
    100;
```

`opacity`는 0부터 1 사이의 값을 사용한다.

올바른 코드

```javascript
box.style.opacity =
    "0.5";
```

---

# style 디버깅 체크리스트

```text
1. 요소를 올바르게 선택했는가?
2. style 속성을 camelCase로 작성했는가?
3. px, %, rem 등의 단위를 작성했는가?
4. display와 visibility를 혼동하지 않았는가?
5. opacity 값이 0~1 범위인가?
6. 개발자 도구에서 style 속성이 실제로 적용되었는가?
7. style보다 classList가 더 적합한 상황은 아닌가?
```

---

# 이번 문서에서 새롭게 배운 내용

- style 객체
- color
- backgroundColor
- fontSize
- width
- height
- display
- visibility
- opacity
- camelCase 속성명
- style과 classList의 차이

---

# 자주 하는 실수

- CSS 속성명을 그대로 사용하는 경우
- 단위를 작성하지 않는 경우
- `display`와 `visibility`를 혼동하는 경우
- `opacity`를 0~1 범위가 아닌 값으로 사용하는 경우
- 여러 스타일을 모두 JavaScript에서 직접 작성하는 경우
- CSS에서 처리해야 할 부분까지 `style`로 제어하는 경우

---

# 면접 포인트

### style 객체란 무엇인가?

HTML 요소의 인라인 스타일을 제어하는 객체이다.

JavaScript를 이용하여 CSS 속성을 직접 변경할 수 있다.

---

### CSS와 JavaScript의 속성명이 다른 이유는?

CSS는 `background-color`처럼 하이픈 표기법을 사용하지만,

JavaScript에서는 camelCase인 `backgroundColor`를 사용한다.

---

### display와 visibility의 차이는?

`display: none`은 요소와 공간을 모두 제거한다.

`visibility: hidden`은 요소만 숨기고 공간은 유지한다.

---

### opacity는 무엇인가?

요소의 투명도를 조절하는 속성이다.

0은 완전 투명, 1은 완전히 보이는 상태이다.

---

### style과 classList는 언제 구분해서 사용하는가?

`style`은 한두 개의 스타일을 즉시 변경할 때 적합하다.

`classList`는 여러 스타일을 한 번에 적용하거나 재사용 가능한 UI를 만들 때 적합하다.

---

# 핵심 정리

- `style` 객체는 요소의 인라인 스타일을 변경한다.
- CSS 속성명은 JavaScript에서 camelCase로 작성한다.
- `display`는 요소와 공간을 함께 제어한다.
- `visibility`는 공간을 유지한 채 요소만 숨긴다.
- `opacity`는 요소의 투명도를 조절한다.
- 여러 스타일을 함께 적용할 때는 `classList`가 유지보수에 유리하다.
- 실무에서는 **디자인은 CSS, 동작은 JavaScript**로 역할을 분리하는 것이 일반적이다.

---

# 변경 이력

| Version | 날짜 | 변경 내용 |
|---------|------|-----------|
| v1.0 | 2026-07-22 | 최초 작성 |
