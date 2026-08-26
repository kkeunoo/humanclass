# JavaScript 동기·비동기와 이벤트 루프

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `14_JavaScript_동기비동기와_이벤트루프.md` |
| 분류 | `03_JavaScript` |
| 원본 기준 | `workspace/workspace_html/javascript/14_async.html`, `workspace_teacher/workspace_html/javascript/14_async.html` |
| 핵심 범위 | 동기 실행, 함수 호출 순서, 호출 스택, `setTimeout()`, 0ms 지연, 비동기 callback, task queue, event loop, 실행 순서 예측 |
| 실습 범위 | 함수 호출 순서, 0ms 타이머, 여러 타이머, Microtask·Task 순서, 타이머 취소, Loading 상태 |
| 문서 형식 | JavaScript Developer-Wiki V3 개인 강의 백과사전 형식 |

> 이 문서는 내 코드와 강사님 코드의 `14_async.html`을 직접 비교해 작성했습니다. 두 파일은 `fn1()` → `fn2()` → `fn3()`의 동기 호출 흐름과 `setTimeout(..., 0)` callback의 비동기 실행 순서를 보여 줍니다. 내 코드는 설명이 훨씬 많고, 주석 처리된 단일 timeout 예제와 timeout 두 개의 실행 순서를 별도로 설명합니다. 원본에는 “같은 setTimeout 0이면 동기화된 것”이라는 표현과 “동기화가 안 되어 있다”라는 다소 부정확한 설명이 있으므로 원문은 보존하고 이벤트 루프 관점에서 정확히 보완합니다.

---

# 학습 목표

- 동기 실행이 무엇인지 설명한다.
- 함수 호출이 호출 스택에 쌓이고 빠지는 흐름을 이해한다.
- `fn1()`에서 `fn2()`를 호출했을 때 실행 순서를 예측한다.
- `fn2()`에서 `fn3()`를 두 번 호출했을 때 출력 순서를 설명한다.
- `setTimeout(callback, 0)`이 즉시 실행을 의미하지 않는다는 점을 이해한다.
- timeout callback이 현재 동기 코드가 끝난 뒤 실행되는 이유를 설명한다.
- 같은 delay의 timeout callback이 등록 순서대로 실행되는 일반적 동작을 이해한다.
- “같은 timeout이면 동기”라는 표현이 왜 부정확한지 설명한다.
- 호출 스택, Web API, task queue, event loop의 관계를 설명한다.
- 실행 순서를 직접 추적하고 예측하는 습관을 기른다.
- 내 코드와 강사님 코드의 설명 차이를 정확히 기록한다.

---

# 1. 동기 실행이란?

동기 실행은 현재 작업이 끝난 뒤 다음 작업을 실행하는 흐름입니다.

```js
console.log("A")
console.log("B")
console.log("C")
```

출력:

```text
A
B
C
```

위에서 아래 순서대로 실행됩니다.

---

# 2. 함수 호출도 동기적으로 실행

원본:

```js
function fn1() {
  console.log("fn1 실행")

  fn2()
}
```

`fn1()`을 호출하면 먼저 `"fn1 실행"`을 출력하고, 이어서 `fn2()`를 호출합니다.

`fn2()`가 끝나기 전에는 `fn1()` 호출도 완전히 끝나지 않습니다.

---

# 3. Fn2 호출

원본:

```js
function fn2() {
  console.log("fn2 실행")

  fn3()
  fn3()

  console.log("1")

  setTimeout(
    function() {
      console.log("2")
    },
    0
  )

  setTimeout(
    function() {
      console.log("3")
    },
    0
  )

  console.log("마지막")
}
```

동기 코드와 비동기 callback 등록이 함께 있습니다.

---

# 4. Fn3 두 번 호출

원본:

```js
function fn3() {
  console.log("fn3 실행")
}
```

`fn2()` 안에서 두 번 호출합니다.

```js
fn3()
fn3()
```

따라서:

```text
fn3 실행
fn3 실행
```

이 연속으로 출력됩니다.

---

# 5. 전체 동기 호출 흐름

시작:

```js
fn1()
```

호출 관계:

```text
fn1()
└─ fn2()
   ├─ fn3()
   └─ fn3()
```

timeout callback을 제외한 동기 출력 순서:

```text
fn1 실행
fn2 실행
fn3 실행
fn3 실행
1
마지막
```

---

# 6. 호출 스택

JavaScript는 실행 중인 함수 호출을 호출 스택에 관리합니다.

개념적 흐름:

```text
fn1 호출
→ fn1이 stack에 들어감

fn2 호출
→ fn2가 fn1 위에 들어감

fn3 호출
→ fn3가 fn2 위에 들어감

fn3 종료
→ stack에서 제거

다시 fn3 호출
→ stack에 들어감

fn3 종료
→ 제거

fn2 종료
→ 제거

fn1 종료
→ 제거
```

