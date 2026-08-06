---
title: Python 딕셔너리와 집합
version: v2.0-final
last_updated: 2026-08-06
status: Completed
---

# Python 딕셔너리와 집합

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `07_Python_딕셔너리와_집합.md` |
| 분류 | `04_Python` |
| 원본 기준 | `workspace_python/07_dict.py`, `workspace_teacher/workspace_python/_07_dict.py` |
| 핵심 범위 | 딕셔너리 생성, 키 조회, `get()`, 중첩 딕셔너리, 값 추가·수정, View 객체, `update()`, `pop()`, `popitem()`, `fromkeys()`, 순회, 집합 |
| 실습 범위 | 사용자 정보, 중첩 스킬 정보, 안전한 기본값, 키·값 순회, 장바구니 금액 계산 |
| 문서 형식 | Python Developer-Wiki V2 확정 형식 |

> 이 문서는 내 코드와 강사님 코드 전체를 순서대로 나열하지 않는다.  
> 딕셔너리의 생성·조회·변경·삭제·순회에 필요한 코드만 발췌하고, 오류 조건과 실무 선택 기준을 함께 설명한다.

---

# 개요

딕셔너리는 값을 **키와 값의 쌍**으로 저장하는 자료형이다.

```text
사용자 이름
→ "name": "Kim"

상품 가격
→ "price": 45000

로그인 여부
→ "active": True
```

리스트가 위치를 이용해 값을 찾는다면 딕셔너리는 의미 있는 키를 이용해 값을 찾는다.

```text
리스트
→ users[0]

딕셔너리
→ user["name"]
```

딕셔너리는 사용자 정보, 상품 정보, 설정값, JSON 데이터처럼 여러 속성을 하나의 객체로 묶을 때 자주 사용한다.

---

# 핵심 개념

| 개념 | 핵심 역할 |
| --- | --- |
| 딕셔너리 | 키와 값의 쌍으로 데이터를 저장 |
| 키 | 값을 찾기 위한 고유한 식별자 |
| 값 | 키에 연결된 실제 데이터 |
| `get()` | 키가 없어도 오류 없이 조회 |
| 중첩 딕셔너리 | 딕셔너리 안에 딕셔너리를 저장 |
| `keys()` | 모든 키를 반환 |
| `values()` | 모든 값을 반환 |
| `items()` | 키와 값의 쌍을 반환 |
| `update()` | 여러 키를 한 번에 추가·수정 |
| `pop()` | 특정 키를 삭제하며 값을 반환 |
| `popitem()` | 마지막 키·값 쌍을 삭제하며 반환 |
| `fromkeys()` | 여러 키로 새 딕셔너리 생성 |
| 집합 `set` | 중복을 제거하며 값을 저장 |

---

# 학습 목표

이 문서를 학습한 뒤 다음 내용을 설명하고 작성할 수 있어야 한다.

- 빈 딕셔너리와 값이 있는 딕셔너리를 만들 수 있다.
- 키와 값의 역할을 설명할 수 있다.
- 중복 키가 있을 때 마지막 값이 남는 이유를 이해한다.
- 대괄호로 필수 키를 조회할 수 있다.
- `get()`으로 선택 키를 안전하게 조회할 수 있다.
- `get()`의 기본값을 지정할 수 있다.
- 중첩 딕셔너리의 값을 조회할 수 있다.
- 중첩 `get()`에서 `NoneType` 오류가 발생하는 이유를 이해한다.
- 키가 있으면 수정되고 없으면 추가된다는 점을 이해한다.
- `in`, `not in`으로 키 포함 여부를 확인할 수 있다.
- `len()`으로 키 개수를 확인할 수 있다.
- `keys()`, `values()`, `items()`의 차이를 구분할 수 있다.
- View 객체가 리스트가 아니라는 점을 이해한다.
- `update()`로 여러 값을 변경할 수 있다.
- `pop()`과 `popitem()`의 차이를 설명할 수 있다.
- `dict.fromkeys()`로 기본 딕셔너리를 만들 수 있다.
- 딕셔너리를 직접 순회하거나 `items()`로 순회할 수 있다.
- 집합으로 중복을 제거할 수 있다.
- 집합의 순서가 보장되지 않는다는 점을 이해한다.

