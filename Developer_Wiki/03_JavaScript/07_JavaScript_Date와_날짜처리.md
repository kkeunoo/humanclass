# JavaScript Date와 날짜 처리

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `07_JavaScript_Date와_날짜처리.md` |
| 분류 | `03_JavaScript` |
| 권장 선수 학습 | `06_JavaScript_배열과_배열메서드.md` |
| 다음 학습 | `08_JavaScript_객체.md` |
| 원본 기준 | `workspace_me/workspace/workspace_html/javascript/07_date.html`, `workspace_teacher/workspace_teacher/workspace_html/javascript/07_date.html` |
| 핵심 범위 | `Date`, 현재 시각, 연·월·일·시·분·초, `getFullYear()`, `getMonth()`, `getDate()`, `getHours()`, `getMinutes()`, `getSeconds()`, `toISOString()`, 문자열 분리, timestamp, `getTime()`, 실행 시간 측정, 특정 날짜 생성, `setHours()` |
| 프로젝트 연결 | 게시물 작성 시각, 예약 날짜, 로그 기록, 경과 시간 측정, 날짜 문자열 출력, 서버와 UTC 데이터 교환 |

> 이 문서는 내 코드와 강사님 코드의 `07_date.html`을 직접 비교해 작성했습니다. 두 파일의 핵심 학습 흐름은 거의 같지만, 내 코드에는 날짜 메서드 설명, UTC·timestamp 설명, 실행 시간 기준에 대한 개인 주석, `time.setHours(time.getHours() + 9)` 호출이 추가되어 있습니다. 원본 코드의 실행 결과는 실행한 시각과 컴퓨터 시간대에 따라 달라지므로 고정된 현재 날짜나 숫자를 임의로 작성하지 않습니다.

---

# 학습 목표

- `Date` 객체가 날짜와 시각을 다루는 내장 객체임을 이해한다.
- `new Date()`로 현재 날짜와 시각을 생성한다.
- 연·월·일·시·분·초를 각각 추출한다.
- `getMonth()`가 0부터 11까지 반환한다는 점을 이해한다.
- `getDate()`와 요일 관련 메서드를 혼동하지 않는다.
- 로컬 시간 메서드와 UTC 기반 ISO 문자열의 차이를 이해한다.
- `toISOString()` 결과에서 날짜 부분을 추출한다.
- `getTime()`으로 Unix epoch 이후 밀리초를 구한다.
- 두 timestamp의 차이로 코드 실행 시간을 측정한다.
- 반복 조건 `< 1000`과 `<= 1000`의 실행 횟수 차이를 계산한다.
- 날짜 문자열로 특정 날짜를 생성한다.
- `setHours()`가 기존 Date 객체를 직접 변경한다는 점을 이해한다.
- 내 코드의 연속된 두 `setHours()` 호출이 어떤 결과를 만드는지 설명한다.
- 날짜 처리에서 로컬 시간대와 UTC를 명확히 구분한다.
- 원본에 없는 확장 지식은 원본 분석과 구분해 학습한다.

---

# 1. Date 객체란?

JavaScript의 `Date`는 날짜와 시각을 표현하는 내장 객체입니다.

```js
const now = new Date()
```

인수를 전달하지 않으면 코드가 실행된 현재 시각을 기준으로 Date 객체를 만듭니다.

```js
console.log(now)
```

Console에 표시되는 형식은 브라우저와 개발자 도구 환경에 따라 달라질 수 있습니다.

---

# 2. 원본 문서 구조

두 원본 모두 HTML 문서의 `<head>` 안에서 내부 `<script>`를 실행합니다.

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
    // Date 실습
  </script>
</head>
<body>
</body>
</html>
```

본문에는 표시 요소가 없습니다.

모든 결과는 개발자 도구 Console에서 확인합니다.

---

# 3. 문서 언어와 제목

공통 원본:

```html
<html lang="en">
<title>Document</title>
```

한국어 학습 문서이므로 다음처럼 개선할 수 있습니다.

```html
<html lang="ko">
<title>JavaScript Date와 날짜 처리</title>
```

JavaScript 실행 결과에는 영향을 주지 않지만 문서 의미와 접근성을 개선합니다.

---

# 4. 현재 날짜와 시각 생성

공통 원본:

```js
const now = new Date()
console.log(now)
```

`now`에는 코드 실행 시점의 날짜와 시각이 들어갑니다.

중요:

```text
문서를 열 때마다 값이 달라질 수 있다.
컴퓨터의 시간 설정과 시간대에 영향을 받는다.
```

따라서 현재 날짜를 문서에 고정된 정답으로 적지 않습니다.

---

# 5. 내 코드의 추가 설명

내 코드:

```js
// now를 썼을 때 표시하기 위한 양식
```

이 주석 아래에서 Date 객체 전체를 직접 출력하는 대신 연·월·일·시·분·초를 각각 꺼내는 메서드를 실습합니다.

Date 객체는 하나의 날짜·시각을 담고 있으며 메서드를 사용해 필요한 부분만 추출할 수 있습니다.

---

# 6. 연도 GetFullYear

공통 원본:

```js
const y = now.getFullYear()
console.log("년 :", y)
```

`getFullYear()`는 로컬 시간 기준 연도를 숫자로 반환합니다.

예:

```text
2026
```

과거에 사용되던 `getYear()`와 혼동하지 않습니다.

연도는 `getFullYear()`를 사용합니다.

---

# 7. 월 GetMonth

공통 원본:

```js
const M = now.getMonth()
console.log("월 :", M + 1)
```

`getMonth()`의 범위:

```text
0~11
```

대응:

```text
0 → 1월
1 → 2월
...
11 → 12월
```

사람이 사용하는 월 번호로 출력하려면 1을 더합니다.

---

# 8. 내 코드의 월 설명

내 코드:

```js
// 월(0~11까지 나옴, 배열과 같이)
```

배열 index처럼 0부터 시작한다는 점을 연결한 설명입니다.

강사님 코드:

```js
// 월(0~11) 주의!!
```

두 코드 모두 `M + 1`로 실제 월을 출력합니다.

---

# 9. 월에서 자주 하는 실수

잘못된 출력:

```js
console.log(now.getMonth())
```

7월에 실행하면 6이 나옵니다.

개선:

```js
const month =
  now.getMonth() + 1