원본에는 호출 스택 용어가 직접 나오지 않지만 실행 순서를 이해하기 위한 확장 설명입니다.

---

# 7. SetTimeout 0의 의미

원본:

```js
setTimeout(
  function() {
    console.log("2")
  },
  0
)
```

`0`은 callback을 즉시 현재 줄에서 실행한다는 뜻이 아닙니다.

보다 정확한 의미:

```text
최소 지연 시간이 지난 뒤
현재 호출 스택이 비었을 때
callback 실행 기회를 기다림
```

---

# 8. 현재 동기 코드가 먼저 끝나는 이유

`setTimeout()`을 만나면 callback을 등록한 뒤 JavaScript는 다음 줄로 계속 진행합니다.

```js
setTimeout(
  function() {
    console.log("2")
  },
  0
)

console.log("마지막")
```

출력:

```text
마지막
2
```

`console.log("마지막")`은 현재 호출 스택에서 즉시 실행되고, timeout callback은 이후 실행됩니다.

---

# 9. 원본 전체 출력 순서

두 원본의 실제 실행 결과:

```text
fn1 실행
fn2 실행
fn3 실행
fn3 실행
1
마지막
2
3
```

핵심:

- `fn1`, `fn2`, `fn3`, `"1"`, `"마지막"`은 동기 실행
- `"2"`, `"3"`은 timeout callback
- 현재 동기 코드가 모두 끝난 뒤 callback 실행
- timeout 등록 순서는 `"2"` callback이 먼저, `"3"` callback이 다음

---

# 10. 같은 0ms Timeout 순서

원본:

```js
setTimeout(
  function() {
    console.log("2")
  },
  0
)

setTimeout(
  function() {
    console.log("3")
  },
  0
)
```

같은 task source와 같은 환경에서 일반적으로 먼저 등록된 callback이 먼저 queue에 들어가므로:

```text
2
3
```

순서로 실행됩니다.

다만 이를 “두 timeout이 동기화되었다”고 표현하는 것은 정확하지 않습니다.

둘 다 비동기 callback입니다.

---

# 11. 내 코드의 표현 검토

내 코드 주석:

```text
같은 setTimeout 0 이라면 두개는 동기화가 된 것
```

정확한 표현:

```text
두 callback은 모두 비동기적으로 실행되며,
같은 조건에서 등록 순서대로 task queue에서 처리되는 일반적 동작을 보인다.
```

“동기”는 callback 자체가 현재 코드와 같은 호출 흐름에서 바로 실행된다는 뜻이 아닙니다.

---

# 12. “동기화가 안 되어 있다” 표현

내 코드 주석:

```text
1-3-2 순서로 출력되게 됨
이 모습이 동기화가 안 되어있는 것
```

주석 처리된 예제:

```js
console.log("1")

setTimeout(
  function() {
    console.log("2")
  },
  0
)

console.log("3")
```

출력:

```text
1
3
2
```

보다 정확한 설명:

```text
1과 3은 현재 동기 코드로 실행되고,
2는 비동기 callback으로 등록되어 호출 스택이 빈 뒤 실행된다.
```

단순히 “동기화가 안 됐다”보다 동기 코드와 비동기 callback의 실행 단계가 다르다고 설명하는 편이 정확합니다.

---

# 13. 지연 함수라는 표현

내 코드 주석:

```text
이러한 것 때문에 지연함수라고 부르며,
두 번째 인자값을 주는 것
```

`setTimeout()`은 일정 delay 이후 callback 실행을 예약하는 timer API입니다.

두 번째 인수는 최소 지연 시간이며 단위는 millisecond입니다.

```js
setTimeout(callback, 1000)
```

은 약 1초 이후 callback 실행 가능 상태가 된다는 뜻입니다.

정확히 1초 후 실행을 보장하지는 않습니다.

---

# 14. Event Loop 개념

개념적 구성:

```text
Call Stack
Web API
Task Queue
Event Loop
```

흐름:

```text
1. setTimeout 호출
2. timer가 브라우저 환경에 등록
3. delay 경과
4. callback이 task queue로 이동
5. call stack이 비었는지 event loop가 확인
6. 비어 있으면 callback을 stack으로 이동
7. callback 실행
```

원본의 출력 순서를 설명하기 위한 확장 개념입니다.

---

# 15. Web API

`setTimeout()`은 JavaScript 언어 자체의 함수라기보다 브라우저 환경이 제공하는 timer API입니다.

Node.js에도 유사한 timer API가 있습니다.

