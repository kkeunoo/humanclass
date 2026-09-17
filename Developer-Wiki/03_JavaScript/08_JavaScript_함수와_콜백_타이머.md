---
title: JavaScript 함수와 콜백·타이머
version: v4.0-detailed-source
last_updated: 2026-09-17
status: Completed
---

# JavaScript 함수와 콜백·타이머

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `08_JavaScript_함수와_콜백_타이머.md` |
| 분류 | `03_JavaScript` |
| 원본 기준 | `workspace_html/javascript/08_function.html`, `workspace_teacher/workspace_html/javascript/08_function.html` |
| 핵심 범위 | 함수 선언·호출, 매개변수, 반환값, 스코프, 기본 매개변수, 익명 함수, 함수 참조, 콜백, 정렬 함수, 타이머 |
| 실습 범위 | 넓이 계산, 중첩 호출, 콜백 실행, 숫자 정렬, 지연 실행, 반복 타이머, 예약 취소 |
| 문서 형식 | JavaScript Developer-Wiki V3 개인 강의 백과사전 형식 |

> 이 문서는 내 코드와 강사님 코드 전체를 그대로 나열하지 않는다.  
> 함수와 콜백·타이머를 이해하는 데 필요한 핵심 코드만 발췌하고, 실행 순서·반환값·스코프·비동기 예약의 차이를 함께 설명한다.

---

## 이 문서에서 바로 찾기

