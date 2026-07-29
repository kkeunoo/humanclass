# JavaScript 함수와 콜백·타이머

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `08_JavaScript_함수와_콜백_타이머.md` |
| 분류 | `03_JavaScript` |
| 권장 선수 학습 | `07_JavaScript_Date와_날짜처리.md` |
| 다음 학습 | `09_JavaScript_스코프와_객체활용.md` |
| 원본 기준 | `workspace_me/workspace/workspace_html/javascript/08_function.html`, `workspace_teacher/workspace_teacher/workspace_html/javascript/08_function.html` |
| 핵심 범위 | 함수 선언과 호출, 매개변수와 인수, 반환값, 중첩 호출, 지역·블록 스코프, shadowing, 기본 매개변수, 익명 함수, 함수 참조, 콜백, 함수 중복 선언, `typeof`, Console 메서드 참조, 배열 정렬 함수, `setTimeout()`, `clearTimeout()`, `setInterval()`, `clearInterval()`, 재귀 호출 |
| 프로젝트 연결 | 공통 로직 분리, 계산 함수, 이벤트 콜백, 비동기 예약, 반복 타이머, 디바운스·지연 실행의 기초, 데이터 정렬 |

> 이 문서는 내 코드와 강사님 코드의 `08_function.html`을 직접 비교해 작성했습니다. 두 원본은 함수 선언부터 콜백과 타이머까지 거의 같은 순서로 진행합니다. 내 코드는 설명을 크게 확장하고 일부 실행식을 주석으로 바꾸었으며, 강사님 코드는 함수 실행 결과를 전역 변수 `x`에 대입하는 코드까지 실제로 실행합니다. 원본의 부정확한 용어, 느슨한 비교, Console 덮어쓰기, 문자열 기반 숫자 정렬, 잘못 작성된 재귀형 `setTimeout()` 표현은 그대로 기록한 뒤 올바른 실행 원리를 설명합니다.

---

# 학습 목표

- 함수 선언과 호출을 구분한다.
- 매개변수와 전달 인수의 역할을 설명한다.
- `return`이 함수 실행을 종료하고 값을 반환한다는 점을 이해한다.
- 함수 호출 결과를 변수에 저장한다.
- 함수 호출을 다른 함수의 인수로 전달한다.
- 함수 참조와 함수 호출 결과의 차이를 구분한다.
- 함수·블록 스코프와 shadowing을 이해한다.
- 선언 전 접근에서 발생할 수 있는 TDZ를 설명한다.
- 인수를 적게 또는 많이 전달했을 때의 동작을 이해한다.
- 기본 매개변수를 작성한다.
- 익명 함수를 변수에 저장하고 다른 변수로 전달한다.
- 콜백 함수를 안전하게 실행한다.
- 같은 이름의 함수 선언이 중복될 때 실제 선택되는 함수를 이해한다.
- 함수도 값처럼 변수에 저장할 수 있음을 이해한다.
- 내장 객체 메서드를 덮어쓰는 위험을 설명한다.
- 배열 정렬 함수가 원본을 변경하며 기본 정렬이 문자열 기준임을 이해한다.
- `setTimeout()`과 `setInterval()`의 예약 ID를 취소에 사용한다.
- 재귀 호출과 콜백 예약을 혼동하지 않는다.
- 원본 코드가 실제로 어떤 순서로 실행되는지 추적한다.

---

# 1. 함수란?

함수는 특정 작업을 수행하는 코드를 하나의 이름으로 묶은 것입니다.

```js
function hello() {
  console.log("hello world")
}
```

이 코드는 함수를 **선언**한 것입니다.

선언만으로 함수 본문이 실행되지는 않습니다.

```js
hello()
```

괄호를 붙여 호출해야 실행됩니다.

내 코드 주석:

```text
function(함수)는 준비해놓고 부르지 않으면 나오지 않음
```

학습 관점에서 적절한 설명입니다.

---

# 2. 원본 문서 구조

두 원본 모두 `<head>` 안의 내부 `<script>`에서 모든 예제를 연속 실행합니다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
  >
  <title>Document</title>
  <script>
    // 함수 실습
  </script>
</head>
<body>
</body>
</html>
```

강사님 문서에는 `<body>`가 있지만 내 코드의 확인 범위는 `<head>` 내부 실습이 중심입니다.

---

# 3. 함수 선언과 함수 호출

선언:

```js
function hello() {
  console.log("hello world")
}
```

호출:

```js
hello()
```

함수 이름만 작성하면 함수 객체 자체를 가리킵니다.

```js
hello
```

괄호를 붙이면 실행 결과를 얻습니다.

```js
hello()
```

이 차이는 뒤의 콜백과 `test1`, `test2` 예제에서 다시 등장합니다.

---

# 4. 매개변수와 인수

공통 원본:

```js
function getArea(width, height) {
  const area = width * height
  console.log("면적 :", area)
}

getArea(10, 20)
```

구분:

```text
width, height
→ 매개변수(parameter)

10, 20
→ 전달 인수(argument)
```

호출 시 전달한 값이 함수 내부 매개변수에 순서대로 들어갑니다.

---

# 5. 값을 출력하는 함수

`getArea()`는 계산 결과를 Console에 출력합니다.

```js
function getArea(width, height) {
  const area = width * height
  console.log(area)
}
```

호출 결과 자체를 변수에 저장하면:

```js
const result =
  getArea(10, 20)
```

명시적인 return이 없으므로 `result`는 undefined입니다.

---

# 6. 값을 반환하는 함수

공통 원본:

```js
function getArea2(width, height) {
  const area = width * height
  return area
}
```

호출:

```js
let result =
  getArea2(10, 20)

console.log(result)
```

결과:

```text
200
```

내 코드 설명:

```text
200을 리턴했으니 아래 getArea2가 200이라는 값을 가지게 됨
```

정확하게는 함수 `getArea2` 자체가 200으로 변하는 것이 아니라, **이번 함수 호출 표현식 `getArea2(10, 20)`의 결과가 200**입니다.

---

# 7. Return의 역할

`return`은 두 가지 역할을 합니다.

```text
1. 호출한 위치로 값을 돌려준다.
2. 현재 함수 실행을 즉시 종료한다.
```

```js
function example() {
  return 10
  console.log("실행되지 않음")
}
```

return 뒤의 같은 함수 블록 코드는 실행되지 않습니다.

원본은 반환값 중심으로 학습합니다.

---

# 8. Plus 함수

공통 원본:

```js
function plus(x, y) {
  console.log("x :", x)
  console.log("y :", y)

  const z = x + y
  return z
}
```

호출:

```js
result = plus(2, 3)
console.log(result)
```

결과:

```text
5
```

함수 안의 `z`는 함수 실행이 끝난 뒤 바깥에서 직접 접근할 수 없는 지역 변수입니다.

---

# 9. 중첩 함수 호출

강사님 코드:

```js
result =
  plus(2, plus(5, 6))
