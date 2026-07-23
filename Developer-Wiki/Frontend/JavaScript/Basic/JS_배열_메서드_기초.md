---
title: JavaScript 배열 메서드 기초
version: v1.0
last_updated: 2026-07-22
status: Completed
---

# JavaScript 배열 메서드 기초

## 문서 정보

| 항목 | 내용 |
|------|------|
| 문서명 | JavaScript 배열 메서드 기초 |
| 분류 | Frontend / JavaScript / Basic |
| 난이도 | Beginner |
| 선수 지식 | JavaScript 배열 |
| 핵심 주제 | push, pop, shift, unshift, indexOf, includes, join, reverse, sort |
| 버전 | v1.0 |
| 최종 수정일 | 2026-07-22 |

---

# 개요

배열(Array)은 데이터를 저장하는 것뿐만 아니라 **다양한 메서드(Method)를 이용하여 데이터를 쉽게 관리**할 수 있다.

배열 메서드를 사용하면

- 데이터 추가
- 데이터 삭제
- 데이터 검색
- 데이터 연결
- 데이터 순서 변경

등의 작업을 간단하게 수행할 수 있다.

실무에서는 배열 메서드를 매우 자주 사용한다.

---

# 메서드(Method)란?

메서드(Method)는 **객체가 가지고 있는 기능(함수)** 을 의미한다.

예를 들어 배열에는 다양한 메서드가 준비되어 있다.

```javascript
const fruits = [
    "사과",
    "바나나"
];

fruits.push("포도");
```

여기서

```javascript
fruits.push()
```

의 `push()`가 배열 메서드이다.

> **참고**
>
> 메서드(Method)는 객체(Object)를 학습하면서 더 자세히 다룬다.
> 현재는 "배열이 제공하는 기능" 정도로 이해하면 충분하다.

---

# push()

`push()`는 **배열의 마지막에 요소를 추가**한다.

기본 문법

```javascript
배열.push(추가할 값);
```

---

## 예제

```javascript
const fruits = [
    "사과",
    "바나나"
];

fruits.push("포도");

console.log(fruits);
```

결과

```text
["사과", "바나나", "포도"]
```

---

## 여러 개 추가

```javascript
const numbers = [
    1,
    2
];

numbers.push(3, 4, 5);

console.log(numbers);
```

결과

```text
[1, 2, 3, 4, 5]
```

한 번에 여러 개의 요소도 추가할 수 있다.

---

# pop()

`pop()`은 **배열의 마지막 요소를 제거**한다.

기본 문법

```javascript
배열.pop();
```

---

## 예제

```javascript
const fruits = [
    "사과",
    "바나나",
    "포도"
];

fruits.pop();

console.log(fruits);
```

결과

```text
["사과", "바나나"]
```

---

## 제거한 값 반환

`pop()`은 삭제한 요소를 반환한다.

```javascript
const fruits = [
    "사과",
    "바나나",
    "포도"
];

const removed = fruits.pop();

console.log(removed);
console.log(fruits);
```

결과

```text
포도
["사과", "바나나"]
```

---

# push()와 pop()

두 메서드는 항상 함께 많이 사용된다.

| 메서드 | 역할 |
|--------|------|
| `push()` | 마지막 요소 추가 |
| `pop()` | 마지막 요소 제거 |

둘 다 **배열의 끝(마지막 요소)** 을 기준으로 동작한다.

---

# shift()

`shift()`는 **배열의 첫 번째 요소를 제거**한다.

기본 문법

```javascript
배열.shift();
```

---

## 예제

```javascript
const fruits = [
    "사과",
    "바나나",
    "포도"
];

fruits.shift();

console.log(fruits);
```

결과

```text
["바나나", "포도"]
```

첫 번째 요소가 제거되고 나머지 요소들이 앞으로 한 칸씩 이동한다.

---

---

# unshift()

`unshift()`는 **배열의 첫 번째 위치에 요소를 추가**한다.

기본 문법

```javascript
배열.unshift(추가할 값);
```

---

## 예제

```javascript id="f8gk2r"
const fruits = [
    "바나나",
    "포도"
];

fruits.unshift("사과");

console.log(fruits);
```

결과

```text id="9sj6pb"
["사과", "바나나", "포도"]
```

기존 요소들은 뒤로 한 칸씩 이동한다.

---

## 여러 개 추가

```javascript id="g2t1nx"
const numbers = [
    3,
    4
];

numbers.unshift(1, 2);

console.log(numbers);
```

결과

```text id="v74n0k"
[1, 2, 3, 4]
```

