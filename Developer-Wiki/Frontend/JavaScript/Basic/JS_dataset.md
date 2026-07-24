---
title: JS_dataset
version: v1.0
last_updated: 2026-07-22
status: completed
---

# 문서 정보

| 항목 | 내용 |
|------|------|
| 문서명 | JS_dataset |
| 분야 | Frontend / JavaScript |
| 버전 | v1.0 |
| 작성일 | 2026-07-22 |

---

# 개요

HTML 요소에는 화면에 표시하지 않는 데이터를 저장해야 하는 경우가 많다.

예를 들어

- 상품 번호
- 회원 번호
- 게시글 번호
- 카테고리
- 가격
- 상태값

등의 데이터를 HTML 요소와 함께 저장하면 JavaScript에서 쉽게 사용할 수 있다.

이때 사용하는 것이 **`data-*` 속성**이며, JavaScript에서는 **`dataset` 객체**를 통해 접근한다.

이번 문서에서는 `dataset`을 이용하여 HTML에 데이터를 저장하고 읽고 수정하는 방법을 학습한다.

---

# 핵심 개념

`dataset`은 HTML 요소의 `data-*` 속성을 JavaScript에서 다룰 수 있도록 제공하는 객체이다.

즉,

```html
<div data-id="100"></div>
```

는 JavaScript에서

```javascript
element.dataset.id
```

로 접근할 수 있다.

---

# data-* 속성이란?

HTML에서 사용자 정의 데이터를 저장하기 위한 속성이다.

형식은 다음과 같다.

```html
data-이름="값"
```

예시

```html
<button
    data-id="101">

상품

</button>
```

또는

```html
<div
    data-name="홍길동">

회원

</div>
```

처럼 사용할 수 있다.

> **실무 팁**  
> `data-*` 속성은 화면에 보이지 않는 데이터를 HTML 요소와 함께 저장할 때 사용한다. 서버에서 전달받은 ID나 상태값을 별도의 전역 변수 없이 관리할 수 있어 많이 활용된다.

---

# dataset 객체

HTML

```html
<button
    id="btn"
    data-id="10">

버튼

</button>
```

JavaScript

```javascript
const btn =
    document.querySelector(
        "#btn"
    );

console.log(
    btn.dataset
);
```

출력 결과는 `DOMStringMap` 객체이며, `data-*` 속성들이 포함되어 있다.

---

# 데이터 읽기

HTML

```html
<button
    id="product"
    data-id="101">

상품

</button>
```

JavaScript

```javascript
const product =
    document.querySelector(
        "#product"
    );

console.log(
    product.dataset.id
);
```

출력

```text
101
```

---

# 여러 개의 데이터 저장

HTML

```html
<button
    id="item"
    data-id="101"
    data-name="노트북"
    data-price="1200000">

상품

</button>
```

JavaScript

```javascript
const item =
    document.querySelector(
        "#item"
    );

console.log(
    item.dataset.id
);

console.log(
    item.dataset.name
);

console.log(
    item.dataset.price
);
```

출력

```text
101
노트북
1200000
```

---

# dataset 구조

```text
HTML

data-id="101"
data-name="노트북"
data-price="1200000"

        ↓

dataset

id
name
price
```

---

# data-*와 dataset의 관계

| HTML | JavaScript |
|------|------------|
| data-id | dataset.id |
| data-name | dataset.name |
| data-price | dataset.price |
| data-category | dataset.category |

---

# camelCase 규칙

하이픈(`-`)이 포함된 이름은 JavaScript에서 camelCase로 변경된다.

HTML

```html
<div
    data-user-name="홍길동">

</div>
```

JavaScript

```javascript
const user =
    document.querySelector(
        "div"
    );

console.log(
    user.dataset.userName
);
```

출력

```text
홍길동
```

---

# dataset의 자료형

`dataset`으로 가져오는 값은 **항상 문자열(String)** 이다.

예를 들어

```html
<div
    data-price="5000">

</div>
```

