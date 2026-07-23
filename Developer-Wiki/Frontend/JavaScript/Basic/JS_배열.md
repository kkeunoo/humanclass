---
title: JavaScript 배열
version: v1.0
last_updated: 2026-07-22
status: Completed
---

# JavaScript 배열

## 문서 정보

| 항목 | 내용 |
|------|------|
| 문서명 | JavaScript 배열 |
| 분류 | Frontend / JavaScript / Basic |
| 난이도 | Beginner |
| 선수 지식 | JavaScript 소개와 실행환경, 변수와 자료형, 연산자, 조건문, 반복문, 함수 |
| 핵심 주제 | 배열, 인덱스, 요소, length, 배열 접근 |
| 버전 | v1.0 |
| 최종 수정일 | 2026-07-22 |

---

# 개요

배열(Array)은 **여러 개의 데이터를 하나의 변수에 저장할 수 있는 자료구조**이다.

변수 하나에는 일반적으로 하나의 값만 저장할 수 있지만, 배열을 사용하면 여러 개의 값을 순서대로 저장할 수 있다.

예를 들어

- 학생 이름 목록
- 상품 목록
- 게시글 목록
- 점수 목록
- 메뉴 목록

과 같은 데이터를 관리할 때 배열을 사용한다.

JavaScript뿐만 아니라 대부분의 프로그래밍 언어에서 매우 자주 사용하는 자료구조이다.

---

# 배열이 필요한 이유

변수만 사용하면 여러 개의 데이터를 각각 저장해야 한다.

```javascript
const student1 = "Kim";
const student2 = "Lee";
const student3 = "Park";
const student4 = "Choi";
```

데이터가 많아질수록 관리가 어려워진다.

배열을 사용하면 다음과 같이 하나의 변수에 저장할 수 있다.

```javascript
const students = [
    "Kim",
    "Lee",
    "Park",
    "Choi"
];
```

관련된 데이터를 하나로 묶어 관리할 수 있으므로 훨씬 효율적이다.

---

# 배열(Array)이란?

배열은 **순서가 있는 여러 개의 값을 저장하는 자료구조**이다.

배열 안에 저장된 각각의 값을 **요소(Element)** 라고 한다.

```javascript
const fruits = [
    "사과",
    "바나나",
    "포도"
];
```

위 배열에는 3개의 요소가 있다.

| 인덱스(Index) | 요소(Element) |
|--------------|--------------|
| 0 | 사과 |
| 1 | 바나나 |
| 2 | 포도 |

---

# 배열 생성

배열은 대괄호(`[]`)를 이용하여 생성한다.

기본 문법

```javascript
const 배열이름 = [
    값1,
    값2,
    값3
];
```

예제

```javascript
const colors = [
    "red",
    "blue",
    "green"
];
```

---

# 인덱스(Index)

배열의 각 요소에는 **인덱스(Index)** 가 있다.

인덱스는 **0부터 시작**한다.

```javascript
const animals = [
    "Dog",
    "Cat",
    "Rabbit"
];
```

| 인덱스 | 값 |
|--------|----|
| 0 | Dog |
| 1 | Cat |
| 2 | Rabbit |

배열의 첫 번째 요소는 `0`번 인덱스를 가진다.

---

# 배열 요소 접근

배열의 요소는 **인덱스**를 이용하여 접근한다.

```javascript
const fruits = [
    "사과",
    "바나나",
    "포도"
];

console.log(fruits[0]);
console.log(fruits[1]);
console.log(fruits[2]);
```

결과

```text
사과
바나나
포도
```

---

# 존재하지 않는 인덱스

없는 인덱스에 접근하면 `undefined`가 반환된다.

```javascript
const fruits = [
    "사과",
    "바나나"
];

console.log(fruits[5]);
```

결과

```text
undefined
```

---

# 다양한 자료형 저장

배열에는 하나의 자료형만 저장할 필요는 없다.