console.log(month)
```

반대로 Date 생성자에 숫자로 월을 전달할 때도 0부터 시작하는 규칙이 적용될 수 있으므로 주의합니다.

---

# 10. 일 GetDate

공통 원본:

```js
const d = now.getDate()
console.log("일 :", d)
```

`getDate()`는 현재 월의 날짜를 반환합니다.

범위:

```text
1~31
```

월에 따라 실제 최대 날짜는 달라집니다.

---

# 11. GetDate와 GetDay 구분

`getDate()`:

```text
월의 몇 일인지
```

`getDay()`:

```text
요일 index
0~6
```

원본은 `getDate()`만 사용합니다.

날짜와 요일은 이름이 비슷하므로 구분해야 합니다.

---

# 12. 시 GetHours

공통 원본:

```js
const h = now.getHours()
console.log("시 :", h)
```

`getHours()`는 로컬 시간 기준 시각을 반환합니다.

범위:

```text
0~23
```

24시간제를 사용합니다.

---

# 13. 분 GetMinutes

공통 원본:

```js
const m = now.getMinutes()
console.log("분 :", m)
```

범위:

```text
0~59
```

한 자리 값도 숫자로 반환하므로 5분은 `"05"`가 아니라 숫자 `5`입니다.

두 자리 문자열이 필요하면 별도 형식화가 필요합니다.

---

# 14. 초 GetSeconds

공통 원본:

```js
const s = now.getSeconds()
console.log("초 :", s)
```

범위:

```text
0~59
```

Date 객체에는 밀리초도 저장됩니다.

확장 메서드:

```js
now.getMilliseconds()
```

원본은 초까지만 개별 출력합니다.

---

# 15. 로컬 시간 추출 메서드

원본에서 사용하는 메서드:

| 목적 | 메서드 | 범위·형식 |
| --- | --- | --- |
| 연도 | `getFullYear()` | 네 자리 연도 |
| 월 | `getMonth()` | 0~11 |
| 일 | `getDate()` | 1~31 |
| 시 | `getHours()` | 0~23 |
| 분 | `getMinutes()` | 0~59 |
| 초 | `getSeconds()` | 0~59 |

이 메서드들은 로컬 시간 기준입니다.

---

# 16. ISO 문자열

공통 원본:

```js
const iso = now.toISOString()

console.log(iso)
```

형식:

```text
YYYY-MM-DDTHH:mm:ss.sssZ
```

예시 형태:

```text
2026-07-28T06:30:15.123Z
```

이 예시는 형식 설명일 뿐 원본 실행 시각을 뜻하지 않습니다.

---

# 17. 내 코드의 ISO 설명 검토

내 코드:

```text
년-월-일T시:분:초.밀리세컨드
iso는 영국시간 UTC세계협정시 기준
```

형식 설명의 핵심은 맞습니다.

다만 UTC를 단순히 “영국시간”이라고만 설명하면 부정확할 수 있습니다.

정확한 표현:

```text
toISOString()은 UTC 기준 문자열을 반환한다.
UTC는 국제적으로 사용하는 협정 세계시 기준이다.
```

영국의 현지 시각은 계절에 따라 UTC와 같지 않을 수 있습니다.

---

# 18. ISO의 Z

ISO 문자열 끝의 `Z`는 UTC 기준임을 나타냅니다.

```text
2026-07-28T06:30:15.123Z
```

로컬 시간이 한국 표준시라면 같은 순간의 로컬 시각과 ISO 시각은 시(hour)가 다르게 보일 수 있습니다.

두 값은 다른 순간이 아니라 같은 순간을 다른 시간대 기준으로 표현한 것입니다.

---

# 19. ISO에서 날짜만 추출

공통 원본:

```js
console.log(
  iso.split("T")[0]
)
```

실행 과정:

```text
"날짜T시간"
→ "T" 기준으로 배열 분리
→ index 0의 날짜 부분 선택
```

결과 형식:

```text
YYYY-MM-DD
```

---

# 20. 내 코드의 주석 처리된 대안

내 코드:

```js
// let date = iso.split('T')
// console.log(date[0])
```

한 줄로 바로 출력하는 코드와 같은 결과입니다.

```js
const parts =
  iso.split("T")

console.log(parts[0])
```

중간 결과를 확인하려면 변수로 나누는 방식이 학습에 도움이 됩니다.

---

# 21. ISO 날짜와 로컬 날짜 차이

`toISOString()`은 UTC 기준입니다.

따라서 로컬 시간이 자정 근처이면:

```text
로컬 날짜
UTC 날짜
```

가 서로 다를 수 있습니다.

예를 들어 한국에서 이른 오전에는 UTC 기준으로 전날일 수 있습니다.

로컬 화면에 오늘 날짜를 출력하려는 목적이라면 `getFullYear()`, `getMonth()`, `getDate()`로 조합하는 방법을 검토합니다.

---

# 22. Timestamp

공통 원본:

```js
const timestamp = now.getTime()

console.log(timestamp)
```

`getTime()`은 1970년 1월 1일 00:00:00 UTC부터 해당 Date 시점까지의 밀리초 수를 반환합니다.

일반적으로 Unix epoch 기반 timestamp라고 설명합니다.

---

# 23. 내 코드의 Timestamp 설명

내 코드:

```text
1970년도 1월 1일 00시 00분 00초(UTC)부터
현재까지 흐른 밀리초의 총합
```

핵심적으로 맞습니다.

내 코드에는 특정 숫자 예시도 들어 있습니다.

```text
1783667295초
970밀리초
1783667295970
```

이 숫자는 실행 시점의 `now`와 항상 일치하는 고정값이 아닙니다.

설명용 예시로만 보존합니다.

---

# 24. Millisecond 단위

```text
1초 = 1000밀리초
```

timestamp 차이:

```js
const difference =
  after - before
```

결과 단위도 밀리초입니다.

초로 바꾸려면:

```js
difference / 1000
```

---

# 25. Date Now 확장

원본:

```js
new Date().getTime()
```

같은 목적의 더 간단한 표현:

```js
Date.now()
```

둘 다 현재 시각의 timestamp를 숫자로 구할 수 있습니다.

원본은 Date 객체와 `getTime()` 연결을 학습하기 위해 긴 형태를 사용합니다.

---

# 26. 실행 시간 측정

공통 원본:

```js
const before =
  new Date().getTime()

