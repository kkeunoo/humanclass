---
title: JavaScript Date와 날짜 처리
version: v2.0-final
last_updated: 2026-08-06
status: Completed
---

# JavaScript Date와 날짜 처리

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `07_JavaScript_Date와_날짜처리.md` |
| 분류 | `03_JavaScript` |
| 원본 기준 | `workspace_html/javascript/07_date.html`, `workspace_teacher/workspace_html/javascript/07_date.html` |
| 핵심 범위 | `Date`, 현재 시각, 날짜 구성 요소, ISO 문자열, UTC, timestamp, 실행 시간 측정, 특정 날짜 생성, 날짜 변경 |
| 실습 범위 | 현재 날짜 출력, 로컬 날짜 형식화, 날짜 차이 계산, 실행 시간 측정, 예약 만료일 계산 |
| 문서 형식 | JavaScript Developer-Wiki V2 확정 형식 |

> 이 문서는 내 코드와 강사님 코드 전체를 그대로 나열하지 않는다.  
> `Date` 객체의 생성·조회·변경·시간대 처리에 필요한 핵심 코드만 발췌하고, 실행 환경에 따라 달라지는 값과 날짜 처리 시 주의점을 함께 설명한다.

---

# 개요

JavaScript의 `Date` 객체는 하나의 날짜와 시각을 표현한다.

```javascript
const now = new Date()
```

인수를 전달하지 않으면 코드가 실행된 현재 순간을 기준으로 객체를 만든다.

`Date` 객체에서는 다음 작업을 할 수 있다.

| 작업 | 대표 기능 |
| --- | --- |
| 현재 시각 생성 | `new Date()` |
| 연·월·일 추출 | `getFullYear()`, `getMonth()`, `getDate()` |
| 시·분·초 추출 | `getHours()`, `getMinutes()`, `getSeconds()` |
| UTC 문자열 생성 | `toISOString()` |
| timestamp 추출 | `getTime()`, `Date.now()` |
| 날짜 변경 | `setHours()`, `setDate()` |
| 날짜 차이 계산 | timestamp 뺄셈 |

> [!IMPORTANT]
> 날짜와 시각은 **같은 순간**, **표시 시간대**, **문자열 형식**을 구분해서 이해해야 한다.

---

# 핵심 개념

| 개념 | 핵심 역할 |
| --- | --- |
| `Date` 객체 | 날짜와 시각을 표현 |
| 로컬 시간 | 실행 환경의 시간대 기준 |
| UTC | 협정 세계시 기준 |
| ISO 8601 | 날짜와 시각을 교환하는 표준 문자열 형식 |
| timestamp | Unix epoch부터 흐른 밀리초 |
| Unix epoch | `1970-01-01T00:00:00.000Z` |
| getter | 날짜 구성 요소를 읽는 메서드 |
| setter | 기존 `Date` 객체 값을 변경하는 메서드 |
| 시간대 | 같은 순간을 지역별 시각으로 표시하는 기준 |
| 경과 시간 | 두 timestamp의 차이 |

---

# 학습 목표

- `new Date()`로 현재 날짜와 시각을 생성할 수 있다.
- `Date` 객체의 출력값이 실행 환경에 따라 달라질 수 있음을 이해한다.
- 연·월·일·시·분·초를 각각 추출할 수 있다.
- `getMonth()`가 0부터 시작함을 설명할 수 있다.
- `getDate()`와 `getDay()`를 구분할 수 있다.
- 로컬 getter와 UTC getter의 차이를 이해한다.
- `toISOString()`의 형식과 UTC 기준을 설명할 수 있다.
- ISO 문자열에서 날짜 부분을 추출할 수 있다.
- 로컬 날짜와 UTC 날짜가 달라질 수 있음을 이해한다.
- `getTime()`과 `Date.now()`를 사용할 수 있다.
- timestamp 차이로 경과 시간을 계산할 수 있다.
- `performance.now()`가 실행 시간 측정에 적합한 이유를 이해한다.
- 날짜 문자열 생성 시 시간대 해석 차이를 주의할 수 있다.
- 숫자 인수로 특정 날짜를 안전하게 생성할 수 있다.
- setter가 원본 `Date` 객체를 직접 변경함을 이해한다.
- 날짜 복사본을 만든 뒤 변경할 수 있다.
- 날짜 출력에서 두 자리 형식을 만들 수 있다.
- `Intl.DateTimeFormat`으로 지역화된 날짜를 표시할 수 있다.