```javascript
const values = [
    "Kim",
    20,
    true,
    null
];
```

문자열, 숫자, Boolean 등 다양한 자료형을 함께 저장할 수 있다.

다만 실무에서는 **같은 성격의 데이터를 저장하는 것이 일반적**이다.

---

# 빈 배열 생성

처음에는 비어 있는 배열을 만들 수도 있다.

```javascript
const items = [];
```

이후 필요한 데이터를 추가하여 사용할 수 있다.

> **참고**
>
> 배열에 데이터를 추가하거나 삭제하는 방법은 **배열 메서드** 문서에서 자세히 학습한다.

---

---

# length 속성

배열에는 저장된 요소의 개수를 나타내는 `length` 속성이 있다.

기본 문법

```javascript
배열이름.length
```

예제

```javascript id="h81lqz"
const fruits = [
    "사과",
    "바나나",
    "포도"
];

console.log(fruits.length);
```

결과

```text id="rz6v1s"
3
```

`length`는 배열의 요소 개수를 반환한다.

---

# 마지막 요소 접근

배열의 마지막 요소는 `length`를 이용하면 쉽게 접근할 수 있다.

```javascript id="n3dbvk"
const fruits = [
    "사과",
    "바나나",
    "포도"
];

console.log(fruits[fruits.length - 1]);
```

결과

```text id="k4evp7"
포도
```

마지막 인덱스는 항상 `length - 1`이다.

---

# 배열 요소 수정

배열의 요소는 인덱스를 이용하여 수정할 수 있다.

```javascript id="eqzjrv"
const fruits = [
    "사과",
    "바나나",
    "포도"
];

fruits[1] = "딸기";

console.log(fruits);
```

결과

```text id="8t6kxp"
["사과", "딸기", "포도"]
```

---

# 배열 요소 추가(인덱스 사용)

배열의 현재 길이와 같은 인덱스에 값을 저장하면 새로운 요소가 추가된다.

```javascript id="g7v6te"
const fruits = [
    "사과",
    "바나나"
];

fruits[2] = "포도";

console.log(fruits);
```

결과

```text id="n9ktm5"
["사과", "바나나", "포도"]
```

> **참고**
>
> 실무에서는 보통 `push()` 메서드를 사용하여 요소를 추가한다.
> `push()`는 배열 메서드 문서에서 자세히 학습한다.

---

# 배열과 반복문

배열은 반복문과 함께 사용할 때 가장 큰 장점을 가진다.

예를 들어 학생 이름을 하나씩 출력해 보자.

```javascript id="v5r1dh"
const students = [
    "Kim",
    "Lee",
    "Park"
];

for (let i = 0; i < students.length; i++) {

    console.log(students[i]);

}
```

결과

```text id="k2r9bu"
Kim
Lee
Park
```

배열의 요소 개수가 변경되어도 반복문의 조건을 수정할 필요가 없다.

---

# 배열 순회

배열의 모든 요소를 처음부터 끝까지 하나씩 처리하는 것을 **배열 순회(Iteration)** 라고 한다.

가장 기본적인 방법은 `for`문을 사용하는 것이다.

```javascript id="a8f4yn"
const numbers = [
    10,
    20,
    30,
    40
];

for (let i = 0; i < numbers.length; i++) {

    console.log(numbers[i]);

}
```

배열을 순회할 때는 대부분 `length`를 함께 사용한다.

---

# 배열의 합계 구하기

반복문과 배열을 함께 사용하면 누적 계산도 쉽게 할 수 있다.

```javascript id="4x9rph"
const scores = [
    80,
    90,
    70,
    100
];

let total = 0;

for (let i = 0; i < scores.length; i++) {

    total += scores[i];

}

console.log(total);
```

결과

```text id="2e7wha"
340
```

---

# 배열의 평균 구하기

합계를 구한 후 `length`로 나누면 평균을 구할 수 있다.

