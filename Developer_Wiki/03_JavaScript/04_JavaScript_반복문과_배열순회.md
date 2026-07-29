# JavaScript 반복문과 배열 순회

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `04_JavaScript_반복문과_배열순회.md` |
| 분류 | `03_JavaScript` |
| 권장 선수 학습 | `03_JavaScript_조건문과_Switch.md` |
| 다음 학습 | `05_JavaScript_함수.md` |
| 원본 기준 | `workspace_me/workspace/workspace_html/javascript/04_for.html`, `workspace_teacher/workspace_teacher/workspace_html/javascript/04_for.html`, 양쪽의 `04_1_pyramid.html` |
| 추가 원본 | 내 코드에만 `04_2_...html` 형식의 피라미드 복습 파일이 하나 더 존재하며, 압축 파일 내부의 한글 파일명이 깨져 표시되어 정확한 원래 이름은 확인하기 어렵다. |
| 핵심 범위 | `for`, 초기화식·조건식·증감식, 누적 합계, 역순 반복, 홀짝 판별, 중첩 반복문, 구구단, 주사위 조합, 난수 반복, `break`, `continue`, 플래그, `for...in`, `for...of`, `forEach()`, `map()`, `sort()`, `filter()`, 화살표 함수, 문자열 패턴·피라미드 |
| 프로젝트 연결 | 목록 출력, 데이터 집계, 검색 중단, 특정 항목 건너뛰기, 배열 변환·필터링·정렬, 페이지 목록 생성, 좌석 탐색, 조합 생성, 패턴 렌더링 |

> 이 문서는 `04_for.html`과 `04_1_pyramid.html`을 함께 분석해 작성했습니다. 반복문 기본 문법뿐 아니라 배열 순회 메서드와 중첩 반복문을 이용한 문자열 패턴까지 하나의 단원으로 통합했습니다. 내 코드에만 존재하는 추가 피라미드 복습 파일도 별도 차이로 기록합니다. 원본의 오타, 선언 누락, 부정확한 주석과 미완성 코드는 조용히 수정하지 않고 보존한 뒤 설명합니다.

---

# 학습 목표

- 반복문이 필요한 이유를 설명한다.
- `for`문의 초기화식, 조건식, 실행 블록, 증감식 순서를 이해한다.
- 증가 반복과 감소 반복을 작성한다.
- 누적 변수로 합계와 개수를 계산한다.
- 조건문을 반복문 안에서 사용한다.
- 중첩 반복문의 실행 횟수를 추적한다.
- 구구단과 주사위 조합을 생성한다.
- `break`와 `continue`의 차이를 설명한다.
- 중첩 반복문을 플래그로 종료하는 구조를 이해한다.
- `for...in`과 `for...of`의 차이를 구분한다.
- `forEach()`, `map()`, `filter()`의 반환값 차이를 이해한다.
- 숫자 배열을 비교 함수로 정렬한다.
- 화살표 함수 축약 문법을 읽고 작성한다.
- 문자열 누적과 중첩 반복문으로 피라미드 패턴을 만든다.
- prompt 입력 줄 수에 맞춰 동적 패턴을 출력한다.
- 원본 코드의 오류와 개선점을 실제 실행 흐름에 근거해 설명한다.

---

# 1. 반복문이란?

반복문은 같은 구조의 코드를 여러 번 실행합니다.

반복문이 없다면 다음처럼 직접 작성해야 합니다.

```js
console.log(1)
console.log(2)
console.log(3)
console.log(4)
console.log(5)
```

`for`문을 사용하면 반복 규칙을 한 번만 작성할 수 있습니다.

```js
for (let i = 1; i <= 5; i++) {
  console.log(i)
}
```

반복문은 단순한 복사·붙여넣기를 줄이고, 반복 횟수가 바뀌어도 조건만 수정할 수 있게 합니다.

---

# 2. 원본 파일 구성

JavaScript 04번은 하나의 파일만으로 구성되지 않습니다.

공통 파일:

```text
04_for.html
04_1_pyramid.html
```

내 코드에만 존재하는 추가 파일:

```text
04_2_...html
```

추가 파일은 압축 내부 한글 파일명이 깨져 표시되지만, 내용상 `04_1_pyramid.html`의 1~12단계 복습·정리 버전입니다.

따라서 이 문서는 다음 두 축으로 구성합니다.

```text
04_for.html
→ 반복문 기본, 중첩 반복, break·continue, 배열 순회 메서드

04_1_pyramid.html 및 추가 복습 파일
→ 문자열 누적, 중첩 반복, 패턴·피라미드
```

---

# 3. 원본 문서 구조

양쪽 원본은 모두 `<head>` 안의 내부 `<script>`에서 코드를 실행합니다.

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
    // 반복문 실습
  </script>
</head>
<body>
</body>
</html>
```

결과는 브라우저 개발자 도구 Console에서 확인합니다.

---

# 4. 문서 언어와 제목

공통 원본:

```html
<html lang="en">
<title>Document</title>
```

콘텐츠가 한국어이므로 다음처럼 개선할 수 있습니다.

```html
<html lang="ko">
<title>JavaScript 반복문과 배열 순회</title>
```

---

# 5. For문의 기본 구조

강사님 원본:

```js
for (초기화식; 조건식; 증감식)
```

내 코드:

```js
for( 초기화식; 조건식; 증감식; )
```

내 코드에는 증감식 뒤에 세미콜론이 하나 더 적혀 있습니다.

실제 문법은 다음과 같습니다.

```js
for (초기화식; 조건식; 증감식) {
  실행문
}
```

괄호 안에는 구분용 세미콜론이 두 개 들어갑니다.

---

# 6. For문의 실행 순서

공통 설명을 정리하면:

```text
1. 초기화식 실행
2. 조건식 검사
3. 조건이 true이면 실행 블록 실행
4. 증감식 실행
5. 다시 조건식 검사
6. 조건이 false가 될 때 종료
```

흐름:

```text
초기화
→ 조건 검사
→ 블록 실행
→ 증감
→ 조건 검사
→ 블록 실행
→ ...
```

초기화식은 반복 전체에서 한 번만 실행됩니다.

---

# 7. 생략 가능한 항목

원본 주석은 초기화식, 조건식, 증감식을 생략할 수 있다고 설명합니다.

예:

```js
let i = 1

for (; i <= 5; i++) {
  console.log(i)
}
```

모두 생략할 수도 있습니다.

```js
for (;;) {
  // 무한 반복
}
```

이 경우 반드시 내부에서 종료 조건과 `break`를 관리해야 합니다.

---

# 8. 1부터 10까지 출력

공통 원본:

```js
for (let i = 1; i <= 10; i++) {
  console.log(i)
}
```

구성:

```text
let i = 1
→ 시작값

i <= 10
→ 반복 조건

i++
→ 한 번 실행 후 1 증가
```

출력:

```text
1
2
3
...
10
```

조건이 `i < 10`이면 9까지만 출력됩니다.

---

# 9. 반복 변수의 블록 스코프

```js
for (let i = 1; i <= 5; i++) {
  console.log(i)
}
```

`let i`는 for 블록 범위에 속합니다.

```js
console.log(i)
```

를 반복문 밖에서 실행하면 같은 이름의 외부 변수가 없는 경우 ReferenceError가 발생합니다.

서로 다른 반복문에서 `let i`를 다시 선언할 수 있습니다.

---

# 10. 직접 작성한 1~5 합계

공통 원본은 먼저 반복문 없이 합계를 작성합니다.

```js
let sum = 0

sum = sum + 1
sum += 2
sum += 3
sum += 4
sum += 5

console.log(sum)
```

결과:

```text
15
```

반복되는 구조는 다음입니다.

```js
sum += 숫자
```

숫자 부분만 1씩 변합니다.

---

# 11. For문으로 1~5 합계

공통 원본:

```js
sum = 0

for (let i = 1; i <= 5; i++) {
  sum += i
}

console.log(sum)
```

실행 추적:

| i | 이전 sum | 계산 | 새 sum |
| ---: | ---: | --- | ---: |
| 1 | 0 | `0 + 1` | 1 |
| 2 | 1 | `1 + 2` | 3 |
| 3 | 3 | `3 + 3` | 6 |
| 4 | 6 | `6 + 4` | 10 |
| 5 | 10 | `10 + 5` | 15 |

---

# 12. 누적 변수

`sum`처럼 반복 결과를 계속 더해 저장하는 변수를 누적 변수로 볼 수 있습니다.

```js
let total = 0

