---
title: Python 조건문과 패턴 매칭
version: v2.0-final
last_updated: 2026-08-06
status: Completed
---

# Python 조건문과 패턴 매칭

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `08_Python_조건문과_패턴매칭.md` |
| 분류 | `04_Python` |
| 원본 기준 | `workspace_python/08_if.py`, `workspace_teacher/workspace_python/_08_if.py` |
| 핵심 범위 | 비교식, `if`, 들여쓰기, `pass`, Truthy/Falsy, 중첩 조건문, `elif`, `match·case`, 조건 표현식 |
| 실습 범위 | 점수 유효성 검사, 합격 판정, 자판기 메뉴, 계절 분류 |
| 문서 형식 | Python Developer-Wiki V2 확정 형식 |

> 이 문서는 내 코드와 강사님 코드 전체를 그대로 나열하지 않는다.  
> 조건 판단에 필요한 핵심 코드만 발췌하고, 실행 순서·들여쓰기·오류 조건·실무 개선 방향을 함께 설명한다.

---

# 개요

조건문은 프로그램이 상황에 따라 다른 코드를 실행하도록 만든다.

```text
조건 확인
    ↓
참이면 실행
    ↓
거짓이면 다른 코드 실행
```

예를 들어 다음과 같은 판단에 사용한다.

- 점수가 80점 이상인지
- 사용자가 로그인했는지
- 재고가 남아 있는지
- 입력값이 올바른 범위인지
- 선택한 메뉴 번호가 존재하는지

```python
score = 85

if score >= 80:
    print("합격")
else:
    print("불합격")
```

출력:

```text
합격
```

> [!IMPORTANT]
> 조건문은 단순히 `True`와 `False`를 확인하는 문법이 아니다.
>
> 프로그램의 실행 경로를 결정하는 핵심 제어문이다.

---

# 핵심 개념

| 개념 | 핵심 역할 |
| --- | --- |
| 조건식 | 참·거짓으로 평가되는 표현식 |
| `if` | 조건이 참일 때 코드 실행 |
| `elif` | 앞 조건이 거짓일 때 추가 조건 검사 |
| `else` | 모든 앞 조건이 거짓일 때 실행 |
| 들여쓰기 | 조건문 내부 코드 블록 구분 |
| `pass` | 아무 작업 없이 문법적 자리만 채움 |
| Truthy/Falsy | 값을 참 또는 거짓처럼 평가하는 규칙 |
| 중첩 조건문 | 조건문 안에 다른 조건문 작성 |
| 연속 비교 | 여러 비교를 하나의 식으로 표현 |
| `match·case` | 값 또는 패턴에 따라 분기 |
| 조건 표현식 | 한 줄로 조건에 따른 값 선택 |

---

# 학습 목표

이 문서를 학습한 뒤 다음 내용을 설명하고 작성할 수 있어야 한다.

- 비교 연산의 결과가 불리언임을 이해한다.
- 연속 비교식을 작성할 수 있다.
- `if`, `elif`, `else`의 실행 순서를 설명할 수 있다.
- Python 조건문에서 들여쓰기가 필요한 이유를 이해한다.
- 잘못된 들여쓰기로 발생하는 오류를 찾을 수 있다.
- `pass`의 역할을 설명할 수 있다.
- Truthy/Falsy 값을 구분할 수 있다.
- 빈 리스트가 거짓으로 평가됨을 이해한다.
- 중첩 조건문을 작성할 수 있다.
- 점수 범위를 검증하고 평균을 계산할 수 있다.
- 내장 함수 이름을 변수명으로 사용하면 안 되는 이유를 이해한다.
- `elif`로 여러 조건을 순서대로 검사할 수 있다.
- `match·case`의 기본 구조를 사용할 수 있다.
- 여러 값을 `|`로 묶어 하나의 `case`에서 처리할 수 있다.
- `case _`의 역할을 설명할 수 있다.
- 조건 표현식을 작성하고 복잡한 중첩을 피할 수 있다.

---

# 1. 비교식의 결과

## 1-1. 내 코드와 강사님 코드

```python
a = 10
b = 5

print(3 < a < 20)
```

## 1-2. 출력 결과

```text
True
```

## 1-3. 연속 비교 해석

```python
3 < a < 20
```

다음 조건과 같은 의미다.

```python
3 < a and a < 20
```

`a`가 3보다 크고 20보다 작은지 확인한다.

