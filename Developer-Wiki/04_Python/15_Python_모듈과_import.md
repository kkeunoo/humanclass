# 15. 모듈과 `import` — 다른 파일의 코드 사용하기

[Python 목차](README.md) · [이전: 예외 발생과 오류 추적](14-02_Python_예외발생과_오류추적.md)

두 원본은 `fn/fn_15_1.py`의 함수·클래스를 불러 쓰고, 표준 라이브러리 `random`과 `urllib.request`도 가져온다. 핵심은 **어느 파일에 정의한 이름을 어떻게 불러서 호출하는지**다.

## 먼저: 다른 파일의 이름을 가져오기

모듈은 함수를 비롯한 Python 코드를 담은 파일이다. `import`는 그 파일에 정의된 이름을 다른 파일에서 사용하도록 연결한다. 원본을 읽을 때는 **정의가 있는 파일 → 가져오는 문장 → 실제 호출한 이름**을 화살표로 이어 보자.

| 형태 | 다음 줄에서 사용하는 이름 |
| --- | --- |
| `import random` | `random.random()`처럼 모듈 이름을 붙임 |
| `from random import random` | `random()`처럼 가져온 함수 이름을 바로 사용 |

두 줄을 동시에 적으면 `random`이라는 이름이 나중 문장에서 다른 대상을 가리킬 수 있으므로 **각각 별도 예제**로 생각한다. 양쪽 원본의 `fn.fn_15_1.add`와 일부 이름만 가져온 호출을 같은 기준으로 비교하자.

다음은 아래 원본에 실제로 있는 `add` 함수를 이용해 **수업 문법으로 줄인 설명용 재구성**이다. `fn/fn_15_1.py`가 실행 위치에서 가져올 수 있는 경로에 있을 때 결과가 나온다.

```python
from fn.fn_15_1 import add
print(add(2, 3))  # 출력: 5
```

`from ... import add`이므로 호출할 때 `fn.fn_15_1.add(...)`라고 길게 쓰지 않는다. 이제 강사님과 내 원본에서 별칭 `fn1`을 붙인 호출과 비교하자.

<!-- chapter-toc -->