---

# 1. 빈 딕셔너리 생성

## 1-1. 내 코드와 강사님 코드

```python
data = {}
data = dict()

print(type(data))
```

## 1-2. 출력 결과

```text
<class 'dict'>
```

`{}`와 `dict()`는 모두 빈 딕셔너리를 만든다.

> [!TIP]
> 빈 딕셔너리는 일반적으로 `{}`로 작성하는 경우가 많다.

---

# 2. 키와 값

## 2-1. 원본 코드

```python
user = {
    "이름": "홍길동",
    "직업": "도적",
}
```

## 2-2. 구성

| 요소 | 의미 |
| --- | --- |
| `"이름"` | 키 |
| `"홍길동"` | 값 |
| `:` | 키와 값을 연결 |
| `,` | 각 키·값 쌍을 구분 |

## 2-3. 실행

```python
print(user)
```

출력:

```text
{'이름': '홍길동', '직업': '도적'}
```

---

# 3. 딕셔너리 키 규칙

딕셔너리 키는 고유해야 한다.

```python
user = {
    "직업": "마법사",
    "직업": "마법사2",
}

print(user)
```

## 3-1. 출력 결과

```text
{'직업': '마법사2'}
```

같은 키가 여러 번 작성되면 마지막 값이 남는다.

## 3-2. 키로 사용할 수 있는 값

일반적으로 다음과 같은 불변 자료형을 키로 사용할 수 있다.

- 문자열
- 숫자
- 튜플

리스트는 키로 사용할 수 없다.

```python
data = {
    [1, 2]: "값",
}
```

발생 결과:

```text
TypeError: unhashable type: 'list'
```

---

# 4. `dict()`로 생성

## 4-1. 원본 코드

```python
values = dict(
    a=10,
    b=20,
)

print(values)
```

## 4-2. 출력 결과

```text
{'a': 10, 'b': 20}
```

키워드 전달인자로 생성하면 키가 문자열로 저장된다.

> [!WARNING]
> `dict(a=10)` 방식에서는 Python 변수명 규칙을 따르는 키만 직접 작성할 수 있다.
>
> 공백이나 하이픈이 있는 키는 일반 딕셔너리 문법을 사용한다.

---

# 5. 대괄호로 값 조회

## 5-1. 내 코드와 강사님 코드

```python
user = {
    "이름": "홍길동",
    "직업": "도적",
}

print(user["이름"])
```

## 5-2. 출력 결과

```text
홍길동
```

대괄호 안에 키를 작성하면 연결된 값을 반환한다.

---

# 6. 없는 키 조회와 `KeyError`

```python
user = {
    "이름": "홍길동",
}

print(user["이름2"])
```

## 6-1. 발생 결과

```text
KeyError: '이름2'
```

대괄호 조회는 키가 반드시 존재해야 할 때 적합하다.

> [!IMPORTANT]
> 필수 키가 누락되면 오류가 발생하는 것이 오히려 데이터 문제를 빨리 발견하는 데 도움이 될 수 있다.

---

# 7. `get()`으로 안전하게 조회

## 7-1. 원본 코드

```python
print(user.get("이름"))
print(user.get("이름2"))
```

## 7-2. 출력 결과

```text
홍길동
None
```

`get()`은 키가 없으면 기본적으로 `None`을 반환한다.

## 7-3. 대괄호와 비교

| 방식 | 키가 있을 때 | 키가 없을 때 |
| --- | --- | --- |
| `user["이름"]` | 값 반환 | `KeyError` |
| `user.get("이름")` | 값 반환 | `None` |

---

# 8. `get()` 기본값

```python
name = user.get(
    "이름2",
    "이름 없음",
)

print(name)
```

## 8-1. 출력 결과