```

실행 순서:

```text
plus(5, 6)
→ 11

plus(2, 11)
→ 13
```

결과:

```text
13
```

인수에 들어간 함수 호출이 먼저 평가됩니다.

---

# 10. 내 코드의 중첩 호출 차이

내 코드:

```js
result =
  plus(2, plus(result, 6))
```

직전에 `result`는 `plus(2, 3)`의 결과인 5입니다.

따라서:

```text
plus(result, 6)
→ plus(5, 6)
→ 11

plus(2, 11)
→ 13
```

강사님과 최종 결과는 같지만 내 코드는 기존 변수 `result`에 의존합니다.

이전 코드 순서가 바뀌면 결과도 달라질 수 있습니다.

---

# 11. 함수 지역 변수

공통 원본:

```js
function plus(x, y) {
  const z = x + y
  return z
}

const z = plus(2, 3)
```

함수 내부의 `z`와 함수 밖의 `z`는 서로 다른 스코프에 있습니다.

따라서 같은 이름을 사용할 수 있습니다.

내 설명의 핵심:

```text
함수 안 const는 함수 안에서만 정의되는 지역 변수
```

맞는 설명입니다.

---

# 12. 블록 스코프

공통 원본:

```js
{
  const a = 10

  {
    console.log("a", a)

    const b = 20
    console.log("b", b)
  }

  // console.log(b)
}
```

안쪽 블록은 바깥 블록의 `a`에 접근할 수 있습니다.

바깥 블록은 안쪽 블록에서 선언한 `b`에 접근할 수 없습니다.

```text
상위 → 하위 접근 가능
하위 선언값 → 상위에서 직접 접근 불가
```

정확하게는 lexical scope 규칙에 따라 안쪽 스코프가 바깥 스코프를 탐색합니다.

---

# 13. Shadowing

내 코드의 상세 주석에는 안쪽에 같은 이름의 `a`를 선언하는 실험이 있습니다.

```js
{
  const a = 10

  {
    const a = 20
    console.log(a)
  }
}
```

안쪽 `a`가 바깥 `a`를 가립니다.

이를 shadowing이라고 합니다.

안쪽 블록이 끝나면 바깥 `a`는 다시 정상적으로 접근됩니다.

---

# 14. TDZ와 선언 전 접근

내 코드에서 설명한 형태:

```js
{
  const a = 10

  {
    console.log(a)
    const a = 20
  }
}
```

안쪽 블록에 `const a` 선언이 존재하면 해당 블록의 `a`는 블록 시작부터 그 선언에 연결됩니다.

하지만 선언문 실행 전에는 Temporal Dead Zone에 있어 접근 시 ReferenceError가 발생합니다.

바깥 `a`로 자동 대체되지 않습니다.

---

# 15. For문의 블록 변수

공통 원본:

```js
for (let i = 0; i < 5; i++) {
  let a = 10
}

for (let i = 0; i < 5; i++) {
  let i = 10
}
```

서로 다른 for문의 `i`는 각 반복문 블록에 속하므로 다시 선언할 수 있습니다.

두 번째 반복문의 내부:

```js
let i = 10
```

은 for 헤더의 `i`와 같은 블록에서 다시 선언하는 것처럼 보이지만, for 본문의 블록은 별도의 중첩 스코프이므로 문법적으로 가능합니다.

본문의 `i`가 헤더 `i`를 가립니다.

---

# 16. 인수가 부족한 경우

공통 원본:

```js
function plus2(x, y) {
  if (y == undefined) {
    y = 0
  }

  return x + y
}

let a = plus2(2)
```

두 번째 인수가 없으므로 `y`는 undefined입니다.

방어 코드가 0으로 바꾸어 결과는 2가 됩니다.

---

# 17. Undefined 비교 개선

원본:

```js
if (y == undefined)
```

느슨한 비교는 `null`도 같은 조건으로 취급할 수 있습니다.

정확히 undefined만 검사하려면:

```js
if (y === undefined)
```

다만 이 문제에는 기본 매개변수가 더 자연스럽습니다.

---

# 18. 기본 매개변수

공통 원본:

```js
function plus3(x, y = 0) {
  return x + y
}
```

호출:

```js
plus3(2)
```

`y`에 전달값이 없거나 undefined가 명시적으로 전달되면 기본값 0을 사용합니다.

```js
plus3(2, undefined)
// 2
```

null은 기본값을 사용하지 않습니다.

```js
plus3(2, null)
// 2 + null
// 숫자 연산에서 2
```

---

# 19. 중복 방어 코드

원본 `plus3()`:

```js
function plus3(x, y = 0) {
  if (y == undefined) {
    y = 0
  }

  return x + y
}
```

기본 매개변수 `y = 0`이 이미 undefined를 처리합니다.

내부의 `if`는 현재 목적에서는 중복입니다.

간결한 형태:

```js
function plus3(x, y = 0) {
  return x + y
}
```

---

# 20. 인수를 많이 전달한 경우

공통 원본:

```js
a = plus3(2, 3, 4)
```

함수의 매개변수는 `x`, `y` 두 개입니다.

대응:

```text
x → 2
y → 3
4 → 이름 있는 매개변수로 받지 않음
```

오류가 발생하지 않으며 결과는 5입니다.

추가 인수는 `arguments`나 rest parameter로 받을 수 있지만 원본 범위를 넘어서는 확장 개념입니다.

---

# 21. 내 코드의 추가 출력

강사님 코드는:

```js
a = plus3(2, 3, 4)
```

뒤에 결과 출력이 없습니다.

내 코드:

```js
a = plus3(2, 3, 4)
console.log(a)
```

추가 인수가 무시되고 5가 반환되는 것을 실제로 확인합니다.

---

# 22. 익명 함수

공통 원본:

```js
let noName = function() {
  console.log("익명 함수")
}
```

함수 표현식 오른쪽의 함수에는 별도 이름이 없습니다.

변수 `noName`이 함수 객체를 참조합니다.

호출:

```js
noName()
```

---

# 23. 함수 참조 복사

공통 원본:

```js
let noName2 = noName