`unshift()`도 여러 개의 요소를 한 번에 추가할 수 있다.

---

# shift()와 unshift()

두 메서드는 배열의 **앞(첫 번째 요소)** 을 기준으로 동작한다.

| 메서드 | 역할 |
|--------|------|
| `shift()` | 첫 번째 요소 제거 |
| `unshift()` | 첫 번째 요소 추가 |

반면 `push()`와 `pop()`은 배열의 **끝(마지막 요소)** 을 기준으로 동작한다.

---

# indexOf()

`indexOf()`는 **특정 요소의 인덱스를 찾는 메서드**이다.

기본 문법

```javascript
배열.indexOf(찾을 값);
```

---

## 예제

```javascript id="7h1j8m"
const fruits = [
    "사과",
    "바나나",
    "포도"
];

console.log(fruits.indexOf("바나나"));
```

결과

```text id="m5y8pa"
1
```

`"바나나"`는 인덱스 `1`에 있으므로 `1`을 반환한다.

---

## 없는 값 찾기

찾는 값이 없으면 `-1`을 반환한다.

```javascript id="ph4n8e"
const fruits = [
    "사과",
    "바나나",
    "포도"
];

console.log(fruits.indexOf("딸기"));
```

결과

```text id="v8gq6m"
-1
```

실무에서는 `-1`인지 확인하여 데이터 존재 여부를 판단하는 경우가 많다.

---

# includes()

`includes()`는 **배열에 특정 값이 포함되어 있는지 확인**하는 메서드이다.

기본 문법

```javascript
배열.includes(찾을 값);
```

---

## 예제

```javascript id="k4v3rb"
const fruits = [
    "사과",
    "바나나",
    "포도"
];

console.log(fruits.includes("포도"));
console.log(fruits.includes("딸기"));
```

결과

```text id="f1dqaz"
true
false
```

`includes()`는 `true` 또는 `false`를 반환한다.

---

# indexOf()와 includes() 비교

두 메서드는 모두 데이터를 찾을 때 사용하지만 반환값이 다르다.

| 메서드 | 반환값 |
|--------|---------|
| `indexOf()` | 인덱스 또는 `-1` |
| `includes()` | `true` 또는 `false` |

예를 들어

```javascript id="t9e4mc"
const menu = [
    "피자",
    "햄버거",
    "파스타"
];

console.log(menu.indexOf("햄버거"));
console.log(menu.includes("햄버거"));
```

결과

```text id="u0z9jh"
1
true
```

---

# join()

`join()`은 **배열의 요소를 하나의 문자열로 연결**하는 메서드이다.

기본 문법

```javascript
배열.join(구분자);
```

---

## 예제

```javascript id="n3w1te"
const fruits = [
    "사과",
    "바나나",
    "포도"
];

console.log(fruits.join(", "));
```

결과

```text id="q6t0lr"
사과, 바나나, 포도
```

구분자를 변경하면 다양한 형태로 연결할 수 있다.

```javascript id="w8n5ga"
console.log(fruits.join(" / "));
```

결과

```text id="b7x4yu"
사과 / 바나나 / 포도
```

---

# join() 활용 예제

화면에 목록을 출력하기 전에 문자열을 만드는 경우 자주 사용한다.

```javascript id="h2m6pv"
const subjects = [
    "HTML",
    "CSS",
    "JavaScript"
];

const result = subjects.join(" → ");

console.log(result);
```

결과

```text id="c9r2ok"
HTML → CSS → JavaScript
```

---

# 배열 메서드 사용 시 주의사항

- `push()`와 `pop()`은 배열의 **끝**에서 동작한다.
- `shift()`와 `unshift()`는 배열의 **앞**에서 동작한다.
- `indexOf()`는 값을 찾지 못하면 `-1`을 반환한다.
- `includes()`는 `true` 또는 `false`를 반환한다.
- `join()`의 결과는 **배열이 아닌 문자열(String)** 이다.

---

---

# reverse()

`reverse()`는 **배열의 요소 순서를 반대로 뒤집는 메서드**이다.

기본 문법

```javascript
배열.reverse();
```

---

## 예제

```javascript
const fruits = [
    "사과",
    "바나나",
    "포도"
];

fruits.reverse();

console.log(fruits);
```

결과

```text
["포도", "바나나", "사과"]
```

배열의 첫 번째 요소와 마지막 요소의 위치가 서로 바뀐다.

---

## 원본 배열 변경

`reverse()`는 **원본 배열 자체를 변경**한다.

```javascript
const numbers = [
    1,
    2,
    3
];

numbers.reverse();

console.log(numbers);
```

결과