```javascript
console.log(
    typeof box.dataset.price
);
```

출력

```text
string
```

숫자로 사용하려면 변환이 필요하다.

```javascript
const price =
    Number(
        box.dataset.price
    );
```

> **왜 이렇게 사용하는가?**  
> HTML 속성은 모두 문자열로 저장되기 때문에 `dataset`도 문자열을 반환한다. 계산이 필요한 경우에는 `Number()`, `parseInt()` 등을 이용해 숫자로 변환해야 한다.

---

---

# dataset 값 수정

`dataset`은 읽기뿐 아니라 값도 변경할 수 있다.

HTML

```html
<button
    id="product"
    data-price="10000">

상품

</button>
```

JavaScript

```javascript
const product =
    document.querySelector(
        "#product"
    );

product.dataset.price =
    "15000";

console.log(
    product.dataset.price
);
```

출력

```text
15000
```

HTML의 `data-price` 값도 함께 변경된다.

---

# 새로운 data 속성 추가

기존에 존재하지 않는 속성도 추가할 수 있다.

```javascript
const box =
    document.querySelector(
        "#box"
    );

box.dataset.category =
    "전자제품";
```

HTML

```html
<div
    id="box"
    data-category="전자제품">

</div>
```

처럼 추가된다.

---

# dataset과 이벤트

`dataset`은 이벤트와 함께 사용할 때 가장 많이 활용된다.

예를 들어 버튼마다 서로 다른 상품 번호를 저장할 수 있다.

## HTML

```html
<button
    class="product"
    data-id="101">

상품 1

</button>

<button
    class="product"
    data-id="102">

상품 2

</button>

<button
    class="product"
    data-id="103">

상품 3

</button>
```

---

## JavaScript

```javascript
const products =
    document.querySelectorAll(
        ".product"
    );

products.forEach(function(product){

    product.addEventListener(
        "click",
        function(){

            console.log(
                product.dataset.id
            );

        }
    );

});
```

출력

```text
101
102
103
```

클릭한 버튼의 상품 번호를 쉽게 확인할 수 있다.

---

# event.target과 함께 사용하기

`dataset`은 `event.target`과 함께 사용하는 경우가 매우 많다.

```javascript
products.forEach(function(product){

    product.addEventListener(
        "click",
        function(event){

            console.log(
                event.target.dataset.id
            );

        }
    );

});
```

이 방법은 클릭된 요소를 직접 가져오기 때문에 실무에서 자주 사용된다.

---

# 상품 목록 예제

## HTML

```html
<button
    class="item"
    data-name="노트북"
    data-price="1200000">

노트북

</button>

<button
    class="item"
    data-name="키보드"
    data-price="90000">

키보드

</button>
```

---

## JavaScript

```javascript
const items =
    document.querySelectorAll(
        ".item"
    );

items.forEach(function(item){

    item.addEventListener(
        "click",
        function(){

            console.log(
                item.dataset.name
            );

            console.log(
                item.dataset.price
            );

        }
    );

});
```

출력

```text
노트북
1200000

키보드
90000
```

---

# 게시글 번호 관리

게시판에서도 `dataset`을 많이 사용한다.

HTML

```html
<tr
    data-post-id="35">

...

</tr>
```

JavaScript

```javascript
const post =
    document.querySelector(
        "tr"
    );

console.log(
    post.dataset.postId
);
```

출력

```text
35
```

게시글 번호를 별도의 변수 없이 관리할 수 있다.

---

# classList와 함께 사용하기

```javascript
products.forEach(function(product){

    product.addEventListener(
        "click",
        function(){

            product.classList.add(
                "selected"
            );

            console.log(
                product.dataset.id
            );

        }
    );

});
```

클래스를 변경하면서 동시에 상품 번호를 사용할 수 있다.

---

# style과 함께 사용하기

```javascript
button.addEventListener(
    "click",
    function(){

        button.style.backgroundColor =
            "#4f46e5";

        console.log(
            button.dataset.id
        );

    }
);
```