```javascript id="w0rdv3"
const scores = [
    80,
    90,
    70,
    100
];

let total = 0;

for (let i = 0; i < scores.length; i++) {

    total += scores[i];

}

const average = total / scores.length;

console.log(average);
```

결과

```text id="5l2qfr"
85
```

---

# 조건에 맞는 요소 찾기

반복문과 조건문을 함께 사용하면 원하는 데이터를 찾을 수 있다.

```javascript id="6mt5ab"
const scores = [
    80,
    95,
    70,
    100
];

for (let i = 0; i < scores.length; i++) {

    if (scores[i] >= 90) {

        console.log(scores[i]);

    }

}
```

결과

```text id="r3wj8m"
95
100
```

---

# 배열 출력

배열 전체를 출력할 수도 있다.

```javascript id="twf8sm"
const fruits = [
    "사과",
    "바나나",
    "포도"
];

console.log(fruits);
```

결과

```text id="hv1m5x"
["사과", "바나나", "포도"]
```

특정 요소만 출력하려면 인덱스를 사용한다.

```javascript id="zt4d7q"
console.log(fruits[0]);
```

---

# 배열 작성 시 주의사항

- 인덱스는 `0`부터 시작한다.
- 마지막 인덱스는 `length - 1`이다.
- 존재하지 않는 인덱스는 `undefined`를 반환한다.
- 배열을 순회할 때는 `length`를 사용하는 것이 좋다.
- 같은 성격의 데이터를 하나의 배열로 관리하는 것이 일반적이다.

---

---

# 배열 사용 패턴

배열은 여러 데이터를 저장하는 것뿐만 아니라 **반복문과 함께 다양한 작업을 수행**할 때 자주 사용된다.

대표적인 활용은 다음과 같다.

- 전체 데이터 출력
- 합계 계산
- 평균 계산
- 원하는 데이터 검색
- 조건에 맞는 데이터만 출력

실무에서도 이러한 패턴을 매우 자주 사용한다.

---

# 배열 요소 개수 세기

조건에 맞는 요소가 몇 개인지 계산할 수도 있다.

```javascript
const scores = [
    80,
    95,
    70,
    100
];

let count = 0;

for (let i = 0; i < scores.length; i++) {

    if (scores[i] >= 90) {

        count++;

    }

}

console.log(count);
```

결과

```text
2
```

90점 이상인 학생은 2명이다.

---

# 배열에서 최댓값 찾기

반복문을 이용하면 배열에서 가장 큰 값을 찾을 수 있다.

```javascript
const numbers = [
    30,
    80,
    50,
    100,
    60
];

let max = numbers[0];

for (let i = 1; i < numbers.length; i++) {

    if (numbers[i] > max) {

        max = numbers[i];

    }

}

console.log(max);
```

결과

```text
100
```

---

# 배열에서 최솟값 찾기

최솟값도 같은 방법으로 구할 수 있다.

```javascript
const numbers = [
    30,
    80,
    50,
    100,
    60
];

let min = numbers[0];

for (let i = 1; i < numbers.length; i++) {

    if (numbers[i] < min) {

        min = numbers[i];

    }

}

console.log(min);
```

결과

```text
30
```

---

# 문자열 배열 출력

배열의 각 요소를 하나씩 출력할 수도 있다.

```javascript
const menu = [
    "피자",
    "햄버거",
    "파스타"
];

for (let i = 0; i < menu.length; i++) {

    console.log(`${i + 1}. ${menu[i]}`);

}
```

결과

```text
1. 피자
2. 햄버거
3. 파스타
```

---

# 2차원 배열 (미리 보기)

배열 안에는 또 다른 배열을 저장할 수도 있다.

```javascript
const seats = [
    ["A1", "A2", "A3"],
    ["B1", "B2", "B3"]
];
```

이처럼 배열 안에 배열이 들어 있는 형태를 **2차원 배열(Two-dimensional Array)** 이라고 한다.

2차원 배열은 좌석 배치, 달력, 게임 맵 등 행(Row)과 열(Column) 구조를 표현할 때 사용한다.

