---
title: Python 문자열과 포매팅
version: v2.0-final
last_updated: 2026-08-06
status: Completed
---

# Python 문자열과 포매팅

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `03_Python_문자열과_포매팅.md` |
| 분류 | `04_Python` |
| 원본 기준 | `workspace_python/03_string.py`, `workspace_teacher/workspace_python/_03_string.py` |
| 핵심 범위 | 문자열 생성, 이스케이프, 문자열 연결, f-string, `format()`, `%` 포매팅, 문자열 메서드, 분리·결합, 대소문자, 공백 제거, 숫자·정렬 포맷 |
| 실습 범위 | 온도 메시지, HTML 문자열, 문자열 검색, 치환, 목록 결합, 검색 정규화, 숫자 표시 |
| 문서 형식 | Python Developer-Wiki V2 확정 형식 |

> 이 문서는 내 코드와 강사님 코드 전체를 한 번에 나열하지 않는다.  
> 문자열 생성·출력·검색·변환·포매팅에 필요한 코드만 발췌하고, 실행 결과와 사용 목적을 함께 설명한다.

---

# 개요

문자열은 이름, 이메일, 게시글 제목, 상품 설명처럼 문자로 이루어진 데이터를 표현한다.

```text
사용자 이름
상품명
주소
메시지
HTML 코드
로그 내용
    ↓
문자열로 저장
```

문자열을 다룰 때는 단순히 값을 저장하는 것뿐 아니라 다음 작업이 필요하다.

```text
문자열 만들기
    ↓
값 삽입하기
    ↓
길이 확인하기
    ↓
검색·치환하기
    ↓
분리·결합하기
    ↓
공백·대소문자 정리하기
    ↓
출력 형식 맞추기
```

> [!IMPORTANT]
> 문자열은 사용자 입력, 파일 내용, 웹 데이터, 데이터베이스 값에서 계속 만나게 되는 핵심 자료형이다.

---

# 핵심 개념

| 개념 | 핵심 역할 |
| --- | --- |
| 문자열 | 문자 데이터를 저장하는 자료형 |
| 이스케이프 문자 | 따옴표·줄바꿈 등 특수 문자를 표현 |
| 문자열 연결 | 여러 문자열을 하나로 결합 |
| f-string | 문자열 안에 변수와 표현식을 삽입 |
| `format()` | 위치 또는 이름을 이용한 문자열 포매팅 |
| `%` 포매팅 | 오래된 문자열 포매팅 방식 |
| 문자열 메서드 | 검색·치환·분리·결합·정리 기능 |
| `len()` | 문자열 길이 반환 |
| `find()` | 일치 위치 반환, 없으면 `-1` |
| `index()` | 일치 위치 반환, 없으면 예외 |
| `split()` | 문자열을 목록으로 분리 |
| `join()` | 문자열 목록을 하나로 결합 |
| 포맷 지정자 | 자리수·정렬·소수점·천 단위 형식 지정 |

---

# 학습 목표

이 문서를 학습한 뒤 다음 내용을 설명하고 작성할 수 있어야 한다.

- 작은따옴표와 큰따옴표로 문자열을 만들 수 있다.
- 여러 줄 문자열을 작성할 수 있다.
- 이스케이프 문자로 따옴표를 표현할 수 있다.
- 문자열과 숫자를 연결할 때 형 변환이 필요한 이유를 설명할 수 있다.
- f-string으로 변수값을 문자열에 삽입할 수 있다.
- `format()`과 `%` 포매팅의 기본 사용법을 이해한다.
- `len()`, `count()`, `find()`, `index()`, `rfind()`를 사용할 수 있다.
- `replace()`, `split()`, `join()`을 사용할 수 있다.
- 문자열은 변경 불가능한 자료형이라는 점을 이해한다.
- `upper()`, `lower()`, `strip()`, `zfill()`을 사용할 수 있다.
- f-string 포맷 지정자로 정렬과 자리수를 조절할 수 있다.
- 실수의 소수점 자리와 천 단위 구분 기호를 출력할 수 있다.

