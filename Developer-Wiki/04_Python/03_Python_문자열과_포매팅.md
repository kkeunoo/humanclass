# Python 문자열과 포매팅

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `03_Python_문자열과_포매팅.md` |
| 분류 | `04_Python` |
| 권장 선수 학습 | `00-01_Python_실행방식과_프로그래밍_패러다임.md`, `00-02_Python_오류와_예외.md`, `01_Python_출력과_주석.md`, `02_Python_변수와_자료형_연산자.md` |
| 다음 학습 | `04_Python_리스트.md` |
| 원본 기준 | `workspace_python/03_string.py`, `workspace_teacher/workspace_python/_03_string.py` |
| 핵심 범위 | 문자열 생성, 이스케이프 문자, 문자열 연결, 포매팅, 길이와 검색, 치환, 분리와 결합, 대소문자 변환, 공백 제거, 숫자 형식 지정 |

> 이 문서는 내 코드의 `03_string.py`와 강사님 코드의 `_03_string.py`를 직접 비교해 작성했습니다. 두 파일은 문자열 생성부터 문자열 포매팅, 검색, 치환, 분리와 결합, 정렬과 숫자 출력 형식까지 다룹니다.

---

# 학습 목표

- 작은따옴표와 큰따옴표로 문자열을 만들 수 있다.
- 따옴표 3개로 여러 줄 문자열을 작성할 수 있다.
- 이스케이프 문자를 사용해 따옴표와 특수 문자를 표현할 수 있다.
- 문자열과 숫자를 연결할 때 형 변환이 필요한 이유를 설명할 수 있다.
- 문자열 연결, f-string, `str.format()`, `%` 포매팅의 차이를 구분할 수 있다.
- `len()`, `count()`, `find()`, `index()`, `rfind()`를 사용할 수 있다.
- `replace()`, `split()`, `join()`의 역할을 설명할 수 있다.
- 문자열이 변경 불가능한 객체라는 의미를 이해한다.
- `upper()`, `lower()`를 이용해 대소문자를 정규화할 수 있다.
- `strip()`으로 양쪽 공백을 제거할 수 있다.
- `zfill()`과 f-string 형식 지정자를 사용할 수 있다.
- 내 코드와 강사님 코드의 차이 및 개선점을 설명할 수 있다.

---

# 1. 원본 코드 범위

두 원본은 다음 흐름으로 구성되어 있습니다.

```text
작은따옴표와 큰따옴표
→ 여러 줄 문자열
→ 따옴표 이스케이프
→ 문자열과 숫자 연결
→ f-string
→ str.format()
→ % 포매팅
→ 문자열 길이
→ 문자 개수와 위치 검색
→ 문자열 치환
→ split()과 구조 분해 대입
→ join()과 split()
→ 대소문자 변환 후 검색
→ strip()
→ zfill()
→ f-string 정렬과 숫자 형식
```

내 코드는 강사님 코드에 비해 각 메서드의 동작과 JavaScript의 `indexOf()`를 연결한 주석을 더 많이 포함합니다.

---

# 2. 문자열이란?

문자열은 문자들이 순서대로 연결된 자료형입니다.

```python
name = "Python"
message = "문자열 학습"
```

Python에서 문자열 자료형은 `str`입니다.

```python
print(type("hello"))
```

출력:

```text
<class 'str'>
```

문자열은 이름, 문장, 파일 경로, HTML 코드, 사용자 입력 등 다양한 텍스트 데이터를 표현할 때 사용합니다.

---

# 3. 작은따옴표와 큰따옴표

공통 원본:

```python
a = 'hello'
b = "world"
```

강사님 코드에는 `world`가 다음처럼 작성되어 있습니다.

```python
b = "wolrd"
```

이는 문자열 문법의 차이가 아니라 단순한 철자 차이입니다.

Python에서는 작은따옴표와 큰따옴표 모두 문자열을 생성합니다.

```python
single = 'hello'
double = "hello"

print(single == double)
```

출력:

```text
True
```

두 방식의 자료형과 값은 같습니다. 프로젝트에서는 한 가지 스타일을 일관되게 사용하는 편이 좋습니다.

---

# 4. 문자열 내부의 따옴표

문자열 바깥과 다른 종류의 따옴표를 사용하면 내부 따옴표를 그대로 작성할 수 있습니다.

```python
message1 = "He's a developer"
message2 = '그는 "Python"을 공부합니다.'
```

바깥과 같은 따옴표를 내부에 넣어야 한다면 이스케이프 문자를 사용할 수 있습니다.

원본 예제:

```python
'he\'s name is \"민수\"'
```

조금 더 자연스럽게 작성하면 다음과 같습니다.

```python
message = 'His name is "민수".'
```

또는:

```python
message = "His name is \"민수\"."
```

---

# 5. 이스케이프 문자

역슬래시 `\` 뒤에 특정 문자를 작성하면 문자열 안에서 특별한 의미를 표현할 수 있습니다.

| 표현 | 의미 |
| --- | --- |
| `\'` | 작은따옴표 |
| `\"` | 큰따옴표 |
| `\\` | 역슬래시 |
| `\n` | 줄바꿈 |
| `\t` | 탭 |
| `\r` | 캐리지 리턴 |

예제:

```python
print("첫 번째 줄\n두 번째 줄")
print("이름\t나이")
```

출력:

```text
첫 번째 줄
두 번째 줄
이름    나이
```

---

# 6. 여러 줄 문자열

공통 원본:

```python
c = '''여기에
여러 줄
넣을 수 있다'''

d = """여러 줄
가능"""
```

따옴표 3개를 사용하면 줄바꿈을 포함한 문자열을 만들 수 있습니다.

```python
message = """첫 번째 줄
두 번째 줄
세 번째 줄"""

print(message)
```

출력:

```text
첫 번째 줄
두 번째 줄
세 번째 줄
```

HTML이나 SQL처럼 여러 줄의 텍스트를 변수에 저장할 때 유용합니다.

---

# 7. 여러 줄 문자열과 주석의 차이

강사님 원본에는 다음 코드가 있습니다.

```python
'''
여러줄
주석으로 사용됨
'''
```

내 코드에도 변수에 넣지 않은 여러 줄 문자열을 주석처럼 사용할 수 있다는 설명이 있습니다.

하지만 따옴표 3개는 문법적으로 여러 줄 주석이 아니라 **문자열 리터럴**입니다.

```python
"""
이 내용도 문자열입니다.
"""
```

코드 어디에도 저장하지 않으면 결과가 사용되지 않아 주석처럼 보일 수 있습니다. 그러나 Python의 실제 주석 문법은 `#`입니다.

