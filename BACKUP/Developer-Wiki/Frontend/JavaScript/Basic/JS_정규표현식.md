---
title: JS_정규표현식
version: v1.0
last_updated: 2026-07-22
status: completed
---

# 문서 정보

| 항목 | 내용 |
|------|------|
| 문서명 | JS_정규표현식 |
| 분야 | Frontend / JavaScript |
| 버전 | v1.0 |
| 작성일 | 2026-07-22 |

---

# 개요

정규표현식(Regular Expression, RegExp)은 문자열이 특정한 규칙을 만족하는지 검사하거나, 원하는 문자열을 검색하고 치환하는 데 사용하는 패턴이다.

회원가입, 로그인, 검색 기능, 입력값 검증 등 실무 프로젝트에서 매우 자주 사용된다.

이번 문서에서는 JavaScript에서 정규표현식을 생성하고 문자열을 검사하는 기본적인 방법을 학습한다.

---

# 핵심 개념

정규표현식은 문자열 자체를 비교하는 것이 아니라 **문자열의 규칙(Pattern)** 을 비교한다.

예를 들어

```text
abc123
```

라는 문자열이 있다면

```text
영문 + 숫자
```

라는 규칙으로 검사할 수 있다.

---

# 정규표현식 작성 방법

방법 1

```javascript
const reg = /abc/;
```

방법 2

```javascript
const reg =
    new RegExp("abc");
```

실무에서는 대부분 `/패턴/` 형식을 사용한다.

---

# test()

가장 많이 사용하는 메서드이다.

문자열이 패턴과 일치하면 `true`, 그렇지 않으면 `false`를 반환한다.

```javascript
const reg = /abc/;

console.log(
    reg.test("abc")
);
```

출력

```text
true
```

---

```javascript
const reg = /abc/;

console.log(
    reg.test("hello")
);
```

출력

```text
false
```

---

# exec()

일치하는 문자열을 찾아 반환한다.

```javascript
const reg = /abc/;

console.log(
    reg.exec("123abc456")
);
```

출력 예시

```text
["abc"]
```

일치하지 않으면

```text
null
```

을 반환한다.

---

# 문자열 메서드와 함께 사용

```javascript
const text =
    "Hello JavaScript";

console.log(
    text.match(/Java/)
);
```

출력

```text
["Java"]
```

---

# 정규표현식의 기본 기호

| 기호 | 의미 |
|------|------|
| . | 임의의 한 문자 |
| * | 0개 이상 |
| + | 1개 이상 |
| ? | 0개 또는 1개 |
| \| | OR(또는) |
| [] | 문자 집합 |
| () | 그룹 |

---

# 문자 하나 검사

```javascript
const reg = /a/;

console.log(
    reg.test("apple")
);
```

출력

```text
true
```

문자열 안에 `a`가 하나라도 있으면 `true`를 반환한다.

---

# 여러 문자 중 하나

```javascript
const reg = /[abc]/;

console.log(
    reg.test("cat")
);
```

출력

```text
true
```

`a`, `b`, `c` 중 하나가 포함되어 있으면 일치한다.

---

# 숫자 검사

```javascript
const reg = /[0-9]/;

console.log(
    reg.test("abc123")
);
```

출력

```text
true
```

숫자가 하나 이상 포함되어 있는지 검사한다.

---

# 영문 소문자 검사

```javascript
const reg = /[a-z]/;

console.log(
    reg.test("Hello")
);
```

출력

```text
true
```

소문자가 하나 이상 포함되어 있는지 확인한다.

---

# 영문 대문자 검사

```javascript
const reg = /[A-Z]/;

console.log(
    reg.test("Hello")
);
```

출력

```text
true
```

---

# 실무 팁

정규표현식은 복잡한 패턴을 한 번에 작성하기보다, **작은 단위로 나누어 테스트하면서 작성하는 것이 좋다.**

예를 들어 이메일 검증을 만들 때도

1. 영문 검사
2. 숫자 검사
3. `@` 포함 여부
4. 도메인 검사

순서로 나누어 확인하면 디버깅이 훨씬 쉬워진다.

---

---

# 수량 지정자 {}

수량 지정자는 특정 문자가 몇 번 반복되는지 지정할 때 사용한다.

| 표현식 | 의미 |
|--------|------|
| {3} | 정확히 3번 |
| {2,5} | 2~5번 |
| {3,} | 3번 이상 |

---

# 정확히 3자리 숫자

```javascript
const reg = /^\d{3}$/;

console.log(
    reg.test("123")
);
```

출력

```text
true
```

```javascript
console.log(
    reg.test("12")
);
```

출력

```text
false
```

---

# 2~5자리 문자