noName2()
```

함수 실행 결과를 저장한 것이 아닙니다.

함수 객체의 참조를 다른 변수에 저장합니다.

```text
noName
→ 함수 자체

noName()
→ 함수 실행 결과
```

현재 익명 함수에는 return이 없으므로 `noName()`의 결과는 undefined입니다.

---

# 24. 콜백 함수

공통 원본:

```js
function test(fn) {
  console.log(typeof fn)

  if (typeof fn == "function") {
    fn()
  }
}

test(noName)
```

`noName` 함수 자체를 `test`의 인수로 전달합니다.

`test` 내부에서 나중에 호출되는 `fn`을 콜백으로 볼 수 있습니다.

---

# 25. 콜백 용어 검토

내 코드 주석:

```text
fn이 noName 함수를 인자로 받았는데,
이럴 때 fn을 콜백함수라고 부른다.
```

조금 더 정확한 구분:

```text
noName
→ 전달된 콜백 함수

fn
→ 그 콜백을 받는 매개변수
```

`fn`이 참조하는 함수가 callback입니다.

---

# 26. Typeof Function

```js
typeof noName
```

결과:

```text
function
```

함수는 객체처럼 값으로 전달할 수 있지만 `typeof` 결과는 `"function"`입니다.

비교 개선:

```js
typeof fn === "function"
```

---

# 27. 같은 이름의 함수 선언

공통 원본:

```js
function print() {
  console.log("첫번째 print 실행")
}

function print() {
  console.log("두번째 print 실행")
}

print()
```

같은 스코프의 함수 선언은 호이스팅 과정에서 뒤 선언이 앞 선언을 덮어쓴 것처럼 동작합니다.

실행 결과:

```text
두번째 print 실행
```

강사님 첫 문구는 `"print 실행"`, 내 코드는 `"첫번째 print 실행"`입니다.

최종 실행되는 두 번째 함수는 동일한 의미입니다.

---

# 28. 함수 중복 선언 주의

중복 선언은 실행되더라도 유지보수에 위험합니다.

- 앞 함수가 조용히 가려짐
- 어떤 구현이 실행되는지 찾기 어려움
- 파일 병합 시 오류 발견이 어려움

함수 이름은 중복되지 않게 관리합니다.

---

# 29. 함수 자체 출력

공통 원본:

```js
console.log(print)
```

함수 객체 자체를 출력합니다.

브라우저 Console에서는 함수 정의 형태가 보일 수 있습니다.

```js
console.log(print())
```

는 함수를 먼저 실행하고 그 반환값을 출력합니다.

현재 `print()`는 return이 없으므로 실행 메시지 뒤 undefined가 출력될 수 있습니다.

---

# 30. 함수 별칭

공통 원본:

```js
let p = print
p()
```

`p`도 같은 함수 객체를 참조합니다.

따라서 `p()`는 두 번째 `print()` 구현을 실행합니다.

함수는 숫자나 문자열처럼 변수에 저장하고 전달할 수 있는 값입니다.

---

# 31. Console 객체 참조

공통 원본:

```js
let c = console
c.log(123)
```

`c`는 Console 객체를 참조합니다.

```js
let c1 = console.log
c1(1234)
```

`c1`은 당시의 `console.log` 함수 참조를 저장합니다.

현대 브라우저에서는 호출될 수 있지만, 객체 메서드를 분리하면 `this` 연결 문제가 생기는 API도 있으므로 일반화하지 않습니다.

---

# 32. Console Log 덮어쓰기

공통 원본:

```js
console.log = 3
```

이제 `console.log`는 함수가 아니라 숫자입니다.

```js
console.log()
```

를 호출하면 TypeError가 발생합니다.

원본에서는 해당 호출을 주석 처리해 즉시 오류를 피합니다.

---

# 33. Console Log 복구형 함수

공통 원본:

```js
console.log = function(x) {
  c1("이거 해킹된거임")
  c1(x)
}

console.log(123)
```

앞서 저장한 원본 함수 참조 `c1`을 사용해 새 `console.log` 구현 내부에서도 출력합니다.

결과:

```text
이거 해킹된거임
123
```

---

# 34. 내장 메서드 덮어쓰기 위험

이 시점 이후 모든 `console.log()`는 원래 동작이 아니라 새 함수로 실행됩니다.

따라서 이후 예제 출력에는 매번 `"이거 해킹된거임"`이 먼저 붙습니다.

학습 실험으로는 의미가 있지만 실제 프로젝트에서 전역 내장 API를 덮어쓰면 디버깅과 라이브러리 동작을 망가뜨릴 수 있습니다.

---

# 35. Desc 함수

공통 원본:

```js
function desc(arr) {
  return arr.sort().reverse()
}

a = [1, 6, 2, 9, 3, 4]

console.log(desc(a))
```

한 자리 숫자 배열에서는:

```text
[9, 6, 4, 3, 2, 1]
```

처럼 보입니다.

---

# 36. Desc 함수의 두 문제

첫째, 기본 `sort()`는 문자열 기준입니다.

```js
desc([2, 10, 3])
```

은 숫자 내림차순을 보장하지 않습니다.

둘째, `sort()`와 `reverse()`는 인수로 받은 원본 배열을 직접 변경합니다.

개선:

```js
function desc(numbers) {
  return [...numbers]
    .sort((a, b) => b - a)
}
```

---

# 37. Test1 반환값

공통 원본:

```js
function test1() {
  console.log("test1")
  return 3
}
```

호출:

```js
test1()
```

실행 흐름:

```text
"test1" 출력
3 반환
```

---

# 38. Test2

공통 원본:

```js
function test2(a) {
  console.log("test2")
  console.log(a)
}
```

전달받은 값을 출력합니다.

`a`가 숫자일 수도 있고 함수 객체일 수도 있습니다.

---

# 39. 함수 호출 결과 전달

공통 원본:

```js
test2(test1())
```

실행 순서:

```text
1. test1 실행
2. "test1" 출력
3. 3 반환
4. test2(3) 실행
5. "test2"와 3 출력
```

내 코드 주석은 이를 `x = test1() → test2(x)` 형태로 설명합니다.

---

# 40. 함수 자체 전달

공통 원본:

```js
test2(test1)
```

`test1`을 실행하지 않고 함수 객체 자체를 전달합니다.

`test2`는 함수 정의를 출력합니다.

`test2` 내부에서 `a()`를 호출하지 않으므로 `test1` 본문은 실행되지 않습니다.

---

# 41. 강사님 코드의 전역 X

강사님 원본에는 다음 코드가 실제로 실행됩니다.

```js
x = test1()
test2(x)