원본은 브라우저 HTML 문서에서 실행되므로 browser timer를 기준으로 이해하면 됩니다.

---

# 16. Task Queue

timeout callback은 delay가 끝났다고 바로 실행되는 것이 아닙니다.

먼저 task queue에서 대기합니다.

현재 stack에 실행 중인 코드가 있으면 기다립니다.

```text
Call Stack이 비어야 callback 실행 가능
```

---

# 17. Event Loop 역할

event loop는 지속적으로 다음을 확인합니다.

```text
Call Stack이 비었는가?
Task Queue에 실행할 callback이 있는가?
```

조건이 충족되면 queue의 callback을 stack으로 보냅니다.

---

# 18. 0ms가 즉시가 아닌 예제

```js
console.log("start")

setTimeout(
  function() {
    console.log("timeout")
  },
  0
)

for (
  let i = 0;
  i < 1000000;
  i++
) {
}

console.log("end")
```

출력:

```text
start
end
timeout
```

반복문이 끝날 때까지 timeout callback은 실행되지 않습니다.

---

# 19. Blocking

긴 동기 작업은 호출 스택을 오래 점유합니다.

```js
for (
  let i = 0;
  i < 10_000_000_000;
  i++
) {
}
```

이런 작업이 실행 중이면:

- UI 반응이 느려질 수 있음
- click event 처리 지연
- timeout callback 지연
- 화면 렌더링 지연

원본에는 없는 실무 확장 내용입니다.

---

# 20. Single Thread 기본 이해

JavaScript 실행은 일반적으로 한 번에 하나의 작업을 호출 스택에서 처리합니다.

비동기 API를 사용해도 callback의 JavaScript 코드는 결국 호출 스택에서 하나씩 실행됩니다.

따라서 비동기라고 해서 JavaScript callback들이 동시에 같은 stack에서 실행되는 것은 아닙니다.

---

# 21. 내 코드의 주석 처리 예제

내 코드에는 다음 코드가 주석 처리되어 있습니다.

```js
// setTimeout(
//   function() {
//     console.log("2")
//   },
//   0
// )

// console.log("3")
```

이 예제를 활성화하고 아래 timeout 두 개까지 그대로 두면 출력 구성이 달라질 수 있습니다.

현재 실제 실행 코드에서는 이 단일 timeout 예제가 비활성화되어 있습니다.

문서에서는 주석 설명과 실제 실행 코드를 구분해야 합니다.

---

# 22. 강사님 코드의 주석 처리된 Console

강사님 코드:

```js
// console.log("3")
```

직접 동기 출력하는 `"3"`은 주석 처리되어 있습니다.

대신 아래 timeout callback에서 `"3"`을 출력합니다.

```js
setTimeout(
  function() {
    console.log("3")
  },
  0
)
```

따라서 실제 결과의 `"3"`은 동기 출력이 아니라 비동기 callback 출력입니다.

---

# 23. 함수 선언 순서

원본에서 `fn1()`은 `fn2()`보다 먼저 작성되어 있지만 호출 시점에는 두 함수 선언이 모두 사용할 수 있습니다.

함수 선언문은 실행 컨텍스트 생성 과정에서 등록됩니다.

```js
fn1()

function fn1() {
}
```

처럼 선언문보다 앞에서 호출할 수도 있습니다.

원본은 선언 뒤 호출하므로 hoisting에 의존할 필요는 없습니다.

---

# 24. Fn2 안의 Fn3 호출

`fn3()`는 `fn2()` 안에서 두 번 호출됩니다.

```js
fn3()
fn3()
```

각 호출은 독립적으로 stack에 들어갔다가 종료됩니다.

한 번의 호출이 자동으로 재사용되는 것은 아닙니다.

---

# 25. Console 출력과 실제 실행 시간

Console 출력 순서는 실행 순서를 확인하는 데 유용하지만 Console 자체의 출력 구현은 개발자 도구 환경에 따라 차이가 있을 수 있습니다.

현재 원본처럼 단순 문자열 출력에서는 순서 확인에 충분합니다.

객체 출력은 나중에 펼쳤을 때 최신 상태로 보이는 브라우저도 있으므로 문자열과 객체 로그를 구분해야 합니다.

---

# 26. Timeout ID

`setTimeout()`은 timer ID를 반환합니다.

```js
const timerId =
  setTimeout(
    function() {
      console.log("실행")
    },
    1000
  )
```

취소:

```js
clearTimeout(
  timerId
)
```

원본은 ID를 저장하지 않습니다.

---

# 27. 취소 예제

```js
const timerId =
  setTimeout(
    function() {
      console.log("실행 안 됨")
    },
    1000
  )

clearTimeout(
  timerId
)
```