---

# 1. 작은따옴표와 큰따옴표

## 1-1. 내 코드

```python
a = 'hello'
b = "world"
```

## 1-2. 강사님 코드

```python
a = 'hello'
b = "wolrd"
```

강사님 코드의 `"wolrd"`는 `"world"`의 오타로 보인다. 문자열 문법에는 문제가 없지만 실제 값은 의도와 다르다.

## 1-3. 실행

```python
a = "hello"
b = "world"

print(a)
print(b)
```

## 1-4. 출력 결과

```text
hello
world
```

| 요소 | 의미 |
| --- | --- |
| `a`, `b` | 문자열을 저장하는 변수 |
| `'hello'` | 작은따옴표 문자열 |
| `"world"` | 큰따옴표 문자열 |

> [!TIP]
> 작은따옴표와 큰따옴표는 같은 문자열을 만들 수 있다. 프로젝트 안에서는 한 가지 스타일을 정해 일관되게 사용하는 것이 좋다.

---

# 2. 여러 줄 문자열

## 2-1. 내 코드

```python
c = '''여기에
여러 줄
넣을 수 있다'''

d = """여러 줄
쌉 가능"""
```

## 2-2. 강사님 코드

```python
c = '''여기에
여러 줄
넣을 수 있다'''

d = """여러 줄
가능"""
```

## 2-3. 실행

```python
message = """첫 번째 줄
두 번째 줄
세 번째 줄"""

print(message)
```

## 2-4. 출력 결과

```text
첫 번째 줄
두 번째 줄
세 번째 줄
```

> [!IMPORTANT]
> 따옴표 3개는 실제 여러 줄 주석 문법이 아니라 여러 줄 문자열이다. 함수나 클래스의 첫 문장에 놓이면 Docstring으로 사용될 수 있다.

---

# 3. 이스케이프 문자

## 3-1. 원본 코드

```python
text = 'he\'s name is "name"'
```

## 3-2. 실행

```python
text = 'He\'s name is "Min-su".'

print(text)
```

## 3-3. 출력 결과

```text
He's name is "Min-su".
```

| 표현 | 의미 |
| --- | --- |
| `\'` | 작은따옴표 문자 |
| `\"` | 큰따옴표 문자 |
| `\\` | 백슬래시 문자 |
| `\n` | 줄바꿈 |
| `\t` | 탭 |

---

# 4. 문자열과 숫자 연결 오류

## 4-1. 오류 예제

```python
temperature = 32.5
message = "지금 온도는 " + temperature + "도 입니다."
```

## 4-2. 발생 결과

```text
TypeError
```

문자열과 실수는 `+`로 바로 연결할 수 없다.

## 4-3. `str()`로 변환

```python
temperature = 32.5

message = (
    "지금 온도는 "
    + str(temperature)
    + "도 입니다."
)

print(message)
```

## 4-4. 출력 결과

```text
지금 온도는 32.5도 입니다.
```

---

# 5. f-string

## 5-1. 내 코드

```python
temperature = 32.5
message = f"지금 온도는 {temperature}도 입니다."

print(message)
```

## 5-2. 강사님 코드

```python
temperature = 32.5
message = f"지금 온도는 {temperature}도 입니다"

print(message)
```

## 5-3. 출력 결과

```text
지금 온도는 32.5도 입니다.
```

| 코드 | 사용하는 이유 |
| --- | --- |
| `f"..."` | f-string 시작 |
| `{temperature}` | 변수값 삽입 |
| `message` | 완성된 문자열 저장 |

> [!TIP]
> 현재 Python 코드에서는 문자열 포매팅에 f-string을 가장 먼저 고려하는 경우가 많다.

---

# 6. f-string 안의 표현식

```python
unit_price = 45000
quantity = 2

message = (
    f"총 금액은 "
    f"{unit_price * quantity:,}원입니다."
)

print(message)
```

## 6-1. 출력 결과

```text
총 금액은 90,000원입니다.
```

메서드 호출도 가능하다.

