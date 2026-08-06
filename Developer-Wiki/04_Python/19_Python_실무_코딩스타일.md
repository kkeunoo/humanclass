---
title: Python 실무 코딩 스타일
version: v2.0-final
last_updated: 2026-08-06
status: Completed
---

# Python 실무 코딩 스타일

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `19_Python_실무_코딩스타일.md` |
| 분류 | `04_Python` |
| 권장 선수 학습 | `01~18` Python 문서 |
| 다음 학습 | `20_Python_종합실습.md` |
| 문서 성격 | Python 실무 예제 및 리팩토링 기준 문서 |
| 핵심 범위 | 이름 작성, 조건문, 반복문, 함수 분리, 자료구조 활용, 예외 처리, 타입 힌트, 클래스 설계, 파일 경로, import, 리팩토링 |
| 예제 형식 | Before → After → 실행 결과 → 개선 이유 → 실무 선택 기준 |
| 종합 실습 | 별도 문서 `20_Python_종합실습.md`에서 관리 |
| 문서 형식 | Python Developer-Wiki V2 확정 형식 |

> 이 문서는 새로운 문법을 배우는 문서가 아니다.  
> 지금까지 배운 Python 문법을 **실무에서는 왜, 어떻게 선택하고 조합하는지** 설명하는 실무 예제 문서다.

---

# 개요

실행되는 코드가 반드시 좋은 코드는 아니다.

다음 두 코드는 같은 결과를 출력한다.

```python
for index in range(len(users)):
    print(users[index])
```

```python
for user in users:
    print(user)
```

두 코드 모두 동작하지만 두 번째 코드는 의도가 더 분명하다.

```text
첫 번째 코드
→ 인덱스를 만들고
→ 인덱스로 값을 다시 조회

두 번째 코드
→ 사용자 객체를 직접 순회
```

실무 코드는 다음 질문을 계속 확인한다.

```text
이름만 보고 역할을 알 수 있는가?
    ↓
코드의 의도가 바로 보이는가?
    ↓
수정할 범위가 명확한가?
    ↓
잘못된 상태를 막을 수 있는가?
    ↓
다른 개발자가 안전하게 사용할 수 있는가?
```

> [!IMPORTANT]
> 실무 코딩 스타일의 목적은 코드를 무조건 짧게 만드는 것이 아니다.
>
> **읽기 쉽고, 변경하기 쉽고, 잘못 사용하기 어려운 코드**를 만드는 것이 목적이다.

---

# 공통 실무 데이터

이 문서에서는 다음 사용자 데이터를 여러 예제에서 함께 사용한다.

```python
users = [
    {
        "id": 1,
        "name": "Kim",
        "age": 21,
        "active": True,
        "email": "kim@example.com",
        "score": 85,
    },
    {
        "id": 2,
        "name": "Lee",
        "age": 17,
        "active": False,
        "email": "lee@example.com",
        "score": 58,
    },
    {
        "id": 3,
        "name": "Park",
        "age": 28,
        "active": True,
        "email": "park@example.com",
        "score": 92,
    },
]
```

한 가지 데이터로 다음 개념을 연결한다.

- 조건문
- 반복문
- `enumerate()`
- `zip()`
- `any()`와 `all()`
- 리스트 컴프리헨션
- `sorted()`
- 함수 분리
- 타입 힌트
- 예외 처리
- 클래스 설계
- 리팩토링

---

# 핵심 기준

| 기준 | 의미 |
| --- | --- |
| 가독성 | 코드의 의도를 빠르게 이해할 수 있음 |
| 명확한 이름 | 변수·함수·클래스의 역할이 이름에 드러남 |
| 단일 책임 | 함수나 클래스가 하나의 주요 역할을 담당 |
| 중복 최소화 | 같은 로직을 여러 곳에 반복하지 않음 |
| 예측 가능성 | 입력과 결과, 오류 흐름이 분명함 |
| 확장성 | 기능 추가 시 기존 코드를 크게 깨지 않음 |
| 테스트 가능성 | 작은 단위로 입력과 결과를 확인할 수 있음 |
| Pythonic | Python의 기본 문법과 관례를 자연스럽게 활용 |

---

# 학습 목표

이 문서를 학습한 뒤 다음 내용을 판단하고 작성할 수 있어야 한다.

- 실행되는 코드와 유지보수하기 좋은 코드의 차이를 설명할 수 있다.
- 의미가 분명한 변수명과 함수명을 작성할 수 있다.
- 인덱스가 필요하지 않을 때 직접 순회할 수 있다.
- 인덱스가 필요할 때 `enumerate()`를 선택할 수 있다.
- 두 반복 가능한 객체를 함께 처리할 때 `zip()`을 사용할 수 있다.
- 비어 있는 컬렉션을 Pythonic하게 검사할 수 있다.
- `dict.get()`과 직접 키 접근의 차이를 구분할 수 있다.
- `any()`와 `all()`의 사용 상황을 판단할 수 있다.
- 컴프리헨션이 적합한 경우와 반복문이 더 좋은 경우를 구분할 수 있다.
- `sorted()`의 `key`를 이용해 객체 목록을 정렬할 수 있다.
- 함수 하나의 책임을 작게 분리할 수 있다.
- Guard Clause로 중첩 조건을 줄일 수 있다.
- 매직 넘버와 매직 문자열을 상수로 분리할 수 있다.
- 가변 기본 인자의 문제를 설명할 수 있다.
- 타입 힌트와 Docstring의 목적을 이해한다.
- 넓은 예외 처리보다 구체적인 예외 처리를 작성할 수 있다.
- `pathlib.Path`로 파일 경로를 다룰 수 있다.
- 클래스가 필요한 상황과 함수·딕셔너리로 충분한 상황을 구분할 수 있다.
- 큰 코드를 검증·가공·저장·출력 단계로 리팩토링할 수 있다.

---

# 1. 좋은 코드는 의도가 보인다

## 1-1. Before

```python
a = 21
b = True

if a >= 19 and b:
    print("가능")
```

## 1-2. After

```python
user_age = 21
is_active = True

if user_age >= 19 and is_active:
    print("이용 가능")
```

## 1-3. 실행 결과

```text
이용 가능
```

## 1-4. 왜 개선됐을까?

| Before | After |
| --- | --- |
| `a`, `b`의 의미를 알 수 없음 | 값의 역할이 이름에 드러남 |
| `"가능"`의 대상이 불분명 | `"이용 가능"`으로 상황 표현 |
| 코드를 끝까지 읽어야 의미 파악 | 조건식만 보고 의도 파악 가능 |

> [!TIP]
> 변수명은 값의 자료형보다 **업무에서 어떤 의미를 가지는지** 표현한다.
>
> `str_value`, `bool_value`보다 `user_name`, `is_active`가 더 좋다.

---

# 2. 변수명은 명사, 불리언은 질문처럼 작성

일반 값은 명사 형태로 작성한다.

```python
user_name = "Kim"
total_price = 30000
login_count = 3
```

불리언은 참·거짓 질문처럼 읽히게 작성한다.

```python
is_active = True
has_permission = False
can_edit = True
```

## 2-1. Before

```python
active = True

if active:
    print("활성 사용자")
```

## 2-2. After

```python
is_active = True

if is_active:
    print("활성 사용자")
```

## 2-3. 실행 결과

```text
활성 사용자
```

> 💼 **실무에서는 이렇게 생각합니다.**
>
> 조건문 안에서 자연스러운 질문으로 읽히는가?
>
> - `if is_active:` → 활성 상태인가?
> - `if has_permission:` → 권한이 있는가?
> - `if can_edit:` → 수정할 수 있는가?

