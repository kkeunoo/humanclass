# Python 딕셔너리와 집합

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `07_Python_딕셔너리와_집합.md` |
| 분류 | `04_Python` |
| 권장 선수 학습 | `04_Python_리스트와_컴프리헨션.md`, `05_Python_튜플과_불변자료형.md`, `06_Python_시퀀스와_슬라이싱.md` |
| 다음 학습 | `08_Python_조건문.md` |
| 원본 기준 | `workspace_python/07_dict.py`, `workspace_teacher/workspace_python/_07_dict.py` |
| 핵심 범위 | 딕셔너리 선언, 키와 값, 중첩 딕셔너리, `[]`, `get()`, 추가·수정, `in`, `len()`, `keys()`, `values()`, `items()`, `update()`, `pop()`, `popitem()`, `fromkeys()`, 반복문 |
| 보충 범위 | 해시 가능성, 키의 조건, 순서 보존, 복사, `setdefault()`, 딕셔너리 컴프리헨션, 집합 기초 |
| Quiz 처리 | 강사님 원본 하단 문제 1~5는 최종 Quiz 문서 단계에서 별도 분석 |

> 이 문서는 내 코드의 `07_dict.py`와 강사님 코드의 `_07_dict.py`를 직접 비교해 작성했습니다. 두 파일은 딕셔너리 생성부터 조회, 중첩 접근, 수정, 삭제, 순회까지 거의 같은 흐름을 가집니다. 강사님 파일 하단에는 문제 1~5가 포함되어 있지만, 현재 학습 문서에서는 문제의 존재와 연계 주제만 기록하고 상세 풀이와 Quiz 문서화는 전체 수업 문서 완성 후 진행합니다.

---

# 학습 목표

- 딕셔너리가 키와 값을 한 쌍으로 저장하는 자료형임을 설명할 수 있다.
- `{}`와 `dict()`를 사용해 빈 딕셔너리를 생성할 수 있다.
- 딕셔너리 리터럴로 여러 키와 값을 저장할 수 있다.
- 키가 중복될 때 뒤의 값이 남는다는 점을 이해한다.
- 문자열 키를 작성할 때 따옴표가 필요한 경우를 설명할 수 있다.
- `dict(a=10, b=20)` 형태의 생성 규칙과 제한을 설명할 수 있다.
- `dictionary[key]` 방식과 `get()` 방식의 차이를 구분할 수 있다.
- 존재하지 않는 키 접근에서 `KeyError`가 발생하는 이유를 안다.
- `get(key, default)`로 기본값을 지정할 수 있다.
- 중첩 딕셔너리의 값에 단계적으로 접근할 수 있다.
- 중첩 `get()` 호출에서 `NoneType` 오류가 발생하는 원인을 설명할 수 있다.
- 딕셔너리의 값을 수정하고 새 키를 추가할 수 있다.
- `in`과 `not in`이 기본적으로 키를 검사한다는 점을 이해한다.
- `len()`이 딕셔너리의 최상위 키 개수를 반환함을 안다.
- `keys()`, `values()`, `items()`의 반환 객체를 구분할 수 있다.
- 딕셔너리 뷰 객체가 리스트와 다른 점을 설명할 수 있다.
- `update()`로 값을 수정하거나 새 키를 추가할 수 있다.
- `pop()`과 `popitem()`의 차이를 설명할 수 있다.
- `dict.fromkeys()`로 여러 키를 한 번에 생성할 수 있다.
- 딕셔너리를 직접 순회하면 키가 나온다는 점을 이해한다.
- `items()`와 언패킹으로 키와 값을 함께 순회할 수 있다.
- 집합이 중복을 제거하고 원소 순서에 의존하지 않는 자료형임을 안다.
- 해시 가능성과 딕셔너리 키의 조건을 설명할 수 있다.
- 원본 주석의 부정확한 표현을 찾아 정확하게 수정할 수 있다.

---

# 1. 원본 코드

## 1.1 내 코드

```python
# 딕셔너리 선언
a = {}
a = dict()
print(type(a))

b = {
    # key는 javascript와 다르게 ''를 써줘야 함 (웬만해선 str)
    # 중복된 key값이 2개일 경우, 뒤에 오는 value를 가져옴
    '이름': '홍길동',
    '직업': '도적',
    '스킬': {
        '공격': '훔치기',
        '방어': '도망가기',
        'javascript': '중'
    }
}

print(b)

c = dict(a=10, b=20)
print(c)

# b.이름
print(b['이름'])
# print(b['이름2']) # 없는 key일 경우 KeyError: '이름2'

print(b.get('이름'))
print(b.get('이름2'))
print(b.get('이름2', '이름없음'))

d = b['스킬']
d['공격']
b['스킬']['공격']
print(b['스킬']['공격'])

print(b.get('스킬').get('공격'))
# print(b.get('스킬2').get('공격'))
print(b.get('스킬2', {}).get('공격', 0))

b['직업'] = '전사'
print(b)

b['직업2'] = '전사2'
print(b)

print('스킬' in b)
print('공격' in b['스킬'])
print('공격' not in b['스킬'])
print('공격' in b.get('스킬'))

print(len(b))

e = b.keys()
print(e)

f = b.values()
print(f)
# print(f[0])
print(list(f)[0])

g = b.items()
print(g)

a = 'hello'
print(list(a))
print(set(a))

b = {
    '이름': '홍길동',
    '직업': '도적',
    '스킬': {
        '공격': '훔치기',
        '방어': '도망가기',
        'javascript': '중'
    }
}

b.update(이름='타이거', 직업='호랑이')
b.update(이름='타이거', 직업='호랑이', 나이='30')
print(b)

c = b.pop('나이')
print(b)
print(c)

c = b.pop('나이', 0)
print(c)

c = b.popitem()
print(c)
print(b)

a = ['a', 'b', 'c']

b = {
    'a': 0,
    'b': 0,
    'c': 0,
}

b = {}
b[a[0]] = 0
b[a[1]] = 0

c = dict.fromkeys(a)
print(c)

for i in c:
    print(i)
    print(c[i])

for key, value in c.items():
    print(key, value)
```

## 1.2 강사님 코드

```python
# 딕셔너리 선언
a = {}
a = dict()
print(type(a))

b = {
    '이름': '호랑이심장',
    '직업': '마법사',
    '직업': '마법사2',
    '스킬': {
        '공격': '고백',
        '방어': '철벽남',
        'javascript': '상'
    }
}
print(b)

c = dict(a=10, b=20)
print(c)

# b.이름
print(b['이름'])
# print(b['이름2'])

print(b.get('이름'))
print(b.get('이름2'))
print(b.get('이름2', '이름없음'))

d = b['스킬']
d['공격']
b['스킬']['공격']
print(b['스킬']['공격'])

print(b.get('스킬').get('공격'))

print(b.get('스킬2', {}).get('공격', 0))

b['직업'] = '도적'
print(b)

b['직업2'] = '도적2'
print(b)

print('스킬' in b)
print('공격' in b)
print('공격' in b['스킬'])
print('공격' not in b['스킬'])

print(len(b))

e = b.keys()
print(e)

f = b.values()
print(f)
print(list(f)[0])

g = b.items()
print(g)

a = 'hello'
print(list(a))
print(set(a))

b = {
    '이름': '호랑이심장',
    '직업': '마법사',
    '직업': '마법사2',
    '스킬': {
        '공격': '고백',
        '방어': '철벽남',
        'javascript': '상'
    }
}

b.update(이름='타이거', 직업='강사')
b.update(이름='타이거', 직업='강사', 나이=20)
print(b)

c = b.pop('나이')
print(b)
print(c)

c = b.pop('나이', 0)
print(c)

c = b.popitem()
print(c)
print(b)

a = ['a', 'b', 'c']

b = {
    'a': 0,
    'b': 0,
    'c': 0
}

b = {}
b[a[0]] = 0
b[a[1]] = 0

c = dict.fromkeys(a)
print(c)

for i in c:
    print(i)
    print(c[i])

for k, v in c.items():
    print(k, v)
```

---

# 2. 강사님 원본의 Quiz 블록

강사님 파일 하단에는 다음 문제들이 포함되어 있습니다.

```text
문제 1
숫자 리스트에서 짝수 리스트와 홀수 합 구하기

문제 2
장바구니 전체 가격 계산

문제 3
UP/DOWN 게임

문제 4
딕셔너리를 이용한 로그인 검사

문제 5
랜덤 투표 결과와 최다 득표자 구하기
```

이 문제들은 다음 문서와 연결됩니다.