```text
이름 없음
```

두 번째 전달인자는 키가 없을 때 사용할 기본값이다.

```text
키 존재
→ 실제 값 반환

키 없음
→ 두 번째 값 반환
```

---

# 9. 대괄호와 `get()` 선택 기준

```text
반드시 존재해야 하는 키
→ data["id"]

없을 수 있는 선택 키
→ data.get("nickname")

없으면 기본값 사용
→ data.get("nickname", "익명")
```

> [!TIP]
> 모든 키에 무조건 `get()`을 사용하면 필수 데이터가 누락된 버그를 숨길 수 있다.

---

# 10. 중첩 딕셔너리

딕셔너리의 값으로 다른 딕셔너리를 저장할 수 있다.

```python
user = {
    "이름": "홍길동",
    "스킬": {
        "공격": "훔치기",
        "방어": "도망가기",
    },
}
```

## 10-1. 구조

```text
user
├─ 이름
└─ 스킬
   ├─ 공격
   └─ 방어
```

---

# 11. 중첩 값 조회

## 11-1. 원본 코드

```python
print(
    user["스킬"]["공격"]
)
```

## 11-2. 출력 결과

```text
훔치기
```

## 11-3. 단계별 조회

```python
skills = user["스킬"]
attack = skills["공격"]

print(attack)
```

출력:

```text
훔치기
```

---

# 12. 중첩 `get()`

## 12-1. 원본 코드

```python
print(
    user.get("스킬")
    .get("공격")
)
```

## 12-2. 출력 결과

```text
훔치기
```

첫 번째 `get()`이 딕셔너리를 반환하므로 두 번째 `get()`을 호출할 수 있다.

---

# 13. 중첩 `get()`의 오류

```python
print(
    user.get("스킬2")
    .get("공격")
)
```

## 13-1. 발생 결과

```text
AttributeError: 'NoneType' object has no attribute 'get'
```

## 13-2. 오류 원인

```text
user.get("스킬2")
→ None

None.get("공격")
→ 사용할 수 없음
```

---

# 14. 빈 딕셔너리를 기본값으로 사용

## 14-1. 원본 코드

```python
attack = (
    user.get("스킬2", {})
    .get("공격", 0)
)

print(attack)
```

## 14-2. 출력 결과

```text
0
```

첫 번째 키가 없으면 빈 딕셔너리를 사용하므로 다음 `get()`을 안전하게 호출할 수 있다.

> [!TIP]
> 중첩 데이터가 지나치게 깊어지면 `get()` 연결도 읽기 어려워질 수 있다.
>
> 복잡한 구조에서는 단계별 변수나 검증 함수를 사용한다.

---

# 15. 값 수정

## 15-1. 원본 코드

```python
user["직업"] = "전사"

print(user)
```

기존 키에 값을 대입하면 수정된다.

## 15-2. 출력 결과

```text
{'이름': '홍길동', '직업': '전사', ...}
```

---

# 16. 새 키 추가

```python
user["직업2"] = "전사2"

print(user["직업2"])
```

## 16-1. 출력 결과

```text
전사2
```

키가 없으면 새로운 키·값 쌍이 추가된다.

```text
기존 키에 대입
→ 수정

없는 키에 대입
→ 추가
```

---

# 17. 중첩 값 추가

```python
user["스킬"]["버프"] = "힐"

print(
    user["스킬"]
)
```

## 17-1. 출력 결과

```text
{'공격': '훔치기', '방어': '도망가기', '버프': '힐'}
```

중첩 딕셔너리도 같은 방식으로 추가·수정할 수 있다.

---

# 18. `in`과 `not in`

딕셔너리에서 `in`은 기본적으로 **키**를 검사한다.

```python
print("스킬" in user)
print("공격" in user)
print(
    "공격"
    in user["스킬"]
)
```

## 18-1. 출력 결과

```text
True
False
True
```

`"공격"`은 최상위 딕셔너리의 키가 아니라 `"스킬"` 딕셔너리 안의 키다.