---

# 3. 함수명은 동작을 표현한다

함수는 무엇을 하는지 동사 형태로 표현한다.

좋은 예:

```python
get_active_users()
calculate_total_price()
validate_email()
save_user()
```

좋지 않은 예:

```python
user()
data()
process()
work()
```

## 3-1. Before

```python
def data(users):
    result = []

    for user in users:
        if user["active"]:
            result.append(user)

    return result
```

## 3-2. After

```python
def get_active_users(users):
    active_users = []

    for user in users:
        if user["active"]:
            active_users.append(user)

    return active_users
```

## 3-3. 실행

```python
active_users = get_active_users(users)

for user in active_users:
    print(user["name"])
```

## 3-4. 실행 결과

```text
Kim
Park
```

## 3-5. 왜 개선됐을까?

- 함수 이름만 보고 반환 결과를 예상할 수 있다.
- `result`보다 `active_users`가 데이터 의미를 드러낸다.
- 호출 코드가 문장처럼 읽힌다.

---

# 4. 인덱스가 필요하지 않으면 직접 순회

## 4-1. Before

```python
for index in range(len(users)):
    print(users[index]["name"])
```

## 4-2. After

```python
for user in users:
    print(user["name"])
```

## 4-3. 실행 결과

```text
Kim
Lee
Park
```

## 4-4. 왜 개선됐을까?

Before는 다음 단계를 거친다.

```text
인덱스 생성
    ↓
리스트에서 인덱스로 사용자 조회
    ↓
사용자 이름 조회
```

After는 필요한 객체를 바로 사용한다.

```text
사용자 객체 직접 순회
    ↓
이름 조회
```

> 💼 **실무에서는 이렇게 생각합니다.**
>
> 인덱스가 필요한가?
>
> - 필요 없음 → `for user in users`
> - 필요함 → `enumerate(users)`
> - 특정 위치를 직접 수정해야 함 → 인덱스 사용 검토

---

# 5. 인덱스가 필요하면 `enumerate()`

## 5-1. Before

```python
for index in range(len(users)):
    user = users[index]

    print(index + 1, user["name"])
```

## 5-2. After

```python
for number, user in enumerate(
    users,
    start=1,
):
    print(number, user["name"])
```

## 5-3. 실행 결과

```text
1 Kim
2 Lee
3 Park
```

## 5-4. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `enumerate(users)` | 인덱스와 값을 함께 얻기 위해 |
| `start=1` | 화면 번호를 1부터 시작하기 위해 |
| `number` | 출력용 순번 |
| `user` | 현재 사용자 객체 |

> [!TIP]
> `range(len())`보다 `enumerate()`는 인덱스와 값의 관계를 명확하게 보여준다.

---

# 6. 두 목록을 함께 처리할 때 `zip()`

## 6-1. Before

```python
names = ["Kim", "Lee", "Park"]
scores = [85, 58, 92]

for index in range(len(names)):
    print(names[index], scores[index])
```

## 6-2. After

```python
names = ["Kim", "Lee", "Park"]
scores = [85, 58, 92]

for name, score in zip(names, scores):
    print(name, score)
```

## 6-3. 실행 결과

```text
Kim 85
Lee 58
Park 92
```

## 6-4. 왜 개선됐을까?

- 인덱스를 직접 관리하지 않는다.
- 이름과 점수의 관계가 반복문에 바로 보인다.
- 인덱스 범위 오류 가능성을 줄인다.

> [!WARNING]
> 기본 `zip()`은 가장 짧은 반복 가능한 객체가 끝나면 함께 종료된다.
>
> 두 목록 길이가 반드시 같아야 한다면 길이 검증 또는 `zip(..., strict=True)` 사용을 검토한다.

```python
for name, score in zip(
    names,
    scores,
    strict=True,
):
    print(name, score)
```

---

# 7. 빈 컬렉션은 Truthy/Falsy로 확인

## 7-1. Before

```python
if len(users) > 0:
    print("사용자가 있습니다.")
```

## 7-2. After

```python
if users:
    print("사용자가 있습니다.")
```

## 7-3. 실행 결과

```text
사용자가 있습니다.
```

빈 경우:

```python
users = []

if not users:
    print("사용자가 없습니다.")
```

출력:

```text
사용자가 없습니다.
```

## 7-4. 왜 개선됐을까?

Python에서는 다음 값이 거짓으로 평가된다.

- 빈 리스트
- 빈 튜플
- 빈 딕셔너리
- 빈 집합
- 빈 문자열
- 숫자 `0`
- `None`
- `False`

> 💼 **실무에서는 이렇게 생각합니다.**
>
> 컬렉션이 비어 있는지만 확인하는가?
>
> - 예 → `if not items:`
> - 길이 자체가 필요한가? → `len(items)`
> - 정확히 `None`인지 확인하는가? → `is None`

---

# 8. `None`은 `is`로 비교

## 8-1. Before

```python
if user == None:
    print("사용자 없음")
```

## 8-2. After

```python
if user is None:
    print("사용자 없음")
```

## 8-3. 왜 개선됐을까?

`None`은 하나의 특별한 객체다.

값 동등성 비교 `==`보다 동일한 객체인지 확인하는 `is`를 사용한다.

권장:

```python
if user is None:
    ...
```

```python
if user is not None:
    ...
```

---

# 9. 딕셔너리 키가 없을 수 있으면 `get()`

## 9-1. Before

```python
user = {
    "name": "Kim",
}

print(user["email"])
```

발생 결과:

```text
KeyError
```

## 9-2. After

```python
user = {
    "name": "Kim",
}

print(user.get("email"))
```

출력:

```text
None
```

기본값 지정:

```python
email = user.get(
    "email",
    "이메일 없음",
)

print(email)
```

출력:

```text
이메일 없음
```

## 9-3. 언제 직접 접근해야 할까?

키가 반드시 존재해야 하는 데이터라면 직접 접근이 더 적절할 수 있다.

```python
user_id = user["id"]
```

키가 없다는 것은 데이터 구조 오류이므로 `KeyError`가 발생하는 편이 문제 발견에 도움이 될 수 있다.

> 💼 **실무에서는 이렇게 생각합니다.**
>
> 이 키는 반드시 존재해야 하는가?
>
> - 반드시 존재 → `user["id"]`
> - 선택값 → `user.get("nickname")`
> - 없으면 기본값 → `user.get("nickname", "익명")`

---

# 10. 딕셔너리는 `items()`로 순회

## 10-1. Before

```python
user = {
    "name": "Kim",
    "age": 21,
}

for key in user:
    print(key, user[key])
```

## 10-2. After

```python
for key, value in user.items():
    print(key, value)
```

## 10-3. 실행 결과

```text
name Kim
age 21
```

## 10-4. 선택 기준

```text
키만 필요
→ for key in user

값만 필요
→ for value in user.values()

키와 값 모두 필요
→ for key, value in user.items()
```

---

# 11. 하나라도 만족하는지 확인할 때 `any()`

활성 사용자가 한 명이라도 있는지 확인한다.

## 11-1. Before

```python
has_active_user = False

for user in users:
    if user["active"]:
        has_active_user = True
        break

print(has_active_user)
```

## 11-2. After

```python
has_active_user = any(
    user["active"]
    for user in users
)

print(has_active_user)
```

## 11-3. 실행 결과

```text
True
```

## 11-4. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `user["active"]` | 각 사용자의 활성 상태 확인 |
| 제너레이터 표현식 | 값을 하나씩 전달 |
| `any()` | 하나라도 참이면 `True` 반환 |