| 문제 | 연결 개념 |
| --- | --- |
| 문제 1 | 리스트, 반복문, 조건문 |
| 문제 2 | 중첩 딕셔너리, 반복문, 산술 연산 |
| 문제 3 | 조건문, 반복문, 난수 |
| 문제 4 | 딕셔너리 조회, 조건문, 사용자 입력 |
| 문제 5 | 딕셔너리 집계, 반복문, 난수, 최댓값 |

Quiz 문서는 전체 Python 학습 문서가 완성된 뒤 `04_Python/Quiz/`에서 별도로 제작합니다.

---

# 3. 딕셔너리란?

딕셔너리(dictionary)는 데이터를 `키(key): 값(value)`의 쌍으로 저장하는 자료형입니다.

```python
user = {
    "name": "홍길동",
    "job": "개발자",
}
```

각 항목은 다음 구조를 가집니다.

```text
키 → 값
```

예:

```text
"name" → "홍길동"
"job"  → "개발자"
```

딕셔너리의 자료형은 `dict`입니다.

```python
print(type(user))
```

출력:

```text
<class 'dict'>
```

---

# 4. 딕셔너리의 특징

| 특징 | 설명 |
| --- | --- |
| 키와 값 저장 | 데이터를 이름과 값의 관계로 표현한다. |
| 키 중복 불가 | 같은 키를 여러 번 작성하면 마지막 값이 남는다. |
| 값 중복 가능 | 여러 키가 같은 값을 가질 수 있다. |
| 변경 가능 | 항목을 추가·수정·삭제할 수 있다. |
| 키로 조회 | 숫자 위치보다 의미 있는 이름으로 값을 가져온다. |
| 삽입 순서 보존 | 현대 Python에서는 추가한 순서를 유지한다. |

리스트는 위치 중심입니다.

```python
user = ["홍길동", "개발자"]
```

딕셔너리는 의미 중심입니다.

```python
user = {
    "name": "홍길동",
    "job": "개발자",
}
```

---

# 5. 빈 딕셔너리 생성

공통 원본:

```python
a = {}
a = dict()

print(type(a))
```

출력:

```text
<class 'dict'>
```

두 방식 모두 빈 딕셔너리를 만듭니다.

```python
empty1 = {}
empty2 = dict()
```

일반적으로 단순한 빈 딕셔너리에는 `{}`를 자주 사용합니다.

---

# 6. 빈 집합과 구분

```python
empty = {}
```

이 값은 빈 집합이 아니라 빈 딕셔너리입니다.

빈 집합은 다음처럼 만듭니다.

```python
empty_set = set()
```

자료형 비교:

```python
print(type({}))
print(type(set()))
```

출력:

```text
<class 'dict'>
<class 'set'>
```

---

# 7. 딕셔너리 리터럴

공통 원본의 기본 형태:

```python
b = {
    "이름": "홍길동",
    "직업": "도적",
}
```

기본 문법:

```python
dictionary = {
    key1: value1,
    key2: value2,
}
```

항목은 쉼표로 구분합니다.

---

# 8. 문자열 키와 따옴표

내 코드 주석:

```python
# key는 javascript와 다르게 ''를 써줘야 함
```

딕셔너리 리터럴에서 문자열 키는 문자열이므로 따옴표를 사용합니다.

```python
user = {
    "name": "홍길동",
}
```

따옴표가 없으면 Python은 변수를 찾습니다.

```python
name = "이름"

user = {
    name: "홍길동",
}
```

이 경우 실제 키는 변수 `name`의 값인 `"이름"`입니다.

---

# 9. 키는 문자열만 가능한가?

내 코드에는 “웬만해선 str”이라는 주석이 있습니다.

실무에서 문자열 키가 매우 흔하지만 딕셔너리 키가 반드시 문자열일 필요는 없습니다.

```python
data = {
    1: "첫 번째",
    (10, 20): "좌표",
    True: "참",
}
```

딕셔너리 키는 해시 가능한 객체여야 합니다.

대표적으로 사용할 수 있는 키:

- 문자열
- 정수
- 실수
- 튜플
- `frozenset`
- 일부 불변 객체

---

# 10. 리스트는 키로 사용할 수 없다

```python
data = {
    [1, 2]: "값",
}
```

오류:

```text
TypeError: unhashable type: 'list'
```

리스트는 변경 가능한 자료형이므로 딕셔너리 키로 사용할 수 없습니다.

이 개념은 Quiz의 `unhashable type: 'dict'` 오류와도 연결됩니다.

---

# 11. 딕셔너리도 키로 사용할 수 없다

```python
data = {
    {"id": 1}: "사용자",
}
```

오류:

```text
TypeError: unhashable type: 'dict'
```

딕셔너리도 변경 가능하므로 해시할 수 없습니다.

---

# 12. 중복 키

강사님 원본:

```python
b = {
    "이름": "호랑이심장",
    "직업": "마법사",
    "직업": "마법사2",
}
```

같은 `"직업"` 키가 두 번 작성되었습니다.

결과:

```python
print(b)
```

```text
{'이름': '호랑이심장', '직업': '마법사2'}
```

뒤에 작성된 값이 앞의 값을 덮어씁니다.

---

# 13. 중복 키는 두 항목으로 유지되지 않는다

```python
data = {
    "a": 10,
    "a": 20,
}
```

길이:

```python
print(len(data))
```

출력:

```text
1
```

키는 고유해야 합니다.

---

# 14. 값은 중복 가능

```python
users = {
    "user1": "일반",
    "user2": "일반",
    "user3": "관리자",
}
```

값 `"일반"`은 여러 키에서 사용할 수 있습니다.

딕셔너리의 고유성 제약은 키에 적용됩니다.

---

# 15. 중첩 딕셔너리

공통 원본:

```python
b = {
    "이름": "홍길동",
    "직업": "도적",
    "스킬": {
        "공격": "훔치기",
        "방어": "도망가기",
        "javascript": "중",
    },
}
```

`"스킬"` 키의 값이 또 다른 딕셔너리입니다.

구조:

```text
b
├─ 이름 → 홍길동
├─ 직업 → 도적
└─ 스킬
   ├─ 공격 → 훔치기
   ├─ 방어 → 도망가기
   └─ javascript → 중
```

---

# 16. `dict()`로 생성

공통 원본:

```python
c = dict(a=10, b=20)

print(c)
```

출력:

```text
{'a': 10, 'b': 20}
```

키워드 인자 방식에서는 키 이름이 자동으로 문자열 키가 됩니다.

```python
dict(name="홍길동", age=30)
```

---

# 17. 키워드 인자 방식의 제한

다음과 같은 문자열은 키워드 인자 이름으로 직접 사용할 수 없습니다.

```text
공백이 있는 키
하이픈이 있는 키
숫자로 시작하는 키
Python 문법상 유효하지 않은 식별자
```

이런 키는 딕셔너리 리터럴을 사용합니다.

```python
data = {
    "user-name": "홍길동",
    "1st": "첫 번째",
}
```

---

# 18. 키와 값 쌍으로 `dict()` 생성

```python
pairs = [
    ("name", "홍길동"),
    ("age", 30),
]

user = dict(pairs)

print(user)
```

출력:

```text
{'name': '홍길동', 'age': 30}
```

이 방식은 원본에는 직접 등장하지 않는 보충 학습입니다.

---

# 19. 대괄호로 값 조회

공통 원본:

```python
print(b["이름"])
```

딕셔너리는 인덱스 번호 대신 키를 사용해 값을 조회합니다.

```python
dictionary[key]
```

출력:

```text
홍길동
```

---

# 20. 점 표기법은 사용할 수 없다

원본 주석:

```python
# b.이름
```

일반 Python 딕셔너리는 JavaScript 객체처럼 점 표기법으로 키를 조회하지 않습니다.

```python
b.이름
```

은 일반 딕셔너리 키 접근 문법이 아닙니다.

다음처럼 사용합니다.

```python
b["이름"]
```

---

# 21. 존재하지 않는 키와 `KeyError`

공통 원본의 주석 처리된 코드:

```python
# print(b["이름2"])
```

실행하면:

```text
KeyError: '이름2'
```

대괄호 조회는 해당 키가 반드시 존재해야 합니다.

---

# 22. `get()`으로 값 조회

공통 원본:

```python
print(b.get("이름"))
```

출력:

```text
홍길동
```

`get()`의 기본 구조:

```python
dictionary.get(key)
```

키가 있으면 해당 값을 반환합니다.

---

# 23. 없는 키와 `get()`

공통 원본:

```python
print(b.get("이름2"))
```

출력:

```text
None
```

대괄호 접근과 달리 `KeyError`가 발생하지 않습니다.

---

# 24. `get()`의 기본값

공통 원본:

```python
print(b.get("이름2", "이름없음"))
```

출력:

```text
이름없음
```

기본 구조:

```python
dictionary.get(key, default)
```