```python
# 이것이 Python의 한 줄 주석입니다.
```

함수, 클래스, 모듈의 첫 문자열은 문서 문자열인 docstring으로 사용될 수 있습니다.

```python
def greet():
    """인사말을 출력하는 함수입니다."""
    print("안녕하세요")
```

정리하면 다음과 같습니다.

| 형태 | 실제 의미 |
| --- | --- |
| `# 설명` | 주석 |
| 변수에 저장한 `'''...'''` | 여러 줄 문자열 |
| 함수·클래스·모듈 첫 문자열 | docstring |
| 그 외 단독 문자열 | 실행 중 만들어졌다가 사용되지 않는 문자열 객체 |

---

# 8. Raw String

원본에는 직접 등장하지 않지만 이스케이프 문자와 연결되는 보충 개념입니다.

문자열 앞에 `r`을 붙이면 역슬래시를 대부분 일반 문자처럼 처리합니다.

```python
path = r"C:\new_folder\test"
print(path)
```

출력:

```text
C:\new_folder\test
```

정규 표현식이나 Windows 경로를 표현할 때 자주 사용합니다.

단, raw string도 마지막이 홀수 개의 역슬래시로 끝날 수는 없습니다.

```python
# 잘못된 예
# path = r"C:\folder\"
```

---

# 9. 문자열과 숫자 연결

공통 원본:

```python
b = 32.5
c = "지금 온도는 " + str(b) + "도 입니다."
print(c)
```

출력:

```text
지금 온도는 32.5도 입니다.
```

문자열과 실수를 `+`로 바로 연결할 수는 없습니다.

```python
temperature = 32.5

# TypeError 발생
# message = "현재 온도는 " + temperature
```

예외:

```text
TypeError: can only concatenate str (not "float") to str
```

연결하려면 숫자를 문자열로 변환해야 합니다.

```python
message = "현재 온도는 " + str(temperature) + "도입니다."
```

---

# 10. 문자열 연결 연산자 `+`

`+`는 문자열을 이어 붙입니다.

```python
first = "Hello"
second = "Python"

print(first + " " + second)
```

출력:

```text
Hello Python
```

짧은 문자열 몇 개를 연결할 때는 간단하지만, 변수와 문장이 많아지면 f-string이 더 읽기 쉽습니다.

---

# 11. 문자열 반복 연산자 `*`

원본에는 직접 등장하지 않지만 문자열의 기본 연산으로 함께 알아두면 좋습니다.

```python
print("-" * 10)
print("Python " * 3)
```

출력:

```text
----------
Python Python Python 
```

구분선이나 반복 패턴을 만들 때 사용할 수 있습니다.

---

# 12. f-string

공통 원본:

```python
d = f"지금 온도는 {b}도 입니다."
print(d)
```

출력:

```text
지금 온도는 32.5도 입니다.
```

문자열 앞에 `f`를 붙이고 `{}` 안에 변수나 표현식을 작성합니다.

```python
name = "민수"
age = 20

print(f"{name}의 나이는 {age}세입니다.")
```

f-string은 JavaScript의 백틱 문자열과 비슷한 역할을 하지만, Python에서는 백틱이 아니라 문자열 앞의 `f`와 중괄호를 사용합니다.

```text
Python      f"값: {value}"
JavaScript  `값: ${value}`
```

내 코드 주석의 `fomentic`은 일반적인 Python 용어가 아닙니다. 정확한 명칭은 **formatted string literal**, 줄여서 **f-string**입니다.

---

# 13. f-string 내부 표현식

중괄호 안에는 단순 변수뿐 아니라 표현식도 사용할 수 있습니다.

```python
x = 10
y = 20

print(f"합계: {x + y}")
print(f"큰 값: {max(x, y)}")
```

출력:

```text
합계: 30
큰 값: 20
```

복잡한 로직을 중괄호 안에 길게 작성하면 가독성이 낮아지므로, 복잡한 계산은 먼저 변수에 저장하는 편이 좋습니다.

---

# 14. 여러 줄 f-string

공통 원본:

```python
f = f'''
<div>
    지금 온도는 {b}도 입니다
</div>
'''
```

내 코드는 이어서 출력합니다.

```python
print(f)
```

강사님 코드는 문자열을 변수 `f`에 저장하지만 `print(f)`는 작성하지 않습니다. 따라서 강사님 코드를 그대로 실행하면 HTML 형태의 문자열은 화면에 출력되지 않습니다.

여러 줄 f-string은 HTML 템플릿이나 긴 메시지를 만들 때 사용할 수 있습니다.

```python
name = "Python"
content = f"""
<section>
    <h1>{name}</h1>
</section>
"""
```

---

# 15. `str.format()`

공통 원본:

```python
e = "지금 온도는 {0}도 입니다".format(b)
print(e)
```

`{0}`은 `format()`에 전달한 첫 번째 값을 의미합니다.

```python
name = "민수"
age = 20

message = "이름: {0}, 나이: {1}".format(name, age)
print(message)
```

출력:

```text
이름: 민수, 나이: 20
```

이름을 붙여 사용할 수도 있습니다.

```python
message = "이름: {name}, 나이: {age}".format(
    name="민수",
    age=20
)
```

현대 Python에서는 일반적으로 f-string이 더 간결하지만, 기존 코드를 읽기 위해 `format()`도 이해해야 합니다.

---

# 16. `%` 문자열 포매팅

공통 원본:

```python
g = '지금 온도는 %d도 입니다' % b
print(g)

h = '지금 온도는 %f도 입니다' % b
print(h)
```

`%d`는 정수 형식으로 출력합니다.

```text
지금 온도는 32도 입니다
```

`%f`는 실수 형식으로 출력합니다.

```text
지금 온도는 32.500000도 입니다
```

대표적인 형식 문자는 다음과 같습니다.

| 형식 | 의미 |
| --- | --- |
| `%s` | 문자열 |
| `%d` | 정수 |
| `%f` | 실수 |

여러 값을 넣을 때는 튜플을 사용합니다.

```python
name = "민수"
age = 20

print("이름: %s, 나이: %d" % (name, age))
```

`%` 포매팅은 오래된 코드에서 자주 볼 수 있지만 새 코드에서는 f-string이 더 선호됩니다.

---

# 17. 문자열 포매팅 비교

같은 내용을 네 가지 방식으로 작성할 수 있습니다.

```python
name = "민수"
age = 20
```

문자열 연결:

```python
message = "이름은 " + name + "이고 나이는 " + str(age) + "세입니다."
```

`%` 포매팅:

```python
message = "이름은 %s이고 나이는 %d세입니다." % (name, age)
```