```text
[3, 2, 1]
```

`reverse()`를 실행하면 새로운 배열이 만들어지는 것이 아니라 기존 배열이 변경된다.

---

# sort()

`sort()`는 **배열의 요소를 정렬하는 메서드**이다.

기본 문법

```javascript
배열.sort();
```

---

## 문자열 정렬

```javascript
const fruits = [
    "포도",
    "사과",
    "바나나"
];

fruits.sort();

console.log(fruits);
```

결과

```text
["바나나", "사과", "포도"]
```

문자열은 기본적으로 **사전(유니코드) 순서**로 정렬된다.

---

## 숫자 정렬 시 주의사항

숫자를 그대로 `sort()`하면 기대한 결과와 다를 수 있다.

```javascript
const numbers = [
    10,
    2,
    30,
    5
];

numbers.sort();

console.log(numbers);
```

결과

```text
[10, 2, 30, 5]
```

또는

```text
[10, 2, 5, 30]
```

처럼 **문자열 기준**으로 정렬되어 원하는 결과가 나오지 않을 수 있다.

> **참고**
>
> 숫자를 올바르게 정렬하는 방법은 비교 함수(Compare Function)를 사용해야 한다.
> 이는 함수 심화 및 배열 메서드 심화 문서에서 자세히 학습한다.

---

# reverse()와 sort() 비교

| 메서드 | 역할 |
|--------|------|
| `reverse()` | 요소의 순서를 반대로 뒤집는다. |
| `sort()` | 요소를 정렬한다. |

둘 다 **원본 배열을 직접 변경(Mutating)** 하는 메서드이다.

---

# 배열 메서드 조합

배열 메서드는 함께 사용할 수도 있다.

```javascript
const fruits = [
    "포도",
    "사과",
    "바나나"
];

fruits.sort();
fruits.reverse();

console.log(fruits);
```

결과

```text
["포도", "사과", "바나나"]
```

먼저 오름차순으로 정렬한 후 순서를 뒤집으면 내림차순과 비슷한 결과를 얻을 수 있다.

> **참고**
>
> 숫자 배열에서는 이 방법이 항상 올바른 내림차순 정렬을 보장하지 않는다.
> 숫자 정렬은 비교 함수를 사용하는 방법을 이후 문서에서 학습한다.

---

# 자주 사용하는 배열 메서드 정리

| 메서드 | 설명 |
|--------|------|
| `push()` | 마지막에 요소 추가 |
| `pop()` | 마지막 요소 제거 |
| `shift()` | 첫 번째 요소 제거 |
| `unshift()` | 첫 번째 요소 추가 |
| `indexOf()` | 요소의 인덱스 검색 |
| `includes()` | 요소 포함 여부 확인 |
| `join()` | 문자열로 연결 |
| `reverse()` | 순서 뒤집기 |
| `sort()` | 정렬 |

---

# 배열 메서드 작성 원칙

실무에서는 다음과 같은 원칙을 자주 사용한다.

- 데이터를 추가할 때는 `push()`를 우선 고려한다.
- 데이터 존재 여부만 확인할 때는 `includes()`가 읽기 쉽다.
- 위치가 필요한 경우에는 `indexOf()`를 사용한다.
- 문자열을 만들 때는 `join()`을 활용한다.
- `reverse()`와 `sort()`는 원본 배열을 변경한다는 점을 항상 기억한다.

---

# 실무에서 자주 사용하는 패턴

## 메뉴 존재 여부 확인

```javascript
const menu = [
    "피자",
    "햄버거",
    "파스타"
];

if (menu.includes("피자")) {

    console.log("판매 중");

}
```

---

## 마지막 데이터 삭제

```javascript
const history = [
    "페이지1",
    "페이지2",
    "페이지3"
];

history.pop();

console.log(history);
```

---

## 화면에 문자열 출력

```javascript
const skills = [
    "HTML",
    "CSS",
    "JavaScript"
];

console.log(skills.join(", "));
```

---

---

# 실무 예제 프로젝트

다음은 장바구니에 상품을 추가하고 삭제한 뒤 화면에 출력하는 간단한 예제이다.

## HTML

```html
<h2>장바구니</h2>

<p id="cart"></p>
```

---

## JavaScript

```javascript
const cart = [
    "노트북",
    "마우스"
];

// 상품 추가
cart.push("키보드");

// 마지막 상품 삭제
cart.pop();

const result = document.querySelector("#cart");

result.textContent = cart.join(", ");
```

실행 결과

```text
노트북, 마우스
```

배열 메서드를 이용하면 데이터를 쉽게 추가·삭제하고 원하는 형태의 문자열로 출력할 수 있다.