for (...) {
  console.log(i)
}

const after =
  new Date().getTime()

console.log(
  "after - before :",
  after - before
)
```

코드 실행 전후의 timestamp 차이를 계산합니다.

---

# 27. 강사님 반복 횟수

강사님 코드:

```js
for (let i = 0; i < 1000; i++) {
  console.log(i)
}
```

출력 범위:

```text
0~999
```

실행 횟수:

```text
1000회
```

---

# 28. 내 코드 반복 횟수

내 코드:

```js
for (let i = 0; i <= 1000; i++) {
  console.log(i)
}
```

출력 범위:

```text
0~1000
```

실행 횟수:

```text
1001회
```

두 코드의 중요한 실제 차이입니다.

---

# 29. 실행 시간 비교 시 주의

두 원본은 반복 횟수가 다르므로 측정값을 직접 비교하기 어렵습니다.

```text
내 코드 → 1001회
강사님 코드 → 1000회
```

또한 `console.log()`는 환경에 따라 비용이 크며 개발자 도구 상태에도 영향을 받습니다.

따라서 이 예제는 정밀 성능 측정보다 전후 시각 차이 계산 원리를 익히는 용도입니다.

---

# 30. 내 코드의 20ms 설명 검토

내 코드:

```text
보통 20ms 이하는 우연히 벌어질 수 있고
이상의 경우 느림이 있을 수 있음
```

이 기준은 원본 개인 메모로 보존합니다.

하지만 모든 코드와 장치에 적용되는 보편적 성능 기준으로 볼 수 없습니다.

실행 시간은 다음에 따라 달라집니다.

- 장치 성능
- 브라우저
- 개발자 도구
- Console 출력량
- 백그라운드 작업
- 반복 횟수

따라서 20ms만으로 느림을 단정하지 않습니다.

---

# 31. 정밀 측정 확장

브라우저에서는 더 정밀한 시간 측정에 다음을 사용할 수 있습니다.

```js
const before = performance.now()

// 측정할 코드

const after = performance.now()

console.log(after - before)
```

원본은 `Date.getTime()`을 사용합니다.

`performance.now()`는 원본 외 확장 학습입니다.

---

# 32. 특정 날짜 생성

공통 원본:

```js
let time =
  new Date("2026-06-29")

console.log(
  time.toISOString()
)
```

문자열을 인수로 전달해 특정 날짜의 Date 객체를 생성합니다.

---

# 33. 날짜 전용 문자열 해석 주의

`"2026-06-29"`처럼 시간대 정보가 없는 날짜 전용 ISO 형식은 UTC 자정 기준으로 해석될 수 있습니다.

```text
2026-06-29T00:00:00.000Z
```

로컬 시간대에서 객체를 출력하면 날짜와 시각이 다르게 보일 수 있습니다.

날짜 문자열 파싱 규칙은 입력 형식에 따라 달라질 수 있으므로 명확한 형식을 사용해야 합니다.

---

# 34. 로컬 날짜 생성 확장

로컬 시간 기준 2026년 6월 29일 자정을 명확히 만들려면 숫자 인수를 사용할 수 있습니다.

```js
const time =
  new Date(2026, 5, 29)
```

월은 0부터 시작하므로 6월은 숫자 5입니다.

이 방식은 원본 외 확장 예제입니다.

---

# 35. Setter 메서드

내 코드:

```text
보편적으로 get이 있다면 set도 있는 경우가 많음
```

Date에는 값을 읽는 getter와 값을 변경하는 setter가 여러 개 있습니다.

예:

```text
getHours() ↔ setHours()
getDate() ↔ setDate()
getMonth() ↔ setMonth()
getFullYear() ↔ setFullYear()
```

모든 getter와 setter의 이름이 완전히 일대일 대응한다고 단정하기보다 Date API별로 확인합니다.

---

# 36. SetHours 기본

원본의 주석 처리 예:

```js
// time.setHours(10)
```

해당 Date 객체의 로컬 시간 시(hour)를 10으로 설정합니다.

`setHours()`는 새로운 Date 객체를 반환하는 것이 아니라 기존 객체를 변경합니다.

반환값은 변경된 시점의 timestamp입니다.

---

# 37. 강사님 SetHours

강사님 코드:

```js
time.setHours(
  now.getHours() + 9
)

console.log(
  time.toISOString()
)
```

`time`의 날짜를 유지하면서 시(hour)를 현재 로컬 시각의 시 + 9로 설정합니다.

주의:

- 분·초·밀리초는 `time`에 남아 있는 값의 영향을 받습니다.
- 시가 범위를 넘으면 날짜가 자동으로 조정될 수 있습니다.
- ISO 출력은 다시 UTC 기준입니다.

---

# 38. 내 코드의 첫 번째 SetHours

내 코드에는 강사님 코드에 없는 다음 문장이 먼저 있습니다.

```js
time.setHours(
  time.getHours() + 9
)
```

`time` 객체 자신의 로컬 시각에 9시간을 더합니다.

이 호출 직후라면 “기존 time에서 9시간 뒤”에 가까운 결과를 만듭니다.

---

# 39. 내 코드의 두 번째 SetHours

바로 다음 줄:

```js
time.setHours(
  now.getHours() + 9
)
```

이 문장은 앞에서 더한 시간을 다시 기준으로 더하는 것이 아닙니다.

`time`의 시(hour)를 `now.getHours() + 9` 값으로 다시 설정합니다.

따라서 첫 번째 `setHours()`의 시 설정은 두 번째 호출에 의해 덮어쓰여집니다.

---

# 40. 두 SetHours의 실제 영향

내 코드:

```js
time.setHours(time.getHours() + 9)
time.setHours(now.getHours() + 9)
```

흐름:

```text
1. time 자신의 시에 9시간 추가
2. time의 시를 현재 now의 시 + 9로 다시 설정
```

최종 결과는 두 번째 호출의 영향을 크게 받습니다.

첫 번째 호출은 날짜 rollover가 발생했다면 날짜 부분에 흔적을 남길 가능성이 있지만, 단순히 “18시간을 더했다”고 해석하면 안 됩니다.

---

# 41. 시간 더하기와 시간 설정 차이

시간을 9시간 더하려는 목적:

```js
time.setTime(
  time.getTime() +
  9 * 60 * 60 * 1000
)
```

또는:

```js
time.setHours(
  time.getHours() + 9
)
```

현재 시각의 시(hour) 값으로 교체하려는 목적:

```js
time.setHours(
  now.getHours() + 9
)
```

두 목적은 다릅니다.

---

# 42. Date 객체의 변경 가능성

```js
const date = new Date()