---

# 1. `Date` 객체 생성

## 1-1. 내 코드와 강사님 코드

```javascript
const now = new Date()

console.log(now)
```

두 원본은 동일하게 현재 날짜와 시각을 생성한다.

## 1-2. 실행 결과

출력값은 코드를 실행한 순간과 브라우저 환경에 따라 달라진다.

```text
Thu Aug 06 2026 13:51:00 GMT+0900 ...
```

위 형태는 예시일 뿐 고정 결과가 아니다.

---

# 2. `Date`는 객체다

```javascript
const now = new Date()

console.log(typeof now)
```

출력:

```text
object
```

배열처럼 `Date`도 내장 객체이며 날짜 처리를 위한 메서드를 제공한다.

---

# 3. 문서 구조 개선

원본:

```html
<html lang="en">
<title>Document</title>
```

개선:

```html
<html lang="ko">
<title>JavaScript Date와 날짜 처리</title>
```

학습 문서의 언어와 제목을 실제 내용에 맞춘다.

---

# 4. 연도 `getFullYear()`

```javascript
const year = now.getFullYear()

console.log("년:", year)
```

네 자리 연도를 숫자로 반환한다.

```text
2026
```

과거의 `getYear()`가 아니라 `getFullYear()`를 사용한다.

---

# 5. 월 `getMonth()`

```javascript
const monthIndex = now.getMonth()

console.log("월:", monthIndex + 1)
```

`getMonth()`의 반환 범위:

```text
0~11
```

| 반환값 | 실제 월 |
| ---: | ---: |
| `0` | 1월 |
| `1` | 2월 |
| `11` | 12월 |

> [!WARNING]
> 사람에게 표시할 월에는 일반적으로 1을 더해야 한다.

---

# 6. 월 변수 이름

원본에서는 대문자 `M`을 사용한다.

```javascript
const M = now.getMonth()
```

의미가 분명한 이름으로 개선할 수 있다.

```javascript
const month = (
    now.getMonth() + 1
)
```

JavaScript 변수명은 일반적으로 camelCase를 사용한다.

---

# 7. 날짜 `getDate()`

```javascript
const date = now.getDate()

console.log("일:", date)
```

현재 월의 몇 번째 날짜인지 반환한다.

범위는 월에 따라 `1~28`, `1~29`, `1~30`, `1~31`이다.

---

# 8. `getDate()`와 `getDay()`

| 메서드 | 의미 | 반환 범위 |
| --- | --- | --- |
| `getDate()` | 월의 날짜 | `1~31` |
| `getDay()` | 요일 인덱스 | `0~6` |

요일 인덱스:

```text
0 → 일요일
1 → 월요일
...
6 → 토요일
```

---

# 9. 요일 문자열 만들기

```javascript
const dayNames = [
    "일",
    "월",
    "화",
    "수",
    "목",
    "금",
    "토",
]

const dayName = (
    dayNames[now.getDay()]
)

console.log(`${dayName}요일`)
```

---

# 10. 시 `getHours()`

```javascript
const hours = now.getHours()

console.log("시:", hours)
```

로컬 시간 기준 `0~23`을 반환한다.

---

# 11. 분 `getMinutes()`

```javascript
const minutes = now.getMinutes()

console.log("분:", minutes)
```

반환 범위:

```text
0~59
```

숫자 `5`는 자동으로 `"05"`가 되지 않는다.

---

# 12. 초 `getSeconds()`

```javascript
const seconds = now.getSeconds()

console.log("초:", seconds)
```

반환 범위:

```text
0~59
```

---

# 13. 밀리초 `getMilliseconds()`

```javascript
const milliseconds = (
    now.getMilliseconds()
)

console.log(milliseconds)
```

반환 범위:

```text
0~999
```

원본의 ISO 문자열에는 밀리초가 포함되지만 개별 getter는 사용하지 않는다. 이를 보충한 내용이다.

---

# 14. 로컬 시간 getter 정리

| 목적 | 메서드 |
| --- | --- |
| 연도 | `getFullYear()` |
| 월 | `getMonth()` |
| 날짜 | `getDate()` |
| 요일 | `getDay()` |
| 시 | `getHours()` |
| 분 | `getMinutes()` |
| 초 | `getSeconds()` |
| 밀리초 | `getMilliseconds()` |