`str.format()`:

```python
message = "이름은 {}이고 나이는 {}세입니다.".format(name, age)
```

f-string:

```python
message = f"이름은 {name}이고 나이는 {age}세입니다."
```

| 방식 | 특징 |
| --- | --- |
| 문자열 연결 | 간단하지만 형 변환과 `+`가 많아질 수 있음 |
| `%` 포매팅 | 오래된 코드에서 자주 보임 |
| `str.format()` | 위치·이름 기반 포매팅 가능 |
| f-string | 현대 Python에서 가장 간결하고 읽기 쉬움 |

---

# 18. 문자열은 시퀀스

문자열은 문자가 순서대로 저장된 시퀀스입니다.

```python
text = "Python"

print(text[0])
print(text[1])
print(text[-1])
```

출력:

```text
P
y
n
```

인덱스는 0부터 시작하며 음수 인덱스는 뒤에서부터 접근합니다.

```text
문자    P  y  t  h  o  n
인덱스  0  1  2  3  4  5
음수   -6 -5 -4 -3 -2 -1
```

---

# 19. 문자열 슬라이싱

문자열 일부를 잘라 새 문자열을 만들 수 있습니다.

```python
text = "Python"

print(text[0:3])
print(text[2:])
print(text[:4])
print(text[::-1])
```

출력:

```text
Pyt
thon
Pyth
nohtyP
```

기본 형식:

```python
문자열[start:stop:step]
```

`stop` 위치는 결과에 포함되지 않습니다.

---

# 20. 문자열의 불변성

문자열은 생성된 뒤 내부 문자를 직접 변경할 수 없는 immutable 객체입니다.

```python
text = "hello"

# TypeError 발생
# text[0] = "H"
```

예외:

```text
TypeError: 'str' object does not support item assignment
```

문자열을 바꾸려면 새로운 문자열을 만들어 다시 대입해야 합니다.

```python
text = "hello"
text = "H" + text[1:]

print(text)
```

출력:

```text
Hello
```

`replace()`, `upper()`, `strip()` 등의 메서드도 원본 문자열을 직접 변경하지 않고 새로운 문자열을 반환합니다.

---

# 21. `len()` 문자열 길이

공통 원본:

```python
i = '_hello'
print(len(i))
```

출력:

```text
6
```

`len()`은 문자열에 포함된 문자의 개수를 반환합니다.

```python
print(len("Python"))
print(len("안녕하세요"))
print(len("a b"))
```

출력:

```text
6
5
3
```

공백도 하나의 문자로 계산됩니다.

---

# 22. `count()` 문자 개수 세기

공통 원본:

```python
print(i.count('l'))
```

`i`가 `_hello`이므로 출력은 다음과 같습니다.

```text
2
```

부분 문자열의 등장 횟수도 셀 수 있습니다.

```python
text = "banana"

print(text.count("a"))
print(text.count("an"))
```

출력:

```text
3
2
```

---

# 23. `find()` 위치 찾기

공통 원본:

```python
print(i.find('l'))
print(i.find('z'))
```

출력:

```text
3
-1
```

`find()`는 처음 발견한 부분 문자열의 시작 인덱스를 반환합니다. 찾지 못하면 `-1`을 반환합니다.

```python
text = "hello"

position = text.find("l")

if position != -1:
    print(f"찾은 위치: {position}")
```

내 코드와 강사님 코드 모두 JavaScript의 `indexOf()`와 연결해 설명합니다. 찾지 못했을 때 `-1`을 반환한다는 점이 비슷합니다.

---

# 24. `index()` 위치 찾기

공통 원본:

```python
print(i.index('l'))
# print(i.index('z'))
```

찾는 값이 존재하면 `find()`와 같은 인덱스를 반환합니다.

```text
3
```

하지만 값이 없으면 `ValueError`가 발생합니다.

```python
"hello".index("z")
```

예외:

```text
ValueError: substring not found
```

---

# 25. `find()`와 `index()` 비교

| 메서드 | 찾은 경우 | 찾지 못한 경우 |
| --- | --- | --- |
| `find()` | 인덱스 반환 | `-1` 반환 |
| `index()` | 인덱스 반환 | `ValueError` 발생 |

존재 여부를 조건문으로 확인하려면 `find()`를 사용할 수 있습니다.

```python
if text.find("Python") != -1:
    print("포함되어 있습니다.")
```

단순히 포함 여부만 확인할 때는 `in` 연산자가 더 읽기 쉽습니다.

```python
if "Python" in text:
    print("포함되어 있습니다.")
```

찾지 못한 상황 자체가 비정상 상태라면 `index()`가 적합할 수 있습니다.

---

# 26. `rfind()` 오른쪽 기준 검색

공통 원본:

```python
print(i.rfind('l'))
```

`_hello`에서 마지막 `l`의 인덱스는 4입니다.

```text
4
```

`rfind()`는 문자열의 오른쪽에서부터 검색하지만 반환하는 값은 원래 문자열 기준의 인덱스입니다.

```python
text = "banana"
print(text.rfind("a"))
```

출력:

```text
5
```

---

# 27. 문자열 포함 여부 `in`

원본에는 직접 등장하지 않지만 검색과 함께 사용하는 핵심 문법입니다.

```python
text = "Python String"

print("String" in text)
print("Java" in text)
print("Java" not in text)
```

출력:

```text
True
False
True
```

위치가 필요하지 않고 포함 여부만 확인한다면 `find()`보다 의도가 분명합니다.

---

# 28. `replace()` 문자열 치환

공통 원본:

```python
print(i.replace('l', 'w'))
```

출력:

```text
_hewwo
```

기본적으로 일치하는 모든 부분 문자열을 바꿉니다.

```python
text = "banana"
print(text.replace("a", "o"))
```

```text
bonono
```

치환 횟수를 제한할 수도 있습니다.

```python
text = "banana"
print(text.replace("a", "o", 1))
```

```text
bonana
```

내 코드의 주석에 있는 “하나만 바꾸고 싶으면”이라는 질문에는 `replace(old, new, count)`의 세 번째 인수로 답할 수 있습니다.

```python
j = "그럼 저기서 하나만 바꾸고 싶으면요?"
result = j.replace("요", "다", 1)
```

---

# 29. `replace()`는 원본을 변경하지 않는다

```python
text = "hello"
text.replace("h", "H")

print(text)
```

출력:

```text
hello
```

문자열은 불변 객체이므로 반환값을 다시 저장해야 합니다.

```python
text = text.replace("h", "H")
print(text)
```

```text
Hello
```

---

# 30. `split()` 문자열 분리

공통 원본:

```python
j = '그럼 저기서 하나만 바꾸고 싶으면요?'
k = j.split()
print(k)
```

인수를 생략하면 연속된 공백을 기준으로 문자열을 나눕니다.

출력:

```text
['그럼', '저기서', '하나만', '바꾸고', '싶으면요?']
```

구분자를 직접 지정할 수도 있습니다.

```python
data = "apple,banana,peach"
items = data.split(",")

print(items)
```

출력:

```text
['apple', 'banana', 'peach']
```

---

# 31. `split()`의 최대 분리 횟수

두 번째 인수로 최대 분리 횟수를 지정할 수 있습니다.

```python
data = "2026-07-30-python"
print(data.split("-", 2))
```

출력:

```text
['2026', '07', '30-python']
```

파일 형식이나 앞부분의 고정된 필드를 분리할 때 유용합니다.

---

# 32. 구조 분해 대입

공통 원본:

```python
m = [1, 2, 3]
a, b, c = m
```

오른쪽 시퀀스의 각 요소를 왼쪽 변수에 순서대로 대입합니다.

```python
print(a)
print(b)
print(c)
```

```text
1
2
3
```

변수 개수와 요소 개수가 맞지 않으면 `ValueError`가 발생합니다.

```python
# ValueError
# a, b = [1, 2, 3]
```

```text
ValueError: too many values to unpack
```

나머지 값을 `*`로 받을 수 있습니다.

```python
first, *rest = [1, 2, 3, 4]

print(first)
print(rest)
```

```text
1
[2, 3, 4]
```

---

# 33. `join()` 문자열 결합

공통 원본:

```python
a = ['a', 'b', 'c', 'd', 'e']
b = '-'.join(a)
print(b)
```

출력:

```text
a-b-c-d-e
```

`join()`은 구분자 문자열을 기준으로 반복 가능한 객체의 문자열 요소들을 결합합니다.

```text
'-'.join(['a', 'b', 'c'])
 │       └─ 연결할 문자열들
 └───────── 각 문자열 사이에 들어갈 구분자
```

`join()`이 리스트의 메서드가 아니라 문자열의 메서드라는 점에 주의합니다.

```python
# 올바른 사용
result = ", ".join(["사과", "바나나", "복숭아"])
```

---

# 34. 숫자 목록과 `join()`

`join()`은 문자열만 연결할 수 있습니다.

```python
numbers = [1, 2, 3]

# TypeError 발생
# result = "-".join(numbers)
```

예외:

```text
TypeError: sequence item 0: expected str instance, int found
```

강사님 원본에는 두 가지 변환 방식이 있습니다.

```python
a = [1, 2, 3, 4, 5]
'-'.join(map(str, a))
'-'.join(str(data) for data in a)
```

내 코드에는 주석으로 `map(str, a)` 방식이 언급되어 있고, generator expression 방식이 실행됩니다.

```python
numbers = [1, 2, 3]

result1 = "-".join(map(str, numbers))
result2 = "-".join(str(number) for number in numbers)
```

두 결과는 같습니다.

```text
1-2-3
```

---

# 35. `split()`과 `join()`의 관계

원본:

```python
b = '-'.join(a)
c = b.split('-')
print(c)
```

동작 흐름:

```text
['a', 'b', 'c', 'd', 'e']
          ↓ join('-')
'a-b-c-d-e'
          ↓ split('-')
['a', 'b', 'c', 'd', 'e']
```

`join()`은 여러 문자열을 하나로 합치고, `split()`은 하나의 문자열을 여러 부분으로 나눕니다.

---

# 36. 대소문자와 문자열 검색

내 코드:

```python
a = "Don't Look Back is Anger"
b = a.find('back')
print(b)
```

강사님 코드:

```python
a = "Don't Look Back in Anger"
b = a.find('back')
print(b)
```

두 코드 모두 문자열에는 `Back`이 있지만 검색 문자열은 `back`입니다.

Python 문자열 검색은 대소문자를 구분하므로 결과는 다음과 같습니다.

```text
-1
```

문장 자체는 강사님 코드의 `in Anger`와 내 코드의 `is Anger`가 다릅니다. 문자열 메서드 학습에는 영향을 주지 않지만 원문 비교 시 구분해야 합니다.

---

# 37. `upper()`와 `lower()`

공통 원본 흐름:

```python
c = a.upper()
print(c)

d = a.upper().find('back'.upper())
print(d)
```

두 문자열을 같은 대소문자로 변환한 뒤 검색합니다.

```python
text = "Don't Look Back in Anger"
keyword = "back"

position = text.upper().find(keyword.upper())
print(position)
```

출력:

```text
11
```

소문자로 통일해도 됩니다.

```python
position = text.lower().find(keyword.lower())
```

`upper()`와 `lower()`도 원본 문자열을 변경하지 않고 새 문자열을 반환합니다.

---

# 38. `casefold()` 보충

영문 위주의 단순 비교에는 `lower()`가 충분한 경우가 많습니다. 국제화된 문자열을 더 강하게 소문자화해 비교할 때는 `casefold()`를 사용할 수 있습니다.

```python
left = "Straße"
right = "STRASSE"

print(left.casefold() == right.casefold())
```

```text
True
```

초급 단계에서는 `lower()`를 우선 익히고, 다국어 텍스트 비교가 필요할 때 `casefold()`를 고려합니다.

---

# 39. 메서드 체이닝

원본에는 여러 문자열 메서드를 연속해서 호출하는 코드가 있습니다.

```python
print(a.strip().replace(' ', ''))
```

이처럼 반환값에 바로 다음 메서드를 호출하는 방식을 메서드 체이닝이라고 합니다.

```text
a.strip()
    ↓ 새 문자열
.replace(' ', '')
    ↓ 최종 문자열
```

단계가 많아지면 중간 변수를 사용해 읽기 쉽게 만들 수 있습니다.

```python
trimmed = a.strip()
result = trimmed.replace(" ", "")
```

---

# 40. `strip()` 양쪽 공백 제거

내 코드:

```python
a = '   a b   '
print(a.strip())
print(a.strip().replace(' ', ''))
```

강사님 코드:

```python
a = '  a b  '
print(a.strip())
```

`strip()`은 문자열 양쪽 끝의 공백 문자를 제거합니다.

출력:

```text
a b
ab
```

중간 공백은 제거하지 않습니다.

```python
text = "   a b   "
print(text.strip())
```

```text
a b
```

모든 일반 공백을 없애려면 원본처럼 `replace()`를 함께 사용할 수 있습니다.

```python
text.strip().replace(" ", "")
```

---

# 41. `lstrip()`과 `rstrip()`