```python
user_name = "kim"

print(f"사용자: {user_name.upper()}")
```

출력:

```text
사용자: KIM
```

---

# 7. `format()` 메서드

## 7-1. 내 코드와 강사님 코드

```python
temperature = 32.5

message = (
    "지금 온도는 {0}도 입니다"
    .format(temperature)
)

print(message)
```

## 7-2. 출력 결과

```text
지금 온도는 32.5도 입니다
```

여러 값도 넣을 수 있다.

```python
message = (
    "{0}님의 점수는 {1}점입니다."
    .format("Kim", 95)
)

print(message)
```

출력:

```text
Kim님의 점수는 95점입니다.
```

---

# 8. 여러 줄 f-string

```python
temperature = 32.5

html = f'''
<div>
    지금 온도는 {temperature}도 입니다
</div>
'''

print(html)
```

## 8-1. 출력 결과

```text

<div>
    지금 온도는 32.5도 입니다
</div>
```

여러 줄 메시지, HTML 템플릿, SQL 문장 등에 활용할 수 있다.

> [!WARNING]
> 사용자 입력을 SQL 문장에 직접 삽입하면 위험하다. 데이터베이스에서는 문자열 포매팅 대신 파라미터 바인딩을 사용한다.

---

# 9. `%` 문자열 포매팅

## 9-1. 정수 형식 `%d`

```python
temperature = 32.5

message = (
    "지금 온도는 %d도 입니다"
    % temperature
)

print(message)
```

출력:

```text
지금 온도는 32도 입니다
```

## 9-2. 실수 형식 `%f`

```python
temperature = 32.5

message = (
    "지금 온도는 %f도 입니다"
    % temperature
)

print(message)
```

출력:

```text
지금 온도는 32.500000도 입니다
```

| 기호 | 의미 |
| --- | --- |
| `%s` | 문자열 |
| `%d` | 정수 |
| `%f` | 실수 |

> [!TIP]
> `%` 포매팅은 기존 코드에서 볼 수 있으므로 읽는 법은 알아두되, 새 코드에서는 f-string을 우선 고려한다.

---

# 10. 문자열 포매팅 방식 비교

| 방식 | 예시 | 특징 |
| --- | --- | --- |
| 문자열 연결 | `"온도: " + str(value)` | 형 변환을 직접 해야 함 |
| `%` 포매팅 | `"온도: %f" % value` | 오래된 코드에서 자주 보임 |
| `format()` | `"온도: {}".format(value)` | 위치·이름 지정 가능 |
| f-string | `f"온도: {value}"` | 간결하고 값 위치가 명확함 |

---

# 11. `len()`으로 문자열 길이 확인

```python
text = "_hello"

print(len(text))
```

## 11-1. 출력 결과

```text
6
```

`_`, `h`, `e`, `l`, `l`, `o` 총 6글자다.

---

# 12. `count()`

```python
text = "_hello"

print(text.count("l"))
```

## 12-1. 출력 결과

```text
2
```

문자열도 셀 수 있다.

```python
print("banana".count("an"))
```

출력:

```text
2
```

---

# 13. `find()`

```python
text = "_hello"

print(text.find("l"))
print(text.find("z"))
```

## 13-1. 출력 결과

```text
3
-1
```

```text
_ h e l l o
0 1 2 3 4 5
```

`find()`는 값이 없으면 `-1`을 반환한다.

---

# 14. `index()`

```python
text = "_hello"

print(text.index("l"))
```

## 14-1. 출력 결과

```text
3
```

없는 값을 찾으면 다음 예외가 발생한다.

```text
ValueError: substring not found
```

| 메서드 | 찾았을 때 | 없을 때 |
| --- | --- | --- |
| `find()` | 인덱스 반환 | `-1` |
| `index()` | 인덱스 반환 | `ValueError` |

---

# 15. `rfind()`

```python
text = "_hello"

print(text.rfind("l"))
```

## 15-1. 출력 결과

```text
4
```

`find()`는 첫 번째 위치, `rfind()`는 마지막 위치를 반환한다.

