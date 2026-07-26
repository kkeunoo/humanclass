---
title: JS_Date
version: v1.0
last_updated: 2026-07-22
status: completed
---

# 문서 정보

| 항목 | 내용 |
|------|------|
| 문서명 | JS_Date |
| 분야 | Frontend / JavaScript |
| 버전 | v1.0 |
| 작성일 | 2026-07-22 |

---

# 개요

JavaScript에서는 날짜와 시간을 처리하기 위해 `Date` 객체를 사용한다.

현재 날짜를 가져오거나 특정 날짜를 생성할 수 있으며, 연도·월·일·요일·시간 등을 각각 구할 수도 있다.

또한 두 날짜의 차이를 계산하여 D-Day, 나이 계산, 예약 시간 확인 등 다양한 기능을 구현할 수 있다.

이번 문서에서는 `Date` 객체의 생성 방법과 주요 메서드를 학습한다.

---

# 핵심 개념

`Date` 객체는 날짜와 시간을 하나의 객체로 관리한다.

```text
Date

↓

현재 날짜

현재 시간

연도

월

일

요일

시

분

초
```

---

# Date 객체 생성

현재 날짜와 시간을 생성한다.

```javascript
const now =

    new Date();
```

출력

```javascript
console.log(now);
```

예시

```text
Tue Jul 22 2026 14:30:20 GMT+0900
```

---

# 특정 날짜 생성

원하는 날짜를 직접 생성할 수도 있다.

```javascript
const date =

    new Date(

        2026,

        6,

        22

    );
```

> **주의**  
> 월(Month)은 **0부터 시작**한다.
>
> - 0 → 1월
> - 1 → 2월
> - ...
> - 6 → 7월
> - 11 → 12월

---

# 문자열로 날짜 생성

```javascript
const date =

    new Date(

        "2026-07-22"

    );
```

---

# 연도 가져오기

```javascript
const now =

    new Date();

console.log(

    now.getFullYear()

);
```

출력

```text
2026
```

---

# 월 가져오기

```javascript
console.log(

    now.getMonth()

);
```

출력

```text
6
```

7월이지만 6이 출력된다.

필요하면

```javascript
console.log(

    now.getMonth() + 1

);
```

처럼 사용한다.

---

# 날짜 가져오기

```javascript
console.log(

    now.getDate()

);
```

출력

```text
22
```

---

# 요일 가져오기

```javascript
console.log(

    now.getDay()

);
```

출력

```text
2
```

요일 번호

| 값 | 요일 |
|----|------|
|0|일요일|
|1|월요일|
|2|화요일|
|3|수요일|
|4|목요일|
|5|금요일|
|6|토요일|

---

# 시간 가져오기

```javascript
console.log(

    now.getHours()

);
```

출력 예시

```text
14
```

---

# 분 가져오기

```javascript
console.log(

    now.getMinutes()

);
```

---

# 초 가져오기

```javascript
console.log(

    now.getSeconds()

);
```

---

# 실무 팁

`Date` 객체는 생성한 순간의 시간을 저장한다.

```javascript
const now =

    new Date();
```

이 객체는 자동으로 시간이 계속 변하지 않는다.

현재 시간을 계속 표시하려면 `setInterval()`과 함께 새로운 `Date` 객체를 반복해서 생성해야 한다.

```javascript
setInterval(function(){

    const now =

        new Date();

    console.log(now);

},1000);
```

---

---

# 날짜 변경

`Date` 객체는 생성한 날짜를 변경할 수도 있다.

이를 위해 `set` 계열 메서드를 사용한다.

---

# setFullYear()

연도를 변경한다.

```javascript
const date =

    new Date();

date.setFullYear(2030);

console.log(date);
```

출력 예시

```text
Sun Jul 21 2030 ...
```

---

# setMonth()

월을 변경한다.

```javascript
const date =

    new Date();

date.setMonth(11);

console.log(date);
```

출력 예시

```text
12월
```

> **주의**  
> `setMonth()` 역시 0부터 시작한다.
>
> - 0 → 1월
> - 11 → 12월

---

# setDate()

날짜를 변경한다.

```javascript
const date =

    new Date();

date.setDate(15);

console.log(date);
```

출력 예시

```text
15일
```

---

# setHours()

시간을 변경한다.

```javascript
const date =

    new Date();

date.setHours(9);

console.log(date);
```

출력 예시

```text
09시
```

---

# Timestamp

