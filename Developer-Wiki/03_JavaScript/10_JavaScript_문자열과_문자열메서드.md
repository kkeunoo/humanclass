# JavaScript 문자열과 문자열 메서드

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `10_JavaScript_문자열과_문자열메서드.md` |
| 분류 | `03_JavaScript` |
| 권장 선수 학습 | `09_JavaScript_화살표함수와_TV상태관리.md` |
| 다음 학습 | `11_JavaScript_객체와_메서드.md` |
| 원본 기준 | `workspace_me/workspace/workspace_html/javascript/10_string.html`, `workspace_teacher/workspace_teacher/workspace_html/javascript/10_string.html` |
| 핵심 범위 | 문자열 길이, `indexOf()`, `replace()`, 정규 표현식 전역 치환, `slice()`, `split()`, `substring()`, `substr()`, `trim()`, 문자열 불변성, 이메일 ID 추출, 주민등록번호 성별 코드, 날짜 문자열 분리, 이메일 마스킹 |
| 프로젝트 연결 | 검색어 처리, 회원가입 입력 검증, 이메일 가림 처리, 로그 문자열 분석, 날짜·시간 파싱, 개인정보 출력 보호 |

> 이 문서는 내 코드와 강사님 코드의 `10_string.html`을 직접 비교해 작성했습니다. 강사님 코드는 문자열 메서드의 기본 사용법과 문제 1~5를 제시하고 문제 5만 구현합니다. 내 코드는 문제 1~5를 직접 풀고 별도의 문제 4 재시도 코드까지 추가했습니다. 원본의 문제 요구와 실제 구현 불일치, 느슨한 비교, 잘못된 성별 판정, `@`가 없을 때의 처리, `replace()` 반복 사용 오류, deprecated된 `substr()` 사용은 원본을 보존한 뒤 별도로 설명합니다.

---

# 학습 목표

- 문자열의 `length`가 문자 수를 나타낸다는 점을 이해한다.
- `indexOf()`로 부분 문자열의 첫 위치를 찾는다.
- 찾지 못했을 때 `-1`을 반환한다는 점을 활용한다.
- `replace()`가 첫 일치 항목만 바꾸는 기본 동작을 이해한다.
- 정규 표현식의 `g` 플래그로 전체 일치 항목을 바꾼다.
- 문자열 메서드가 원본 문자열을 직접 변경하지 않는다는 점을 이해한다.
- `slice()`, `substring()`, `substr()`의 인수 의미를 구분한다.
- `substr()`가 오래된 API라는 점을 이해한다.
- `split()`으로 문자열을 배열로 분리한다.
- `trim()`으로 앞뒤 공백을 제거한다.
- 이메일에서 `@` 앞의 ID를 추출한다.
- 주민등록번호 뒤 첫 숫자로 성별 코드를 판정한다.
- 날짜·시간 문자열에서 월과 분을 추출한다.
- 이메일 ID의 앞 두 글자를 남기고 나머지를 마스킹한다.
- 고정 별표 개수와 실제 가려지는 글자 수만큼 별표를 만드는 요구를 구분한다.
- 내 코드와 강사님 코드의 문제 풀이 차이와 오류를 정확히 설명한다.

---

# 1. 문자열이란?

문자열은 문자들의 순서 있는 집합입니다.

```js
const str =
  "기사도가 죽었을 리가"
```

문자열은 index로 각 문자에 접근할 수 있습니다.

```js
console.log(str[0])
```

첫 문자를 출력합니다.

문자열 index는 배열처럼 0부터 시작합니다.

---

# 2. 원본 문서 구조

두 원본 모두 `<head>` 내부의 `<script>`에서 실습을 실행합니다.

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
    // 문자열 실습
  </script>
</head>
<body>
</body>
</html>
```

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
<title>JavaScript 문자열과 문자열 메서드</title>
```

---

# 4. 문자열 Length

공통 원본:

```js
console.log(
  "str.length : " +
  str.length
)
```

`length`는 문자열의 문자 단위 길이를 반환합니다.

공백도 문자열의 일부이므로 길이에 포함됩니다.

```js
"ab cd".length
```

결과:

```text
5
```

---

# 5. Length의 Unicode 주의

JavaScript의 문자열 length는 내부 UTF-16 code unit 수를 기준으로 계산합니다.

일반적인 한글 한 글자는 대부분 1로 계산되지만 일부 emoji나 결합 문자는 화면상 한 글자와 length가 다를 수 있습니다.

원본 범위에서는 일반 한글과 공백의 길이를 확인합니다.

---

# 6. IndexOf 기본

강사님 코드:

```js
console.log(
  "죽었",
  str.indexOf("죽었")
)
```

내 코드:

```js
console.log(
  "str.indexOf(죽었) : " +
  str.indexOf("죽었")
)
```

`indexOf()`는 찾은 부분 문자열이 시작하는 첫 index를 반환합니다.

원본 주석에 따르면 `"죽었"`의 시작 index는 5입니다.

---

# 7. IndexOf 미발견

공통 원본:

```js
str.indexOf("나")
```

결과:

```text
-1
```

찾지 못한 상태를 검사할 때:

```js
if (
  str.indexOf("나") !== -1
) {
}
```

처럼 사용할 수 있습니다.

---

# 8. 첫 번째 일치 위치

공통 원본:

```js
str.indexOf("가")
```

문자열 안에 같은 글자가 여러 번 있어도 첫 번째 일치 위치만 반환합니다.

내 코드 주석:

```text
동일하게 있어도 앞에서부터, 찾으면 끝
```

핵심적으로 맞습니다.

다음 위치부터 다시 찾으려면 두 번째 인수를 사용할 수 있습니다.

```js
str.indexOf("가", 4)
```

---

# 9. 내 코드의 추가 IndexOf 예제

내 코드에는 다음 주석 처리된 예가 있습니다.

```js
// str.indexOf("죽지")
// → -1
```

강사님 코드에는 없습니다.

존재하지 않는 부분 문자열의 결과를 확인하려는 학습용 예제입니다.

---

# 10. Replace 기본

공통 원본:

```js
let s1 =
  str.replace("죽었", "살았")
```

결과 개념:

```text
기사도가 죽었을 리가
→ 기사도가 살았을 리가
```

`replace()`는 변경된 새 문자열을 반환합니다.

---

# 11. 문자열 불변성

공통 원본:

```js
console.log(str)
console.log(s1)
```

`replace()` 호출 후에도 원본 `str`은 그대로입니다.

문자열은 immutable 값입니다.

```text
str
→ 기존 문자열 유지

s1
→ 변경 결과가 저장된 새 문자열
```