---

# 16. `replace()`

```python
text = "_hello"

result = text.replace(
    "l",
    "w",
)

print(result)
```

## 16-1. 출력 결과

```text
_hewwo
```

교체 횟수를 제한할 수도 있다.

```python
result = text.replace(
    "l",
    "w",
    1,
)

print(result)
```

출력:

```text
_hewlo
```

---

# 17. 문자열은 변경 불가능하다

```python
text = "hello"

changed_text = text.replace(
    "h",
    "H",
)

print(text)
print(changed_text)
```

## 17-1. 출력 결과

```text
hello
Hello
```

문자열 메서드는 기존 문자열을 직접 변경하지 않고 새 문자열을 반환한다.

---

# 18. `split()`

```python
sentence = (
    "그럼 저기서 하나만 "
    "바꾸고 싶으면요?"
)

words = sentence.split()

print(words)
```

## 18-1. 출력 결과

```text
['그럼', '저기서', '하나만', '바꾸고', '싶으면요?']
```

특정 구분자를 사용할 수도 있다.

```python
date = "2026-08-06"

print(date.split("-"))
```

출력:

```text
['2026', '08', '06']
```

---

# 19. 리스트 언패킹

```python
numbers = [1, 2, 3]

first, second, third = numbers

print(first)
print(second)
print(third)
```

## 19-1. 출력 결과

```text
1
2
3
```

변수 개수와 값 개수가 다르면 `ValueError`가 발생한다.

---

# 20. `join()`

```python
letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
]

result = "-".join(letters)

print(result)
```

## 20-1. 출력 결과

```text
a-b-c-d-e
```

숫자 목록은 문자열로 변환해야 한다.

```python
numbers = [1, 2, 3]

result = "-".join(
    str(number)
    for number in numbers
)

print(result)
```

출력:

```text
1-2-3
```

---

# 21. `split()`과 `join()` 연결

```python
letters = [
    "a",
    "b",
    "c",
]

joined = "-".join(letters)
split_result = joined.split("-")

print(joined)
print(split_result)
```

## 21-1. 출력 결과

```text
a-b-c
['a', 'b', 'c']
```

```text
리스트
    ↓ join()
문자열
    ↓ split()
리스트
```

---

# 22. 대소문자 구분 검색

## 22-1. 내 코드

```python
text = "Don't Look Back is Anger"
position = text.find("back")

print(position)
```

## 22-2. 강사님 코드

```python
text = "Don't Look Back in Anger"
position = text.find("back")

print(position)
```

## 22-3. 출력 결과

```text
-1
```

문자열 검색은 기본적으로 대소문자를 구분한다.

---

# 23. `upper()`와 `lower()`

```python
text = "Don't Look Back in Anger"
keyword = "back"

position = text.lower().find(
    keyword.lower()
)

print(text.upper())
print(position)
```

## 23-1. 출력 결과

```text
DON'T LOOK BACK IN ANGER
11
```

> [!TIP]
> 검색 전에 입력값과 기준값을 모두 소문자 또는 대문자로 맞추면 대소문자 차이를 줄일 수 있다.

---

# 24. `casefold()`

```python
text = "Python"
keyword = "PYTHON"

print(
    text.casefold()
    == keyword.casefold()
)
```

## 24-1. 출력 결과

```text
True
```

국제 문자를 포함한 대소문자 정규화에는 `casefold()`가 더 적합할 수 있다.

---

# 25. `strip()`

## 25-1. 내 코드

```python
text = "   a b   "

print(text.strip())
```

## 25-2. 강사님 코드

```python
text = "  a b  "

print(text.strip())
```

## 25-3. 출력 결과

```text
a b
```

양쪽 공백만 제거되고 문자열 내부 공백은 유지된다.

---

# 26. 모든 공백 제거

```python
text = "   a b   "

result = (
    text.strip()
    .replace(" ", "")
)

print(result)
```

## 26-1. 출력 결과

```text
ab
```

탭과 줄바꿈까지 포함한 공백 문자를 제거하려면 다음처럼 작성할 수 있다.