한쪽 공백만 제거할 수도 있습니다.

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

파일의 줄바꿈만 제거할 때는 `rstrip("\n")`처럼 제거할 문자를 지정할 수 있습니다.

---

# 42. `strip()` 인수의 의미

`strip(chars)`는 정확한 접두사나 접미사를 제거하는 함수가 아닙니다. 전달한 문자 집합에 속하는 문자를 양끝에서 반복 제거합니다.

```python
text = "xyPythonxy"
print(text.strip("xy"))
```

출력:

```text
Python
```

정확한 접두사나 접미사를 제거하려면 다음 메서드를 사용할 수 있습니다.

```python
filename = "test.py"
print(filename.removesuffix(".py"))
```

---

# 43. `zfill()` 0 채우기

공통 원본:

```python
print('35'.zfill(4))
print('35000'.zfill(4))
```

출력:

```text
0035
35000
```

`zfill(width)`은 문자열 길이가 지정한 너비보다 짧으면 왼쪽을 `0`으로 채웁니다.

이미 너비보다 길다면 원본 문자열을 그대로 반환합니다.

```python
print("7".zfill(3))
print("1234".zfill(3))
```

```text
007
1234
```

일련번호나 날짜 일부를 고정 자릿수로 표현할 때 사용할 수 있습니다.

---

# 44. f-string 기본 너비 지정

공통 원본 흐름:

```python
a = 7
print(f'{a:03}')
print(f'{a:3}')
```

출력:

```text
007
  7
```

`03`은 전체 너비를 3으로 하고 빈자리를 `0`으로 채웁니다.

`3`은 전체 너비를 3으로 하고 기본 정렬에 따라 공백을 채웁니다.

```python
number = 7

print(f"{number:03}")
print(f"{number:3}")
```

---

# 45. f-string 정렬

원본:

```python
print(f'..{a:<3}..')
print(f'..{a:>3}..')
print(f'..{a:^10}..')
```

강사님 코드에는 `>3` 예제가 없고, 내 코드에는 왼쪽·오른쪽·가운데 정렬이 모두 있습니다.

| 표현 | 의미 |
| --- | --- |
| `<` | 왼쪽 정렬 |
| `>` | 오른쪽 정렬 |
| `^` | 가운데 정렬 |

```python
value = 7

print(f"|{value:<5}|")
print(f"|{value:>5}|")
print(f"|{value:^5}|")
```

출력:

```text
|7    |
|    7|
|  7  |
```

---

# 46. 채움 문자 지정

정렬 기호 앞에 채움 문자를 지정할 수 있습니다.

```python
value = "Python"

print(f"{value:-<10}")
print(f"{value:->10}")
print(f"{value:-^10}")
```

출력:

```text
Python----
----Python
--Python--
```

형식:

```text
{값:채움문자정렬기호너비}
```

---

# 47. 실수 자릿수 지정

공통 원본:

```python
a = 3.14
print(f'{a:08.3f}')
```

출력:

```text
0003.140
```

형식의 의미:

```text
08.3f
││ │└─ 실수 형식
││ └── 소수점 아래 3자리
│└──── 전체 너비 8
└───── 빈자리 0 채우기
```

다른 예제:

```python
pi = 3.141592

print(f"{pi:.2f}")
print(f"{pi:.4f}")
```

출력:

```text
3.14
3.1416
```

표시 자릿수에 따라 반올림됩니다.

---

# 48. 천 단위 구분 기호

공통 원본:

```python
a = 15000
print(f'{a:,}')
```

출력:

```text
15,000
```

금액이나 큰 수를 읽기 쉽게 표시할 수 있습니다.

```python
price = 123456789
print(f"{price:,}원")
```

```text
123,456,789원
```

---

# 49. 퍼센트 형식 보충

비율을 백분율로 출력할 수 있습니다.

```python
rate = 0.1567

print(f"{rate:.1%}")
print(f"{rate:.2%}")
```

출력:

```text
15.7%
15.67%
```

값에 100을 곱해 표시하고 `%` 기호를 붙입니다.

---

# 50. 디버깅용 f-string 보충

Python의 f-string에서는 변수 이름과 값을 함께 출력할 수 있습니다.

```python
temperature = 32.5
print(f"{temperature=}")
```

출력:

```text
temperature=32.5
```

간단한 디버깅 시 유용하지만 사용자에게 보여주는 최종 문구에는 일반 f-string을 사용하는 편이 좋습니다.

---

# 51. 문자열 메서드 호출 방식

문자열 메서드는 점 표기법으로 호출합니다.

```python
text = "Python"

text.upper()
text.lower()
text.find("th")
text.replace("Py", "J")
```

기본 구조:

```text
문자열객체.메서드(인수)
```

반면 `len()`은 문자열 메서드가 아니라 내장 함수입니다.

```python
len(text)
```

```python
# 존재하지 않는 방식
# text.len()
```

---

# 52. 원본 전체 실행 결과 핵심

내 코드의 주요 출력 흐름은 다음과 같습니다.

```text
지금 온도는 32.5도 입니다.
지금 온도는 32.5도 입니다.
지금 온도는 32.5도 입니다

<div>
    지금 온도는 32.5도 입니다
</div>

지금 온도는 32도 입니다
지금 온도는 32.500000도 입니다
6
2
3
-1
3
4
_hewwo
['그럼', '저기서', '하나만', '바꾸고', '싶으면요?']
a-b-c-d-e
['a', 'b', 'c', 'd', 'e']
-1
DON'T LOOK BACK IS ANGER
11
a b
ab
0035
35000
007
..  7..
..7  ..
..  7..
..    7     ..
0003.140
15,000
```

출력 문구의 마침표와 공백은 내 코드와 강사님 코드 사이에 일부 차이가 있습니다.

---

# 53. 내 코드와 강사님 코드 공통점

두 코드 모두 다음 내용을 다룹니다.

- 작은따옴표와 큰따옴표 문자열
- 따옴표 3개를 이용한 여러 줄 문자열
- 이스케이프 문자
- `str()`을 이용한 숫자 변환
- f-string
- `str.format()`
- `%d`, `%f` 포매팅
- `len()`
- `count()`
- `find()`, `index()`, `rfind()`
- `replace()`
- `split()`
- 구조 분해 대입
- `join()`
- 대소문자 변환 후 검색
- `strip()`
- `zfill()`
- f-string 너비, 정렬, 실수, 천 단위 형식

따라서 두 파일의 전체 학습 흐름은 거의 같습니다.

---

# 54. 내 코드와 강사님 코드 차이