> [!TIP]
> `any()`는 참인 값을 찾으면 나머지 항목을 확인하지 않고 종료할 수 있다.

---

# 12. 모두 만족하는지 확인할 때 `all()`

모든 사용자가 이메일을 가지고 있는지 확인한다.

## 12-1. Before

```python
all_have_email = True

for user in users:
    if not user.get("email"):
        all_have_email = False
        break

print(all_have_email)
```

## 12-2. After

```python
all_have_email = all(
    user.get("email")
    for user in users
)

print(all_have_email)
```

## 12-3. 실행 결과

```text
True
```

## 12-4. 선택 기준

```text
하나라도 조건 만족
→ any()

모두 조건 만족
→ all()
```

---

# 13. 단순한 변환은 리스트 컴프리헨션

## 13-1. Before

```python
user_names = []

for user in users:
    user_names.append(user["name"])

print(user_names)
```

## 13-2. After

```python
user_names = [
    user["name"]
    for user in users
]

print(user_names)
```

## 13-3. 실행 결과

```text
['Kim', 'Lee', 'Park']
```

## 13-4. 왜 개선됐을까?

- 새 리스트를 만든다는 목적이 바로 보인다.
- 단순 반복과 `append()`를 줄인다.
- 값 변환 흐름이 한곳에 모인다.

> [!IMPORTANT]
> 컴프리헨션은 단순한 변환과 필터링에 적합하다.
>
> 여러 조건과 복잡한 처리, 예외 처리가 섞이면 일반 반복문이 더 읽기 쉽다.

---

# 14. 단순한 필터링도 컴프리헨션

## 14-1. Before

```python
adult_users = []

for user in users:
    if user["age"] >= 19:
        adult_users.append(user)

print(adult_users)
```

## 14-2. After

```python
adult_users = [
    user
    for user in users
    if user["age"] >= 19
]

for user in adult_users:
    print(user["name"])
```

## 14-3. 실행 결과

```text
Kim
Park
```

---

# 15. 복잡한 컴프리헨션은 피한다

## 15-1. 읽기 어려운 코드

```python
result = [
    user["name"].upper()
    if user["active"]
    else user["name"].lower()
    for user in users
    if user["score"] >= 60
]
```

실행할 수 있지만 조건이 여러 개 섞여 있다.

## 15-2. 개선

```python
result = []

for user in users:
    if user["score"] < 60:
        continue

    name = user["name"]

    if user["active"]:
        result.append(name.upper())
    else:
        result.append(name.lower())
```

## 15-3. 실행 결과

```text
['KIM', 'PARK']
```

> 💼 **실무에서는 이렇게 생각합니다.**
>
> 한 번 읽고 바로 이해할 수 있는가?
>
> - 단순 변환·필터 → 컴프리헨션
> - 조건이 여러 단계 → 일반 반복문
> - 예외 처리나 로그 필요 → 함수 또는 반복문

---

# 16. 중첩 조건은 Guard Clause로 줄인다

## 16-1. Before

```python
def print_user(user):
    if user is not None:
        if user.get("active"):
            if user.get("age", 0) >= 19:
                print(user["name"])
```

## 16-2. After

```python
def print_adult_active_user(user):
    if user is None:
        return

    if not user.get("active"):
        return

    if user.get("age", 0) < 19:
        return

    print(user["name"])
```

## 16-3. 실행

```python
for user in users:
    print_adult_active_user(user)
```

## 16-4. 실행 결과

```text
Kim
Park
```

## 16-5. 왜 개선됐을까?

Before:

```text
정상 흐름이 깊은 중첩 안에 있음
```

After:

```text
처리하지 않을 조건을 먼저 반환
    ↓
정상 흐름이 마지막에 평평하게 위치
```

> [!TIP]
> Guard Clause는 잘못된 입력이나 처리하지 않을 조건을 함수 앞부분에서 빠르게 종료하는 방식이다.

---

# 17. 비교식을 간단하게 작성

## 17-1. Before

```python
if user["active"] == True:
    print(user["name"])
```

## 17-2. After

```python
if user["active"]:
    print(user["name"])
```

거짓 확인:

```python
if not user["active"]:
    print("비활성 사용자")
```

## 17-3. 주의점

값이 반드시 불리언인지 확인해야 하는 상황에서는 명시적 비교가 의미를 가질 수 있다.

```python
if response.get("success") is True:
    ...
```

일반적인 불리언 조건에서는 직접 사용한다.

---

# 18. 여러 값 포함 검사는 `in`

## 18-1. Before

```python
role = "admin"

if (
    role == "admin"
    or role == "manager"
    or role == "operator"
):
    print("관리 기능 사용 가능")
```

## 18-2. After

```python
allowed_roles = {
    "admin",
    "manager",
    "operator",
}

if role in allowed_roles:
    print("관리 기능 사용 가능")
```

## 18-3. 실행 결과

```text
관리 기능 사용 가능
```

## 18-4. 왜 집합을 사용할까?

- 값의 포함 여부가 목적임을 표현한다.
- 중복을 허용하지 않는다.
- 많은 값의 포함 검사에서 효율적이다.

---

# 19. 매직 넘버를 상수로 분리

## 19-1. Before

```python
if user["age"] >= 19:
    print("성인")
```

코드가 여러 곳에 있다면 `19`의 의미와 정책 변경 범위를 찾기 어렵다.

## 19-2. After

```python
ADULT_AGE = 19

if user["age"] >= ADULT_AGE:
    print("성인")
```

## 19-3. 실행 결과

```text
성인
```

## 19-4. 상수 이름

상수는 일반적으로 대문자와 밑줄을 사용한다.

```python
ADULT_AGE = 19
PASS_SCORE = 60
MAX_LOGIN_ATTEMPTS = 5
```

> [!IMPORTANT]
> 상수는 Python 문법상 변경이 금지되는 값은 아니다.
>
> 대문자 이름은 “이 값을 변경하지 않고 공통 기준으로 사용한다”는 개발자 간 약속이다.

---

# 20. 매직 문자열도 상수로 분리

## 20-1. Before

```python
if user_role == "admin":
    ...
```

여러 파일에서 `"admin"`을 반복하면 오타와 정책 변경 위험이 생긴다.

## 20-2. After

```python
ROLE_ADMIN = "admin"

if user_role == ROLE_ADMIN:
    ...
```

값 종류가 많다면 `Enum`도 고려할 수 있다.

```python
from enum import Enum


class UserRole(str, Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    USER = "user"
```

---

# 21. 정렬은 `sorted()`와 `key`

점수 높은 순으로 사용자를 정렬한다.

## 21-1. Before

```python
for index in range(len(users)):
    for next_index in range(
        index + 1,
        len(users),
    ):
        if (
            users[index]["score"]
            < users[next_index]["score"]
        ):
            users[index], users[next_index] = (
                users[next_index],
                users[index],
            )
```

직접 정렬 알고리즘을 작성할 수 있지만 실무에서는 목적에 맞는 내장 기능을 우선 사용한다.

## 21-2. After

```python
sorted_users = sorted(
    users,
    key=lambda user: user["score"],
    reverse=True,
)
```

## 21-3. 실행

```python
for user in sorted_users:
    print(
        user["name"],
        user["score"],
    )
```

## 21-4. 실행 결과

```text
Park 92
Kim 85
Lee 58
```

## 21-5. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `sorted()` | 원본을 유지하며 새 정렬 리스트 생성 |
| `key` | 정렬 기준 지정 |
| `lambda user: user["score"]` | 사용자 점수를 기준값으로 반환 |
| `reverse=True` | 내림차순 정렬 |

---

# 22. `lambda`는 짧은 기준 함수에만 사용