키가 없으면 두 번째 인자를 반환합니다.

---

# 25. `[]`와 `get()` 비교

| 방식 | 키가 있을 때 | 키가 없을 때 |
| --- | --- | --- |
| `data[key]` | 값 반환 | `KeyError` |
| `data.get(key)` | 값 반환 | `None` |
| `data.get(key, default)` | 값 반환 | 기본값 반환 |

키가 반드시 있어야 하는 데이터라면 `[]`가 오류를 빠르게 드러냅니다.

키가 선택 사항이라면 `get()`이 편리합니다.

---

# 26. `get()`이 항상 더 안전한 것은 아니다

내 코드 주석은 `get()`을 “더 안전한 방법”이라고 설명합니다.

하지만 `get()`이 오류를 숨길 수도 있습니다.

```python
price = product.get("가격")
total = price * 3
```

`"가격"` 키가 없으면 `price`는 `None`이고 이후 연산에서 다른 `TypeError`가 발생할 수 있습니다.

필수 키는 대괄호 접근이 더 적합할 수 있습니다.

---

# 27. 키는 있지만 값이 `None`인 경우

```python
data = {
    "name": None,
}
```

```python
print(data.get("name"))
print(data.get("missing"))
```

둘 다 `None`을 반환합니다.

키 존재 여부를 정확히 구분하려면:

```python
"name" in data
"missing" in data
```

를 사용합니다.

---

# 28. 중첩 딕셔너리 대괄호 접근

공통 원본:

```python
print(b["스킬"]["공격"])
```

접근 순서:

```text
b["스킬"]
→ 내부 딕셔너리

b["스킬"]["공격"]
→ 내부 딕셔너리의 "공격" 값
```

---

# 29. 단계별 접근

원본:

```python
d = b["스킬"]
d["공격"]
```

의미 있는 변수로 바꾸면:

```python
skills = b["스킬"]
attack = skills["공격"]
```

단계를 나누면 디버깅하기 쉽습니다.

---

# 30. 중첩 `get()`

공통 원본:

```python
print(b.get("스킬").get("공격"))
```

`"스킬"` 키가 존재하고 값이 딕셔너리일 때 정상 동작합니다.

---

# 31. 중첩 `get()`의 위험

내 코드의 주석 처리된 예:

```python
# b.get("스킬2").get("공격")
```

`"스킬2"`가 없으면 첫 `get()`은 `None`을 반환합니다.

이후:

```python
None.get("공격")
```

을 호출하게 되어 다음 오류가 발생합니다.

```text
AttributeError: 'NoneType' object has no attribute 'get'
```

---

# 32. 빈 딕셔너리를 기본값으로 사용

공통 원본:

```python
print(
    b.get("스킬2", {}).get("공격", 0)
)
```

처리 과정:

```text
스킬2가 있으면 그 값을 사용
없으면 빈 딕셔너리 {} 사용
빈 딕셔너리에서 공격을 조회
없으면 0 반환
```

최종 결과:

```text
0
```

---

# 33. 기본값 `{}` 사용 시 주의

다음 방식은 조회만 할 때는 유용합니다.

```python
data.get("child", {}).get("value")
```

그러나 반환된 빈 딕셔너리에 값을 넣어도 원본에 자동 저장되지 않습니다.

```python
data = {}

child = data.get("child", {})
child["value"] = 10

print(data)
```

출력:

```text
{}
```

원본에 실제 중첩 딕셔너리를 만들려면 별도 대입이나 `setdefault()`가 필요합니다.

---

# 34. 값 수정

공통 원본:

```python
b["직업"] = "전사"
```

기존 키가 있으면 값이 수정됩니다.

```python
print(b)
```

`"직업"`의 이전 값은 새 값으로 교체됩니다.

---

# 35. 새 키 추가

공통 원본:

```python
b["직업2"] = "전사2"
```

해당 키가 없으면 새 항목이 추가됩니다.

```text
기존 키 → 값 수정
없는 키 → 새 항목 추가
```

같은 문법이 두 기능을 수행합니다.

---

# 36. 중첩 딕셔너리에 항목 추가

내 코드에는 주석 처리된 예가 있습니다.

```python
# b["스킬"]["버프"] = "힐"
```

실행하면 `"스킬"` 내부 딕셔너리에 새 키가 추가됩니다.

```python
b["스킬"]["버프"] = "힐"
```

---

# 37. `in`은 키를 검사한다

공통 원본:

```python
print("스킬" in b)
```

딕셔너리에서 `in`은 기본적으로 키의 존재 여부를 검사합니다.

```python
key in dictionary
```

---

# 38. 값이 아니라 키 검사

강사님 원본:

```python
print("공격" in b)
```

최상위 딕셔너리 `b`에는 `"공격"` 키가 없습니다.

`"공격"`은 `"스킬"` 내부 딕셔너리의 키입니다.

따라서 결과는:

```text
False
```

---

# 39. 중첩 키 검사

공통 원본:

```python
print("공격" in b["스킬"])
```

출력:

```text
True
```

검사 대상 딕셔너리를 정확히 선택해야 합니다.

---

# 40. `not in`

공통 원본:

```python
print("공격" not in b["스킬"])
```

출력:

```text
False
```

`"공격"` 키가 존재하기 때문입니다.

---

# 41. 값 포함 여부 확인

값을 확인하려면 `values()`를 사용할 수 있습니다.

```python
user = {
    "name": "홍길동",
    "job": "전사",
}

print("홍길동" in user.values())
```

단, 값 검색은 키 검색보다 사용 목적을 신중하게 판단해야 합니다.

---

# 42. 키-값 쌍 포함 여부

```python
user = {
    "name": "홍길동",
}

print(
    ("name", "홍길동") in user.items()
)
```

결과:

```text
True
```

---

# 43. `len()`과 딕셔너리

공통 원본:

```python
print(len(b))
```

`len()`은 최상위 키의 개수를 반환합니다.

중첩 딕셔너리 내부의 키까지 모두 합산하지 않습니다.

---

# 44. 중첩 딕셔너리 길이

```python
print(len(b))
print(len(b["스킬"]))
```

첫 번째는 최상위 항목 수, 두 번째는 `"스킬"` 내부 항목 수입니다.

---

# 45. `keys()`

공통 원본:

```python
e = b.keys()

print(e)
```

출력 형태:

```text
dict_keys(['이름', '직업', '스킬', '직업2'])
```

`keys()`는 키를 보여 주는 딕셔너리 뷰 객체를 반환합니다.

---

# 46. 딕셔너리 뷰 객체

`dict_keys`, `dict_values`, `dict_items`는 리스트가 아닙니다.

이 객체들은 원본 딕셔너리의 현재 상태를 보여 주는 뷰입니다.

```python
data = {"a": 1}
keys = data.keys()

data["b"] = 2

print(keys)
```

출력:

```text
dict_keys(['a', 'b'])
```

원본 변경이 뷰에 반영됩니다.

---

# 47. `keys()`를 리스트로 변환

```python
keys_list = list(b.keys())
```

인덱싱이 필요하거나 고정된 복사본이 필요할 때 리스트로 변환할 수 있습니다.

하지만 단순 반복에는 변환할 필요가 없습니다.

```python
for key in b.keys():
    print(key)
```

---

# 48. `values()`

공통 원본:

```python
f = b.values()

print(f)
```

출력 형태:

```text
dict_values([...])
```

딕셔너리의 값들을 보여 주는 뷰입니다.

---

# 49. 뷰 객체 인덱싱 불가

원본 주석 처리된 코드:

```python
# print(f[0])
```

실행하면:

```text
TypeError: 'dict_values' object is not subscriptable
```

딕셔너리 뷰 객체는 리스트 인덱싱을 지원하지 않습니다.

---

# 50. 리스트로 변환 후 인덱싱

공통 원본:

```python
print(list(f)[0])
```

`values()` 결과를 리스트로 만든 뒤 첫 값을 가져옵니다.

단, 딕셔너리에서 특정 값이 필요하다면 키로 직접 접근하는 것이 더 명확한 경우가 많습니다.

---

# 51. `items()`

공통 원본:

```python
g = b.items()

print(g)
```

출력 형태:

```text
dict_items([
    ('이름', '홍길동'),
    ('직업', '전사'),
    ...
])
```

각 항목을 `(key, value)` 튜플 형태로 제공합니다.

---

# 52. `keys()`, `values()`, `items()` 비교

| 메서드 | 제공 내용 | 각 요소 형태 |
| --- | --- | --- |
| `keys()` | 키 | 키 객체 |
| `values()` | 값 | 값 객체 |
| `items()` | 키와 값 | `(키, 값)` 튜플 |

---

# 53. 키 순서

현대 Python의 딕셔너리는 삽입 순서를 보존합니다.