이처럼 `dataset`은 이전에 배운 `style`, `classList`, `event`와 자연스럽게 함께 사용된다.

---

# 실무 활용

`dataset`은 다음과 같은 기능에서 자주 사용된다.

- 상품 번호 저장
- 게시글 번호 저장
- 회원 ID 저장
- 카테고리 구분
- 탭 메뉴
- 드롭다운 메뉴
- 슬라이드 인덱스
- 모달창 대상 정보
- 버튼 상태 관리

> **실무 팁**  
> 서버에서 받은 데이터를 화면에 출력할 때, 데이터베이스의 기본 키(ID)를 `data-id`에 저장해 두면 수정·삭제 버튼 클릭 시 해당 데이터를 쉽게 식별할 수 있다.

---

# dataset 디버깅

문제가 발생하면 다음 사항을 확인한다.

```text
1. data-* 속성이 HTML에 존재하는가?
2. dataset 이름을 camelCase로 작성했는가?
3. data-user-name → dataset.userName으로 접근했는가?
4. 값이 문자열(String)이라는 점을 고려했는가?
5. querySelector()와 querySelectorAll()를 올바르게 사용했는가?
6. event.target이 원하는 요소를 가리키는가?
```

---

---

# 실무 활용

`dataset`은 HTML 요소에 데이터를 저장하고 JavaScript에서 사용하는 가장 대표적인 방법이다.

특히 다음과 같은 기능에서 자주 사용된다.

- 상품 목록
- 게시판
- 회원 목록
- 장바구니
- 탭 메뉴
- FAQ
- 드롭다운 메뉴
- 이미지 슬라이더
- 관리자 페이지

JavaScript 코드와 화면의 데이터를 자연스럽게 연결할 수 있기 때문에 실무에서 매우 많이 사용된다.

---

# 실무 예제 프로젝트

이번 예제에서는 상품을 클릭하면 선택한 상품 정보를 출력하는 기능을 구현한다.

## HTML

```html
<ul>

    <li
        class="product"
        data-id="101"
        data-name="노트북"
        data-price="1200000">

        노트북

    </li>

    <li
        class="product"
        data-id="102"
        data-name="키보드"
        data-price="90000">

        키보드

    </li>

    <li
        class="product"
        data-id="103"
        data-name="마우스"
        data-price="35000">

        마우스

    </li>

</ul>
```

---

## JavaScript

```javascript
const products =
    document.querySelectorAll(
        ".product"
    );

products.forEach(function(product){

    product.addEventListener(
        "click",
        function(event){

            const target =
                event.target;

            console.log(
                "상품번호 :",
                target.dataset.id
            );

            console.log(
                "상품명 :",
                target.dataset.name
            );

            console.log(
                "가격 :",
                Number(target.dataset.price)
            );

        }
    );

});
```

---

# 예제 코드 흐름

```text
상품 클릭
      ↓
event.target
      ↓
dataset 접근
      ↓
상품 정보 읽기
      ↓
화면 출력 또는 서버 요청
```

---

# dataset와 localStorage

`dataset`과 `localStorage`는 함께 사용하는 경우가 많다.

예를 들어

```javascript
const id =
    event.target.dataset.id;

localStorage.setItem(
    "productId",
    id
);
```

처럼 선택한 상품 번호를 저장하여 다음 페이지에서도 사용할 수 있다.

> **실무 연결**  
> 다음 문서에서 학습할 `localStorage`는 `dataset`과 함께 자주 사용된다. 사용자가 클릭한 상품의 ID를 저장하거나 최근 본 상품 목록을 관리할 때 많이 활용된다.

---

# 오류 분석

## 오류 1

```javascript
console.log(
    box.dataset.user-name
);
```

JavaScript에서는 하이픈(`-`)을 사용할 수 없다.

올바른 코드

```javascript
console.log(
    box.dataset.userName
);
```

---

## 오류 2

```javascript
if(
    box.dataset.price > 1000
){
    ...
}
```

`dataset`의 값은 문자열이다.