내 코드 주석:

```text
string쪽은 거의 원본값을 바꾸지 않음
```

보다 정확한 표현은:

```text
문자열 메서드는 문자열 자체를 직접 수정하지 않고 새 문자열을 반환한다.
```

입니다.

---

# 12. Replace의 첫 일치 항목

공통 원본:

```js
let s2 =
  str.replace("가", "나")
```

기본 문자열 인수를 사용하면 첫 번째 `"가"`만 `"나"`로 바뀝니다.

문자열 전체의 모든 `"가"`를 바꾸지는 않습니다.

---

# 13. 정규 표현식 전역 치환

공통 원본:

```js
s2 =
  str.replace(/가/g, "나")
```

구성:

```text
/가/
→ 찾을 정규 표현식 패턴

g
→ global, 전체 일치 항목
```

문자열 안의 모든 `"가"`를 `"나"`로 바꿉니다.

---

# 14. 내 정규 표현식 설명 검토

내 코드:

```text
Regular Expression /VALUE/i
패턴구분자+찾을 문자열 패턴+패턴구분자+
패턴변경자(g는 global)
```

설명 속 `/VALUE/i`는 대소문자를 구분하지 않는 `i` 플래그 예시이고 실제 코드는 `/가/g`를 사용합니다.

`i`와 `g`는 서로 다른 플래그입니다.

```text
g → 모든 일치 항목
i → 영문 대소문자 무시
```

한글 `"가"`에는 대소문자 개념이 없으므로 현재 목적에는 `g`가 핵심입니다.

---

# 15. ReplaceAll 확장

문자열 전체를 단순 문자열 기준으로 바꾸려면 현대 JavaScript에서 다음을 사용할 수 있습니다.

```js
str.replaceAll("가", "나")
```

원본은 정규 표현식 `g` 플래그를 학습합니다.

---

# 16. Slice

공통 원본:

```js
str.slice(3, 6)
```

규칙:

```text
시작 index 포함
끝 index 제외
```

index 3, 4, 5에 해당하는 부분을 복사합니다.

원본 문자열은 변경되지 않습니다.

---

# 17. Slice 음수 Index

`slice()`는 음수 index를 사용할 수 있습니다.

```js
"abcdef".slice(-3)
```

결과:

```text
def
```

뒤에서 세 번째 문자부터 끝까지 추출합니다.

원본에는 양수 index 예제만 있습니다.

---

# 18. Split

공통 원본:

```js
str.split(" ")
```

공백을 기준으로 문자열을 나누어 배열로 반환합니다.

예상 형태:

```js
["기사도가", "죽었을", "리가"]
```

구분자 공백 자체는 결과 배열에 포함되지 않습니다.

---

# 19. Split의 빈 구분자

문자 단위로 분리하려면:

```js
"abc".split("")
```

결과:

```js
["a", "b", "c"]
```

복잡한 Unicode 문자에서는 화면상 글자 단위와 완전히 일치하지 않을 수 있습니다.

---

# 20. Substring

공통 원본:

```js
let s =
  str.substring(3, 6)
```

기본 양수 범위에서는 `slice(3, 6)`과 같은 결과를 냅니다.

둘 다 시작 index를 포함하고 끝 index는 제외합니다.

---

# 21. Slice와 Substring 차이

주요 차이:

```text
slice()
→ 음수 index를 뒤에서부터 계산

substring()
→ 음수 값을 0으로 처리
→ 시작값이 끝값보다 크면 서로 교환
```

예:

```js
"abcdef".slice(4, 1)
// ""

"abcdef".substring(4, 1)
// "bcd"
```

내 코드 주석:

```text
substring은 slice와 동일한 역할
```

기본 양수 예제에서는 같아 보이지만 모든 동작이 동일하지는 않습니다.

---

# 22. Substr

공통 원본:

```js
s = str.substr(3, 7)
```

인수 의미:

```text
3
→ 시작 index

7
→ 가져올 문자 개수
```

`slice()`와 `substring()`의 두 번째 인수가 끝 index인 것과 다릅니다.

---

# 23. Substr 사용 주의

`String.prototype.substr()`는 오래된 legacy 메서드입니다.

새 코드에서는 일반적으로 `slice()` 또는 `substring()`을 사용합니다.

동일한 의도:

```js
str.substr(3, 7)
```

대체:

```js
str.slice(3, 3 + 7)
```

원본의 API는 그대로 기록하고 개선 방향을 분리합니다.

---

# 24. Trim

공통 원본:

```js
let str2 =
  "    1 2  3   "

s = str2.trim()
```

`trim()`은 문자열 앞과 뒤의 공백을 제거합니다.

문자열 내부의 공백은 유지합니다.

결과 개념:

```text
"1 2  3"
```

---

# 25. Trim은 원본을 변경하지 않음

```js
const trimmed =
  str2.trim()
```

`str2` 자체는 기존 공백을 유지합니다.

변경된 값을 사용하려면 반환값을 변수에 저장해야 합니다.

---

# 26. 입력값 검사

강사님 코드:

```js
str2 = "      "

if (str2.length != 0) {
}

if (
  str2.trim().length != 0
) {
}
```

첫 조건은 공백 문자들이 있으므로 true입니다.

두 번째 조건은 앞뒤 공백을 제거하면 빈 문자열이므로 false입니다.

로그인·검색 입력에서 공백만 입력한 경우를 걸러내는 데 유용합니다.

---

# 27. 내 입력값 차이

내 코드:

```js
str2 = "abc"
```

따라서:

```text
str2.length != 0
→ true

str2.trim().length != 0
→ true
```

공백만 입력한 경우를 실제로 비교하려던 강사님 예제의 효과가 사라졌습니다.

내 주석은 공백 입력 검사를 설명하지만 실제 값 `"abc"`는 그 상황을 테스트하지 않습니다.

---

# 28. 느슨한 비교

공통 원본:

```js
str2.length != 0
pos != -1
```

숫자끼리 비교하므로 현재 코드에서는 동작합니다.

일관된 엄격 비교 개선:

```js
str2.length !== 0
pos !== -1
```

---

# 29. 문제 1: 이메일 ID 추출

강사님은 문제만 제시합니다.

내 코드:

```js
function emailValue(email) {
  emailCheck =
    email.indexOf("@")

  console.log(
    "ID : " +
    email.slice(0, emailCheck)
  )
}
```

테스트:

```js
emailValue("abcd@naver.com")
emailValue("abcdef@google.com")
emailValue("abcdefgh@daum.net")
```

출력 ID:

```text
abcd
abcdef
abcdefgh
```

---

# 30. 문제 1의 전역 변수

내 코드:

```js
let emailCheck
```

함수 내부에서 매번 값을 대입합니다.

다른 함수가 이 값을 사용할 필요가 없으므로 지역 변수로 선언하는 편이 안전합니다.

```js
function emailValue(email) {
  const atIndex =
    email.indexOf("@")
}
```

---

# 31. 문제 1의 At 미발견 오류

`@`가 없으면:

```js
email.indexOf("@")
// -1
```

이후:

```js
email.slice(0, -1)
```

가 실행되어 마지막 문자를 제외한 문자열을 ID처럼 출력합니다.

즉, 올바른 오류 처리가 아닙니다.

개선:

```js
if (atIndex === -1) {
  console.log("올바른 이메일이 아닙니다.")
  return
}
```

---

# 32. 문제 1 Split 풀이

간단한 형태:

```js
const id =
  email.split("@")[0]
```

그러나 `@`가 없는 문자열도 그대로 첫 요소로 반환하므로 여전히 유효성 검사가 필요합니다.

원본 강사님 주석에도 문제 5에서 `split("@")[0]` 대안이 적혀 있습니다.

---

# 33. 문제 2: 주민번호 성별 출력

내 코드:

```js
function genderValue(gender) {
  genderCheck =
    gender.indexOf("-")

  genderResult =
    gender.substr(
      genderCheck + 1,
      1
    )

  if (genderResult == 1) {
    console.log("남자입니다")
  } else {
    console.log("여자입니다")
  }
}
```

테스트:

```text
960119-1111111
→ 남자

960119-2111111
→ 여자
```

현재 두 테스트에서는 기대대로 동작합니다.

---

# 34. 성별 코드 범위

일반적인 주민등록번호 뒤 첫 숫자에는 여러 코드가 존재할 수 있습니다.

기본 학습 범위:

```text
1, 3
→ 남성

2, 4
→ 여성
```

현재 내 코드는 1만 남성으로 처리하고 나머지는 모두 여성으로 처리합니다.

따라서 3은 잘못 여성으로 판정됩니다.

---

# 35. 성별 코드 입력 검증

현재 코드는 다음도 모두 여성으로 출력할 수 있습니다.

```text
잘못된 문자열
하이픈 없음
빈 문자열
코드 9
```

개선:

```js
if (
  code === "1" ||
  code === "3"
) {
  console.log("남자입니다")
} else if (
  code === "2" ||
  code === "4"
) {
  console.log("여자입니다")
} else {
  console.log("확인할 수 없습니다.")
}
```

개인정보 예제이므로 실제 서비스에서는 원문 주민번호를 Console에 출력하거나 불필요하게 저장하지 않아야 합니다.

---

# 36. 문제 2의 Substr 대체

원본:

```js
gender.substr(
  genderCheck + 1,
  1
)
```

대체:

```js
gender.slice(
  genderCheck + 1,
  genderCheck + 2
)
```

또는 하이픈 위치가 확실할 때:

```js
gender.split("-")[1][0]
```

각 단계의 유효성 검사가 필요합니다.

---

# 37. 문제 3: 월과 분 구하기

내 코드:

```js
const value =
  "2026-07-14 12:43:19"
```

함수:

```js
function resultCheck(date) {
  dateValue =
    date.split(" ")

  monthCheck =
    dateValue[0].split("-")

  minCheck =
    dateValue[1].split(":")

  console.log(
    `${monthCheck[1]}월, ` +
    `${minCheck[1]}분 입니다`
  )
}
```

출력:

```text
07월, 43분 입니다
```

---

# 38. 문제 3의 전역 변수

내 코드:

```js
let dateValue
let monthCheck
let minCheck
```

모두 함수 내부에서만 사용합니다.

지역 변수로 바꾸는 것이 좋습니다.

```js
function resultCheck(date) {
  const dateValue =
    date.split(" ")
}
```

전역 변수를 줄이면 다른 함수와 값이 충돌할 가능성이 낮아집니다.

---

# 39. 문제 3 입력 형식 의존

현재 코드는 정확히 다음 형식을 전제로 합니다.

```text
YYYY-MM-DD HH:mm:ss
```

공백이나 구분자가 다르면 오류가 발생할 수 있습니다.

```js
dateValue[1].split(":")
```

에서 `dateValue[1]`이 undefined이면 TypeError가 발생합니다.

입력 구조를 먼저 검증해야 합니다.

---

# 40. 문제 3 정규 표현식 확장

형식이 정확할 때 정규 표현식으로 추출할 수도 있습니다.

```js
const match =
  value.match(
    /^\d{4}-(\d{2})-\d{2} \d{2}:(\d{2}):\d{2}$/
  )
```

원본은 `split()` 연습이 목적이므로 단계별 배열 분리가 적절합니다.

---

# 41. 문제 4 요구사항

내 코드:

```text
앞 2글자만 제대로 표기
별표 4개 표시
@부터 전부 출력

todair@naver.com
→ to****@naver.com
```

이 요구는 **별표를 항상 4개 표시**하는 문제입니다.

ID 실제 길이와 관계없이 결과가 고정된 별표 4개여야 합니다.

---

# 42. 내 첫 번째 문제 4 구현

내 코드:

```js
let testLEN =
  testID.length - 2

let testSEC = ""

for (
  let i = 0;
  i < testLEN;
  i++
) {
  testSEC += "*"
}
```

이 코드는 앞 두 글자를 제외한 실제 ID 길이만큼 별표를 만듭니다.

`study.todair`처럼 긴 ID라면 별표가 4개보다 많아집니다.

즉, 문제 4의 “항상 별표 4개” 요구보다 문제 5의 “가려진 개수만큼” 요구에 가깝습니다.

---

# 43. 문제 4의 테스트 결과

입력:

```text
study.todair@gmail.com
```

ID:

```text
study.todair
```

앞 두 글자:

```text
st
```

나머지 ID 문자 수만큼 별표를 만들기 때문에 결과 개념은:

```text
st**********@gmail.com
```

점도 ID 문자이므로 별표로 바뀝니다.

문제 4 주석의 `to****@...`처럼 별표 4개 고정 구현은 아닙니다.

---

# 44. 고정 별표 4개 구현

문제 4 요구 그대로:

```js
function maskFixed(email) {
  const atIndex =
    email.indexOf("@")

  if (atIndex < 2) {
    return "잘못된 이메일"
  }

  const prefix =
    email.slice(0, 2)

  const domain =
    email.slice(atIndex)

  return (
    prefix +
    "****" +
    domain
  )
}
```