| 비교 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 두 번째 문자열 | `world` | `wolrd` |
| 여러 줄 문자열 문구 | `쌉 가능` | `가능` |
| 단독 여러 줄 문자열 | 설명 주석만 있음 | 실제 단독 문자열 작성 |
| 이스케이프 예제 | 주석으로 설명 | 실제 문자열 리터럴 작성 |
| 문자열 연결 문장 | 마침표 포함 | 마침표 없음 |
| f-string 설명 | JavaScript 백틱과 비교 | 설명 없음 |
| 여러 줄 f-string 출력 | `print(f)` 있음 | 변수에만 저장 |
| `find()` 설명 | `indexOf()`와 반환값 상세 | 간단한 `indexOf` 주석 |
| `index()` 오류 | 구체적인 `ValueError` 기록 | “없으면 에러” |
| 숫자 `join()` | `map()`은 주석, generator 실행 | 두 방식 모두 작성 |
| 원문 문장 | `Don't Look Back is Anger` | `Don't Look Back in Anger` |
| `strip()` | `replace()` 체이닝 추가 | `strip()`만 사용 |
| 오른쪽 정렬 | `>3` 예제 있음 | 없음 |
| 출력 형식 주석 | 결과 설명이 상세함 | 코드 중심 |

---

# 55. 내 코드의 장점

- 문자열 연결 시 자료형 변환이 필요한 이유를 주석으로 남겼습니다.
- f-string을 JavaScript 템플릿 리터럴과 연결해 이해하려고 했습니다.
- 여러 줄 f-string을 실제로 출력해 결과를 확인했습니다.
- `find()`와 `index()`의 실패 동작 차이를 구체적으로 기록했습니다.
- `rfind()`가 오른쪽부터 검색한다는 점을 주석으로 남겼습니다.
- `strip()`과 `replace()`를 연결해 양끝 공백과 모든 공백 제거를 비교했습니다.
- 왼쪽, 오른쪽, 가운데 정렬 예제를 모두 작성했습니다.
- 숫자 형식 지정 결과를 주석으로 확인할 수 있습니다.

---

# 56. 내 코드의 개선점

- 변수 이름 `a`, `b`, `c`를 반복해서 재사용해 각 값의 의미를 추적하기 어렵습니다.
- “변수에 넣지 않으면 주석으로 사용”이라는 설명은 단독 문자열과 주석의 문법적 차이를 구분하도록 수정할 필요가 있습니다.
- `fomentic`은 일반 용어가 아니므로 `f-string` 또는 `formatted string literal`로 표현하는 것이 정확합니다.
- Python의 f-string은 JavaScript 백틱과 역할이 비슷하지만 문법은 다르다는 점을 명확히 해야 합니다.
- “float으로 선언 가능”보다는 `%f 형식으로 출력한다`고 표현하는 것이 정확합니다.
- `rfind()`는 “오른쪽부터 indexOf”보다는 “오른쪽에서 검색해 원본 기준 인덱스를 반환한다”고 설명하는 편이 정확합니다.
- `replace()`로 하나만 바꾸려면 세 번째 `count` 인수를 사용할 수 있다는 코드가 추가되면 좋습니다.
- `'-'.join(str(data) for data in a)`의 반환값을 변수에 저장하거나 출력하지 않아 실행 결과를 확인할 수 없습니다.
- 대소문자 검색 예제의 문장 `is Anger`는 강사님 코드의 `in Anger`와 다르므로 의도한 수정인지 확인할 필요가 있습니다.
- `strip().replace(' ', '')`는 일반 공백만 제거하므로 모든 종류의 공백 처리 목적이라면 요구사항을 더 명확히 해야 합니다.

---

# 57. 강사님 코드의 장점

- 문자열 생성부터 출력 형식까지 수업 순서가 간결하게 이어집니다.
- 단독 여러 줄 문자열을 실제 코드로 작성해 주석처럼 보이는 사용 방식을 확인할 수 있습니다.
- 문자열 숫자 연결, f-string, `format()`, `%` 포매팅을 연속해서 비교할 수 있습니다.
- `map(str, a)`와 generator expression을 모두 제시합니다.
- 주요 문자열 메서드를 짧은 코드로 빠르게 실습할 수 있습니다.
- `zfill()`과 f-string 형식 지정을 함께 학습할 수 있습니다.

---

# 58. 강사님 코드의 개선점

- `wolrd`는 `world`로 수정하는 편이 좋습니다.
- 따옴표 3개를 “여러 줄 주석”이라고만 설명하면 문자열 리터럴이라는 사실을 오해할 수 있습니다.
- 변수 `f`에 저장한 여러 줄 f-string을 출력하지 않아 결과를 확인할 수 없습니다.
- `find()`와 `index()`의 차이를 예외 이름까지 명확히 설명하면 좋습니다.
- `join()` 결과 두 개를 변수에 저장하거나 출력하지 않아 숫자 변환 결과를 확인하기 어렵습니다.
- `strip()`이 중간 공백을 제거하지 않는다는 설명이 있으면 좋습니다.
- 오른쪽 정렬 `>` 예제가 없어 왼쪽·가운데 정렬과 함께 비교하기 어렵습니다.
- 변수 이름을 반복 재사용하여 초보자가 현재 자료형과 값을 추적하기 어렵습니다.

---

# 59. 개선된 대표 코드

```python
temperature = 32.5

concatenated = (
    "지금 온도는 "
    + str(temperature)
    + "도입니다."
)
formatted = f"지금 온도는 {temperature}도입니다."
legacy_format = "지금 온도는 {0}도입니다.".format(
    temperature
)

print(concatenated)
print(formatted)
print(legacy_format)

text = "_hello"

print(len(text))
print(text.count("l"))
print(text.find("l"))
print(text.find("z"))
print(text.rfind("l"))
print(text.replace("l", "w", 1))

sentence = "그럼 저기서 하나만 바꾸고 싶으면요?"
words = sentence.split()
print(words)

letters = ["a", "b", "c", "d", "e"]
joined = "-".join(letters)
restored = joined.split("-")

print(joined)
print(restored)

numbers = [1, 2, 3, 4, 5]
number_text = "-".join(
    str(number)
    for number in numbers
)
print(number_text)

song_title = "Don't Look Back in Anger"
keyword = "back"
position = song_title.lower().find(
    keyword.lower()
)
print(position)

padded = "35".zfill(4)
print(padded)

value = 7
print(f"{value:03}")
print(f"|{value:<3}|")
print(f"|{value:>3}|")
print(f"|{value:^10}|")

pi = 3.14
print(f"{pi:08.3f}")

price = 15000
print(f"{price:,}원")
```

---

# 60. 실무 활용 예제: 사용자 입력 정리

