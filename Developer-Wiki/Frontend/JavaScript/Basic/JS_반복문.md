---
title: JavaScript 반복문
version: v1.0
last_updated: 2026-07-22
status: Completed
---

# JavaScript 반복문

## 문서 정보

| 항목 | 내용 |
|------|------|
| 문서명 | JavaScript 반복문 |
| 분류 | Frontend / JavaScript / Basic |
| 난이도 | Beginner |
| 선수 지식 | JavaScript 소개와 실행환경, 변수와 자료형, 연산자, 조건문 |
| 핵심 주제 | for, while, do...while, break, continue, 중첩 반복문 |
| 버전 | v1.0 |
| 최종 수정일 | 2026-07-22 |

---

# 개요

반복문(Loop)은 **같은 코드를 여러 번 실행하기 위한 문법**이다.

예를 들어

- 상품 목록 출력
- 게시글 출력
- 회원 목록 출력
- 별 찍기
- 배열의 모든 데이터 처리

등과 같이 같은 작업을 반복해야 하는 경우에 사용한다.

실무에서는 반복문을 거의 모든 프로젝트에서 사용한다.

---

# 반복문이 필요한 이유

반복문이 없다면 같은 코드를 여러 번 작성해야 한다.

```javascript
console.log("안녕하세요.");
console.log("안녕하세요.");
console.log("안녕하세요.");
console.log("안녕하세요.");
console.log("안녕하세요.");
```

이처럼 같은 코드를 반복해서 작성하는 것은 비효율적이다.

반복문을 사용하면 다음과 같이 간단하게 작성할 수 있다.

```javascript
for (let i = 0; i < 5; i++) {

    console.log("안녕하세요.");

}
```

---

# 반복문의 종류

JavaScript에는 여러 종류의 반복문이 있다.

| 반복문 | 특징 |
|--------|------|
| `for` | 반복 횟수를 알고 있을 때 |
| `while` | 조건이 참인 동안 반복 |
| `do...while` | 최소 한 번은 실행 |
| `for...of` | 배열 등을 순회할 때 |
| `for...in` | 객체의 속성을 순회할 때 |

> **참고**
>
> 현재 문서에서는 국비교육 진도에 맞추어 `for`, `while`, `do...while`를 먼저 학습한다.
> `for...of`와 `for...in`은 배열과 객체를 학습한 후 별도 문서에서 자세히 다룬다.

---

# for 문

가장 많이 사용하는 반복문이다.

반복 횟수를 알고 있을 때 적합하다.

기본 문법

```javascript
for (초기식; 조건식; 증감식) {

    실행할 코드

}
```

---

# for 문의 구성

```javascript
for (let i = 0; i < 5; i++) {

    console.log(i);

}
```

각 부분의 역할은 다음과 같다.

| 구성 요소 | 역할 |
|-----------|------|
| 초기식 | 반복 시작 시 한 번 실행 |
| 조건식 | 반복 여부를 판단 |
| 증감식 | 반복이 끝날 때마다 실행 |
| 실행문 | 반복할 코드 |

---

# 실행 순서

다음 코드를 살펴보자.

```javascript
for (let i = 0; i < 3; i++) {

    console.log(i);

}
```

실행 순서는 다음과 같다.

```text
① 초기식

↓

② 조건식 검사

↓

③ 실행문

↓

④ 증감식

↓

② 조건식 검사

↓

③ 실행문

...

↓

조건이 거짓이면 종료
```

---

# 예제 1

```javascript
for (let i = 1; i <= 5; i++) {

    console.log(i);

}
```

결과

```text
1
2
3
4
5
```

---

# 예제 2

```javascript
for (let i = 5; i >= 1; i--) {

    console.log(i);

}
```

결과

```text
5
4
3
2
1
```

감소하는 반복도 가능하다.

---

# 예제 3

2씩 증가하기

```javascript
for (let i = 0; i <= 10; i += 2) {

    console.log(i);

}
```