> [!TIP]
> 범위 검사는 연속 비교식으로 작성하면 의도가 더 명확하게 보인다.

---

# 2. `if` 기본 구조

```python
if 조건식:
    실행문
```

조건식이 참이면 들여쓰기된 코드가 실행된다.

```python
if True:
    print(1)
```

출력:

```text
1
```

조건식이 거짓이면 내부 코드를 건너뛴다.

```python
if False:
    print("실행되지 않음")
```

---

# 3. 들여쓰기

## 3-1. 원본 코드

```python
if True:
    print(1)
    print(3)

    if True:
        print(4)
```

## 3-2. 출력 결과

```text
1
3
4
```

같은 들여쓰기 깊이는 같은 블록에 속한다.

```text
if True:
    print(1)       ┐
    print(3)       ├ 같은 블록
                   │
    if True:       │
        print(4)   ┘ 중첩 블록
```

> [!IMPORTANT]
> Python은 중괄호가 아니라 들여쓰기로 코드 블록을 구분한다.

---

# 4. 들여쓰기 오류

원본에는 다음 메모가 있다.

```python
# Indent가 들어가면 들여쓰기 오류
# IndentationError: unindent does not match any outer indentation level
```

## 4-1. 잘못된 코드

```text
if True:
    print(1)
  print(2)
```

발생 결과:

```text
IndentationError
```

## 4-2. 올바른 코드

```python
if True:
    print(1)
    print(2)
```

## 4-3. 주의할 점

- 같은 블록은 같은 깊이로 들여쓴다.
- 공백 4칸을 일반적으로 사용한다.
- 탭과 공백을 섞지 않는다.
- 블록이 끝나면 들여쓰기를 원래 위치로 되돌린다.

---

# 5. 중첩 조건문

조건문 안에 다른 조건문을 작성할 수 있다.

```python
is_logged_in = True
is_admin = True

if is_logged_in:
    print("로그인 사용자")

    if is_admin:
        print("관리자 권한")
```

## 5-1. 출력 결과

```text
로그인 사용자
관리자 권한
```

## 5-2. 실행 순서

```text
로그인 여부 확인
    ↓ 참
관리자 여부 확인
    ↓ 참
관리자 권한 출력
```

> [!WARNING]
> 중첩이 너무 깊어지면 실행 흐름을 이해하기 어렵다.
>
> 처리하지 않을 조건을 먼저 종료하거나 논리 연산자로 단순화할 수 있는지 검토한다.

---

# 6. `pass`

## 6-1. 내 코드와 강사님 코드

```python
if True:
    pass
else:
    pass
```

## 6-2. 역할

`pass`는 아무 작업도 하지 않고 넘어간다.

Python은 블록 안에 최소 하나의 문장이 필요하므로, 아직 구현하지 않은 위치를 임시로 채울 때 사용한다.

```python
def save_user():
    pass
```

## 6-3. 주의점

`pass`를 사용했다고 기능이 구현된 것은 아니다.

> [!TIP]
> 임시 코드임을 명확히 하려면 작업 항목이나 이슈와 연결해 관리한다.

---

# 7. 불리언이 아닌 조건식

## 7-1. 원본 코드

```python
if 1:
    print("참")
```

## 7-2. 출력 결과

```text
참
```

조건식에는 `True`와 `False`뿐 아니라 Truthy/Falsy 규칙으로 평가할 수 있는 값도 사용할 수 있다.

---

# 8. Falsy 값

원본에는 다음 값들이 거짓으로 평가된다고 정리되어 있다.

```text
False
None
0
0.0
빈 문자열
빈 리스트
빈 튜플
빈 딕셔너리
빈 집합
```

실행:

```python
values = [
    False,
    None,
    0,
    0.0,
    "",
    [],
    (),
    {},
    set(),
]

for value in values:
    print(bool(value))
```

출력:

```text
False
False
False
False
False
False
False
False
False
```

---

# 9. Truthy 값

Falsy가 아닌 대부분의 값은 참처럼 평가된다.

```python
values = [
    True,
    1,
    -1,
    "Python",
    [0],
    (0,),
    {"key": 0},
]

for value in values:
    print(bool(value))
```

출력:

```text
True
True
True
True
True
True
True
```

> [!IMPORTANT]
> 컨테이너 안의 값이 `0`이나 `False`여도 컨테이너 자체가 비어 있지 않으면 Truthy다.

---

# 10. 빈 리스트 검사