- [1. 가져올 파일에 정의한 함수와 클래스](15_Python_모듈과_import.md#section-1)
- [2. 모듈 전체 가져오기와 일부 이름 가져오기](15_Python_모듈과_import.md#section-2)
- [3. 원본 마지막의 웹페이지 읽기](15_Python_모듈과_import.md#section-3)
- [직접 확인할 질문](15_Python_모듈과_import.md#section-4)
- [추가로 알면 좋은 것](15_Python_모듈과_import.md#section-5)

<a id="section-1"></a>

## 1. 가져올 파일에 정의한 함수와 클래스

### 강사님 코드

출처: `teacher/workspace_python/fn/fn_15_1.py` 2–10행 · **원본 발췌**

```python
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

class Hero:
    def attack(self):
        print('공격한다')
```

### 내 코드

출처: `me/workspace_python/fn/fn_15_1.py` 2–10행 · **원본 발췌**

```python
def add(x, y) :
    return x + y

def sub(x, y) :
    return x - y

class Hero :
    def attack(self) :
        print('공격한다')
```

두 파일 모두 `add(1,2)`는 3, `sub(3,2)`는 1을 돌려주고, `Hero().attack()`은 `공격한다`를 출력한다. 이 파일 자체에는 외부 페이지 요청이나 다른 기능이 없다. 다음의 `15_module.py`가 이 이름들을 가져다 쓴다.

<a id="section-2"></a>

## 2. 모듈 전체 가져오기와 일부 이름 가져오기

### 강사님 코드

출처: `teacher/workspace_python/_15_module.py` 2–24행 · **원본 발췌**

```python
# import fn.fn_15_1
import fn.fn_15_1 as fn1

# a = fn.fn_15_1.add(1,2)
a = fn1.add(1,2)
print(a)


from fn.fn_15_1 import add as addd, sub
b = sub(3,2)
print(b)

import random
print( random.random() )

# from random import random
from random import random as rand
# print( random() )
print( rand() )

from fn.fn_15_1 import Hero
h = Hero()
h.attack()
```

### 내 코드

출처: `me/workspace_python/15_module.py` 1–28행 · **원본 발췌**

```python
# import는 숫자로 시작하면 안된다
# 폴더가 있을 경우 .으로 구분한다

# import로 하던, from으로 하던 메모리의 용량 차이는 없으며 경로를 알려주는 것

# import fn.fn_15_1 
import fn.fn_15_1 as fn1 # import로 가져와 as로 별칭을 정할 수 있음

# a = fn.fn_15_1.add(1,2)
a = fn1.add(1,2)
print(a)

from fn.fn_15_1 import add as addd, sub as subb
from fn.fn_15_1 import sub # from으로 가져와 그 안에있는 특정 함수만 import로 가져올 수 있음
b = sub(3,2)
print(b)

import random
print(random.random())

# from random import random
from random import random as rand
# print(random())
print(rand())

from fn.fn_15_1 import Hero # 다른 file의 class의 def를 가져오는 방법
h = Hero()
h.attack()
```

`import fn.fn_15_1 as fn1`을 쓰면 `fn1.add(1,2)`처럼 **모듈 이름을 붙여** 호출한다. `from fn.fn_15_1 import sub`는 가져온 이름 `sub(3,2)`을 바로 호출한다. 강사님은 `add as addd, sub`를 한 줄에서 가져오고, 나는 `add as addd`, `sub as subb`를 가져온 뒤 `sub`를 한 번 더 가져왔다. `addd`와 `subb`는 정의만 가져왔을 뿐 아래에서 호출하지 않는다.

`import random` 뒤의 `random.random()`은 모듈 이름을 붙이고, `from random import random as rand` 뒤의 `rand()`는 가져온 함수의 별칭으로 호출한다. 두 호출의 실제 난수 값은 실행할 때 달라진다. `Hero`는 양쪽 모두 `from ... import Hero`로 가져와 객체를 만든 뒤 `h.attack()`을 실행한다.

내 첫 주석의 “`import`는 숫자로 시작하면 안 된다”는 **일반적인 `import 이름` 문법에서 식별자 이름을 짓는 규칙**을 떠올린 메모다. 이 예제의 `fn_15_1`은 숫자가 **앞이 아니라 뒤**에 있어 정상적인 이름이다. “`import`와 `from`은 메모리 용량 차이가 없다”는 주석도 이 두 코드의 출력으로 확인한 결과는 아니므로 필수 규칙으로 외우지 말자.

<a id="section-3"></a>

## 3. 원본 마지막의 웹페이지 읽기

### 강사님 코드

출처: `teacher/workspace_python/_15_module.py` 26–28행 · **원본 발췌**

```python
import urllib.request
response = urllib.request.urlopen('http://google.co.kr')
print(response.read().decode('utf-8'))
```

### 내 코드

출처: `me/workspace_python/15_module.py` 30–32행 · **원본 발췌**

```python
import urllib.request
response = urllib.request.urlopen('http://www.google.co.kr')
print(response.read().decode('utf-8'))
```

두 파일 모두 `urllib.request.urlopen(...)`으로 주소를 열어 응답을 읽고 UTF-8 문자열로 바꿔 출력하는 **실제 실행 코드**가 있다. 강사님 주소는 `http://google.co.kr`, 내 주소는 `http://www.google.co.kr`다. 이 장에서는 모듈을 불러 호출하는 **수업 예제**로 설명하고, 외부 사이트의 현재 응답 내용까지 학습 결과로 고정하지 않는다. 앞의 로컬 `fn` 모듈 동작과 이 외부 요청은 성격이 다르므로, 문서 검증 과정에서 원본 전체 파일을 그대로 실행하지 않았다.

### 강사님 코드 — 별도 `requests` 실습

출처: `teacher/workspace_python/test1/main.py` 1–3행 · **원본 발췌**

```python
import requests
r = requests.get('http://google.co.kr')
print(r.text)
```

### 내 코드 — 별도 `requests` 실습

출처: `me/workspace_python/test1/main.py` 1–3행 · **원본 발췌**

```python
import requests
r = requests.get('http://www.google.co.kr')
print(r.text)
```

별도 `test1/main.py`에도 양쪽 모두 `import requests`와 `requests.get(...)`가 있다. 이 **실제 작성한 모듈 사용 예**는 위의 `urllib.request`와 함께 읽되, 외부 페이지의 내용이나 HTTP 세부 동작을 이 장의 필수 선행 지식으로 늘리지 않는다. 이 코드도 검증을 위해 외부 주소에 다시 접속하지 않았다.

<a id="section-4"></a>

## 직접 확인할 질문

1. `fn1.add(1,2)`와 `sub(3,2)`에서 이름 앞부분이 다른 이유는?
2. 내 코드에서 `addd`와 `subb`는 실제로 호출되는가?
3. `Hero`를 가져온 뒤 공격 문장을 출력하려면 어떤 순서로 호출하는가?

<a id="section-5"></a>

## 추가로 알면 좋은 것

외부 웹페이지 요청의 오류 처리, 응답 형식, HTTP 헤더를 읽는 방법은 이 두 모듈 파일에서 배우는 핵심이 아니다. 이런 내용은 필요할 때 **별도 확장**으로 다루고, 이 장의 본문에서는 실제 코드에 있는 `import`와 호출 순서를 먼저 익힌다.

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/15_Python_모듈과_import_연습문제.md) → [Python 목차에서 다음 읽을 자료 고르기](README.md)