이 메서드는 실행 환경의 로컬 시간대를 기준으로 한다.

---

# 15. UTC getter

UTC 기준 값이 필요하면 다음 메서드를 사용할 수 있다.

```javascript
now.getUTCFullYear()
now.getUTCMonth()
now.getUTCDate()
now.getUTCHours()
```

로컬 getter와 UTC getter는 같은 순간을 서로 다른 시간대 기준으로 읽는다.

---

# 16. ISO 문자열

## 16-1. 원본 코드

```javascript
const iso = now.toISOString()

console.log(iso)
```

형식:

```text
YYYY-MM-DDTHH:mm:ss.sssZ
```

예시:

```text
2026-08-06T04:51:00.123Z
```

---

# 17. ISO는 UTC 기준

원본 주석에는 ISO를 “영국시간”이라고 설명한다.

더 정확한 표현:

```text
toISOString()
→ UTC 기준 ISO 8601 문자열
```

UTC는 협정 세계시다. 영국의 현지 시각은 일광 절약 시간 적용 여부에 따라 UTC와 다를 수 있으므로 단순히 영국시간이라고 부르지 않는다.

---

# 18. ISO 문자열의 `Z`

```text
2026-08-06T04:51:00.123Z
```

마지막 `Z`는 UTC 기준이라는 의미다.

```text
Z
→ zero UTC offset
→ +00:00
```

---

# 19. 같은 순간의 다른 표현

한국 로컬 시각:

```text
2026-08-06 13:51
```

UTC ISO:

```text
2026-08-06T04:51:00.000Z
```

표시된 시각은 다르지만 같은 순간을 나타낼 수 있다.

---

# 20. ISO에서 날짜 추출

## 20-1. 원본 코드

```javascript
console.log(
    iso.split("T")[0],
)
```

출력 형식:

```text
YYYY-MM-DD
```

`T`를 기준으로 날짜와 시간을 나눈 뒤 첫 요소를 선택한다.

---

# 21. 구조 분해 할당

```javascript
const [
    isoDate,
    isoTime,
] = iso.split("T")

console.log(isoDate)
console.log(isoTime)
```

날짜와 시간 부분을 각각 변수에 저장할 수 있다.

---

# 22. UTC 날짜와 로컬 날짜 차이

```javascript
const isoDate = (
    now.toISOString().split("T")[0]
)
```

이 값은 UTC 기준 날짜다.

로컬 시간이 자정 근처이면 로컬 날짜와 하루 차이가 날 수 있다.

> [!WARNING]
> 사용자 화면의 “오늘”을 표시하려는 목적으로 ISO 날짜 부분을 그대로 사용하면 시간대에 따라 날짜가 달라질 수 있다.

---

# 23. 로컬 날짜 직접 만들기

```javascript
const year = now.getFullYear()
const month = String(
    now.getMonth() + 1,
).padStart(2, "0")
const date = String(
    now.getDate(),
).padStart(2, "0")

const localDate = (
    `${year}-${month}-${date}`
)

console.log(localDate)
```

로컬 시간 기준 `YYYY-MM-DD` 문자열을 만든다.

---

# 24. `padStart()`

```javascript
console.log(
    String(5).padStart(2, "0"),
)
```

출력:

```text
05
```

월·일·시·분처럼 두 자리 표시가 필요한 값에 사용할 수 있다.

---

# 25. 로컬 날짜와 시각 형식화

```javascript
function formatLocalDateTime(
    date,
) {
    const year = (
        date.getFullYear()
    )

    const month = String(
        date.getMonth() + 1,
    ).padStart(2, "0")

    const day = String(
        date.getDate(),
    ).padStart(2, "0")

    const hours = String(
        date.getHours(),
    ).padStart(2, "0")

    const minutes = String(
        date.getMinutes(),
    ).padStart(2, "0")

    return (
        `${year}-${month}-${day}`
        + ` ${hours}:${minutes}`
    )
}
```

---

# 26. Timestamp

## 26-1. 원본 코드

```javascript
const timestamp = now.getTime()

console.log(timestamp)
```

Unix epoch부터 해당 순간까지 흐른 밀리초를 반환한다.

Unix epoch:

```text
1970-01-01T00:00:00.000Z
```

---

# 27. 밀리초 단위