## 10-1. 내 코드와 강사님 코드

```python
values = []

if values:
    print("참")
else:
    print("거짓")
```

## 10-2. 출력 결과

```text
거짓
```

## 10-3. 실무형 표현

목록이 비어 있는지 확인할 때는 다음처럼 작성한다.

```python
if not values:
    print("목록이 비어 있습니다.")
```

`len(values) == 0`보다 의도가 간결하게 드러난다.

---

# 11. `if·else`

조건이 참일 때와 거짓일 때 서로 다른 코드를 실행한다.

```python
score = 75

if score >= 80:
    print("합격")
else:
    print("불합격")
```

출력:

```text
불합격
```

`else`에는 조건식을 작성하지 않는다.

---

# 12. 점수 입력

## 12-1. 원본 코드

```python
score_text = input(
    "점수 4개 입력, 띄어쓰기로 구분 : "
)

scores = score_text.split(" ")
```

사용자가 다음과 같이 입력한다고 가정한다.

```text
90 85 80 95
```

`scores`의 값:

```text
['90', '85', '80', '95']
```

## 12-2. 주의점

`split(" ")`은 공백이 여러 개일 때 빈 문자열을 만들 수 있다.

더 안전한 기본 방식:

```python
scores = score_text.split()
```

전달인자 없는 `split()`은 연속된 공백을 하나의 구분처럼 처리한다.

---

# 13. 점수를 정수로 변환

원본에서는 각 인덱스를 직접 변환한다.

```python
total = (
    int(scores[0])
    + int(scores[1])
    + int(scores[2])
    + int(scores[3])
)
```

리스트 컴프리헨션으로 한 번에 변환할 수 있다.

```python
scores = [
    int(score)
    for score in score_text.split()
]
```

입력:

```text
90 85 80 95
```

결과:

```text
[90, 85, 80, 95]
```

---

# 14. 내장 함수 이름을 변수명으로 사용하지 않기

원본에서는 다음 이름을 사용한다.

```python
sum = (
    int(scores[0])
    + int(scores[1])
    + int(scores[2])
    + int(scores[3])
)
```

`sum`은 Python 내장 함수 이름이다.

변수에 같은 이름을 사용하면 이후 `sum()` 함수를 호출할 수 없게 된다.

## 14-1. 개선

```python
total_score = sum(scores)
average_score = (
    total_score / len(scores)
)
```

> [!WARNING]
> `sum`, `list`, `str`, `input`, `type` 같은 내장 함수 이름을 변수명으로 사용하지 않는다.

---

# 15. 점수 범위 검사

## 15-1. 원본 코드

```python
if (
    0 <= scores[0] <= 100
    and 0 <= scores[1] <= 100
    and 0 <= scores[2] <= 100
    and 0 <= scores[3] <= 100
):
    print("올바른 점수")
```

각 점수가 0부터 100 사이인지 검사한다.

## 15-2. `all()`로 개선

```python
is_valid = all(
    0 <= score <= 100
    for score in scores
)

print(is_valid)
```

출력:

```text
True
```

`all()`은 모든 조건이 참일 때 `True`를 반환한다.

---

# 16. 줄 연속 문자 `\`

원본에서는 긴 조건문을 다음 줄로 연결하기 위해 백슬래시를 사용한다.

```python
if condition_a \
    and condition_b:
    pass
```

문법적으로 가능하지만 괄호를 사용하는 편이 안전하고 읽기 쉽다.

```python
if (
    condition_a
    and condition_b
):
    pass
```

> [!TIP]
> 백슬래시 뒤에 공백이 들어가면 오류가 발생할 수 있다.
>
> 긴 표현식은 괄호로 묶어 여러 줄로 작성한다.

---

# 17. 중첩 합격 판정

## 17-1. 원본 흐름

```python
if is_valid:
    if average_score >= 80:
        print("합격")
    else:
        print("불합격")
else:
    print("잘못된 입력입니다.")
```

## 17-2. 실행 예시

점수:

```text
90 85 80 95
```

평균:

```text
87.5
```

출력:

```text
합격
```

## 17-3. 역할

```text
첫 번째 조건
→ 점수 범위가 올바른가?

두 번째 조건
→ 평균이 80 이상인가?
```

---

# 18. 점수 개수 검증

원본 코드는 점수가 정확히 4개라고 가정한다.

입력 개수가 부족하면 `IndexError`, 많으면 의도하지 않은 결과가 발생할 수 있다.

