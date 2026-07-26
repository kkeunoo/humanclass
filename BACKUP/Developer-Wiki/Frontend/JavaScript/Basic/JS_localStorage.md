---
title: JS_localStorage
version: v1.0
last_updated: 2026-07-22
status: completed
---

# 문서 정보

| 항목 | 내용 |
|------|------|
| 문서명 | JS_localStorage |
| 분야 | Frontend / JavaScript |
| 버전 | v1.0 |
| 작성일 | 2026-07-22 |

---

# 개요

일반 변수에 저장한 데이터는 브라우저를 새로고침하거나 종료하면 모두 사라진다.

하지만 로그인 상태, 다크 모드 설정, 최근 본 상품처럼 브라우저를 다시 열어도 유지되어야 하는 데이터가 있다.

이럴 때 사용하는 것이 **localStorage**이다.

`localStorage`는 브라우저에 데이터를 저장하는 Web Storage API 중 하나이며, 저장된 데이터는 브라우저를 종료해도 유지된다.

이번 문서에서는 `localStorage`를 이용하여 데이터를 저장하고, 읽고, 삭제하는 방법과 객체 및 배열을 저장하는 방법을 학습한다.

---

# 핵심 개념

`localStorage`는 브라우저에 **Key(이름) - Value(값)** 형태로 데이터를 저장하는 객체이다.

모든 데이터는 문자열(String) 형태로 저장된다.

```text
Key            Value

theme      →   dark

userName   →   홍길동

productId  →   101
```

---

# localStorage 특징

- 브라우저에 저장된다.
- 브라우저를 종료해도 유지된다.
- 문자열(String)만 저장할 수 있다.
- 같은 도메인에서 사용할 수 있다.
- 개발자 도구에서 확인할 수 있다.

---

# localStorage 구조

```text
JavaScript

↓

localStorage

↓

Key

↓

Value

↓

브라우저 저장
```

---

# 데이터 저장

기본 문법

```javascript
localStorage.setItem(
    "key",
    "value"
);
```

예시

```javascript
localStorage.setItem(
    "user",
    "홍길동"
);
```

---

# 데이터 읽기

기본 문법

```javascript
localStorage.getItem(
    "key"
);
```

예시

```javascript
const user =
    localStorage.getItem(
        "user"
    );

console.log(user);
```

출력

```text
홍길동
```

---

# 데이터 수정

같은 Key로 다시 저장하면 기존 값이 변경된다.

```javascript
localStorage.setItem(
    "user",
    "김철수"
);
```

기존 `"홍길동"`은 `"김철수"`로 변경된다.

---

# 데이터 삭제

```javascript
localStorage.removeItem(
    "user"
);
```

`user` 데이터만 삭제된다.

---

# 전체 데이터 삭제

```javascript
localStorage.clear();
```

저장된 모든 데이터가 삭제된다.

> **실무 팁**  
> `clear()`는 해당 사이트의 모든 localStorage 데이터를 삭제하므로, 필요한 데이터만 삭제할 때는 `removeItem()`을 사용하는 것이 안전하다.

---

# 데이터 존재 여부 확인

```javascript
const theme =
    localStorage.getItem(
        "theme"
    );

console.log(theme);
```

저장된 값이 없다면

```text
null
```

이 반환된다.

따라서 다음과 같이 확인하는 경우가 많다.

```javascript
if (
    localStorage.getItem("theme")
) {

    console.log("데이터 존재");

}
```

---

# 문자열만 저장되는 이유

`localStorage`는 모든 값을 문자열(String)로 저장한다.

예를 들어

```javascript
localStorage.setItem(
    "age",
    20
);
```

저장된 값은 `"20"`이다.

```javascript
console.log(
    typeof localStorage.getItem("age")
);
```

출력

```text
string
```

> **왜 이렇게 사용하는가?**  
> `localStorage`는 브라우저 내부 저장소이기 때문에 데이터 형식을 구분하지 않고 문자열로 저장한다. 객체나 배열은 다음 Part에서 학습할 `JSON.stringify()`를 이용하여 문자열로 변환한 뒤 저장한다.

---

---

# JSON.stringify()

객체(Object)와 배열(Array)은 `localStorage`에 그대로 저장할 수 없다.

따라서 먼저 문자열(JSON)로 변환해야 한다.

이때 사용하는 메서드가 `JSON.stringify()`이다.

기본 문법

```javascript
JSON.stringify(
    객체
);
```

---

# 객체 저장

```javascript
const user = {

    name : "홍길동",

    age : 20

};

localStorage.setItem(

    "user",

    JSON.stringify(user)

);
```