```javascript
const reg = /^[a-z]{2,5}$/;

console.log(
    reg.test("hello")
);
```

출력

```text
true
```

---

# 시작(^)과 끝($)

정규표현식은 원하는 위치에서만 검사하도록 지정할 수 있다.

| 기호 | 의미 |
|------|------|
| ^ | 문자열의 시작 |
| $ | 문자열의 끝 |

예제

```javascript
const reg = /^abc$/;

console.log(
    reg.test("abc")
);
```

출력

```text
true
```

```javascript
console.log(
    reg.test("abc123")
);
```

출력

```text
false
```

`abc`만 정확하게 일치해야 한다.

---

# \d

숫자를 의미한다.

```javascript
const reg = /\d/;

console.log(
    reg.test("abc5")
);
```

출력

```text
true
```

---

# \w

영문, 숫자, 밑줄(`_`)을 의미한다.

```javascript
const reg = /\w+/;

console.log(
    reg.test("user_01")
);
```

출력

```text
true
```

---

# \s

공백을 의미한다.

```javascript
const reg = /\s/;

console.log(
    reg.test("Hello World")
);
```

출력

```text
true
```

---

# 플래그(flag)

정규표현식 뒤에 붙여 동작 방식을 변경한다.

| 플래그 | 의미 |
|--------|------|
| g | 전체 검색 |
| i | 대소문자 구분 안 함 |
| m | 여러 줄 검사 |

---

# i 플래그

```javascript
const reg = /javascript/i;

console.log(
    reg.test("JavaScript")
);
```

출력

```text
true
```

---

# g 플래그

```javascript
const text =
    "apple apple apple";

console.log(
    text.match(/apple/g)
);
```

출력

```text
["apple", "apple", "apple"]
```

---

# 이메일 검사

```javascript
const emailReg =

    /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}$/;

console.log(

    emailReg.test(
        "test@example.com"
    )

);
```

출력

```text
true
```

> **실무 팁**  
> 이메일 형식은 매우 다양하다. 대부분의 서비스에서는 RFC 규격 전체를 구현하기보다 일반적인 형식을 검사한 뒤, 실제 이메일 인증을 통해 최종 확인한다.

---

# 비밀번호 검사

예시 조건

- 영문
- 숫자
- 8~20자리

```javascript
const passwordReg =

    /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,20}$/;

console.log(

    passwordReg.test(
        "abc12345"
    )

);
```

출력

```text
true
```

---

# 전화번호 검사

```javascript
const phoneReg =

    /^010-\d{4}-\d{4}$/;

console.log(

    phoneReg.test(
        "010-1234-5678"
    )

);
```

출력

```text
true
```

---

# 아이디 검사

조건

- 영문 소문자로 시작
- 영문 소문자와 숫자 사용
- 5~20자리

```javascript
const idReg =

    /^[a-z][a-z0-9]{4,19}$/;

console.log(

    idReg.test(
        "user01"
    )

);
```

출력

```text
true
```

---

# 문자열 치환

`replace()`와 함께 사용하면 문자열을 변경할 수 있다.

```javascript
const text =
    "JavaScript";

console.log(

    text.replace(
        /Java/,
        "Type"
    )

);
```

출력

```text
TypeScript
```

---

# 실무 활용

정규표현식은 다음과 같은 기능에서 자주 사용된다.

- 회원가입 입력 검증
- 로그인
- 비밀번호 변경
- 이메일 검사
- 전화번호 검사
- 검색 기능
- 문자열 치환
- 금지어 필터링

---

# 정규표현식 디버깅

문제가 발생하면 다음 사항을 확인한다.

```text
1. ^와 $를 올바르게 사용했는가?
2. 수량 지정자({})가 조건과 맞는가?
3. 대소문자 구분이 필요한가?
4. i, g 플래그를 적절히 사용했는가?
5. test()와 match()의 목적을 구분했는가?
6. 실제 입력값으로 충분히 테스트했는가?
```

---

---

# 실무 예제 프로젝트

이번 예제에서는 회원가입 폼의 이메일과 비밀번호를 검사한다.

## HTML

```html
<form id="signupForm">

    <input
        type="text"
        id="email"
        placeholder="이메일">

    <input
        type="password"
        id="password"
        placeholder="비밀번호">

    <button>

        가입하기

    </button>

</form>
```

---

## JavaScript

```javascript
const form =
    document.querySelector(
        "#signupForm"
    );

const email =
    document.querySelector(
        "#email"
    );

const password =
    document.querySelector(
        "#password"
    );

const emailReg =
    /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}$/;

const passwordReg =
    /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,20}$/;

form.addEventListener(
    "submit",
    function(event){

        event.preventDefault();

        if(!emailReg.test(email.value)){

            alert("이메일 형식이 올바르지 않습니다.");

            return;

        }

        if(!passwordReg.test(password.value)){

            alert("비밀번호 형식이 올바르지 않습니다.");

            return;

        }

        alert("회원가입 성공");

    }
);
```