```text
1초
→ 1,000밀리초

1분
→ 60,000밀리초

1시간
→ 3,600,000밀리초

1일
→ 86,400,000밀리초
```

---

# 28. `Date.now()`

```javascript
const timestamp = Date.now()

console.log(timestamp)
```

현재 timestamp만 필요하다면 다음보다 간결하다.

```javascript
new Date().getTime()
```

---

# 29. Timestamp에서 Date 생성

```javascript
const timestamp = Date.now()
const date = new Date(timestamp)

console.log(date)
```

timestamp와 `Date` 객체를 서로 변환할 수 있다.

---

# 30. 두 날짜의 차이

```javascript
const start = new Date(
    2026,
    7,
    1,
)

const end = new Date(
    2026,
    7,
    6,
)

const difference = (
    end.getTime()
    - start.getTime()
)

const days = (
    difference
    / (1000 * 60 * 60 * 24)
)

console.log(days)
```

출력:

```text
5
```

---

# 31. 실행 시간 측정

## 31-1. 원본 코드

```javascript
const before = (
    new Date().getTime()
)

for (
    let index = 0;
    index < 1000;
    index += 1
) {
    console.log(index)
}

const after = (
    new Date().getTime()
)

console.log(
    "after - before:",
    after - before,
)
```

차이의 단위는 밀리초다.

---

# 32. 내 코드와 강사님 코드의 반복 횟수

내 코드:

```javascript
index <= 1000
```

출력 범위:

```text
0~1000
```

실행 횟수:

```text
1001회
```

강사님 코드:

```javascript
index < 1000
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

# 33. `console.log()` 성능 측정 주의

반복문의 실제 계산보다 `console.log()` 출력 비용이 더 크게 측정될 수 있다.

측정 결과는 다음 환경에 영향을 받는다.

- 브라우저
- 개발자 도구 상태
- 컴퓨터 성능
- 백그라운드 작업
- Console 출력량
- JavaScript 엔진 최적화

원본의 “20ms를 넘으면 느리다”는 값을 보편적인 기준으로 사용할 수 없다.

---

# 34. `performance.now()`

브라우저 코드 실행 시간 측정에는 더 정밀한 값을 제공하는 `performance.now()`를 사용할 수 있다.

```javascript
const before = performance.now()

let total = 0

for (
    let index = 0;
    index < 100000;
    index += 1
) {
    total += index
}

const after = performance.now()

console.log(
    `${after - before}ms`,
)
```

---

# 35. 측정 코드에서 출력 제거

성능을 비교하려는 코드 내부에 반복적인 `console.log()`를 넣지 않는 편이 좋다.

기존:

```text
for (...) {
    console.log(index)
}
```

개선:

```text
let total = 0

for (...) {
    total += index
}
```

측정하려는 작업 자체에 집중할 수 있다.

---

# 36. 특정 날짜 문자열 생성

## 36-1. 원본 코드

```javascript
const time = new Date(
    "2026-06-29",
)

console.log(
    time.toISOString(),
)
```

`YYYY-MM-DD` 형태의 문자열은 UTC 자정 기준으로 해석될 수 있다.

---

# 37. 날짜 문자열의 시간대 주의

```javascript
const time = new Date(
    "2026-06-29",
)
```

한국 로컬 getter로 읽으면 시간대에 따라 다음 날 오전으로 보일 수 있다.

같은 날짜의 로컬 자정을 만들려는 목적이라면 숫자 인수를 사용하는 편이 명확하다.

```javascript
const time = new Date(
    2026,
    5,
    29,
)
```

월 인수는 0부터 시작하므로 6월은 `5`다.

---

# 38. 숫자 인수 Date 생성

```javascript
const date = new Date(
    2026,
    5,
    29,
    10,
    30,
    0,
)
```

구성:

```text
연도
월 인덱스
날짜
시
분
초
밀리초
```

---

# 39. 날짜 파싱 검증

```javascript
const date = new Date(
    "잘못된 날짜",
)

console.log(date)
console.log(
    Number.isNaN(
        date.getTime(),
    ),
)
```

출력:

```text
Invalid Date
true
```

날짜 문자열 입력을 사용할 때 유효성을 검사한다.

---

# 40. `setHours()`

## 40-1. 원본 코드

```javascript
time.setHours(
    now.getHours() + 9,
)
```

`setHours()`는 기존 `Date` 객체의 로컬 시 값을 변경한다.

반환값은 변경된 timestamp다.

---

# 41. Setter는 원본 변경

```javascript
const date = new Date(
    2026,
    5,
    29,
)

