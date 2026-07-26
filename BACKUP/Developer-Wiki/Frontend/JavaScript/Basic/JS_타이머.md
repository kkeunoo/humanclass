---
title: JS_타이머
version: v1.0
last_updated: 2026-07-22
status: completed
---

# 문서 정보

| 항목 | 내용 |
|------|------|
| 문서명 | JS_타이머 |
| 분야 | Frontend / JavaScript |
| 버전 | v1.0 |
| 작성일 | 2026-07-22 |

---

# 개요

JavaScript는 일정 시간이 지난 후 코드를 실행하거나, 일정한 시간 간격으로 반복 실행하는 기능을 제공한다.

이 기능을 **타이머(Timer)** 라고 하며 다음과 같은 기능에서 많이 사용된다.

- 알림창
- 자동 슬라이드
- 광고 배너
- 디지털 시계
- 카운트다운
- 버튼 중복 클릭 방지
- 자동 로그아웃
- 게임

이번 문서에서는 JavaScript의 대표적인 타이머 함수인 `setTimeout()`과 `setInterval()` 그리고 이를 종료하는 방법을 학습한다.

---

# 핵심 개념

JavaScript의 타이머는 크게 두 가지가 있다.

| 함수 | 설명 |
|------|------|
| setTimeout() | 일정 시간이 지난 후 한 번 실행 |
| setInterval() | 일정 시간마다 반복 실행 |

---

# setTimeout()

지정한 시간이 지난 후 **한 번만** 실행된다.

기본 문법

```javascript
setTimeout(

    함수,

    시간(ms)

);
```

---

# 첫 번째 예제

```javascript
setTimeout(

    function(){

        console.log("3초 후 실행");

    },

    3000

);
```

출력

```text
(3초 후)

3초 후 실행
```

---

# 화살표 함수 사용

```javascript
setTimeout(

    () => {

        console.log("실행");

    },

    1000

);
```

---

# 시간 단위

```text
1000 = 1초

2000 = 2초

3000 = 3초

5000 = 5초
```

---

# 함수를 직접 전달하기

```javascript
function hello(){

    console.log("안녕하세요.");

}

setTimeout(

    hello,

    2000

);
```

> **실무 팁**  
> `setTimeout(hello(), 2000)`처럼 괄호를 붙이면 함수가 즉시 실행된다. 실행 예약을 하려면 함수 자체(`hello`)를 전달해야 한다.

---

# setInterval()

지정한 시간마다 계속 실행된다.

기본 문법

```javascript
setInterval(

    함수,

    시간(ms)

);
```

---

# 첫 번째 예제

```javascript
setInterval(

    function(){

        console.log("1초");

    },

    1000

);
```

출력

```text
1초

1초

1초

1초

...
```

---

# setInterval() 실행 흐름

```text
시작

↓

1초

↓

실행

↓

1초

↓

실행

↓

반복
```

---

---

# clearTimeout()

`setTimeout()`으로 예약한 작업은 실행되기 전에 취소할 수 있다.

이때 사용하는 함수가 `clearTimeout()`이다.

기본 문법

```javascript
const timer =

    setTimeout(

        함수,

        시간

    );

clearTimeout(
    timer
);
```

---

# 실행 취소 예제

```javascript
const timer =

    setTimeout(

        function(){

            console.log("실행");

        },

        5000

    );

clearTimeout(
    timer
);
```

출력

```text
(출력 없음)
```

5초 전에 타이머가 취소되었기 때문에 실행되지 않는다.

---

# clearInterval()

`setInterval()`의 반복 실행을 종료한다.

기본 문법

```javascript
const timer =

    setInterval(

        함수,

        시간

    );

clearInterval(
    timer
);
```

---

# 반복 종료 예제

```javascript
const timer =

    setInterval(

        function(){

            console.log("실행");

        },

        1000

    );

setTimeout(

    function(){

        clearInterval(timer);

    },

    5000

);
```

출력