- [개념에서 실제 실행까지: 함수는 호출할 때 동작하고, return은 호출자에게 값을 준다](#js-08-section-4)
- [26. 함수 참조와 호출 결과 비교](#js-08-section-30)
- [57. 내 코드와 강사님 코드 비교](#js-08-section-61)
- [59. 실무형 예제: 지연 작업 실행기](#js-08-section-63)
- [60. 대표 오류로 이해하기](#js-08-section-64)
- [61. 자주 하는 실수](#js-08-section-65)
- [62. 핵심 요약](#js-08-section-66)
- [63. 최종 체크리스트](#js-08-section-67)

<details>
<summary>세부 목차 펼치기 — 번호형 본문 전체</summary>

- [개요](#js-08-section-1)
- [핵심 개념](#js-08-section-2)
- [학습 목표](#js-08-section-3)
- [개념에서 실제 실행까지: 함수는 호출할 때 동작하고, return은 호출자에게 값을 준다](#js-08-section-4)
- [1. 함수 선언](#js-08-section-5)
- [2. 함수 호출](#js-08-section-6)
- [3. 함수 자체와 실행 결과](#js-08-section-7)
- [4. 매개변수와 인수](#js-08-section-8)
- [5. 출력하는 함수](#js-08-section-9)
- [6. 반환하는 함수](#js-08-section-10)
- [7. `return`의 두 역할](#js-08-section-11)
- [8. 덧셈 함수](#js-08-section-12)
- [9. 중첩 함수 호출](#js-08-section-13)
- [10. 이전 변수에 의존한 중첩 호출](#js-08-section-14)
- [11. 함수 지역 변수](#js-08-section-15)
- [12. 같은 이름의 지역·외부 변수](#js-08-section-16)
- [13. 블록 스코프](#js-08-section-17)
- [14. Shadowing](#js-08-section-18)
- [15. TDZ](#js-08-section-19)
- [16. 반복문의 블록 변수](#js-08-section-20)
- [17. 인수가 부족한 경우](#js-08-section-21)
- [18. `undefined` 방어](#js-08-section-22)
- [19. 기본 매개변수](#js-08-section-23)
- [20. 기본값 적용 조건](#js-08-section-24)
- [21. 중복 방어 코드](#js-08-section-25)
- [22. 인수를 많이 전달한 경우](#js-08-section-26)
- [23. 나머지 매개변수](#js-08-section-27)
- [24. 익명 함수](#js-08-section-28)
- [25. 함수 참조 복사](#js-08-section-29)
- [26. 함수 참조와 호출 결과 비교](#js-08-section-30)
- [27. 콜백 함수](#js-08-section-31)
- [28. 콜백 용어](#js-08-section-32)
- [29. 콜백 타입 검사](#js-08-section-33)
- [30. 같은 이름의 함수 선언](#js-08-section-34)
- [31. 함수 별칭](#js-08-section-35)
- [32. 선언 없는 전역 대입](#js-08-section-36)
- [33. Console 객체 참조](#js-08-section-37)
- [34. 메서드 참조](#js-08-section-38)
- [35. `console.log` 덮어쓰기](#js-08-section-39)
- [36. 내장 API 덮어쓰기 위험](#js-08-section-40)
- [37. 숫자 내림차순 함수](#js-08-section-41)
- [38. 기본 `sort()` 문제](#js-08-section-42)
- [39. 원본 배열 변경 문제](#js-08-section-43)
- [40. 안전한 숫자 내림차순](#js-08-section-44)
- [41. 함수 호출 결과 전달](#js-08-section-45)
- [42. 함수 자체 전달](#js-08-section-46)
- [43. 전달된 함수 실행](#js-08-section-47)
- [44. `setTimeout()`](#js-08-section-48)
- [45. 타이머의 실행 시점](#js-08-section-49)
- [46. 함수 참조 전달](#js-08-section-50)
- [47. 인수가 필요한 타이머 콜백](#js-08-section-51)
- [48. `clearTimeout()`](#js-08-section-52)
- [49. `setInterval()`](#js-08-section-53)
- [50. `clearInterval()`](#js-08-section-54)
- [51. 타이머 ID](#js-08-section-55)
- [52. 재귀 함수](#js-08-section-56)
- [53. 잘못된 재귀형 타이머](#js-08-section-57)
- [54. 올바른 재귀형 타이머](#js-08-section-58)
- [55. 재귀형 `setTimeout()`과 `setInterval()`](#js-08-section-59)
- [56. 취소 가능한 재귀 타이머](#js-08-section-60)
- [57. 내 코드와 강사님 코드 비교](#js-08-section-61)
- [58. 기존 코드에서 개선 코드로 바꾼 이유](#js-08-section-62)
- [59. 실무형 예제: 지연 작업 실행기](#js-08-section-63)
- [60. 대표 오류로 이해하기](#js-08-section-64)
- [61. 자주 하는 실수](#js-08-section-65)
- [62. 핵심 요약](#js-08-section-66)
- [63. 최종 체크리스트](#js-08-section-67)
- [마무리](#js-08-section-68)
- [V3 실행 추적 카드 — 함수 등록 → 호출/예약 → 콜백 실행](#js-08-section-69)

</details>

---

<a id="js-08-section-1"></a>

## 개요

함수는 특정 작업을 하나의 이름으로 묶은 재사용 가능한 코드다.

```javascript
function hello() {
    console.log("hello world")
}
```

함수는 선언만으로 실행되지 않는다.

```javascript
hello()
```

콜백은 함수를 다른 함수에 전달해 내부 또는 나중 시점에 실행하는 구조다.

```javascript
function run(callback) {
    callback()
}
```

타이머는 콜백을 일정 시간이 지난 뒤 또는 일정 간격마다 실행하도록 예약한다.

```javascript
setTimeout(
    () => {
        console.log("1초 후 실행")
    },
    1000,
)
```

> [!IMPORTANT]
> `함수이름`은 함수 자체이고, `함수이름()`은 함수를 실행한 결과다.
>
> 이 차이를 이해해야 콜백과 타이머를 정확하게 사용할 수 있다.

---

<a id="js-08-section-2"></a>

## 핵심 개념

| 개념 | 핵심 역할 |
| --- | --- |
| 함수 선언 | 실행할 코드를 이름으로 정의 |
| 함수 호출 | 정의된 함수 실행 |
| 매개변수 | 함수가 입력값을 받는 변수 |
| 인수 | 호출할 때 전달하는 실제 값 |
| `return` | 결과 반환과 함수 종료 |
| 지역 변수 | 함수 내부에서만 접근 가능한 변수 |
| 블록 스코프 | `{}` 내부의 `let`, `const` 범위 |
| Shadowing | 안쪽 변수가 바깥의 같은 이름을 가림 |
| TDZ | `let`, `const` 선언 전 접근 불가 구간 |
| 기본 매개변수 | 인수가 없을 때 사용할 기본값 |
| 함수 표현식 | 함수를 값으로 변수에 저장 |
| 콜백 | 다른 함수에 전달되어 호출되는 함수 |
| 함수 참조 | 실행하지 않은 함수 객체 자체 |
| `setTimeout()` | 일정 시간 후 한 번 실행 예약 |
| `setInterval()` | 일정 간격으로 반복 실행 예약 |
| 타이머 ID | 예약된 타이머를 취소하는 식별값 |

---

<a id="js-08-section-3"></a>

## 학습 목표

- 함수 전달과 즉시 호출, 타이머 예약을 구분한다.
- 원본의 해당 부분을 찾아 실행 순서와 결과를 다시 확인한다.

---

<a id="js-08-section-4"></a>

## 개념에서 실제 실행까지: 함수는 호출할 때 동작하고, return은 호출자에게 값을 준다

함수 선언은 실행할 절차를 준비한다. getArea(10,20)는 width와 height에 인수를 넣고 면적을 로그로 출력하지만 return이 없으므로 호출 결과는 undefined다. getArea2는 200을 반환하여 다른 계산에 사용할 수 있다. return 자체가 화면이나 Console에 출력하는 것은 아니다.

수업의 test(noName)는 함수 참조를 전달하고 test 내부에서 fn()으로 호출한다. test2(test1())는 안쪽 함수를 지금 실행한 결과 3을 전달한다. 콜백이라는 말이 항상 비동기를 뜻하지도 않는다: test 안의 fn()은 지금 동기 실행된다. 반면 setTimeout에 준 함수는 예약 후에 실행된다.

두 원본의 기계_1초후_한번더(함수)는 setTimeout 첫 인수에서 자기 자신을 즉시 호출한다. 타이머를 기다리는 재귀가 아니라 동기 재귀로 스택이 넘칠 수 있는 오류 예제다. 원본의 console.log 덮어쓰기 실험도 다른 실습 로그에 영향을 준다. 💡 새 실습에서는 원래 Console을 변경하지 말고 별도 함수로 감싼다.

### 수업 원본에서 사용한 부분

아래는 전체 실행 파일이 아니라 **개념에 대응하는 문맥 발췌**다. 나머지 HTML·선언·등록 코드는 원본과 기존 번호형 본문에서 이어 확인한다. 

내 코드: `workspace_html/javascript/08_function.html`

```javascript
function getArea(width, height) {
                console.log(`width: ${width}, height: ${height}`)
                let area = width * height;
                console.log('면적 : ', area);
            }
            
            getArea(10, 20);
```

강사님 코드: `workspace_teacher/workspace_html/javascript/08_function.html`

```javascript
function getArea(width, height){
        console.log(`width: ${width}, height: ${height}`)
        let area = width * height
        console.log('면적: ', area)
    }
    getArea(10, 20)
```

### 직접 재현하는 최소 예제와 결과

이 예제는 **이번 리팩토링의 설명용 재구성**이다. 원본 그대로의 발췌와 구별한다. 외부 통신 없이 Console에서 실행한다. 다른 예제의 변수와 섞이지 않게 새 실행 문맥에서 실행한다.

```javascript
function printArea(w, h) { console.log(w * h); }
function getArea(w, h) { return w * h; }
console.log(printArea(10, 20));
console.log(getArea(10, 20) + 5);
function run(fn) { console.log("호출 전"); fn(); console.log("호출 후"); }
run(() => console.log("콜백"));
```

예상 출력:

```text
200
undefined
205
호출 전
콜백
호출 후
```

### 결과를 역추적하는 방법

재귀 예약은 setTimeout(() => repeat(fn), 1000)처럼 함수를 나중에 호출하는 콜백으로 감싼다. 반복 중단 상태나 timer ID도 관리해야 한다. 기본 매개변수는 undefined에 적용되고 null에는 적용되지 않는다.

출력은 아래의 확인 경로로 추적한다. return 값은 호출자에게 전달되고 자동으로 화면에 표시되지 않는다. Console 로그, DOM 변경, 저장소 변경, 서버 응답은 별개 단계다.

| 확인할 단계 | 이 예제에서 볼 것 |
| --- | --- |
| 입력 | 리터럴·현재 폼 값·이벤트 인수·응답 중 출처를 위 설명과 대조 |
| 실행 | 각 줄 또는 콜백이 지금 실행되는지, 나중에 실행되는지 구분 |
| 결과 | 위 예상 출력과 현재 값·자료형을 함께 대조 |
| 오류 | 첫 오류 줄의 입력과 직전 상태를 확인하고 뒤 로그 누락 원인 추적 |

### 단계별 복습 실습과 정답

**기본 실습:** function area(w,h){console.log(w*h)}의 호출 결과로 +5를 계산한다.

**응용·디버깅 실습:** setTimeout 안에 재귀 함수를 호출한 결과를 직접 인수로 넣은 코드를 수정한다.

**통합 확인:** 위 최소 예제를 새 문맥에서 작성하고 정상값·빈 값·경계값으로 실행한다. 원본에서 대응하는 선언·호출·콜백을 찾아 위에 나타난 차이가 무엇을 바꾸는지 설명한다. 아래 정답은 먼저 예측한 뒤 펼친다. 이 실습은 💡 설명용 보강이며 원본에 모두 완성되어 있다는 뜻은 아니다.

<details>
<summary>정답과 처리 순서 해설</summary>

1. 로그200 뒤 호출 결과undefined이므로 undefined+5는NaN이다. return w*h를 넣어야205를 얻는다.
2. setTimeout(()=>repeat(fn),1000)처럼 콜백으로 감싼다. 종료 조건도 추가한다.
3. 최소 예제의 예상 출력과 한 줄씩 대조한다. 값이 다른 경우 입력 → 형 변환 → 분기/상태 변경 → 출력 순서로 첫 차이를 찾는다. DOM·API 예제는 Console 값만 아니라 화면·Elements·Network가 서로 같은 상태를 말하는지도 점검한다.

</details>

### 복습 질문과 해설

**질문:** setTimeout(hello(),1000)는 왜 예약 전달이 아닐까?

**해설:** hello()를 현재 즉시 평가한 반환값을 첫 인수로 넘긴다. hello 자체 또는 () => hello()를 넘겨야 호출을 나중에 하도록 준비한다.

**한 번 더 확인:** 예제의 입력을 하나 바꾸고 결과를 먼저 예상한 뒤 실행한다. 정상 입력만 아니라 비어 있는 값, 경계값, 두 번 실행했을 때의 상태를 기존 실습·오류 절에서 반복 확인한다.

---

<a id="js-08-section-5"></a>

## 1. 함수 선언

```javascript
function hello() {
    console.log("hello world")
}
```

이 코드는 함수를 준비한 것이며 아직 실행되지 않는다.

---

<a id="js-08-section-6"></a>

## 2. 함수 호출

```javascript
hello()
```

출력:

```text
hello world
```

함수 이름 뒤에 괄호를 붙이면 함수 본문이 실행된다.

---

<a id="js-08-section-7"></a>

## 3. 함수 자체와 실행 결과

```javascript
console.log(hello)
console.log(hello())
```

첫 번째는 함수 객체를 출력한다.

두 번째는 함수를 실행한 뒤 반환값을 출력한다.

현재 `hello()`에는 `return`이 없으므로 실행 메시지 뒤 `undefined`가 출력될 수 있다.

---

<a id="js-08-section-8"></a>

## 4. 매개변수와 인수

```javascript
function getArea(
    width,
    height,
) {
    const area = (
        width * height
    )

    console.log(area)
}

getArea(10, 20)
```

| 구분 | 값 |
| --- | --- |
| 매개변수 | `width`, `height` |
| 인수 | `10`, `20` |

출력:

```text
200
```

---

<a id="js-08-section-9"></a>

## 5. 출력하는 함수

```javascript
function getArea(
    width,
    height,
) {
    console.log(
        width * height,
    )
}
```

호출 결과를 저장하면:

```javascript
const result = getArea(
    10,
    20,
)

console.log(result)
```

출력:

```text
200
undefined
```

함수 내부에서 출력했지만 값을 반환하지는 않았다.

---

<a id="js-08-section-10"></a>

## 6. 반환하는 함수

```javascript
function getArea(
    width,
    height,
) {
    return (
        width * height
    )
}

const result = getArea(
    10,
    20,
)

console.log(result)
```

출력:

```text
200
```

> [!IMPORTANT]
> 계산 함수는 화면에 직접 출력하기보다 결과를 반환하도록 작성하면 재사용하기 쉽다.

---

<a id="js-08-section-11"></a>

## 7. `return`의 두 역할

```text
1. 호출 위치로 값 반환
2. 현재 함수 실행 종료
```

```javascript
function example() {
    return 10

    console.log(
        "실행되지 않음",
    )
}
```

`return` 뒤의 같은 함수 블록 코드는 실행되지 않는다.

---

<a id="js-08-section-12"></a>

## 8. 덧셈 함수

```javascript
function plus(
    x,
    y,
) {
    const result = x + y

    return result
}

console.log(
    plus(2, 3),
)
```

출력:

```text
5
```

---

<a id="js-08-section-13"></a>

## 9. 중첩 함수 호출

```javascript
const result = plus(
    2,
    plus(5, 6),
)

console.log(result)
```

실행 순서:

```text
plus(5, 6)
→ 11

plus(2, 11)
→ 13
```

출력:

```text
13
```

안쪽 함수 호출이 먼저 평가된다.

---

<a id="js-08-section-14"></a>

## 10. 이전 변수에 의존한 중첩 호출

내 코드 원본:

```javascript
let result = plus(2, 3)

result = plus(
    2,
    plus(result, 6),
)
```

현재 순서에서는 `result`가 5이므로 최종 결과는 13이다.

하지만 앞 코드의 실행 결과에 의존하므로 다음처럼 직접 값을 전달하는 편이 더 명확하다.

```javascript
const result = plus(
    2,
    plus(5, 6),
)
```

---

<a id="js-08-section-15"></a>

## 11. 함수 지역 변수

```javascript
function plus(
    x,
    y,
) {
    const result = x + y

    return result
}
```

함수 내부 `result`는 함수 밖에서 직접 접근할 수 없다.

```text
ReferenceError
```

---

<a id="js-08-section-16"></a>

## 12. 같은 이름의 지역·외부 변수

```javascript
function calculate() {
    const value = 10

    return value
}

const value = 20

console.log(
    calculate(),
)

console.log(value)
```

출력:

```text
10
20
```

서로 다른 스코프의 변수다.

---

<a id="js-08-section-17"></a>

## 13. 블록 스코프

```javascript
{
    const outer = 10

    {
        const inner = 20

        console.log(outer)
        console.log(inner)
    }
}
```

안쪽 블록은 바깥 변수에 접근할 수 있다.

바깥 블록은 안쪽 변수에 직접 접근할 수 없다.

---

<a id="js-08-section-18"></a>

## 14. Shadowing

```javascript
const value = 10

{
    const value = 20

    console.log(value)
}

console.log(value)
```

출력:

```text
20
10
```

안쪽 `value`가 바깥 `value`를 일시적으로 가린다.

---

<a id="js-08-section-19"></a>

## 15. TDZ

```text
{
    console.log(value)
    const value = 20
}
```

발생 결과:

```text
ReferenceError
```

`const value`가 있는 블록에서는 선언문 실행 전까지 Temporal Dead Zone에 있다.

---

<a id="js-08-section-20"></a>

## 16. 반복문의 블록 변수

```javascript
for (
    let index = 0;
    index < 5;
    index += 1
) {
    const value = 10

    console.log(
        index,
        value,
    )
}
```

`index`와 `value`는 반복문 블록 밖에서 직접 접근할 수 없다.

---

<a id="js-08-section-21"></a>

## 17. 인수가 부족한 경우

```javascript
function plus(
    x,
    y,
) {
    console.log(y)

    return x + y
}

console.log(
    plus(2),
)
```

출력:

```text
undefined
NaN
```

두 번째 매개변수에는 `undefined`가 들어간다.

---

<a id="js-08-section-22"></a>

## 18. `undefined` 방어

원본:

```javascript
function plus(
    x,
    y,
) {
    if (y == undefined) {
        y = 0
    }

    return x + y
}
```

엄격 비교:

```javascript
if (y === undefined) {
    y = 0
}
```

더 자연스러운 방법은 기본 매개변수다.

---

<a id="js-08-section-23"></a>

## 19. 기본 매개변수

```javascript
function plus(
    x,
    y = 0,
) {
    return x + y
}

console.log(
    plus(2),
)
```

출력:

```text
2
```

---

<a id="js-08-section-24"></a>

## 20. 기본값 적용 조건

```javascript
plus(2)
// y = 0

plus(2, undefined)
// y = 0

plus(2, null)
// y = null
```

기본 매개변수는 인수가 없거나 `undefined`일 때 적용된다.

---

<a id="js-08-section-25"></a>

## 21. 중복 방어 코드

다음 함수의 내부 `if`는 중복이다.

```javascript
function plus(
    x,
    y = 0,
) {
    if (y === undefined) {
        y = 0
    }

    return x + y
}
```

개선:

```javascript
function plus(
    x,
    y = 0,
) {
    return x + y
}
```

---

<a id="js-08-section-26"></a>

## 22. 인수를 많이 전달한 경우

```javascript
function plus(
    x,
    y,
) {
    return x + y
}

console.log(
    plus(2, 3, 4),
)
```

출력:

```text
5
```

세 번째 인수는 이름 있는 매개변수에 연결되지 않는다.

---

<a id="js-08-section-27"></a>

## 23. 나머지 매개변수

추가 인수를 모두 사용하려면 rest parameter를 사용할 수 있다.

```javascript
function sum(
    ...numbers
) {
    let total = 0

    for (
        const number
        of numbers
    ) {
        total += number
    }

    return total
}

console.log(
    sum(1, 2, 3, 4),
)
```

출력:

```text
10
```

---

<a id="js-08-section-28"></a>

## 24. 익명 함수

```javascript
const noName = function () {
    console.log(
        "익명 함수",
    )
}

noName()
```

함수 자체에는 이름이 없지만 변수 `noName`이 함수 객체를 참조한다.

---

<a id="js-08-section-29"></a>

## 25. 함수 참조 복사

```javascript
const noName2 = noName

noName2()
```

`noName()`의 실행 결과를 저장한 것이 아니라 함수 자체를 다른 변수에 저장했다.

---

<a id="js-08-section-30"></a>

## 26. 함수 참조와 호출 결과 비교

```text
noName
→ 함수 객체

noName()
→ 함수 실행 결과
```

현재 함수에 `return`이 없다면 `noName()`의 결과는 `undefined`다.

---

<a id="js-08-section-31"></a>

## 27. 콜백 함수

```javascript
function runCallback(
    callback,
) {
    if (
        typeof callback
        === "function"
    ) {
        callback()
    }
}

runCallback(noName)
```

`noName` 함수 자체를 인수로 전달한다.

---

<a id="js-08-section-32"></a>

## 28. 콜백 용어

```text
noName
→ 전달된 콜백 함수

callback
→ 콜백을 받는 매개변수
```

매개변수 이름 자체가 콜백인 것이 아니라, 그 매개변수가 참조하는 함수가 콜백이다.

---

<a id="js-08-section-33"></a>

## 29. 콜백 타입 검사

```javascript
function runCallback(
    callback,
) {
    if (
        typeof callback
        !== "function"
    ) {
        console.error(
            "함수를 전달해야 합니다.",
        )

        return
    }

    callback()
}
```

함수가 아닌 값이 전달되었을 때 호출 오류를 방지한다.

---

<a id="js-08-section-34"></a>

## 30. 같은 이름의 함수 선언

```javascript
function printMessage() {
    console.log(
        "첫 번째 함수",
    )
}

function printMessage() {
    console.log(
        "두 번째 함수",
    )
}

printMessage()
```

출력:

```text
두 번째 함수
```

같은 스코프의 중복 함수 선언은 뒤 선언이 사용되는 형태로 동작한다.

> [!WARNING]
> 중복 선언은 앞 구현이 조용히 가려져 유지보수에 위험하다.

---

<a id="js-08-section-35"></a>

## 31. 함수 별칭

```javascript
const print = printMessage

print()
```

두 변수는 같은 함수 객체를 참조한다.

---

<a id="js-08-section-36"></a>

## 32. 선언 없는 전역 대입

원본 강사님 코드에는 다음 형태가 있다.

```text
x = test1()
```

Strict mode나 module에서는 다음 오류가 발생한다.

```text
ReferenceError: x is not defined
```

개선:

```javascript
const x = test1()
```

또는 재할당이 필요하면:

```javascript
let x = test1()
```

---

<a id="js-08-section-37"></a>

## 33. Console 객체 참조

```javascript
const consoleReference = console

consoleReference.log(123)
```

객체 자체를 다른 변수에 저장할 수 있다.

---

<a id="js-08-section-38"></a>

## 34. 메서드 참조

```javascript
const originalLog = (
    console.log
)

originalLog(1234)
```

함수도 값이므로 메서드 참조를 변수에 저장할 수 있다.

다만 모든 객체 메서드가 객체와 분리된 상태에서도 안전하게 호출되는 것은 아니다.

---

<a id="js-08-section-39"></a>

## 35. `console.log` 덮어쓰기

원본 실험:

```text
console.log = 3
```

이후 다음 호출은 불가능하다.

```text
console.log()
```

발생 결과:

```text
TypeError: console.log is not a function
```

---

<a id="js-08-section-40"></a>

## 36. 내장 API 덮어쓰기 위험

```javascript
const originalLog = console.log

console.log = function (
    value,
) {
    originalLog(
        "변경된 로그:",
        value,
    )
}
```

학습 실험으로는 함수가 값임을 확인할 수 있지만 실제 프로젝트에서 전역 내장 API를 변경하면 다음 문제가 생긴다.

- 다른 코드의 출력 결과 변경
- 라이브러리 디버깅 방해
- 오류 추적 어려움
- 테스트 격리 실패

---

<a id="js-08-section-41"></a>

## 37. 숫자 내림차순 함수

원본:

```javascript
function desc(
    array,
) {
    return (
        array
            .sort()
            .reverse()
    )
}
```

한 자리 숫자에서는 정상처럼 보일 수 있다.

---

<a id="js-08-section-42"></a>

## 38. 기본 `sort()` 문제

```javascript
console.log(
    [2, 10, 3].sort(),
)
```

출력:

```text
[10, 2, 3]
```

기본 `sort()`는 문자열 기준으로 비교한다.

---

<a id="js-08-section-43"></a>

## 39. 원본 배열 변경 문제

`sort()`와 `reverse()`는 인수로 받은 배열을 직접 변경한다.

```javascript
const numbers = [
    1,
    6,
    2,
]

desc(numbers)

console.log(numbers)
```

원본 순서도 바뀐다.

---

<a id="js-08-section-44"></a>

## 40. 안전한 숫자 내림차순

```javascript
function sortDescending(
    numbers,
) {
    return [
        ...numbers,
    ].sort(
        (a, b) => b - a,
    )
}

const numbers = [
    2,
    10,
    3,
]

const sorted = (
    sortDescending(numbers)
)

console.log(sorted)
console.log(numbers)
```

출력:

```text
[10, 3, 2]
[2, 10, 3]
```

---

<a id="js-08-section-45"></a>

## 41. 함수 호출 결과 전달

```javascript
function test1() {
    console.log("test1")

    return 3
}

function test2(
    value,
) {
    console.log("test2")
    console.log(value)
}

test2(
    test1(),
)
```

실행 순서:

```text
test1 실행
→ "test1" 출력
→ 3 반환
→ test2(3) 실행
```

---

<a id="js-08-section-46"></a>

## 42. 함수 자체 전달

```javascript
test2(test1)
```

`test1`을 실행하지 않고 함수 객체를 전달한다.

`test2` 내부에서 출력하면 함수 정의가 보일 수 있다.

---

<a id="js-08-section-47"></a>

## 43. 전달된 함수 실행

```javascript
function test2(
    callback,
) {
    if (
        typeof callback
        === "function"
    ) {
        callback()
    }
}

test2(test1)
```

이제 `test2`가 전달된 함수를 호출한다.

---

<a id="js-08-section-48"></a>

## 44. `setTimeout()`

```javascript
const timeoutId = setTimeout(
    function () {
        console.log(
            "1초 후 실행",
        )
    },
    1000,
)
```

두 번째 인수는 밀리초다.

```text
1000ms
→ 1초
```

---

<a id="js-08-section-49"></a>

## 45. 타이머의 실행 시점

`setTimeout(callback, 1000)`은 정확히 1초 후 실행을 보장하지 않는다.

더 정확한 의미:

```text
최소 1초가 지난 뒤
→ 이벤트 루프가 실행 가능한 시점에 콜백 실행
```

현재 실행 중인 코드나 브라우저 상태에 따라 더 늦을 수 있다.

---

<a id="js-08-section-50"></a>

## 46. 함수 참조 전달

올바른 형태:

```javascript
setTimeout(
    test1,
    1000,
)
```

함수 호출 결과를 전달하는 형태:

```javascript
setTimeout(
    test1(),
    1000,
)
```

두 번째 코드는 등록 시점에 `test1()`이 즉시 실행된다.

반환값이 함수가 아니라면 타이머 콜백으로 사용할 수 없다.

---

<a id="js-08-section-51"></a>

## 47. 인수가 필요한 타이머 콜백

```javascript
function greet(
    name,
) {
    console.log(
        `${name}님 안녕하세요.`,
    )
}

setTimeout(
    () => {
        greet("Kim")
    },
    1000,
)
```

화살표 함수로 실행 시점에 필요한 인수를 전달한다.

---

<a id="js-08-section-52"></a>

## 48. `clearTimeout()`

```javascript
const timeoutId = setTimeout(
    () => {
        console.log(
            "실행되지 않음",
        )
    },
    2000,
)

clearTimeout(timeoutId)
```

예약이 실행되기 전에 취소한다.

---

<a id="js-08-section-53"></a>

## 49. `setInterval()`

```javascript
const intervalId = setInterval(
    () => {
        console.log("반복")
    },
    1000,
)
```

일정 간격마다 콜백 실행을 예약한다.

---

<a id="js-08-section-54"></a>

## 50. `clearInterval()`

```javascript
const intervalId = setInterval(
    () => {
        console.log("반복")
    },
    1000,
)

setTimeout(
    () => {
        clearInterval(
            intervalId,
        )

        console.log(
            "반복 종료",
        )
    },
    5000,
)
```

실제 반복 횟수와 정확한 시점은 이벤트 루프 상황에 따라 달라질 수 있다.

---

<a id="js-08-section-55"></a>

## 51. 타이머 ID

| 예약 | 취소 |
| --- | --- |
| `setTimeout()` | `clearTimeout()` |
| `setInterval()` | `clearInterval()` |

예약 함수의 반환값은 실행 결과가 아니라 예약을 식별하는 ID다.

---

<a id="js-08-section-56"></a>

## 52. 재귀 함수

```javascript
function countdown(
    number,
) {
    if (number <= 0) {
        return
    }

    console.log(number)

    countdown(
        number - 1,
    )
}
```

자기 자신을 직접 호출한다.

종료 조건이 반드시 필요하다.

---

<a id="js-08-section-57"></a>

## 53. 잘못된 재귀형 타이머

원본 개념:

```text
setTimeout(
    repeat(callback),
    1000
)
```

`repeat(callback)`이 예약 전에 즉시 실행된다.

그 함수가 다시 자기 자신을 즉시 호출하면 stack overflow가 발생할 수 있다.

---

<a id="js-08-section-58"></a>

## 54. 올바른 재귀형 타이머

```javascript
function repeat(
    callback,
) {
    callback()

    setTimeout(
        () => {
            repeat(callback)
        },
        1000,
    )
}
```

현재 실행이 끝난 뒤 다음 호출을 타이머로 예약한다.

---

<a id="js-08-section-59"></a>

## 55. 재귀형 `setTimeout()`과 `setInterval()`

| 방식 | 특징 |
| --- | --- |
| `setInterval()` | 고정 간격으로 반복 예약 |
| 재귀형 `setTimeout()` | 이전 작업 완료 뒤 다음 예약 가능 |

비동기 작업 시간이 일정하지 않은 경우 재귀형 `setTimeout()`이 실행 겹침을 줄이는 데 유리할 수 있다.

---

<a id="js-08-section-60"></a>

## 56. 취소 가능한 재귀 타이머

```javascript
function createRepeater(
    callback,
    delay,
) {
    let timeoutId
    let isRunning = true

    function run() {
        if (!isRunning) {
            return
        }

        callback()

        timeoutId = setTimeout(
            run,
            delay,
        )
    }

    run()

    return function stop() {
        isRunning = false
        clearTimeout(timeoutId)
    }
}

const stop = createRepeater(
    () => {
        console.log("반복")
    },
    1000,
)

// stop()
```

---

<a id="js-08-section-61"></a>

## 57. 내 코드와 강사님 코드 비교

| 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 함수 설명 | 주석과 실행 흐름 상세 | 핵심 코드 중심 |
| 중첩 호출 | 이전 `result` 값에 의존 | 직접 값 전달 |
| 스코프 | Shadowing·TDZ 설명 상세 | 기본 블록 예제 |
| 기본값 | 중복 방어 코드 포함 | 동일 |
| 익명 함수 | 함수 참조 차이 상세 | 기본 실행 |
| 콜백 | 용어 설명 확장 | 호출 구조 중심 |
| 전역 변수 | 일부 실행식 주석 처리 | 선언 없는 `x` 대입 실행 |
| Console | 덮어쓰기 위험 메모 | 실제 덮어쓰기 실험 |
| 정렬 | 기본 문자열 정렬 사용 | 동일 |
| 타이머 | 재귀형 코드 설명 상세 | 선언과 예약 중심 |

### 57-1. 내 코드의 장점

- 함수 선언과 호출 차이를 초보자 관점에서 상세히 설명했다.
- 스코프·Shadowing·TDZ를 단계적으로 기록했다.
- 함수 참조와 실행 결과를 여러 예제로 확인했다.
- 콜백과 타이머의 실행 시점을 연결해 설명했다.

### 57-2. 내 코드의 개선점

- 이전 변수 `result`에 의존하는 중첩 호출은 실행 순서 의존성이 있다.
- `== undefined`보다 기본 매개변수 또는 엄격 비교가 적합하다.
- 내장 `console.log`를 덮어쓰면 이후 모든 예제에 영향을 준다.
- 숫자 정렬에 기본 `sort()`를 사용하면 잘못된 결과가 나올 수 있다.
- 재귀형 타이머는 함수 호출 결과가 아니라 함수 참조를 예약해야 한다.

### 57-3. 강사님 코드의 장점

- 함수 기본부터 콜백과 타이머까지 한 흐름으로 연결한다.
- 함수도 값처럼 저장·전달할 수 있음을 다양한 예제로 보여 준다.
- 실제 타이머 예약과 취소 함수를 소개한다.
- 중첩 호출의 평가 순서를 직접 확인할 수 있다.

### 57-4. 강사님 코드의 보충점

- 선언 없는 전역 대입을 피해야 한다.
- 엄격 비교를 사용해야 한다.
- 내장 API 덮어쓰기 위험을 명확히 설명할 필요가 있다.
- 숫자 정렬의 비교 함수와 원본 복사가 필요하다.
- 잘못된 재귀 타이머가 즉시 실행되는 이유를 보충해야 한다.

---

<a id="js-08-section-62"></a>

## 58. 기존 코드에서 개선 코드로 바꾼 이유

### 58-1. 출력 함수에서 반환 함수로

기존:

```javascript
function getArea(
    width,
    height,
) {
    console.log(
        width * height,
    )
}
```

개선:

```javascript
function getArea(
    width,
    height,
) {
    return (
        width * height
    )
}
```

### 58-2. 느슨한 비교 제거

기존:

```javascript
typeof callback == "function"
```

개선:

```javascript
typeof callback === "function"
```

### 58-3. 정렬 원본 유지

기존:

```javascript
array.sort().reverse()
```

개선:

```javascript
[
    ...array,
].sort(
    (a, b) => b - a,
)
```

### 58-4. 타이머 콜백 참조

기존:

```text
setTimeout(
    callback(),
    1000
)
```

개선:

```javascript
setTimeout(
    callback,
    1000,
)
```

---

<a id="js-08-section-63"></a>

## 59. 실무형 예제: 지연 작업 실행기

```javascript
function runTask(
    task,
    delay,
    onComplete,
) {
    if (
        typeof task
        !== "function"
        || typeof onComplete
        !== "function"
    ) {
        throw new TypeError(
            "task와 onComplete는 함수여야 합니다.",
        )
    }

    return setTimeout(
        () => {
            const result = task()

            onComplete(result)
        },
        delay,
    )
}

const taskId = runTask(
    () => {
        return 100 + 200
    },
    1000,
    result => {
        console.log(
            `작업 결과: ${result}`,
        )
    },
)

// 실행 전에 취소할 때:
// clearTimeout(taskId)
```

### 59-1. 실행 결과

약 1초 이후:

```text
작업 결과: 300
```

### 59-2. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| 함수 매개변수 | 실행할 작업과 완료 처리 전달 |
| `typeof` | 콜백 자료형 검사 |
| `throw` | 잘못된 사용을 즉시 알림 |
| `return setTimeout()` | 예약 ID 반환 |
| `task()` | 실제 작업 실행 |
| `onComplete(result)` | 결과를 후속 콜백에 전달 |
| `clearTimeout()` | 필요할 때 예약 취소 |

---

<a id="js-08-section-64"></a>

## 60. 대표 오류로 이해하기

### 60-1. 함수 이름만 작성하고 실행 기대

괄호가 없으면 함수가 실행되지 않는다.

### 60-2. 반환값 없는 함수 결과 사용

`undefined`가 저장된다.

### 60-3. 지역 변수 외부 접근

`ReferenceError`가 발생한다.

<a id="index-section-85"></a>

### 60-4. `const` 선언 전 접근

TDZ로 `ReferenceError`가 발생한다.

### 60-5. 함수를 호출한 결과를 콜백으로 전달

등록 시점에 즉시 실행된다.

### 60-6. 숫자를 함수처럼 호출

```text
TypeError: value is not a function
```

### 60-7. 종료 조건 없는 직접 재귀

`RangeError: Maximum call stack size exceeded`가 발생할 수 있다.

### 60-8. 타이머 ID를 저장하지 않음

나중에 예약을 취소하기 어렵다.

---

<a id="js-08-section-65"></a>

## 61. 자주 하는 실수

### 61-1. 함수 선언만 하고 호출하지 않음

함수 본문은 실행되지 않는다.

<a id="index-section-92"></a>

### 61-2. `console.log()`와 `return`을 같은 역할로 이해

출력과 값 반환은 다르다.

### 61-3. 중첩 호출의 바깥 함수부터 실행된다고 생각

인수의 안쪽 호출이 먼저 평가된다.

### 61-4. 기본 매개변수와 `undefined` 방어를 중복 작성

하나의 방식으로 단순화할 수 있다.

### 61-5. 함수 참조에 괄호를 붙임

콜백 전달 전에 즉시 실행된다.

### 61-6. 같은 이름의 함수를 여러 번 선언

앞 구현이 가려진다.

### 61-7. 선언 키워드 없이 반환값 저장

전역 오염 또는 `ReferenceError`가 발생한다.

### 61-8. 내장 API를 직접 덮어쓰기

다른 코드 전체에 영향을 준다.

<a id="index-section-99"></a>

### 61-9. 숫자 배열에 기본 `sort()` 사용

문자열 기준 정렬이 된다.

### 61-10. 타이머 지연 시간을 정확한 실행 시각으로 생각

이벤트 루프 상태에 따라 늦어질 수 있다.

---

<a id="js-08-section-66"></a>

## 62. 핵심 요약

```text
function name() {}
→ 함수 선언

name()
→ 함수 호출

name
→ 함수 객체
```

```text
매개변수
→ 함수 정의에서 값 받기

인수
→ 호출할 때 실제 값 전달

return
→ 값 반환 + 함수 종료
```

```text
함수 표현식
→ 함수를 변수에 저장

콜백
→ 다른 함수에 전달된 함수

typeof fn === "function"
→ 함수 여부 검사
```

```text
setTimeout()
→ 일정 시간 후 한 번

setInterval()
→ 일정 간격 반복

clearTimeout()
clearInterval()
→ 예약 취소
```

---

<a id="js-08-section-67"></a>

## 63. 최종 체크리스트

- [ ] 함수 선언과 호출을 구분할 수 있는가?
- [ ] 함수 자체와 실행 결과를 구분할 수 있는가?
- [ ] 매개변수와 인수를 설명할 수 있는가?
- [ ] `return`의 두 역할을 이해했는가?
- [ ] 반환값을 변수에 저장할 수 있는가?
- [ ] 중첩 호출의 실행 순서를 추적할 수 있는가?
- [ ] 함수·블록 스코프를 구분할 수 있는가?
- [ ] Shadowing과 TDZ를 설명할 수 있는가?
- [ ] 기본 매개변수를 사용할 수 있는가?
- [ ] 추가 인수를 rest parameter로 받을 수 있는가?
- [ ] 익명 함수를 변수에 저장할 수 있는가?
- [ ] 함수 참조를 다른 변수에 복사할 수 있는가?
- [ ] 콜백 함수의 타입을 검사할 수 있는가?
- [ ] 중복 함수 선언을 피할 수 있는가?
- [ ] 선언 없는 전역 대입을 사용하지 않는가?
- [ ] 내장 API를 덮어쓰지 않는가?
- [ ] 숫자 배열을 원본 변경 없이 정렬할 수 있는가?
- [ ] `setTimeout()`에 함수 참조를 전달할 수 있는가?
- [ ] 타이머 ID를 이용해 예약을 취소할 수 있는가?
- [ ] `setInterval()`과 재귀형 `setTimeout()`을 구분할 수 있는가?
- [ ] 재귀 함수에 종료 조건을 작성할 수 있는가?

---

<a id="js-08-section-68"></a>

## 마무리

함수의 핵심은 코드를 이름으로 묶는 것에서 끝나지 않는다.

```text
입력값을 매개변수로 받고
    ↓
결과를 return으로 반환하고
    ↓
스코프를 작게 유지하고
    ↓
함수를 값처럼 전달해 콜백으로 사용하고
    ↓
필요한 시점에 안전하게 실행을 예약하는 것
```

이 흐름을 이해하면 이후 화살표 함수, 이벤트 처리, 비동기 작업을 더 자연스럽게 학습할 수 있다.
<a id="js-08-section-69"></a>

## V3 실행 추적 카드 — 함수 등록 → 호출/예약 → 콜백 실행

함수 정의와 호출은 다르다. `setTimeout(callback, delay)`는 함수를 즉시 실행하지 않고 최소 지연 뒤 실행할 작업으로 등록하며 현재 호출 스택이 끝난 뒤 처리된다.

`console.log("A"); setTimeout(()=>console.log("B"),0); console.log("C");`는 `A`, `C`, `B` 순이다.

**원본 연결:** 내 코드와 강사님 코드의 `workspace_html/javascript/08_function.html`에서 실제 사용 위치와 차이를 확인한다.
