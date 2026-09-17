---
title: JavaScript 문자열과 문자열 메서드
version: v4.0-detailed-source
last_updated: 2026-09-17
status: Completed
---

# JavaScript 문자열과 문자열 메서드

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `10_JavaScript_문자열과_문자열메서드.md` |
| 분류 | `03_JavaScript` |
| 원본 기준 | `workspace_html/javascript/10_string.html`, `workspace_teacher/workspace_html/javascript/10_string.html` |
| 핵심 범위 | 문자열 길이, 검색, 치환, 정규표현식, 자르기, 분리, 공백 제거, 문자열 불변성 |
| 실습 범위 | 이메일 ID 추출, 주민번호 성별 코드, 날짜 문자열 분석, 이메일 마스킹 |
| 문서 형식 | JavaScript Developer-Wiki V3 개인 강의 백과사전 형식 |

> 이 문서는 내 코드와 강사님 코드 전체를 그대로 나열하지 않는다.  
> 문자열을 검색·치환·분리·가공하는 데 필요한 핵심 코드만 발췌하고, 잘못된 입력과 개인정보 마스킹까지 함께 설명한다.

---

## 이 문서에서 바로 찾기

- [개념에서 실제 실행까지: 문자열 메서드는 새 문자열을 반환한다](#js-10-section-4)
- [56. 문자열 비교 시 엄격 비교](#js-10-section-60)
- [58. 내 코드와 강사님 코드 비교](#js-10-section-62)
- [60. 실무형 예제: 회원 정보 표시용 마스킹](#js-10-section-64)
- [61. 대표 오류로 이해하기](#js-10-section-65)
- [62. 자주 하는 실수](#js-10-section-66)
- [63. 핵심 요약](#js-10-section-67)
- [64. 최종 체크리스트](#js-10-section-68)

<details>
<summary>세부 목차 펼치기 — 번호형 본문 전체</summary>

- [개요](#js-10-section-1)
- [핵심 개념](#js-10-section-2)
- [학습 목표](#js-10-section-3)
- [개념에서 실제 실행까지: 문자열 메서드는 새 문자열을 반환한다](#js-10-section-4)
- [1. 문자열 생성](#js-10-section-5)
- [2. 문자열 길이](#js-10-section-6)
- [3. 공백도 길이에 포함](#js-10-section-7)
- [4. 빈 문자열](#js-10-section-8)
- [5. 문자열 인덱스](#js-10-section-9)
- [6. 마지막 문자](#js-10-section-10)
- [7. 문자열 불변성](#js-10-section-11)
- [8. `indexOf()`](#js-10-section-12)
- [9. 첫 번째 일치 위치](#js-10-section-13)
- [10. 찾지 못한 경우](#js-10-section-14)
- [11. `indexOf()` 조건 검사](#js-10-section-15)
- [12. `includes()`](#js-10-section-16)
- [13. `startsWith()`와 `endsWith()`](#js-10-section-17)
- [14. `replace()`](#js-10-section-18)
- [15. 첫 번째 일치만 치환](#js-10-section-19)
- [16. 모든 문자열 치환](#js-10-section-20)
- [17. 정규표현식 전역 치환](#js-10-section-21)
- [18. 정규표현식 기본 구조](#js-10-section-22)
- [19. 대소문자 무시 치환](#js-10-section-23)
- [20. `replace()`의 원본 유지](#js-10-section-24)
- [21. `slice()`](#js-10-section-25)
- [22. `slice()` 종료 생략](#js-10-section-26)
- [23. 음수 인덱스](#js-10-section-27)
- [24. `substring()`](#js-10-section-28)
- [25. `slice()`와 `substring()` 차이](#js-10-section-29)
- [26. `substr()`](#js-10-section-30)
- [27. `substr()` 대체](#js-10-section-31)
- [28. `split()`](#js-10-section-32)
- [29. 구분자가 없는 경우](#js-10-section-33)
- [30. 빈 문자열로 분리](#js-10-section-34)
- [31. 분리 개수 제한](#js-10-section-35)
- [32. `trim()`](#js-10-section-36)
- [33. `trimStart()`와 `trimEnd()`](#js-10-section-37)
- [34. 공백 입력 검증](#js-10-section-38)
- [35. `trim()` 원본 유지](#js-10-section-39)
- [36. 문제 1: 이메일 ID 추출](#js-10-section-40)
- [37. `@`가 없을 때의 문제](#js-10-section-41)
- [38. 안전한 이메일 ID 추출](#js-10-section-42)
- [39. `split()`을 이용한 이메일 분리](#js-10-section-43)
- [40. 문제 2: 주민번호 성별 코드](#js-10-section-44)
- [41. 원본 성별 판정 문제](#js-10-section-45)
- [42. 성별 코드 규칙](#js-10-section-46)
- [43. 안전한 성별 판정](#js-10-section-47)
- [44. 개인정보 최소 처리](#js-10-section-48)
- [45. 문제 3: 날짜 문자열에서 월·분 추출](#js-10-section-49)
- [46. 단계별 분리](#js-10-section-50)
- [47. 날짜 문자열 검증](#js-10-section-51)
- [48. 문제 4: 고정 별표 이메일 마스킹](#js-10-section-52)
- [49. 문제 5: 길이에 맞는 이메일 마스킹](#js-10-section-53)
- [50. `repeat()`을 이용한 마스킹](#js-10-section-54)
- [51. 출력 결과](#js-10-section-55)
- [52. 짧은 ID 처리](#js-10-section-56)
- [53. 원본 문제 4 재시도의 오류](#js-10-section-57)
- [54. 누적 치환 방식](#js-10-section-58)
- [55. 부분 마스킹 규칙 설계](#js-10-section-59)
- [56. 문자열 비교 시 엄격 비교](#js-10-section-60)
- [57. 문자열 메서드 원본 변경 여부](#js-10-section-61)
- [58. 내 코드와 강사님 코드 비교](#js-10-section-62)
- [59. 기존 코드에서 개선 코드로 바꾼 이유](#js-10-section-63)
- [60. 실무형 예제: 회원 정보 표시용 마스킹](#js-10-section-64)
- [61. 대표 오류로 이해하기](#js-10-section-65)
- [62. 자주 하는 실수](#js-10-section-66)
- [63. 핵심 요약](#js-10-section-67)
- [64. 최종 체크리스트](#js-10-section-68)
- [마무리](#js-10-section-69)
- [V3 실행 추적 카드 — 문자열 입력 → 검색/변환 → 새 문자열](#js-10-section-70)

</details>

---

<a id="js-10-section-1"></a>

## 개요

문자열은 문자들의 순서 있는 집합이다.

```javascript
const text = "JavaScript"
```

문자열도 인덱스를 사용해 각 문자에 접근할 수 있다.

```javascript
console.log(text[0])
console.log(text[4])
```

출력:

```text
J
S
```

문자열 메서드를 사용하면 다음 작업을 할 수 있다.

| 작업 | 대표 기능 |
| --- | --- |
| 길이 확인 | `length` |
| 위치 검색 | `indexOf()`, `includes()` |
| 문자 치환 | `replace()`, `replaceAll()` |
| 일부 복사 | `slice()`, `substring()` |
| 문자열 분리 | `split()` |
| 공백 제거 | `trim()` |
| 반복 문자열 | `repeat()` |
| 시작·끝 확인 | `startsWith()`, `endsWith()` |

> [!IMPORTANT]
> JavaScript 문자열은 불변이다.
>
> 문자열 메서드는 원본을 직접 바꾸지 않고 새로운 문자열을 반환한다.

---

<a id="js-10-section-2"></a>

## 핵심 개념

| 개념 | 핵심 역할 |
| --- | --- |
| 문자열 | 문자의 순서 있는 값 |
| 인덱스 | 각 문자의 위치 |
| `length` | 문자열 길이 |
| 불변성 | 생성된 문자열 내용은 직접 변경할 수 없음 |
| `indexOf()` | 문자열 위치 검색 |
| `replace()` | 첫 번째 일치 문자열 치환 |
| `replaceAll()` | 모든 일치 문자열 치환 |
| 정규표현식 | 문자열 패턴 검색·치환 |
| `slice()` | 시작부터 종료 직전까지 복사 |
| `substring()` | 두 인덱스 사이 문자열 복사 |
| `split()` | 구분자를 기준으로 배열 생성 |
| `trim()` | 앞뒤 공백 제거 |
| 마스킹 | 개인정보 일부를 숨겨서 표시 |

---

<a id="js-10-section-3"></a>

## 학습 목표

- 검색 실패와 정규표현식 범위를 확인한다.
- 원본의 해당 부분을 찾아 실행 순서와 결과를 다시 확인한다.

---

<a id="js-10-section-4"></a>

## 개념에서 실제 실행까지: 문자열 메서드는 새 문자열을 반환한다

문자열은 변경 불가능한 원시값이다. replace나 slice를 호출해도 기존 str은 그대로이고 반환값을 새 변수에 저장해야 한다. indexOf는 찾은 위치0도 반환하므로 if(indexOf(...))처럼 사용하면 처음에 있던 문자를 놓치고 -1을 참으로 취급한다.

두 원본은 replace("가","나")와 replace(/가/g,"나")를 비교한다. 문자열 검색은 첫 일치, g 정규표현식은 전체 일치를 바꾼다. slice(시작,끝)은 끝 직전까지, 수업의 substr(시작,개수)는 두 번째 인수 의미가 다르다. 💡 substr은 레거시라 새 예제는 slice를 우선 사용한다.

내 이메일 secCheck는 매회 원래 email.replace를 다시 실행해 바뀐 결과가 누적되지 않는다. 강사님은 앞두글자+별표누적+도메인을 합친다. 두 번째 문제는 별표 개수 규칙이 다르므로 '항상4개'와 '가려진 글자 수'를 별도로 설명해야 한다. [a-Z]는 대소문자 전체를 의미하지 않고 범위 순서가 역전되어 오류가 난다. [a-zA-Z]가 영문자 범위다.

### 수업 원본에서 사용한 부분

아래는 전체 실행 파일이 아니라 **개념에 대응하는 문맥 발췌**다. 나머지 HTML·선언·등록 코드는 원본과 기존 번호형 본문에서 이어 확인한다. 

내 코드: `workspace_html/javascript/10_string.html`

```javascript
// 첫번째 전달인자를 두번째 전달인자로 바꾼다 (string쪽은 거의 원본값을 바꾸지 않음)
            let s1 = str.replace('죽었','살았')
            console.log(str)
            console.log(s1)

            // '가'가 2개 있어도 처음 만나는것만 바꿈 
            // (반복하려면 while indexof로 -1 받을 때 까지)
            let s2 = str.replace('가','나')
```

강사님 코드: `workspace_teacher/workspace_html/javascript/10_string.html`

```javascript
// 단, 처음 만나는 것만 바꾼다
    let s1 = str.replace('죽었', '살았')
    console.log(str)
    console.log(s1)

    let s2 = str.replace('가', '나')
    console.log(s2)
```

### 직접 재현하는 최소 예제와 결과

이 예제는 **이번 리팩토링의 설명용 재구성**이다. 원본 그대로의 발췌와 구별한다. 외부 통신 없이 Console에서 실행한다. 다른 예제의 변수와 섞이지 않게 새 실행 문맥에서 실행한다.

```javascript
const email = "study.todair@gmail.com";
const pos = email.indexOf("@");
const masked = email.slice(0, 2) + "*".repeat(pos - 2) + email.slice(pos);
console.log(masked);
const original = "가가";
console.log(original.replace("가", "나"), original.replace(/가/g, "나"), original);
console.log(/^[a-zA-Z]+$/.test("Abc"), /^[a-zA-Z]+$/.test("Abc1"));
```

예상 출력:

```text
st**********@gmail.com
나가 나나 가가
true false
```

### 결과를 역추적하는 방법

[A-z]는 대문자A~소문자z 사이의 [, \, ], ^, _, 백틱도 포함한다. 전체 영문만 검증하려면 ^와 $ 및 반복 +를 포함한 /^[a-zA-Z]+$/를 사용한다. 이 규칙은 ASCII 영문만 허용한다.

출력은 아래의 확인 경로로 추적한다. return 값은 호출자에게 전달되고 자동으로 화면에 표시되지 않는다. Console 로그, DOM 변경, 저장소 변경, 서버 응답은 별개 단계다.

| 확인할 단계 | 이 예제에서 볼 것 |
| --- | --- |
| 입력 | 리터럴·현재 폼 값·이벤트 인수·응답 중 출처를 위 설명과 대조 |
| 실행 | 각 줄 또는 콜백이 지금 실행되는지, 나중에 실행되는지 구분 |
| 결과 | 위 예상 출력과 현재 값·자료형을 함께 대조 |
| 오류 | 첫 오류 줄의 입력과 직전 상태를 확인하고 뒤 로그 누락 원인 추적 |

### 단계별 복습 실습과 정답

**기본 실습:** abcd@example.com을 고정 별표4개와 길이 기반 별표로 각각 가린다.

**응용·디버깅 실습:** [A-z]를 영문자 전용 검증으로 사용하면 생기는 문제를 고친다.

**통합 확인:** 위 최소 예제를 새 문맥에서 작성하고 정상값·빈 값·경계값으로 실행한다. 원본에서 대응하는 선언·호출·콜백을 찾아 위에 나타난 차이가 무엇을 바꾸는지 설명한다. 아래 정답은 먼저 예측한 뒤 펼친다. 이 실습은 💡 설명용 보강이며 원본에 모두 완성되어 있다는 뜻은 아니다.

<details>
<summary>정답과 처리 순서 해설</summary>

1. ab****@example.com과 ab**@example.com이다. 요구사항이 다르면 결과도 다르다.
2. ASCII 중간기호가 포함될 수 있다. /^[a-zA-Z]+$/로 전체 영문 문자열을 검사한다.
3. 최소 예제의 예상 출력과 한 줄씩 대조한다. 값이 다른 경우 입력 → 형 변환 → 분기/상태 변경 → 출력 순서로 첫 차이를 찾는다. DOM·API 예제는 Console 값만 아니라 화면·Elements·Network가 서로 같은 상태를 말하는지도 점검한다.

</details>

### 복습 질문과 해설

**질문:** email에 @가 없는데 slice(0,-1)을 하면?

**해설:** 마지막 글자를 제외한 문자열을 만든다. 실패가 자동 표시되지 않으므로 indexOf의 -1을 먼저 처리해야 한다.

**한 번 더 확인:** 예제의 입력을 하나 바꾸고 결과를 먼저 예상한 뒤 실행한다. 정상 입력만 아니라 비어 있는 값, 경계값, 두 번 실행했을 때의 상태를 기존 실습·오류 절에서 반복 확인한다.

---

<a id="js-10-section-5"></a>

## 1. 문자열 생성

```javascript
const text = "기사도가 죽었을 리가"
```

큰따옴표, 작은따옴표, 백틱으로 문자열을 만들 수 있다.

```javascript
const first = "문자열"
const second = '문자열'
const third = `문자열`
```

---

<a id="js-10-section-6"></a>

## 2. 문자열 길이

### 2-1. 원본 코드

```javascript
const text = "기사도가 죽었을 리가"

console.log(
    text.length,
)
```

`length`는 문자열에 포함된 UTF-16 코드 단위 개수를 반환한다.

---

<a id="js-10-section-7"></a>

## 3. 공백도 길이에 포함

```javascript
const text = "a b"

console.log(text.length)
```

출력:

```text
3
```

가운데 공백도 하나의 위치를 차지한다.

---

<a id="js-10-section-8"></a>

## 4. 빈 문자열

```javascript
const text = ""

console.log(text.length)
```

출력:

```text
0
```

---

<a id="js-10-section-9"></a>

## 5. 문자열 인덱스

```javascript
const text = "JavaScript"

console.log(text[0])
console.log(text[1])
```

출력:

```text
J
a
```

인덱스는 0부터 시작한다.

---

<a id="js-10-section-10"></a>

## 6. 마지막 문자

```javascript
const text = "JavaScript"

const lastCharacter = (
    text[text.length - 1]
)

console.log(lastCharacter)
```

출력:

```text
t
```

현대 JavaScript에서는 다음도 가능하다.

```javascript
console.log(
    text.at(-1),
)
```

---

<a id="js-10-section-11"></a>

## 7. 문자열 불변성

```javascript
let text = "abc"

text[0] = "A"

console.log(text)
```

출력:

```text
abc
```

문자열의 특정 위치를 직접 변경할 수 없다.

새 문자열을 만들어 다시 저장해야 한다.

```javascript
text = (
    "A" + text.slice(1)
)
```

---

<a id="js-10-section-12"></a>

## 8. `indexOf()`

### 8-1. 원본 코드

```javascript
const text = "기사도가 죽었을 리가"

console.log(
    text.indexOf("죽었"),
)
```

찾은 문자열이 시작하는 인덱스를 반환한다.

---

<a id="js-10-section-13"></a>

## 9. 첫 번째 일치 위치

```javascript
console.log(
    text.indexOf("가"),
)
```

같은 문자열이 여러 번 있어도 첫 번째 위치를 반환한다.

---

<a id="js-10-section-14"></a>

## 10. 찾지 못한 경우

```javascript
console.log(
    text.indexOf("나"),
)
```

출력:

```text
-1
```

> [!IMPORTANT]
> `indexOf()`는 찾지 못했을 때 `undefined`가 아니라 `-1`을 반환한다.

---

<a id="js-10-section-15"></a>

## 11. `indexOf()` 조건 검사

```javascript
const atIndex = (
    email.indexOf("@")
)

if (atIndex !== -1) {
    console.log(
        "이메일 형식에 @가 있습니다.",
    )
}
```

엄격 비교를 사용한다.

---

<a id="js-10-section-16"></a>

## 12. `includes()`

위치가 필요하지 않고 포함 여부만 필요하다면 다음이 더 직접적이다.

```javascript
const hasAtSign = (
    email.includes("@")
)

console.log(hasAtSign)
```

출력:

```text
true
```

---

<a id="js-10-section-17"></a>

## 13. `startsWith()`와 `endsWith()`

```javascript
const fileName = "report.pdf"

console.log(
    fileName.startsWith("report"),
)

console.log(
    fileName.endsWith(".pdf"),
)
```

파일 확장자나 접두어 검사에 사용할 수 있다.

---

<a id="js-10-section-18"></a>

## 14. `replace()`

### 14-1. 원본 코드

```javascript
const text = "기사도가 죽었을 리가"

const changed = text.replace(
    "죽었",
    "살았",
)

console.log(text)
console.log(changed)
```

원본은 유지되고 새 문자열이 반환된다.

---

<a id="js-10-section-19"></a>

## 15. 첫 번째 일치만 치환

```javascript
const changed = text.replace(
    "가",
    "나",
)
```

`"가"`가 여러 번 있어도 첫 번째 일치만 바뀐다.

---

<a id="js-10-section-20"></a>

## 16. 모든 문자열 치환

현대 JavaScript에서는 `replaceAll()`을 사용할 수 있다.

```javascript
const changed = text.replaceAll(
    "가",
    "나",
)
```

---

<a id="js-10-section-21"></a>

## 17. 정규표현식 전역 치환

원본:

```javascript
const changed = text.replace(
    /가/g,
    "나",
)
```

`g` 플래그는 global의 약자로 모든 일치를 대상으로 한다.

---

<a id="js-10-section-22"></a>

## 18. 정규표현식 기본 구조

```text
/패턴/플래그
```

대표 플래그:

| 플래그 | 의미 |
| --- | --- |
| `g` | 모든 일치 |
| `i` | 대소문자 무시 |
| `m` | 여러 줄 모드 |

---

<a id="js-10-section-23"></a>

## 19. 대소문자 무시 치환

```javascript
const text = "JavaScript javascript"

const changed = text.replace(
    /javascript/gi,
    "JS",
)

console.log(changed)
```

출력:

```text
JS JS
```

---

<a id="js-10-section-24"></a>

## 20. `replace()`의 원본 유지

```javascript
let text = "abc abc"

text.replace(
    "abc",
    "ABC",
)

console.log(text)
```

출력:

```text
abc abc
```

반환값을 다시 저장해야 한다.

```javascript
text = text.replace(
    "abc",
    "ABC",
)
```

---

<a id="js-10-section-25"></a>

## 21. `slice()`

### 21-1. 원본 코드

```javascript
const text = "기사도가 죽었을 리가"

console.log(
    text.slice(3, 6),
)
```

시작 인덱스는 포함하고 종료 인덱스는 포함하지 않는다.

---

<a id="js-10-section-26"></a>

## 22. `slice()` 종료 생략

```javascript
console.log(
    text.slice(3),
)
```

인덱스 3부터 끝까지 복사한다.

---

<a id="js-10-section-27"></a>

## 23. 음수 인덱스

```javascript
const text = "JavaScript"

console.log(
    text.slice(-6),
)
```

출력:

```text
Script
```

음수는 문자열 끝에서부터 위치를 계산한다.

---

<a id="js-10-section-28"></a>

## 24. `substring()`

### 24-1. 원본 코드

```javascript
const result = text.substring(
    3,
    6,
)
```

`slice()`와 비슷하게 시작부터 종료 직전까지 반환한다.

---

<a id="js-10-section-29"></a>

## 25. `slice()`와 `substring()` 차이

| 항목 | `slice()` | `substring()` |
| --- | --- | --- |
| 음수 인덱스 | 끝에서 계산 | 0으로 처리 |
| 시작 > 종료 | 빈 문자열 | 두 값을 교환 |
| 일반 권장 | 자주 사용 | 기존 코드에서 사용 |

예:

```javascript
const text = "abcdef"

console.log(
    text.slice(4, 2),
)

console.log(
    text.substring(4, 2),
)
```

출력:

```text

cd
```

---

<a id="js-10-section-30"></a>

## 26. `substr()`

원본:

```javascript
const result = text.substr(
    3,
    7,
)
```

첫 번째 인수는 시작 인덱스, 두 번째 인수는 가져올 길이다.

하지만 `substr()`은 오래된 레거시 메서드이며 신규 코드에서는 사용하지 않는 편이 좋다.

---

<a id="js-10-section-31"></a>

## 27. `substr()` 대체

```javascript
const start = 3
const length = 7

const result = text.slice(
    start,
    start + length,
)
```

---

<a id="js-10-section-32"></a>

## 28. `split()`

### 28-1. 원본 코드

```javascript
const words = text.split(" ")

console.log(words)
```

공백을 기준으로 문자열을 배열로 나눈다.

---

<a id="js-10-section-33"></a>

## 29. 구분자가 없는 경우

```javascript
console.log(
    "abc".split(","),
)
```

출력:

```text
['abc']
```

구분자를 찾지 못하면 원본 문자열 하나가 들어 있는 배열을 반환한다.

---

<a id="js-10-section-34"></a>

## 30. 빈 문자열로 분리

```javascript
console.log(
    "abc".split(""),
)
```

출력:

```text
['a', 'b', 'c']
```

문자 단위 배열을 만들 수 있다.

---

<a id="js-10-section-35"></a>

## 31. 분리 개수 제한

```javascript
const values = (
    "a,b,c,d".split(
        ",",
        2,
    )
)

console.log(values)
```

출력:

```text
['a', 'b']
```

---

<a id="js-10-section-36"></a>

## 32. `trim()`

### 32-1. 원본 코드

```javascript
const text = "    1 2  3   "

const trimmed = text.trim()

console.log(trimmed)
```

앞뒤 공백을 제거하고 새 문자열을 반환한다.

가운데 공백은 유지된다.

---

<a id="js-10-section-37"></a>

## 33. `trimStart()`와 `trimEnd()`

```javascript
text.trimStart()
text.trimEnd()
```

한쪽 공백만 제거할 때 사용한다.

---

<a id="js-10-section-38"></a>

## 34. 공백 입력 검증

원본:

```javascript
if (
    text.trim().length !== 0
) {
    // 값 있음
}
```

더 직접적으로 작성할 수 있다.

```javascript
if (
    text.trim() !== ""
) {
    // 값 있음
}
```

---

<a id="js-10-section-39"></a>

## 35. `trim()` 원본 유지

```javascript
let text = "  abc  "

text.trim()

console.log(text)
```

출력:

```text
  abc
```

저장해야 한다.

```javascript
text = text.trim()
```

---

<a id="js-10-section-40"></a>

## 36. 문제 1: 이메일 ID 추출

### 36-1. 내 코드

```javascript
function getEmailId(
    email,
) {
    const atIndex = (
        email.indexOf("@")
    )

    return email.slice(
        0,
        atIndex,
    )
}
```

정상 이메일에서는 ID를 반환한다.

---

<a id="js-10-section-41"></a>

## 37. `@`가 없을 때의 문제

```javascript
"abcdef".slice(
    0,
    -1,
)
```

출력:

```text
abcde
```

`indexOf("@")`가 `-1`인데 그대로 `slice()`에 사용하면 마지막 문자가 잘린 잘못된 결과가 나온다.

---

<a id="js-10-section-42"></a>

## 38. 안전한 이메일 ID 추출

```javascript
function getEmailId(
    email,
) {
    const atIndex = (
        email.indexOf("@")
    )

    if (
        atIndex <= 0
        || atIndex
        === email.length - 1
    ) {
        return null
    }

    return email.slice(
        0,
        atIndex,
    )
}
```

---

<a id="js-10-section-43"></a>

## 39. `split()`을 이용한 이메일 분리

```javascript
function splitEmail(
    email,
) {
    const parts = email.split("@")

    if (
        parts.length !== 2
        || parts[0] === ""
        || parts[1] === ""
    ) {
        return null
    }

    return {
        id: parts[0],
        domain: parts[1],
    }
}
```

---

<a id="js-10-section-44"></a>

## 40. 문제 2: 주민번호 성별 코드

원본은 하이픈 뒤 첫 문자를 추출한다.

```javascript
const code = residentNumber.slice(
    residentNumber.indexOf("-") + 1,
    residentNumber.indexOf("-") + 2,
)
```

---

<a id="js-10-section-45"></a>

## 41. 원본 성별 판정 문제

원본:

```javascript
if (code == 1) {
    console.log("남자")
} else {
    console.log("여자")
}
```

다음 문제가 있다.

- 문자열과 숫자를 느슨하게 비교
- 코드 `3`도 남성인데 여성으로 처리
- 코드 `4` 외의 잘못된 값도 여성으로 처리
- 형식 검증이 없음

---

<a id="js-10-section-46"></a>

## 42. 성별 코드 규칙

일반적인 성별 코드 기준:

| 코드 | 의미 |
| --- | --- |
| `1`, `3` | 남성 |
| `2`, `4` | 여성 |
| 기타 | 확인 필요 |

개인정보 처리 정책이나 외국인 코드 등 실제 요구사항에 따라 규칙이 달라질 수 있다.

---

<a id="js-10-section-47"></a>

## 43. 안전한 성별 판정

```javascript
function getGenderText(
    residentNumber,
) {
    const match = (
        residentNumber.match(
            /^\d{6}-([1-4])\d{6}$/,
        )
    )

    if (!match) {
        return "형식을 확인해주세요."
    }

    const code = match[1]

    if (
        code === "1"
        || code === "3"
    ) {
        return "남성"
    }

    return "여성"
}
```

---

<a id="js-10-section-48"></a>

## 44. 개인정보 최소 처리

주민등록번호는 민감한 개인정보다.

실제 서비스에서는 다음 원칙이 필요하다.

- 꼭 필요한 경우만 수집
- 전체 번호를 Console에 출력하지 않기
- 저장 시 암호화·접근 제어
- 표시 시 마스킹
- 보관 기간 최소화

---

<a id="js-10-section-49"></a>

## 45. 문제 3: 날짜 문자열에서 월·분 추출

입력:

```text
2026-07-14 12:43:19
```

원본은 공백·하이픈·콜론 순서로 분리한다.

---

<a id="js-10-section-50"></a>

## 46. 단계별 분리

```javascript
const value = (
    "2026-07-14 12:43:19"
)

const [
    datePart,
    timePart,
] = value.split(" ")

const [
    year,
    month,
    day,
] = datePart.split("-")

const [
    hour,
    minute,
    second,
] = timePart.split(":")

console.log(
    `${month}월, ${minute}분`,
)
```

출력:

```text
07월, 43분
```

---

<a id="js-10-section-51"></a>

## 47. 날짜 문자열 검증

```javascript
function parseDateTime(
    value,
) {
    const match = value.match(
        /^(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})$/,
    )

    if (!match) {
        return null
    }

    return {
        year: match[1],
        month: match[2],
        day: match[3],
        hour: match[4],
        minute: match[5],
        second: match[6],
    }
}
```

형식이 달라졌을 때 잘못된 인덱스 접근을 막을 수 있다.

---

<a id="js-10-section-52"></a>

## 48. 문제 4: 고정 별표 이메일 마스킹

요구사항:

```text
todair@naver.com
→ to****@naver.com
```

가려진 실제 글자 수와 관계없이 별표 4개를 사용한다.

```javascript
function maskEmailFixed(
    email,
) {
    const parsed = splitEmail(
        email,
    )

    if (!parsed) {
        return null
    }

    const visible = (
        parsed.id.slice(0, 2)
    )

    return (
        `${visible}****@${parsed.domain}`
    )
}
```

---

<a id="js-10-section-53"></a>

## 49. 문제 5: 길이에 맞는 이메일 마스킹

요구사항:

```text
study.todair@gmail.com
→ st**********@gmail.com
```

ID의 앞 두 글자만 남기고 나머지 길이만큼 별표를 만든다.

---

<a id="js-10-section-54"></a>

## 50. `repeat()`을 이용한 마스킹

```javascript
function maskEmail(
    email,
) {
    const parsed = splitEmail(
        email,
    )

    if (!parsed) {
        return null
    }

    const visibleLength = Math.min(
        2,
        parsed.id.length,
    )

    const visible = (
        parsed.id.slice(
            0,
            visibleLength,
        )
    )

    const hidden = "*".repeat(
        parsed.id.length
        - visibleLength,
    )

    return (
        `${visible}${hidden}@${parsed.domain}`
    )
}
```

---

<a id="js-10-section-55"></a>

## 51. 출력 결과

```javascript
console.log(
    maskEmail(
        "todair@naver.com",
    ),
)

console.log(
    maskEmail(
        "study.todair@gmail.com",
    ),
)
```

출력:

```text
to****@naver.com
st**********@gmail.com
```

---

<a id="js-10-section-56"></a>

## 52. 짧은 ID 처리

```javascript
console.log(
    maskEmail(
        "a@test.com",
    ),
)
```

출력:

```text
a@test.com
```

ID 길이가 두 글자 이하인 경우 가릴 문자가 없다.

업무 요구사항에 따라 최소 한 글자를 가리도록 별도 규칙을 정할 수도 있다.

---

<a id="js-10-section-57"></a>

## 53. 원본 문제 4 재시도의 오류

내 코드의 두 번째 문제 4 풀이:

```javascript
for (
    let index = 2;
    index < atIndex;
    index += 1
) {
    masked = email.replace(
        email[index],
        "*",
    )
}
```

문제점:

- 매 반복마다 원본 `email`에서 다시 치환
- 이전 결과가 누적되지 않음
- 같은 문자가 앞에 있으면 다른 위치가 바뀔 수 있음
- 마지막 반복 결과만 남음
- 중간 결과를 매번 Console에 출력

---

<a id="js-10-section-58"></a>

## 54. 누적 치환 방식

반드시 치환 방식으로 구현한다면 새 결과를 계속 갱신해야 한다.

```javascript
let masked = email

for (
    let index = 2;
    index < atIndex;
    index += 1
) {
    masked = (
        masked.slice(0, index)
        + "*"
        + masked.slice(index + 1)
    )
}
```

하지만 `slice()`와 `repeat()` 조합이 더 간결하다.

---

<a id="js-10-section-59"></a>

## 55. 부분 마스킹 규칙 설계

마스킹 코드는 먼저 규칙을 정해야 한다.

| 항목 | 결정할 내용 |
| --- | --- |
| 표시 문자 수 | 앞 1글자·2글자 등 |
| 별표 개수 | 고정 또는 실제 길이 |
| 짧은 ID | 전부 표시 또는 일부 마스킹 |
| 잘못된 이메일 | `null`, 오류 메시지 등 |
| 도메인 | 전체 표시 또는 일부 마스킹 |
| 국제 문자 | 사용자에게 보이는 문자 단위 고려 |

---

<a id="js-10-section-60"></a>

## 56. 문자열 비교 시 엄격 비교

원본:

```text
if (
    position != -1
) {
```

개선:

```text
if (
    position !== -1
) {
```

문자열 메서드가 반환하는 숫자와 정확히 비교한다.

---

<a id="js-10-section-61"></a>

## 57. 문자열 메서드 원본 변경 여부

| 기능 | 원본 변경 |
| --- | --- |
| `replace()` | 아니오 |
| `replaceAll()` | 아니오 |
| `slice()` | 아니오 |
| `substring()` | 아니오 |
| `split()` | 아니오 |
| `trim()` | 아니오 |
| `toUpperCase()` | 아니오 |
| `toLowerCase()` | 아니오 |

문자열은 불변이므로 항상 새 문자열을 반환한다.

---

<a id="js-10-section-62"></a>

## 58. 내 코드와 강사님 코드 비교

| 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 메서드 설명 | 상세 주석 추가 | 핵심 설명 중심 |
| 검색 | 같은 문자열·없는 문자열까지 확인 | 동일 |
| 전체 치환 | 정규표현식 설명 추가 | 기본 코드 |
| 문제 1~4 | 직접 풀이 | 요구사항만 제시 |
| 문제 5 | 직접 풀이 | 완성 코드 제공 |
| 마스킹 | 두 가지 방식 시도 | `slice()`와 반복문 사용 |
| 비교 | `!=`, `==` 사용 | `!=` 사용 |
| 형식 검증 | 거의 없음 | 없음 |

### 58-1. 내 코드의 장점

- 문자열 메서드의 반환값과 원본 유지 여부를 주석으로 기록했다.
- 문제 1~5를 직접 구현했다.
- 이메일 마스킹을 두 방식으로 시도했다.
- 날짜 문자열을 단계별로 분리했다.

### 58-2. 내 코드의 개선점

- 이메일에 `@`가 없을 때 `slice(0, -1)`이 실행될 수 있다.
- 주민번호 코드 `3`을 남성으로 처리하지 않는다.
- 잘못된 성별 코드도 모두 여성으로 처리한다.
- 느슨한 비교를 사용한다.
- `substr()`은 신규 코드에서 피하는 것이 좋다.
- 문제 4 재시도는 이전 치환 결과를 누적하지 않는다.
- 전역 변수를 여러 함수가 공유한다.
- 입력값 형식 검증이 부족하다.

### 58-3. 강사님 코드의 장점

- 문자열 검색·치환·자르기·분리를 순서대로 보여 준다.
- `replace()`가 첫 일치만 변경함을 설명한다.
- 정규표현식 `g` 플래그를 소개한다.
- 이메일 마스킹 문제의 기본 풀이를 제공한다.

### 58-4. 강사님 코드의 보충점

- `substr()`의 레거시 상태를 설명할 필요가 있다.
- `replaceAll()`과 `includes()`를 보충할 수 있다.
- 이메일 형식 검증이 필요하다.
- 주민번호·날짜 문제의 완성 풀이가 필요하다.
- 문자열 불변성을 더 명확히 설명할 수 있다.
- 개인정보 처리 주의가 필요하다.

---

<a id="js-10-section-63"></a>

## 59. 기존 코드에서 개선 코드로 바꾼 이유

### 59-1. `substr()` 제거

기존:

```javascript
text.substr(
    start,
    length,
)
```

개선:

```javascript
text.slice(
    start,
    start + length,
)
```

### 59-2. 이메일 분리

기존:

```javascript
const atIndex = (
    email.indexOf("@")
)

const id = email.slice(
    0,
    atIndex,
)
```

개선:

```javascript
const parsed = splitEmail(
    email,
)
```

### 59-3. 마스킹 반복문 제거

기존:

```text
for (...) {
    hidden += "*"
}
```

개선:

```javascript
const hidden = "*".repeat(
    hiddenLength,
)
```

### 59-4. 전역 변수 제거

기존:

```javascript
let emailCheck
let genderCheck
let genderResult
```

개선:

```javascript
function getEmailId(
    email,
) {
    const atIndex = (
        email.indexOf("@")
    )

    // ...
}
```

필요한 값을 함수 내부 지역 변수로 관리한다.

---

<a id="js-10-section-64"></a>

## 60. 실무형 예제: 회원 정보 표시용 마스킹

```javascript
function maskEmail(
    email,
) {
    const parsed = splitEmail(
        email,
    )

    if (!parsed) {
        throw new TypeError(
            "올바른 이메일 형식이 아닙니다.",
        )
    }

    const visibleLength = Math.min(
        2,
        parsed.id.length,
    )

    const visible = (
        parsed.id.slice(
            0,
            visibleLength,
        )
    )

    const hidden = "*".repeat(
        parsed.id.length
        - visibleLength,
    )

    return (
        `${visible}${hidden}@${parsed.domain}`
    )
}

function createMemberSummary(
    member,
) {
    return {
        name: member.name.trim(),
        email: maskEmail(
            member.email.trim(),
        ),
    }
}

const member = {
    name: "  Kim  ",
    email: "study.todair@gmail.com",
}

console.log(
    createMemberSummary(member),
)
```

### 60-1. 출력 결과

```text
{
    name: "Kim",
    email: "st**********@gmail.com"
}
```

### 60-2. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `trim()` | 사용자 입력 앞뒤 공백 제거 |
| `splitEmail()` | 이메일 ID·도메인 검증과 분리 |
| `slice()` | 표시할 앞부분 추출 |
| `repeat()` | 가릴 길이만큼 별표 생성 |
| `throw` | 잘못된 형식을 즉시 알림 |
| 새 객체 반환 | 원본 회원 데이터 변경 방지 |

---

<a id="js-10-section-65"></a>

## 61. 대표 오류로 이해하기

### 61-1. `indexOf()` 실패값 미처리

`-1`을 인덱스로 사용해 잘못된 문자열이 만들어진다.

### 61-2. 문자열 메서드 반환값 미저장

원본 문자열은 바뀌지 않는다.

### 61-3. `substr()` 의존

실행은 될 수 있지만 신규 코드에서 권장되지 않는다.

### 61-4. 주민번호 형식 검증 누락

하이픈이 없으면 잘못된 위치의 문자를 읽을 수 있다.

### 61-5. 반복 `replace()` 누적 실패

매번 원본에서 다시 치환하면 이전 결과가 사라진다.

### 61-6. `split()` 결과 길이 미검사

예상한 배열 요소가 없어 `undefined`가 될 수 있다.

---

<a id="js-10-section-66"></a>

## 62. 자주 하는 실수

### 62-1. 문자열 인덱스를 직접 변경

문자열은 불변이다.

<a id="index-section-99"></a>

### 62-2. `length`에서 공백 제외

공백도 길이에 포함된다.

<a id="index-section-100"></a>

### 62-3. `indexOf()` 실패값을 `undefined`로 생각

`-1`이다.

### 62-4. `replace()`가 모든 문자열을 바꾼다고 생각

기본적으로 첫 일치만 변경한다.

### 62-5. `trim()`이 가운데 공백도 제거한다고 생각

앞뒤 공백만 제거한다.

### 62-6. `slice()` 종료 인덱스 포함

종료 직전까지만 복사한다.

### 62-7. `substring()`에서 음수 인덱스 사용

0으로 처리된다.

### 62-8. 이메일 `@` 존재 여부를 검사하지 않음

잘못된 결과가 만들어질 수 있다.

### 62-9. 주민번호 코드 1만 남성으로 처리

3도 남성 코드일 수 있다.

### 62-10. 개인정보 원문을 Console에 출력

실제 서비스에서는 노출을 최소화해야 한다.

---

<a id="js-10-section-67"></a>

## 63. 핵심 요약

```text
text.length
→ 문자열 길이

text[index]
→ 문자 접근

text.at(-1)
→ 마지막 문자
```

```text
indexOf()
→ 위치 또는 -1

includes()
→ 포함 여부 Boolean

replace()
→ 첫 일치 치환

replaceAll()
→ 모든 일치 치환
```

```text
slice()
substring()
→ 일부 문자열 복사

split()
→ 문자열을 배열로

trim()
→ 앞뒤 공백 제거
```

```text
문자열은 불변
→ 메서드 결과를 새 변수에 저장

repeat()
→ 같은 문자열 반복

마스킹
→ 노출할 부분 + 별표 + 나머지
```

---

<a id="js-10-section-68"></a>

## 64. 최종 체크리스트

- [ ] 문자열 길이를 확인할 수 있는가?
- [ ] 문자열 인덱스가 0부터 시작함을 이해했는가?
- [ ] 문자열이 불변임을 설명할 수 있는가?
- [ ] 마지막 문자를 찾을 수 있는가?
- [ ] `indexOf()`의 `-1`을 처리할 수 있는가?
- [ ] `includes()`로 포함 여부를 확인할 수 있는가?
- [ ] `replace()`와 `replaceAll()`을 구분할 수 있는가?
- [ ] 정규표현식의 `g` 플래그를 이해했는가?
- [ ] `slice()`와 `substring()`의 차이를 설명할 수 있는가?
- [ ] `substr()` 대신 `slice()`를 사용할 수 있는가?
- [ ] `split()`으로 문자열을 배열로 만들 수 있는가?
- [ ] `trim()`으로 공백 입력을 검증할 수 있는가?
- [ ] 이메일에 `@`가 없는 경우를 처리할 수 있는가?
- [ ] 이메일 ID와 도메인을 안전하게 분리할 수 있는가?
- [ ] 주민번호 성별 코드를 엄격하게 비교할 수 있는가?
- [ ] 날짜 문자열의 형식을 검증할 수 있는가?
- [ ] `repeat()`으로 마스킹 문자열을 만들 수 있는가?
- [ ] 문자열 메서드 반환값을 다시 저장할 수 있는가?
- [ ] 전역 변수 대신 지역 변수를 사용할 수 있는가?
- [ ] 개인정보를 마스킹해 표시할 수 있는가?

---

<a id="js-10-section-69"></a>

## 마무리

문자열 처리의 핵심은 문자를 자르고 붙이는 것에서 끝나지 않는다.

```text
입력 형식을 먼저 검증하고
    ↓
검색 실패값을 정확히 처리하고
    ↓
문자열 불변성을 이해하고
    ↓
목적에 맞는 메서드를 선택하고
    ↓
개인정보는 필요한 부분만 안전하게 표시하는 것
```

이 흐름을 이해하면 이후 객체와 DOM 문서에서 사용자 입력과 화면 문자열을 더 안전하게 처리할 수 있다.
<a id="js-10-section-70"></a>

## V3 실행 추적 카드 — 문자열 입력 → 검색/변환 → 새 문자열

문자열은 불변이므로 메서드 결과는 새 문자열이다. `trim`, `replace`, `toUpperCase` 결과를 계속 쓰려면 저장해야 한다.

`const s=" hi "; console.log(s.trim().toUpperCase(), s.length);`는 `HI 4`다. 없는 위치의 문자 접근과 `indexOf`의 `-1`을 구분한다.

**원본 연결:** 내 코드와 강사님 코드의 `workspace_html/javascript/10_string.html`에서 실제 사용 위치와 차이를 확인한다.