```text
실행
실행
실행
실행
실행

(종료)
```

---

# Timer ID

`setTimeout()`과 `setInterval()`은 타이머를 식별할 수 있는 **Timer ID**를 반환한다.

```javascript
const timer =

    setTimeout(

        function(){

            console.log("Hello");

        },

        3000

    );

console.log(timer);
```

출력 예시

```text
1
```

브라우저마다 숫자는 다를 수 있다.

이 ID를 이용하여 타이머를 취소한다.

---

# 카운트다운

```javascript
let count = 5;

const timer =

    setInterval(

        function(){

            console.log(count);

            count--;

            if(count < 0){

                clearInterval(timer);

            }

        },

        1000

    );
```

출력

```text
5

4

3

2

1

0
```

---

# 화면에 카운트다운 출력

HTML

```html
<h1 id="count">

5

</h1>
```

JavaScript

```javascript
let count = 5;

const title =

    document.querySelector(

        "#count"

    );

const timer =

    setInterval(

        function(){

            title.innerText = count;

            count--;

            if(count < 0){

                clearInterval(timer);

            }

        },

        1000

    );
```

---

# 디지털 시계

```javascript
setInterval(

    function(){

        const now =

            new Date();

        console.log(

            now.toLocaleTimeString()

        );

    },

    1000

);
```

출력

```text
15:20:01

15:20:02

15:20:03
```

---

# 버튼 중복 클릭 방지

HTML

```html
<button id="submit">

전송

</button>
```

JavaScript

```javascript
const submit =

    document.querySelector(

        "#submit"

    );

submit.addEventListener(

    "click",

    function(){

        submit.disabled = true;

        setTimeout(

            function(){

                submit.disabled = false;

            },

            3000

        );

    }

);
```

3초 동안 버튼을 다시 누를 수 없게 된다.

> **실무 팁**  
> 서버에 데이터를 전송하는 버튼은 연속 클릭을 막기 위해 일시적으로 비활성화하는 경우가 많다. 중복 주문이나 중복 결제를 방지하는 데 활용된다.

---

# 자동 슬라이드 예제

```javascript
let index = 0;

setInterval(

    function(){

        index++;

        console.log(index);

    },

    2000

);
```

실제 프로젝트에서는 `index`를 이용하여 다음 이미지를 보여준다.

---

# 실무 활용

타이머는 다음과 같은 기능에서 자주 사용된다.

- 자동 슬라이드
- 광고 배너
- 디지털 시계
- 시험 시간 표시
- 로그인 유지 시간
- 자동 로그아웃
- 버튼 비활성화
- 게임 애니메이션
- 로딩 화면

---

# 타이머 디버깅

문제가 발생하면 다음 사항을 확인한다.

```text
1. 시간(ms)을 올바르게 작성했는가?
2. clearTimeout() 또는 clearInterval()을 너무 빨리 호출하지 않았는가?
3. Timer ID를 변수에 저장했는가?
4. 반복 종료 조건이 올바른가?
5. 함수를 즉시 실행하지 않았는가?
```

---

---

# 실무 예제 프로젝트

이번 예제에서는 인증번호 재전송 버튼을 구현한다.

버튼을 누르면 10초 동안 비활성화되고, 시간이 지나면 다시 활성화된다.

## HTML

```html
<button id="authBtn">

인증번호 받기

</button>
```

---

## JavaScript

```javascript
const authBtn =
    document.querySelector(
        "#authBtn"
    );

authBtn.addEventListener(
    "click",
    function(){

        authBtn.disabled = true;

        authBtn.innerText =
            "10초 후 재전송";

        let count = 10;

        const timer =
            setInterval(function(){

                count--;

                authBtn.innerText =
                    count + "초 후 재전송";

                if(count <= 0){

                    clearInterval(timer);

                    authBtn.disabled = false;

                    authBtn.innerText =
                        "인증번호 받기";

                }

            }, 1000);

    }
);
```