```python
data = {
    "a": 1,
    "b": 2,
    "c": 3,
}
```

일반적으로 순회하면 `a`, `b`, `c` 순서가 유지됩니다.

그러나 딕셔너리를 정렬 자료형처럼 오해하면 안 됩니다.

자동으로 키의 크기순이나 가나다순으로 정렬하지 않습니다.

---

# 54. 집합 생성

공통 원본:

```python
a = "hello"

print(set(a))
```

문자열의 각 문자를 집합의 원소로 만듭니다.

중복된 `"l"`은 하나만 남습니다.

---

# 55. 집합의 특징

| 특징 | 설명 |
| --- | --- |
| 중복 제거 | 같은 원소는 하나만 유지 |
| 해시 가능한 원소 | 리스트나 딕셔너리는 원소로 사용 불가 |
| 위치 인덱싱 없음 | `set[0]` 형태 사용 불가 |
| 집합 연산 | 합집합, 교집합, 차집합 지원 |

원본에서 집합은 문자열 중복 제거 예제로 짧게 등장합니다.

---

# 56. 집합은 순서를 보장하지 않는다

원본 주석:

```python
# 중복은 제거하지만 순서는 중요하지 않음
```

학습 관점에서 정확한 핵심입니다.

집합의 출력 순서를 데이터의 의미로 사용하면 안 됩니다.

```python
set("hello")
```

출력 순서는 실행 환경에 따라 다르게 보일 수 있습니다.

---

# 57. “JSON 키값이 set으로 관리” 표현 수정

내 코드 주석:

```python
# jason key값이 set으로 관리되기 때문에 중복 없음
```

이 설명은 수정이 필요합니다.

- `JSON`의 철자는 `JSON`입니다.
- Python 딕셔너리의 키가 집합 객체로 저장된다고 설명하는 것은 정확하지 않습니다.
- 딕셔너리와 집합은 모두 해시 기반 구조라는 공통점이 있습니다.
- 딕셔너리는 키와 값을 저장하고 집합은 원소만 저장합니다.

정확한 표현:

```text
딕셔너리 키와 집합 원소는 해시 기반으로 관리되며 중복을 허용하지 않는다.
```

---

# 58. 리스트와 집합 변환

원본:

```python
print(list(a))
print(set(a))
```

문자열 `"hello"` 기준:

```text
list
→ ['h', 'e', 'l', 'l', 'o']

set
→ 중복이 제거된 문자 집합
```

리스트는 순서와 중복을 유지하고 집합은 중복을 제거합니다.

---

# 59. `update()`

공통 원본:

```python
b.update(
    이름="타이거",
    직업="호랑이",
)
```

기존 키는 값이 변경됩니다.

```text
이름 → 타이거
직업 → 호랑이
```

---

# 60. `update()`로 새 키 추가

공통 원본:

```python
b.update(
    이름="타이거",
    직업="호랑이",
    나이="30",
)
```

`"나이"` 키가 없으므로 새 항목으로 추가됩니다.

`update()`도 기존 키 수정과 새 키 추가를 모두 수행합니다.

---

# 61. `update()`에 딕셔너리 전달

```python
user = {
    "name": "홍길동",
}

user.update({
    "name": "김철수",
    "age": 30,
})
```

결과:

```python
{
    "name": "김철수",
    "age": 30,
}
```

키워드 인자보다 자유로운 문자열 키를 사용할 수 있습니다.

---

# 62. `update()`와 직접 대입 비교

단일 키:

```python
user["name"] = "김철수"
```

여러 키:

```python
user.update({
    "name": "김철수",
    "age": 30,
})
```

의도와 항목 수에 따라 선택합니다.

---

# 63. `update()`의 반환값

```python
result = user.update({"age": 30})

print(result)
```

출력:

```text
None
```

`update()`는 원본 딕셔너리를 변경하고 일반적으로 `None`을 반환합니다.

---

# 64. `pop()`

공통 원본:

```python
c = b.pop("나이")
```

`pop(key)`는 키와 항목을 삭제하고 삭제된 값을 반환합니다.

```text
삭제 대상 키 → 나이
반환값 → 해당 나이 값
```

---

# 65. `pop()` 후 원본과 반환값

공통 원본:

```python
print(b)
print(c)
```

딕셔너리에서는 `"나이"` 항목이 사라지고 `c`에는 삭제된 값이 저장됩니다.

---

# 66. 없는 키와 `pop()`

주석 처리된 원본:

```python
# c = b.pop("나이")
```

이미 삭제된 키를 다시 기본값 없이 삭제하면:

```text
KeyError: '나이'
```

가 발생합니다.

---

# 67. `pop()`의 기본값

공통 원본:

```python
c = b.pop("나이", 0)

print(c)
```

키가 없으면 두 번째 인자인 `0`을 반환합니다.

이때 딕셔너리는 변경되지 않습니다.

---

# 68. 인자 없는 `pop()` 불가

원본 주석:

```python
# c = b.pop()
```

딕셔너리의 `pop()`은 삭제할 키가 필요합니다.

리스트의 `pop()`과 다릅니다.

```text
list.pop()
→ 기본적으로 마지막 요소 삭제 가능

dict.pop()
→ 키 인자 필요
```

---

# 69. `popitem()`

공통 원본:

```python
c = b.popitem()
```

`popitem()`은 키-값 한 쌍을 삭제하고 튜플로 반환합니다.

```python
(key, value)
```

---

# 70. `popitem()`의 삭제 순서

내 코드 주석에는 “임의의 키-값 쌍”이라고 되어 있습니다.

현대 Python에서는 `popitem()`이 마지막에 삽입된 항목을 제거합니다.

```text
LIFO
Last In, First Out
```

따라서 “임의”라고 설명하면 현재 Python 동작과 맞지 않습니다.

---

# 71. 빈 딕셔너리와 `popitem()`

```python
data = {}

data.popitem()
```

오류:

```text
KeyError: 'popitem(): dictionary is empty'
```

---

# 72. `del`로 항목 삭제

원본에는 직접 등장하지 않지만 딕셔너리 항목을 삭제할 수 있습니다.

```python
user = {
    "name": "홍길동",
    "age": 30,
}

del user["age"]
```

없는 키를 삭제하면 `KeyError`가 발생합니다.

---

# 73. `clear()`

```python
user.clear()
```

딕셔너리의 모든 항목을 삭제합니다.

딕셔너리 객체 자체는 유지됩니다.

---

# 74. `dict.fromkeys()`

공통 원본:

```python
a = ["a", "b", "c"]

c = dict.fromkeys(a)

print(c)
```

출력:

```text
{'a': None, 'b': None, 'c': None}
```

리스트의 각 요소를 키로 사용하고 기본값은 `None`입니다.

---

# 75. `fromkeys()`에 기본값 지정

```python
keys = ["a", "b", "c"]

data = dict.fromkeys(keys, 0)

print(data)
```

출력:

```text
{'a': 0, 'b': 0, 'c': 0}
```

---

# 76. 직접 생성과 `fromkeys()` 비교

원본은 세 가지 과정을 보여 줍니다.

직접 리터럴:

```python
b = {
    "a": 0,
    "b": 0,
    "c": 0,
}
```

하나씩 대입:

```python
b = {}
b[a[0]] = 0
b[a[1]] = 0
```

한 번에 생성:

```python
c = dict.fromkeys(a)
```

---

# 77. `fromkeys()`와 변경 가능한 기본값 주의

```python
data = dict.fromkeys(
    ["a", "b", "c"],
    [],
)
```

세 키가 같은 리스트 객체를 공유합니다.

```python
data["a"].append(1)

print(data)
```

결과:

```text
{
    'a': [1],
    'b': [1],
    'c': [1],
}
```

각 키마다 독립적인 리스트가 필요하면 컴프리헨션을 사용합니다.

```python
data = {
    key: []
    for key in ["a", "b", "c"]
}
```

---

# 78. 딕셔너리 직접 순회

공통 원본:

```python
for i in c:
    print(i)
    print(c[i])
```

딕셔너리를 직접 순회하면 키가 하나씩 나옵니다.

```text
i → 키
c[i] → 해당 키의 값
```

---

# 79. 의미 있는 반복 변수명

원본:

```python
for i in c:
```

개선:

```python
for key in c:
```

딕셔너리를 직접 순회할 때 값이 아니라 키가 나온다는 점이 변수명에 드러납니다.

---

# 80. `keys()`는 생략 가능

다음 두 코드는 같은 키 순회입니다.

```python
for key in data:
    print(key)
```

```python
for key in data.keys():
    print(key)
```

일반적으로 직접 순회가 간결합니다.

---

# 81. `items()` 순회

공통 원본:

```python
for key, value in c.items():
    print(key, value)
```

`items()`의 각 요소는 `(key, value)` 튜플입니다.

반복문에서 바로 언패킹합니다.

---

# 82. `values()` 순회

```python
for value in data.values():
    print(value)
```

값만 필요할 때 사용합니다.

---

# 83. 딕셔너리 언패킹

함수 호출에서 `**`를 사용하면 딕셔너리 키와 값을 키워드 인자로 전달할 수 있습니다.

```python
def print_user(name, age):
    print(name, age)

user = {
    "name": "홍길동",
    "age": 30,
}

print_user(**user)
```

이 내용은 원본에 직접 등장하지 않는 확장 학습입니다.

---

# 84. 딕셔너리 병합 연산자

현대 Python에서는 `|` 연산자로 새 딕셔너리를 만들 수 있습니다.

```python
a = {"x": 1}
b = {"y": 2}

c = a | b
```

같은 키가 있으면 오른쪽 값이 남습니다.

```python
{"x": 1} | {"x": 100}
```

결과:

```text
{'x': 100}
```

원본 범위를 확장한 보충 학습입니다.

---

# 85. `|=`로 갱신

```python
data = {"x": 1}
data |= {"y": 2}
```

원본 딕셔너리에 항목을 병합합니다.

초기 학습에서는 `update()`를 우선 익혀도 충분합니다.

---

# 86. `setdefault()`

```python
data = {}

skills = data.setdefault(
    "스킬",
    {},
)

skills["공격"] = "훔치기"

print(data)
```

출력:

```text
{'스킬': {'공격': '훔치기'}}
```

키가 없으면 기본값을 실제 딕셔너리에 저장하고 그 값을 반환합니다.

---

# 87. `get()`과 `setdefault()` 차이

```python
data.get("스킬", {})
```

은 기본값을 반환할 뿐 원본에 추가하지 않습니다.

```python
data.setdefault("스킬", {})
```

은 키가 없으면 기본값을 원본에 추가합니다.

---

# 88. 딕셔너리 컴프리헨션

```python
numbers = [1, 2, 3]

squares = {
    number: number ** 2
    for number in numbers
}

print(squares)
```

출력:

```text
{1: 1, 2: 4, 3: 9}
```

기본 구조:

```python
{
    key_expression: value_expression
    for item in iterable
}
```

---

# 89. 조건이 있는 딕셔너리 컴프리헨션

```python
numbers = range(10)

even_squares = {
    number: number ** 2
    for number in numbers
    if number % 2 == 0
}
```

원본의 `fromkeys()`와 반복문 학습을 확장한 개념입니다.

---

# 90. 딕셔너리 복사

```python
original = {
    "name": "홍길동",
}

copied = original.copy()
```

바깥 딕셔너리는 새 객체입니다.

```python
print(original is copied)
print(original == copied)
```

출력:

```text
False
True
```

---

# 91. 얕은 복사

```python
original = {
    "skills": {
        "attack": "훔치기",
    },
}

copied = original.copy()

copied["skills"]["attack"] = "베기"

print(original)
```

중첩 딕셔너리는 공유될 수 있습니다.

`copy()`는 얕은 복사입니다.

---

# 92. 딕셔너리 키와 해시

딕셔너리는 키를 이용해 값을 빠르게 찾기 위해 해시 구조를 사용합니다.

키는 저장된 동안 해시값과 동등성 규칙이 안정적이어야 합니다.

따라서 리스트와 딕셔너리 같은 가변 객체는 키로 사용할 수 없습니다.

---

# 93. 튜플 키

튜플 내부 요소가 모두 해시 가능하면 딕셔너리 키로 사용할 수 있습니다.

```python
seats = {
    (1, 1): "예약",
    (1, 2): "가능",
}
```

좌표나 복합 식별자를 표현할 때 유용합니다.

---

# 94. Boolean과 정수 키 주의

Python에서:

```python
True == 1
False == 0
```

이므로 다음 키는 충돌할 수 있습니다.

```python
data = {
    True: "참",
    1: "하나",
}
```

실제로 하나의 키처럼 처리됩니다.

이 내용은 해시와 동등성의 확장 주의점입니다.

---

# 95. 실무 활용 예제: 사용자 정보

```python
user = {
    "id": "admin",
    "name": "관리자",
    "active": True,
    "roles": [
        "ADMIN",
        "USER",
    ],
}
```

하나의 대상에 대한 서로 다른 속성을 이름으로 저장할 수 있습니다.

---

# 96. 실무 활용 예제: 장바구니

강사님 Quiz 2의 구조:

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
}
```

최상위 키는 상품명이고 값은 상품 상세 딕셔너리입니다.

상세 계산과 풀이 문서는 최종 Quiz 단계에서 다룹니다.

---

# 97. 실무 활용 예제: 설정값

```python
config = {
    "host": "localhost",
    "port": 8000,
    "debug": True,
}
```

키 이름을 통해 각 값의 의미가 분명해집니다.

---

# 98. 실무 활용 예제: 빈도 집계

```python
votes = [
    "a",
    "b",
    "a",
    "c",
    "a",
]

counts = {}

for candidate in votes:
    counts[candidate] = (
        counts.get(candidate, 0) + 1
    )