> **참고**
>
> 2차원 배열은 배열 심화 과정에서 자세히 학습한다.
> 현재는 배열 안에도 배열을 저장할 수 있다는 정도만 이해하면 충분하다.

---

# 배열과 함수 함께 사용하기

배열을 함수의 매개변수로 전달할 수도 있다.

```javascript
function printScores(scores) {

    for (let i = 0; i < scores.length; i++) {

        console.log(scores[i]);

    }

}

const scores = [
    80,
    90,
    100
];

printScores(scores);
```

함수를 사용하면 같은 배열 처리 로직을 여러 곳에서 재사용할 수 있다.

---

# 배열 작성 원칙

실무에서는 다음과 같은 원칙을 자주 사용한다.

- 같은 종류의 데이터를 하나의 배열에 저장한다.
- 배열 이름은 복수형으로 작성하는 것이 일반적이다.
- 반복문에서는 `length`를 사용하여 순회한다.
- 인덱스를 직접 숫자로 작성하는 것은 최소화한다.
- 반복되는 배열 처리 코드는 함수로 분리한다.

---

# 좋은 배열 이름

배열 이름은 여러 개의 데이터를 저장한다는 의미가 드러나도록 작성한다.

좋은 예

```javascript
students
products
users
scores
menus
```

좋지 않은 예

```javascript
data
aaa
test
array1
```

이름만 보고도 어떤 데이터가 저장되어 있는지 알 수 있도록 작성하는 것이 좋다.

---

# 실무에서 자주 사용하는 배열 패턴

## 모든 데이터 출력

```javascript
for (let i = 0; i < products.length; i++) {

    console.log(products[i]);

}
```

---

## 합계 계산

```javascript
let total = 0;

for (let i = 0; i < prices.length; i++) {

    total += prices[i];

}
```

---

## 조건에 맞는 데이터 출력

```javascript
for (let i = 0; i < users.length; i++) {

    if (users[i].age >= 20) {

        console.log(users[i]);

    }

}
```

> **참고**
>
> 위 예제의 `users[i].age`는 객체(Object)를 사용하는 코드이다.
> 객체는 이후 문서에서 자세히 학습한다.
> 여기서는 배열과 조건문을 함께 사용할 수 있다는 점만 이해하면 충분하다.

---

# 배열 사용 시 주의사항

- 인덱스는 항상 `0`부터 시작한다.
- 존재하지 않는 인덱스에 접근하면 `undefined`가 반환된다.
- 반복문의 종료 조건은 `length`를 사용하는 것이 안전하다.
- 같은 종류의 데이터를 하나의 배열에 저장한다.
- 배열을 순회할 때는 요소 개수가 변경될 수 있음을 고려한다.

---

---

# 실무 예제 프로젝트

다음은 배열에 저장된 상품 목록을 화면에 출력하는 예제이다.

## HTML

```html
<h2>상품 목록</h2>

<ul id="productList"></ul>
```

---

## JavaScript

```javascript
const products = [
    "노트북",
    "마우스",
    "키보드",
    "모니터"
];

const productList = document.querySelector("#productList");

let html = "";

for (let i = 0; i < products.length; i++) {

    html += `<li>${products[i]}</li>`;

}

productList.innerHTML = html;
```

반복문과 배열을 함께 사용하면 여러 개의 데이터를 동일한 방식으로 화면에 출력할 수 있다.

> **참고**
>
> `innerHTML`은 HTML 요소 안에 HTML 문자열을 삽입하는 속성이다.
> DOM(Document Object Model) 문서에서 자세히 학습한다.

---

## 학습한 내용

- 배열(Array)
- 요소(Element)
- 인덱스(Index)
- `length`
- 배열 요소 접근
- 배열 요소 수정
- 배열 순회
- 반복문과 배열

---

# 실무 활용

## 1. 상품 목록 출력