입력 ID 길이와 관계없이 별표는 항상 네 개입니다.

---

# 45. 두 번째 문제 4 재시도

내 코드에는 문제 4 제목이 한 번 더 나옵니다.

```js
function secCheck(email) {
  sumCheck =
    email.indexOf("@")

  for (
    let j = 2;
    j < sumCheck;
    j++
  ) {
    securityEmail =
      email.replace(
        email[j],
        "*"
      )

    console.log(
      securityEmail
    )
  }
}
```

완성된 마스킹 문자열 하나를 만드는 대신 반복마다 서로 다른 중간 문자열을 출력합니다.

---

# 46. 두 번째 문제 4의 Replace 오류

매 반복에서 항상 원본 `email`에 대해 `replace()`를 실행합니다.

```js
securityEmail =
  email.replace(
    email[j],
    "*"
  )
```

이전 반복의 마스킹 결과를 이어서 사용하지 않습니다.

따라서 한 번에 문자 하나만 별표로 바뀐 문자열이 출력됩니다.

최종적으로 전체 ID가 가려진 하나의 문자열을 만들지 못합니다.

---

# 47. 중복 문자와 Replace 문제

`replace(email[j], "*")`는 해당 문자의 **첫 번째 일치 항목**을 바꿉니다.

현재 index j의 정확한 위치를 바꾸는 것이 아닙니다.

예를 들어 동일 문자가 앞에도 있으면 앞 문자가 바뀔 수 있습니다.

따라서 위치 기반 마스킹에 `replace()`를 반복 사용하는 방식은 적절하지 않습니다.

---

# 48. 문제 4 중복 번호

내 코드에는 다음 구분선이 두 번 있습니다.

```text
문제4
```

첫 번째는 실제 별표 문자열을 완성합니다.

두 번째는 `secCheck()` 재시도이며 완성된 단일 결과를 만들지 못합니다.

원본의 중복 문제 번호를 그대로 기록합니다.

---

# 49. 문제 5 요구사항

강사님 원본:

```text
앞 두 글자만 표시
가려진 개수만큼 별표

study.todair@gmail.com
→ st**********@gmail.com
```

내 코드 주석:

```text
study.todair@gmail.com
→ st***.******@gmail.com
```

두 설명이 다릅니다.

내 실제 코드는 ID의 점까지 모두 별표로 바꾸므로 강사님 예시처럼:

```text
st**********@gmail.com
```

형태가 됩니다.

내 주석의 `st***.******`처럼 점을 보존하지 않습니다.

---

# 50. 문제 5 구현

공통 핵심 구조:

```js
let pos =
  email.indexOf("@")

let id = ""

if (pos != -1) {
  id =
    email.slice(0, pos)
}

let mask_id_1 =
  id.slice(0, 2)

let len =
  id.length - 2

let mask_id_2 = ""

for (
  let i = 0;
  i < len;
  i++
) {
  mask_id_2 += "*"
}
```

결합:

```js
mask_id_1 +
mask_id_2 +
email.slice(pos)
```

강사님은 마지막에 `substring(pos)`를 사용합니다.

양쪽 결과는 현재 양수 index에서 같습니다.

---

# 51. 문제 5의 At 미발견 오류

`@`가 없으면:

```text
pos → -1
id → ""
len → -2
반복문 실행 안 함
email.slice(-1)
→ 마지막 문자
```

결과가 정상 오류 메시지가 아니라:

```text
마지막 문자 하나
```

처럼 나올 수 있습니다.

`pos === -1`이면 즉시 종료해야 합니다.

---

# 52. 짧은 ID 문제

ID 길이가 2보다 짧은 이메일:

```text
a@example.com
```

현재:

```js
len =
  id.length - 2
```

는 음수가 됩니다.

반복문은 실행되지 않고 앞 두 글자 slice 결과만 사용합니다.

요구사항에 따라 최소 ID 길이를 검증하거나 존재하는 문자만 보존해야 합니다.

---

# 53. Repeat 활용 개선

별표 문자열은 반복문 대신 `repeat()`로 만들 수 있습니다.

```js
const mask =
  "*".repeat(
    id.length - 2
  )
```

음수 repeat는 RangeError가 발생하므로 최소값을 보정합니다.

```js
const hiddenLength =
  Math.max(0, id.length - 2)

const mask =
  "*".repeat(hiddenLength)
```

---

# 54. 문제 5 개선 함수

```js
function maskEmail(email) {
  const atIndex =
    email.indexOf("@")

  if (
    atIndex === -1 ||
    atIndex < 1
  ) {
    return "올바른 이메일이 아닙니다."
  }

  const id =
    email.slice(0, atIndex)

  const domain =
    email.slice(atIndex)

  const visibleLength =
    Math.min(2, id.length)

  const visible =
    id.slice(0, visibleLength)

  const hidden =
    "*".repeat(
      id.length - visibleLength
    )

  return (
    visible +
    hidden +
    domain
  )
}
```

---

# 55. 점을 보존하는 마스킹

내 문제 5 주석처럼 점을 보존하려면 문자별 조건이 필요합니다.

```js
function maskEmailKeepDot(email) {
  const [id, domain] =
    email.split("@")

  if (
    !id ||
    !domain
  ) {
    return "잘못된 이메일"
  }

  const maskedId =
    [...id]
      .map(
        (char, index) => {
          if (index < 2) {
            return char
          }

          return (
            char === "."
              ? "."
              : "*"
          )
        }
      )
      .join("")

  return (
    maskedId +
    "@" +
    domain
  )
}
```

입력:

```text
study.todair@gmail.com
```

결과:

```text
st***.******@gmail.com
```

이는 내 주석과 일치하지만 현재 원본 실제 구현과는 다릅니다.

---

# 56. My Code 분석

## 56.1 장점

- 문자열 원본이 직접 변경되지 않는다는 점을 설명했다.
- `indexOf()`의 발견·미발견 결과를 자세히 주석으로 기록했다.
- `replace()`가 첫 일치 항목만 바꾼다는 점을 설명했다.
- 정규 표현식의 global 플래그를 소개했다.
- `slice()`, `split()`, `substring()`, `substr()`, `trim()`에 설명을 추가했다.
- 문제 1 이메일 ID 추출을 함수로 구현했다.
- 문제 2 주민번호 성별 판정을 함수로 구현했다.
- 문제 3 날짜 문자열에서 월과 분을 추출했다.
- 문제 4 이메일 마스킹을 직접 구현했다.
- 문제 4를 다른 방식으로 다시 시도했다.
- 문제 5에서 ID 길이에 맞춰 별표 개수를 동적으로 생성했다.
- `@`가 있는 경우에만 ID를 자르는 조건을 추가했다.
- 여러 테스트 이메일을 사용해 함수 결과를 확인했다.