const result = date.setHours(10)

console.log(date)
console.log(result)
```

`date` 객체 자체가 변경되고, `result`에는 숫자 timestamp가 저장된다.

---

# 42. Getter와 Setter 대응

| 읽기 | 변경 |
| --- | --- |
| `getFullYear()` | `setFullYear()` |
| `getMonth()` | `setMonth()` |
| `getDate()` | `setDate()` |
| `getHours()` | `setHours()` |
| `getMinutes()` | `setMinutes()` |
| `getSeconds()` | `setSeconds()` |

모든 getter에 항상 정확히 같은 용도의 setter가 있는 것은 아니지만 주요 구성 요소는 대응한다.

---

# 43. 내 코드의 두 번 연속 `setHours()`

내 코드:

```javascript
time.setHours(
    time.getHours() + 9,
)

time.setHours(
    now.getHours() + 9,
)
```

첫 번째 호출로 `time`의 시가 변경되지만, 바로 다음 호출이 다시 시 값을 설정한다.

결과적으로 첫 변경은 최종 결과에 남지 않는다.

> [!WARNING]
> 날짜 setter를 연속 호출할 때 앞의 변경이 뒤 호출로 덮어써지는지 확인한다.

---

# 44. 시간 더하기

현재 `time`에서 9시간을 더하려면 다음처럼 작성한다.

```javascript
time.setHours(
    time.getHours() + 9,
)
```

timestamp 방식:

```javascript
const nineHours = (
    9 * 60 * 60 * 1000
)

const changedTime = new Date(
    time.getTime() + nineHours,
)
```

두 번째 방식은 원본을 변경하지 않고 새 객체를 만든다.

---

# 45. Date 복사

잘못 이해하기 쉬운 코드:

```javascript
const copied = time
```

`copied`와 `time`은 같은 객체를 가리킨다.

복사본 생성:

```javascript
const copied = new Date(
    time.getTime(),
)
```

이제 `copied`를 변경해도 `time`은 바뀌지 않는다.

---

# 46. 날짜 자동 보정

```javascript
const date = new Date(
    2026,
    0,
    31,
)

date.setDate(
    date.getDate() + 1,
)

console.log(date)
```

1월 31일에서 하루를 더하면 JavaScript가 다음 달로 자동 보정한다.

이 특성을 이용해 날짜 더하기를 구현할 수 있다.

---

# 47. 하루 더하기

```javascript
function addDays(
    date,
    days,
) {
    const result = new Date(
        date.getTime(),
    )

    result.setDate(
        result.getDate() + days,
    )

    return result
}
```

원본 날짜를 변경하지 않고 새 날짜를 반환한다.

---

# 48. 지역화 날짜 출력

브라우저의 국제화 API를 사용할 수 있다.

```javascript
const formatter = (
    new Intl.DateTimeFormat(
        "ko-KR",
        {
            dateStyle: "long",
            timeStyle: "short",
        },
    )
)