## 18-2. `not in`

```python
print(
    "공격"
    not in user["스킬"]
)
```

출력:

```text
False
```

---

# 19. `len()`과 키 개수

```python
print(len(user))
```

`len()`은 최상위 키의 개수를 반환한다.

중첩 딕셔너리 안의 키까지 모두 세지 않는다.

```python
data = {
    "a": 1,
    "b": {
        "x": 10,
        "y": 20,
    },
}

print(len(data))
```

출력:

```text
2
```

---

# 20. `keys()`

`keys()`는 모든 키를 View 객체로 반환한다.

```python
keys = user.keys()

print(keys)
```

출력 형태:

```text
dict_keys(['이름', '직업', '스킬', '직업2'])
```

## 20-1. 리스트 변환

```python
key_list = list(
    user.keys()
)

print(key_list[0])
```

---

# 21. `values()`

`values()`는 모든 값을 View 객체로 반환한다.

```python
values = user.values()

print(values)
```

출력 형태:

```text
dict_values([...])
```

View 객체는 리스트처럼 인덱스로 직접 접근할 수 없다.

```python
values[0]
```

발생 결과:

```text
TypeError
```

리스트로 변환:

```python
print(
    list(values)[0]
)
```

---

# 22. `items()`

`items()`는 키와 값을 튜플 형태로 반환한다.

```python
items = user.items()

print(items)
```

출력 형태:

```text
dict_items([('이름', '홍길동'), ...])
```

각 항목의 구조:

```text
(key, value)
```

---

# 23. 딕셔너리 View 객체

`keys()`, `values()`, `items()`는 복사된 리스트가 아니라 딕셔너리를 바라보는 View 객체를 반환한다.

```python
data = {
    "a": 1,
}

keys = data.keys()

data["b"] = 2

print(keys)
```

## 23-1. 출력 결과

```text
dict_keys(['a', 'b'])
```

원본 딕셔너리 변경이 View에 반영된다.

> [!IMPORTANT]
> 특정 시점의 값을 고정하려면 `list(data.keys())`처럼 리스트로 변환한다.

---

# 24. `update()`

`update()`는 여러 키를 한 번에 추가하거나 수정한다.

## 24-1. 원본 코드

```python
user.update(
    이름="타이거",
    직업="호랑이",
)

print(user)
```

기존 키는 수정된다.

## 24-2. 새 키 포함

```python
user.update(
    이름="타이거",
    직업="호랑이",
    나이=30,
)
```

`나이` 키가 없었다면 새로 추가된다.

## 24-3. 딕셔너리 전달

```python
user.update(
    {
        "레벨": 10,
        "지역": "서울",
    }
)
```

> [!TIP]
> 키 이름이 Python 변수명 규칙에 맞지 않으면 딕셔너리를 전달하는 방식을 사용한다.

---

# 25. `pop()`

`pop()`은 지정한 키를 삭제하며 값을 반환한다.

```python
age = user.pop("나이")

print(age)
print("나이" in user)
```

## 25-1. 출력 결과

```text
30
False
```

## 25-2. 없는 키

```python
user.pop("나이")
```

발생 결과:

```text
KeyError
```

---

# 26. `pop()` 기본값

```python
age = user.pop(
    "나이",
    0,
)

print(age)
```

키가 없으면 기본값 `0`을 반환하며 오류가 발생하지 않는다.

> [!TIP]
> 삭제하면서 값도 필요하면 `pop()`을 사용한다.

---

# 27. `popitem()`

`popitem()`은 마지막 키·값 쌍을 삭제하며 튜플로 반환한다.

```python
removed_item = (
    user.popitem()
)

print(removed_item)
```

출력 형태:

```text
('지역', '서울')
```

> [!IMPORTANT]
> 최신 Python에서 `popitem()`은 마지막에 추가된 항목을 제거한다.
>
> 임의 항목을 삭제한다고만 이해하면 안 된다.

---

# 28. `del`