---

## 학습한 내용

- `push()`
- `pop()`
- `shift()`
- `unshift()`
- `indexOf()`
- `includes()`
- `join()`
- `reverse()`
- `sort()`

---

# 실무 활용

## 1. 장바구니 상품 추가

```javascript
const cart = [];

cart.push("노트북");
cart.push("마우스");
```

사용자가 상품을 장바구니에 담을 때 자주 사용하는 형태이다.

---

## 2. 최근 데이터 삭제

```javascript
const history = [
    "A",
    "B",
    "C"
];

history.pop();
```

가장 최근 데이터를 제거할 때 사용할 수 있다.

---

## 3. 메뉴 존재 여부 확인

```javascript
const menu = [
    "피자",
    "햄버거",
    "파스타"
];

if (menu.includes("피자")) {

    console.log("주문 가능");

}
```

특정 값이 존재하는지 확인할 때 유용하다.

---

## 4. 문자열 출력

```javascript
const skills = [
    "HTML",
    "CSS",
    "JavaScript"
];

console.log(skills.join(" / "));
```

결과

```text
HTML / CSS / JavaScript
```

---

## 5. 이름순 정렬

```javascript
const users = [
    "Kim",
    "Lee",
    "Park"
];

users.sort();

console.log(users);
```

문자열 데이터를 정렬할 때 사용할 수 있다.

---

# 이번 문서에서 새롭게 배운 내용

- 배열 메서드는 배열을 쉽게 다루기 위한 기능이다.
- `push()`는 배열의 마지막에 요소를 추가한다.
- `pop()`은 마지막 요소를 제거하고 제거한 값을 반환한다.
- `shift()`는 첫 번째 요소를 제거한다.
- `unshift()`는 첫 번째 위치에 요소를 추가한다.
- `indexOf()`는 요소의 위치를 찾는다.
- `includes()`는 요소의 존재 여부를 확인한다.
- `join()`은 배열을 문자열로 연결한다.
- `reverse()`와 `sort()`는 원본 배열을 직접 변경한다.

---

# 자주 하는 실수

- `push()`와 `unshift()`의 동작 위치를 혼동한다.
- `pop()`과 `shift()`의 제거 위치를 혼동한다.
- `indexOf()`가 `true` 또는 `false`를 반환한다고 생각한다.
- `includes()`가 인덱스를 반환한다고 생각한다.
- `join()`의 결과가 배열이라고 착각한다.
- 숫자 배열을 `sort()`만으로 원하는 순서대로 정렬할 수 있다고 생각한다.
- `reverse()`와 `sort()`가 원본 배열을 변경한다는 점을 놓친다.

---

# 면접 포인트

### 배열 메서드(Method)란?

배열이 기본적으로 제공하는 기능(함수)이다.

데이터의 추가, 삭제, 검색, 정렬 등을 쉽게 수행할 수 있다.

---

### `push()`와 `pop()`의 차이는?

- `push()`는 배열의 마지막에 요소를 추가한다.
- `pop()`은 배열의 마지막 요소를 제거한다.

---

### `shift()`와 `unshift()`의 차이는?

- `shift()`는 첫 번째 요소를 제거한다.
- `unshift()`는 첫 번째 위치에 요소를 추가한다.

---

### `indexOf()`와 `includes()`의 차이는?

- `indexOf()`는 요소의 **위치(인덱스)** 를 반환한다.
- `includes()`는 요소의 **존재 여부(Boolean)** 를 반환한다.

---

### `join()`의 반환값은?

배열이 아닌 **문자열(String)** 을 반환한다.

---

### `reverse()`와 `sort()`를 사용할 때 주의할 점은?

두 메서드 모두 **원본 배열을 직접 변경(Mutating)** 한다.

필요한 경우 원본 데이터가 변경되는 점을 고려해야 한다.

---

# 핵심 정리

- 배열 메서드는 배열을 효율적으로 다루기 위한 기능이다.
- `push()`와 `pop()`은 배열의 끝에서 동작한다.
- `shift()`와 `unshift()`는 배열의 앞에서 동작한다.
- `indexOf()`는 위치를, `includes()`는 존재 여부를 확인한다.
- `join()`은 배열을 문자열로 변환한다.
- `reverse()`는 순서를 뒤집고, `sort()`는 요소를 정렬한다.
- `reverse()`와 `sort()`는 원본 배열을 변경한다.

---

# 변경 이력

| Version | 날짜 | 변경 내용 |
|---------|------|----------|
| v1.0 | 2026-07-22 | 최초 작성 |