x = test1
test2(x)
```

`x`를 `let`, `const`, `var` 없이 대입합니다.

일반 script의 느슨한 모드에서는 전역 객체 속성이 만들어질 수 있습니다.

strict mode에서는 ReferenceError가 발생합니다.

내 코드는 이 대응 설명을 주석으로만 작성하고 실제 `x = ...` 코드는 실행하지 않습니다.

---

# 42. 함수와 호출 결과 비교

| 표현 | 의미 |
| --- | --- |
| `test1` | 함수 객체 자체 |
| `test1()` | 함수 실행 후 반환값 3 |
| `test2(test1)` | 함수를 값으로 전달 |
| `test2(test1())` | 실행 결과 3을 전달 |

콜백을 전달할 때 괄호를 실수로 붙이면 예약 시점이 아니라 즉시 실행될 수 있습니다.

---

# 43. SetTimeout 기본

공통 원본:

```js
let yahoo = function() {
  console.log("야호")
}

setTimeout(yahoo, 3000)
```

`yahoo` 함수 자체를 전달합니다.

약 3000ms 이후 실행하도록 예약합니다.

정확히 3초에 실행된다고 보장하는 것이 아니라 최소 지연 시간이 지난 뒤 이벤트 루프 상황에 따라 실행됩니다.

---

# 44. 익명 콜백 SetTimeout

공통 원본:

```js
setTimeout(
  function() {
    console.log("야호")
  },
  4000
)
```

별도 변수 없이 익명 함수를 콜백으로 전달합니다.

첫 예제와 콜백 형태만 다릅니다.

---

# 45. SetTimeout 반환값

공통 원본:

```js
let idx = setTimeout(
  function() {
    console.log("야호!!!!!!!!!!")
  },
  1000
)
```

브라우저에서 반환값은 타이머를 식별하는 숫자형 ID로 사용됩니다.

원본 주석:

```text
setTimeout의 return은 예약번호
```

학습 용도로 적절한 설명입니다.

---

# 46. ClearTimeout

공통 원본:

```js
clearTimeout(idx)
```

앞서 예약한 1초 후 콜백을 실행 전에 취소합니다.

따라서 `"야호!!!!!!!!!!"`은 정상적으로 취소되면 출력되지 않습니다.

이미 실행된 타이머를 되돌리는 기능은 아닙니다.

---

# 47. RC 함수

공통 원본:

```js
function rc(cb) {
  cb()
  setTimeout(cb, 1000)
}
```

호출한다면:

```text
콜백 즉시 한 번 실행
1초 뒤 같은 콜백 한 번 더 실행 예약
```

이 함수는 스스로를 다시 호출하지 않으므로 무한 반복 재귀는 아닙니다.

원본에서는 `rc()`를 실제 호출하지 않습니다.

---

# 48. 재귀 호출이란?

재귀 호출은 함수가 자신의 실행 과정에서 자기 자신을 다시 호출하는 구조입니다.

```js
function countdown(number) {
  if (number <= 0) {
    return
  }

  console.log(number)
  countdown(number - 1)
}
```

반드시 종료 조건이 필요합니다.

종료 조건이 없으면 call stack이 계속 쌓여 RangeError가 발생할 수 있습니다.

---

# 49. 원본의 재귀형 타이머 함수

공통 원본:

```js
function 기계_1초후_한번더(함수) {
  함수()

  setTimeout(
    기계_1초후_한번더(함수),
    1000
  )
}
```

원본에서는 이 함수를 선언만 하고 호출하지 않으므로 즉시 오류가 발생하지 않습니다.

하지만 실제 호출하면 문제가 생깁니다.

---

# 50. 잘못된 SetTimeout 인수

```js
setTimeout(
  기계_1초후_한번더(함수),
  1000
)
```

`setTimeout`에 함수 자체를 전달하지 않고 함수 호출 결과를 전달합니다.

`기계_1초후_한번더(함수)`가 즉시 실행되고, 그 안에서 다시 같은 함수를 즉시 호출합니다.

지연 예약 전에 재귀가 계속되어 stack overflow가 발생할 수 있습니다.

---

# 51. 올바른 재귀형 타이머

```js
function repeatAfterOneSecond(callback) {
  callback()

  setTimeout(
    function() {
      repeatAfterOneSecond(callback)
    },
    1000
  )
}
```

화살표 함수:

```js
function repeatAfterOneSecond(callback) {
  callback()

  setTimeout(
    () => repeatAfterOneSecond(callback),
    1000
  )
}
```

종료 기능이 필요하면 타이머 ID 또는 외부 상태를 관리해야 합니다.

---

# 52. SetInterval 기본

공통 원본:

```js
let idx2 = setInterval(
  function() {
    console.log("인터발")
  },
  1000 * 2
)
```

약 2초 간격으로 콜백 실행을 반복 예약합니다.

`setInterval()`도 식별 ID를 반환합니다.

---

# 53. ClearInterval

공통 원본:

```js
setTimeout(
  function() {
    clearInterval(idx2)
  },
  1000 * 10
)
```

약 10초 후 반복 타이머를 취소합니다.

대략 2초, 4초, 6초, 8초 부근에서 실행될 수 있지만 실제 횟수와 시각은 이벤트 루프 지연에 따라 달라질 수 있습니다.

10초 타이머와 10초 시점 interval 실행의 순서는 환경 상황에 따라 단순 고정값으로 단정하지 않습니다.

---

# 54. 타이머와 Console 덮어쓰기

원본에서는 타이머 예약 전에 `console.log`를 새 함수로 덮어씁니다.

따라서 나중에 실행되는 타이머 콜백의:

```js
console.log("야호")
console.log("인터발")
```

도 변경된 Console 함수로 실행됩니다.

실제 출력은 각 메시지 앞에 `"이거 해킹된거임"`이 추가됩니다.

이것은 원본 실행 순서를 분석할 때 중요한 영향입니다.

---

# 55. 타이머는 코드 실행을 멈추지 않음

```js
setTimeout(callback, 3000)
```

은 3초 동안 JavaScript 전체를 멈추는 문법이 아닙니다.

콜백을 예약하고 다음 코드를 계속 진행합니다.

따라서 원본에서는 여러 timeout과 interval이 거의 연속으로 예약됩니다.

---

# 56. My Code 분석

## 56.1 장점

- 함수는 선언만으로 실행되지 않는다는 설명을 추가했다.
- `return` 결과가 호출 표현식의 값이 된다는 흐름을 설명했다.
- 함수 내부 지역 변수와 외부 변수의 같은 이름 사용을 설명했다.
- block scope와 shadowing, 선언 전 접근 오류를 상세히 주석으로 기록했다.
- 기본 매개변수와 인수 개수 차이를 자세히 설명했다.
- 추가 인수 호출 결과도 Console로 확인했다.
- 익명 함수와 일반 함수 선언의 대응 형태를 주석으로 비교했다.
- 함수 자체와 함수 호출 결과의 차이를 상세히 설명했다.
- Console 메서드를 숫자로 바꾸었을 때 호출할 수 없음을 기록했다.
- `setTimeout()`의 지연 단위와 예약 취소를 설명했다.
- `setInterval()`을 10초 후 중단하는 이유를 상세히 설명했다.
- 강사님 코드의 전역 `x` 대입을 실제 실행하지 않고 설명 주석으로만 남겼다.

## 56.2 개선점

- `getArea2가 200이라는 값을 가진다`는 설명은 함수 자체와 호출 결과를 혼동할 수 있다.
- callback은 `fn` 매개변수 자체라기보다 `fn`이 참조하는 전달 함수다.
- `typeof fn == "function"`에 느슨한 비교를 사용한다.
- 기본 매개변수 뒤의 undefined 방어 if가 중복이다.
- 같은 이름 함수 중복 선언을 일반적인 덮어쓰기처럼만 설명하면 호이스팅 맥락이 빠진다.
- 전역 `console.log`를 덮어써 이후 모든 예제 출력에 영향을 준다.
- 분리한 `console.log` 메서드가 모든 객체 메서드에서 안전하다고 일반화할 수 없다.
- `desc()`가 기본 문자열 정렬을 사용하며 원본 배열도 변경한다.
- 재귀형 `setTimeout()` 코드가 함수 참조가 아닌 즉시 호출 결과를 전달한다.
- 실제로 재귀 함수를 호출하면 지연 전에 stack overflow가 발생할 수 있다.
- `setTimeout()`과 `setInterval()`을 정확한 실행 시각으로 해석하면 안 된다.
- 많은 서로 다른 개념이 한 파일에서 연속 실행되어 Console 결과 추적이 어렵다.
- 문서 제목과 언어가 학습 내용에 맞지 않는다.

---

# 57. Teacher Code 분석

## 57.1 장점

- 함수 선언, 호출, 매개변수, 반환값을 순서대로 학습한다.
- 중첩 함수 호출의 평가 순서를 보여 준다.
- 함수와 블록 스코프를 예제로 확인한다.
- 인수가 부족하거나 많아도 즉시 오류가 나지 않는 동작을 보여 준다.
- 기본 매개변수를 소개한다.
- 익명 함수를 변수에 저장하고 다른 변수로 복사한다.
- 함수를 인수로 전달해 콜백을 실행한다.
- 같은 이름 함수 선언의 실제 선택 결과를 보여 준다.
- 함수 객체와 실행 결과를 구분한다.
- Console 객체와 메서드도 값으로 저장할 수 있음을 실험한다.
- timeout 예약 ID와 취소를 보여 준다.
- interval 반복과 timeout을 이용한 취소를 연결한다.

## 57.2 개선점

- `x = test1()`과 `x = test1`을 선언 없이 실행해 전역 오염을 만든다.
- strict mode에서는 해당 코드가 ReferenceError가 된다.
- callback 매개변수의 타입 비교에 느슨한 동등 연산자를 사용한다.
- 기본 매개변수 뒤 undefined 검사 코드가 중복이다.
- 같은 이름 함수 선언의 호이스팅 설명이 없다.
- `console.log`를 전역에서 덮어써 이후 로그 결과가 변경된다.
- `desc()`가 문자열 정렬이며 원본 배열을 변경한다.
- 잘못된 재귀형 `setTimeout()` 코드를 올바른 예약 코드처럼 제시한다.
- 타이머가 최소 지연 뒤 실행된다는 이벤트 루프 설명이 없다.
- `rc()`와 재귀 함수가 선언만 되고 호출되지 않는다.
- 문서 제목과 언어가 학습 내용에 맞지 않는다.

---

# 58. My Code vs Teacher Code

| 비교 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 함수 준비 설명 | 상세 추가 | 선언·사용 주석만 |
| `getArea2` 설명 | 반환값 설명 추가 | 코드 중심 |
| 중첩 plus | 기존 `result` 사용 | 숫자 5 직접 사용 |
| 최종 중첩 결과 | 13 | 13 |
| Shadowing·TDZ | 상세 설명 | 기본 block 예제 |
| 추가 인수 결과 출력 | 있음 | 없음 |
| 익명 함수 출력 문구 | `익명함수` | `익명 함수` |
| Callback 설명 | 상세 | 코드 중심 |
| 첫 Print 문구 | `첫번째 print 실행` | `print 실행` |
| 전역 `x` 실제 대입 | 없음, 주석 설명 | 있음 |
| 엄격 모드 전역 위험 | 원본에는 설명 없음 | 실제 위험 존재 |
| Console 덮어쓰기 | 동일 | 동일 |
| Desc 정렬 | 동일 | 동일 |
| 재귀 타이머 오류 | 동일 | 동일 |
| Interval 종료 설명 | 더 상세 | 간단 |
| HTML 들여쓰기 | 더 깊음 | 일반적 |

---

# 59. 공통 핵심 코드

```js
function plus(x, y) {
  return x + y
}