date.setHours(10)
```

변수는 `const`여도 Date 객체 내부 값은 변경할 수 있습니다.

배열과 유사하게:

```text
const는 변수 재할당을 막음
객체 내부 상태 변경까지 자동으로 막지는 않음
```

원본은 `let time`을 사용하지만 재할당하지 않으므로 `const`도 사용할 수 있습니다.

---

# 43. 원본의 변수 이름

```js
const y
const M
const d
const h
const m
const s
```

월만 대문자 `M`, 분은 소문자 `m`으로 구분합니다.

짧은 실습에서는 가능하지만 긴 코드에서는 의미 있는 이름이 읽기 쉽습니다.

```js
const year
const month
const day
const hours
const minutes
const seconds
```

---

# 44. 세미콜론 차이

내 코드 첫 문장:

```js
const now = new Date();
```

이후에는 세미콜론을 대부분 생략합니다.

강사님 코드는 전체적으로 세미콜론을 생략합니다.

자동 세미콜론 삽입으로 실행될 수 있지만 프로젝트에서는 formatter와 lint 규칙에 맞춰 일관성을 유지하는 것이 좋습니다.

---

# 45. HTML 들여쓰기 차이

내 코드:

```html
<html lang="en">
    <head>
```

강사님 코드:

```html
<html lang="en">
<head>
```

내 코드는 `<head>`와 `<body>`를 더 깊게 들여씁니다.

둘 다 HTML 해석에는 영향이 없습니다.

프로젝트 전체에서 일관된 들여쓰기를 유지합니다.

---

# 46. Console Label 차이

내 코드:

```js
console.log("년 : ", y)
```

강사님 코드:

```js
console.log("년 :", y)
```

공백 위치만 다릅니다.

실제 값과 기능에는 차이가 없습니다.

---

# 47. Date 포맷 직접 조합

로컬 날짜·시각을 직접 문자열로 만들 수 있습니다.

```js
const now = new Date()

const year =
  now.getFullYear()

const month =
  String(
    now.getMonth() + 1
  ).padStart(2, "0")

const day =
  String(
    now.getDate()
  ).padStart(2, "0")

console.log(
  `${year}-${month}-${day}`
)
```

이 예제는 원본 메서드를 연결한 확장 학습입니다.

---

# 48. 한 자리 값 PadStart

숫자 7:

```js
String(7).padStart(2, "0")
```

결과:

```text
07
```

날짜 출력에서 월·일·시·분·초를 두 자리로 맞출 때 사용할 수 있습니다.

---

# 49. 로컬 날짜 포맷 함수 확장

```js
function formatLocalDate(date) {
  const year =
    date.getFullYear()

  const month =
    String(
      date.getMonth() + 1
    ).padStart(2, "0")

  const day =
    String(
      date.getDate()
    ).padStart(2, "0")

  return `${year}-${month}-${day}`
}
```

함수는 뒤 단원에서 자세히 학습하지만 Date 메서드 활용 예제로 볼 수 있습니다.

---

# 50. UTC Getter 확장

Date에는 UTC 기준 getter도 있습니다.

```js
date.getUTCFullYear()
date.getUTCMonth()
date.getUTCDate()
date.getUTCHours()
date.getUTCMinutes()
date.getUTCSeconds()
```

로컬 getter와 UTC getter를 한 코드에서 섞으면 날짜가 어긋날 수 있으므로 기준을 일관되게 선택합니다.

원본은 로컬 getter와 `toISOString()`을 함께 비교하는 구조입니다.

---

# 51. 날짜 비교

Date 객체는 timestamp로 비교할 수 있습니다.

```js
const start =
  new Date("2026-06-01")

const end =
  new Date("2026-06-29")

console.log(
  end.getTime() >
  start.getTime()
)
```

날짜 간 차이:

```js
const difference =
  end.getTime() -
  start.getTime()
```

원본의 before·after 측정과 같은 원리입니다.

---

# 52. Invalid Date 확장

잘못된 날짜 문자열:

```js
const date =
  new Date("not-a-date")
```

출력:

```text
Invalid Date
```

검사:

```js
Number.isNaN(
  date.getTime()
)
```

Date 객체를 만들었다고 항상 유효한 날짜는 아닙니다.

원본의 `"2026-06-29"`는 유효한 형식입니다.

---

# 53. 타임존과 데이터 저장

실무에서 자주 사용하는 기준:

```text
저장·서버 통신
→ UTC 또는 명확한 offset 포함

사용자 화면
→ 사용자의 로컬 시간대로 변환
```

`toISOString()`은 UTC 기반 데이터 전달에 유용합니다.

다만 서비스 요구사항에 따라 날짜만 필요한 값과 정확한 순간이 필요한 값을 구분해야 합니다.

---

# 54. 날짜만 필요한 데이터

생일, 마감일, 영업일처럼 “날짜 자체”가 중요한 경우에는 시간대 변환으로 날짜가 바뀌지 않도록 설계해야 합니다.

```text
2026-06-29
```

을 단순히 timestamp로 바꾸면 시간대에 따라 화면 날짜가 달라질 수 있습니다.

원본은 Date 객체 기본 학습이므로 이러한 설계 문제는 확장 개념입니다.

---

# 55. 실행 시간 측정 개선

Console 출력 자체를 측정 대상에 포함하면 로그 출력 비용이 크게 반영됩니다.

연산만 측정하려면:

```js
const before = Date.now()

let sum = 0

for (let i = 0; i < 1000000; i++) {
  sum += i
}

const after = Date.now()