callback이 실행되기 전에 취소하면 출력되지 않습니다.

---

# 28. Timeout Delay 생략

```js
setTimeout(
  function() {
    console.log("callback")
  }
)
```

delay를 생략하면 사실상 0에 가까운 delay로 예약됩니다.

그래도 현재 동기 코드보다 먼저 실행되지 않습니다.

---

# 29. 중첩 Timeout

```js
setTimeout(
  function first() {
    console.log("first")

    setTimeout(
      function second() {
        console.log("second")
      },
      0
    )
  },
  0
)
```

첫 callback 실행 중 두 번째 callback이 새 task로 등록됩니다.

출력:

```text
first
second
```

두 callback이 같은 호출 스택에서 연속 호출되는 것은 아닙니다.

---

# 30. Timer 최소 지연

브라우저는 중첩 timer나 background tab 등 특정 상황에서 실제 delay를 늘릴 수 있습니다.

따라서:

```js
setTimeout(callback, 0)
```

은 “정확히 0ms 후”가 아니라 “가능한 빠른 다음 task 시점”으로 이해하는 것이 좋습니다.

---

# 31. 동기와 비동기 비교

| 구분 | 동기 | 비동기 |
| --- | --- | --- |
| 실행 | 현재 작업이 끝난 뒤 다음 작업 | 작업을 등록하고 나중에 callback |
| 예 | 일반 함수 호출 | `setTimeout()` callback |
| 현재 stack | 즉시 실행 | queue에서 대기 |
| 순서 | 코드 흐름대로 | event loop와 queue 영향 |
| UI 영향 | 긴 작업은 blocking | 기다리는 동안 다른 코드 진행 가능 |

---

# 32. 원본 실행 단계 추적

```text
1. fn1() 호출
2. "fn1 실행"
3. fn2() 호출
4. "fn2 실행"
5. fn3() 호출
6. "fn3 실행"
7. fn3() 호출
8. "fn3 실행"
9. "1"
10. 첫 timeout 등록
11. 두 번째 timeout 등록
12. "마지막"
13. fn2 종료
14. fn1 종료
15. stack 비어 있음
16. 첫 timeout callback 실행 → "2"
17. 두 번째 timeout callback 실행 → "3"
```

---

# 33. 예상 출력 직접 작성 습관

비동기 코드를 읽을 때 다음 순서로 분리하면 좋습니다.

```text
1. 현재 동기 코드 출력 찾기
2. callback 등록 위치 찾기
3. queue 종류 확인
4. 현재 stack 종료 시점 확인
5. callback 등록 순서 확인
6. 최종 출력 순서 작성
```

---

# 34. My Code 분석

## 34.1 장점

- 함수 안에서 다른 함수를 호출하는 동기 흐름을 설명했다.
- `fn1()`과 `fn2()`를 따로 호출하는 경우와 내부 호출을 비교하려 했다.
- `setTimeout(..., 0)`이 즉시 실행이 아니라는 점을 설명했다.
- `1-3-2` 출력 예제를 주석으로 남겨 동기 코드와 timeout callback 차이를 보여 줬다.
- timeout 두 개가 등록 순서대로 실행되는 결과를 설명했다.
- `"마지막"`이 먼저 출력되는 이유를 주석으로 기록했다.
- 각 단계에 학습용 설명을 상세히 추가했다.

## 34.2 개선점

- “fn1 안에 fn2를 넣으면 한 번에 같이 실행되므로 동기화”라는 표현은 다소 모호하다.
- 함수 호출은 순차적으로 실행되며 동시에 같이 실행되는 것이 아니다.
- `1-3-2`를 단순히 “동기화가 안 된 것”으로 표현하면 원리를 설명하기 부족하다.
- “같은 setTimeout 0이면 두 개는 동기화된 것”이라는 설명은 잘못되었다.
- 두 callback은 모두 비동기이며 queue 등록 순서가 같은 것뿐이다.
- `setTimeout`을 “지연 함수”라고만 설명하면 browser timer와 event loop 개념이 빠진다.
- 0ms는 정확한 실행 시각을 보장하지 않는다.
- 호출 스택과 task queue 설명이 없다.
- 문서 lang과 title이 학습 내용에 맞지 않는다.
- semicolon 스타일이 일관되지 않는다.

---

# 35. Teacher Code 분석

## 35.1 장점

- `fn1()` → `fn2()` → `fn3()`의 호출 관계가 간결하다.
- `fn3()` 두 번 호출 결과를 확인할 수 있다.
- 동기 출력 `"1"`과 `"마지막"` 사이에 timeout 두 개를 등록한다.
- 같은 0ms timeout의 callback 등록 순서를 쉽게 확인할 수 있다.
- 불필요한 설명 없이 실제 실행 결과에 집중한다.
- 주석 처리된 직접 `"3"` 출력과 timeout `"3"`을 구분할 수 있다.