const result =
  plus(2, plus(5, 6))

const noName =
  function() {
    console.log("익명 함수")
  }

function test(callback) {
  if (
    typeof callback === "function"
  ) {
    callback()
  }
}

test(noName)

setTimeout(
  noName,
  1000
)

const intervalId =
  setInterval(
    noName,
    2000
  )

setTimeout(
  function() {
    clearInterval(intervalId)
  },
  10000
)
```

---

# 60. 원본 통합 개선 예제

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
  >
  <title>JavaScript 함수와 콜백</title>
  <script>
    "use strict";

    function getArea(width, height) {
      return width * height;
    }

    function plus(x, y = 0) {
      return x + y;
    }

    function runCallback(callback) {
      if (
        typeof callback !== "function"
      ) {
        return;
      }

      callback();
    }

    const printHello = function() {
      console.log("hello world");
    };

    const area =
      getArea(10, 20);

    const sum =
      plus(2, plus(5, 6));

    console.log("면적:", area);
    console.log("합계:", sum);

    runCallback(printHello);
  </script>
</head>
<body>
  <h1>JavaScript 함수와 콜백</h1>
</body>
</html>
```

---

# 61. 정렬 함수 개선 예제

```js
function descending(numbers) {
  return [...numbers]
    .sort((a, b) => b - a)
}

const source =
  [1, 6, 2, 10, 9, 3, 4]

const result =
  descending(source)

console.log("원본:", source)
console.log("결과:", result)
```