console.log(
    formatter.format(now),
)
```

실행 환경에 따라 다음과 같은 형태로 출력된다.

```text
2026년 8월 6일 오후 1:51
```

---

# 49. `toLocaleString()`

```javascript
console.log(
    now.toLocaleString(
        "ko-KR",
    ),
)
```

간단한 지역화 출력에 사용할 수 있다.

정확한 형식을 제어하려면 `Intl.DateTimeFormat` 옵션을 지정한다.

---

# 50. 내 코드와 강사님 코드 비교

| 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 현재 시각 | 동일 | 동일 |
| getter 설명 | 각 메서드 주석 상세 | 핵심 주석 중심 |
| ISO 설명 | 영국시간이라고 표현 | 별도 설명 없음 |
| timestamp | epoch 예시 상세 | 기본 추출 |
| 실행 시간 | `0~1000`, 1001회 | `0~999`, 1000회 |
| 성능 기준 | 20ms 개인 메모 | 없음 |
| 특정 날짜 | 동일 | 동일 |
| `setHours()` | 두 번 연속 호출 | 한 번 호출 |

## 50-1. 내 코드의 장점

- 날짜 구성 요소별 역할을 자세히 기록했다.
- `getMonth()`가 0부터 시작한다는 점을 배열과 연결했다.
- timestamp와 epoch의 관계를 설명했다.
- 실행 전후 timestamp로 경과 시간을 측정했다.
- getter와 setter의 관계를 메모했다.

## 50-2. 내 코드의 개선점

- UTC를 단순히 영국시간이라고 설명하면 부정확하다.
- 특정 timestamp 숫자는 실행 시각에 따라 달라지는 예시일 뿐이다.
- 20ms를 보편적인 성능 기준으로 사용할 수 없다.
- 반복 조건 `<= 1000`은 강사님 코드보다 한 번 더 실행된다.
- 연속된 두 `setHours()` 중 첫 변경이 두 번째 호출로 덮어써진다.
- 날짜 문자열 파싱의 UTC 해석 차이를 설명할 필요가 있다.

## 50-3. 강사님 코드의 장점

- 현재 날짜 생성부터 setter까지 한 흐름으로 구성되어 있다.
- 핵심 getter와 ISO·timestamp를 간결하게 다룬다.
- 실행 시간 측정 원리를 직접 확인할 수 있다.
- 반복 횟수가 정확히 1000회다.

## 50-4. 강사님 코드의 보충점

- 로컬 시간과 UTC의 차이를 보충할 필요가 있다.
- `getDate()`와 `getDay()` 구분이 필요하다.
- 날짜 문자열 생성 시 시간대 해석을 설명할 필요가 있다.
- setter가 원본 객체를 변경한다는 설명이 필요하다.
- 정밀한 성능 측정에는 `performance.now()`가 적합하다는 보충이 가능하다.

---

# 51. 기존 코드에서 개선 코드로 바꾼 이유

## 51-1. 의미 있는 변수명

기존:

```javascript
const y = now.getFullYear()
const M = now.getMonth()
const d = now.getDate()
```

개선:

```javascript
const year = now.getFullYear()
const month = now.getMonth() + 1
const date = now.getDate()
```

## 51-2. Timestamp 생성

기존:

```javascript
new Date().getTime()
```

현재 timestamp만 필요할 때:

```javascript
Date.now()
```

## 51-3. 실행 시간 측정

기존:

```javascript
new Date().getTime()
```

브라우저 성능 측정:

```javascript
performance.now()
```

## 51-4. 날짜 복사 후 변경

기존:

```javascript
time.setHours(
    time.getHours() + 9,
)
```

원본 유지:

```javascript
const changedTime = new Date(
    time.getTime(),
)

changedTime.setHours(
    changedTime.getHours() + 9,
)
```

---

# 52. 실무형 예제: 예약 만료일 계산

```javascript
function addDays(
    date,
    days,
) {
    const result = new Date(
        date.getTime(),
    )

    result.setDate(
        result.getDate() + days,
    )

    return result
}

const reservedAt = new Date(
    2026,
    7,
    6,
    14,
    0,
)

const expiresAt = addDays(
    reservedAt,
    3,
)

const formatter = (
    new Intl.DateTimeFormat(
        "ko-KR",
        {
            dateStyle: "long",
            timeStyle: "short",
        },
    )
)

console.log(
    `예약 시각: ${formatter.format(reservedAt)}`,
)