for (let i = 1; i <= 100; i++) {
  total += i
}
```

주의:

반복문 전에 초기값을 설정해야 합니다.

```js
let total
total += 1
```

처럼 작성하면 `undefined + 1`이 되어 NaN이 됩니다.

---

# 13. 문제 1: 5부터 1까지 출력

공통 원본:

```js
for (let i = 5; i >= 1; i--) {
  console.log(i)
}
```

감소 반복의 구성:

```text
시작값 5
조건 i >= 1
증감식 i--
```

출력:

```text
5
4
3
2
1
```

---

# 14. 감소 반복의 조건 실수

다음 코드는 종료되지 않을 수 있습니다.

```js
for (let i = 5; i <= 1; i--) {
}
```

처음부터 조건이 false이므로 한 번도 실행되지 않습니다.

반대로:

```js
for (let i = 5; i >= 1; i++) {
}
```

증가 방향이 종료 조건과 반대라 무한 반복이 될 수 있습니다.

시작값, 조건, 증감 방향을 함께 확인해야 합니다.

---

# 15. 문제 2: 1~5 홀짝 표시

강사님 코드:

```js
for (let i = 1; i <= 5; i++) {
  if (i % 2 != 0) {
    console.log(`${i}(홀)`)
  } else {
    console.log(`${i}(짝)`)
  }
}
```

내 코드:

```js
for (let i = 1; i <= 5; i++) {
  if (i % 2 == 0) {
    console.log(`${i}(짝)`)
  } else {
    console.log(`${i}(홀)`)
  }
}
```

조건 방향만 다르고 결과는 같습니다.

---

# 16. 엄격 비교 개선

원본은 일부에서 `==`, `!=`를 사용합니다.

숫자 나머지와 숫자 0 또는 1을 비교하므로 엄격 비교가 자연스럽습니다.

```js
i % 2 === 0
i % 2 !== 0
```

---

# 17. 문제 3: 홀수 개수

강사님 코드는 별도 문제 번호 없이 설명하지만, 내 코드는 문제 3으로 이름 붙였습니다.

내 코드:

```js
let count = 0

for (let i = 1; i <= 10; i++) {
  if (i % 2 !== 0) {
    count++
  }
}

console.log(`count : ${count}`)
```

결과:

```text
5
```

홀수:

```text
1, 3, 5, 7, 9
```

---

# 18. 합계와 개수의 차이

합계:

```js
sum += i
```

조건을 만족하는 값 자체를 더합니다.

개수:

```js
count++
```

조건을 만족할 때마다 1만 증가합니다.

예:

```js
let oddSum = 0
let oddCount = 0

for (let i = 1; i <= 10; i++) {
  if (i % 2 !== 0) {
    oddSum += i
    oddCount++
  }
}
```

---

# 19. 반복문을 만드는 원리

공통 원본의 학습 절차:

```text
1. 반복되는 부분을 찾는다.
2. 반복되지 않는 값의 규칙을 찾는다.
3. 변하는 값을 변수로 바꾼다.
4. 시작값을 정한다.
5. 종료 조건을 정한다.
```

예:

```js
console.log("2 x 1 = 2")
console.log("2 x 2 = 4")
```

반복되는 부분:

```text
"2 x "
" = "
```

변하는 부분:

```text
1, 2
결과 2, 4
```

이를 반복 변수로 바꿉니다.

---

# 20. 구구단 2단

공통 원본:

```js
for (let i = 1; i <= 9; i++) {
  console.log(`2 x ${i} = ${i * 2}`)
}
```

한 반복문은 한 단을 출력합니다.

반복 변수 `i`는 곱해지는 수입니다.

---

# 21. 중첩 반복문

구구단 전체:

```js
for (let j = 2; j <= 9; j++) {
  for (let i = 1; i <= 9; i++) {
    console.log(`${j} x ${i} = ${i * j}`)
  }
}
```

바깥 반복문:

```text
2단부터 9단까지 선택
```

안쪽 반복문:

```text
각 단에서 1부터 9까지 곱함
```

총 실행 횟수:

```text
8개 단 × 9회
= 72회
```

---

# 22. 중첩 반복문의 실행 흐름

```text
j = 2
  i = 1~9 전부 실행

j = 3
  i = 1~9 전부 실행

...

j = 9
  i = 1~9 전부 실행
```

안쪽 반복문은 바깥 반복문의 한 번마다 처음부터 끝까지 다시 실행됩니다.

---

# 23. 문제 3: 주사위 하나

공통 원본:

```js
for (let i = 1; i <= 6; i++) {
  console.log(i)
}
```

가능한 결과:

```text
1, 2, 3, 4, 5, 6
```

총 6가지입니다.

내 코드에서는 앞서 홀수 개수를 문제 3이라 불렀고, 이후 주사위 하나도 다시 문제 3으로 표시합니다.

즉, **내 원본의 문제 번호가 중복**됩니다.

문서에서는 원본 번호 중복을 보존하고, 학습 문제 섹션은 새로 1~22로 정리합니다.

---

# 24. 문제 4: 주사위 두 개

공통 원본:

```js
for (let p = 1; p <= 6; p++) {
  for (let q = 1; q <= 6; q++) {
    console.log(`[${p}, ${q}]`)
  }
}
```

가능한 조합 수:

```text
6 × 6
= 36
```

`[1, 2]`와 `[2, 1]`은 서로 다른 순서 있는 결과로 취급합니다.

---

# 25. 문자열 연결과 템플릿 리터럴

강사님 코드:

```js
console.log('[' + j + ',' + i + '] ')
```

내 코드:

```js
console.log(`[${p}, ${q}]`)
```

둘 다 같은 정보를 출력합니다.

템플릿 리터럴이 변수 경계를 읽기 쉽습니다.

---

# 26. 문제 5: 주사위 합별 조합

강사님은 합 2와 합 3을 각각 별도 반복문으로 먼저 확인합니다.

```js
if (j + i == 2) {
  console.log(...)
}
```

이후 합 2~12 전체를 바깥 반복으로 일반화합니다.

내 코드도 여러 시도 코드를 주석으로 남긴 뒤 최종적으로 합 2~12를 순회합니다.

---

# 27. 합별 조합 일반화

내 코드:

```js
for (let r = 2; r <= 12; r++) {
  let value = `합계 ${r} `

  for (let p = 1; p <= 6; p++) {
    for (let q = 1; q <= 6; q++) {
      if (p + q == r) {
        value += `[${p}, ${q}]`
      }
    }
  }

  console.log(value)
}
```

바깥 반복 `r`은 목표 합입니다.

안쪽 두 반복은 주사위 모든 조합을 확인합니다.

---

# 28. 실행 횟수 분석

목표 합:

```text
2~12
→ 11개
```

각 합마다 조합 검사:

```text
6 × 6
→ 36회
```

전체 조건 검사:

```text
11 × 36
→ 396회
```

학습용으로 명확하지만 한 번의 36개 조합 순회에서 합별 배열을 구성하는 방법도 있습니다.

---

# 29. 내 코드의 중복 제거 주석 검토

내 코드:

```js
// 두번째 for문에서 q=p로 바꾸면 중복값을 제거할 수 있음
```

`q = p`로 시작하면 `[1,2]`와 `[2,1]` 중 하나만 남기는 조합을 만들 수 있습니다.

다만 주사위 두 개를 서로 구분한다면 두 결과는 다른 경우입니다.

따라서 “중복” 여부는 문제 정의에 달려 있습니다.

```text
서로 구분되는 두 주사위
→ [1,2]와 [2,1]은 다름

구분하지 않는 두 값의 조합
→ 하나만 남길 수 있음
```

---

# 30. 강사님 Hap9 누적

강사님 코드는 전체 합을 출력하면서 합이 9인 조합만 문자열로 별도 누적합니다.

```js
let hap9 = ""