숫자 비교 함수를 사용하며 원본 배열을 유지합니다.

---

# 62. 타이머 개선 예제

```js
function printMessage(message) {
  console.log(message)
}

const timeoutId =
  setTimeout(
    function() {
      printMessage("1초 후 실행")
    },
    1000
  )

const intervalId =
  setInterval(
    function() {
      printMessage("2초 간격 실행")
    },
    2000
  )

setTimeout(
  function() {
    clearInterval(intervalId)
    printMessage("반복 종료")
  },
  10000
)

// 필요할 때:
// clearTimeout(timeoutId)
```

---

# 63. 재귀 타이머 개선 예제

```js
function repeat(
  callback,
  delay,
  count
) {
  if (count <= 0) {
    return
  }

  callback()

  setTimeout(
    function() {
      repeat(
        callback,
        delay,
        count - 1
      )
    },
    delay
  )
}

repeat(
  function() {
    console.log("반복")
  },
  1000,
  3
)
```

종료 횟수가 있어 무한 예약을 방지합니다.

---

# 64. 자주 하는 실수

## 64.1 함수 이름만 써도 실행된다고 생각

괄호가 있어야 호출됩니다.

## 64.2 함수 자체와 호출 결과 혼동

`fn`은 함수, `fn()`은 실행 결과입니다.

## 64.3 Return이 없어도 계산값이 자동 반환된다고 생각

명시적 return이 없으면 undefined입니다.

## 64.4 기본 매개변수와 방어 If 중복

`y = 0`이 이미 undefined를 처리합니다.

## 64.5 함수 내부 변수를 바깥에서 접근

지역 변수는 해당 함수 스코프 밖에서 직접 접근할 수 없습니다.

## 64.6 안쪽 동일 이름 선언 전에 바깥 변수를 쓸 수 있다고 생각

TDZ 때문에 ReferenceError가 발생할 수 있습니다.

## 64.7 Callback을 전달할 때 괄호 추가

예약할 함수가 즉시 실행될 수 있습니다.

## 64.8 같은 이름 함수 여러 번 선언

뒤 구현이 선택되어 앞 구현이 가려질 수 있습니다.

## 64.9 내장 Console 메서드 덮어쓰기

이후 모든 로그와 다른 코드 동작에 영향을 줍니다.

## 64.10 숫자 배열에 기본 Sort 사용

문자열 기준으로 정렬됩니다.

## 64.11 SetTimeout에 함수 호출 결과 전달

지연 전에 함수가 즉시 실행됩니다.

## 64.12 재귀 종료 조건 누락

Call stack 초과 또는 무한 예약을 만들 수 있습니다.

---

# 65. 면접·복습 포인트

## Q1. 함수 선언과 호출의 차이는 무엇인가요?

선언은 실행할 코드를 정의하고, 호출은 괄호를 붙여 그 코드를 실제로 실행합니다.

## Q2. 매개변수와 인수의 차이는 무엇인가요?

매개변수는 함수 정의에서 값을 받을 이름이고, 인수는 호출할 때 실제로 전달하는 값입니다.

## Q3. Return의 두 역할은 무엇인가요?

호출 위치로 값을 반환하고 현재 함수 실행을 종료합니다.

## Q4. 함수 자체와 실행 결과는 어떻게 구분하나요?

`fn`은 함수 객체 자체이고 `fn()`은 함수를 실행한 결과입니다.

## Q5. 기본 매개변수는 언제 적용되나요?

해당 인수가 전달되지 않았거나 undefined가 전달되었을 때 적용됩니다.

## Q6. Callback 함수란 무엇인가요?

다른 함수에 인수로 전달되어 그 함수 내부 또는 이후 시점에 호출되는 함수입니다.

## Q7. 같은 이름의 함수 선언이 두 개면 무엇이 실행되나요?

같은 스코프의 일반 함수 선언에서는 뒤 선언이 최종 바인딩으로 선택되는 형태로 동작합니다.

## Q8. 원본 `desc()`의 문제는 무엇인가요?

기본 sort가 문자열 기준이며 인수로 받은 원본 배열도 직접 변경합니다.

## Q9. `setTimeout(callback, 1000)`은 정확히 1초에 실행되나요?

최소 지연 시간이 지난 뒤 실행 가능 상태가 되며 이벤트 루프 상황에 따라 더 늦어질 수 있습니다.

## Q10. 원본 재귀형 타이머가 잘못된 이유는 무엇인가요?

`setTimeout`에 함수 참조가 아니라 재귀 함수의 즉시 호출 결과를 전달해 지연 전에 재귀가 계속되기 때문입니다.

---

# Problems

## 문제 1. 함수 선언과 호출

`"안녕하세요"`를 출력하는 함수를 선언하고 호출하세요.

## 문제 2. 매개변수

가로와 세로를 받아 넓이를 출력하는 함수를 작성하세요.

## 문제 3. 반환값

가로와 세로를 받아 넓이를 반환하는 함수를 작성하고 결과를 변수에 저장하세요.

## 문제 4. 중첩 호출

`plus(2, plus(5, 6))`의 결과와 실행 순서를 작성하세요.

## 문제 5. 지역 변수

함수 내부에 `const value = 10`을 선언하고 함수 밖에서 직접 사용할 수 없는 이유를 설명하세요.

## 문제 6. Shadowing

바깥 블록의 `a = 10`, 안쪽 블록의 `a = 20`을 각각 출력하세요.

## 문제 7. TDZ

안쪽 블록에서 동일한 `const a` 선언 전에 `console.log(a)`를 실행하면 왜 오류가 발생하는지 설명하세요.

## 문제 8. 기본 매개변수

두 수를 더하되 두 번째 값이 없으면 0을 사용하는 함수를 작성하세요.

## 문제 9. 추가 인수

매개변수 두 개인 함수에 세 개의 인수를 전달하면 어떻게 되는지 설명하세요.

## 문제 10. 익명 함수

익명 함수를 변수에 저장하고 호출하세요.

## 문제 11. 함수 참조 복사

문제 10의 함수를 다른 변수에 저장하고 새 변수로 호출하세요.

## 문제 12. Callback

함수를 인수로 받아 타입이 함수일 때만 실행하는 함수를 작성하세요.