## 56.2 개선점

- “문자열 메서드는 거의 원본을 바꾸지 않는다”보다 문자열은 불변이라고 명확히 설명하는 것이 좋다.
- 정규 표현식 설명에서 `/VALUE/i`와 실제 `/가/g` 플래그가 섞여 있다.
- `substring()`이 `slice()`와 완전히 같다는 설명은 부정확하다.
- 오래된 `substr()`를 사용한다.
- 공백 검증 주석과 달리 실제 `str2`는 `"abc"`여서 공백만 입력한 상황을 테스트하지 않는다.
- 문제 함수의 임시값을 전역 변수로 선언한다.
- 이메일에 `@`가 없을 때 마지막 문자를 제외한 ID를 출력할 수 있다.
- 성별 코드는 1만 남성으로 판정하고 그 외 모든 값을 여성으로 처리한다.
- 주민번호 입력 형식과 코드 유효성을 검사하지 않는다.
- 문제 3은 문자열 형식이 조금만 달라도 TypeError가 발생할 수 있다.
- 문제 4 요구는 별표 4개 고정인데 첫 구현은 실제 ID 길이만큼 별표를 만든다.
- 문제 4가 중복 번호로 두 번 등장한다.
- 두 번째 문제 4는 이전 마스킹 결과를 누적하지 않는다.
- `replace(email[j], "*")`는 현재 index가 아닌 첫 일치 문자를 바꿀 수 있다.
- 문제 5 주석은 점을 보존하지만 실제 코드는 점도 별표로 바꾼다.
- 문제 5에서 `@`가 없거나 ID가 너무 짧을 때의 처리가 부족하다.
- 비교에 `!=`, `==`를 사용한다.

---

# 57. Teacher Code 분석

## 57.1 장점

- 문자열 length와 indexOf를 간결하게 소개한다.
- 찾은 위치와 미발견 -1을 실제로 출력한다.
- replace 전후 원본 문자열을 비교한다.
- 첫 일치 치환과 정규 표현식 전체 치환을 비교한다.
- slice, split, substring, substr, trim을 순서대로 실습한다.
- 공백만 있는 문자열에서 일반 length와 trim length를 비교한다.
- 문제 1~5의 요구사항을 순서대로 제시한다.
- 문제 5에서 이메일 ID 길이만큼 별표를 만드는 풀이를 제공한다.
- `@` 위치가 있는 경우에만 ID를 추출한다.
- 마지막 도메인 결합에 `substring(pos)`를 사용한다.

## 57.2 개선점

- 문자열 불변성을 명확한 용어로 설명하지 않는다.
- 정규 표현식 `g` 플래그 외의 안전한 문자열 처리 설명이 없다.
- `substring()`과 `slice()` 차이를 설명하지 않는다.
- legacy 메서드인 `substr()`를 사용한다.
- 느슨한 비교를 사용한다.
- 문제 1~4는 정답 코드가 없다.
- 문제 5에서 `@`가 없을 때의 오류 처리가 완전하지 않다.
- ID가 두 글자보다 짧을 때의 정책이 없다.
- 이메일 유효성 전체를 검증하지 않는다.
- 문서 제목과 언어가 학습 내용에 맞지 않는다.
- 문제 4 주석의 `지대루`는 구어체·오타성 표현이다.

---

# 58. My Code vs Teacher Code

| 비교 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 첫 문자열 출력 | `console.log(str)` 추가 | 없음 |
| IndexOf 설명 | 상세 | 핵심만 |
| `"죽지"` 예제 | 주석으로 있음 | 없음 |
| 정규 표현식 설명 | 상세, 플래그 설명 혼재 | 간결 |
| Trim 테스트 값 | `"abc"` | 공백만 있는 문자열 |
| 문제 1 풀이 | 있음 | 문제만 |
| 문제 2 풀이 | 있음, 판정 범위 부족 | 문제만 |
| 문제 3 풀이 | 있음 | 문제만 |
| 문제 4 첫 풀이 | 있음, 고정 4개 요구와 불일치 | 문제만 |
| 문제 4 재시도 | 있음, 미완성 | 없음 |
| 문제 4 번호 | 두 번 등장 | 한 번 |
| 문제 5 예시 | 점 보존 `st***.******` | 점도 마스킹 |
| 문제 5 실제 결과 | 점도 마스킹 | 점도 마스킹 |
| 마지막 도메인 추출 | `slice(pos)` | `substring(pos)` |
| 전역 임시 변수 | 다수 | 상대적으로 적음 |
| 전체 코드 길이 | 문제 풀이로 길음 | 기본 개념 중심 |

---

# 59. 공통 핵심 코드

```js
const str =
  "기사도가 죽었을 리가"

console.log(str.length)

console.log(
  str.indexOf("죽었")
)

const replaced =
  str.replace(
    "죽었",
    "살았"
  )

const allReplaced =
  str.replace(
    /가/g,
    "나"
  )

const part =
  str.slice(3, 6)

const words =
  str.split(" ")

const trimmed =
  "   text   ".trim()
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
  <title>JavaScript 문자열 메서드</title>
  <script>
    "use strict";

    const source =
      "기사도가 죽었을 리가";

    console.log(
      "길이:",
      source.length
    );

    console.log(
      "죽었 위치:",
      source.indexOf("죽었")
    );

    console.log(
      "첫 치환:",
      source.replace(
        "가",
        "나"
      )
    );

    console.log(
      "전체 치환:",
      source.replaceAll(
        "가",
        "나"
      )
    );

    console.log(
      "부분 문자열:",
      source.slice(3, 6)
    );

    console.log(
      "단어 배열:",
      source.split(" ")
    );

    console.log(
      "공백 제거:",
      "   hello   ".trim()
    );
  </script>
</head>
<body>
  <h1>JavaScript 문자열 메서드</h1>
</body>
</html>
```

---

# 61. 이메일 ID 추출 개선 예제

```js
function getEmailId(email) {
  const atIndex =
    email.indexOf("@")

  if (
    atIndex <= 0 ||
    atIndex ===
      email.length - 1
  ) {
    return null
  }

  return email.slice(0, atIndex)
}

const id =
  getEmailId(
    "abcd@naver.com"
  )

if (id === null) {
  console.log(
    "올바른 이메일이 아닙니다."
  )
} else {
  console.log(
    `ID : ${id}`
  )
}
```