## 22-1. 적절한 사용

```python
sorted_users = sorted(
    users,
    key=lambda user: user["age"],
)
```

## 22-2. 복잡한 `lambda`

```python
key=lambda user: (
    0
    if user["active"] and user["score"] >= 60
    else 1
)
```

조건이 복잡하면 이름 있는 함수가 더 읽기 쉽다.

```python
def get_user_priority(user):
    if user["active"] and user["score"] >= 60:
        return 0

    return 1
```

```python
sorted_users = sorted(
    users,
    key=get_user_priority,
)
```

> 💼 **실무에서는 이렇게 생각합니다.**
>
> 한 줄의 단순 계산인가?
>
> - 예 → `lambda` 가능
> - 조건이나 설명이 필요한가? → 이름 있는 함수

---

# 23. 원본을 유지할지 직접 변경할지 구분

```python
numbers = [3, 1, 2]
```

새 리스트 반환:

```python
sorted_numbers = sorted(numbers)
```

원본 직접 변경:

```python
numbers.sort()
```

## 23-1. 비교

| 방식 | 결과 |
| --- | --- |
| `sorted(numbers)` | 새 리스트 반환 |
| `numbers.sort()` | 원본 리스트 변경, 반환값 `None` |

## 23-2. 실무 선택 기준

- 원본을 유지해야 함 → `sorted()`
- 현재 리스트를 이후에도 정렬 상태로 사용 → `.sort()`
- 함수 내부 부작용을 줄이고 싶음 → 새 값 반환 우선 검토

---

# 24. 함수는 하나의 주요 책임만 담당

## 24-1. Before

```python
def process_users(users):
    valid_users = []

    for user in users:
        if (
            user.get("name")
            and user.get("email")
        ):
            valid_users.append(user)

    adult_users = []

    for user in valid_users:
        if user["age"] >= 19:
            adult_users.append(user)

    adult_users.sort(
        key=lambda user: user["score"],
        reverse=True,
    )

    for user in adult_users:
        print(
            user["name"],
            user["score"],
        )
```

한 함수가 검증·필터링·정렬·출력을 모두 담당한다.

## 24-2. After

```python
ADULT_AGE = 19


def is_valid_user(user):
    return bool(
        user.get("name")
        and user.get("email")
    )


def get_adult_users(users):
    return [
        user
        for user in users
        if user["age"] >= ADULT_AGE
    ]


def sort_users_by_score(users):
    return sorted(
        users,
        key=lambda user: user["score"],
        reverse=True,
    )


def print_user_scores(users):
    for user in users:
        print(
            user["name"],
            user["score"],
        )
```

조합:

```python
valid_users = [
    user
    for user in users
    if is_valid_user(user)
]

adult_users = get_adult_users(
    valid_users
)

sorted_users = sort_users_by_score(
    adult_users
)

print_user_scores(sorted_users)
```

## 24-3. 실행 결과

```text
Park 92
Kim 85
```

## 24-4. 개선된 점

- 각 함수의 입력과 결과가 명확하다.
- 개별 함수 테스트가 쉽다.
- 출력 방식을 바꿔도 필터 로직에 영향이 적다.
- 정렬 기준을 수정할 위치가 분명하다.

---

# 25. 함수 분리는 줄 수가 아니라 책임 기준

함수가 길다고 무조건 나누는 것은 아니다.

다음 질문을 확인한다.

```text
이 함수가 두 가지 이상의 목적을 가지는가?
    ↓
일부 로직에 이름을 붙이면 이해가 쉬워지는가?
    ↓
별도로 테스트할 가치가 있는가?
    ↓
다른 곳에서 재사용할 수 있는가?
    ↓
변경 이유가 서로 다른 코드가 섞여 있는가?
```

> [!IMPORTANT]
> 함수 분리의 기준은 “몇 줄인가?”보다 **“몇 가지 이유로 변경되는가?”**에 가깝다.

---

# 26. 반환값은 일관되게 유지

## 26-1. Before

```python
def find_user(users, user_id):
    for user in users:
        if user["id"] == user_id:
            return user

    return False
```

성공 시 딕셔너리, 실패 시 불리언을 반환한다.

## 26-2. After

```python
def find_user(users, user_id):
    for user in users:
        if user["id"] == user_id:
            return user

    return None
```

## 26-3. 실행

```python
user = find_user(
    users,
    user_id=2,
)

if user is None:
    print("사용자를 찾을 수 없습니다.")
else:
    print(user["name"])
```

## 26-4. 실행 결과

```text
Lee
```

## 26-5. 왜 `None`일까?

“결과 없음”을 표현하는 일반적인 값으로 이해하기 쉽다.

타입 힌트에서도 명확하게 표현할 수 있다.

```python
dict | None
```

---

# 27. 가변 기본 인자를 사용하지 않는다

## 27-1. Before

```python
def add_user(
    user,
    user_list=[],
):
    user_list.append(user)
    return user_list
```

호출:

```python
print(add_user("Kim"))
print(add_user("Lee"))
```

출력:

```text
['Kim']
['Kim', 'Lee']
```

기본 리스트가 함수 정의 시 한 번 생성되어 호출 간 공유된다.

## 27-2. After

```python
def add_user(
    user,
    user_list=None,
):
    if user_list is None:
        user_list = []

    user_list.append(user)

    return user_list
```

## 27-3. 실행 결과

```text
['Kim']
['Lee']
```

> [!WARNING]
> 리스트·딕셔너리·집합 같은 변경 가능한 객체를 기본 인자로 직접 사용하지 않는다.

---

# 28. 입력 데이터를 함수 안에서 무조건 변경하지 않는다

## 28-1. Before

```python
def deactivate_users(users):
    for user in users:
        user["active"] = False
```

호출한 쪽의 원본 데이터가 직접 변경된다.

## 28-2. 원본 변경을 명확히 표현

원본 변경이 목적이라면 함수명에 드러낸다.

```python
def deactivate_users_in_place(users):
    for user in users:
        user["active"] = False
```

## 28-3. 새 데이터 반환

원본 유지가 필요하다면 새 딕셔너리를 만든다.

```python
def get_deactivated_users(users):
    return [
        {
            **user,
            "active": False,
        }
        for user in users
    ]
```

> 💼 **실무에서는 이렇게 생각합니다.**
>
> 이 함수가 원본을 변경해도 되는가?
>
> - 변경 의도가 분명함 → 함수명·문서에 표시
> - 원본 보존 필요 → 새 객체 반환
> - 판단이 어려움 → 부작용을 줄이는 방향 우선

---

# 29. 언패킹으로 새 딕셔너리 만들기

## 29-1. Before

```python
updated_user = user.copy()
updated_user["active"] = False
```

## 29-2. After

```python
updated_user = {
    **user,
    "active": False,
}
```

## 29-3. 실행 결과

```python
user = {
    "id": 1,
    "name": "Kim",
    "active": True,
}

updated_user = {
    **user,
    "active": False,
}

print(user["active"])
print(updated_user["active"])
```

```text
True
False
```

원본과 새 객체가 분리된다.

---

# 30. 반복되는 문자열 조합은 함수로 분리

## 30-1. Before

```python
for user in users:
    print(
        user["name"]
        + " / "
        + str(user["age"])
        + "세 / "
        + str(user["score"])
        + "점"
    )
```

## 30-2. After

```python
def format_user_summary(user):
    return (
        f'{user["name"]} / '
        f'{user["age"]}세 / '
        f'{user["score"]}점'
    )
```

```python
for user in users:
    print(format_user_summary(user))
```

## 30-3. 실행 결과