브라우저에는 다음과 같이 문자열로 저장된다.

```text
{"name":"홍길동","age":20}
```

---

# JSON.parse()

저장된 JSON 문자열을 다시 객체로 변환하는 메서드이다.

기본 문법

```javascript
JSON.parse(
    문자열
);
```

---

# 객체 읽기

```javascript
const user =

    JSON.parse(

        localStorage.getItem("user")

    );

console.log(user.name);

console.log(user.age);
```

출력

```text
홍길동

20
```

---

# 배열 저장

```javascript
const fruits = [

    "사과",

    "바나나",

    "포도"

];

localStorage.setItem(

    "fruits",

    JSON.stringify(fruits)

);
```

---

# 배열 읽기

```javascript
const fruits =

    JSON.parse(

        localStorage.getItem("fruits")

    );

console.log(fruits);
```

출력

```text
["사과", "바나나", "포도"]
```

---

# 다크 모드 저장

## HTML

```html
<button id="modeBtn">

다크모드

</button>
```

---

## JavaScript

```javascript
const modeBtn =

    document.querySelector(

        "#modeBtn"

    );

modeBtn.addEventListener(

    "click",

    function(){

        document.body.classList.toggle(

            "dark"

        );

        localStorage.setItem(

            "theme",

            "dark"

        );

    }

);
```

새로고침 후에도 저장된 값을 사용할 수 있다.

---

# 저장된 다크 모드 적용

```javascript
const theme =

    localStorage.getItem(

        "theme"

    );

if(theme === "dark"){

    document.body.classList.add(

        "dark"

    );

}
```

페이지가 다시 열려도 다크 모드가 유지된다.

> **실무 팁**  
> 실제 서비스에서는 페이지가 로드되자마자 `localStorage`를 확인하여 사용자의 설정을 먼저 적용한 뒤 화면을 출력한다.

---

# dataset과 함께 사용하기

앞에서 학습한 `dataset`과 함께 사용하는 경우가 많다.

```javascript
button.addEventListener(

    "click",

    function(event){

        localStorage.setItem(

            "productId",

            event.target.dataset.id

        );

    }

);
```

다음 페이지에서는

```javascript
const id =

    localStorage.getItem(

        "productId"

    );
```

로 선택한 상품 번호를 가져올 수 있다.

---

# TODO 목록 저장

```javascript
const todos = [

    "공부하기",

    "운동하기"

];

localStorage.setItem(

    "todos",

    JSON.stringify(todos)

);
```

다시 가져오기

```javascript
const todos =

    JSON.parse(

        localStorage.getItem(

            "todos"

        )

    );
```

---

# localStorage와 sessionStorage 차이

| localStorage | sessionStorage |
|--------------|----------------|
| 브라우저 종료 후에도 유지 | 브라우저 종료 시 삭제 |
| 장기간 데이터 저장 | 일시적인 데이터 저장 |
| 자동 로그인 | 로그인 세션, 임시 정보 |

---

# 실무 활용

`localStorage`는 다음과 같은 기능에서 자주 사용된다.

- 다크 모드 저장
- 자동 로그인 여부 저장
- 최근 본 상품
- 장바구니
- 검색 기록
- TODO 목록
- 사용자 설정
- 언어 설정

---

# localStorage 디버깅

문제가 발생하면 다음 사항을 확인한다.

```text
1. Key 이름이 정확한가?
2. JSON.stringify()를 사용했는가?
3. JSON.parse()를 사용했는가?
4. getItem()의 반환값이 null은 아닌가?
5. 문자열(String)로 저장된다는 점을 이해했는가?
6. 개발자 도구 → Application → Local Storage에서 저장 여부를 확인했는가?
```

---

---

# 실무 예제 프로젝트

이번 예제에서는 사용자가 마지막으로 선택한 상품을 `localStorage`에 저장하고, 페이지를 다시 열어도 선택 상태를 유지하는 기능을 구현한다.

## HTML

```html
<button
    class="product"
    data-id="101">

노트북

</button>

<button
    class="product"
    data-id="102">

키보드

</button>

<button
    class="product"
    data-id="103">

마우스

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
        function(event){

            const id =
                event.target.dataset.id;

            localStorage.setItem(
                "selectedProduct",
                id
            );

        }
    );

});
```

---

## 페이지가 열릴 때

```javascript
const selected =
    localStorage.getItem(
        "selectedProduct"
    );

console.log(selected);
```

출력

```text
101
```