```python
text = " a\tb\nc "

result = "".join(
    text.split()
)

print(result)
```

출력:

```text
abc
```

---

# 27. `lstrip()`과 `rstrip()`

```python
text = "   Python   "

print(text.lstrip())
print(text.rstrip())
```

| 메서드 | 제거 위치 |
| --- | --- |
| `strip()` | 양쪽 |
| `lstrip()` | 왼쪽 |
| `rstrip()` | 오른쪽 |

---

# 28. `zfill()`

```python
print("35".zfill(4))
print("35000".zfill(4))
```

## 28-1. 출력 결과

```text
0035
35000
```

지정한 길이보다 짧을 때만 왼쪽을 `0`으로 채운다.

---

# 29. f-string 자리수 지정

```python
number = 7

print(f"{number:03}")
print(f"..{number:3}..")
```

## 29-1. 출력 결과

```text
007
..  7..
```

| 표현 | 의미 |
| --- | --- |
| `:03` | 전체 3자리, 빈 자리를 0으로 채움 |
| `:3` | 전체 3자리, 기본 오른쪽 정렬 |

---

# 30. f-string 정렬

```python
number = 7

print(f"..{number:<3}..")
print(f"..{number:>3}..")
print(f"..{number:^10}..")
```

## 30-1. 출력 결과

```text
..7  ..
..  7..
..    7     ..
```

| 기호 | 의미 |
| --- | --- |
| `<` | 왼쪽 정렬 |
| `>` | 오른쪽 정렬 |
| `^` | 가운데 정렬 |

---

# 31. 실수 포맷

```python
number = 3.14

print(f"{number:08.3f}")
```

## 31-1. 출력 결과

```text
0003.140
```

```text
0
→ 빈 자리를 0으로 채움

8
→ 전체 너비

.3f
→ 소수점 아래 3자리 실수
```

---

# 32. 천 단위 구분 기호

```python
price = 15000

print(f"{price:,}")
```

## 32-1. 출력 결과

```text
15,000
```

실무형 예:

```python
product_name = "키보드"
price = 45000

print(
    f"{product_name}: "
    f"{price:,}원"
)
```

출력:

```text
키보드: 45,000원
```

---

# 33. 내 코드와 강사님 코드 비교

| 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 문자열 기본 | `hello`, `world` | `hello`, `wolrd` |
| 여러 줄 문자열 | 추가 설명 포함 | 핵심 예제 중심 |
| 이스케이프 | 사용 이유를 주석으로 기록 | 실제 문자열 예제 |
| 문자열 연결 | 오류 이유를 자료형으로 기록 | 정상 코드 중심 |
| f-string | JavaScript 템플릿 문자열과 비교 메모 | 기본 사용 예제 |
| 검색 메서드 | `find`, `index`, `rfind` 차이 메모 | 핵심 차이 표시 |
| 공백 제거 | 내부 공백 제거 예제 추가 | `strip()` 기본 예제 |
| 포맷 지정 | 왼쪽·오른쪽·가운데 정렬 모두 확인 | 기본 정렬 예제 |
| 문자열 결합 | 제너레이터 표현식 추가 | `map()`과 제너레이터 예제 |

## 33-1. 내 코드의 장점

- 메서드 차이를 직접 비교하며 메모했다.
- 문자열과 숫자 연결 오류의 원인을 기록했다.
- 대소문자 검색, 공백 제거, 정렬 포맷을 확장 실습했다.

## 33-2. 내 코드의 개선점

- f-string은 Python의 문자열 포매팅 문법으로 이해해야 한다.
- 따옴표 3개는 메모리에 남기 때문에 주석이 되는 것이 아니다.
- 문자열 메서드는 원본을 직접 변경하지 않는다는 설명이 필요하다.

## 33-3. 강사님 코드의 장점

- 문자열 생성부터 포맷 지정까지 핵심 메서드를 폭넓게 실습한다.
- `map()`과 제너레이터 표현식으로 숫자 결합 방법을 함께 보여 준다.