print(counts)
```

강사님 Quiz 5의 투표 집계와 연결되는 핵심 패턴입니다.

상세 문제 문서화는 Quiz 단계에서 진행합니다.

---

# 99. 실무 활용 예제: 로그인 데이터

강사님 Quiz 4 구조:

```python
users = {
    "admin": "1234",
    "guest": "guest",
    "user1": "abcd",
}
```

키는 사용자 ID, 값은 비밀번호입니다.

실제 서비스에서는 비밀번호를 평문으로 저장하지 않습니다.

현재 예제는 딕셔너리 조회와 조건문 학습을 위한 교육용 구조입니다.

---

# 100. 내 코드와 강사님 코드 공통점

두 코드 모두 다음 내용을 포함합니다.

- `{}`와 `dict()`로 빈 딕셔너리 생성
- 중첩 딕셔너리 선언
- `dict(a=10, b=20)`
- 대괄호 키 조회
- 없는 키의 `KeyError` 예제
- `get()`
- `get()` 기본값
- 중첩 딕셔너리 조회
- 빈 딕셔너리를 이용한 중첩 기본값
- 기존 값 수정
- 새 키 추가
- `in`, `not in`
- `len()`
- `keys()`
- `values()`
- `items()`
- 문자열을 리스트와 집합으로 변환
- `update()`
- `pop()`
- `pop()` 기본값
- `popitem()`
- `dict.fromkeys()`
- 딕셔너리 키 순회
- `items()` 언패킹 순회

---

# 101. 내 코드와 강사님 코드 차이

| 비교 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 기본 캐릭터 | 홍길동·도적 | 호랑이심장·마법사 |
| 중복 키 실험 | 주석으로 설명 | `"직업"` 키를 실제 중복 선언 |
| 키 설명 | 문자열 키와 JavaScript 비교 | 별도 설명 없음 |
| 없는 키 오류 | `KeyError` 이름 주석 | 코드만 주석 처리 |
| `get()` 설명 | 안전한 방법이라고 표현 | 없음과 기본값 중심 |
| 중첩 `get()` 오류 | `NoneType` 오류 예제 주석 | 오류 예제 없음 |
| 중첩 포함 검사 | `b.get("스킬")` 검사 추가 | 최상위 `"공격" in b` 추가 |
| 집합 설명 | JSON 키와 연결한 부정확한 주석 | 중복 제거·순서 비보장 설명 |
| `update()` 나이 값 | 문자열 `"30"` | 정수 `20` |
| `popitem()` 설명 | 임의 항목 삭제라고 표현 | 설명 없음 |
| 반복 변수명 | `key`, `value` | `k`, `v` |
| Quiz 문제 | 없음 | 문제 1~5 포함 |

---

# 102. 내 코드의 장점

- 딕셔너리 키에 문자열을 사용할 때의 문법을 주석으로 설명했습니다.
- 중복 키가 있을 때 뒤의 값이 남는다는 점을 기록했습니다.
- 없는 키를 대괄호로 조회했을 때 `KeyError`가 발생함을 명시했습니다.
- `get()`의 `None` 반환과 기본값 사용을 비교했습니다.
- 중첩 `get()`에서 `NoneType` 오류가 발생하는 상황을 기록했습니다.
- 빈 딕셔너리 기본값으로 오류를 피하는 방법을 작성했습니다.
- 기존 키 수정과 새 키 추가를 구분했습니다.
- 딕셔너리 뷰 객체를 리스트로 바꿔 인덱싱하는 과정을 확인했습니다.
- 집합을 이용해 문자열 중복 제거를 실험했습니다.
- `pop()`의 기본값과 인자 없는 호출 오류를 기록했습니다.
- `dict.fromkeys()`와 직접 생성 방식을 비교했습니다.
- 반복 변수명을 `key`, `value`로 작성해 강사님 코드보다 의미가 명확합니다.

---

# 103. 내 코드의 개선점

- 딕셔너리 키는 반드시 문자열만 가능한 것이 아닙니다.
- `get()`을 항상 더 안전하다고 설명하면 필수 키 누락을 숨길 수 있습니다.
- 딕셔너리 뷰를 “유사배열”이라고 표현하기보다 뷰 객체라고 설명해야 합니다.
- 집합 출력 순서를 예시 그대로 고정된 결과처럼 기록하면 안 됩니다.
- “JSON 키값이 set으로 관리된다”는 설명은 부정확합니다.
- `JSON` 철자를 `jason`으로 작성한 오타를 수정해야 합니다.
- `popitem()`은 현대 Python에서 마지막 삽입 항목을 제거하므로 임의 삭제라고 설명하면 안 됩니다.
- 나이 값 `"30"`은 숫자 계산이 필요하다면 정수 `30`이 더 적합합니다.
- `d["공격"]`과 `b["스킬"]["공격"]`은 반환값을 사용하지 않아 실행 효과가 보이지 않습니다.
- 변수 `a`, `b`, `c`, `d`가 여러 자료형으로 계속 재사용되어 흐름 추적이 어렵습니다.
- `b = {}` 이후 일부 키만 추가한 딕셔너리를 출력하지 않아 중간 결과가 보이지 않습니다.
- 주석 처리된 `"버프"` 추가 예제를 실제 출력과 함께 분리하면 이해하기 쉽습니다.

---

# 104. 강사님 코드의 장점

- 실제 중복 키를 선언해 뒤의 값이 남는 동작을 보여 줍니다.
- 딕셔너리 생성부터 조회·수정·삭제·반복까지 학습 순서가 자연스럽습니다.
- 최상위 키와 중첩 키의 `in` 결과 차이를 코드로 확인합니다.
- 집합의 중복 제거와 순서 비보장을 정확한 방향으로 설명합니다.
- `update()`, `pop()`, `popitem()`, `fromkeys()`까지 핵심 메서드를 폭넓게 포함합니다.
- 마지막에 관련 문제 1~5를 제시해 조건문과 반복문 학습으로 연결합니다.
- 전체 코드가 내 코드보다 간결해 수업 진행 흐름을 빠르게 파악할 수 있습니다.

---

# 105. 강사님 코드의 개선점

- 중복 `"직업"` 키의 첫 번째 값이 사라지는 이유를 명시적으로 설명하지 않습니다.
- 없는 키의 `KeyError` 이름과 발생 이유가 없습니다.
- `get()`을 중첩 호출할 때 첫 결과가 `None`인 경우를 설명하지 않습니다.
- 리스트와 딕셔너리를 키로 사용할 수 없는 해시 가능성 설명이 없습니다.
- `keys()`, `values()`, `items()`가 뷰 객체라는 설명이 없습니다.
- `popitem()`의 현대 Python 삭제 순서를 설명하지 않습니다.
- `fromkeys()`의 기본값이 `None`이라는 점만 결과로 확인되고 공유 가변값 문제는 다루지 않습니다.
- 딕셔너리의 삽입 순서 보존을 설명하지 않습니다.
- 비밀번호 평문 저장 예제가 실무 보안 방식이 아니라는 구분이 없습니다.
- Quiz 문제의 정답과 상세 해설은 포함되어 있지 않습니다.

---

# 106. 정확하게 수정한 원본 주석

기존:

```python
# key는 javascript와 다르게 ''를 써줘야 함
# (웬만해선 str)
```

개선:

```python
# 문자열 키는 따옴표로 작성한다.
# 딕셔너리 키는 문자열 외에도
# 해시 가능한 불변 객체를 사용할 수 있다.
```

기존:

```python
# get으로 받을 경우 None이 나옴, 더 안전한 방법
```

개선:

```python
# get()은 키가 없을 때 KeyError 대신
# None 또는 지정한 기본값을 반환한다.
# 필수 키인지 선택 키인지에 따라 []와 get()을 선택한다.
```

기존:

```python
# 배열이 아니기 때문에 못 씀
```

개선:

```python
# dict_values는 리스트가 아닌 딕셔너리 뷰 객체이므로
# 정수 인덱싱을 지원하지 않는다.
```

기존:

```python
# jason key값이 set으로 관리되기 때문에 중복 없음
```

개선:

```python
# 딕셔너리 키와 집합 원소는 해시 기반으로 관리되며
# 중복을 허용하지 않는다.
```

기존:

```python
# popitem으로 임의의 키-값 쌍으로 삭제
```

개선:

```python
# 현대 Python의 popitem()은
# 마지막에 삽입된 키-값 쌍을 삭제하고 반환한다.
```

---

# 107. 개선된 대표 코드

```python
user = {
    "name": "홍길동",
    "job": "도적",
    "skills": {
        "attack": "훔치기",
        "defense": "도망가기",
    },
}

print(user["name"])
print(user.get("age"))
print(user.get("age", 0))

attack = (
    user
    .get("skills", {})
    .get("attack", "없음")
)

print(attack)

user["job"] = "전사"
user["level"] = 10

print(user)
```

---

# 108. 개선된 순회 코드

```python
user = {
    "name": "홍길동",
    "job": "전사",
    "level": 10,
}

for key in user:
    print(key, user[key])

for key, value in user.items():
    print(key, value)
```

---

# 109. 개선된 집계 코드

```python
votes = [
    "a",
    "b",
    "a",
    "c",
    "a",
    "b",
]

counts = {}

for candidate in votes:
    counts[candidate] = (
        counts.get(candidate, 0) + 1
    )