JavaScript에서는 날짜를 **1970년 1월 1일 00:00:00 UTC**부터 지난 시간을 밀리초(ms) 단위의 숫자로 관리한다.

이 숫자를 **Timestamp(타임스탬프)** 라고 한다.

---

# getTime()

현재 날짜를 Timestamp로 반환한다.

```javascript
const now =

    new Date();

console.log(

    now.getTime()

);
```

출력 예시

```text
1784707200000
```

환경에 따라 숫자는 달라질 수 있다.

---

# Date.now()

현재 시간을 Timestamp로 바로 가져올 수도 있다.

```javascript
console.log(
    Date.now()
);
```

`new Date().getTime()`과 같은 값을 반환한다.

---

# 날짜 차이 계산

Timestamp를 이용하면 날짜 차이를 계산할 수 있다.

```javascript
const start =

    new Date(

        "2026-07-01"

    );

const end =

    new Date(

        "2026-07-22"

    );

const diff =

    end.getTime() -

    start.getTime();

console.log(diff);
```

출력 예시

```text
1814400000
```

밀리초 단위의 차이가 출력된다.

---

# 일(day) 계산

```javascript
const days =

    diff /

    (1000 * 60 * 60 * 24);

console.log(days);
```

출력

```text
21
```

---

# D-Day 계산

```javascript
const today =

    new Date();

const dday =

    new Date(

        "2026-12-25"

    );

const diff =

    dday.getTime()

    -

    today.getTime();

const days =

    Math.ceil(

        diff /

        (1000 * 60 * 60 * 24)

    );

console.log(

    "D-" + days

);
```

출력 예시

```text
D-156
```

> **실무 팁**  
> `Math.ceil()`을 사용하면 남은 날짜를 올림 처리하여 사용자에게 직관적인 D-Day를 표시할 수 있다.

---

# 날짜 포맷팅

날짜를 원하는 형식으로 출력할 수도 있다.

```javascript
const now =

    new Date();

const result =

    now.getFullYear()

    + "-"

    + (now.getMonth() + 1)

    + "-"

    + now.getDate();

console.log(result);
```

출력 예시

```text
2026-7-22
```

---

# 두 자리 숫자로 출력

```javascript
const month =

    String(

        now.getMonth() + 1

    ).padStart(2,"0");

const day =

    String(

        now.getDate()

    ).padStart(2,"0");

console.log(

    `${now.getFullYear()}-${month}-${day}`

);
```

출력

```text
2026-07-22
```

---

# Timer와 함께 사용하기

`Date` 객체는 `setInterval()`과 함께 자주 사용된다.

```javascript
setInterval(function(){

    const now =

        new Date();

    console.log(

        now.toLocaleTimeString()

    );

},1000);
```

매초 현재 시간이 출력된다.

---

# 실무 활용

`Date` 객체는 다음과 같은 기능에서 자주 사용된다.

- D-Day 계산
- 이벤트 종료 시간
- 예약 시스템
- 게시글 작성 시간
- 출석 체크
- 나이 계산
- 자동 로그 기록
- 디지털 시계

---

# Date 디버깅

문제가 발생하면 다음 사항을 확인한다.

```text
1. Month가 0부터 시작하는 것을 고려했는가?
2. 날짜 차이는 Timestamp로 계산했는가?
3. 밀리초(ms)를 일(day) 단위로 올바르게 변환했는가?
4. padStart()를 사용해 두 자리 형식을 맞췄는가?
5. 현재 시간을 계속 표시하려면 setInterval() 안에서 new Date()를 생성했는가?
```

---

---

# 실무 예제 프로젝트

이번 예제에서는 현재 날짜와 시간을 화면에 출력하는 디지털 시계를 구현한다.

## HTML

```html
<h1 id="clock">

00:00:00

</h1>
```

---

## JavaScript

```javascript
const clock =

    document.querySelector(

        "#clock"

    );

function updateClock(){

    const now =

        new Date();

    const hour =

        String(

            now.getHours()

        ).padStart(2,"0");

    const minute =

        String(

            now.getMinutes()

        ).padStart(2,"0");

    const second =

        String(

            now.getSeconds()

        ).padStart(2,"0");

    clock.innerText =

        `${hour}:${minute}:${second}`;

}

updateClock();

setInterval(

    updateClock,

    1000

);
```

---

# 예제 코드 흐름

```text
페이지 실행
      ↓
new Date()
      ↓
현재 시간 가져오기
      ↓
padStart()로 두 자리 맞춤
      ↓
화면 출력
      ↓
setInterval()
      ↓
1초마다 반복
```