## 35.2 개선점

- 동기와 비동기 개념 설명이 거의 없다.
- 0ms timeout이 즉시 실행되지 않는 이유를 설명하지 않는다.
- 호출 스택, task queue, event loop 설명이 없다.
- 같은 delay timeout 순서가 왜 `"2"` → `"3"`인지 설명하지 않는다.
- timer의 실제 실행 시간이 지연될 수 있다는 설명이 없다.
- clearTimeout과 timer ID 설명이 없다.
- 문서 lang과 title이 학습 내용에 맞지 않는다.

---

# 36. My Code vs Teacher Code

| 비교 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 동기 설명 | 상세 주석 있음 | 없음 |
| 1-3-2 예제 | 주석으로 상세 설명 | 직접 `"3"`만 주석 처리 |
| Timeout 두 개 설명 | 있음 | 코드만 있음 |
| “지연 함수” 표현 | 있음 | 없음 |
| “같은 timeout은 동기” 표현 | 있음, 부정확 | 없음 |
| 함수 spacing | `function fn1() {` | `function fn1(){` |
| 전체 구조 | 동일 | 동일 |
| 실제 출력 | 동일 | 동일 |
| 코드 길이 | 주석 때문에 김 | 짧고 간결 |

---

# 37. 대표 예제

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
  >
  <title>동기와 비동기</title>
</head>
<body>
  <script>
    "use strict";

    function first() {
      console.log("first 시작");

      second();

      console.log("first 끝");
    }

    function second() {
      console.log("second 시작");

      setTimeout(
        function() {
          console.log("timeout");
        },
        0
      );

      console.log("second 끝");
    }

    first();

    console.log("global 끝");
  </script>
</body>
</html>
```

출력:

```text
first 시작
second 시작
second 끝
first 끝
global 끝
timeout
```

---

# 38. 실무 활용: Loading 상태

```js
function loadData() {
  console.log(
    "로딩 시작"
  )

  setTimeout(
    function() {
      console.log(
        "데이터 처리 완료"
      )
    },
    1000
  )

  console.log(
    "다른 UI 작업 계속"
  )
}

loadData()
```

출력:

```text
로딩 시작
다른 UI 작업 계속
데이터 처리 완료
```

실제 서버 요청은 `fetch()`와 Promise 단원에서 다룹니다.

---

# 39. 실행 순서 디버깅

```js
console.log("A")

setTimeout(
  function() {
    console.log("B")
  },
  0
)