```python
if len(scores) != 4:
    print("점수는 4개 입력해야 합니다.")
```

범위 검사보다 먼저 개수를 확인해야 한다.

---

# 19. 개선된 점수 판정 예제

```python
score_text = input(
    "점수 4개 입력: "
)

try:
    scores = [
        int(score)
        for score in score_text.split()
    ]
except ValueError:
    print("점수는 숫자로 입력해야 합니다.")
else:
    if len(scores) != 4:
        print("점수는 4개 입력해야 합니다.")
    elif not all(
        0 <= score <= 100
        for score in scores
    ):
        print("점수는 0~100 사이여야 합니다.")
    else:
        average_score = (
            sum(scores) / len(scores)
        )

        if average_score >= 80:
            print("합격")
        else:
            print("불합격")
```

예외 처리는 14번 문서에서 더 자세히 다룬다.

---

# 20. `if·elif·else`

여러 조건을 순서대로 검사할 때 `elif`를 사용한다.

## 20-1. 원본 자판기 코드

```python
button = int(
    input("번호를 입력하세요: ")
)

if button == 1:
    print("콜라")
elif button == 2:
    print("사이다")
elif button == 3:
    print("환타")
else:
    print("잘못 입력하셨습니다.")
```

## 20-2. 실행 예시

입력:

```text
2
```

출력:

```text
사이다
```

---

# 21. `elif` 실행 순서

```text
if 조건 확인
    ↓ 거짓
첫 번째 elif 확인
    ↓ 거짓
두 번째 elif 확인
    ↓ 참
해당 블록 실행
    ↓
나머지 조건은 검사하지 않음
```

조건은 위에서 아래로 검사한다.

> [!IMPORTANT]
> 여러 조건이 동시에 참일 수 있다면 더 구체적인 조건을 위에 작성한다.

---

# 22. 조건 순서의 중요성

잘못된 순서:

```python
score = 95

if score >= 60:
    print("합격")
elif score >= 90:
    print("우수")
```

출력:

```text
합격
```

`score >= 60`이 먼저 참이므로 뒤 조건은 검사하지 않는다.

개선:

```python
if score >= 90:
    print("우수")
elif score >= 60:
    print("합격")
else:
    print("불합격")
```

출력:

```text
우수
```

---

# 23. 딕셔너리를 이용한 메뉴 조회

조건이 단순한 값 매핑이라면 딕셔너리도 사용할 수 있다.

```python
menu = {
    1: "콜라",
    2: "사이다",
    3: "환타",
}

button = 2

drink = menu.get(
    button,
    "잘못 입력하셨습니다.",
)

print(drink)
```

출력:

```text
사이다
```

> [!TIP]
> 단순히 키와 결과를 연결하는 분기는 딕셔너리가 더 간결할 수 있다.
>
> 각 분기에서 복잡한 처리가 필요하면 조건문이 더 적합하다.

---

# 24. `match·case`

Python 3.10 이상에서는 `match·case`로 값을 분기할 수 있다.

## 24-1. 기본 구조

```python
match value:
    case pattern_1:
        ...
    case pattern_2:
        ...
    case _:
        ...
```

`match` 대상이 어떤 `case` 패턴과 일치하는지 위에서 아래로 확인한다.

---

# 25. 여러 값 패턴 `|`

## 25-1. 원본 코드

```python
month = 7

match month:
    case 6 | 7 | 8:
        print("여름")
    case _:
        print("그 외")
```

## 25-2. 출력 결과

```text
여름
```

`|`는 여러 패턴 중 하나와 일치하면 같은 코드를 실행한다.

```text
6 또는 7 또는 8
→ 여름
```

---

# 26. 원본의 계절 설명 바로잡기

내 코드에는 다음 코드가 있다.

```text
case 6 | 7 | 8:
    print("봄")
```

하지만 일반적인 한국 계절 구분에서 6·7·8월은 여름에 해당한다.

강사님 코드는 `"여름"`으로 출력한다.

개선:

```python
match month:
    case 3 | 4 | 5:
        print("봄")
    case 6 | 7 | 8:
        print("여름")
    case 9 | 10 | 11:
        print("가을")
    case 12 | 1 | 2:
        print("겨울")
    case _:
        print("올바른 월이 아닙니다.")
```

---

# 27. `case _`

`case _`는 앞의 어떤 패턴에도 일치하지 않을 때 실행된다.