```text
Kim / 21세 / 85점
Lee / 17세 / 58점
Park / 28세 / 92점
```

## 30-4. 개선된 점

- 문자열 형식을 한곳에서 관리한다.
- f-string으로 값의 위치가 명확하다.
- 출력 외에도 파일 저장, 응답 생성에 재사용할 수 있다.

---

# 31. f-string을 사용해 의도를 명확하게 표현

## 31-1. Before

```python
message = (
    user["name"]
    + "님의 점수는 "
    + str(user["score"])
    + "점입니다."
)
```

## 31-2. After

```python
message = (
    f'{user["name"]}님의 점수는 '
    f'{user["score"]}점입니다.'
)
```

## 31-3. 결과

```text
Kim님의 점수는 85점입니다.
```

숫자 형식 지정:

```python
price = 1200000

print(f"{price:,}원")
```

출력:

```text
1,200,000원
```

---

# 32. 타입 힌트로 입력과 결과를 표현

## 32-1. 타입 힌트 없는 함수

```python
def get_adult_names(people):
    return [
        person["name"]
        for person in people
        if person["age"] >= 19
    ]
```

## 32-2. 타입 힌트 적용

```python
def get_adult_names(
    people: list[dict[str, object]],
) -> list[str]:
    return [
        str(person["name"])
        for person in people
        if int(person["age"]) >= 19
    ]
```

## 32-3. 입력

```python
people = [
    {
        "name": "Kim",
        "age": 21,
    },
    {
        "name": "Lee",
        "age": 17,
    },
]
```

## 32-4. 실행

```python
adult_names = get_adult_names(
    people
)

print(adult_names)
```

## 32-5. 실행 결과

```text
['Kim']
```

## 32-6. 타입 힌트의 역할

- 입력 자료형의 의도를 보여준다.
- 반환 결과를 예상할 수 있다.
- 에디터 자동 완성과 검사에 도움을 준다.
- 문서 역할을 한다.

> [!IMPORTANT]
> 타입 힌트는 기본적으로 실행 시 자료형을 강제하지 않는다.
>
> 정적 분석 도구와 개발자가 코드를 이해하도록 돕는 정보다.

---

# 33. 복잡한 딕셔너리 타입은 `TypedDict`

`dict[str, object]`는 각 키의 의미와 자료형이 충분히 드러나지 않는다.

```python
from typing import TypedDict


class UserData(TypedDict):
    id: int
    name: str
    age: int
    active: bool
    email: str
    score: int
```

함수:

```python
def get_active_users(
    users: list[UserData],
) -> list[UserData]:
    return [
        user
        for user in users
        if user["active"]
    ]
```

> [!TIP]
> 딕셔너리 구조가 고정되어 있고 여러 함수에서 반복 사용된다면 `TypedDict`로 키와 자료형을 명확히 표현할 수 있다.

---

# 34. Docstring은 함수의 계약을 설명

## 34-1. 코드만 있는 함수

```python
def get_active_users(users):
    return [
        user
        for user in users
        if user["active"]
    ]
```

## 34-2. Docstring 추가

```python
def get_active_users(
    users: list[UserData],
) -> list[UserData]:
    """활성 상태인 사용자만 반환한다."""
    return [
        user
        for user in users
        if user["active"]
    ]
```

## 34-3. 언제 자세히 작성할까?

- 입력 규칙이 복잡함
- 예외가 발생함
- 반환값 의미가 단순하지 않음
- 외부 개발자가 사용하는 공개 함수
- 부작용이 있음

> [!WARNING]
> 코드만 읽어도 알 수 있는 내용을 길게 반복하는 Docstring은 오히려 관리 비용이 된다.

---

# 35. 주석은 이유를 설명

## 35-1. 좋지 않은 주석

```python
# 나이를 확인한다.
if user["age"] >= 19:
    ...
```

코드가 이미 같은 내용을 보여준다.

## 35-2. 의미 있는 주석

```python
# 서비스 정책상 국내 성인 기준을 19세로 적용한다.
if user["age"] >= ADULT_AGE:
    ...
```

주석은 다음 내용을 설명하는 데 적합하다.

- 왜 이 방식이 필요한가?
- 외부 정책이나 제한은 무엇인가?
- 직관적이지 않은 예외 상황은 무엇인가?
- 임시 해결책이 필요한 이유는 무엇인가?

---

# 36. 예외는 구체적으로 처리

## 36-1. Before

```python
try:
    age = int(user_input)
except:
    print("오류")
```

## 36-2. After

```python
try:
    age = int(user_input)
except ValueError:
    print("나이는 숫자로 입력해주세요.")
```

## 36-3. 개선된 점

- 어떤 오류를 처리하는지 명확하다.
- 다른 예상하지 못한 오류를 숨기지 않는다.
- 사용자 안내가 구체적이다.

---

# 37. 예외 대신 조건 검사가 더 자연스러운 경우

## 37-1. 과도한 예외 사용

```python
try:
    first_user = users[0]
except IndexError:
    first_user = None
```

## 37-2. 조건 확인

```python
first_user = (
    users[0]
    if users
    else None
)
```

또는 흐름을 더 명확히 작성한다.

```python
if not users:
    print("사용자가 없습니다.")
else:
    first_user = users[0]
```

> 💼 **실무에서는 이렇게 생각합니다.**
>
> 예외적인 상황인가?
>
> - 일반적으로 충분히 예상되는 분기 → 조건문
> - 작업 도중 실패하는 비정상 상황 → 예외 처리

---

# 38. 오류를 숨기지 않는다

## 38-1. Before

```python
try:
    save_user(user)
except Exception:
    pass
```

문제가 발생해도 아무 정보가 없다.

## 38-2. After

```python
try:
    save_user(user)
except ValueError as error:
    print(
        "사용자 저장 실패:",
        error,
    )
    raise
```

현재 위치에서 로그를 남기고 해결할 수 없다면 다시 예외를 전달한다.

> [!WARNING]
> `except Exception: pass`는 실제 버그와 데이터 손상을 숨길 수 있다.

---

# 39. 파일 경로는 `pathlib.Path`

## 39-1. Before

```python
file_path = (
    "data"
    + "/"
    + "users"
    + "/"
    + "users.json"
)
```

## 39-2. After

```python
from pathlib import Path


file_path = (
    Path("data")
    / "users"
    / "users.json"
)
```

## 39-3. 실행

```python
print(file_path)
print(file_path.name)
print(file_path.suffix)
```

## 39-4. 출력 형태

```text
data/users/users.json
users.json
.json
```

## 39-5. 왜 사용할까?

- 운영체제 경로 차이를 줄인다.
- `/` 연산자로 경로를 자연스럽게 조합한다.
- 파일명, 확장자, 부모 경로 기능을 제공한다.
- 파일 존재 여부와 폴더 생성도 처리할 수 있다.

```python
file_path.parent.mkdir(
    parents=True,
    exist_ok=True,
)
```

---

# 40. 파일은 `with`문으로 연다

## 40-1. Before

```python
file = open(
    "users.txt",
    "r",
    encoding="utf-8",
)

content = file.read()

file.close()
```

## 40-2. After

```python
with open(
    "users.txt",
    "r",
    encoding="utf-8",
) as file:
    content = file.read()
```

블록이 끝나면 파일이 자동으로 닫힌다.

> [!IMPORTANT]
> 파일 작업은 예외가 발생할 수 있으므로 자원 정리가 보장되는 `with`문을 우선 사용한다.

---

# 41. import 순서는 역할별로 구분

일반적인 순서:

```python
import json
from pathlib import Path

import requests

from app.models import User
from app.services import user_service
```