if (k == 9) {
  hap9 += '[' + j + ',' + i + '] '
}
```

마지막 출력:

```js
console.log('합 9 :' + hap9)
```

내 코드에는 `hap9` 별도 누적이 없습니다.

대신 각 합의 조합을 한 문자열에 모아 출력합니다.

---

# 31. 로또 숫자 반복 출력

공통 원본:

```js
for (let i = 1; i <= 6; i++) {
  let lotto =
    parseInt(Math.random() * 45) + 1

  console.log(lotto)
}
```

1~45 숫자를 6번 생성합니다.

하지만 원본 주석처럼 중복이 나올 수 있습니다.

```text
예: 3, 17, 17, 28, 41, 3
```

이 코드는 실제 로또 번호 생성기의 “중복 없는 6개” 조건을 충족하지 않습니다.

---

# 32. Math Floor 개선

숫자 정수화에는 다음 표현이 의도를 더 잘 드러냅니다.

```js
Math.floor(Math.random() * 45) + 1
```

범위:

```text
1 이상
45 이하
```

중복 제거는 배열과 반복 검사가 필요합니다.

---

# 33. Break 기본

공통 원본:

```js
for (let i = 1; i <= 100; i++) {
  if (i == 11) {
    console.log(i, "종료합니다")
    break
  }

  console.log(i)
}
```

`break`는 현재 반복문을 즉시 종료합니다.

출력 흐름:

```text
1~10 출력
11에서 종료 메시지
반복 종료
```

11은 일반 출력문에는 도달하지 않습니다.

---

# 34. 내 코드의 안전성 주석

내 코드:

```js
// i>10이 더욱 안전하고, ==으로 하면 넘어갈수도 있기 때문에 오류가 발생할 수 있다
```

핵심은 맞습니다.

예를 들어 증감이 2씩 진행되면:

```js
for (let i = 1; i <= 100; i += 2) {
  if (i === 10) {
    break
  }
}
```

10을 건너뛰므로 종료되지 않습니다.

경계 기반 종료라면:

```js
if (i > 10)
```

처럼 범위를 사용하는 것이 더 견고할 수 있습니다.

---

# 35. 중첩 반복문 종료

주차장 예제:

```text
총 4층
층마다 10자리
17번째 자리에서 탐색 종료
```

안쪽 반복문에서 `break`를 실행해도 안쪽 반복문만 종료됩니다.

바깥 반복문까지 종료하려면 추가 상태가 필요합니다.

---

# 36. Flag 변수

공통 원본:

```js
let cnt = 0
let flag = false
```

찾았을 때:

```js
flag = true
break
```

안쪽 반복문 종료 후:

```js
if (flag) {
  break
}
```

이렇게 바깥 반복문도 종료합니다.

`flag`는 특정 상태가 발생했는지 표시하는 Boolean 변수입니다.

---

# 37. 강사님 코드의 불필요한 J 증가

강사님 코드:

```js
if (cnt >= 17) {
  flag = true
  j++
  break
}
```

`break`가 즉시 안쪽 반복문을 종료하므로 `j++`는 결과에 필요하지 않습니다.

내 코드에서는 이 `j++`가 제거되어 있습니다.

이 차이는 내 코드의 개선점입니다.

---

# 38. 한층 끝 출력 차이

강사님 코드:

```js
console.log('한층 끝')
```

바깥 반복이 계속될 때 층 종료를 표시합니다.

내 코드에는 이 출력이 없습니다.

기능상 탐색 결과에는 영향이 없지만 실행 흐름을 확인하는 디버깅 출력 차이입니다.

---

# 39. Label문 확장

중첩 반복문을 직접 종료하는 문법도 있습니다.

```js
outer:
for (let floor = 1; floor <= 4; floor++) {
  for (let seat = 1; seat <= 10; seat++) {
    if (조건) {
      break outer
    }
  }
}
```

원본은 flag 방식 학습을 사용합니다.

label은 유용할 수 있지만 과도하게 사용하면 흐름을 읽기 어려울 수 있습니다.

---

# 40. Continue

공통 원본:

```js
for (let i = 1; i <= 10; i++) {
  if (i % 2 == 0) {
    continue
  }

  console.log(i)
}
```

짝수일 때 현재 반복의 남은 코드를 건너뜁니다.

출력:

```text
1
3
5
7
9
```

---

# 41. Break와 Continue 비교

| 구문 | 동작 |
| --- | --- |
| `break` | 현재 반복문 전체 종료 |
| `continue` | 현재 회차만 건너뛰고 다음 반복 진행 |

예:

```js
for (let i = 1; i <= 5; i++) {
  if (i === 3) break
}
```

```text
1, 2 후 종료
```

```js
for (let i = 1; i <= 5; i++) {
  if (i === 3) continue
}
```

```text
1, 2, 4, 5
```

---

# 42. 배열 원본

공통 원본:

```js
let arr = [1, 2, 3, 4, 5, 6, 7]
```

이 배열을 여러 방식으로 순회합니다.

```text
for...in
for...of
forEach()
map()
```

각 방식은 목적과 반환값이 다릅니다.

---

# 43. For In

공통 원본:

```js
for (let i in arr) {
  console.log(i)
  console.log(arr[i])
}
```

배열에서 `i`는 인덱스 키입니다.

출력되는 인덱스는 문자열 형태일 수 있습니다.

```text
"0", "1", "2", ...
```

내 코드 주석은 index가 중요할 때 사용하는 방법이라고 설명합니다.

---

# 44. 배열에서 For In 주의

`for...in`은 객체의 열거 가능한 속성 키를 순회합니다.

배열의 값 순회에는 일반적으로 다음을 더 자주 검토합니다.

```js
for...of
arr.forEach()
전통적인 for
```

인덱스가 필요하다면:

```js
for (let i = 0; i < arr.length; i++) {
  console.log(i, arr[i])
}
```

또는:

```js
for (const [index, value] of arr.entries()) {
  console.log(index, value)
}
```

---

# 45. For Of

공통 원본:

```js
for (let value of arr) {
  console.log(value)
}
```

`for...of`는 배열의 값을 직접 순회합니다.

```text
1
2
3
...
7
```

인덱스를 직접 제공하지는 않습니다.

---

# 46. For In과 For Of 비교

| 구분 | `for...in` | `for...of` |
| --- | --- | --- |
| 기본 대상 | 속성 키 | iterable의 값 |
| 배열에서 받는 값 | 인덱스 키 | 배열 요소 |
| 객체 일반 순회 | 가능 | 일반 객체는 직접 불가 |
| 배열 값 순회 권장도 | 주의 필요 | 자연스러움 |
| `break`·`continue` | 가능 | 가능 |

---

# 47. ForEach 기본

공통 원본:

```js
arr.forEach(function(a, b, c, d) {
  console.log(a)
  console.log(b)
  console.log(c)
  console.log(d)
})
```

콜백에 전달되는 표준 인수는 세 개입니다.

```text
첫 번째 → 현재 요소
두 번째 → 현재 인덱스
세 번째 → 원본 배열
```

네 번째 `d`는 전달되지 않으므로 undefined입니다.

---

# 48. ForEach 반환값

공통 원본:

```js
let r1 = arr.forEach(function(
  element,
  index,
  array
) {
  console.log(element, index, array)
})

console.log(r1)
```

`forEach()` 자체의 반환값은 undefined입니다.

콜백에서 값을 return하더라도 새로운 결과 배열을 만들지 않습니다.

---

# 49. ForEach와 Break

`forEach()` 콜백 내부에서는 일반적인 `break`를 사용할 수 없습니다.

중간 종료가 필요하면 다음을 검토합니다.

```text
for
for...of
some()
every()
find()
```

원본에는 이 차이가 직접 설명되어 있지 않으므로 확장 학습으로 구분합니다.

---

# 50. Map 기본

공통 원본:

```js
let r2 = arr.map(function(el, i, a) {
  if (el % 2 == 0) {
    return "짝"
  } else {
    return "홀"
  }
})
```

결과:

```js
["홀", "짝", "홀", "짝", "홀", "짝", "홀"]
```

`map()`은 각 요소를 변환해 원본과 같은 길이의 새 배열을 만듭니다.

---

# 51. 강사님 Map 주석 오류

강사님 코드:

```js
console.log(r2) // undefined
```

실제 `r2`는 undefined가 아닙니다.

콜백에서 `"짝"` 또는 `"홀"`을 항상 반환하므로 새 배열이 저장됩니다.

내 코드 주석:

```js
console.log(r2) // retrurn이 없으면 undefined array
```

`retrurn`은 `return`의 오타입니다.

정확한 설명:

```text
콜백에서 return하지 않은 요소의 결과 자리에 undefined가 들어간다.
map 자체는 배열을 반환한다.
```

---

# 52. Map에서 Return이 없는 경우

```js
const result = [1, 2, 3].map(function(value) {
  console.log(value)
})
```

결과:

```js
[undefined, undefined, undefined]
```

`result` 자체가 undefined인 것이 아닙니다.

배열의 각 자리가 undefined입니다.

---

# 53. 영화 제목 길이

공통 원본:

```js
let movie = [
  "호프",
  "스파이더맨-브랜드 뉴 데이",
  "오디세이",
  "모아나"
]