## 문제 13. 중복 함수 선언

같은 이름의 함수 선언을 두 번 작성했을 때 어떤 함수가 호출되는지 확인하세요.

## 문제 14. 함수와 실행 결과

`test1`과 `test1()`을 각각 `test2`에 전달해 차이를 확인하세요.

## 문제 15. 엄격 모드 전역

`x = 10`을 strict mode에서 실행할 때 발생하는 문제를 설명하세요.

## 문제 16. 숫자 내림차순

원본 배열을 변경하지 않고 숫자 배열을 내림차순으로 반환하는 함수를 작성하세요.

## 문제 17. SetTimeout

1초 후 `"완료"`를 출력하세요.

## 문제 18. ClearTimeout

2초 후 실행할 타이머를 예약하고 즉시 취소하세요.

## 문제 19. SetInterval

1초마다 `"반복"`을 출력하고 5초 후 반복을 중단하세요.

## 문제 20. 재귀 오류 수정

원본의 `setTimeout(기계_1초후_한번더(함수), 1000)`을 올바른 콜백 전달 방식으로 수정하세요.

## 문제 21. Console 덮어쓰기

`console.log = 3` 이후 `console.log()`를 호출하면 왜 오류가 발생하는지 설명하세요.

## 문제 22. 종합 작업 실행기

다음 요구사항을 만족하세요.

- `runTask(task, delay, onComplete)` 함수
- `task`와 `onComplete`가 함수인지 검사
- delay 밀리초 후 task 실행
- task 반환값을 onComplete에 전달
- 예약 ID 반환
- 예약 취소 가능한 예제 작성
- 엄격 비교 사용

---

# Answers & Explanations

## 정답 1

```js
function hello() {
  console.log("안녕하세요")
}

hello()
```

## 정답 2

```js
function printArea(
  width,
  height
) {
  console.log(
    width * height
  )
}

printArea(10, 20)
```

## 정답 3

```js
function getArea(
  width,
  height
) {
  return width * height
}

const area =
  getArea(10, 20)

console.log(area)
```

## 정답 4

```text
plus(5, 6)
→ 11

plus(2, 11)
→ 13
```

## 정답 5

```js
function example() {
  const value = 10
  console.log(value)
}

example()
```

`value`는 함수 스코프에 있으므로 함수 밖에서 직접 접근할 수 없습니다.

## 정답 6

```js
const a = 10

{
  const a = 20
  console.log(a)
}

console.log(a)
```

출력은 20, 10입니다.

## 정답 7

안쪽 블록에 `const a` 선언이 있으면 그 블록의 `a`가 바깥 `a`를 가립니다. 선언문 실행 전에는 TDZ에 있으므로 접근 시 ReferenceError가 발생합니다.

## 정답 8

```js
function plus(x, y = 0) {
  return x + y
}

console.log(
  plus(2)
)
```

## 정답 9

이름 있는 매개변수 두 개에는 앞의 두 인수만 연결됩니다. 추가 인수 때문에 즉시 오류가 발생하지 않으며 일반적인 반환 결과에는 사용되지 않습니다.

## 정답 10

```js
const printMessage =
  function() {
    console.log("익명 함수")
  }

printMessage()
```

## 정답 11

```js
const copy =
  printMessage

copy()
```

## 정답 12

```js
function runCallback(callback) {
  if (
    typeof callback === "function"
  ) {
    callback()
  }
}

runCallback(
  function() {
    console.log("실행")
  }
)
```

## 정답 13

```js
function print() {
  console.log("첫 번째")
}

function print() {
  console.log("두 번째")
}

print()
```

두 번째 함수가 실행됩니다.

## 정답 14

```js
function test1() {
  return 3
}

function test2(value) {
  console.log(value)
}

test2(test1())
test2(test1)
```

첫 호출은 숫자 3, 두 번째 호출은 함수 객체를 전달합니다.

## 정답 15

```js
"use strict"

x = 10
```

선언되지 않은 식별자에 값을 대입하므로 ReferenceError가 발생합니다.

## 정답 16

```js
function descending(numbers) {
  return [...numbers]
    .sort((a, b) => b - a)
}

const source =
  [1, 6, 2, 10, 9]

console.log(
  descending(source)
)

console.log(source)
```

## 정답 17

```js
setTimeout(
  function() {
    console.log("완료")
  },
  1000
)
```

## 정답 18

```js
const timeoutId =
  setTimeout(
    function() {
      console.log("실행되지 않음")
    },
    2000
  )

clearTimeout(timeoutId)
```

## 정답 19

```js
const intervalId =
  setInterval(
    function() {
      console.log("반복")
    },
    1000
  )

setTimeout(
  function() {
    clearInterval(intervalId)
  },
  5000
)
```

실제 실행 횟수는 이벤트 루프 상황에 따라 고정적으로 단정하지 않습니다.

## 정답 20

```js
function repeat(callback) {
  callback()

  setTimeout(
    function() {
      repeat(callback)
    },
    1000
  )
}
```

함수 호출 결과가 아니라 나중에 실행할 함수 자체를 전달합니다.

## 정답 21

숫자 3은 함수가 아니므로 괄호로 호출할 수 없습니다. `console.log()` 실행 시 TypeError가 발생합니다.

## 정답 22

```js
function runTask(
  task,
  delay,
  onComplete
) {
  if (
    typeof task !== "function" ||
    typeof onComplete !== "function"
  ) {
    throw new TypeError(
      "task와 onComplete는 함수여야 합니다."
    )
  }

  return setTimeout(
    function() {
      const result = task()
      onComplete(result)
    },
    delay
  )
}

const taskId =
  runTask(
    function() {
      return 100 + 200
    },
    1000,
    function(result) {
      console.log(
        `작업 결과: ${result}`
      )
    }
  )

// 실행 전에 취소할 때:
// clearTimeout(taskId)
```

---

# Final Checklist

## 함수 기본

- [ ] 함수 선언과 호출을 구분했다.
- [ ] 함수 이름만 작성한 경우와 괄호를 붙인 경우를 구분했다.
- [ ] 매개변수와 인수를 설명할 수 있다.
- [ ] 함수 호출 결과를 변수에 저장했다.
- [ ] return이 값 반환과 실행 종료를 담당함을 이해했다.
- [ ] return이 없는 함수 결과가 undefined임을 이해했다.
- [ ] 중첩 호출의 안쪽 함수가 먼저 실행됨을 확인했다.

## 스코프