결과

```text
0
2
4
6
8
10
```

---

# 반복문의 변수

반복문에서는 보통 `i`를 많이 사용한다.

```javascript
for (let i = 0; i < 5; i++) {

}
```

중첩 반복문에서는

```javascript
for (let i = 0; i < 3; i++) {

    for (let j = 0; j < 3; j++) {

    }

}
```

처럼 `j`, `k` 등을 사용하기도 한다.

---

# 반복 횟수 계산

다음 반복문은 몇 번 실행될까?

```javascript
for (let i = 0; i < 10; i++) {

    console.log(i);

}
```

초기값은 `0`, 종료 조건은 `i < 10`이므로 총 **10번** 실행된다.

출력되는 값은 다음과 같다.

```text
0
1
2
3
4
5
6
7
8
9
```

반복문의 시작값과 종료 조건을 정확히 이해하는 것이 중요하다.

---

# 실무에서 자주 사용하는 패턴

목록을 일정 횟수만큼 생성하는 경우

```javascript
for (let i = 1; i <= 5; i++) {

    console.log(`상품 ${i}`);

}
```

결과

```text
상품 1
상품 2
상품 3
상품 4
상품 5
```

---

---

# while 문

`while` 문은 **조건이 참(`true`)인 동안 계속 반복**하는 반복문이다.

반복 횟수를 미리 알기 어려운 경우에 주로 사용한다.

기본 문법

```javascript
while (조건식) {

    실행할 코드

}
```

---

# while 실행 과정

다음 코드를 살펴보자.

```javascript
let count = 0;

while (count < 3) {

    console.log(count);

    count++;

}
```

실행 순서는 다음과 같다.

```text
① 조건식 검사

↓

② 실행문

↓

③ 증감식

↓

① 조건식 검사

...

↓

조건이 거짓이면 종료
```

---

# 예제 1

```javascript
let i = 1;

while (i <= 5) {

    console.log(i);

    i++;

}
```

결과

```text
1
2
3
4
5
```

---

# 예제 2

감소하는 반복도 가능하다.

```javascript
let i = 5;

while (i >= 1) {

    console.log(i);

    i--;

}
```

결과

```text
5
4
3
2
1
```

---

# for와 while 비교

다음 두 코드는 같은 결과를 출력한다.

## for

```javascript
for (let i = 1; i <= 5; i++) {

    console.log(i);

}
```

---

## while

```javascript
let i = 1;

while (i <= 5) {

    console.log(i);

    i++;

}
```

---

## 언제 사용할까?

| 상황 | 추천 |
|------|------|
| 반복 횟수를 알고 있음 | `for` |
| 종료 시점을 알기 어려움 | `while` |

실무에서는 반복 횟수가 명확한 경우 `for`를 더 많이 사용한다.

---

# do...while 문

`do...while`은 **조건을 검사하기 전에 먼저 한 번 실행**하는 반복문이다.

기본 문법

```javascript
do {

    실행할 코드

} while (조건식);
```

---

# 예제

```javascript
let i = 1;

do {

    console.log(i);

    i++;

} while (i <= 5);
```

결과

```text
1
2
3
4
5
```

---

# while과 do...while 차이

다음 코드를 살펴보자.

```javascript
let num = 10;

while (num < 5) {

    console.log(num);

}
```

결과

```text
(출력 없음)
```

조건이 처음부터 거짓이므로 실행되지 않는다.

---

반면

```javascript
let num = 10;

do {

    console.log(num);

} while (num < 5);
```

결과

```text
10
```

`do` 블록은 조건과 상관없이 **최소 한 번은 실행**된다.

---

# break

`break`는 반복문을 **즉시 종료**한다.

```javascript
for (let i = 1; i <= 10; i++) {

    if (i === 5) {

        break;

    }

    console.log(i);

}
```

결과

```text
1
2
3
4
```

`i`가 `5`가 되는 순간 반복문이 종료된다.