---

# 예제 코드 흐름

```text
버튼 클릭
      ↓
버튼 비활성화
      ↓
setInterval 시작
      ↓
1초마다 숫자 감소
      ↓
0초
      ↓
clearInterval()
      ↓
버튼 활성화
```

---

# setTimeout()과 setInterval() 비교

| setTimeout() | setInterval() |
|--------------|---------------|
| 한 번 실행 | 반복 실행 |
| 일정 시간이 지나면 종료 | 직접 종료할 때까지 반복 |
| clearTimeout() 사용 | clearInterval() 사용 |

---

# 자주 하는 실수

## 함수를 즉시 실행하는 경우

잘못된 코드

```javascript
setTimeout(
    hello(),
    1000
);
```

`hello()`가 즉시 실행된다.

올바른 코드

```javascript
setTimeout(
    hello,
    1000
);
```

---

## Timer ID를 저장하지 않는 경우

잘못된 코드

```javascript
setInterval(function(){

    console.log("실행");

},1000);

clearInterval();
```

어떤 타이머를 종료해야 하는지 알 수 없다.

올바른 코드

```javascript
const timer =
    setInterval(function(){

        console.log("실행");

    },1000);

clearInterval(timer);
```

---

## 종료 조건이 없는 경우

```javascript
setInterval(function(){

    console.log("계속 실행");

},1000);
```

반복이 계속 실행된다.

필요한 경우 반드시 종료 조건을 작성한다.

---

## ms 단위를 착각하는 경우

```javascript
setTimeout(

    hello,

    5

);
```

5초가 아니라 **5ms**이다.

```text
1000 = 1초
```

---

# 디버깅 체크리스트

```text
1. Timer ID를 저장했는가?
2. clearTimeout()과 clearInterval()을 올바르게 사용했는가?
3. ms 단위를 확인했는가?
4. 종료 조건이 존재하는가?
5. 함수를 즉시 실행하지 않았는가?
6. 이벤트가 중복 등록되지 않았는가?
7. setInterval()이 여러 번 실행되고 있지는 않은가?
```

---

# 이번 문서에서 배운 내용

- setTimeout()
- clearTimeout()
- setInterval()
- clearInterval()
- Timer ID
- 카운트다운
- 디지털 시계
- 버튼 중복 클릭 방지
- 자동 슬라이드
- 인증번호 재전송 구현

---

# 면접 포인트

### setTimeout()과 setInterval()의 차이점은?

- `setTimeout()`은 일정 시간이 지난 후 한 번만 실행된다.
- `setInterval()`은 일정 시간마다 반복 실행된다.

---

### clearTimeout()은 언제 사용하는가?

예약된 `setTimeout()` 작업을 실행 전에 취소할 때 사용한다.

---

### clearInterval()은 언제 사용하는가?

반복 실행 중인 `setInterval()`을 종료할 때 사용한다.

---

### Timer ID란 무엇인가?

`setTimeout()`과 `setInterval()`이 반환하는 식별자이다.

이 값을 이용해 해당 타이머를 취소할 수 있다.

---

### setTimeout(hello(), 1000)이 잘못된 이유는?

`hello()`가 즉시 실행되기 때문이다.

예약 실행을 하려면 함수 자체(`hello`)를 전달해야 한다.

---

# 핵심 정리

- `setTimeout()`은 한 번 실행되는 타이머이다.
- `setInterval()`은 반복 실행되는 타이머이다.
- 타이머를 종료하려면 ID를 저장해야 한다.
- `clearTimeout()`과 `clearInterval()`으로 실행을 취소할 수 있다.
- 시간 단위는 ms(밀리초)이다.
- 타이머는 카운트다운, 시계, 자동 슬라이드, 인증번호 재전송 등에서 많이 사용된다.

---

# 변경 이력

| Version | 날짜 | 변경 내용 |
|---------|------|-----------|
| v1.0 | 2026-07-22 | 최초 작성 |