값을 반환받을 필요 없이 특정 키를 삭제할 수 있다.

```python
user = {
    "name": "Kim",
    "age": 21,
}

del user["age"]

print(user)
```

출력:

```text
{'name': 'Kim'}
```

없는 키를 삭제하면 `KeyError`가 발생한다.

---

# 29. `clear()`

`clear()`는 모든 키·값 쌍을 삭제한다.

```python
user = {
    "name": "Kim",
    "age": 21,
}

user.clear()

print(user)
```

출력:

```text
{}
```

---

# 30. `dict.fromkeys()`

## 30-1. 원본 코드

```python
keys = [
    "a",
    "b",
    "c",
]

data = dict.fromkeys(
    keys
)

print(data)
```

## 30-2. 출력 결과

```text
{'a': None, 'b': None, 'c': None}
```

기본값을 지정할 수도 있다.

```python
data = dict.fromkeys(
    keys,
    0,
)

print(data)
```

출력:

```text
{'a': 0, 'b': 0, 'c': 0}
```

---

# 31. `fromkeys()`의 가변 기본값 주의

```python
data = dict.fromkeys(
    ["a", "b"],
    [],
)

data["a"].append(1)

print(data)
```

## 31-1. 출력 결과

```text
{'a': [1], 'b': [1]}
```

모든 키가 같은 리스트 객체를 공유하기 때문이다.

안전한 생성:

```python
data = {
    key: []
    for key in [
        "a",
        "b",
    ]
}
```

---

# 32. 딕셔너리 직접 순회

딕셔너리를 직접 순회하면 키가 나온다.

```python
data = {
    "a": 10,
    "b": 20,
}

for key in data:
    print(key)
    print(data[key])
```

## 32-1. 출력 결과

```text
a
10
b
20
```

---

# 33. `items()`로 키와 값 순회

```python
data = {
    "a": 10,
    "b": 20,
}

for key, value in data.items():
    print(key, value)
```

## 33-1. 출력 결과

```text
a 10
b 20
```

> [!TIP]
> 키와 값이 모두 필요하면 `items()`를 사용하는 것이 가장 자연스럽다.

---

# 34. `enumerate()`와 `items()`

강사님 코드에는 딕셔너리 항목에 순번을 붙이는 예제가 있다.

```python
users = {
    "admin": "1234",
    "guest": "guest",
    "user1": "abcd",
}

for index, item in enumerate(
    users.items()
):
    print(
        index,
        item[0],
        item[1],
    )
```

더 직접적으로 언패킹할 수 있다.

```python
for index, (
    user_id,
    password,
) in enumerate(
    users.items(),
    start=1,
):
    print(
        index,
        user_id,
        password,
    )
```

---

# 35. 딕셔너리 컴프리헨션

반복문을 이용해 새 딕셔너리를 만들 수 있다.

```python
numbers = [
    1,
    2,
    3,
]

squares = {
    number: number ** 2
    for number in numbers
}

print(squares)
```

## 35-1. 출력 결과

```text
{1: 1, 2: 4, 3: 9}
```

조건 추가:

```python
even_squares = {
    number: number ** 2
    for number in range(6)
    if number % 2 == 0
}
```

---

# 36. 딕셔너리 복사

단순 대입은 같은 객체를 공유한다.

```python
original = {
    "name": "Kim",
}

copied = original

copied["name"] = "Lee"

print(original)
```

출력:

```text
{'name': 'Lee'}
```

얕은 복사:

```python
copied = original.copy()
```

중첩 딕셔너리는 내부 객체를 공유할 수 있으므로 깊은 복사가 필요할 수 있다.

---

# 37. 집합 생성

집합은 중복을 제거하며 값을 저장한다.

## 37-1. 원본 코드

```python
text = "hello"

print(list(text))
print(set(text))
```

## 37-2. 출력 예

```text
['h', 'e', 'l', 'l', 'o']
{'h', 'e', 'l', 'o'}
```

집합은 중복된 `l` 하나를 제거한다.