```python
value = "unknown"

match value:
    case "admin":
        print("관리자")
    case "user":
        print("일반 사용자")
    case _:
        print("알 수 없는 역할")
```

출력:

```text
알 수 없는 역할
```

`if`문의 `else`와 비슷한 기본 분기 역할을 한다.

---

# 28. `match·case`에는 `break`가 필요하지 않다

원본에는 `break`가 필요 없다는 메모가 있다.

```text
하나의 case가 일치
    ↓
해당 블록 실행
    ↓
match문 종료
```

C나 JavaScript의 전통적인 `switch`문처럼 다음 `case`로 자동 진행되지 않는다.

---

# 29. 문자열 패턴

```python
season = "여름"

match season:
    case "봄":
        print("따뜻합니다.")
    case "여름":
        print("덥습니다.")
    case "가을":
        print("선선합니다.")
    case "겨울":
        print("춥습니다.")
    case _:
        print("알 수 없습니다.")
```

출력:

```text
덥습니다.
```

---

# 30. `match·case` 선택 기준

```text
하나의 값과 여러 고정 패턴 비교
→ match·case 검토

범위 비교
→ if·elif

복잡한 논리 조건
→ if·elif

단순 키와 결과 연결
→ 딕셔너리 검토
```

> [!IMPORTANT]
> `match·case`는 단순히 `if`를 대체하는 문법이 아니다.
>
> 값의 구조나 패턴을 비교할 때 장점이 크다.

---

# 31. 조건 표현식

## 31-1. 내 코드

```python
print(
    3
    if 3 > 2
    else 2
)
```

## 31-2. 출력 결과

```text
3
```

## 31-3. 기본 구조

```python
참일_때_값 if 조건식 else 거짓일_때_값
```

다른 언어에서 삼항 연산자라고 부르는 기능과 비슷하지만 Python에서는 조건 표현식이라고 한다.

---

# 32. 조건 표현식 활용

```python
score = 85

result = (
    "합격"
    if score >= 80
    else "불합격"
)

print(result)
```

출력:

```text
합격
```

값 하나를 조건에 따라 선택할 때 적합하다.

---

# 33. 중첩 조건 표현식

강사님 코드에는 중첩 조건 표현식이 있다.

```python
result = (
    3
    if 3 > 2
    else (
        2
        if 2 < 3
        else 1
    )
)

print(result)
```

출력:

```text
3
```

문법적으로 가능하지만 여러 조건이 중첩되면 읽기 어려워진다.

개선:

```python
if first_condition:
    result = 3
elif second_condition:
    result = 2
else:
    result = 1
```

> [!WARNING]
> 조건 표현식은 간단한 값 선택에만 사용한다.
>
> 중첩이 필요하면 일반 `if·elif·else`가 더 읽기 쉽다.

---

# 34. Guard Clause

함수 안에서 처리하지 않을 조건을 먼저 종료하면 중첩을 줄일 수 있다.

```python
def get_result(
    scores,
):
    if len(scores) != 4:
        return "점수는 4개여야 합니다."

    if not all(
        0 <= score <= 100
        for score in scores
    ):
        return "점수 범위가 잘못되었습니다."

    average_score = (
        sum(scores) / len(scores)
    )

    if average_score >= 80:
        return "합격"

    return "불합격"
```

중첩 조건문보다 정상 흐름이 평평하게 보인다.

---

# 35. 내 코드와 강사님 코드 비교

| 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 연속 비교 | `3 < a < 20` | 동일 |
| 들여쓰기 | 오류 원인 메모 추가 | 기본 중첩 예제 |
| `pass` | 아무 일 없이 넘어간다고 설명 | 기본 사용 |
| Falsy | JavaScript의 `null`과 연결한 메모 | Python 값 중심 |
| 점수 문제 | 별도 평균 예제와 범위 검증 | 범위 검증 중심 |
| 줄 연결 | 백슬래시 사용 이유 설명 | 동일한 방식 사용 |
| 자판기 | 사용자 안내 문구 상세 | 기본 메뉴 문구 |
| `match` | 계절 출력에 `"봄"` 작성 | `"여름"` 작성 |
| 조건 표현식 | 기본 표현식 | 중첩 표현식 추가 |

## 35-1. 내 코드의 장점