console.log(after - before)
```

출력을 반복문 밖에 둡니다.

---

# 56. My Code 분석

## 56.1 장점

- `now`에서 각 날짜 요소를 꺼내는 흐름을 주석으로 자세히 설명했다.
- `getMonth()`가 0~11이라는 점을 배열 index와 연결했다.
- ISO 문자열의 구성 요소를 설명했다.
- `split("T")[0]`의 중간 변수 풀이도 주석으로 남겼다.
- timestamp가 1970년 UTC부터의 밀리초라는 점을 설명했다.
- 초와 밀리초를 합친 숫자 예시를 추가했다.
- before·after로 실행 시간을 측정하는 목적을 설명했다.
- 특정 날짜 생성의 의미를 설명했다.
- getter와 setter의 관계를 학습하려는 주석을 추가했다.
- `time.getHours() + 9` 방식도 직접 실험했다.
- 강사님보다 Date 메서드의 의미를 더 자세히 기록했다.

## 56.2 개선점

- UTC를 단순히 영국시간이라고 설명한 부분은 부정확하다.
- timestamp 예시 숫자는 현재 실행 결과처럼 오해될 수 있다.
- 20ms를 일반적인 성능 경계로 설명하기 어렵다.
- 반복 조건이 `i <= 1000`이라 강사님보다 한 번 더 실행된다.
- 반복문 안의 `console.log()` 비용 때문에 정밀 성능 측정에 적합하지 않다.
- `time.setHours()`를 연속 두 번 호출해 첫 번째 시 설정을 두 번째가 덮어쓴다.
- 두 호출을 18시간 더하기로 해석하면 안 된다.
- `time`을 재할당하지 않으므로 `let` 대신 `const`도 가능하다.
- 짧은 변수 이름은 긴 코드에서 의미 파악이 어렵다.
- ISO 날짜와 로컬 날짜가 다를 수 있다는 설명이 없다.
- 날짜 전용 문자열의 UTC 해석 가능성을 설명하지 않는다.
- 세미콜론 사용이 일관되지 않다.
- 문서 제목과 언어가 학습 내용에 맞지 않는다.

---

# 57. Teacher Code 분석

## 57.1 장점

- `new Date()`로 현재 시각을 생성한다.
- 연·월·일·시·분·초 getter를 순서대로 실습한다.
- 월이 0~11이라는 점을 강하게 주의시킨다.
- ISO 문자열 전체와 날짜 부분을 출력한다.
- timestamp를 출력한다.
- 전후 timestamp 차이로 실행 시간을 측정한다.
- 정확히 1000회의 반복을 실행한다.
- 특정 날짜 문자열로 Date 객체를 생성한다.
- `setHours()`로 시간 값을 변경한다.
- 코드가 내 파일보다 간결하다.

## 57.2 개선점

- 로컬 getter와 UTC ISO 문자열의 차이를 설명하지 않는다.
- ISO 문자열의 형식을 설명하는 주석이 없다.
- timestamp의 기준과 단위 설명이 없다.
- Console 출력이 성능 측정에 미치는 영향 설명이 없다.
- 날짜 문자열 파싱의 시간대 주의점이 없다.
- `setHours(now.getHours() + 9)`가 시간 더하기인지 시각 교체인지 설명이 부족하다.
- `setHours()`가 원본 Date 객체를 변경한다는 설명이 없다.
- `Date.now()`나 `performance.now()` 대안은 다루지 않는다.
- 유효하지 않은 Date 검사 방법이 없다.
- 문서 제목과 언어가 학습 내용에 맞지 않는다.

---

# 58. My Code vs Teacher Code

| 비교 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 현재 Date 생성 | 동일 | 동일 |
| 첫 문장 세미콜론 | 있음 | 없음 |
| getter 설명 | 상세 | 간결 |
| 월 설명 | 배열과 연결 | `주의!!` |
| ISO 형식 설명 | 있음 | 없음 |
| UTC 설명 | 있음, 일부 부정확 | 없음 |
| ISO 중간 변수 코드 | 주석으로 있음 | 없음 |
| timestamp 기준 설명 | 상세 | 없음 |
| timestamp 숫자 예시 | 있음 | 없음 |
| 성능 기준 20ms 주석 | 있음 | 없음 |
| 반복 조건 | `i <= 1000` | `i < 1000` |
| 반복 실행 횟수 | 1001회 | 1000회 |
| 첫 `setHours()` | `time.getHours() + 9` 추가 | 없음 |
| 두 번째 `setHours()` | `now.getHours() + 9` | 동일 |
| 최종 SetHours 영향 | 첫 호출 후 다시 덮어씀 | 한 번만 변경 |
| HTML 들여쓰기 | 더 깊음 | 일반적 |
| 전체 코드 길이 | 더 길고 설명 많음 | 더 간결 |

---

# 59. 공통 핵심 코드

```js
const now = new Date()

const year =
  now.getFullYear()

const month =
  now.getMonth() + 1

const day =
  now.getDate()

const hours =
  now.getHours()

const minutes =
  now.getMinutes()

const seconds =
  now.getSeconds()

const iso =
  now.toISOString()

const dateOnly =
  iso.split("T")[0]

const timestamp =
  now.getTime()

console.log(
  year,
  month,
  day,
  hours,
  minutes,
  seconds
)

console.log(iso)
console.log(dateOnly)
console.log(timestamp)
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
  <title>JavaScript Date와 날짜 처리</title>
  <script>
    "use strict";

    const now = new Date();

    const year =
      now.getFullYear();

    const month =
      now.getMonth() + 1;

    const day =
      now.getDate();

    const hours =
      now.getHours();

    const minutes =
      now.getMinutes();

    const seconds =
      now.getSeconds();

    console.log({
      year,
      month,
      day,
      hours,
      minutes,
      seconds
    });

    console.log(
      "UTC ISO:",
      now.toISOString()
    );

    console.log(
      "timestamp:",
      now.getTime()
    );
  </script>
</head>
<body>
  <h1>JavaScript Date</h1>
  <p>개발자 도구의 Console을 확인하세요.</p>
</body>
</html>
```

---

# 61. 날짜 포맷 개선 예제

```js
const now = new Date()

const year =
  now.getFullYear()

const month =
  String(
    now.getMonth() + 1
  ).padStart(2, "0")

const day =
  String(
    now.getDate()
  ).padStart(2, "0")

const hours =
  String(
    now.getHours()
  ).padStart(2, "0")

const minutes =
  String(
    now.getMinutes()
  ).padStart(2, "0")

const seconds =
  String(
    now.getSeconds()
  ).padStart(2, "0")