```python
raw_name = "   홍 길 동   "

clean_name = raw_name.strip()
compact_name = clean_name.replace(" ", "")

print(clean_name)
print(compact_name)
```

출력:

```text
홍 길 동
홍길동
```

사용자 입력에는 앞뒤 공백이 포함될 수 있으므로 저장 전에 정리할 수 있습니다.

---

# 61. 실무 활용 예제: CSV 형태의 문자열

```python
raw_data = "apple,banana,peach"
fruits = raw_data.split(",")

print(fruits)
print(" / ".join(fruits))
```

출력:

```text
['apple', 'banana', 'peach']
apple / banana / peach
```

단순한 문자열은 `split()`으로 처리할 수 있지만, 따옴표와 쉼표가 복잡한 실제 CSV 파일은 표준 라이브러리 `csv`를 사용하는 편이 안전합니다.

---

# 62. 실무 활용 예제: 파일 확장자 검사

```python
filename = "report.PDF"

if filename.lower().endswith(".pdf"):
    print("PDF 파일입니다.")
```

`endswith()`는 문자열이 특정 접미사로 끝나는지 확인합니다.

```python
url = "https://example.com"

if url.startswith("https://"):
    print("보안 연결 형식입니다.")
```

`startswith()`는 특정 접두사로 시작하는지 확인합니다.

---

# 63. 실무 활용 예제: 고정 길이 번호

```python
order_number = 35
formatted_order = str(order_number).zfill(6)

print(formatted_order)
```

```text
000035
```

f-string으로도 표현할 수 있습니다.

```python
print(f"{order_number:06}")
```

숫자 계산이 필요한 값은 숫자로 보관하고, 화면에 표시할 때만 형식을 적용하는 편이 좋습니다.

---

# 64. 실무 활용 예제: 영수증 출력

```python
product = "키보드"
price = 89000
quantity = 2
amount = price * quantity

print(f"상품명 : {product}")
print(f"단가   : {price:>10,}원")
print(f"수량   : {quantity:>10}개")
print(f"합계   : {amount:>10,}원")
```

형식 지정을 사용하면 숫자를 일정한 너비로 정렬할 수 있습니다.

---

# 65. 자주 하는 실수: 숫자와 문자열 직접 연결

잘못된 코드:

```python
age = 20
# print("나이: " + age)
```

개선:

```python
print("나이: " + str(age))
print(f"나이: {age}")
```

f-string을 사용하면 명시적인 `str()` 호출 없이 표현할 수 있습니다.

---

# 66. 자주 하는 실수: `find()` 결과를 Boolean처럼 사용

다음 코드는 찾은 위치가 0일 때 문제가 됩니다.

```python
text = "Python"

if text.find("Python"):
    print("찾았습니다.")
```

`find()` 결과가 `0`이면 falsy이므로 출력되지 않습니다.

정확한 방식:

```python
if text.find("Python") != -1:
    print("찾았습니다.")
```

포함 여부만 필요하면:

```python
if "Python" in text:
    print("찾았습니다.")
```

---

# 67. 자주 하는 실수: `replace()` 반환값 무시

잘못된 기대:

```python
text = "hello"
text.replace("h", "H")
print(text)
```

출력:

```text
hello
```

개선:

```python
text = text.replace("h", "H")
```

문자열 메서드 대부분은 새로운 문자열을 반환합니다.

---

# 68. 자주 하는 실수: `join()` 방향 반대로 작성

잘못된 코드:

```python
items = ["a", "b", "c"]
# items.join("-")
```

올바른 코드:

```python
"-".join(items)
```

구분자 문자열이 `join()` 메서드를 호출합니다.

---

# 69. 자주 하는 실수: 숫자 목록 바로 결합

잘못된 코드:

```python
numbers = [1, 2, 3]
# "-".join(numbers)
```

개선:

```python
"-".join(map(str, numbers))
```

또는:

```python
"-".join(str(number) for number in numbers)
```

---

# 70. 자주 하는 실수: `strip()`이 중간 공백도 제거한다고 생각하기

```python
text = "  a b  "
print(text.strip())
```

결과:

```text
a b
```

중간 공백은 남습니다.

```python
print(text.strip().replace(" ", ""))
```

```text
ab
```

---

# 71. 자주 하는 실수: 문자열 인덱스 직접 수정

잘못된 코드:

```python
text = "hello"
# text[0] = "H"
```

문자열은 불변 객체입니다.

개선:

```python
text = "H" + text[1:]
```

또는:

```python
text = text.replace("h", "H", 1)
```

---

# 72. 자주 하는 실수: `index()` 예외 미처리

```python
text = "hello"
# position = text.index("z")
```

찾는 문자열이 없을 가능성이 있다면 `find()`나 `in`을 사용합니다.

```python
if "z" in text:
    position = text.index("z")
```

---

# 73. 자주 하는 실수: 포매팅과 값 자체 혼동

```python
number = 7
formatted = f"{number:03}"

print(number)
print(formatted)
print(type(number))
print(type(formatted))
```

출력:

```text
7
007
<class 'int'>
<class 'str'>
```

포매팅 결과는 화면 표시용 문자열이며 원래 숫자 값이 7에서 007로 바뀌는 것은 아닙니다.

---

# 74. 면접·복습 질문 1

## 문자열은 왜 불변 객체인가?

문자열이 생성된 뒤 내부 문자를 직접 변경할 수 없다는 의미입니다.

```python
text = "hello"
# text[0] = "H"
```

변경처럼 보이는 메서드도 실제로는 새 문자열을 반환합니다.

```python
upper_text = text.upper()
```

불변성은 문자열을 안전하게 공유하고 해시 가능한 값으로 사용할 수 있게 하는 특성과 연결됩니다.

---

# 75. 면접·복습 질문 2

## `find()`와 `index()`의 차이는?

둘 다 부분 문자열의 위치를 반환합니다.

- `find()`는 찾지 못하면 `-1`
- `index()`는 찾지 못하면 `ValueError`

단순 포함 여부는 `in`이 더 명확할 수 있습니다.

---

# 76. 면접·복습 질문 3

## `split()`과 `join()`의 차이는?

- `split()`은 문자열을 나누어 리스트를 반환합니다.
- `join()`은 문자열 요소들을 하나의 문자열로 결합합니다.

```python
"a-b-c".split("-")
"-".join(["a", "b", "c"])
```

---

# 77. 면접·복습 질문 4

## f-string의 장점은?

- 변수와 표현식을 문자열 안에서 바로 사용할 수 있습니다.
- 문자열 연결보다 읽기 쉽습니다.
- 정렬, 소수점, 천 단위 등 형식 지정을 함께 사용할 수 있습니다.
- 현대 Python 코드에서 널리 사용됩니다.