---

# 62. 성별 코드 개선 예제

```js
function getGenderLabel(number) {
  const dashIndex =
    number.indexOf("-")

  if (
    dashIndex === -1 ||
    dashIndex ===
      number.length - 1
  ) {
    return "확인할 수 없습니다."
  }

  const code =
    number.slice(
      dashIndex + 1,
      dashIndex + 2
    )

  if (
    code === "1" ||
    code === "3"
  ) {
    return "남자입니다"
  }

  if (
    code === "2" ||
    code === "4"
  ) {
    return "여자입니다"
  }

  return "확인할 수 없습니다."
}
```

---

# 63. 날짜 문자열 개선 예제

```js
function getMonthAndMinute(value) {
  const parts =
    value.split(" ")

  if (parts.length !== 2) {
    return null
  }

  const dateParts =
    parts[0].split("-")

  const timeParts =
    parts[1].split(":")

  if (
    dateParts.length !== 3 ||
    timeParts.length !== 3
  ) {
    return null
  }

  return {
    month: dateParts[1],
    minute: timeParts[1]
  }
}

const result =
  getMonthAndMinute(
    "2026-07-14 12:43:19"
  )

if (result !== null) {
  console.log(
    `${result.month}월, ` +
    `${result.minute}분 입니다`
  )
}
```

---

# 64. 자주 하는 실수

## 64.1 IndexOf 결과 0을 False처럼 처리

첫 위치에서 찾으면 0이므로 `if (index)`만 사용하면 잘못 판정할 수 있습니다.

## 64.2 IndexOf 미발견 후 Slice 실행

-1이 음수 index로 사용되어 예상하지 않은 문자열이 나올 수 있습니다.

## 64.3 Replace가 모든 문자를 바꾼다고 생각

문자열 검색값은 첫 일치 항목만 바꿉니다.

## 64.4 문자열 원본이 직접 수정된다고 생각

문자열 메서드는 새 문자열을 반환합니다.

## 64.5 Slice와 Substring이 완전히 같다고 생각

음수 처리와 시작·끝 순서에서 차이가 있습니다.

## 64.6 Substr 두 번째 인수를 끝 Index로 생각

두 번째 인수는 문자 개수입니다.

## 64.7 Trim이 문자열 내부 공백도 제거한다고 생각

앞뒤 공백만 제거합니다.

## 64.8 성별 코드 1 외 모든 값을 여성으로 처리

3과 잘못된 값까지 여성으로 판정합니다.

## 64.9 마스킹 반복마다 원본에 Replace 적용

이전 마스킹 결과가 누적되지 않습니다.

## 64.10 요구사항의 점 보존 여부와 실제 코드 불일치

내 문제 5 주석은 점을 남기지만 실제 코드는 점도 별표로 바꿉니다.

---

# 65. 면접·복습 포인트

## Q1. `indexOf()`가 찾지 못했을 때 반환하는 값은 무엇인가요?

-1입니다.

## Q2. 문자열의 `replace()`는 원본을 변경하나요?

아닙니다. 변경된 새 문자열을 반환합니다.

## Q3. 모든 일치 항목을 바꾸는 방법은 무엇인가요?

정규 표현식의 `g` 플래그 또는 `replaceAll()`을 사용할 수 있습니다.

## Q4. `slice(3, 6)`의 범위는 무엇인가요?

index 3을 포함하고 index 6은 제외합니다.

## Q5. `substring()`과 `slice()`의 주요 차이는 무엇인가요?

substring은 음수를 0으로 처리하고 시작값이 더 크면 두 값을 교환합니다. slice는 음수를 뒤쪽 index로 해석합니다.

## Q6. `substr(3, 7)`의 두 번째 인수는 무엇인가요?

끝 index가 아니라 가져올 문자 개수입니다.

## Q7. Trim은 어떤 공백을 제거하나요?

문자열 앞과 뒤의 공백을 제거하며 내부 공백은 유지합니다.

## Q8. 내 문제 2 성별 판정의 오류는 무엇인가요?

1만 남성으로 처리하고 3과 잘못된 코드까지 여성으로 처리합니다.

## Q9. 두 번째 문제 4 구현이 완성된 마스킹을 만들지 못하는 이유는 무엇인가요?

매 반복마다 원본 이메일에서 한 문자만 바꾸고 이전 변경 결과를 이어서 사용하지 않기 때문입니다.

## Q10. 내 문제 5 주석과 실제 결과의 차이는 무엇인가요?

주석은 ID의 점을 보존하지만 실제 코드는 앞 두 글자 이후의 점까지 모두 별표로 바꿉니다.

---

# Problems

## 문제 1. 문자열 길이

문자열 `"JavaScript"`의 길이를 출력하세요.

## 문제 2. IndexOf

문자열 `"hello world"`에서 `"world"`의 시작 index를 찾으세요.

## 문제 3. 미발견 검사

문자열에 `"java"`가 없을 때 `"찾을 수 없음"`을 출력하세요.

## 문제 4. 첫 번째 Replace

문자열 `"a-b-a-b"`에서 첫 번째 `"a"`만 `"x"`로 바꾸세요.

## 문제 5. 전체 Replace

문자열 `"a-b-a-b"`의 모든 `"a"`를 `"x"`로 바꾸세요.

## 문제 6. 문자열 불변성

`replace()` 전후의 원본 문자열과 새 문자열을 모두 출력하세요.

## 문제 7. Slice

문자열 `"abcdef"`에서 `"bcd"`를 추출하세요.

## 문제 8. Split

문자열 `"html,css,javascript"`를 쉼표 기준 배열로 만드세요.

## 문제 9. Substring 차이

`"abcdef".slice(4, 1)`과 `substring(4, 1)`의 결과 차이를 설명하세요.

## 문제 10. Trim

공백만 입력한 문자열을 trim한 뒤 빈 값인지 검사하세요.

## 문제 11. 이메일 ID

`"student@example.com"`에서 `"student"`를 추출하세요.

## 문제 12. 이메일 검증

`@`가 없는 문자열이면 오류 메시지를 반환하도록 문제 11을 개선하세요.

## 문제 13. 성별 코드

뒤 첫 숫자가 1·3이면 남성, 2·4이면 여성으로 출력하세요.

## 문제 14. 잘못된 성별 코드

뒤 첫 숫자가 1~4 범위가 아니면 `"확인할 수 없습니다"`를 출력하세요.

## 문제 15. 날짜 월 추출

`"2026-07-14 12:43:19"`에서 월 `"07"`을 추출하세요.

## 문제 16. 날짜 분 추출