## 33-4. 강사님 코드의 보충점

- `"wolrd"` 오타를 수정할 필요가 있다.
- 여러 줄 문자열과 주석의 차이를 정확히 설명할 필요가 있다.
- `%d` 사용 시 실수의 소수 부분이 사라지는 점을 설명해야 한다.

---

# 34. 기존 코드에서 개선 코드로 바꾼 이유

## 34-1. 문자열 연결을 f-string으로 개선

기존:

```python
message = (
    "지금 온도는 "
    + str(temperature)
    + "도 입니다."
)
```

개선:

```python
message = (
    f"지금 온도는 "
    f"{temperature}도 입니다."
)
```

## 34-2. 의미 있는 변수명 사용

기존:

```python
a = "Don't Look Back in Anger"
b = a.find("back")
```

개선:

```python
song_title = (
    "Don't Look Back in Anger"
)
keyword_position = (
    song_title.lower()
    .find("back")
)
```

## 34-3. 검색 실패를 안전하게 처리

```python
position = text.find(keyword)

if position == -1:
    print("검색 결과가 없습니다.")
else:
    print("검색 위치:", position)
```

---

# 35. 실무형 예제: 사용자 정보 요약

```python
user_name = " kim "
user_email = "KIM@EXAMPLE.COM"
login_count = 7
point = 15000

normalized_name = (
    user_name.strip().title()
)

normalized_email = (
    user_email.strip().lower()
)

summary = f"""
사용자: {normalized_name}
이메일: {normalized_email}
로그인 횟수: {login_count:03}
포인트: {point:,}점
""".strip()

print(summary)
```

## 35-1. 출력 결과

```text
사용자: Kim
이메일: kim@example.com
로그인 횟수: 007
포인트: 15,000점
```

| 코드 | 사용하는 이유 |
| --- | --- |
| `strip()` | 입력값 양쪽 공백 제거 |
| `title()` | 이름 첫 문자를 대문자로 표시 |
| `lower()` | 이메일 대소문자 정규화 |
| `:03` | 로그인 횟수를 3자리로 표시 |
| `:,` | 포인트에 천 단위 구분 기호 표시 |
| 여러 줄 f-string | 여러 정보를 하나의 문자열로 구성 |

---

# 36. 대표 오류로 이해하기

## 36-1. 문자열과 숫자 연결

```python
print("점수: " + 95)
```

발생 결과:

```text
TypeError
```

개선:

```python
print(f"점수: {95}")
```

## 36-2. 없는 문자열에 `index()`

```python
"hello".index("z")
```

발생 결과:

```text
ValueError
```

## 36-3. 숫자 리스트를 `join()`

```python
"-".join([1, 2, 3])
```

발생 결과:

```text
TypeError
```

## 36-4. 문자열 메서드 결과를 저장하지 않음

```python
text = " hello "
text.strip()

print(text)
```

출력:

```text
 hello 
```

## 36-5. `find()` 결과를 바로 참·거짓으로 사용

```python
position = "Python".find("P")

if position:
    print("찾음")
```

`"P"`의 위치는 `0`이고 `0`은 Falsy이므로 출력되지 않는다.

개선:

```python
if position != -1:
    print("찾음")
```

또는:

```python
if "P" in "Python":
    print("찾음")
```

---

# 37. 자주 하는 실수

## 37-1. 작은따옴표와 큰따옴표를 닫지 않음

`SyntaxError`가 발생한다.

## 37-2. 여러 줄 문자열을 실제 주석으로만 이해

정확히는 문자열 객체다.

## 37-3. 문자열과 숫자를 `+`로 직접 연결

숫자를 문자열로 변환하거나 f-string을 사용한다.

## 37-4. `%d`에 실수를 넣고 소수값이 유지된다고 생각

정수 형식으로 출력되어 소수 부분이 보이지 않는다.

## 37-5. `find()`와 `index()` 실패 동작 혼동

`find()`는 `-1`, `index()`는 예외다.

## 37-6. 문자열 메서드가 원본을 변경한다고 생각