---

# 실무 활용

검색을 하다가 원하는 데이터를 찾으면 반복을 종료할 수 있다.

```javascript
for (let i = 0; i < users.length; i++) {

    if (users[i].id === targetId) {

        console.log("찾음");

        break;

    }

}
```

이처럼 더 이상 반복이 필요 없는 경우 `break`를 사용하면 불필요한 연산을 줄일 수 있다.

---

# continue

`continue`는 **현재 반복만 건너뛰고 다음 반복으로 이동**한다.

```javascript
for (let i = 1; i <= 5; i++) {

    if (i === 3) {

        continue;

    }

    console.log(i);

}
```

결과

```text
1
2
4
5
```

`3`만 출력되지 않는다.

---

# break와 continue 비교

| 키워드 | 동작 |
|---------|------|
| `break` | 반복문 전체 종료 |
| `continue` | 현재 반복만 건너뜀 |

예를 들어

```javascript
for (let i = 1; i <= 5; i++) {

    if (i === 3) {

        continue;

    }

    console.log(i);

}
```

↓

```text
1
2
4
5
```

---

```javascript
for (let i = 1; i <= 5; i++) {

    if (i === 3) {

        break;

    }

    console.log(i);

}
```

↓

```text
1
2
```

---

# 무한 반복(Infinite Loop)

조건이 항상 참이면 반복문은 끝나지 않는다.

```javascript
while (true) {

    console.log("반복");

}
```

이러한 반복을 **무한 반복(Infinite Loop)** 이라고 한다.

---

# 무한 반복을 사용하는 경우

실무에서는 일반적으로 무한 반복을 사용하지 않는다.

다만 다음과 같이 종료 조건을 함께 사용하는 경우가 있다.

```javascript
while (true) {

    if (isFinished) {

        break;

    }

}
```

`break`를 통해 원하는 시점에 반복을 종료한다.

---

# 반복문 작성 시 주의사항

- 종료 조건을 반드시 확인한다.
- 증감식을 빠뜨리지 않는다.
- 필요 이상으로 반복하지 않는다.
- `break`와 `continue`를 적절히 사용한다.
- 무한 반복이 발생하지 않도록 주의한다.

---

---

# 중첩 반복문 (Nested Loop)

반복문 안에 또 다른 반복문을 작성하는 것을 **중첩 반복문(Nested Loop)** 이라고 한다.

기본 문법

```javascript
for (let i = 0; i < 3; i++) {

    for (let j = 0; j < 3; j++) {

        실행할 코드;

    }

}
```

바깥쪽 반복문이 한 번 실행될 때마다 안쪽 반복문이 처음부터 끝까지 실행된다.

---

# 실행 순서

다음 코드를 살펴보자.

```javascript
for (let i = 1; i <= 2; i++) {

    for (let j = 1; j <= 3; j++) {

        console.log(i, j);

    }

}
```

실행 결과

```text
1 1
1 2
1 3
2 1
2 2
2 3
```

실행 순서를 그림으로 표현하면 다음과 같다.

```text
i = 1
 ├─ j = 1
 ├─ j = 2
 └─ j = 3

i = 2
 ├─ j = 1
 ├─ j = 2
 └─ j = 3
```

---

# 구구단 출력

중첩 반복문의 대표적인 예제이다.

```javascript
for (let dan = 2; dan <= 9; dan++) {

    console.log(`${dan}단`);

    for (let num = 1; num <= 9; num++) {

        console.log(`${dan} × ${num} = ${dan * num}`);

    }

}
```

출력

```text
2단
2 × 1 = 2
...
9 × 9 = 81
```

---

# 별 찍기 예제

반복문을 연습할 때 가장 많이 사용하는 예제이다.

---

## 별 5개 출력

```javascript
for (let i = 0; i < 5; i++) {

    console.log("*");

}
```

결과

```text
*
*
*
*
*
```

---

## 가로로 출력