console.log(
  `${year}-${month}-${day} ` +
  `${hours}:${minutes}:${seconds}`
)
```

---

# 62. 경과 시간 개선 예제

```js
const before = Date.now()

let total = 0

for (
  let i = 0;
  i < 1000000;
  i++
) {
  total += i
}

const after = Date.now()

console.log("합계:", total)
console.log(
  "실행 시간:",
  `${after - before}ms`
)
```

반복문 내부 Console 출력을 제거해 계산 자체에 더 집중합니다.

---

# 63. 특정 날짜 변경 개선 예제

9시간 더하기:

```js
const time =
  new Date("2026-06-29T00:00:00Z")

time.setTime(
  time.getTime() +
  9 * 60 * 60 * 1000
)

console.log(
  time.toISOString()
)
```

로컬 시(hour) 설정:

```js
const time =
  new Date(2026, 5, 29)

time.setHours(10)

console.log(time)
```

두 동작의 목적을 구분합니다.

---

# 64. 자주 하는 실수

## 64.1 GetMonth에 1을 더하지 않기

사람이 사용하는 월보다 1 작은 숫자가 출력됩니다.

## 64.2 GetDate와 GetDay 혼동

`getDate()`는 날짜, `getDay()`는 요일 index입니다.

## 64.3 ToISOString을 로컬 시간이라고 생각

UTC 기준 문자열입니다.

## 64.4 ISO 날짜 부분을 로컬 오늘 날짜로 단정

시간대에 따라 로컬 날짜와 다를 수 있습니다.

## 64.5 Timestamp 단위를 초로 생각

`getTime()`은 밀리초입니다.

## 64.6 0부터 1000까지를 1000회라고 생각

양 끝을 모두 포함하면 1001회입니다.

## 64.7 Console Log 반복을 순수 계산 성능으로 해석

로그 출력 비용이 측정값에 포함됩니다.

## 64.8 SetHours가 새 Date를 반환한다고 생각

기존 Date 객체를 변경합니다.

## 64.9 SetHours를 두 번 호출하면 단순히 두 번 더한다고 생각

두 번째 호출은 시 값을 다시 설정할 수 있습니다.

## 64.10 날짜 문자열을 항상 로컬 자정으로 해석

문자열 형식에 따라 UTC 기준으로 해석될 수 있습니다.

---

# 65. 면접·복습 포인트

## Q1. `new Date()`는 무엇을 생성하나요?

코드 실행 시점의 날짜와 시각을 나타내는 Date 객체를 생성합니다.

## Q2. `getMonth()`의 반환 범위는 무엇인가요?

0부터 11입니다. 화면에 일반적인 월을 표시하려면 1을 더합니다.

## Q3. `getDate()`와 `getDay()`의 차이는 무엇인가요?

`getDate()`는 월의 날짜이고 `getDay()`는 요일 index입니다.

## Q4. `toISOString()`은 어떤 기준인가요?

UTC 기준 ISO 8601 형식 문자열을 반환합니다.

## Q5. `getTime()`의 기준과 단위는 무엇인가요?

Unix epoch부터 해당 시점까지의 밀리초 수입니다.

## Q6. 내 코드와 강사님 코드의 반복 횟수 차이는 무엇인가요?

내 코드는 0~1000으로 1001회, 강사님 코드는 0~999로 1000회 실행합니다.

## Q7. 실행 시간 측정에서 Console Log가 문제가 되는 이유는 무엇인가요?

로그 출력 비용이 포함되어 측정하려는 계산보다 Console 작업이 결과를 크게 좌우할 수 있기 때문입니다.

## Q8. `setHours()`는 원본 Date를 변경하나요?

그렇습니다. Date 객체 자체의 시각을 변경합니다.

## Q9. 내 코드의 두 `setHours()`는 18시간을 더하나요?

아닙니다. 첫 호출 후 두 번째 호출이 `now.getHours() + 9` 값으로 시를 다시 설정합니다.

## Q10. 날짜 문자열 `"2026-06-29"` 사용 시 주의점은 무엇인가요?

시간대 정보가 없는 날짜 전용 ISO 문자열이 UTC 자정 기준으로 해석될 수 있으므로 로컬 출력과 날짜가 달라질 가능성을 고려해야 합니다.

---

# Problems

## 문제 1. 현재 Date 생성

현재 날짜와 시각을 나타내는 Date 객체를 생성하고 출력하세요.

## 문제 2. 연도 출력

현재 연도를 출력하세요.

## 문제 3. 월 출력

현재 월을 사람이 사용하는 1~12 범위로 출력하세요.

## 문제 4. 날짜 출력

현재 월의 날짜를 출력하세요.

## 문제 5. 시간 출력

현재 시, 분, 초를 각각 출력하세요.

## 문제 6. 메서드 구분

`getDate()`와 `getDay()`의 차이를 설명하세요.

## 문제 7. ISO 출력

현재 시각을 ISO 문자열로 출력하세요.

## 문제 8. ISO 날짜 추출

ISO 문자열에서 `YYYY-MM-DD` 부분만 출력하세요.

## 문제 9. Timestamp

현재 timestamp를 밀리초 단위로 출력하세요.

## 문제 10. 실행 시간

1부터 1,000,000까지 더하는 코드의 실행 시간을 `Date.now()`로 측정하세요.

## 문제 11. 반복 횟수

다음 두 반복문의 실행 횟수를 각각 작성하세요.

```js
for (let i = 0; i < 1000; i++) {
}