let r3 = movie.map(function(el) {
  return el.length
})
```

각 문자열의 길이를 새 배열로 만듭니다.

문자열 `length`는 JavaScript 코드 단위 기준이며 사용자에게 보이는 문자 수와 항상 같다고 단정할 수는 없습니다.

현재 한글·일반 기호 예제에서는 학습 목적으로 사용할 수 있습니다.

---

# 54. 화살표 함수 단계

공통 원본:

```js
let r3 = movie.map(function(el) {
  return el.length
})
```

화살표 함수:

```js
let r4 = movie.map((el) => {
  return el.length
})
```

매개변수 하나와 표현식 하나:

```js
let r5 = movie.map(el => el.length)
```

이 경우 표현식 결과가 암묵적으로 반환됩니다.

---

# 55. 화살표 함수 생략 조건

매개변수 하나:

```js
el => el.length
```

매개변수 없음:

```js
() => 10
```

매개변수 둘 이상:

```js
(a, b) => a + b
```

객체 리터럴을 바로 반환하려면 괄호가 필요합니다.

```js
value => ({ value })
```

---

# 56. Sort 기본

원본:

```js
r3.sort(function(y, x) {
  return Number(x) - Number(y)
})
```

내림차순 정렬을 의도합니다.

일반적인 매개변수 이름은 `a`, `b`가 더 익숙합니다.

```js
numbers.sort((a, b) => b - a)
```

오름차순:

```js
numbers.sort((a, b) => a - b)
```

---

# 57. 내 코드 Sort 설명 오류

내 코드 주석:

```text
음수가 나오면 뒤에게 크고,
양수가 나오면 앞에게 크고
```

표현이 부정확합니다.

비교 함수 `compare(a, b)`의 일반 의미:

```text
음수 반환
→ a를 b보다 앞에 배치

양수 반환
→ a를 b보다 뒤에 배치

0 반환
→ 순서를 동일하게 취급
```

`뒤에게`, `앞에게`는 문장상 어색한 표현입니다.

---

# 58. Sort는 원본 배열 변경

```js
r3.sort((a, b) => a - b)
```

`sort()`는 새 배열만 반환하는 메서드가 아니라 기존 배열 자체의 순서를 변경합니다.

원본을 유지하려면:

```js
const sorted =
  [...r3].sort((a, b) => a - b)
```

원본에는 이 부작용 설명이 없습니다.

---

# 59. 마지막 요소 접근

공통 원본:

```js
console.log(r3[r3.length - 1])
```

배열 길이가 4이면 마지막 인덱스는 3입니다.

```text
length = 4
마지막 index = 3
```

내 코드에는 `console.log(r3.length)`도 추가되어 있습니다.

현대 JavaScript에서는 다음도 사용할 수 있습니다.

```js
r3.at(-1)
```

---

# 60. Filter 기본

공통 원본:

```js
let r6 = movie.filter(function(el) {
  return el.length >= 4
})
```

조건을 만족한 요소만 새 배열에 포함합니다.

`map()`은 각 요소를 변환하며 길이를 유지하지만, `filter()`는 요소를 선택하므로 길이가 줄어들 수 있습니다.

---

# 61. Filter의 Return

다음 코드는 명시적인 Boolean을 반환합니다.

```js
return el.length >= 4
```

truthy 또는 falsy를 반환해도 선택 여부가 결정됩니다.

내 코드 주석:

```js
// 값이 0일수가 있기에 true를 주는게 나음
```

이 설명은 문맥이 불명확합니다.

`filter()`는 반환값을 Boolean으로 변환해 판단하므로, 조건식 자체를 반환하는 방식이 가장 명확합니다.

---

# 62. Filter 화살표 함수

공통 원본:

```js
r6 = movie.filter(
  el => el.length >= 4
)
```

다음과 같은 의미입니다.

```js
r6 = movie.filter(function(el) {
  return el.length >= 4
})
```

---

# 63. 배열 메서드 비교

| 방식 | 주요 목적 | 반환값 | 중간 종료 |
| --- | --- | --- | --- |
| `for` | 범용 반복 | 없음 | 가능 |
| `for...of` | 값 순회 | 없음 | 가능 |
| `forEach()` | 각 요소 작업 | `undefined` | 일반 break 불가 |
| `map()` | 요소 변환 | 같은 길이의 새 배열 | 일반 break 불가 |
| `filter()` | 조건 요소 선택 | 새 배열 | 일반 break 불가 |
| `sort()` | 순서 변경 | 정렬된 같은 배열 참조 | 해당 없음 |

---

# 64. 피라미드 파일의 목적

`04_1_pyramid.html`은 반복문의 패턴 찾기 연습입니다.

핵심 요소:

```text
바깥 반복문
→ 줄 수

안쪽 반복문
→ 한 줄의 문자 개수

string 변수
→ 한 줄의 결과 누적

console.log(string)
→ 한 줄 출력
```

---

# 65. 문자열 누적

공통 기본:

```js
let string = ""

for (let i = 1; i <= 5; i++) {
  string += "+"
}