console.log("C")
```

예상:

```text
A
C
B
```

비동기 코드에서는 callback 내부 로그를 별도로 표시하면 흐름 파악에 도움이 됩니다.

---

# 40. 자주 하는 실수

## 40.1 0ms를 즉시 실행으로 생각

현재 동기 코드가 끝난 뒤 실행됩니다.

## 40.2 Timeout 두 개를 동기 코드라고 생각

둘 다 비동기 callback입니다.

## 40.3 Delay만 지나면 무조건 바로 실행된다고 생각

호출 스택이 비어야 합니다.

## 40.4 긴 동기 작업 중 Timeout이 실행될 것으로 생각

stack이 점유된 동안 callback은 대기합니다.

## 40.5 함수 호출이 동시에 실행된다고 생각

호출 스택에서 하나씩 순차 실행됩니다.

## 40.6 Console 출력만 보고 내부 queue를 구분하지 않음

동기 출력과 callback 출력을 따로 표시해야 합니다.

## 40.7 같은 Delay는 항상 정확히 같은 시각이라고 생각

등록 순서와 실행 환경에 따라 실제 시각은 달라질 수 있습니다.

## 40.8 Timer ID를 저장하지 않아 취소할 수 없음

취소가 필요하면 반환값을 저장합니다.

## 40.9 비동기를 병렬 실행과 동일시

callback JavaScript 실행은 호출 스택에서 하나씩 처리됩니다.

## 40.10 주석 처리 코드와 실제 실행 코드 혼동

원본의 `1-3-2` 예제는 실제 실행되지 않는 주석 코드입니다.

---

# 41. 면접·복습 포인트

## Q1. 동기 실행이란 무엇인가요?

현재 작업이 끝난 뒤 다음 작업을 순서대로 실행하는 방식입니다.

## Q2. SetTimeout 0은 즉시 실행인가요?

아닙니다. 최소 지연 후 task queue에서 대기하며 호출 스택이 비었을 때 실행됩니다.

## Q3. 원본 전체 출력 순서는 무엇인가요?

`fn1 실행`, `fn2 실행`, `fn3 실행`, `fn3 실행`, `1`, `마지막`, `2`, `3`입니다.

## Q4. “마지막”이 “2”보다 먼저 출력되는 이유는 무엇인가요?

“마지막”은 현재 동기 코드이고 “2”는 timeout callback이기 때문입니다.

## Q5. 두 timeout이 2, 3 순서로 출력되는 이유는 무엇인가요?

같은 조건에서 먼저 등록된 callback이 먼저 task queue에 들어가는 일반적 동작 때문입니다.

## Q6. 두 timeout을 동기라고 부를 수 있나요?

아닙니다. 둘 다 비동기 callback입니다.

## Q7. Event Loop는 무엇을 확인하나요?

호출 스택이 비었는지와 queue에 실행 가능한 callback이 있는지를 확인합니다.

## Q8. 긴 동기 반복문이 있으면 timeout은 어떻게 되나요?

반복문이 끝날 때까지 callback 실행이 지연됩니다.

## Q9. SetTimeout 반환값은 무엇에 쓰나요?

timer ID로 저장해 clearTimeout으로 취소할 수 있습니다.

## Q10. 비동기와 병렬은 같은 뜻인가요?

아닙니다. 비동기 callback의 JavaScript 실행도 호출 스택에서 하나씩 처리됩니다.

---

# Problems

## 문제 1. 기본 동기 순서

`A`, `B`, `C`를 순서대로 출력하는 코드를 작성하세요.

## 문제 2. 함수 호출 순서

`first()`가 `second()`를 호출할 때 출력 순서를 작성하세요.

## 문제 3. 원본 출력 예측

원본 `fn1()` 실행의 전체 출력 순서를 작성하세요.

## 문제 4. 0ms Timeout

`A`, timeout의 `B`, `C`가 있을 때 출력 순서를 예측하세요.

## 문제 5. 두 Timeout 순서

0ms timeout 두 개를 순서대로 등록해 `"first"`, `"second"`를 출력하세요.

## 문제 6. 마지막이 먼저인 이유

원본에서 `"마지막"`이 `"2"`보다 먼저 출력되는 이유를 설명하세요.

## 문제 7. 호출 스택

`fn1()` → `fn2()` → `fn3()` 호출 시 stack 변화를 설명하세요.

## 문제 8. Queue

timeout callback이 어떤 조건에서 호출 스택으로 이동하는지 설명하세요.

## 문제 9. 긴 반복문

timeout 뒤에 긴 반복문을 두고 callback이 늦게 실행되는지 확인하세요.

## 문제 10. Timer 취소

1초 뒤 실행할 callback을 등록한 뒤 취소하세요.

## 문제 11. Delay 생략

delay를 생략한 setTimeout과 동기 코드의 순서를 확인하세요.

## 문제 12. 중첩 Timeout

timeout callback 안에서 또 다른 timeout을 등록하세요.

## 문제 13. 함수 두 번 호출

`fn3()`를 두 번 호출했을 때 출력 횟수를 설명하세요.

## 문제 14. 잘못된 설명 수정

“같은 0ms timeout 두 개는 동기다”라는 문장을 정확히 고치세요.

## 문제 15. 비동기와 병렬

두 개념이 같은지 설명하세요.

## 문제 16. 로딩 표시

“로딩 시작”, 1초 뒤 “완료”, 즉시 “다른 작업”을 출력하세요.

## 문제 17. Timer ID

setTimeout 반환값을 변수에 저장하고 출력하세요.

## 문제 18. 실행 순서 추적

동기 코드와 timeout callback을 주석으로 구분하세요.

## 문제 19. Blocking 설명

긴 동기 작업이 UI에 미치는 영향을 설명하세요.

## 문제 20. 원본 주석 코드

원본의 `1-3-2` 예제가 현재 실제로 실행되는지 설명하세요.

## 문제 21. Event Loop 설명

call stack, Web API, task queue를 포함해 설명하세요.

## 문제 22. 종합 실행 순서

다음 코드의 출력 순서를 작성하고 이유를 설명하세요.

```js
console.log("A")

setTimeout(
  function() {
    console.log("B")

    setTimeout(
      function() {
        console.log("C")
      },
      0
    )
  },
  0
)

console.log("D")

setTimeout(
  function() {
    console.log("E")
  },
  0
)
```

---

# Answers & Explanations

## 정답 1

```js
console.log("A")
console.log("B")
console.log("C")
```

## 정답 2

```js
function first() {
  console.log("first")
  second()
}

function second() {
  console.log("second")
}

first()
```

출력:

```text
first
second
```

## 정답 3

```text
fn1 실행
fn2 실행
fn3 실행
fn3 실행
1
마지막
2
3
```

## 정답 4

```js
console.log("A")