---

# 예제 코드 흐름

```text
사용자 입력
      ↓
submit 이벤트
      ↓
event.preventDefault()
      ↓
이메일 검사
      ↓
비밀번호 검사
      ↓
통과
      ↓
회원가입 처리
```

---

# replace() 활용 예제

숫자를 제외한 문자를 제거하는 예제이다.

```javascript
const phone =
    "010-1234-5678";

const result =
    phone.replace(
        /[^0-9]/g,
        ""
    );

console.log(result);
```

출력

```text
01012345678
```

---

# match() 활용 예제

문자열에서 모든 숫자를 찾는다.

```javascript
const text =
    "A10 B20 C30";

console.log(
    text.match(/\d+/g)
);
```

출력

```text
["10", "20", "30"]
```

---

# 자주 하는 실수

## ^와 $를 생략하는 경우

잘못된 코드

```javascript
const reg =
    /abc/;
```

```text
abc123
```

도 통과한다.

올바른 코드

```javascript
const reg =
    /^abc$/;
```

---

## test() 대신 == 비교하는 경우

잘못된 코드

```javascript
if(email.value == emailReg){

    ...

}
```

정규표현식은 문자열과 직접 비교하지 않는다.

올바른 코드

```javascript
if(emailReg.test(email.value)){

    ...

}
```

---

## 점(.)을 그대로 사용하는 경우

```javascript
/a.b/
```

에서 `.`은 **마침표가 아니라 임의의 한 문자**를 의미한다.

마침표 자체를 검사하려면 이스케이프 문자를 사용해야 한다.

```javascript
/a\.b/
```

---

## 정규표현식을 너무 복잡하게 작성하는 경우

하나의 거대한 패턴으로 작성하기보다,

- 아이디
- 이메일
- 비밀번호

처럼 목적별로 분리하는 것이 유지보수에 유리하다.

---

# 디버깅 체크리스트

```text
1. ^와 $를 사용했는가?
2. test()를 사용했는가?
3. 수량 지정자가 올바른가?
4. 점(.)의 의미를 이해했는가?
5. 필요한 플래그(i, g)를 사용했는가?
6. 실제 입력값으로 충분히 테스트했는가?
7. 복잡한 패턴은 단계별로 나누어 확인했는가?
```

---

# 이번 문서에서 배운 내용

- RegExp 객체
- test()
- exec()
- match()
- replace()
- 문자 클래스
- 수량 지정자
- 시작(^), 끝($)
- \d
- \w
- \s
- 플래그(g, i, m)
- 이메일 검사
- 비밀번호 검사
- 전화번호 검사
- 아이디 검사

---

# 면접 포인트

### 정규표현식이란 무엇인가?

문자열이 특정 규칙을 만족하는지 검사하거나 검색·치환하기 위한 패턴이다.

---

### test()와 match()의 차이는?

- `test()`는 패턴과 일치하는지 `true` 또는 `false`를 반환한다.
- `match()`는 일치한 문자열을 배열로 반환한다.

---

### ^와 $는 무엇을 의미하는가?

- `^`는 문자열의 시작을 의미한다.
- `$`는 문자열의 끝을 의미한다.

두 기호를 함께 사용하면 문자열 전체가 패턴과 일치하는지 검사할 수 있다.

---

### \d와 [0-9]의 차이는?

일반적인 숫자 검사에서는 같은 의미로 사용할 수 있다.

`\d`는 숫자를 의미하는 축약 표현이다.

---

### 이메일 검증을 정규표현식만으로 완벽하게 할 수 있는가?

아니다.

정규표현식은 일반적인 형식을 검사하는 데 적합하며, 실제 이메일 사용 가능 여부는 인증 메일 발송 등의 절차를 통해 확인해야 한다.

---

# 핵심 정리

- 정규표현식은 문자열의 규칙을 검사하는 도구이다.
- `test()`는 입력값 검증에서 가장 많이 사용된다.
- `match()`와 `replace()`를 함께 사용하면 검색과 치환을 쉽게 구현할 수 있다.
- `^`와 `$`를 사용하면 전체 문자열을 검사할 수 있다.
- 이메일, 비밀번호, 전화번호 등 다양한 입력 검증에 활용된다.
- 복잡한 패턴은 단계적으로 작성하고 테스트하는 것이 유지보수에 유리하다.

---

# 변경 이력

| Version | 날짜 | 변경 내용 |
|---------|------|-----------|
| v1.0 | 2026-07-22 | 최초 작성 |