```text
표준 라이브러리
    ↓
서드파티 라이브러리
    ↓
프로젝트 내부 모듈
```

각 그룹 사이에 빈 줄을 둔다.

> [!TIP]
> import 순서는 자동 정렬 도구를 사용할 수도 있지만, 기본 구조를 이해해야 충돌과 순환 import를 줄일 수 있다.

---

# 42. 클래스가 필요한지 먼저 판단

데이터를 한 번 변환하는 단순 기능은 함수로 충분할 수 있다.

```python
def format_user_name(user):
    return user["name"].upper()
```

상태와 관련 동작이 함께 유지되어야 한다면 클래스를 고려한다.

```python
class User:
    def __init__(
        self,
        name,
        age,
    ):
        self.name = name
        self.age = age

    def is_adult(self):
        return self.age >= 19
```

## 42-1. 선택 기준

```text
입력 → 결과만 필요한가?
→ 함수

여러 값이 하나의 상태를 이루는가?
→ 클래스 검토

상태와 관련 동작이 함께 유지되는가?
→ 클래스

단순히 함수를 묶고 싶은가?
→ 모듈도 검토
```

---

# 43. 클래스는 유효한 상태를 유지

## 43-1. Before

```python
class User:
    def __init__(
        self,
        name,
        age,
    ):
        self.name = name
        self.age = age
```

빈 이름과 음수 나이도 저장할 수 있다.

## 43-2. After

```python
class User:
    def __init__(
        self,
        name: str,
        age: int,
    ) -> None:
        name = name.strip()

        if not name:
            raise ValueError(
                "이름을 입력해야 합니다."
            )

        if age < 0:
            raise ValueError(
                "나이는 음수일 수 없습니다."
            )

        self.name = name
        self.age = age

    def is_adult(self) -> bool:
        return self.age >= ADULT_AGE
```

## 43-3. 실행

```python
user = User(
    "Kim",
    21,
)

print(user.name)
print(user.is_adult())
```

## 43-4. 실행 결과

```text
Kim
True
```

> [!IMPORTANT]
> 객체는 생성 직후부터 유효한 상태여야 한다.
>
> 잘못된 값을 저장한 뒤 나중에 수정하는 것보다 생성 시점에 차단하는 편이 안전하다.

---

# 44. Getter·Setter를 기계적으로 만들지 않는다

## 44-1. 과도한 코드

```python
class User:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
```

검증이나 계산이 없다면 공개 속성도 자연스럽다.

```python
class User:
    def __init__(self, name):
        self.name = name
```

값 변경 시 검증이 필요하면 `property`를 검토한다.

```python
class User:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        value = value.strip()

        if not value:
            raise ValueError(
                "이름을 입력해야 합니다."
            )

        self._name = value
```

---

# 45. 클래스 메서드 선택 기준

```text
현재 객체의 상태 사용
→ 인스턴스 메서드

클래스 공통 상태 사용
→ @classmethod

객체·클래스 상태 사용 안 함
→ @staticmethod 또는 일반 함수
```

예:

```python
class User:
    count = 0

    def __init__(self, name):
        self.name = name
        type(self).count += 1

    def get_display_name(self):
        return self.name.upper()

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def is_valid_name(name):
        return bool(name.strip())
```

> 💼 **실무에서는 이렇게 생각합니다.**
>
> 이 기능이 반드시 클래스 안에 있어야 하는가?
>
> 클래스 역할과 관련이 약한 정적 메서드는 일반 함수가 더 자연스러울 수 있다.

---

# 46. 데이터 저장 중심 클래스는 `dataclass`

## 46-1. 일반 클래스

```python
class User:
    def __init__(
        self,
        user_id,
        name,
        age,
    ):
        self.user_id = user_id
        self.name = name
        self.age = age
```

## 46-2. `dataclass`

```python
from dataclasses import dataclass


@dataclass
class User:
    user_id: int
    name: str
    age: int
```

## 46-3. 실행

```python
user = User(
    user_id=1,
    name="Kim",
    age=21,
)

print(user)
```

## 46-4. 출력 결과

```text
User(user_id=1, name='Kim', age=21)
```

데이터 저장이 중심이고 특별한 초기화 로직이 적다면 `dataclass`가 코드를 줄일 수 있다.

---

# 47. 같은 의미의 중복 로직을 함수로 모은다

## 47-1. Before

```python
if (
    user["name"] != ""
    and user["email"] != ""
):
    print("저장 가능")
```

다른 위치:

```python
if (
    user["name"] != ""
    and user["email"] != ""
):
    save_user(user)
```

## 47-2. After

```python
def is_valid_user(user):
    return bool(
        user.get("name")
        and user.get("email")
    )
```

```python
if is_valid_user(user):
    print("저장 가능")
```

```python
if is_valid_user(user):
    save_user(user)
```

검증 규칙이 바뀌면 함수 한곳만 수정한다.

---

# 48. 데이터 가공과 출력 로직을 분리

## 48-1. Before

```python
def print_active_user_names(users):
    for user in users:
        if user["active"]:
            print(
                user["name"].upper()
            )
```

함수가 필터링·변환·출력을 모두 담당한다.

## 48-2. After

```python
def get_active_user_names(users):
    return [
        user["name"].upper()
        for user in users
        if user["active"]
    ]
```

```python
active_names = get_active_user_names(
    users
)

for name in active_names:
    print(name)
```

## 48-3. 실행 결과

```text
KIM
PARK
```

가공 결과를 화면뿐 아니라 파일, API 응답, 테스트에도 사용할 수 있다.

---

# 49. 로그와 사용자 메시지를 구분

사용자에게는 이해하기 쉬운 메시지를 보여준다.

```python
print(
    "사용자 정보를 저장하지 못했습니다."
)
```

개발자 로그에는 원인과 위치를 기록한다.

```python
import logging


logger = logging.getLogger(__name__)

try:
    save_user(user)
except ValueError as error:
    logger.exception(
        "사용자 저장 실패: %s",
        user.get("id"),
    )
    print(
        "입력값을 확인해주세요."
    )
```

> [!TIP]
> `print()`는 학습과 간단한 확인에 적합하지만, 실무 애플리케이션의 상태 기록은 `logging`을 사용한다.

---

# 50. PEP 8 핵심 규칙

Python의 대표적인 스타일 가이드가 PEP 8이다.

핵심 규칙:

- 들여쓰기 4칸
- 클래스 이름은 PascalCase
- 함수·변수는 snake_case
- 상수는 UPPER_SNAKE_CASE
- 연산자 주변 공백
- 관련 없는 코드는 빈 줄로 구분
- 너무 긴 줄은 여러 줄로 분리
- import는 파일 상단에서 그룹별 정리
- 한 줄에 여러 문장을 작성하지 않음

## 50-1. Before

```python
def add(a,b):return a+b
```

## 50-2. After

```python
def add(a, b):
    return a + b
```

> [!IMPORTANT]
> 스타일 가이드는 코드를 꾸미기 위한 규칙이 아니라, 여러 개발자가 같은 방식으로 읽고 수정하기 위한 공통 약속이다.

---

# 51. 자동화 도구를 활용한다

실무에서는 스타일을 사람의 기억에만 의존하지 않는다.

대표 도구의 역할:

| 종류 | 역할 |
| --- | --- |
| Formatter | 코드 형식을 자동 정리 |
| Linter | 잠재 오류와 스타일 문제 검사 |
| Type Checker | 타입 힌트 기반 오류 검사 |
| Test Runner | 자동 테스트 실행 |

도구 이름은 프로젝트 환경에 따라 달라질 수 있다.