setTimeout(
  function() {
    console.log("B")
  },
  0
)

console.log("C")
```

출력:

```text
A
C
B
```

## 정답 5

```js
setTimeout(
  function() {
    console.log("first")
  },
  0
)

setTimeout(
  function() {
    console.log("second")
  },
  0
)
```

## 정답 6

`"마지막"`은 현재 호출 스택에서 실행되는 동기 코드이고 `"2"`는 timeout callback이라 task queue에서 기다리기 때문입니다.

## 정답 7

```text
fn1 stack 진입
→ fn2 진입
→ fn3 진입
→ fn3 종료
→ fn3 다시 진입
→ fn3 종료
→ fn2 종료
→ fn1 종료
```

## 정답 8

delay가 지나 callback이 queue에 들어가고, 현재 호출 스택이 비었을 때 event loop가 callback을 stack으로 이동합니다.

## 정답 9

```js
setTimeout(
  function() {
    console.log("timeout")
  },
  0
)

for (
  let i = 0;
  i < 100000000;
  i++
) {
}

console.log("loop 끝")
```

일반적으로:

```text
loop 끝
timeout
```

순서입니다.

## 정답 10

```js
const timerId =
  setTimeout(
    function() {
      console.log("실행")
    },
    1000
  )

clearTimeout(
  timerId
)
```

## 정답 11

```js
setTimeout(
  function() {
    console.log("timeout")
  }
)

console.log("sync")
```

출력:

```text
sync
timeout
```

## 정답 12

```js
setTimeout(
  function() {
    console.log("first")

    setTimeout(
      function() {
        console.log("second")
      },
      0
    )
  },
  0
)
```

## 정답 13

함수를 두 번 호출했으므로 함수 본문도 두 번 실행되고 `"fn3 실행"`이 두 번 출력됩니다.

## 정답 14

```text
같은 0ms timeout 두 개는 모두 비동기 callback이며,
일반적으로 등록 순서대로 task queue에서 처리된다.
```

## 정답 15

같지 않습니다. 비동기는 작업 완료를 기다리지 않고 다음 흐름을 진행하는 방식이고, 병렬은 여러 작업이 실제로 동시에 진행되는 것을 뜻합니다.

## 정답 16

```js
console.log(
  "로딩 시작"
)

setTimeout(
  function() {
    console.log("완료")
  },
  1000
)

console.log(
  "다른 작업"
)
```

## 정답 17

```js
const timerId =
  setTimeout(
    function() {
      console.log("실행")
    },
    1000
  )

console.log(timerId)
```

## 정답 18

```js
// 동기
console.log("A")

// 비동기 callback 등록
setTimeout(
  function() {
    console.log("B")
  },
  0
)

// 동기
console.log("C")
```

## 정답 19

긴 동기 작업은 호출 스택을 오래 점유해 화면 렌더링, click event, timeout callback 등의 처리를 지연시킬 수 있습니다.

## 정답 20

현재는 주석 처리되어 있으므로 실행되지 않습니다. 실제 실행 코드에는 timeout `"2"`, timeout `"3"`, 동기 `"마지막"`이 있습니다.

## 정답 21

`setTimeout()`이 호출되면 browser Web API가 timer를 관리합니다. delay가 끝나면 callback이 task queue에 들어갑니다. event loop는 call stack이 비었는지 확인하고, 비어 있으면 queue의 callback을 stack으로 이동시켜 실행합니다.

## 정답 22

출력:

```text
A
D
B
E
C
```

이유:

```text
A
→ 동기

첫 timeout B 등록

D
→ 동기

두 번째 timeout E 등록

현재 stack 종료

B callback 실행
→ B 출력
→ 내부 timeout C 등록

E callback 실행
→ E 출력