> [!IMPORTANT]
> 집합의 출력 순서는 실행 환경에 따라 달라질 수 있다.

---

# 38. 빈 집합

빈 중괄호는 딕셔너리다.

```python
print(type({}))
```

출력:

```text
<class 'dict'>
```

빈 집합은 `set()`으로 만든다.

```python
empty_set = set()

print(type(empty_set))
```

출력:

```text
<class 'set'>
```

---

# 39. 집합의 주요 특징

- 중복 값을 저장하지 않는다.
- 순서를 보장하지 않는다.
- 인덱스로 조회할 수 없다.
- 포함 검사에 적합하다.
- 합집합·교집합·차집합 연산이 가능하다.

```python
permissions = {
    "read",
    "write",
}

print(
    "read"
    in permissions
)
```

출력:

```text
True
```

---

# 40. 집합의 추가와 삭제

```python
skills = {
    "Python",
    "HTML",
}

skills.add("CSS")
skills.discard("HTML")

print(skills)
```

`discard()`는 값이 없어도 오류가 발생하지 않는다.

`remove()`는 값이 없으면 `KeyError`가 발생한다.

---

# 41. 집합 연산

```python
frontend = {
    "HTML",
    "CSS",
    "JavaScript",
}

backend = {
    "Python",
    "Java",
    "JavaScript",
}
```

## 41-1. 합집합

```python
print(
    frontend | backend
)
```

## 41-2. 교집합

```python
print(
    frontend & backend
)
```

출력:

```text
{'JavaScript'}
```

## 41-3. 차집합

```python
print(
    frontend - backend
)
```

---

# 42. 딕셔너리와 집합 비교

| 구분 | 딕셔너리 | 집합 |
| --- | --- | --- |
| 구조 | 키와 값 | 값만 저장 |
| 중복 | 키 중복 불가 | 값 중복 불가 |
| 조회 | 키로 값 조회 | 값 포함 여부 |
| 순서 | 삽입 순서 유지 | 순서 목적 아님 |
| 주요 사용 | 구조화된 데이터 | 중복 제거·집합 연산 |

---

# 43. 내 코드와 강사님 코드 비교

| 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 딕셔너리 생성 | JavaScript와 비교한 메모 추가 | 핵심 문법 중심 |
| 중복 키 | 마지막 값이 남는 점 메모 | 실제 중복 키 예제 |
| `get()` | 안전한 조회와 기본값 상세 기록 | 핵심 동작 설명 |
| 중첩 조회 | `NoneType` 오류와 빈 딕셔너리 기본값 추가 | 정상 조회 중심 |
| View 객체 | 리스트 변환 필요성 메모 | `values()` 변환 예제 |
| `popitem()` | 임의 삭제라고 기록 | 기본 실행 예제 |
| 집합 | JSON 키와 연결한 메모 | 중복 제거·순서 미보장 설명 |
| 순회 | `items()` 언패킹 | 기본 순회와 `enumerate()` 추가 |

## 43-1. 내 코드의 장점

- `get()`과 대괄호 조회의 차이를 구체적으로 기록했다.
- 중첩 딕셔너리에서 발생할 수 있는 `NoneType` 오류를 직접 확인했다.
- `keys()`, `values()`, `items()`의 반환 형태를 실험했다.
- 삭제 메서드와 기본값 사용을 자세히 확인했다.

## 43-2. 내 코드의 개선점

- Python 딕셔너리 키는 문자열만 가능한 것이 아니다.
- `popitem()`은 최신 Python에서 마지막 항목을 제거한다.
- 집합과 JSON 키는 서로 다른 개념이다.
- View 객체는 “유사 배열”보다 동적 View 객체라고 설명하는 것이 정확하다.
- 모든 선택 키에 `get()`을 사용하는 것이 항상 안전한 것은 아니다.

## 43-3. 강사님 코드의 장점