중요한 기준:

```text
팀 규칙을 정함
    ↓
도구 설정을 저장
    ↓
모든 개발자가 같은 설정 사용
    ↓
코드 리뷰에서 형식 논쟁 감소
```

---

# 52. 실무 리팩토링 예제: 사용자 보고서

## 52-1. 요구사항

사용자 목록에서 다음 작업을 수행한다.

1. 이름과 이메일이 있는 사용자만 사용
2. 성인 사용자만 선택
3. 점수 높은 순으로 정렬
4. 활성 사용자의 이름과 점수를 출력
5. 합격 기준은 60점

---

## 52-2. Before

```python
def report(users):
    result = []

    for user in users:
        if (
            "name" in user
            and "email" in user
        ):
            if user["age"] >= 19:
                if user["active"] == True:
                    if user["score"] >= 60:
                        result.append(user)

    result.sort(
        key=lambda user: user["score"],
        reverse=True,
    )

    for index in range(len(result)):
        print(
            str(index + 1)
            + ". "
            + result[index]["name"]
            + " - "
            + str(result[index]["score"])
        )
```

코드는 실행되지만 하나의 함수에 모든 책임이 모여 있고 중첩이 깊다.

---

## 52-3. After

```python
ADULT_AGE = 19
PASS_SCORE = 60


def is_complete_user(user):
    return bool(
        user.get("name")
        and user.get("email")
    )


def is_report_target(user):
    return (
        user["age"] >= ADULT_AGE
        and user["active"]
        and user["score"] >= PASS_SCORE
    )


def get_report_users(users):
    report_users = [
        user
        for user in users
        if (
            is_complete_user(user)
            and is_report_target(user)
        )
    ]

    return sorted(
        report_users,
        key=lambda user: user["score"],
        reverse=True,
    )


def format_report_line(
    number,
    user,
):
    return (
        f'{number}. '
        f'{user["name"]} - '
        f'{user["score"]}점'
    )


def print_user_report(users):
    report_users = get_report_users(
        users
    )

    for number, user in enumerate(
        report_users,
        start=1,
    ):
        print(
            format_report_line(
                number,
                user,
            )
        )
```

## 52-4. 실행

```python
print_user_report(users)
```

## 52-5. 실행 결과

```text
1. Park - 92점
2. Kim - 85점
```

## 52-6. 개선 과정

```text
매직 넘버
→ ADULT_AGE, PASS_SCORE 상수

중첩 조건
→ 의미 있는 검증 함수

한 함수의 여러 책임
→ 검증·선택·정렬·형식·출력 분리

range(len())
→ enumerate()

문자열 +
→ f-string
```

---

# 53. 실무 리팩토링 예제: 회원 등록

## 53-1. Before

```python
def join(user_data):
    if user_data["name"] == "":
        print("이름 없음")
        return

    if user_data["email"] == "":
        print("이메일 없음")
        return

    if "@" not in user_data["email"]:
        print("이메일 오류")
        return

    user_data["name"] = (
        user_data["name"]
        .strip()
    )

    user_data["active"] = True

    print("저장:", user_data)
    print("가입 완료")
```

## 53-2. After

```python
def normalize_name(name):
    normalized_name = name.strip()

    if not normalized_name:
        raise ValueError(
            "이름을 입력해야 합니다."
        )

    return normalized_name


def validate_email(email):
    email = email.strip()

    if not email:
        raise ValueError(
            "이메일을 입력해야 합니다."
        )

    if "@" not in email:
        raise ValueError(
            "이메일 형식이 올바르지 않습니다."
        )

    return email


def create_user(user_data):
    return {
        **user_data,
        "name": normalize_name(
            user_data.get("name", "")
        ),
        "email": validate_email(
            user_data.get("email", "")
        ),
        "active": True,
    }


def register_user(user_data):
    try:
        user = create_user(user_data)
    except ValueError as error:
        print("가입 실패:", error)
        return None

    print("저장:", user)
    print("가입 완료")

    return user
```

## 53-3. 실행

```python
new_user = register_user(
    {
        "id": 4,
        "name": "  Choi  ",
        "email": "choi@example.com",
        "age": 24,
        "score": 0,
    }
)
```

## 53-4. 출력 결과

```text
저장: {'id': 4, 'name': 'Choi', 'email': 'choi@example.com', 'age': 24, 'score': 0, 'active': True}
가입 완료
```

## 53-5. 개선된 점

- 이름 정리와 이메일 검증을 각각 분리했다.
- 오류를 출력 코드가 아니라 예외로 전달한다.
- 원본 딕셔너리를 직접 변경하지 않는다.
- 등록 결과를 반환해 이후 로직에서 사용할 수 있다.

---

# 54. 실무에서는 이렇게 선택한다

## 54-1. 반복문 선택

```text
값만 필요
→ for item in items

번호와 값 필요
→ enumerate(items)

두 목록 함께 순회
→ zip(items_a, items_b)

하나라도 참인지 확인
→ any()

모두 참인지 확인
→ all()
```

## 54-2. 컬렉션 선택

```text
순서와 중복 필요
→ list

변경하지 않는 순서 데이터
→ tuple

키로 값 조회
→ dict

중복 제거·포함 검사
→ set
```

## 54-3. 결과 생성 방식

```text
작은 결과를 여러 번 사용
→ list

한 번 순회하는 큰 데이터
→ generator

키와 값 구조
→ dict

고정 데이터 객체
→ dataclass 검토
```

## 54-4. 코드 구조 선택

```text
단순 입력 → 결과
→ 함수

상태와 동작이 함께 유지
→ 클래스

관련 함수 모음
→ 모듈

프로그램 고유 오류
→ 사용자 정의 예외 검토
```

---

# 55. 초보자 코드 → 실무형 코드 빠른 비교

## 55-1. 빈 리스트 확인

```python
# Before
if len(users) == 0:
    ...
```

```python
# After
if not users:
    ...
```

## 55-2. 리스트 순회

```python
# Before
for index in range(len(users)):
    user = users[index]
```

```python
# After
for user in users:
    ...
```

## 55-3. 순번 포함

```python
# Before
for index in range(len(users)):
    print(index + 1, users[index])
```

```python
# After
for number, user in enumerate(
    users,
    start=1,
):
    print(number, user)
```

## 55-4. 선택 키 조회

```python
# Before
if "nickname" in user:
    nickname = user["nickname"]
else:
    nickname = "익명"
```

```python
# After
nickname = user.get(
    "nickname",
    "익명",
)
```

## 55-5. 불리언 비교

```python
# Before
if is_active == True:
    ...
```

```python
# After
if is_active:
    ...
```

## 55-6. 여러 값 비교

```python
# Before
if role == "admin" or role == "manager":
    ...
```

```python
# After
if role in {
    "admin",
    "manager",
}:
    ...
```

## 55-7. 리스트 생성

```python
# Before
names = []

for user in users:
    names.append(user["name"])
```

```python
# After
names = [
    user["name"]
    for user in users
]
```

## 55-8. 하나라도 참

```python
# Before
found = False

for user in users:
    if user["active"]:
        found = True
        break
```

```python
# After
found = any(
    user["active"]
    for user in users
)
```

## 55-9. 모두 참

```python
# Before
valid = True

for user in users:
    if not user.get("email"):
        valid = False
        break
```

```python
# After
valid = all(
    user.get("email")
    for user in users
)
```

## 55-10. 파일 경로

```python
# Before
path = "data/" + name + ".json"
```

```python
# After
path = (
    Path("data")
    / f"{name}.json"
)
```

## 55-11. 파일 열기