사용자가 마지막으로 선택한 상품 번호를 계속 사용할 수 있다.

---

# 예제 코드 흐름

```text
상품 클릭
      ↓
event.target.dataset.id
      ↓
localStorage.setItem()
      ↓
브라우저 저장
      ↓
새로고침
      ↓
localStorage.getItem()
      ↓
선택 정보 복원
```

---

# localStorage와 classList

저장된 설정을 이용하여 클래스를 적용하는 경우가 많다.

```javascript
const theme =
    localStorage.getItem(
        "theme"
    );

if(theme === "dark"){

    document.body.classList.add(
        "dark"
    );

}
```

---

# localStorage와 style

```javascript
const fontSize =
    localStorage.getItem(
        "fontSize"
    );

if(fontSize){

    document.body.style.fontSize =
        fontSize;

}
```

사용자가 선택한 글자 크기를 유지할 수 있다.

---

# 자주 하는 실수

## 객체를 그대로 저장하는 경우

잘못된 코드

```javascript
const user = {

    name : "홍길동"

};

localStorage.setItem(
    "user",
    user
);
```

브라우저에는

```text
[object Object]
```

가 저장된다.

올바른 코드

```javascript
localStorage.setItem(

    "user",

    JSON.stringify(user)

);
```

---

## JSON.parse()를 하지 않는 경우

```javascript
const user =

    localStorage.getItem(
        "user"
    );

console.log(user.name);
```

문자열이므로 원하는 값이 출력되지 않는다.

올바른 코드

```javascript
const user =

    JSON.parse(

        localStorage.getItem(
            "user"
        )

    );

console.log(user.name);
```

---

## 없는 Key를 읽는 경우

```javascript
const user =

    localStorage.getItem(
        "user"
    );
```

저장된 값이 없다면

```text
null
```

이 반환된다.

따라서

```javascript
if(user){

    ...

}
```

처럼 먼저 확인하는 것이 좋다.

---

## clear()를 남용하는 경우

```javascript
localStorage.clear();
```

모든 데이터가 삭제된다.

실무에서는 필요한 데이터만 삭제하도록 `removeItem()`을 사용하는 것이 일반적이다.

---

# 디버깅 체크리스트

```text
1. Key 이름이 정확한가?
2. setItem()과 getItem()의 Key가 같은가?
3. JSON.stringify()를 사용했는가?
4. JSON.parse()를 사용했는가?
5. null 여부를 확인했는가?
6. Application → Local Storage에서 저장 상태를 확인했는가?
7. 브라우저 콘솔에 오류는 없는가?
```

---

# 이번 문서에서 배운 내용

- localStorage 개념
- Key-Value 구조
- setItem()
- getItem()
- removeItem()
- clear()
- JSON.stringify()
- JSON.parse()
- 객체 저장
- 배열 저장
- 다크 모드 저장
- 사용자 설정 저장
- dataset과 함께 사용

---

# 면접 포인트

### localStorage란 무엇인가?

브라우저에 데이터를 저장하는 Web Storage API이다.

브라우저를 종료해도 데이터가 유지된다.

---

### localStorage에는 어떤 자료형이 저장되는가?

모든 데이터는 문자열(String)로 저장된다.

객체와 배열은 `JSON.stringify()`로 문자열로 변환하여 저장해야 한다.

---

### JSON.stringify()는 왜 사용하는가?

객체나 배열을 JSON 문자열로 변환하여 `localStorage`에 저장하기 위해 사용한다.

---

### JSON.parse()는 언제 사용하는가?

`localStorage`에서 읽어온 JSON 문자열을 다시 객체나 배열로 복원할 때 사용한다.

---

### localStorage와 sessionStorage의 차이점은?

- `localStorage`는 브라우저를 종료해도 데이터가 유지된다.
- `sessionStorage`는 브라우저(탭)를 닫으면 데이터가 삭제된다.

---

# 핵심 정리

- `localStorage`는 브라우저에 데이터를 저장한다.
- 데이터는 Key-Value 형태로 관리된다.
- 모든 값은 문자열(String)이다.
- 객체와 배열은 `JSON.stringify()`로 저장한다.
- 사용할 때는 `JSON.parse()`로 복원한다.
- `dataset`, `classList`, `style`, `event`와 함께 자주 사용된다.
- 사용자 설정, 다크 모드, 최근 본 상품 등 다양한 기능에 활용된다.

---

# 변경 이력

| Version | 날짜 | 변경 내용 |
|---------|------|-----------|
| v1.0 | 2026-07-22 | 최초 작성 |