print(counts)
```

이 패턴은 강사님 Quiz 5와 연결됩니다.

---

# 110. 자주 하는 실수: 집합과 빈 딕셔너리 혼동

```python
data = {}
```

은 빈 딕셔너리입니다.

빈 집합:

```python
data = set()
```

---

# 111. 자주 하는 실수: 키 따옴표 누락

```python
user = {
    name: "홍길동",
}
```

`name` 변수가 정의되어 있지 않으면 `NameError`가 발생합니다.

문자열 키:

```python
user = {
    "name": "홍길동",
}
```

---

# 112. 자주 하는 실수: 중복 키 유지 기대

```python
data = {
    "job": "마법사",
    "job": "전사",
}
```

두 항목이 아니라 마지막 값 하나만 남습니다.

---

# 113. 자주 하는 실수: 점 표기법 사용

```python
user.name
```

일반 딕셔너리 키 조회가 아닙니다.

```python
user["name"]
```

을 사용합니다.

---

# 114. 자주 하는 실수: 없는 키 대괄호 조회

```python
user["age"]
```

키가 없으면 `KeyError`입니다.

선택값이라면:

```python
user.get("age")
```

를 사용할 수 있습니다.

---

# 115. 자주 하는 실수: `get()` 결과를 바로 딕셔너리라고 가정

```python
user.get("skills").get("attack")
```

`"skills"`가 없으면 `NoneType` 오류가 발생합니다.

```python
user.get("skills", {}).get("attack")
```

처럼 처리할 수 있습니다.

---

# 116. 자주 하는 실수: `get(..., {})` 결과 수정

```python
data.get("child", {})["value"] = 10
```

`"child"`가 없으면 임시 빈 딕셔너리만 수정되고 원본에는 저장되지 않습니다.

---

# 117. 자주 하는 실수: `in`으로 값 검색

```python
"name" in user
```

은 키 검색입니다.

값 검색:

```python
"홍길동" in user.values()
```

---

# 118. 자주 하는 실수: `values()[0]`

```python
user.values()[0]
```

뷰 객체는 인덱싱할 수 없습니다.

```python
list(user.values())[0]
```

로 변환할 수 있지만 가능하면 키로 직접 조회합니다.

---

# 119. 자주 하는 실수: `update()` 결과 대입

```python
user = user.update({
    "age": 30,
})
```

`update()` 반환값이 `None`이므로 `user`가 `None`이 됩니다.

개선:

```python
user.update({
    "age": 30,
})
```

---

# 120. 자주 하는 실수: `pop()` 인자 생략

```python
user.pop()
```

딕셔너리 `pop()`에는 키가 필요합니다.

```python
user.pop("age")
```

---

# 121. 자주 하는 실수: 없는 키 `pop()`

```python
user.pop("age")
```

키가 없으면 `KeyError`입니다.

기본값:

```python
user.pop("age", None)
```

---

# 122. 자주 하는 실수: `popitem()`을 무작위 삭제로 이해

현대 Python에서는 마지막 삽입 항목을 제거합니다.

삭제 순서가 중요한 로직이라면 이 동작을 명확히 알고 사용해야 합니다.

---

# 123. 자주 하는 실수: `fromkeys()`의 공유 리스트

```python
data = dict.fromkeys(
    ["a", "b"],
    [],
)
```

두 키가 같은 리스트를 공유합니다.

독립 값:

```python
data = {
    key: []
    for key in ["a", "b"]
}
```

---

# 124. 자주 하는 실수: 리스트를 키로 사용

```python
data = {
    [1, 2]: "value",
}
```

오류:

```text
TypeError: unhashable type: 'list'
```

---

# 125. 자주 하는 실수: 딕셔너리 집합 생성

```python
cart = {
    {
        "상품명": "사과",
    },
    {
        "상품명": "바나나",
    },
}
```

바깥 `{}`가 집합으로 해석되고 내부 딕셔너리는 해시할 수 없으므로 다음 오류가 발생합니다.

```text
TypeError: unhashable type: 'dict'
```

여러 딕셔너리를 순서대로 저장하려면 리스트를 사용합니다.

```python
cart = [
    {
        "상품명": "사과",
    },
    {
        "상품명": "바나나",
    },
]
```

---

# 126. 자주 하는 실수: 숫자를 문자열로 저장

```python
product = {
    "price": "1000",
    "quantity": "3",
}
```

출력만 할 때는 가능하지만 계산 전에 형 변환이 필요합니다.

```python
total = (
    int(product["price"])
    * int(product["quantity"])
)
```

처음부터 계산용 데이터라면 숫자로 저장하는 편이 자연스럽습니다.

---

# 127. 면접·복습 질문 1

## 딕셔너리란 무엇인가?

딕셔너리는 데이터를 고유한 키와 값의 쌍으로 저장하는 변경 가능한 자료형입니다. 위치 인덱스 대신 키를 사용해 값을 조회합니다.

---

# 128. 면접·복습 질문 2

## 같은 키를 여러 번 작성하면 어떻게 되는가?

마지막에 작성하거나 대입한 값이 이전 값을 덮어씁니다. 딕셔너리에서 하나의 키는 하나의 값과 연결됩니다.

---

# 129. 면접·복습 질문 3

## `data[key]`와 `data.get(key)`의 차이는 무엇인가?

`data[key]`는 키가 없으면 `KeyError`를 발생시킵니다. `get()`은 키가 없으면 `None` 또는 지정한 기본값을 반환합니다.

---

# 130. 면접·복습 질문 4

## 딕셔너리에서 `in`은 무엇을 검사하는가?

기본적으로 키의 존재 여부를 검사합니다. 값을 검사하려면 `values()`, 키와 값 쌍을 검사하려면 `items()`를 사용할 수 있습니다.

---

# 131. 면접·복습 질문 5

## `keys()`, `values()`, `items()`는 무엇을 반환하는가?

딕셔너리의 현재 상태를 반영하는 뷰 객체를 반환합니다. `items()`의 각 요소는 키와 값을 가진 튜플입니다.

---

# 132. 면접·복습 질문 6

## 어떤 객체를 딕셔너리 키로 사용할 수 있는가?

해시 가능하고 동등성 규칙이 안정적인 객체를 사용할 수 있습니다. 문자열, 숫자, 해시 가능한 튜플 등이 대표적이며 리스트와 딕셔너리는 사용할 수 없습니다.

---

# 133. 면접·복습 질문 7

## `pop()`과 `popitem()`의 차이는 무엇인가?

`pop(key)`는 지정한 키의 항목을 삭제하고 값을 반환합니다. `popitem()`은 마지막 삽입 항목을 삭제하고 `(key, value)` 튜플을 반환합니다.

---

# 134. 면접·복습 질문 8

## `dict.fromkeys()`의 주의점은 무엇인가?

모든 키에 같은 값 객체를 사용합니다. 변경 가능한 리스트나 딕셔너리를 기본값으로 지정하면 여러 키가 같은 객체를 공유할 수 있습니다.

---

# 135. 면접·복습 질문 9

## 딕셔너리를 직접 `for` 문으로 순회하면 무엇이 나오는가?

키가 나옵니다. 값을 얻으려면 `data[key]`, 키와 값을 함께 얻으려면 `data.items()`를 사용합니다.

---

# 136. 면접·복습 질문 10

## 집합과 딕셔너리의 공통점과 차이는 무엇인가?

둘 다 해시 기반이며 중복 키 또는 원소를 허용하지 않습니다. 딕셔너리는 키와 값을 저장하고 집합은 원소만 저장합니다.

---

# 137. Problems

## 문제 1

빈 딕셔너리를 두 가지 방법으로 생성하세요.

---

## 문제 2

이름과 직업을 저장하는 딕셔너리를 작성하세요.

```text
이름: 홍길동
직업: 개발자
```

---

## 문제 3

다음 딕셔너리에서 `"name"` 값을 대괄호로 출력하세요.

```python
user = {
    "name": "홍길동",
    "age": 30,
}
```

---

## 문제 4

다음 딕셔너리에서 없는 `"email"` 키를 `get()`으로 조회하세요.

```python
user = {
    "name": "홍길동",
}
```

---

## 문제 5

없는 `"email"` 키를 조회할 때 `"없음"`을 반환하도록 작성하세요.

---

## 문제 6

다음 중첩 딕셔너리에서 공격 스킬을 출력하세요.

```python
user = {
    "skills": {
        "attack": "베기",
        "defense": "막기",
    },
}
```

---

## 문제 7

`"skills"` 키가 없을 수도 있을 때 공격 스킬을 조회하고 없으면 `"없음"`을 출력하세요.

---

## 문제 8

다음 딕셔너리의 직업을 `"전사"`로 수정하세요.

```python
user = {
    "name": "홍길동",
    "job": "도적",
}
```

---

## 문제 9

다음 딕셔너리에 `"level": 10`을 추가하세요.

---

## 문제 10

다음 딕셔너리에 `"name"` 키가 있는지 출력하세요.

```python
user = {
    "name": "홍길동",
}
```

---

## 문제 11

다음 딕셔너리에 값 `"홍길동"`이 있는지 출력하세요.

---

## 문제 12

다음 딕셔너리의 최상위 키 개수를 출력하세요.

```python
user = {
    "name": "홍길동",
    "age": 30,
    "job": "개발자",
}
```

---

## 문제 13

다음 딕셔너리의 키 뷰를 출력하세요.

---

## 문제 14

다음 딕셔너리의 값 뷰를 출력하세요.

---

## 문제 15

다음 딕셔너리의 키와 값 쌍을 출력하세요.

---

## 문제 16

`update()`를 사용해 이름을 `"김철수"`로 수정하고 나이 `30`을 추가하세요.

```python
user = {
    "name": "홍길동",
}
```

---

## 문제 17

다음 딕셔너리에서 `"age"`를 삭제하고 삭제된 값을 출력하세요.

```python
user = {
    "name": "홍길동",
    "age": 30,
}
```

---

## 문제 18

없는 `"email"` 키를 `pop()`하되 오류 없이 `"없음"`을 반환하세요.

---

## 문제 19

다음 키 리스트로 모든 값이 `0`인 딕셔너리를 만드세요.

```python
keys = ["a", "b", "c"]
```

---

## 문제 20

다음 딕셔너리의 키와 값을 반복문으로 함께 출력하세요.

```python
user = {
    "name": "홍길동",
    "age": 30,
}
```

---

## 문제 21

문자열 `"hello"`를 집합으로 변환해 중복 문자를 제거하세요.

---

## 문제 22

1부터 5까지 숫자를 키로, 제곱값을 값으로 가진 딕셔너리를 컴프리헨션으로 만드세요.

---

## 문제 23

다음 투표 목록을 딕셔너리로 집계하세요.

```python
votes = [
    "a",
    "b",
    "a",
    "c",
    "a",
]
```

---

## 문제 24

다음 코드가 오류를 발생시키는 이유를 설명하세요.

```python
data = {
    [1, 2]: "value",
}
```

---

## 문제 25

다음 잘못된 장바구니 구조를 올바른 리스트 구조로 수정하세요.

```python
cart = {
    {
        "name": "사과",
        "price": 1000,
    },
    {
        "name": "바나나",
        "price": 2000,
    },
}
```

---

# 138. Answers

## 정답 1

```python
a = {}
b = dict()
```

---

## 정답 2

```python
user = {
    "이름": "홍길동",
    "직업": "개발자",
}
```

---

## 정답 3

```python
user = {
    "name": "홍길동",
    "age": 30,
}