```javascript
let stars = "";

for (let i = 0; i < 5; i++) {

    stars += "*";

}

console.log(stars);
```

결과

```text
*****
```

---

## 직사각형 출력

```javascript
for (let i = 0; i < 3; i++) {

    let stars = "";

    for (let j = 0; j < 5; j++) {

        stars += "*";

    }

    console.log(stars);

}
```

결과

```text
*****
*****
*****
```

---

## 직각삼각형 출력

```javascript
for (let i = 1; i <= 5; i++) {

    let stars = "";

    for (let j = 0; j < i; j++) {

        stars += "*";

    }

    console.log(stars);

}
```

결과

```text
*
**
***
****
*****
```

---

# 반복문의 활용

반복문은 단순히 숫자를 출력하는 것이 아니라, **같은 작업을 여러 데이터에 적용**할 때 사용한다.

예를 들어 학생 이름을 출력한다고 가정해 보자.

```javascript
const students = [
    "Kim",
    "Lee",
    "Park"
];
```

현재는 배열을 배우기 전이므로 아래 코드는 **미리 보기** 정도로 이해하면 된다.

```javascript
for (let i = 0; i < students.length; i++) {

    console.log(students[i]);

}
```

> **참고**
>
> `Array(배열)`와 `length`는 이후 문서에서 자세히 학습한다.
> 지금은 반복문이 여러 데이터를 처리하는 데 사용된다는 점만 이해하면 충분하다.

---

# 반복문 작성 원칙

좋은 반복문을 작성하기 위한 기준은 다음과 같다.

- 반복 횟수를 명확하게 작성한다.
- 종료 조건을 쉽게 이해할 수 있도록 작성한다.
- 변수명은 의미 있게 작성한다.
- 불필요한 중첩 반복문은 피한다.
- 반복문 안에서 동일한 계산을 여러 번 하지 않는다.

---

# 성능을 고려한 반복문

다음과 같이 반복마다 같은 값을 계산하는 코드는 비효율적일 수 있다.

```javascript
for (let i = 0; i < users.length; i++) {

    console.log(users[i]);

}
```

실무에서는 필요한 값을 미리 저장하는 경우도 있다.

```javascript
const length = users.length;

for (let i = 0; i < length; i++) {

    console.log(users[i]);

}
```

> **참고**
>
> 최신 JavaScript 엔진은 이러한 부분을 대부분 최적화한다.
> 따라서 초보 단계에서는 **가독성을 우선**하는 것이 더 중요하다.

---

# 반복문에서 많이 사용하는 패턴

## 일정 횟수 반복

```javascript
for (let i = 0; i < 10; i++) {

    console.log(i);

}
```

---

## 조건을 만족하는 값만 출력

```javascript
for (let i = 1; i <= 10; i++) {

    if (i % 2 === 0) {

        console.log(i);

    }

}
```

결과

```text
2
4
6
8
10
```

---

## 누적 계산

```javascript
let sum = 0;

for (let i = 1; i <= 5; i++) {

    sum += i;

}

console.log(sum);
```

결과

```text
15
```

누적 계산은 이후 배열, 객체, DOM 처리에서도 매우 자주 사용된다.

---

---

# 실무 예제 프로젝트

다음은 상품 목록을 반복문으로 출력하는 간단한 예제이다.

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

> **참고**
>
> `Array(배열)`와 `length`는 이후 문서에서 자세히 학습한다.
> 지금은 반복문을 이용하면 여러 데이터를 같은 방식으로 처리할 수 있다는 점에 집중하면 된다.

---

## 학습한 내용

- `for`
- `while`
- `do...while`
- `break`
- `continue`
- 중첩 반복문
- 문자열 누적
- DOM 출력

---

# 실무 활용

## 1. 일정 횟수 반복

```javascript
for (let i = 1; i <= 10; i++) {

    console.log(i);

}
```

가장 기본적인 반복 형태이다.

---

## 2. 짝수만 출력