같은 문자열에서 분 `"43"`을 추출하세요.

## 문제 17. 고정 마스킹

`"todair@naver.com"`을 `"to****@naver.com"`으로 만드세요.

## 문제 18. 길이 기반 마스킹

`"study.todair@gmail.com"`에서 앞 두 글자만 남기고 나머지 ID 문자를 모두 별표로 바꾸세요.

## 문제 19. 점 보존 마스킹

문제 18에서 ID 안의 점은 그대로 남기세요.

## 문제 20. 원본 오류 분석

내 두 번째 문제 4의 `email.replace(email[j], "*")` 방식이 잘못된 이유를 설명하세요.

## 문제 21. Substr 대체

`str.substr(3, 7)`을 `slice()`로 바꾸세요.

## 문제 22. 종합 개인정보 출력

다음 요구사항을 만족하는 함수를 작성하세요.

- 이메일 문자열을 인수로 받음
- 앞뒤 공백 제거
- 정확히 하나의 `@`가 있어야 함
- ID와 도메인이 모두 비어 있지 않아야 함
- ID 앞 두 글자만 표시
- ID의 점은 보존
- 나머지 ID 문자는 별표
- 잘못된 이메일이면 오류 문자열 반환
- 원본 이메일 문자열은 변경하지 않음

---

# Answers & Explanations

## 정답 1

```js
const value =
  "JavaScript"

console.log(
  value.length
)
```

## 정답 2

```js
const value =
  "hello world"

console.log(
  value.indexOf("world")
)
```

결과는 6입니다.

## 정답 3

```js
const value =
  "hello world"

if (
  value.indexOf("java") === -1
) {
  console.log("찾을 수 없음")
}
```

## 정답 4

```js
const value =
  "a-b-a-b"

console.log(
  value.replace("a", "x")
)
```

## 정답 5

```js
const value =
  "a-b-a-b"

console.log(
  value.replace(/a/g, "x")
)
```

또는:

```js
console.log(
  value.replaceAll("a", "x")
)
```

## 정답 6

```js
const original =
  "hello world"

const changed =
  original.replace(
    "world",
    "JavaScript"
  )

console.log(original)
console.log(changed)
```

## 정답 7

```js
const value = "abcdef"

console.log(
  value.slice(1, 4)
)
```

## 정답 8

```js
const value =
  "html,css,javascript"

const result =
  value.split(",")

console.log(result)
```

## 정답 9

```js
console.log(
  "abcdef".slice(4, 1)
)

console.log(
  "abcdef".substring(4, 1)
)
```

`slice(4, 1)`은 빈 문자열이고 `substring(4, 1)`은 인수를 교환해 `"bcd"`를 반환합니다.

## 정답 10

```js
const input = "     "

if (
  input.trim().length === 0
) {
  console.log("빈 값")
}
```

## 정답 11

```js
const email =
  "student@example.com"

const atIndex =
  email.indexOf("@")

const id =
  email.slice(0, atIndex)

console.log(id)
```

## 정답 12

```js
function getEmailId(email) {
  const atIndex =
    email.indexOf("@")

  if (atIndex === -1) {
    return "올바른 이메일이 아닙니다."
  }

  return email.slice(0, atIndex)
}
```

## 정답 13

```js
function printGender(code) {
  if (
    code === "1" ||
    code === "3"
  ) {
    console.log("남자입니다")
  } else if (
    code === "2" ||
    code === "4"
  ) {
    console.log("여자입니다")
  }
}

const number =
  "960119-3111111"

const dash =
  number.indexOf("-")

printGender(
  number.slice(
    dash + 1,
    dash + 2
  )
)
```

## 정답 14

```js
function getGender(code) {
  if (
    code === "1" ||
    code === "3"
  ) {
    return "남자입니다"
  }

  if (
    code === "2" ||
    code === "4"
  ) {
    return "여자입니다"
  }

  return "확인할 수 없습니다"
}
```

## 정답 15

```js
const value =
  "2026-07-14 12:43:19"

const datePart =
  value.split(" ")[0]

const month =
  datePart.split("-")[1]

console.log(month)
```

## 정답 16

```js
const value =
  "2026-07-14 12:43:19"

const timePart =
  value.split(" ")[1]

const minute =
  timePart.split(":")[1]

console.log(minute)
```

## 정답 17

```js
function maskFixed(email) {
  const atIndex =
    email.indexOf("@")

  if (atIndex < 2) {
    return "잘못된 이메일"
  }

  return (
    email.slice(0, 2) +
    "****" +
    email.slice(atIndex)
  )
}

console.log(
  maskFixed(
    "todair@naver.com"
  )
)
```

## 정답 18

```js
function maskEmail(email) {
  const atIndex =
    email.indexOf("@")

  if (atIndex === -1) {
    return "잘못된 이메일"
  }

  const id =
    email.slice(0, atIndex)

  const domain =
    email.slice(atIndex)

  const visible =
    id.slice(0, 2)

  const hidden =
    "*".repeat(
      Math.max(
        0,
        id.length - 2
      )
    )

  return (
    visible +
    hidden +
    domain
  )
}
```

## 정답 19

```js
function maskKeepDot(email) {
  const atIndex =
    email.indexOf("@")

  if (atIndex === -1) {
    return "잘못된 이메일"
  }

  const id =
    email.slice(0, atIndex)

  const domain =
    email.slice(atIndex)

  const masked =
    [...id]
      .map(
        (char, index) => {
          if (index < 2) {
            return char
          }

          return (
            char === "."
              ? "."
              : "*"
          )
        }
      )
      .join("")

  return masked + domain
}
```

## 정답 20

매 반복마다 변경 전 원본 `email`에 `replace()`를 실행하므로 앞선 별표 변경이 누적되지 않습니다. 또한 문자열 인수 `replace()`는 현재 index 위치가 아니라 같은 문자의 첫 일치 위치를 바꿀 수 있습니다.

## 정답 21

```js
const result =
  str.slice(3, 3 + 7)
```

즉:

```js
str.slice(3, 10)
```

입니다.

## 정답 22

```js
function maskPersonalEmail(source) {
  const email =
    source.trim()

  const firstAt =
    email.indexOf("@")

  const lastAt =
    email.lastIndexOf("@")

  if (
    firstAt <= 0 ||
    firstAt !== lastAt ||
    firstAt ===
      email.length - 1
  ) {
    return "올바른 이메일이 아닙니다."
  }

  const id =
    email.slice(0, firstAt)

  const domain =
    email.slice(firstAt + 1)

  if (
    id.length === 0 ||
    domain.length === 0
  ) {
    return "올바른 이메일이 아닙니다."
  }

  const maskedId =
    [...id]
      .map(
        (char, index) => {
          if (index < 2) {
            return char
          }

          if (char === ".") {
            return "."
          }

          return "*"
        }
      )
      .join("")

  return (
    maskedId +
    "@" +
    domain
  )
}
```