```javascript
const products = [
    "노트북",
    "마우스",
    "키보드"
];

for (let i = 0; i < products.length; i++) {

    console.log(products[i]);

}
```

---

## 2. 학생 점수 합계

```javascript
const scores = [
    80,
    90,
    100
];

let total = 0;

for (let i = 0; i < scores.length; i++) {

    total += scores[i];

}

console.log(total);
```

---

## 3. 최고 점수 찾기

```javascript
const scores = [
    80,
    95,
    70,
    100
];

let max = scores[0];

for (let i = 1; i < scores.length; i++) {

    if (scores[i] > max) {

        max = scores[i];

    }

}

console.log(max);
```

---

## 4. 조건에 맞는 데이터 출력

```javascript
const scores = [
    80,
    95,
    70,
    100
];

for (let i = 0; i < scores.length; i++) {

    if (scores[i] >= 90) {

        console.log(scores[i]);

    }

}
```

---

## 5. 마지막 요소 출력

```javascript
const fruits = [
    "사과",
    "바나나",
    "포도"
];

console.log(fruits[fruits.length - 1]);
```

---

# 이번 문서에서 새롭게 배운 내용

- 배열은 여러 개의 데이터를 하나의 변수에 저장하는 자료구조이다.
- 배열의 각 데이터는 요소(Element)라고 한다.
- 배열은 인덱스(Index)를 이용하여 요소에 접근한다.
- 인덱스는 항상 `0`부터 시작한다.
- `length`를 이용하여 요소 개수를 확인할 수 있다.
- 반복문과 함께 사용하면 배열의 모든 요소를 쉽게 처리할 수 있다.
- 배열 요소는 인덱스를 이용하여 수정할 수 있다.
- 배열은 함수와 함께 사용하면 재사용성이 높아진다.

---

# 자주 하는 실수

- 인덱스를 `1`부터 시작한다고 생각한다.
- 마지막 요소를 `length`로 접근하려고 한다.
- (`length - 1`이 마지막 인덱스이다.)
- 존재하지 않는 인덱스에 접근하면서 오류가 날 것이라고 생각한다.
- 배열 순회 시 `length` 대신 고정된 숫자를 사용한다.
- 서로 다른 성격의 데이터를 하나의 배열에 무분별하게 저장한다.
- 배열과 객체를 같은 개념으로 혼동한다.

---

# 면접 포인트

### 배열(Array)이란?

여러 개의 데이터를 순서대로 저장할 수 있는 자료구조이다.

---

### 인덱스(Index)는 왜 0부터 시작하는가?

JavaScript를 포함한 대부분의 프로그래밍 언어는 메모리의 시작 위치를 기준으로 요소를 관리하기 때문에 인덱스를 `0`부터 사용한다.

---

### `length`의 역할은?

배열에 저장된 요소의 개수를 반환한다.

마지막 요소의 인덱스는 `length - 1`이다.

---

### 배열과 반복문을 함께 사용하는 이유는?

배열의 모든 요소를 같은 방식으로 처리할 수 있기 때문이다.

데이터 개수가 변경되어도 반복문의 조건을 수정할 필요가 없다.

---

### 배열과 변수의 차이는?

- 변수는 하나의 값을 저장한다.
- 배열은 여러 개의 값을 하나의 변수에 저장한다.

---

# 핵심 정리

- 배열은 여러 데이터를 효율적으로 관리하기 위한 자료구조이다.
- 요소는 인덱스를 통해 접근한다.
- 인덱스는 `0`부터 시작한다.
- `length`는 요소의 개수를 반환한다.
- 배열은 반복문과 함께 사용할 때 가장 많이 활용된다.
- 배열의 요소는 수정할 수 있으며, 반복문을 통해 순회할 수 있다.
- 같은 종류의 데이터는 하나의 배열로 관리하는 것이 좋다.

---

# 변경 이력

| Version | 날짜 | 변경 내용 |
|---------|------|----------|
| v1.0 | 2026-07-22 | 최초 작성 |