다음 task인 C callback 실행
→ C 출력
```

---

# Final Checklist

## 동기 실행

- [ ] 위에서 아래로 실행되는 기본 순서를 이해했다.
- [ ] 함수 호출이 끝나야 호출한 위치로 돌아감을 이해했다.
- [ ] fn3가 두 번 호출되어 두 번 출력됨을 확인했다.
- [ ] 호출 스택의 push·pop 흐름을 이해했다.
- [ ] 함수 호출이 동시에 실행되는 것이 아님을 이해했다.

## SetTimeout

- [ ] 0ms가 즉시 실행을 의미하지 않음을 이해했다.
- [ ] delay가 최소 대기 시간임을 이해했다.
- [ ] timeout 등록 후 다음 동기 코드가 계속 실행됨을 확인했다.
- [ ] timer callback이 task queue에서 대기함을 이해했다.
- [ ] 현재 stack이 비어야 callback이 실행됨을 이해했다.
- [ ] timer ID와 clearTimeout 사용법을 이해했다.

## Event Loop

- [ ] call stack의 역할을 이해했다.
- [ ] Web API의 timer 관리 역할을 이해했다.
- [ ] task queue의 대기 역할을 이해했다.
- [ ] event loop가 stack과 queue를 확인함을 이해했다.
- [ ] 긴 동기 작업이 callback을 지연시킴을 이해했다.
- [ ] 비동기와 병렬을 구분했다.

## 원본 실행

- [ ] 실제 출력 순서를 정확히 작성했다.
- [ ] `"마지막"`이 `"2"`보다 먼저인 이유를 설명했다.
- [ ] `"2"`와 `"3"` timeout 등록 순서를 확인했다.
- [ ] 강사님 `"console.log('3')"`가 주석임을 확인했다.
- [ ] 내 `1-3-2` 예제가 주석 처리 상태임을 확인했다.
- [ ] 두 timeout을 동기라고 부르지 않았다.

## 원본 코드 검수

- [ ] 두 실제 14_async.html만 비교했다.
- [ ] 내 코드의 상세 주석을 기록했다.
- [ ] 강사님 코드의 간결한 구조를 기록했다.
- [ ] 실제 실행 코드는 양쪽이 같은 흐름임을 확인했다.
- [ ] “같은 timeout은 동기” 표현을 보완했다.
- [ ] “동기화가 안 됨” 표현을 보완했다.
- [ ] 0ms 정확성 오해를 보완했다.
- [ ] 문서 lang과 title 개선을 기록했다.
- [ ] BACKUP을 분석하지 않았다.

---

# Key Summary

- JavaScript 14번은 함수 호출의 동기 흐름과 `setTimeout()` callback의 비동기 실행 순서를 다룬다.
- `fn1()`은 `"fn1 실행"`을 출력한 뒤 `fn2()`를 호출한다.
- `fn2()`는 `"fn2 실행"` 후 `fn3()`를 두 번 호출한다.
- 따라서 `"fn3 실행"`은 두 번 출력된다.
- timeout 전의 `"1"`과 timeout 뒤의 `"마지막"`은 현재 호출 스택에서 동기적으로 실행된다.
- `setTimeout(callback, 0)`은 callback을 즉시 실행하지 않는다.
- 0ms는 최소 지연 후 가능한 다음 task 시점에 실행될 수 있다는 뜻이다.
- timeout callback은 현재 호출 스택이 끝날 때까지 기다린다.
- 원본 전체 출력은 `fn1 실행`, `fn2 실행`, `fn3 실행`, `fn3 실행`, `1`, `마지막`, `2`, `3`이다.
- `"마지막"`이 먼저 출력되는 이유는 동기 코드이고 `"2"`와 `"3"`은 비동기 callback이기 때문이다.
- 같은 0ms timeout 두 개는 동기 코드가 아니다.
- 둘 다 비동기 callback이며 일반적으로 등록 순서대로 task queue에서 처리된다.
- 내 코드의 “같은 setTimeout 0이면 동기화”라는 표현은 부정확하다.
- 내 코드의 `1-3-2` 설명은 동기 코드와 비동기 callback 순서로 설명하는 편이 정확하다.
- `setTimeout()`은 browser timer API이며 delay 뒤 callback을 queue에 넣는다.
- event loop는 호출 스택이 비었을 때 queue의 callback을 실행시킨다.
- 긴 동기 작업은 timeout, click event, 화면 렌더링을 지연시킬 수 있다.
- 비동기는 병렬 실행과 같은 뜻이 아니다.
- timeout ID를 저장하면 `clearTimeout()`으로 취소할 수 있다.
- 강사님 코드의 직접 `"3"` 출력은 주석 처리되어 있고 실제 `"3"`은 timeout callback에서 출력된다.
- 내 코드의 `1-3-2` 예제도 현재는 주석 처리되어 실제 실행되지 않는다.
# V3 실행 추적 카드 — 동기 스택 → Web API → 작업 큐 → 콜백

JavaScript는 현재 호출 스택을 먼저 비운다. 타이머·이벤트·네트워크 완료 콜백은 준비되더라도 스택이 빌 때까지 기다린다. Promise 반응 작업은 일반 타이머보다 먼저 처리되는 microtask다.

동기 `A`, Promise의 `B`, 0ms 타이머의 `C`를 등록하면 보통 `A`, `B`, `C` 순이다. 지연시간은 정확한 실행 보장 시간이 아니다.

**원본 연결:** 내 코드와 강사님 코드의 `workspace_html/javascript/14_async.html`에서 실제 사용 위치와 차이를 확인한다.