입력 문자열을 `trim()`한 새 문자열과 마스킹 결과를 만들 뿐 원본 문자열 자체는 변경하지 않습니다.

---

# Final Checklist

## 문자열 기본

- [ ] 문자열 index가 0부터 시작함을 이해했다.
- [ ] 공백도 length에 포함됨을 확인했다.
- [ ] indexOf가 첫 일치 위치를 반환함을 이해했다.
- [ ] 찾지 못하면 -1임을 확인했다.
- [ ] index 0과 미발견 -1을 구분했다.
- [ ] 문자열이 immutable임을 이해했다.

## 치환과 정규 표현식

- [ ] 문자열 인수 replace가 첫 일치만 바꿈을 확인했다.
- [ ] 정규 표현식 `g` 플래그로 전체 치환했다.
- [ ] `g`와 `i` 플래그 의미를 구분했다.
- [ ] replaceAll 대안을 이해했다.
- [ ] 치환 결과를 새 변수에 저장했다.

## 추출과 분리

- [ ] slice의 끝 index가 제외됨을 이해했다.
- [ ] slice의 음수 index를 이해했다.
- [ ] substring과 slice의 차이를 확인했다.
- [ ] substr 두 번째 인수가 문자 개수임을 이해했다.
- [ ] 새 코드에서 legacy substr 사용을 피했다.
- [ ] split 결과가 배열임을 확인했다.
- [ ] trim이 앞뒤 공백만 제거함을 이해했다.

## 문제 풀이

- [ ] 이메일에서 @ 위치를 먼저 검사했다.
- [ ] @가 없으면 slice를 실행하지 않았다.
- [ ] 함수 임시값은 지역 변수로 선언했다.
- [ ] 성별 코드 1·3과 2·4를 구분했다.
- [ ] 알 수 없는 성별 코드를 별도로 처리했다.
- [ ] 날짜·시간 문자열 형식을 검사했다.
- [ ] 고정 별표 문제와 길이 기반 별표 문제를 구분했다.
- [ ] ID의 점을 보존할지 요구사항을 확인했다.
- [ ] 마스킹 결과를 한 문자열로 완성했다.
- [ ] 중복 문자에도 위치 기준 마스킹이 동작하도록 작성했다.

## 원본 코드 검수

- [ ] 두 실제 원본 경로를 기록했다.
- [ ] 내 코드에만 첫 str 출력이 있음을 기록했다.
- [ ] 내 trim 테스트 값이 공백이 아니라 abc임을 기록했다.
- [ ] 양쪽 substr 사용을 기록했다.
- [ ] 강사님 문제 1~4가 미구현임을 기록했다.
- [ ] 내 문제 1의 @ 미발견 오류를 기록했다.
- [ ] 내 문제 2의 성별 코드 판정 오류를 기록했다.
- [ ] 내 문제 3의 형식 의존성을 기록했다.
- [ ] 내 문제 4 고정 별표 요구와 구현 차이를 기록했다.
- [ ] 내 문제 4가 두 번 등장함을 기록했다.
- [ ] 두 번째 문제 4의 replace 누적 오류를 기록했다.
- [ ] 내 문제 5 주석과 실제 점 처리 차이를 기록했다.
- [ ] 강사님과 내 문제 5 실제 결과가 같은 방향임을 기록했다.
- [ ] 문제 5의 @ 미발견 처리 문제를 기록했다.

---

# Key Summary

- JavaScript 10번 원본 파일은 양쪽 모두 `10_string.html`이다.
- 문자열의 `length`에는 공백도 포함된다.
- `indexOf()`는 부분 문자열의 첫 시작 index를 반환하고 찾지 못하면 -1을 반환한다.
- 첫 위치에서 찾으면 0이므로 단순 truthy 검사보다 `!== -1`을 사용한다.
- `replace()`는 변경된 새 문자열을 반환하고 원본 문자열은 바뀌지 않는다.
- 문자열 검색값을 사용한 replace는 첫 일치 항목만 바꾼다.
- `/가/g`의 `g`는 모든 일치 항목을 대상으로 하는 global 플래그다.
- 내 정규 표현식 주석에는 `i` 예시와 실제 `g` 코드가 함께 있어 플래그 의미를 구분해야 한다.
- `slice(start, end)`는 시작을 포함하고 끝을 제외한다.
- `substring()`은 기본 양수 범위에서 slice와 같아 보이지만 음수와 인수 순서 처리에서 다르다.
- `substr(start, length)`의 두 번째 인수는 문자 개수이며 이 메서드는 legacy API다.
- `split()`은 문자열을 구분자 기준 배열로 반환한다.
- `trim()`은 앞뒤 공백만 제거하며 문자열 내부 공백은 유지한다.
- 강사님은 공백만 있는 문자열로 length와 trim length를 비교한다.
- 내 코드는 같은 설명 아래 `"abc"`를 사용해 공백 전용 검증을 실제로 보여주지 못한다.
- 강사님은 문제 1~4를 요구사항만 제시하고 문제 5만 구현한다.
- 내 문제 1은 이메일 ID를 추출하지만 @가 없으면 `slice(0, -1)` 문제가 생긴다.
- 내 문제 2는 코드 1만 남성으로 처리하고 3과 잘못된 값까지 여성으로 판정한다.
- 내 문제 3은 `YYYY-MM-DD HH:mm:ss` 형식에 강하게 의존한다.
- 내 문제 4 요구는 별표 4개 고정이지만 첫 구현은 실제 ID 길이만큼 별표를 만든다.
- 내 코드에는 문제 4가 중복 번호로 두 번 등장한다.
- 두 번째 문제 4는 매번 원본에 replace를 적용해 전체 마스킹을 누적하지 못한다.
- `replace(email[j], "*")`는 현재 index가 아니라 같은 문자의 첫 일치 위치를 바꿀 수 있다.
- 내 문제 5 주석은 점을 보존한 `st***.******`을 제시하지만 실제 코드는 점도 별표로 바꾼다.
- 강사님 문제 5 예시와 양쪽 실제 구현은 `st**********@gmail.com` 방향이다.
- 이메일 마스킹에서는 @ 존재 여부, ID·도메인 빈 값, 짧은 ID, 점 보존 정책을 명확히 검증해야 한다.