```javascript
for (let i = 1; i <= 20; i++) {

    if (i % 2 === 0) {

        console.log(i);

    }

}
```

조건문과 반복문을 함께 사용하는 대표적인 예제이다.

---

## 3. 합계 계산

```javascript
let total = 0;

for (let i = 1; i <= 100; i++) {

    total += i;

}

console.log(total);
```

누적 계산은 실무에서도 매우 자주 사용된다.

---

## 4. 특정 조건에서 반복 종료

```javascript
for (let i = 1; i <= 100; i++) {

    if (i === 50) {

        break;

    }

    console.log(i);

}
```

원하는 데이터를 찾으면 더 이상 반복하지 않는다.

---

## 5. 특정 값 건너뛰기

```javascript
for (let i = 1; i <= 10; i++) {

    if (i === 5) {

        continue;

    }

    console.log(i);

}
```

특정 데이터만 제외하고 처리할 수 있다.

---

# 이번 문서에서 새롭게 배운 내용

- 반복문은 같은 작업을 여러 번 수행하기 위한 문법이다.
- `for`는 반복 횟수를 알고 있을 때 적합하다.
- `while`은 조건이 참인 동안 반복한다.
- `do...while`은 최소 한 번은 실행된다.
- `break`는 반복문을 즉시 종료한다.
- `continue`는 현재 반복만 건너뛴다.
- 중첩 반복문을 이용해 2차원 형태의 반복을 구현할 수 있다.
- 별 찍기와 구구단은 중첩 반복문의 대표적인 예제이다.
- 반복문은 여러 데이터를 동일한 방식으로 처리할 때 사용된다.

---

# 자주 하는 실수

- 종료 조건을 잘못 작성하여 무한 반복이 발생한다.
- 증감식을 작성하지 않는다.
- `break`와 `continue`의 차이를 혼동한다.
- 반복 횟수를 잘못 계산하여 한 번 더 실행하거나 덜 실행한다.
- 중첩 반복문을 과도하게 사용하여 코드가 복잡해진다.
- 반복문 안에서 동일한 계산을 계속 수행하여 가독성을 떨어뜨린다.

---

# 면접 포인트

### `for`와 `while`의 차이는 무엇인가?

- `for`는 반복 횟수가 명확할 때 적합하다.
- `while`은 반복 종료 시점을 미리 알기 어려운 경우 적합하다.

---

### `do...while`은 언제 사용하는가?

조건과 상관없이 **최소 한 번은 실행되어야 하는 경우** 사용한다.

---

### `break`와 `continue`의 차이는?

- `break`는 반복문 전체를 종료한다.
- `continue`는 현재 반복만 건너뛰고 다음 반복을 계속한다.

---

### 중첩 반복문은 언제 사용하는가?

행과 열처럼 **2차원 구조를 처리하거나**, 구구단·별 찍기와 같이 반복 안에서 또 다른 반복이 필요한 경우 사용한다.

---

### 반복문에서 가장 주의해야 할 점은?

- 종료 조건이 올바른지 확인한다.
- 무한 반복이 발생하지 않는지 확인한다.
- 불필요한 반복을 줄여 가독성과 성능을 함께 고려한다.

---

# 핵심 정리

- 반복문은 같은 작업을 여러 번 수행하기 위해 사용한다.
- `for`는 가장 많이 사용하는 반복문이다.
- `while`은 조건 기반 반복에 적합하다.
- `do...while`은 최소 한 번 실행된다.
- `break`는 반복 종료, `continue`는 현재 반복 건너뛰기이다.
- 중첩 반복문은 2차원 형태의 반복 작업에 활용된다.
- 반복문과 조건문은 함께 사용하는 경우가 많다.
- 종료 조건과 증감식을 정확하게 작성하는 것이 중요하다.

---

# 변경 이력

| Version | 날짜 | 변경 내용 |
|---------|------|----------|
| v1.0 | 2026-07-22 | 최초 작성 |