console.log(
    `만료 시각: ${formatter.format(expiresAt)}`,
)
```

## 52-1. 출력 결과 형태

```text
예약 시각: 2026년 8월 6일 오후 2:00
만료 시각: 2026년 8월 9일 오후 2:00
```

## 52-2. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `new Date(timestamp)` | 원본 날짜 복사 |
| `setDate()` | 날짜 단위 변경 |
| `getDate()` | 현재 날짜 읽기 |
| 함수 반환 | 변경된 날짜 재사용 |
| `Intl.DateTimeFormat` | 사용자 지역에 맞는 출력 |
| 원본 유지 | 예약 생성 시각과 만료 시각을 각각 보존 |

---

# 53. 대표 오류로 이해하기

## 53-1. 월에 1을 더하지 않음

8월에 `getMonth()`는 `7`을 반환한다.

## 53-2. `getDate()`와 `getDay()` 혼동

날짜 대신 요일 인덱스가 출력된다.

## 53-3. ISO 날짜를 로컬 오늘 날짜로 사용

자정 근처에서 하루 차이가 날 수 있다.

## 53-4. 잘못된 날짜 문자열

`Invalid Date`가 생성될 수 있다.

## 53-5. setter 반환값을 Date로 생각

`setHours()` 등은 timestamp 숫자를 반환한다.

## 53-6. Date 객체를 대입으로 복사

두 변수가 같은 객체를 공유한다.

---

# 54. 자주 하는 실수

## 54-1. `getMonth()`가 1부터 시작한다고 생각

0부터 11까지다.

## 54-2. ISO를 로컬 시각이라고 생각

UTC 기준이다.

## 54-3. UTC를 단순히 영국 현지 시각이라고 설명

UTC와 영국 현지 시각은 계절에 따라 다를 수 있다.

## 54-4. Timestamp 단위를 초로 생각

JavaScript `Date` timestamp는 밀리초다.

## 54-5. `console.log()` 반복을 순수 계산 성능으로 측정

Console 출력 비용이 크게 포함된다.

## 54-6. 날짜 문자열이 항상 로컬 시간으로 해석된다고 생각

형식에 따라 UTC 또는 로컬 기준으로 해석될 수 있다.

## 54-7. setter가 새 Date를 반환한다고 생각

원본을 변경하고 timestamp를 반환한다.

## 54-8. `const copied = original`로 날짜 복사

같은 객체 참조를 공유한다.

## 54-9. 한 자리 월·일을 그대로 문자열에 연결

`padStart()`로 두 자리 형식을 만들 수 있다.

## 54-10. 날짜 출력 형식을 직접 문자열로만 구성

지역화가 필요하면 `Intl.DateTimeFormat`을 검토한다.

---

# 55. 핵심 요약

```text
new Date()
→ 현재 날짜와 시각

getFullYear()
→ 연도

getMonth()
→ 0~11 월 인덱스

getDate()
→ 월의 날짜
```

```text
getHours()
getMinutes()
getSeconds()
→ 로컬 시각 구성 요소
```

```text
toISOString()
→ UTC ISO 문자열

getTime()
Date.now()
→ epoch 기준 밀리초
```

```text
setHours()
setDate()
→ 원본 Date 변경

new Date(
    original.getTime()
)
→ Date 복사
```

---

# 56. 최종 체크리스트

- [ ] `new Date()`로 현재 날짜를 만들 수 있는가?
- [ ] `Date` 출력이 실행 환경에 따라 달라짐을 이해했는가?
- [ ] 연·월·일·시·분·초를 추출할 수 있는가?
- [ ] `getMonth()`가 0부터 시작함을 이해했는가?
- [ ] `getDate()`와 `getDay()`를 구분할 수 있는가?
- [ ] 로컬 getter와 UTC getter를 구분할 수 있는가?
- [ ] `toISOString()`이 UTC 기준임을 설명할 수 있는가?
- [ ] ISO 끝의 `Z` 의미를 이해했는가?
- [ ] ISO 날짜와 로컬 날짜가 다를 수 있음을 이해했는가?
- [ ] `padStart()`로 두 자리 날짜 형식을 만들 수 있는가?
- [ ] `getTime()`과 `Date.now()`를 사용할 수 있는가?
- [ ] timestamp의 단위가 밀리초임을 이해했는가?
- [ ] 두 날짜의 차이를 계산할 수 있는가?
- [ ] `performance.now()`로 실행 시간을 측정할 수 있는가?
- [ ] 날짜 문자열 파싱의 시간대 차이를 주의할 수 있는가?
- [ ] 숫자 인수로 특정 로컬 날짜를 만들 수 있는가?
- [ ] `Invalid Date`를 검사할 수 있는가?
- [ ] setter가 원본 객체를 변경함을 이해했는가?
- [ ] Date 객체를 복사한 뒤 안전하게 변경할 수 있는가?
- [ ] `Intl.DateTimeFormat`으로 날짜를 지역화할 수 있는가?

---

# 마무리

날짜 처리의 핵심은 연·월·일을 꺼내는 것에서 끝나지 않는다.

```text
같은 순간과 표시 시간대를 구분하고
    ↓
로컬 시간과 UTC를 목적에 맞게 선택하고
    ↓
문자열 파싱의 기준을 확인하고
    ↓
원본 Date 변경 여부를 관리하고
    ↓
사용자에게 알맞은 형식으로 출력하는 것
```

이 흐름을 이해하면 예약 시각, 작성 일시, 만료 시간, 경과 시간 같은 실제 기능을 더 안전하게 구현할 수 있다.