console.log(string)
```

결과:

```text
+++++
```

`string`을 반복 전에 초기화하면 문자들이 한 줄에 누적됩니다.

---

# 66. String 초기화 위치

여러 줄 패턴에서는 바깥 반복마다 문자열을 비워야 합니다.

```js
for (let row = 1; row <= 3; row++) {
  let line = ""

  for (let col = 1; col <= 5; col++) {
    line += "+"
  }

  console.log(line)
}
```

초기화를 바깥 반복문 밖에 두면 이전 줄 내용이 계속 누적됩니다.

---

# 67. 1단계: 더하기 5개

공통 결과:

```text
+++++
```

강사님은 변수 `m`을 사용합니다.

```js
string = string + m
```

내 코드는 직접 `"+"`를 더합니다.

```js
string += "+"
```

둘 다 동작합니다.

---

# 68. 2단계: Plus와 Underscore 반복

공통 결과:

```text
+_+_+_+_+_
```

코드:

```js
for (let i = 1; i <= 5; i++) {
  string += "+"
  string += "_"
}
```

한 반복에서 두 문자를 순서대로 누적합니다.

---

# 69. 3단계: 같은 줄 3번

결과:

```text
+++++
+++++
+++++
```

바깥 반복이 3줄을 관리하고, 안쪽 반복이 각 줄의 5개 문자를 관리합니다.

---

# 70. 4단계: 줄 번호 5개

결과:

```text
11111
22222
33333
44444
55555
```

바깥 변수 `j`가 출력할 숫자이자 줄 번호입니다.

```js
for (let j = 1; j <= 5; j++) {
  let line = ""

  for (let i = 1; i <= 5; i++) {
    line += j
  }

  console.log(line)
}
```

---

# 71. 5단계: 증가하는 숫자 개수

목표:

```text
1
22
333
4444
55555
```

가장 간단한 규칙:

```js
for (let row = 1; row <= 5; row++) {
  let line = ""

  for (let count = 1; count <= row; count++) {
    line += row
  }

  console.log(line)
}
```

줄 번호만큼 문자를 출력합니다.

---

# 72. 내 04_1 파일의 불필요한 반복

내 `04_1_pyramid.html`은 5단계에서 다음 구조를 사용합니다.

```js
for (let j = 1; j <= 5; j++) {
  string = ""

  for (k = 1; k <= 5; k++) {
    if (j == k) {
      for (let i = 1; i <= k; i++) {
        string += j
      }

      console.log(string)
    }
  }
}
```

중간 `k` 반복과 `if (j == k)`는 필요하지 않습니다.

줄 번호 `j`를 바로 반복 횟수로 사용할 수 있습니다.

---

# 73. 선언 없는 K

내 `04_1_pyramid.html`의 여러 단계:

```js
for (k = 1; k <= 5; k++) {
```

`let`, `const`, `var`가 없습니다.

느슨한 일반 script에서는 전역 속성을 만들 수 있고, strict mode에서는 ReferenceError가 발생합니다.

권장:

```js
for (let k = 1; k <= 5; k++) {
```

이것은 중요한 원본 오류입니다.

---

# 74. 6단계: 증가하는 Plus

목표:

```text
+
++
+++
++++
+++++
```

규칙은 5단계와 같고 누적 문자가 `"+"`로 바뀝니다.

내 `04_1`은 불필요한 `k` 반복을 포함하지만, 추가 복습 파일은 간단한 두 반복으로 정리되어 있습니다.

---

# 75. 7단계: 감소하는 숫자 개수

목표:

```text
11111
2222
333
44
5
```

반복 횟수:

```text
6 - row
```

코드:

```js
for (let row = 1; row <= 5; row++) {
  let line = ""

  for (
    let count = 1;
    count <= 6 - row;
    count++
  ) {
    line += row
  }

  console.log(line)
}
```

---

# 76. 강사님 7단계 두 방법

강사님 파일은 두 가지 방법을 보여 줍니다.

방법 1:

```js
for (let i = 1; i <= 5 + 1 - j; i++)
```

방법 2:

```js
for (let i = 5; i >= j; i--)
```

둘 다 줄마다 `6 - j`번 실행됩니다.

내 코드는 첫 번째 형태를 사용합니다.

---

# 77. 강사님 피라미드 중간의 대형 패턴

강사님 `04_1_pyramid.html`에는 7단계 뒤에 `ㅁ`과 `-`를 조합하는 긴 중첩 반복 코드가 있습니다.

여러 반복문이 연속으로 한 줄의 패턴을 구성합니다.

하지만 목표 출력 모양을 설명하는 주석이 충분하지 않아 의도를 파악하기 어렵습니다.

문서에서는 원본에 존재하는 추가 패턴 실험으로 기록하며, 핵심 1~12단계와 분리합니다.

---

# 78. 8단계: 왼쪽 Plus와 오른쪽 Underscore

목표:

```text
+____
++___
+++__
++++_
+++++
```

한 줄의 전체 길이는 5입니다.

```text
plus 개수 = row
underscore 개수 = 5 - row
```

---

# 79. 9단계: 왼쪽 Underscore와 오른쪽 Plus

목표:

```text
____+
___++
__+++
_++++
+++++
```

규칙:

```text
underscore 개수 = 5 - row
plus 개수 = row
```

8단계의 두 반복 순서만 바뀝니다.

---

# 80. 10단계: 홀수 개수 피라미드

목표:

```text
____+
___+++
__+++++
_+++++++
+++++++++
```

Plus 개수:

```text
1, 3, 5, 7, 9
```

공식:

```text
2 × row - 1
```

왼쪽 underscore:

```text
5 - row
```

---

# 81. 내 10단계 두 풀이

내 `04_1_pyramid.html`은 먼저 Plus를 두 반복으로 나누어 만듭니다.

```js
for (let i = 1; i <= k; i++) {
  string += "+"
}

for (let i = 2; i <= k; i++) {
  string += "+"
}
```

합계:

```text
k + (k - 1)
= 2k - 1
```

이후 `10단계-1`에서 직접 공식으로 단순화합니다.

```js
for (let k = 1; k <= 2 * j - 1; k++) {
  string += "+"
}
```

두 번째 방식이 규칙을 더 직접 표현합니다.

---

# 82. 11단계: 양쪽 여백

목표:

```text
____+____
___+++___
__+++++__
_+++++++_
+++++++++
```

규칙:

```text
왼쪽 underscore = 5 - row
plus = 2 × row - 1
오른쪽 underscore = 5 - row
```

총 문자열 길이는 항상 9입니다.

---

# 83. 12단계: 입력 줄 수

내 파일은 prompt로 줄 수를 입력받아 11단계를 일반화합니다.

```js
let value =
  prompt("12. 줄 수를 입력해주세요.")
```

반복 조건:

```js
for (let j = 1; j <= value; j++)
```

비교 연산에서 문자열이 숫자로 암묵적 변환될 수 있지만 명시적 변환과 검증이 안전합니다.

---

# 84. 12단계 입력 검증

개선:

```js
const input =
  prompt("줄 수를 입력해주세요.")

if (input === null || input.trim() === "") {
  console.log("입력을 취소했거나 값이 없습니다.")
} else {
  const rows = Number(input)

  if (
    !Number.isInteger(rows) ||
    rows <= 0
  ) {
    console.log("1 이상의 정수를 입력하세요.")
  } else {
    // 피라미드 출력
  }
}
```

너무 큰 수를 입력하면 Console 출력량이 매우 커질 수 있으므로 최대값 제한도 고려할 수 있습니다.

---

# 85. 추가 복습 파일

내 코드에만 존재하는 추가 `04_2_...html` 파일은 피라미드 1~12단계를 다시 구현합니다.

주요 특징:

- 5단계와 6단계를 간단한 중첩 반복으로 작성
- 7단계를 두 방법으로 반복
- 8~11단계를 명확한 두세 개 반복으로 분리
- 12단계 prompt 입력 피라미드까지 완성
- `04_1_pyramid.html`의 불필요한 `k` 반복을 줄임
- 선언 없는 `k` 문제를 대부분 제거

따라서 내용상 **복습·정리 버전**으로 볼 수 있습니다.

다만 파일명이 깨져 정확한 원래 한글 이름은 단정하지 않습니다.

---

# 86. String Repeat 확장

패턴 문제는 `repeat()`로도 작성할 수 있습니다.

```js
for (let row = 1; row <= 5; row++) {
  const line =
    "_".repeat(5 - row) +
    "+".repeat(2 * row - 1) +
    "_".repeat(5 - row)

  console.log(line)
}
```

원본은 반복문 훈련이 목적이므로 중첩 반복을 유지하는 것이 학습에 적합합니다.

`repeat()`는 확장 학습입니다.

---

# 87. My Code 분석

## 87.1 장점

- for문의 실행 순서를 더 자세히 주석으로 설명했다.
- 조건식 생략 시 무한 반복 가능성을 기록했다.
- 합계 코드에 복합 할당을 일관되게 사용했다.
- 홀수 개수 문제를 명시적으로 문제 3으로 구성했다.
- 홀수 판별에 `!==`를 사용했다.
- 반복문을 만드는 원리를 더 자연스러운 문장으로 정리했다.
- 주사위 두 개 출력에 템플릿 리터럴을 사용했다.
- 합별 주사위 조합을 한 문자열로 모아 보기 좋게 출력했다.
- `break` 조건에서 정확한 값보다 범위 조건이 더 안전할 수 있음을 설명했다.
- 주차장 예제에서 강사님의 불필요한 `j++`를 제거했다.
- `for...in`, `for...of`의 index와 value 차이를 상세히 적었다.
- `forEach()` 콜백 인수 의미를 주석으로 기록했다.
- `map()`, 화살표 함수, `sort()`, `filter()` 설명을 확장했다.
- 배열 길이와 마지막 인덱스 관계를 추가로 출력했다.
- 피라미드 5~12단계를 대부분 완성했다.
- 10단계에서 복잡한 풀이를 `2 * j - 1` 공식으로 다시 단순화했다.
- 입력 줄 수에 따라 피라미드를 출력했다.
- 별도 복습 파일에서 패턴 코드를 더 간단하게 정리했다.

## 87.2 개선점

- for 문법 설명에 `증감식;`처럼 불필요한 세미콜론이 하나 더 있다.
- 주사위 하나와 홀수 개수가 모두 문제 3으로 표시되어 번호가 중복된다.
- 비교 연산에서 `==`가 여러 곳에 남아 있다.
- 로또 번호는 중복 제거가 되지 않는다.
- 난수 정수화에 `parseInt()`를 사용한다.
- `for...in`을 배열 index 순회용으로 일반화한 설명은 주의가 필요하다.
- `forEach()` 네 번째 인수는 제공되지 않는다는 설명을 더 명확히 해야 한다.
- `retrurn` 오타가 있다.
- `map()`에서 return이 없으면 “undefined array”라는 설명은 모호하다.
- `sort()` 비교 함수의 음수·양수 설명이 부정확하다.
- `sort()`가 원본 배열을 변경한다는 설명이 없다.
- `filter()`의 “0일 수 있어 true가 낫다”는 주석은 문맥이 불명확하다.
- `04_1_pyramid.html`에서 `k`를 선언하지 않은 반복문이 여러 개 있다.
- 5단계와 6단계에 불필요한 중간 반복과 조건문이 있다.
- prompt 줄 수를 숫자로 변환하거나 검증하지 않는다.
- 조건문과 배열 메서드까지 한 파일에 매우 많은 개념이 포함되어 학습 범위가 넓다.
- 추가 피라미드 파일의 한글 파일명이 깨져 관리와 링크에 불편함이 있다.

---

# 88. Teacher Code 분석

## 88.1 장점

- for문의 실행 순서를 기본 구조부터 설명한다.
- 직접 합산한 코드와 반복문 합산 코드를 비교한다.
- 증가·감소 반복, 홀짝, 개수 집계를 단계적으로 다룬다.
- 반복 패턴을 찾는 사고 절차를 제시한다.
- 한 단 구구단에서 전체 구구단으로 확장한다.
- 주사위 한 개에서 두 개, 합별 조합으로 난도를 높인다.
- 합이 9인 경우를 별도 누적해 누적 문자열 예제를 보여 준다.
- `break`, 중첩 반복 종료, flag, `continue`를 순서대로 학습한다.
- `for...in`, `for...of`, `forEach()`, `map()`, `sort()`, `filter()`를 폭넓게 소개한다.
- 화살표 함수 축약 단계를 보여 준다.
- 피라미드 파일에서 1~4단계와 7단계를 실제 구현한다.
- 7단계를 두 가지 반복 조건으로 구현한다.
- 추가적인 복잡한 문자열 패턴 실험이 있다.

## 88.2 개선점

- 비교에 느슨한 동등 연산자를 자주 사용한다.
- 주차장 예제의 `j++`는 break 직전에 있어 불필요하다.
- 로또 숫자 중복 처리 설명이나 구현이 없다.
- 난수 정수화에 `parseInt()`를 사용한다.
- `for...in`의 배열 사용 주의점이 없다.
- `forEach()`의 네 번째 인수 d가 undefined라는 설명이 없다.
- `map()` 결과를 `undefined`라고 적은 주석은 잘못이다.
- `sort()`가 기존 배열을 변경한다는 설명이 없다.
- `filter()`의 콜백 반환값과 Boolean 변환 설명이 부족하다.
- 피라미드 5, 6, 8~12단계가 미완성이다.
- 피라미드 중간의 대형 패턴은 목표 출력 설명이 부족하다.
- `04_for.html`에 반복문 기본부터 배열 고차 메서드까지 범위가 매우 넓다.
- 문서 언어와 제목이 콘텐츠에 맞지 않는다.

---

# 89. My Code vs Teacher Code

| 비교 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 기본 for 설명 | 더 상세 | 기본 순서 설명 |
| for 괄호 문법 | 증감식 뒤 세미콜론 추가 표기 | 올바른 기본 표기 |
| 홀짝 조건 | 짝수 먼저 | 홀수 먼저 |
| 홀수 개수 번호 | 문제 3 명시 | 번호 없이 설명 |
| 주사위 하나 번호 | 다시 문제 3 | 문제 3 |
| 문제 번호 중복 | 있음 | 없음 |
| 주사위 출력 | 템플릿 리터럴 | 문자열 `+` 연결 |
| 합별 조합 출력 | 합마다 문자열 누적 | 합마다 즉시 출력 |
| 합 9 별도 누적 | 없음 | `hap9` 있음 |
| 로또 중복 주석 | 중복 가능 명시 | 중복 설명 없음 |
| Break 안전성 설명 | `> 10` 권장 설명 | 없음 |
| 주차장 `j++` | 제거 | break 전 불필요하게 있음 |
| `한층 끝` 출력 | 없음 | 있음 |
| For in 설명 | 상세 | 간단 |
| For of 설명 | 상세 | 간단 |
| ForEach 설명 | 상세 | 간단 |
| Map 결과 주석 | 오타·모호함 | `undefined`라고 잘못 표기 |
| Sort 설명 | 추가, 일부 부정확 | 비교 함수 코드 중심 |
| 배열 length 출력 | 추가 | 마지막 요소만 출력 |
| 피라미드 5·6단계 | 구현 | 미완성 |
| 피라미드 8~12단계 | 구현 | 미완성 |
| 선언 없는 `k` | 여러 곳 존재 | 없음 |
| 별도 피라미드 복습 파일 | 있음 | 없음 |
| 복잡한 `ㅁ` 패턴 | 없음 | 있음 |

---

# 90. 공통 핵심 코드

```js
for (let i = 1; i <= 10; i++) {
  console.log(i)
}

let sum = 0

for (let i = 1; i <= 5; i++) {
  sum += i
}

for (let i = 5; i >= 1; i--) {
  console.log(i)
}

for (let i = 1; i <= 5; i++) {
  if (i % 2 === 0) {
    console.log(`${i}(짝)`)
  } else {
    console.log(`${i}(홀)`)
  }
}

for (let dan = 2; dan <= 9; dan++) {
  for (let number = 1; number <= 9; number++) {
    console.log(
      `${dan} x ${number} = ${dan * number}`
    )
  }
}

for (let dice1 = 1; dice1 <= 6; dice1++) {
  for (let dice2 = 1; dice2 <= 6; dice2++) {
    console.log(`[${dice1}, ${dice2}]`)
  }
}
```

---

# 91. 배열 순회 통합 개선 예제

```js
"use strict";

const numbers = [1, 2, 3, 4, 5, 6, 7];

for (const [index, value] of numbers.entries()) {
  console.log(`index: ${index}, value: ${value}`);
}

numbers.forEach((value, index, array) => {
  console.log(value, index, array);
});

const parity = numbers.map(
  value => value % 2 === 0 ? "짝" : "홀"
);

console.log(parity);

const evenNumbers = numbers.filter(
  value => value % 2 === 0
);

console.log(evenNumbers);

const descending = [...numbers].sort(
  (a, b) => b - a
);

console.log(descending);
console.log(numbers);
```

---

# 92. 중복 없는 로또 확장 예제

```js
const lottoNumbers = [];

while (lottoNumbers.length < 6) {
  const number =
    Math.floor(Math.random() * 45) + 1;

  if (!lottoNumbers.includes(number)) {
    lottoNumbers.push(number);
  }
}

lottoNumbers.sort((a, b) => a - b);

console.log(lottoNumbers);
```

`while`, `includes()`, `push()`는 뒤 단원 또는 배열 확장 학습으로 볼 수 있습니다.

---

# 93. 피라미드 통합 개선 예제

```js
const input =
  prompt("피라미드 줄 수를 입력하세요.");

if (input === null) {
  console.log("입력을 취소했습니다.");
} else if (input.trim() === "") {
  console.log("줄 수를 입력하세요.");
} else {
  const rows = Number(input);

  if (
    !Number.isInteger(rows) ||
    rows < 1 ||
    rows > 20
  ) {
    console.log("1~20 사이 정수를 입력하세요.");
  } else {
    for (let row = 1; row <= rows; row++) {
      let line = "";

      for (
        let blank = 1;
        blank <= rows - row;
        blank++
      ) {
        line += "_";
      }

      for (
        let mark = 1;
        mark <= 2 * row - 1;
        mark++
      ) {
        line += "+";
      }

      for (
        let blank = 1;
        blank <= rows - row;
        blank++
      ) {
        line += "_";
      }

      console.log(line);
    }
  }
}
```

---

# 94. 자주 하는 실수

## 94.1 For 괄호에 세미콜론 세 개 작성

```js
for (초기화; 조건; 증감;)
```

가 아니라 구분 세미콜론은 두 개입니다.

## 94.2 감소 반복에서 증감 방향 반대로 작성

종료되지 않거나 한 번도 실행되지 않을 수 있습니다.

## 94.3 누적 변수 초기화 누락

`undefined + 숫자`가 NaN이 될 수 있습니다.

## 94.4 반복문 밖의 변수를 이전 값 그대로 재사용

합계를 다시 계산하기 전에 `sum = 0`이 필요합니다.

## 94.5 중첩 반복문의 전체 실행 횟수 과소평가

바깥 횟수와 안쪽 횟수를 곱해야 합니다.

## 94.6 Break가 모든 중첩 반복을 끝낸다고 생각

현재 가장 가까운 반복문만 종료합니다.

## 94.7 Continue 뒤 코드도 실행된다고 생각

현재 회차의 나머지 코드는 건너뜁니다.

## 94.8 배열 값 순회에 For In을 무조건 사용

`for...in`은 속성 키 순회입니다.

## 94.9 ForEach가 새 배열을 반환한다고 생각

반환값은 undefined입니다.

## 94.10 Map 자체가 Undefined라고 생각

map은 새 배열을 반환하며, callback return이 없으면 각 요소가 undefined가 됩니다.

## 94.11 Sort가 새 배열만 만든다고 생각

기존 배열을 직접 변경합니다.

## 94.12 피라미드 반복 변수 선언 누락

```js
for (k = 1; ...)
```

는 전역 오염 또는 strict mode 오류를 만들 수 있습니다.

## 94.13 줄마다 String 초기화 누락

이전 줄이 계속 누적됩니다.

## 94.14 Prompt 값을 검증 없이 반복 횟수로 사용

취소, 빈 값, 문자, 음수, 지나치게 큰 수를 처리해야 합니다.

---

# 95. 면접·복습 포인트

## Q1. For문의 실행 순서는 무엇인가요?

초기화식이 한 번 실행된 뒤 조건식, 실행 블록, 증감식 순으로 반복하고 조건이 false가 되면 종료합니다.

## Q2. 누적 합계와 개수 집계의 차이는 무엇인가요?

합계는 조건에 맞는 값 자체를 더하고, 개수는 조건을 만족할 때마다 1을 증가시킵니다.

## Q3. 중첩 반복문의 실행 횟수는 어떻게 계산하나요?

각 반복문의 횟수가 고정이라면 바깥 반복 횟수와 안쪽 반복 횟수를 곱합니다.

## Q4. Break와 Continue의 차이는 무엇인가요?

break는 반복문을 종료하고, continue는 현재 회차의 남은 코드를 건너뛰고 다음 회차로 이동합니다.

## Q5. 중첩 반복문을 두 단계 모두 종료하려면 어떻게 하나요?

flag를 사용해 바깥 반복에서도 break하거나, 상황에 따라 label문 또는 함수 반환을 사용할 수 있습니다.

## Q6. For In과 For Of의 차이는 무엇인가요?

for...in은 속성 키를 순회하고, for...of는 iterable의 값을 순회합니다.

## Q7. ForEach의 반환값은 무엇인가요?

undefined입니다.

## Q8. Map과 Filter의 차이는 무엇인가요?

map은 각 요소를 변환해 같은 길이의 새 배열을 만들고, filter는 조건을 만족한 요소만 모아 새 배열을 만듭니다.

## Q9. Sort 비교 함수에서 음수를 반환하면 어떻게 되나요?

첫 번째 인수를 두 번째 인수보다 앞에 배치합니다.

## Q10. Sort의 중요한 부작용은 무엇인가요?

원본 배열의 순서를 직접 변경합니다.

## Q11. 피라미드에서 `2 * row - 1`은 무엇을 의미하나요?

각 줄의 Plus 개수를 1, 3, 5, 7처럼 홀수로 증가시키는 공식입니다.

## Q12. 내 피라미드 코드의 선언 없는 k가 위험한 이유는 무엇인가요?

느슨한 script에서는 전역 오염을 만들고 strict mode에서는 ReferenceError가 발생하기 때문입니다.

---

# Problems

## 문제 1. 1부터 10 출력

for문으로 1부터 10까지 출력하세요.

## 문제 2. 10부터 1 출력

for문으로 10부터 1까지 역순으로 출력하세요.

## 문제 3. 1부터 100 합계

1부터 100까지 합계를 구하세요.

## 문제 4. 짝수 합계

1부터 20까지 짝수의 합계를 구하세요.

## 문제 5. 홀수 개수

1부터 30까지 홀수의 개수를 구하세요.

## 문제 6. 3단 구구단

3단을 1부터 9까지 출력하세요.

## 문제 7. 전체 구구단

2단부터 9단까지 중첩 반복문으로 출력하세요.

## 문제 8. 주사위 한 개

주사위 한 개의 모든 결과를 출력하세요.

## 문제 9. 주사위 두 개

주사위 두 개의 36가지 순서 있는 결과를 출력하세요.

## 문제 10. 합이 7인 주사위

주사위 두 개의 합이 7인 조합만 출력하세요.

## 문제 11. Break

1부터 100까지 반복하되 21에 도달하면 종료하세요.

## 문제 12. Continue

1부터 20까지 홀수만 출력하도록 짝수를 건너뛰세요.

## 문제 13. 중첩 반복 종료

4층, 층마다 10자리인 주차장에서 27번째 자리를 찾으면 두 반복을 모두 종료하세요.

## 문제 14. For Of

배열 `[10, 20, 30]`의 값을 for...of로 출력하세요.

## 문제 15. Entries

배열 `["A", "B", "C"]`의 index와 값을 함께 출력하세요.

## 문제 16. ForEach

배열 `[2, 4, 6]`의 각 값과 index를 forEach로 출력하고 forEach 반환값도 확인하세요.

## 문제 17. Map

배열 `[1, 2, 3, 4]`를 `["홀", "짝", "홀", "짝"]`으로 변환하세요.

## 문제 18. Filter

영화 제목 배열에서 길이가 4 이상인 제목만 새 배열로 만드세요.

## 문제 19. Sort

숫자 배열 `[2, 14, 4, 3]`을 오름차순과 내림차순으로 각각 정렬하되 원본 배열은 유지하세요.

## 문제 20. 증가 피라미드

다음을 출력하세요.

```text
+
++
+++
++++
+++++
```

## 문제 21. 중앙 피라미드

5줄 기준 다음 패턴을 출력하세요.

```text
____+____
___+++___
__+++++__
_+++++++_
+++++++++
```

## 문제 22. 종합 데이터 처리

다음 요구사항을 만족하세요.

- 배열 `[3, 8, 11, 14, 20, 25]`
- 각 값의 index와 값을 출력
- 짝수만 새 배열로 필터링
- 필터링한 값을 2배로 변환
- 내림차순 정렬
- 원본 배열은 변경하지 않음
- 최종 합계를 for문으로 계산
- 결과 배열과 합계 출력

---

# Answers & Explanations

## 정답 1

```js
for (let i = 1; i <= 10; i++) {
  console.log(i)
}
```

## 정답 2

```js
for (let i = 10; i >= 1; i--) {
  console.log(i)
}
```

## 정답 3

```js
let sum = 0

for (let i = 1; i <= 100; i++) {
  sum += i
}

console.log(sum)
```

결과는 5050입니다.

## 정답 4

```js
let sum = 0

for (let i = 1; i <= 20; i++) {
  if (i % 2 === 0) {
    sum += i
  }
}

console.log(sum)
```

결과는 110입니다.

## 정답 5

```js
let count = 0

for (let i = 1; i <= 30; i++) {
  if (i % 2 !== 0) {
    count++
  }
}

console.log(count)
```

결과는 15입니다.

## 정답 6

```js
for (let i = 1; i <= 9; i++) {
  console.log(`3 x ${i} = ${3 * i}`)
}
```

## 정답 7

```js
for (let dan = 2; dan <= 9; dan++) {
  for (let number = 1; number <= 9; number++) {
    console.log(
      `${dan} x ${number} = ${dan * number}`
    )
  }
}
```

## 정답 8

```js
for (let dice = 1; dice <= 6; dice++) {
  console.log(dice)
}
```

## 정답 9

```js
for (let dice1 = 1; dice1 <= 6; dice1++) {
  for (let dice2 = 1; dice2 <= 6; dice2++) {
    console.log(`[${dice1}, ${dice2}]`)
  }
}
```

## 정답 10

```js
for (let dice1 = 1; dice1 <= 6; dice1++) {
  for (let dice2 = 1; dice2 <= 6; dice2++) {
    if (dice1 + dice2 === 7) {
      console.log(`[${dice1}, ${dice2}]`)
    }
  }
}
```

## 정답 11

```js
for (let i = 1; i <= 100; i++) {
  if (i === 21) {
    break
  }

  console.log(i)
}
```

1부터 20까지 출력합니다.

## 정답 12

```js
for (let i = 1; i <= 20; i++) {
  if (i % 2 === 0) {
    continue
  }

  console.log(i)
}
```

## 정답 13

```js
let count = 0
let found = false

for (let floor = 1; floor <= 4; floor++) {
  for (let seat = 1; seat <= 10; seat++) {
    count++

    if (count === 27) {
      console.log(
        `${floor}층 ${seat}번째 자리`
      )

      found = true
      break
    }
  }

  if (found) {
    break
  }
}
```

## 정답 14

```js
const values = [10, 20, 30]

for (const value of values) {
  console.log(value)
}
```

## 정답 15

```js
const values = ["A", "B", "C"]

for (const [index, value] of values.entries()) {
  console.log(index, value)
}
```

## 정답 16

```js
const values = [2, 4, 6]

const result = values.forEach(
  (value, index) => {
    console.log(value, index)
  }
)

console.log(result)
```

마지막 결과는 undefined입니다.

## 정답 17

```js
const values = [1, 2, 3, 4]

const result = values.map(
  value =>
    value % 2 === 0
      ? "짝"
      : "홀"
)

console.log(result)
```

## 정답 18

```js
const movies = [
  "호프",
  "스파이더맨-브랜드 뉴 데이",
  "오디세이",
  "모아나"
]

const result = movies.filter(
  title => title.length >= 4
)

console.log(result)
```

## 정답 19

```js
const numbers = [2, 14, 4, 3]

const ascending =
  [...numbers].sort((a, b) => a - b)

const descending =
  [...numbers].sort((a, b) => b - a)

console.log(ascending)
console.log(descending)
console.log(numbers)
```

## 정답 20

```js
for (let row = 1; row <= 5; row++) {
  let line = ""

  for (let count = 1; count <= row; count++) {
    line += "+"
  }

  console.log(line)
}
```

## 정답 21

```js
const rows = 5

for (let row = 1; row <= rows; row++) {
  let line = ""

  for (
    let blank = 1;
    blank <= rows - row;
    blank++
  ) {
    line += "_"
  }

  for (
    let mark = 1;
    mark <= 2 * row - 1;
    mark++
  ) {
    line += "+"
  }

  for (
    let blank = 1;
    blank <= rows - row;
    blank++
  ) {
    line += "_"
  }

  console.log(line)
}
```

## 정답 22

```js
const source = [3, 8, 11, 14, 20, 25]

for (
  const [index, value]
  of source.entries()
) {
  console.log(index, value)
}

const result = source
  .filter(value => value % 2 === 0)
  .map(value => value * 2)
  .sort((a, b) => b - a)

let sum = 0

for (const value of result) {
  sum += value
}

console.log("원본:", source)
console.log("결과:", result)
console.log("합계:", sum)
```

결과 배열:

```text
[40, 28, 16]
```

합계:

```text
84
```

---

# Final Checklist

## For 기본

- [ ] 초기화식, 조건식, 증감식을 구분했다.
- [ ] for문의 실행 순서를 설명할 수 있다.
- [ ] 조건이 false일 때 반복이 종료됨을 이해했다.
- [ ] 증가 반복과 감소 반복을 작성했다.
- [ ] 시작값과 증감 방향이 종료 조건과 맞는지 확인했다.
- [ ] 반복 변수의 블록 스코프를 이해했다.
- [ ] 무한 반복이 생기지 않는지 확인했다.

## 누적과 조건

- [ ] 합계 변수에 0을 초기값으로 넣었다.
- [ ] 개수 변수와 합계 변수를 구분했다.
- [ ] 홀짝 판별에 나머지 연산자를 사용했다.
- [ ] 숫자 비교에 엄격 비교를 사용했다.
- [ ] 반복문 안의 조건 실행 횟수를 추적했다.

## 중첩 반복문

- [ ] 바깥 반복과 안쪽 반복의 역할을 구분했다.
- [ ] 전체 실행 횟수를 계산했다.
- [ ] 구구단 전체를 출력할 수 있다.
- [ ] 주사위 두 개의 36가지 결과를 생성했다.
- [ ] 합별 조합을 만들 수 있다.
- [ ] 순서 있는 결과와 중복 제거 조합을 구분했다.

## Break와 Continue

- [ ] break가 현재 반복문을 즉시 종료함을 이해했다.
- [ ] continue가 현재 회차만 건너뜀을 이해했다.
- [ ] 중첩 반복에서 안쪽 break만으로 바깥 반복이 종료되지 않음을 확인했다.
- [ ] flag 변수를 이용해 바깥 반복도 종료했다.
- [ ] break 직전 불필요한 증감문을 작성하지 않았다.
- [ ] 정확한 값보다 범위 조건이 안전한 상황을 구분했다.

## 배열 순회

- [ ] for...in이 키를 순회함을 이해했다.
- [ ] for...of가 값을 순회함을 이해했다.
- [ ] 배열 index와 값이 모두 필요하면 entries를 검토했다.
- [ ] forEach 콜백 인수 세 개를 구분했다.
- [ ] forEach 반환값이 undefined임을 확인했다.
- [ ] map이 같은 길이의 새 배열을 반환함을 이해했다.
- [ ] map callback에서 return이 없으면 해당 자리가 undefined가 됨을 이해했다.
- [ ] filter가 조건을 만족한 요소만 반환함을 이해했다.
- [ ] sort 비교 함수의 음수·양수 의미를 이해했다.
- [ ] sort가 원본 배열을 변경한다는 점을 확인했다.

## 피라미드 패턴

- [ ] 바깥 반복이 줄 수를 담당함을 이해했다.
- [ ] 안쪽 반복이 문자 개수를 담당함을 이해했다.
- [ ] 각 줄 시작 전에 문자열을 초기화했다.
- [ ] `row`, `rows - row`, `2 * row - 1` 규칙을 설명할 수 있다.
- [ ] 반복 변수를 let으로 선언했다.
- [ ] 입력 줄 수를 Number로 변환했다.
- [ ] 취소, 빈 값, 정수가 아닌 값, 음수를 검증했다.
- [ ] 너무 큰 입력에 최대 범위를 적용할 수 있다.

## 원본 코드 검수

- [ ] `04_for.html`과 `04_1_pyramid.html`을 함께 분석했다.
- [ ] 내 코드에만 추가 피라미드 복습 파일이 있음을 기록했다.
- [ ] 추가 파일의 한글 파일명이 깨져 정확한 이름을 단정하지 않았다.
- [ ] 내 for 문법 주석의 불필요한 세미콜론을 기록했다.
- [ ] 내 문제 3 번호 중복을 기록했다.
- [ ] 강사님 주차장 코드의 불필요한 `j++`를 기록했다.
- [ ] 양쪽 로또 코드에 중복 가능성이 있음을 기록했다.
- [ ] `for...in` 배열 사용 주의점을 설명했다.
- [ ] forEach 네 번째 인수가 undefined임을 설명했다.
- [ ] 강사님 map 결과 `undefined` 주석 오류를 기록했다.
- [ ] 내 코드의 `retrurn` 오타를 기록했다.
- [ ] sort 설명의 부정확한 표현을 보완했다.
- [ ] sort의 원본 배열 변경을 설명했다.
- [ ] 내 피라미드 파일의 선언 없는 `k`를 기록했다.
- [ ] 강사님 피라미드 5·6·8~12단계가 미완성임을 기록했다.
- [ ] 내 코드가 해당 단계를 완성했음을 기록했다.
- [ ] prompt 피라미드 입력 검증 누락을 기록했다.

---

# Key Summary

- for문은 초기화식, 조건식, 실행 블록, 증감식 순으로 반복한다.
- 초기화식은 처음 한 번만 실행되고 조건식은 매 회차 전에 검사된다.
- 증가 반복과 감소 반복은 시작값·조건·증감 방향이 서로 맞아야 한다.
- 누적 합계는 초기값 0에서 값을 계속 더한다.
- 개수 집계는 조건을 만족할 때마다 count를 1 증가시킨다.
- 내 원본은 홀수 개수와 주사위 하나를 모두 문제 3으로 표시해 번호가 중복된다.
- 중첩 반복문의 전체 횟수는 보통 바깥 횟수와 안쪽 횟수를 곱한다.
- 전체 구구단은 8개 단 × 9회로 72번 출력한다.
- 주사위 두 개의 순서 있는 결과는 36가지다.
- 합 2~12별 모든 조합을 만들려면 목표 합 반복과 두 주사위 반복을 중첩할 수 있다.
- 두 주사위를 구분하면 [1,2]와 [2,1]은 다른 결과다.
- 원본 로또 코드는 1~45 숫자를 6번 만들지만 중복을 제거하지 않는다.
- break는 현재 반복문을 종료하고 continue는 현재 회차만 건너뛴다.
- 중첩 반복에서 안쪽 break는 바깥 반복을 종료하지 않는다.
- flag는 안쪽에서 찾은 상태를 바깥 반복에 전달할 수 있다.
- 강사님 주차장 코드의 break 직전 `j++`는 불필요하다.
- for...in은 키를, for...of는 값을 순회한다.
- 배열 값 순회에는 for...of가 더 자연스러운 경우가 많다.
- forEach는 각 요소에 작업을 수행하지만 반환값은 undefined다.
- forEach callback의 표준 인수는 현재 값, index, 배열 전체 세 개다.
- map은 각 요소의 return 값으로 같은 길이의 새 배열을 만든다.
- 강사님 코드의 `console.log(r2) // undefined` 주석은 잘못이다.
- map callback에 return이 없으면 map 자체가 undefined가 아니라 각 결과 요소가 undefined가 된다.
- filter는 조건을 만족한 원본 요소만 새 배열로 만든다.
- sort의 비교 함수가 음수면 첫 번째 값을 앞에, 양수면 뒤에 배치한다.
- sort는 원본 배열을 직접 변경한다.
- 화살표 함수는 매개변수 하나와 표현식 하나일 때 괄호와 중괄호를 생략할 수 있다.
- 피라미드에서 바깥 반복은 줄, 안쪽 반복은 한 줄의 문자 개수를 담당한다.
- 각 줄을 출력하기 전에 누적 문자열을 빈 문자열로 초기화해야 한다.
- 증가 피라미드의 문자 수는 row, 여백은 rows-row로 표현할 수 있다.
- 중앙 피라미드의 기호 개수는 `2 * row - 1`이다.
- 내 `04_1_pyramid.html`의 `for(k=...)`는 선언 없는 할당 문제를 만든다.
- 내 코드는 피라미드 5·6·8~12단계를 완성했지만 강사님 코드는 해당 단계가 미완성이다.
- 내 코드에만 피라미드 복습 파일이 하나 더 있으며 파일명 한글이 깨져 정확한 이름은 확인하기 어렵다.
- prompt로 받은 줄 수는 문자열이므로 명시적 숫자 변환과 유효성 검증이 필요하다.