```python
# Before
file = open(path)
content = file.read()
file.close()
```

```python
# After
with path.open(
    "r",
    encoding="utf-8",
) as file:
    content = file.read()
```

## 55-12. 예외 처리

```python
# Before
try:
    ...
except:
    pass
```

```python
# After
try:
    ...
except ValueError as error:
    logger.warning(
        "입력값 오류: %s",
        error,
    )
```

## 55-13. 문자열 조합

```python
# Before
message = name + " " + str(age)
```

```python
# After
message = f"{name} {age}"
```

## 55-14. 상수

```python
# Before
if score >= 60:
    ...
```

```python
# After
PASS_SCORE = 60

if score >= PASS_SCORE:
    ...
```

## 55-15. 가변 기본 인자

```python
# Before
def append_item(
    item,
    items=[],
):
    ...
```

```python
# After
def append_item(
    item,
    items=None,
):
    if items is None:
        items = []
```

---

# 56. 좋은 코드라고 무조건 짧은 것은 아니다

짧지만 이해하기 어려운 코드:

```python
result = [
    x["name"]
    for x in sorted(
        filter(
            lambda x: x["active"],
            users,
        ),
        key=lambda x: -x["score"],
    )
]
```

조금 길지만 단계가 명확한 코드:

```python
active_users = [
    user
    for user in users
    if user["active"]
]

sorted_users = sorted(
    active_users,
    key=lambda user: user["score"],
    reverse=True,
)

user_names = [
    user["name"]
    for user in sorted_users
]
```

> [!IMPORTANT]
> 코드 길이는 품질 기준 중 하나일 뿐이다.
>
> 중간 변수에 의미 있는 이름을 붙이면 처리 단계가 문서처럼 읽힐 수 있다.

---

# 57. 리팩토링 순서

기존 코드를 한 번에 완전히 바꾸기보다 다음 순서로 개선한다.

```text
1. 현재 동작 확인
    ↓
2. 실행 결과 고정
    ↓
3. 이름 개선
    ↓
4. 중복 제거
    ↓
5. 함수 책임 분리
    ↓
6. 예외 흐름 정리
    ↓
7. 타입 힌트·문서 보강
    ↓
8. 다시 실행·테스트
```

> [!WARNING]
> 동작 확인 없이 구조부터 크게 변경하면 기존 기능이 깨져도 원인을 찾기 어렵다.

---

# 58. 리팩토링 전 확인할 질문

- 이 코드의 현재 입력과 출력은 무엇인가?
- 어떤 값이 반드시 존재해야 하는가?
- 어떤 오류가 발생할 수 있는가?
- 같은 로직이 반복되고 있는가?
- 함수 하나에 서로 다른 책임이 섞였는가?
- 원본 데이터를 변경하고 있는가?
- 이름만 보고 역할을 이해할 수 있는가?
- 테스트하기 어려운 외부 작업이 섞였는가?
- 더 짧은 코드가 실제로 더 읽기 쉬운가?

---

# 59. 자주 하는 실수

## 59-1. Pythonic 코드를 무조건 짧은 코드로 생각

짧아도 의미가 불분명하면 좋은 코드가 아니다.

## 59-2. 모든 반복문을 컴프리헨션으로 변경

조건이 복잡하면 일반 반복문이 더 읽기 쉽다.

## 59-3. 모든 함수를 지나치게 작게 분리

한 줄 함수가 너무 많아지면 흐름을 따라가기 어려울 수 있다.

## 59-4. 타입 힌트가 실행 시 검증한다고 생각

타입 힌트는 기본적으로 문서와 정적 분석 정보다.

## 59-5. `dict.get()`을 모든 키에 사용

필수 키가 누락된 버그까지 숨길 수 있다.

## 59-6. 모든 코드를 클래스로 작성

상태가 필요 없는 기능은 함수나 모듈이 더 적합할 수 있다.

## 59-7. `lambda`에 복잡한 조건 작성

이름 있는 함수로 분리하는 편이 읽기 쉽다.

## 59-8. 원본 객체 변경 여부를 고려하지 않음

함수 호출 후 외부 데이터가 예상치 않게 바뀔 수 있다.

## 59-9. 예외를 잡고 아무 처리도 하지 않음

버그와 데이터 오류를 숨길 수 있다.

## 59-10. 주석으로 나쁜 이름을 보완

주석보다 변수와 함수 이름을 먼저 개선한다.

## 59-11. 매직 넘버와 문자열 반복

정책 변경 시 수정 위치를 찾기 어렵다.

## 59-12. 리팩토링과 기능 추가를 동시에 크게 진행

오류가 발생했을 때 원인을 구분하기 어렵다.

---

# 60. 핵심 요약

```text
좋은 이름
→ 코드의 역할 설명

직접 순회
→ 값만 필요할 때

enumerate()
→ 번호와 값이 필요할 때

zip()
→ 여러 목록을 함께 순회할 때

any()
→ 하나라도 참

all()
→ 모두 참
```

```text
컴프리헨션
→ 단순 변환·필터

일반 반복문
→ 복잡한 조건·예외·로그

Guard Clause
→ 중첩 감소

상수
→ 정책값 의미 부여

타입 힌트
→ 입력과 반환 의도 표현
```

```text
함수
→ 하나의 주요 책임

클래스
→ 상태와 동작을 함께 관리

예외 처리
→ 구체적인 오류만 처리

리팩토링
→ 동작을 유지하며 구조 개선
```

---

# 61. 최종 체크리스트

- [ ] 변수명과 함수명만 보고 역할을 이해할 수 있는가?
- [ ] 인덱스가 필요하지 않은데 `range(len())`을 사용하지 않았는가?
- [ ] 인덱스가 필요하면 `enumerate()`를 검토했는가?
- [ ] 두 목록을 함께 순회할 때 `zip()`을 검토했는가?
- [ ] 빈 컬렉션을 자연스럽게 검사했는가?
- [ ] `None`을 `is None`으로 비교했는가?
- [ ] 선택 키와 필수 키를 구분했는가?
- [ ] 하나 또는 모두 조건에 `any()`·`all()`을 검토했는가?
- [ ] 컴프리헨션이 한 번에 이해되는 수준인가?
- [ ] 중첩 조건을 Guard Clause로 줄일 수 있는가?
- [ ] 매직 넘버와 문자열을 상수로 분리했는가?
- [ ] 함수가 하나의 주요 책임을 담당하는가?
- [ ] 반환값 자료형이 일관적인가?
- [ ] 가변 기본 인자를 사용하지 않았는가?
- [ ] 원본 데이터를 변경하는지 명확한가?
- [ ] 타입 힌트와 Docstring이 실제 이해에 도움이 되는가?
- [ ] 구체적인 예외만 처리하고 있는가?
- [ ] 파일과 외부 자원을 `with`로 관리하는가?
- [ ] 클래스가 실제로 필요한 구조인가?
- [ ] 중복 로직을 의미 있는 함수로 모았는가?
- [ ] 리팩토링 전후 실행 결과가 같은지 확인했는가?

---

# 마무리

실무 코딩 스타일은 특정 문법을 많이 사용하는 것이 아니다.

```text
코드의 목적을 이름으로 표현하고
    ↓
가장 자연스러운 자료구조와 문법을 선택하며
    ↓
함수와 클래스의 책임을 분리하고
    ↓
잘못된 상태와 오류를 명확하게 처리하고
    ↓
다른 개발자가 안전하게 수정할 수 있게 만드는 것
```

Pythonic한 코드는 단순히 짧은 코드가 아니라, **Python을 사용하는 개발자가 자연스럽게 읽고 예상할 수 있는 코드**다.