print(user["name"])
```

---

## 정답 4

```python
user = {
    "name": "홍길동",
}

print(user.get("email"))
```

---

## 정답 5

```python
print(
    user.get("email", "없음")
)
```

---

## 정답 6

```python
user = {
    "skills": {
        "attack": "베기",
        "defense": "막기",
    },
}

print(
    user["skills"]["attack"]
)
```

---

## 정답 7

```python
attack = (
    user
    .get("skills", {})
    .get("attack", "없음")
)

print(attack)
```

---

## 정답 8

```python
user = {
    "name": "홍길동",
    "job": "도적",
}

user["job"] = "전사"

print(user)
```

---

## 정답 9

```python
user["level"] = 10
```

---

## 정답 10

```python
user = {
    "name": "홍길동",
}

print("name" in user)
```

---

## 정답 11

```python
print(
    "홍길동" in user.values()
)
```

---

## 정답 12

```python
user = {
    "name": "홍길동",
    "age": 30,
    "job": "개발자",
}

print(len(user))
```

---

## 정답 13

```python
print(user.keys())
```

---

## 정답 14

```python
print(user.values())
```

---

## 정답 15

```python
print(user.items())
```

---

## 정답 16

```python
user = {
    "name": "홍길동",
}

user.update({
    "name": "김철수",
    "age": 30,
})

print(user)
```

---

## 정답 17

```python
user = {
    "name": "홍길동",
    "age": 30,
}

removed_age = user.pop("age")

print(user)
print(removed_age)
```

---

## 정답 18

```python
result = user.pop(
    "email",
    "없음",
)

print(result)
```

---

## 정답 19

```python
keys = ["a", "b", "c"]

data = dict.fromkeys(
    keys,
    0,
)

print(data)
```

---

## 정답 20

```python
user = {
    "name": "홍길동",
    "age": 30,
}

for key, value in user.items():
    print(key, value)
```

---

## 정답 21

```python
letters = set("hello")

print(letters)
```

집합의 출력 순서는 고정적으로 가정하지 않습니다.

---

## 정답 22

```python
squares = {
    number: number ** 2
    for number in range(1, 6)
}

print(squares)
```

---

## 정답 23

```python
votes = [
    "a",
    "b",
    "a",
    "c",
    "a",
]

counts = {}

for candidate in votes:
    counts[candidate] = (
        counts.get(candidate, 0) + 1
    )

print(counts)
```

---

## 정답 24

리스트는 변경 가능한 자료형이므로 해시할 수 없습니다. 딕셔너리 키는 해시 가능한 객체여야 하므로 `TypeError: unhashable type: 'list'`가 발생합니다.

---

## 정답 25

```python
cart = [
    {
        "name": "사과",
        "price": 1000,
    },
    {
        "name": "바나나",
        "price": 2000,
    },
]

print(cart)
```

여러 딕셔너리를 순서대로 저장하려면 바깥 자료형으로 리스트를 사용합니다.

---

# 139. Final Checklist

- [ ] `{}`와 `dict()`로 빈 딕셔너리를 만들 수 있다.
- [ ] 빈 `{}`가 집합이 아니라 딕셔너리임을 안다.
- [ ] 키와 값의 쌍으로 딕셔너리를 선언할 수 있다.
- [ ] 문자열 키에 따옴표를 사용할 수 있다.
- [ ] 딕셔너리 키가 반드시 문자열일 필요는 없음을 안다.
- [ ] 키가 해시 가능해야 함을 설명할 수 있다.
- [ ] 리스트와 딕셔너리를 키로 사용할 수 없음을 안다.
- [ ] 중복 키에서 마지막 값이 남는다는 점을 안다.
- [ ] 딕셔너리 값은 중복될 수 있음을 안다.
- [ ] 중첩 딕셔너리를 작성할 수 있다.
- [ ] `dict(a=10)` 방식의 특징과 제한을 안다.
- [ ] 대괄호로 키의 값을 조회할 수 있다.
- [ ] 일반 딕셔너리에서 점 표기법을 사용하지 않음을 안다.
- [ ] 없는 키의 대괄호 조회가 `KeyError`를 발생시킴을 안다.
- [ ] `get()`과 기본값을 사용할 수 있다.
- [ ] 필수 키와 선택 키에 따라 `[]`와 `get()`을 선택할 수 있다.
- [ ] 키가 존재하지만 값이 `None`인 경우와 키 부재를 구분할 수 있다.
- [ ] 중첩 딕셔너리의 값을 조회할 수 있다.
- [ ] 중첩 `get()`에서 `NoneType` 오류가 발생하는 이유를 안다.
- [ ] 빈 딕셔너리 기본값 조회의 한계를 안다.
- [ ] 기존 키의 값을 수정할 수 있다.
- [ ] 없는 키를 새 항목으로 추가할 수 있다.
- [ ] 중첩 딕셔너리에 새 항목을 추가할 수 있다.
- [ ] 딕셔너리의 `in`이 키를 검사함을 안다.
- [ ] `values()`와 `items()`로 다른 포함 검사를 할 수 있다.
- [ ] `len()`이 최상위 키 개수를 반환함을 안다.
- [ ] `keys()`, `values()`, `items()`를 구분할 수 있다.
- [ ] 딕셔너리 뷰 객체가 리스트가 아님을 안다.
- [ ] 뷰 객체가 원본 변경을 반영함을 이해한다.
- [ ] 딕셔너리의 삽입 순서 보존을 설명할 수 있다.
- [ ] 집합이 중복을 제거함을 안다.
- [ ] 집합 출력 순서를 의존하지 않아야 함을 안다.
- [ ] 딕셔너리와 집합의 공통점과 차이를 설명할 수 있다.
- [ ] `update()`로 수정과 추가를 할 수 있다.
- [ ] `update()`가 `None`을 반환함을 안다.
- [ ] `pop()`으로 키를 삭제하고 값을 받을 수 있다.
- [ ] `pop()`의 기본값을 사용할 수 있다.
- [ ] 딕셔너리 `pop()`에는 키 인자가 필요함을 안다.
- [ ] `popitem()`이 마지막 삽입 항목을 삭제함을 안다.
- [ ] `del`과 `clear()`로 항목을 삭제할 수 있다.
- [ ] `dict.fromkeys()`를 사용할 수 있다.
- [ ] 변경 가능한 기본값 공유 문제를 설명할 수 있다.
- [ ] 딕셔너리를 직접 순회하면 키가 나옴을 안다.
- [ ] `items()`로 키와 값을 함께 순회할 수 있다.
- [ ] `setdefault()`와 `get()`의 차이를 설명할 수 있다.
- [ ] 딕셔너리 컴프리헨션을 작성할 수 있다.
- [ ] 딕셔너리 복사가 얕은 복사임을 안다.
- [ ] `unhashable type: 'dict'` 오류 원인을 설명할 수 있다.
- [ ] 강사님 원본 Quiz 문제들이 어떤 개념과 연결되는지 안다.
- [ ] Quiz 상세 문서화는 최종 단계에서 진행됨을 확인했다.

---

# 140. Key Summary

```text
dict
→ 키와 값의 쌍을 저장
→ 키는 중복 불가
→ 값은 중복 가능
→ 변경 가능한 자료형
```

빈 딕셔너리:

```python
a = {}
b = dict()
```

기본 선언:

```python
user = {
    "name": "홍길동",
    "age": 30,
}
```

조회:

```python
user["name"]
user.get("name")
user.get("email", "없음")
```

```text
[]
→ 키가 없으면 KeyError

get()
→ 키가 없으면 None 또는 기본값
```

중첩 조회:

```python
user["skills"]["attack"]

user.get(
    "skills",
    {},
).get(
    "attack",
    "없음",
)
```

수정과 추가:

```python
user["age"] = 31
user["job"] = "개발자"
```

포함 여부:

```python
"name" in user
"홍길동" in user.values()
("name", "홍길동") in user.items()
```

뷰 객체:

```python
user.keys()
user.values()
user.items()
```

갱신:

```python
user.update({
    "age": 31,
    "job": "개발자",
})
```

삭제:

```python
user.pop("age")
user.pop("email", None)
user.popitem()
del user["job"]
user.clear()
```

여러 키 생성:

```python
dict.fromkeys(
    ["a", "b", "c"],
    0,
)
```

순회:

```python
for key in user:
    print(key, user[key])

for key, value in user.items():
    print(key, value)
```

집합:

```python
set("hello")
```

```text
중복 제거
순서에 의존하지 않음
해시 가능한 원소만 저장
```

딕셔너리는 값의 위치보다 의미를 이름으로 표현하는 자료형입니다. 사용자 정보, 상품 정보, 설정값, 집계 결과처럼 각 값에 명확한 역할이 있을 때 매우 유용합니다.