- [ ] 함수 지역 변수는 바깥에서 직접 접근할 수 없음을 이해했다.
- [ ] 안쪽 블록이 바깥 블록 변수에 접근할 수 있음을 확인했다.
- [ ] 바깥 블록은 안쪽 변수에 접근할 수 없음을 확인했다.
- [ ] shadowing을 이해했다.
- [ ] 동일 이름 선언 전 접근에서 TDZ 오류를 이해했다.
- [ ] for 본문 블록의 변수가 헤더 변수를 가릴 수 있음을 이해했다.

## 매개변수

- [ ] 인수가 부족하면 해당 매개변수가 undefined가 됨을 확인했다.
- [ ] 기본 매개변수를 작성했다.
- [ ] 기본 매개변수와 중복 방어 if를 제거할 수 있음을 이해했다.
- [ ] 추가 인수를 전달해도 즉시 오류가 발생하지 않음을 이해했다.
- [ ] undefined와 null의 기본값 적용 차이를 확인했다.

## 함수 값과 Callback

- [ ] 익명 함수를 변수에 저장했다.
- [ ] 함수 참조를 다른 변수에 복사했다.
- [ ] callback 함수를 인수로 전달했다.
- [ ] callback 매개변수 타입을 엄격 비교했다.
- [ ] 함수 자체와 함수 호출 결과를 구분했다.
- [ ] 같은 이름 함수 중복 선언의 위험을 이해했다.
- [ ] 선언 없는 전역 대입을 사용하지 않았다.

## 내장 함수와 정렬

- [ ] Console 객체와 메서드도 값으로 참조할 수 있음을 이해했다.
- [ ] 전역 `console.log`를 덮어쓰지 않았다.
- [ ] 숫자 정렬에 비교 함수를 사용했다.
- [ ] 정렬 함수가 원본 배열을 변경하지 않도록 복사했다.

## 타이머

- [ ] setTimeout에 함수 자체를 전달했다.
- [ ] 지연 시간이 정확한 실행 시각을 보장하지 않음을 이해했다.
- [ ] timeout ID로 예약을 취소했다.
- [ ] setInterval ID로 반복을 취소했다.
- [ ] 타이머 예약 후 다음 코드가 계속 실행됨을 이해했다.
- [ ] 재귀 호출에 종료 조건을 작성했다.
- [ ] 원본 재귀 타이머의 즉시 호출 오류를 설명했다.

## 원본 코드 검수

- [ ] 두 실제 원본 경로를 기록했다.
- [ ] 내 중첩 plus가 기존 result에 의존함을 기록했다.
- [ ] 두 코드의 최종 중첩 결과가 13임을 확인했다.
- [ ] 내 callback 용어 설명을 보완했다.
- [ ] 강사님 코드의 선언 없는 `x` 대입을 기록했다.
- [ ] strict mode에서 해당 코드가 오류임을 설명했다.
- [ ] 두 원본의 Console 덮어쓰기를 기록했다.
- [ ] 이후 모든 Console 출력이 변경됨을 설명했다.
- [ ] `desc()`의 문자열 정렬과 원본 변경 문제를 기록했다.
- [ ] 원본의 재귀형 setTimeout 코드가 잘못됨을 기록했다.
- [ ] rc와 재귀 함수가 선언만 되고 호출되지 않음을 확인했다.
- [ ] 타이머 출력 횟수를 고정값으로 단정하지 않았다.

---

# Key Summary

- 함수는 선언한 뒤 괄호를 붙여 호출해야 실행된다.
- 함수 이름 `fn`은 함수 객체 자체이고 `fn()`은 실행 결과다.
- 매개변수는 함수 정의에서 값을 받을 이름이고 인수는 호출할 때 전달하는 실제 값이다.
- `return`은 호출 위치로 값을 반환하고 현재 함수 실행을 종료한다.
- 명시적 return이 없는 함수의 호출 결과는 undefined다.
- 강사님 `plus(2, plus(5, 6))`와 내 `plus(2, plus(result, 6))`은 현재 코드 순서에서 모두 13이다.
- 내 코드는 직전 `result = 5`에 의존하므로 실행 순서가 달라지면 결과도 달라질 수 있다.
- 함수 내부 변수와 외부 변수는 서로 다른 스코프에서 같은 이름을 사용할 수 있다.
- 안쪽 스코프의 같은 이름 변수가 바깥 변수를 가리는 것을 shadowing이라고 한다.
- 안쪽 `const` 선언 전에 같은 이름을 접근하면 TDZ로 ReferenceError가 발생할 수 있다.
- 인수가 부족하면 매개변수는 undefined가 되고, 추가 인수는 이름 있는 매개변수에 연결되지 않을 수 있다.
- 기본 매개변수 `y = 0`이 있으면 undefined 방어 if는 현재 예제에서 중복이다.
- 익명 함수도 변수에 저장하고 다른 변수나 함수 인수로 전달할 수 있다.
- callback은 다른 함수에 전달되어 내부 또는 나중 시점에 호출되는 함수다.
- `fn`은 callback을 받는 매개변수이고 `fn`이 참조하는 전달 함수가 callback이다.
- 같은 이름의 일반 함수 선언이 중복되면 뒤 선언이 최종적으로 사용되는 형태로 동작한다.
- 강사님 코드는 `x`를 선언하지 않고 대입해 전역 오염을 만들며 strict mode에서는 오류다.
- `console.log = 3`은 log를 숫자로 바꾸므로 함수 호출이 불가능해진다.
- 두 원본은 이후 `console.log`를 사용자 함수로 다시 덮어써 모든 후속 로그에 영향을 준다.
- 원본 `desc()`는 기본 문자열 정렬을 사용하고 전달받은 원본 배열도 변경한다.
- 숫자 내림차순은 복사 후 `(a, b) => b - a` 비교 함수로 정렬하는 것이 안전하다.
- `setTimeout()`에는 함수 호출 결과가 아니라 나중에 실행할 함수 자체를 전달한다.
- timeout과 interval의 반환 ID는 각각 clearTimeout과 clearInterval에서 취소에 사용한다.
- 타이머 지연 시간은 최소 대기 시간에 가까우며 정확한 실행 시각을 보장하지 않는다.
- 원본의 `setTimeout(기계_1초후_한번더(함수), 1000)`은 함수를 즉시 호출해 실제 호출 시 stack overflow를 만들 수 있다.
- 올바른 재귀 타이머는 익명 함수나 화살표 함수 안에서 다음 재귀 호출을 예약해야 한다.
- 원본의 `rc()`와 재귀형 함수는 선언만 되고 실제로 호출되지는 않는다.