대부분 새 문자열을 반환한다.

## 37-7. `replace()`가 첫 번째 값만 바꾼다고 생각

기본적으로 모든 일치값을 바꾼다.

## 37-8. `split()` 결과를 문자열로 생각

리스트를 반환한다.

## 37-9. 숫자 목록에 `join()`을 바로 사용

모든 항목이 문자열이어야 한다.

## 37-10. 대소문자 차이를 고려하지 않고 검색

양쪽을 `lower()` 또는 `casefold()`로 정규화한다.

## 37-11. `strip()`이 문자열 내부 공백까지 제거한다고 생각

양쪽 공백만 제거한다.

## 37-12. `find()` 결과 `0`을 찾지 못한 것으로 처리

`0`은 문자열 시작 위치다.

## 37-13. 포맷 너비와 소수점 자리수를 혼동

`8.3f`에서 `8`은 전체 너비, `3`은 소수점 아래 자리수다.

---

# 38. 핵심 요약

```text
'문자열'
"문자열"
→ 한 줄 문자열

'''문자열'''
"""문자열"""
→ 여러 줄 문자열

\'
\"
\n
\t
→ 이스케이프 문자
```

```text
f"{value}"
→ f-string

"{}".format(value)
→ format 포매팅

"%s" % value
→ % 포매팅
```

```text
len()
→ 길이

count()
→ 개수

find()
→ 위치 또는 -1

index()
→ 위치 또는 예외

replace()
→ 치환

split()
→ 문자열에서 리스트

join()
→ 리스트에서 문자열
```

```text
upper(), lower()
→ 대소문자 변환

strip()
→ 양쪽 공백 제거

zfill()
→ 앞쪽 0 채우기

:<, :>, :^
→ 정렬

:.2f
→ 소수점 자리

:,
→ 천 단위 구분
```

---

# 39. 최종 체크리스트

- [ ] 작은따옴표와 큰따옴표 문자열을 작성할 수 있는가?
- [ ] 여러 줄 문자열을 작성할 수 있는가?
- [ ] 문자열과 주석의 차이를 이해했는가?
- [ ] 이스케이프 문자로 따옴표를 표현할 수 있는가?
- [ ] 문자열과 숫자 연결 시 형 변환이 필요함을 이해했는가?
- [ ] f-string으로 변수와 표현식을 삽입할 수 있는가?
- [ ] `format()`과 `%` 포매팅을 읽을 수 있는가?
- [ ] `len()`과 `count()`를 사용할 수 있는가?
- [ ] `find()`와 `index()`의 차이를 설명할 수 있는가?
- [ ] `rfind()`로 마지막 위치를 찾을 수 있는가?
- [ ] `replace()` 결과를 저장할 수 있는가?
- [ ] 문자열이 변경 불가능한 자료형임을 이해했는가?
- [ ] `split()`과 `join()`을 사용할 수 있는가?
- [ ] 숫자 목록을 문자열로 변환한 뒤 결합할 수 있는가?
- [ ] 대소문자 구분 없이 검색할 수 있는가?
- [ ] `strip()`과 `lstrip()`·`rstrip()`을 구분할 수 있는가?
- [ ] `zfill()`로 고정 자리 문자열을 만들 수 있는가?
- [ ] f-string으로 정렬과 자리수를 지정할 수 있는가?
- [ ] 실수 소수점 자리와 천 단위 구분 기호를 출력할 수 있는가?
- [ ] `find()` 결과가 `0`일 수 있음을 이해했는가?

---

# 마무리

문자열 처리의 핵심은 단순히 글자를 저장하는 데 있지 않다.

```text
문자열을 만들고
    ↓
필요한 값을 삽입하고
    ↓
검색·치환·분리·결합하고
    ↓
공백과 대소문자를 정리하고
    ↓
사용자에게 읽기 좋은 형식으로 출력하는 것
```

이 흐름을 익히면 사용자 입력, 파일 데이터, 웹 응답, 로그 메시지를 더 안정적으로 처리할 수 있다.