- 딕셔너리의 생성부터 순회까지 핵심 흐름이 명확하다.
- 중복 키, 중첩 딕셔너리, 기본값, 삭제를 한 파일에서 비교할 수 있다.
- 로그인·장바구니 같은 실습 문제로 실제 활용을 연결한다.

## 43-4. 강사님 코드의 보충점

- 키 자료형과 해시 가능성 설명이 필요하다.
- View 객체가 원본 변화를 반영한다는 설명이 필요하다.
- `fromkeys()`에 가변 기본값을 사용할 때의 문제가 필요하다.
- 집합의 생성·연산을 조금 더 보충하면 좋다.

---

# 44. 기존 코드에서 개선 코드로 바꾼 이유

## 44-1. 의미 있는 영문 키 사용

기존 학습 예제:

```python
user = {
    "이름": "홍길동",
}
```

실무형 예제:

```python
user = {
    "name": "Kim",
    "age": 21,
}
```

API·JSON·데이터베이스와 연결할 때 영문 키를 자주 사용한다.

## 44-2. 중첩 조회 분리

기존:

```python
user.get(
    "스킬2",
    {},
).get(
    "공격",
    0,
)
```

복잡해지면:

```python
skills = user.get(
    "skills",
    {}
)

attack = skills.get(
    "attack",
    0,
)
```

중간 변수에 의미를 부여하면 흐름이 명확해진다.

## 44-3. 키와 값 순회

기존:

```python
for key in data:
    print(
        key,
        data[key],
    )
```

개선:

```python
for key, value in data.items():
    print(key, value)
```

---

# 45. 실무형 예제: 장바구니 금액 계산

```python
cart = {
    "사과": {
        "가격": 1000,
        "개수": 3,
    },
    "바나나": {
        "가격": 2000,
        "개수": 4,
    },
    "복숭아": {
        "가격": 1500,
        "개수": 2,
    },
    "키위": {
        "가격": 2200,
        "개수": 5,
    },
}

total_price = 0

for product_name, product in (
    cart.items()
):
    subtotal = (
        product["가격"]
        * product["개수"]
    )

    total_price += subtotal

    print(
        f"{product_name}: "
        f"{subtotal:,}원"
    )

print(
    f"총 금액: "
    f"{total_price:,}원"
)
```

## 45-1. 출력 결과

```text
사과: 3,000원
바나나: 8,000원
복숭아: 3,000원
키위: 11,000원
총 금액: 25,000원
```

## 45-2. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| 중첩 딕셔너리 | 상품별 가격과 개수 저장 |
| `items()` | 상품명과 상세정보를 함께 순회 |
| 대괄호 조회 | 반드시 존재해야 하는 가격·개수 조회 |
| 누적 변수 | 상품별 금액을 총액에 계속 더함 |
| f-string | 금액을 읽기 좋은 형식으로 출력 |

---

# 46. 대표 오류로 이해하기

## 46-1. 없는 키 대괄호 조회

```python
user["nickname"]
```

발생 결과:

```text
KeyError
```

---

## 46-2. 중첩 `get()`의 `NoneType` 오류

```python
user.get(
    "skills"
).get(
    "attack"
)
```

첫 번째 결과가 `None`이면 오류가 발생한다.

---

## 46-3. View 객체 인덱싱

```python
values = user.values()

print(values[0])
```

발생 결과:

```text
TypeError
```

---

## 46-4. 없는 키 `pop()`

```python
user.pop("age")
```

발생 결과:

```text
KeyError
```

기본값을 전달하면 안전하게 처리할 수 있다.

---

## 46-5. 빈 집합을 `{}`로 생성

```python
value = {}

print(type(value))
```

출력:

```text
<class 'dict'>
```

집합은 `set()`을 사용한다.

---

# 47. 자주 하는 실수

## 47-1. 딕셔너리 키는 문자열만 가능하다고 생각

해시 가능한 값이면 숫자·튜플도 키로 사용할 수 있다.

## 47-2. 중복 키가 모두 저장된다고 생각

마지막 값만 남는다.

## 47-3. 선택 키를 대괄호로 조회