for (let i = 0; i <= 1000; i++) {
}
```

## 문제 12. 특정 날짜

`2026-06-29`를 나타내는 Date 객체를 생성하고 ISO 문자열을 출력하세요.

## 문제 13. 로컬 날짜 생성

숫자 인수를 사용해 로컬 기준 2026년 6월 29일을 생성하세요.

## 문제 14. 시간 설정

Date 객체의 로컬 시를 10시로 설정하세요.

## 문제 15. 9시간 더하기

Date 객체에 정확히 9시간을 밀리초 방식으로 더하세요.

## 문제 16. 두 SetHours 분석

다음 코드가 단순히 18시간을 더하는 것이 아닌 이유를 설명하세요.

```js
time.setHours(time.getHours() + 9)
time.setHours(now.getHours() + 9)
```

## 문제 17. 두 자리 월

현재 월을 두 자리 문자열로 출력하세요.

## 문제 18. 로컬 날짜 문자열

현재 로컬 날짜를 `YYYY-MM-DD` 형식으로 출력하세요.

## 문제 19. 유효하지 않은 Date

잘못된 날짜 문자열로 Date를 만든 뒤 유효하지 않은지 검사하세요.

## 문제 20. 날짜 비교

2026년 6월 1일과 2026년 6월 29일 중 뒤 날짜를 timestamp로 비교하세요.

## 문제 21. 원본 비교

내 코드와 강사님 코드의 반복 조건 및 `setHours()` 차이를 설명하세요.

## 문제 22. 종합 예약 시간

다음 요구사항을 만족하세요.

- 현재 시각 Date 생성
- 예약 시작 시각은 현재 시각에서 2시간 뒤
- 원본 현재 Date는 변경하지 않음
- 시작 시각을 ISO 문자열로 출력
- 로컬 기준 `YYYY-MM-DD HH:mm:ss`도 출력
- 두 시각의 timestamp 차이를 분 단위로 출력

---

# Answers & Explanations

## 정답 1

```js
const now = new Date()

console.log(now)
```

## 정답 2

```js
const now = new Date()

console.log(
  now.getFullYear()
)
```

## 정답 3

```js
const now = new Date()

console.log(
  now.getMonth() + 1
)
```

## 정답 4

```js
const now = new Date()

console.log(
  now.getDate()
)
```

## 정답 5

```js
const now = new Date()

console.log(
  now.getHours()
)

console.log(
  now.getMinutes()
)

console.log(
  now.getSeconds()
)
```

## 정답 6

```text
getDate()
→ 월의 날짜 1~31

getDay()
→ 요일 index 0~6
```

## 정답 7

```js
const now = new Date()

console.log(
  now.toISOString()
)
```

## 정답 8

```js
const now = new Date()

const dateOnly =
  now
    .toISOString()
    .split("T")[0]

console.log(dateOnly)
```

UTC 기준 날짜 부분이라는 점에 주의합니다.

## 정답 9

```js
console.log(
  Date.now()
)
```

또는:

```js
const now = new Date()

console.log(
  now.getTime()
)
```

## 정답 10

```js
const before = Date.now()

let total = 0

for (
  let i = 1;
  i <= 1000000;
  i++
) {
  total += i
}

const after = Date.now()

console.log(total)
console.log(
  `${after - before}ms`
)
```

## 정답 11

```text
i < 1000
→ 0~999
→ 1000회

i <= 1000
→ 0~1000
→ 1001회
```

## 정답 12

```js
const date =
  new Date("2026-06-29")

console.log(
  date.toISOString()
)
```

## 정답 13

```js
const date =
  new Date(2026, 5, 29)

console.log(date)
```

6월은 month index 5입니다.

## 정답 14

```js
const date = new Date()

date.setHours(10)

console.log(date)
```

## 정답 15

```js
const date = new Date()

const nineHours =
  9 * 60 * 60 * 1000

date.setTime(
  date.getTime() + nineHours
)

console.log(date)
```

## 정답 16

첫 번째 호출은 `time` 자신의 시에 9를 더합니다. 두 번째 호출은 그 결과에 다시 9를 더하는 대신, `time`의 시를 `now.getHours() + 9` 값으로 다시 설정합니다. 따라서 단순 누적 18시간이 아닙니다.

## 정답 17

```js
const now = new Date()

const month =
  String(
    now.getMonth() + 1
  ).padStart(2, "0")

console.log(month)
```

## 정답 18

```js
const now = new Date()

const year =
  now.getFullYear()

const month =
  String(
    now.getMonth() + 1
  ).padStart(2, "0")

const day =
  String(
    now.getDate()
  ).padStart(2, "0")

console.log(
  `${year}-${month}-${day}`
)
```

## 정답 19

```js
const invalidDate =
  new Date("not-a-date")

const isInvalid =
  Number.isNaN(
    invalidDate.getTime()
  )

console.log(isInvalid)
```

## 정답 20

```js
const first =
  new Date("2026-06-01")

const second =
  new Date("2026-06-29")

if (
  second.getTime() >
  first.getTime()
) {
  console.log("두 번째 날짜가 뒤입니다.")
}
```

## 정답 21

내 코드는 `i <= 1000`으로 1001회 반복하고 강사님 코드는 `i < 1000`으로 1000회 반복합니다. 내 코드는 `time.getHours() + 9` 설정을 먼저 실행한 뒤 강사님과 같은 `now.getHours() + 9` 설정을 다시 실행하므로 첫 시 설정이 두 번째 호출에 의해 덮어써집니다.

## 정답 22

```js
const now = new Date()

const reservation =
  new Date(now.getTime())

reservation.setTime(
  reservation.getTime() +
  2 * 60 * 60 * 1000
)

const year =
  reservation.getFullYear()

const month =
  String(
    reservation.getMonth() + 1
  ).padStart(2, "0")

const day =
  String(
    reservation.getDate()
  ).padStart(2, "0")

const hours =
  String(
    reservation.getHours()
  ).padStart(2, "0")

const minutes =
  String(
    reservation.getMinutes()
  ).padStart(2, "0")

const seconds =
  String(
    reservation.getSeconds()
  ).padStart(2, "0")

const differenceMinutes =
  (
    reservation.getTime() -
    now.getTime()
  ) / 1000 / 60

console.log(
  "현재:",
  now
)

console.log(
  "예약 ISO:",
  reservation.toISOString()
)

console.log(
  "예약 로컬:",
  `${year}-${month}-${day} ` +
  `${hours}:${minutes}:${seconds}`
)