---

# 78. 면접·복습 질문 5

## `strip()`은 문자열 내부 공백도 제거하는가?

아닙니다. 기본 `strip()`은 양쪽 끝의 공백 문자를 제거하고 중간 공백은 유지합니다.

---

# 79. 면접·복습 질문 6

## `join()`을 사용할 때 요소가 숫자라면?

모든 요소를 문자열로 변환해야 합니다.

```python
"-".join(map(str, [1, 2, 3]))
```

---

# 80. Problems

## 문제 1

다음 변수들을 사용해 f-string으로 문장을 출력하세요.

```python
name = "민수"
age = 20
```

예상 출력:

```text
민수의 나이는 20세입니다.
```

---

## 문제 2

다음 문자열의 길이와 `o`의 개수를 출력하세요.

```python
text = "Hello Python"
```

---

## 문제 3

다음 문자열에서 `Python`의 시작 위치를 출력하세요.

```python
text = "Hello Python"
```

찾지 못했을 때 예외가 발생하지 않는 메서드를 사용하세요.

---

## 문제 4

다음 문자열의 모든 `apple`을 `orange`로 바꾸세요.

```python
text = "apple banana apple"
```

---

## 문제 5

다음 문자열을 쉼표 기준으로 나누어 리스트로 만드세요.

```python
data = "HTML,CSS,JavaScript,Python"
```

---

## 문제 6

다음 리스트를 ` -> `로 연결하세요.

```python
languages = ["HTML", "CSS", "Python"]
```

예상 출력:

```text
HTML -> CSS -> Python
```

---

## 문제 7

다음 숫자 리스트를 하이픈으로 연결하세요.

```python
numbers = [2026, 7, 30]
```

예상 출력:

```text
2026-7-30
```

---

## 문제 8

다음 문자열에서 양쪽 공백을 제거하고 모든 일반 공백을 제거하세요.

```python
text = "   P y t h o n   "
```

---

## 문제 9

숫자 35를 네 자리 문자열 `0035`로 출력하세요.

`zfill()`과 f-string 두 가지 방식으로 작성하세요.

---

## 문제 10

다음 가격을 천 단위 쉼표와 `원`을 포함해 출력하세요.

```python
price = 1250000
```

예상 출력:

```text
1,250,000원
```

---

## 문제 11

다음 문자열에서 대소문자를 구분하지 않고 `python`이 포함되어 있는지 확인하세요.

```python
text = "I Like PYTHON"
```

---

## 문제 12

다음 문장에서 첫 번째 `좋아`만 `싫어`로 바꾸세요.

```python
text = "좋아 좋아 좋아"
```

---

# 81. Answers

## 정답 1

```python
name = "민수"
age = 20

print(f"{name}의 나이는 {age}세입니다.")
```

---

## 정답 2

```python
text = "Hello Python"

print(len(text))
print(text.count("o"))
```

---

## 정답 3

```python
text = "Hello Python"

print(text.find("Python"))
```

---

## 정답 4

```python
text = "apple banana apple"

print(text.replace("apple", "orange"))
```

---

## 정답 5

```python
data = "HTML,CSS,JavaScript,Python"

print(data.split(","))
```

---

## 정답 6

```python
languages = ["HTML", "CSS", "Python"]

print(" -> ".join(languages))
```

---

## 정답 7

```python
numbers = [2026, 7, 30]

print("-".join(map(str, numbers)))
```

또는:

```python
print(
    "-".join(
        str(number)
        for number in numbers
    )
)
```

---

## 정답 8

```python
text = "   P y t h o n   "

print(text.strip().replace(" ", ""))
```

---

## 정답 9

```python
number = 35

print(str(number).zfill(4))
print(f"{number:04}")
```

---

## 정답 10

```python
price = 1250000

print(f"{price:,}원")
```

---

## 정답 11

```python
text = "I Like PYTHON"

print("python" in text.lower())
```

---

## 정답 12

```python
text = "좋아 좋아 좋아"

print(text.replace("좋아", "싫어", 1))
```

---

# 82. Final Checklist

- [ ] 작은따옴표와 큰따옴표로 문자열을 만들 수 있다.
- [ ] 따옴표 3개가 여러 줄 문자열 문법임을 설명할 수 있다.
- [ ] 단독 여러 줄 문자열과 실제 주석의 차이를 설명할 수 있다.
- [ ] 이스케이프 문자를 사용할 수 있다.
- [ ] 문자열과 숫자를 연결할 때 `str()`을 사용할 수 있다.
- [ ] f-string으로 변수와 표현식을 출력할 수 있다.
- [ ] `str.format()`과 `%` 포매팅을 읽을 수 있다.
- [ ] 문자열 인덱싱과 슬라이싱을 사용할 수 있다.
- [ ] 문자열이 불변 객체임을 설명할 수 있다.
- [ ] `len()`과 `count()`를 사용할 수 있다.
- [ ] `find()`, `index()`, `rfind()`의 차이를 설명할 수 있다.
- [ ] `replace()`의 반환값을 다시 저장해야 함을 이해한다.
- [ ] `split()`과 `join()`을 사용할 수 있다.
- [ ] 숫자 목록을 문자열로 변환해 `join()`할 수 있다.
- [ ] `upper()`, `lower()`로 대소문자를 정규화할 수 있다.
- [ ] `strip()`, `lstrip()`, `rstrip()`을 구분할 수 있다.
- [ ] `zfill()`과 f-string 0 채우기를 사용할 수 있다.
- [ ] f-string으로 정렬, 소수점, 천 단위 형식을 지정할 수 있다.
- [ ] 내 코드와 강사님 코드의 차이를 설명할 수 있다.

---

# 83. Key Summary

```text
문자열 생성
'a' == "a"

여러 줄 문자열
'''...'''
"""..."""

문자열 연결
"값: " + str(value)

f-string
f"값: {value}"

길이와 검색
len(text)
text.count(value)
text.find(value)
text.index(value)
text.rfind(value)

변환
text.replace(old, new)
text.split(separator)
separator.join(strings)

대소문자와 공백
text.upper()
text.lower()
text.strip()

형식 지정
f"{number:04}"
f"{value:>10}"
f"{value:.2f}"
f"{price:,}"
```

문자열은 단순한 문자의 모음이 아니라 순서를 가진 불변 시퀀스입니다. 검색, 분리, 결합, 정규화와 포매팅을 정확히 이해하면 사용자 입력 처리와 화면 출력 코드를 더 명확하게 작성할 수 있습니다.