---

# 날짜 비교

두 날짜를 비교할 때는 Timestamp를 사용하는 것이 가장 안전하다.

```javascript
const today =

    new Date();

const eventDate =

    new Date(

        "2026-08-15"

    );

if(

    today.getTime()

    >

    eventDate.getTime()

){

    console.log(

        "이벤트 종료"

    );

}
```

---

# 나이 계산

```javascript
const birth =

    new Date(

        "2000-03-15"

    );

const today =

    new Date();

const age =

    today.getFullYear()

    -

    birth.getFullYear();

console.log(age);
```

> **실무 팁**  
> 실제 만나이는 생일이 지났는지 여부까지 확인해야 한다. 위 예제는 기본적인 계산 방식이며, 서비스에서는 월과 일도 함께 비교하여 정확한 나이를 계산한다.

---

# 자주 하는 실수

## Month를 그대로 사용하는 경우

잘못된 코드

```javascript
console.log(

    now.getMonth()

);
```

7월인데

```text
6
```

이 출력된다.

올바른 코드

```javascript
console.log(

    now.getMonth() + 1

);
```

---

## Date 객체를 한 번만 생성하는 경우

```javascript
const now =

    new Date();

setInterval(function(){

    console.log(now);

},1000);
```

시간이 계속 바뀌지 않는다.

올바른 코드

```javascript
setInterval(function(){

    const now =

        new Date();

    console.log(now);

},1000);
```

---

## Timestamp를 사용하지 않는 경우

잘못된 코드

```javascript
const diff =

    end - start;
```

권장 코드

```javascript
const diff =

    end.getTime()

    -

    start.getTime();
```

---

## 날짜 형식을 맞추지 않는 경우

```javascript
2026-7-2
```

보다

```javascript
2026-07-02
```

처럼 두 자리 형식을 사용하는 것이 일반적이다.

---

# 디버깅 체크리스트

```text
1. Month가 0부터 시작하는 것을 고려했는가?
2. 날짜 비교에 Timestamp를 사용했는가?
3. padStart()로 날짜와 시간을 두 자리로 맞췄는가?
4. setInterval() 안에서 new Date()를 생성했는가?
5. D-Day 계산 시 Math.ceil() 또는 Math.floor()를 목적에 맞게 사용했는가?
6. 날짜 문자열 형식이 올바른가?
```

---

# 이번 문서에서 배운 내용

- Date 객체 생성
- 현재 날짜와 시간
- getFullYear()
- getMonth()
- getDate()
- getDay()
- getHours()
- getMinutes()
- getSeconds()
- setFullYear()
- setMonth()
- setDate()
- getTime()
- Date.now()
- 날짜 차이 계산
- D-Day 계산
- 날짜 포맷팅
- 디지털 시계 구현

---

# 면접 포인트

### Date 객체란 무엇인가?

JavaScript에서 날짜와 시간을 처리하기 위한 내장 객체이다.

---

### getMonth() 사용 시 주의할 점은?

월은 0부터 시작하므로 실제 월을 출력하려면 `+1`을 해야 한다.

---

### Timestamp란 무엇인가?

1970년 1월 1일 00:00:00 UTC부터 경과한 시간을 밀리초(ms) 단위로 나타낸 값이다.

---

### 날짜 차이는 어떻게 계산하는가?

두 `Date` 객체의 `getTime()` 값을 빼서 밀리초 차이를 구한 뒤 필요한 단위(초, 분, 시간, 일)로 변환한다.

---

### Date.now()와 new Date()의 차이는?

- `Date.now()`는 현재 시간을 Timestamp(숫자)로 반환한다.
- `new Date()`는 날짜와 시간을 담은 `Date` 객체를 생성한다.

---

# 핵심 정리

- `Date` 객체는 날짜와 시간을 관리한다.
- `getMonth()`는 0부터 시작한다.
- `getTime()`을 이용하면 날짜 차이를 계산할 수 있다.
- `Date.now()`는 현재 Timestamp를 반환한다.
- `padStart()`를 이용하면 날짜와 시간을 일정한 형식으로 출력할 수 있다.
- `Date`는 `setInterval()`과 함께 디지털 시계, D-Day, 예약 시스템 등에서 자주 사용된다.

---

# 변경 이력

| Version | 날짜 | 변경 내용 |
|---------|------|-----------|
| v1.0 | 2026-07-22 | 최초 작성 |