- 들여쓰기 오류의 종류와 원인을 직접 기록했다.
- Truthy/Falsy 값과 `pass`의 역할을 이해하기 쉽게 메모했다.
- 점수 범위 검사와 합격 판정을 직접 구성했다.
- `match·case`와 조건 표현식의 의미를 주석으로 정리했다.

## 35-2. 내 코드의 개선점

- `sum`을 변수명으로 사용하면 내장 함수 `sum()`을 가린다.
- 점수 개수와 숫자 변환 오류도 함께 검증해야 한다.
- 6·7·8월을 `"봄"`으로 출력한 부분은 `"여름"`으로 수정해야 한다.
- 백슬래시보다 괄호를 이용한 여러 줄 조건식이 안전하다.
- 중첩 조건은 Guard Clause나 함수 분리를 검토할 수 있다.

## 35-3. 강사님 코드의 장점

- `if`의 기본 구조부터 `match·case`까지 흐름이 연결된다.
- Truthy/Falsy와 빈 리스트 조건을 직접 확인할 수 있다.
- 평균 점수와 자판기 문제로 조건 분기를 실습할 수 있다.
- 중첩 조건 표현식까지 확인할 수 있다.

## 35-4. 강사님 코드의 보충점

- 점수 입력 개수와 숫자 변환 예외 검사가 필요하다.
- `sum` 변수명 문제를 설명할 필요가 있다.
- 중첩 조건 표현식은 가독성 주의가 필요하다.
- `match·case`가 범위 조건보다 패턴 분기에 적합하다는 설명이 필요하다.

---

# 36. 기존 코드에서 개선 코드로 바꾼 이유

## 36-1. `sum` 변수명 변경

기존:

```python
sum = 350
```

개선:

```python
total_score = 350
```

이유:

- Python 내장 함수 `sum()`을 그대로 사용할 수 있다.
- 값의 의미가 명확하다.

## 36-2. `split(" ")` 개선

기존:

```python
scores = text.split(" ")
```

개선:

```python
scores = text.split()
```

이유:

- 연속된 공백에도 빈 문자열이 생기지 않는다.

## 36-3. 반복 조건을 `all()`로 개선

기존:

```python
(
    0 <= scores[0] <= 100
    and 0 <= scores[1] <= 100
    and 0 <= scores[2] <= 100
    and 0 <= scores[3] <= 100
)
```

개선:

```python
all(
    0 <= score <= 100
    for score in scores
)
```

## 36-4. 백슬래시 대신 괄호

기존:

```python
if condition_a \
    and condition_b:
    pass
```

개선:

```python
if (
    condition_a
    and condition_b
):
    pass
```

---

# 37. 실무형 예제: 주문 상태 안내

```python
order = {
    "paid": True,
    "stock_available": True,
    "shipped": False,
}

if not order["paid"]:
    message = "결제가 필요합니다."
elif not order["stock_available"]:
    message = "재고가 부족합니다."
elif order["shipped"]:
    message = "배송이 시작되었습니다."
else:
    message = "배송을 준비하고 있습니다."

print(message)
```

## 37-1. 출력 결과

```text
배송을 준비하고 있습니다.
```

## 37-2. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| 딕셔너리 | 주문 상태를 키와 값으로 저장 |
| `not` | 거짓 상태를 자연스럽게 확인 |
| `if·elif·else` | 우선순위에 따라 상태 분기 |
| `message` | 최종 안내 문구 저장 |

## 37-3. 조건 순서

```text
결제 여부
    ↓
재고 여부
    ↓
배송 여부
    ↓
배송 준비 상태
```

더 중요한 차단 조건을 먼저 검사한다.

---

# 38. 대표 오류로 이해하기

## 38-1. 콜론 누락

```text
if score >= 80
    print("합격")
```

발생 결과:

```text
SyntaxError
```

개선:

```python
if score >= 80:
    print("합격")
```

---

## 38-2. 들여쓰기 누락

```text
if score >= 80:
print("합격")
```

발생 결과:

```text
IndentationError
```

---

## 38-3. `=`와 `==` 혼동

```text
if button = 1:
    print("콜라")
```

발생 결과:

```text
SyntaxError
```

비교에는 `==`를 사용한다.

---

## 38-4. 점수 개수 부족

```python
scores = [
    "90",
    "80",
]

print(scores[3])
```

발생 결과:

```text
IndexError
```

인덱스 접근 전에 개수를 확인한다.

---

## 38-5. 숫자가 아닌 입력

```python
int("점수")
```

발생 결과:

```text
ValueError
```