필요하면 숫자로 변환한다.

```javascript
const price =
    Number(
        box.dataset.price
    );

if(price > 1000){

    ...

}
```

---

## 오류 3

```javascript
console.log(
    box.dataset.code
);
```

HTML에

```html
data-code
```

속성이 없으면 `undefined`가 출력된다.

먼저 HTML의 `data-*` 속성이 존재하는지 확인해야 한다.

---

## 오류 4

```javascript
const products =
    document.querySelectorAll(
        ".product"
    );

console.log(
    products.dataset.id
);
```

`querySelectorAll()`은 `NodeList`를 반환하므로 `dataset`을 직접 사용할 수 없다.

올바른 코드

```javascript
products.forEach(function(product){

    console.log(
        product.dataset.id
    );

});
```

또는

```javascript
const product =
    document.querySelector(
        ".product"
    );

console.log(
    product.dataset.id
);
```

---

# dataset 디버깅 체크리스트

```text
1. HTML에 data-* 속성이 존재하는가?
2. dataset 이름을 camelCase로 작성했는가?
3. data-user-name → dataset.userName으로 접근했는가?
4. dataset 값이 문자열(String)이라는 점을 고려했는가?
5. querySelectorAll()의 결과에 dataset을 사용하지 않았는가?
6. event.target이 원하는 요소를 가리키는가?
7. 개발자 도구에서 data-* 속성이 실제로 존재하는가?
```

---

# 이번 문서에서 새롭게 배운 내용

- data-* 속성
- dataset 객체
- 데이터 읽기
- 데이터 수정
- camelCase 규칙
- 문자열 자료형
- event와 함께 사용
- classList와 함께 사용
- style과 함께 사용
- 실무 데이터 관리 방법

---

# 자주 하는 실수

- `data-user-name`을 `dataset.user-name`으로 접근하는 경우
- `dataset` 값을 숫자로 착각하는 경우
- 존재하지 않는 `data-*` 속성에 접근하는 경우
- `querySelectorAll()`의 반환값에 `dataset`을 사용하는 경우
- `event.target` 대신 잘못된 요소를 참조하는 경우

---

# 면접 포인트

### dataset이란 무엇인가?

HTML의 `data-*` 속성에 저장된 사용자 정의 데이터를 JavaScript에서 쉽게 사용할 수 있도록 제공하는 객체이다.

---

### data-* 속성은 언제 사용하는가?

상품 ID, 게시글 번호, 회원 번호, 상태값처럼 화면에는 표시하지 않지만 JavaScript에서 필요한 데이터를 저장할 때 사용한다.

---

### dataset의 값은 어떤 자료형인가?

항상 문자열(String)이다.

계산이 필요한 경우에는 `Number()` 등을 사용해 숫자로 변환해야 한다.

---

### data-user-name은 JavaScript에서 어떻게 접근하는가?

```javascript
element.dataset.userName
```

하이픈(`-`)은 camelCase로 변환된다.

---

### querySelectorAll()에서 dataset을 사용할 수 없는 이유는?

`querySelectorAll()`은 `NodeList`를 반환한다.

`dataset`은 각각의 HTML 요소(Element)에 존재하므로 반복문을 사용하거나 하나의 요소를 선택해야 한다.

---

# 핵심 정리

- `data-*`는 HTML에 사용자 정의 데이터를 저장하는 속성이다.
- `dataset`은 `data-*` 속성을 JavaScript에서 다루는 객체이다.
- `dataset`의 값은 항상 문자열(String)이다.
- 하이픈(`-`)은 camelCase로 변환된다.
- `dataset`은 이벤트와 함께 사용할 때 가장 많이 활용된다.
- `dataset`, `classList`, `style`은 함께 사용하는 경우가 많다.
- 실무에서는 데이터와 화면을 연결하는 중요한 역할을 한다.

---

# 변경 이력

| Version | 날짜 | 변경 내용 |
|---------|------|-----------|
| v1.0 | 2026-07-22 | 최초 작성 |