console.log(
  `차이: ${differenceMinutes}분`
)
```

원본 `now` 객체를 복사한 새 Date 객체를 변경하므로 현재 시각 객체는 유지됩니다.

---

# Final Checklist

## Date 기본

- [ ] `new Date()`로 현재 Date 객체를 만들었다.
- [ ] 실행 시점과 컴퓨터 시간대에 따라 값이 달라짐을 이해했다.
- [ ] 연·월·일·시·분·초 getter를 구분했다.
- [ ] `getMonth()` 결과에 1을 더했다.
- [ ] `getDate()`와 `getDay()`를 혼동하지 않았다.
- [ ] 시가 0~23 범위임을 확인했다.
- [ ] 분과 초가 숫자로 반환됨을 이해했다.

## ISO와 UTC

- [ ] `toISOString()`이 UTC 기준임을 이해했다.
- [ ] ISO 문자열의 `T`와 `Z` 의미를 확인했다.
- [ ] `split("T")[0]`으로 날짜 부분을 추출했다.
- [ ] ISO 날짜 부분과 로컬 오늘 날짜가 다를 수 있음을 이해했다.
- [ ] UTC를 단순히 영국 현지 시각과 동일시하지 않았다.
- [ ] 저장 기준과 사용자 표시 기준을 구분했다.

## Timestamp와 성능

- [ ] `getTime()`의 기준이 Unix epoch임을 이해했다.
- [ ] timestamp 단위가 밀리초임을 확인했다.
- [ ] before와 after 차이를 계산했다.
- [ ] `Date.now()` 대안을 이해했다.
- [ ] 0~999와 0~1000의 반복 횟수를 구분했다.
- [ ] 반복문 안 Console 출력이 측정값에 영향을 줌을 이해했다.
- [ ] 20ms를 모든 환경의 고정 성능 기준으로 사용하지 않았다.

## 날짜 생성과 변경

- [ ] 날짜 문자열로 Date를 생성했다.
- [ ] 날짜 전용 문자열의 UTC 해석 가능성을 이해했다.
- [ ] 숫자 생성자의 월이 0부터 시작함을 확인했다.
- [ ] `setHours()`가 기존 Date를 변경함을 이해했다.
- [ ] 시간 설정과 시간 더하기를 구분했다.
- [ ] 연속된 setter가 앞선 값을 덮어쓸 수 있음을 이해했다.
- [ ] Date 복사 시 `new Date(original.getTime())`를 사용할 수 있다.
- [ ] 유효하지 않은 Date를 timestamp로 검사했다.

## 출력 형식

- [ ] 월·일·시·분·초를 문자열로 변환했다.
- [ ] `padStart(2, "0")`으로 두 자리를 맞췄다.
- [ ] 로컬 날짜 문자열을 직접 조합했다.
- [ ] 짧은 변수명 대신 의미 있는 이름을 검토했다.

## 원본 코드 검수

- [ ] 두 실제 원본 경로를 기록했다.
- [ ] 현재 시각은 고정값으로 작성하지 않았다.
- [ ] 내 ISO·UTC 설명의 부정확한 부분을 기록했다.
- [ ] 내 timestamp 숫자 예시를 고정 실행 결과로 해석하지 않았다.
- [ ] 내 20ms 설명이 보편적 기준이 아님을 기록했다.
- [ ] 내 반복문이 1001회 실행됨을 확인했다.
- [ ] 강사님 반복문이 1000회 실행됨을 확인했다.
- [ ] 내 코드의 추가 `time.getHours() + 9` 호출을 기록했다.
- [ ] 두 번째 setHours가 첫 번째 시 설정을 덮어씀을 설명했다.
- [ ] 두 호출을 18시간 더하기로 설명하지 않았다.
- [ ] HTML 들여쓰기와 Console label 공백 차이를 기록했다.
- [ ] 세미콜론 사용의 비일관성을 기록했다.

---

# Key Summary

- `new Date()`는 실행 시점의 현재 날짜와 시각을 담은 Date 객체를 만든다.
- 현재 Date 결과는 실행 시각과 컴퓨터 시간대에 따라 달라진다.
- `getFullYear()`는 연도, `getMonth()`는 0~11의 월 index를 반환한다.
- 사람이 사용하는 월을 출력하려면 `getMonth() + 1`을 사용한다.
- `getDate()`는 월의 날짜이고 `getDay()`는 요일 index다.
- `getHours()`, `getMinutes()`, `getSeconds()`는 로컬 시간 기준 값을 반환한다.
- `toISOString()`은 UTC 기준 `YYYY-MM-DDTHH:mm:ss.sssZ` 문자열을 반환한다.
- UTC를 단순히 영국 현지 시각이라고만 설명하면 부정확하다.
- `iso.split("T")[0]`으로 UTC 기준 날짜 부분을 추출할 수 있다.
- UTC 날짜와 로컬 날짜는 시간대와 시각에 따라 다를 수 있다.
- `getTime()`은 1970년 1월 1일 00:00:00 UTC부터의 밀리초 수를 반환한다.
- 내 코드의 특정 timestamp 숫자는 설명용 예시이며 현재 실행 결과로 고정할 수 없다.
- before와 after timestamp의 차이로 경과 시간을 밀리초 단위로 계산할 수 있다.
- 내 코드는 `i <= 1000`으로 1001회, 강사님 코드는 `i < 1000`으로 1000회 반복한다.
- 반복문 안 `console.log()`는 실행 시간 측정값에 큰 영향을 줄 수 있다.
- 내 코드의 20ms 설명은 모든 환경에 적용되는 보편적 성능 기준이 아니다.
- 현재 timestamp는 `Date.now()`로도 구할 수 있다.
- `"2026-06-29"`로 특정 Date를 만들 수 있지만 날짜 전용 문자열의 시간대 해석에 주의한다.
- 로컬 기준 2026년 6월 29일은 `new Date(2026, 5, 29)`처럼 만들 수 있다.
- `setHours()`는 새로운 Date를 만드는 것이 아니라 기존 Date 객체를 변경한다.
- `time.setHours(time.getHours() + 9)`는 time 자신의 로컬 시에 9를 더한다.
- `time.setHours(now.getHours() + 9)`는 time의 시를 현재 now의 시 + 9 값으로 다시 설정한다.
- 내 코드의 연속된 두 `setHours()` 호출은 단순히 18시간을 더하는 동작이 아니다.
- 첫 번째 시 설정은 두 번째 호출에 의해 덮어써질 수 있다.
- 정확한 시간 차이는 timestamp 밀리초를 더하는 방식으로 계산할 수 있다.
- Date 객체도 `const`로 선언한 뒤 내부 날짜 값을 setter로 변경할 수 있다.
- 날짜 출력의 한 자리 값은 `padStart(2, "0")`으로 두 자리를 맞출 수 있다.
- 유효하지 않은 Date는 `Number.isNaN(date.getTime())`으로 검사할 수 있다.