예외 처리 또는 입력 검증이 필요하다.

---

## 38-6. `match` 기본 분기 누락

모든 입력 경우를 처리해야 한다면 `case _`를 작성한다.

```python
match button:
    case 1:
        print("콜라")
    case _:
        print("메뉴 없음")
```

---

# 39. 자주 하는 실수

## 39-1. `if` 뒤 콜론 누락

`SyntaxError`가 발생한다.

## 39-2. 같은 블록의 들여쓰기 깊이가 다름

`IndentationError`가 발생할 수 있다.

## 39-3. `pass`가 기능을 실행한다고 생각

아무 작업도 하지 않는다.

## 39-4. 빈 리스트 안에 값 `0`이 있으면 Falsy라고 생각

`[0]`은 비어 있지 않으므로 Truthy다.

## 39-5. `else`에 조건식을 작성

추가 조건은 `elif`를 사용한다.

## 39-6. 더 넓은 조건을 먼저 작성

뒤의 구체적인 조건이 실행되지 않을 수 있다.

## 39-7. 사용자 입력을 바로 숫자로 믿음

`input()`은 문자열을 반환한다.

## 39-8. 입력 개수를 확인하지 않고 인덱스 접근

`IndexError`가 발생할 수 있다.

## 39-9. `sum`을 변수명으로 사용

내장 함수 `sum()`을 가린다.

## 39-10. 긴 조건식에 백슬래시 사용

괄호가 더 안전하고 읽기 쉽다.

## 39-11. `match·case`를 모든 조건문에 사용

범위와 복잡한 논리 조건은 `if·elif`가 더 적합하다.

## 39-12. 조건 표현식을 여러 단계 중첩

가독성이 크게 떨어질 수 있다.

---

# 40. 핵심 요약

```text
if
→ 첫 조건 검사

elif
→ 추가 조건 검사

else
→ 모든 조건이 거짓일 때
```

```text
들여쓰기
→ 조건문 블록 구분

pass
→ 아무 작업 없이 통과

Truthy/Falsy
→ 값을 참·거짓처럼 평가
```

```text
match value
→ 대상 확인

case pattern
→ 패턴 분기

case _
→ 기본 분기

|
→ 여러 패턴 중 하나
```

```text
참값 if 조건 else 거짓값
→ 조건 표현식
```

---

# 41. 최종 체크리스트

- [ ] 비교식의 결과가 `True` 또는 `False`임을 이해했는가?
- [ ] 연속 비교식을 작성할 수 있는가?
- [ ] `if`, `elif`, `else`의 실행 순서를 설명할 수 있는가?
- [ ] 조건문 내부를 공백 4칸으로 들여쓸 수 있는가?
- [ ] 잘못된 들여쓰기 오류를 찾을 수 있는가?
- [ ] `pass`의 역할을 설명할 수 있는가?
- [ ] 대표적인 Falsy 값을 구분할 수 있는가?
- [ ] 빈 리스트를 `not values`로 확인할 수 있는가?
- [ ] 중첩 조건문을 작성할 수 있는가?
- [ ] 사용자 입력값을 숫자로 변환할 수 있는가?
- [ ] 입력 개수를 먼저 검증할 수 있는가?
- [ ] `sum` 같은 내장 함수 이름을 변수로 사용하지 않는가?
- [ ] `all()`로 여러 값의 범위를 검사할 수 있는가?
- [ ] 긴 조건식을 괄호로 여러 줄 작성할 수 있는가?
- [ ] 조건 우선순위를 고려해 `elif` 순서를 정할 수 있는가?
- [ ] `match·case`의 기본 구조를 사용할 수 있는가?
- [ ] `|`로 여러 패턴을 하나의 `case`에 작성할 수 있는가?
- [ ] `case _`로 기본 분기를 처리할 수 있는가?
- [ ] 조건 표현식을 간단한 값 선택에 사용할 수 있는가?
- [ ] 복잡한 중첩 조건을 줄일 방법을 검토했는가?

---

# 마무리

조건문의 핵심은 참·거짓을 확인하는 것에서 끝나지 않는다.

```text
입력값을 검증하고
    ↓
조건의 우선순위를 정하고
    ↓
상황에 맞는 실행 경로를 선택하고
    ↓
잘못된 입력을 안전하게 처리하는 것
```

이 흐름을 이해하면 이후 반복문과 함수 안에서 프로그램의 동작을 더 명확하게 제어할 수 있다.