키가 없으면 `KeyError`가 발생한다.

## 47-4. 필수 키까지 모두 `get()`으로 조회

누락된 데이터 오류를 숨길 수 있다.

## 47-5. 중첩 `get()` 앞 결과가 `None`일 수 있음을 무시

`NoneType` 오류가 발생할 수 있다.

## 47-6. `in`이 값을 검사한다고 생각

딕셔너리에서는 기본적으로 키를 검사한다.

## 47-7. `keys()`·`values()`를 리스트로 생각

View 객체이며 인덱싱할 수 없다.

## 47-8. `popitem()`이 임의 항목을 삭제한다고 생각

최신 Python에서는 마지막 항목을 제거한다.

## 47-9. `fromkeys()`에 가변 객체 기본값 사용

모든 키가 같은 객체를 공유할 수 있다.

## 47-10. 빈 집합을 `{}`로 작성

빈 딕셔너리가 생성된다.

## 47-11. 집합의 순서를 기대

집합은 순서 표현을 위한 자료형이 아니다.

## 47-12. 집합에 인덱스 접근

집합은 인덱스를 제공하지 않는다.

---

# 48. 핵심 요약

```text
{}
dict()
→ 딕셔너리 생성

data["key"]
→ 필수 키 조회

data.get("key")
→ 선택 키 조회

data.get("key", default)
→ 기본값 사용
```

```text
keys()
→ 키

values()
→ 값

items()
→ 키와 값

update()
→ 여러 값 추가·수정

pop()
→ 키 삭제 + 값 반환

popitem()
→ 마지막 항목 삭제
```

```text
for key in data
→ 키 순회

for key, value in data.items()
→ 키와 값 순회

set()
→ 빈 집합

set(values)
→ 중복 제거
```

---

# 49. 최종 체크리스트

- [ ] 빈 딕셔너리와 값이 있는 딕셔너리를 만들 수 있는가?
- [ ] 키와 값의 역할을 설명할 수 있는가?
- [ ] 중복 키는 마지막 값만 남음을 이해했는가?
- [ ] 대괄호와 `get()`의 차이를 설명할 수 있는가?
- [ ] `get()`의 기본값을 지정할 수 있는가?
- [ ] 중첩 딕셔너리 값을 조회할 수 있는가?
- [ ] 중첩 `get()`의 `NoneType` 오류를 방지할 수 있는가?
- [ ] 기존 키 수정과 새 키 추가를 구분할 수 있는가?
- [ ] `in`이 키를 검사함을 이해했는가?
- [ ] `keys()`, `values()`, `items()`를 구분할 수 있는가?
- [ ] View 객체가 원본 변경을 반영함을 이해했는가?
- [ ] `update()`로 여러 값을 변경할 수 있는가?
- [ ] `pop()`과 `popitem()`을 구분할 수 있는가?
- [ ] `dict.fromkeys()`를 사용할 수 있는가?
- [ ] 가변 기본값 공유 문제를 이해했는가?
- [ ] 딕셔너리를 직접 순회할 수 있는가?
- [ ] `items()`로 키와 값을 함께 순회할 수 있는가?
- [ ] 딕셔너리 컴프리헨션을 작성할 수 있는가?
- [ ] 빈 집합을 `set()`으로 만들 수 있는가?
- [ ] 집합의 중복 제거와 순서 특성을 이해했는가?
- [ ] 집합 연산을 사용할 수 있는가?

---

# 마무리

딕셔너리와 집합의 핵심은 데이터를 목적에 맞게 찾고 관리하는 것이다.

```text
키로 값을 구조화하고
    ↓
필수값과 선택값을 구분해 조회하고
    ↓
필요한 값을 추가·수정·삭제하고
    ↓
키와 값을 함께 반복 처리하고
    ↓
중복 제거와 포함 검사는 집합으로 처리하는 것
```

이 흐름을 이해하면 이후 조건문·반복문·함수에서 구조화된 데이터를 더 자연스럽게 처리할 수 있다.
