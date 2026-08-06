---
title: Python 모듈과 import
version: v2.0-final
last_updated: 2026-08-06
status: Completed
---

# Python 모듈과 import

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `15_Python_모듈과_import.md` |
| 분류 | `04_Python` |
| 권장 선수 학습 | `11_Python_함수.md`, `12_Python_클래스.md`, `14_Python_예외처리.md` |
| 다음 학습 | `16_Python_이터레이터.md` |
| 원본 기준 | `workspace_python/15_module.py`, `workspace_python/fn/fn_15_1.py`, 강사님 동일 파일 |
| 핵심 범위 | 모듈, 패키지 경로, `import`, `from ... import ...`, `as`, 함수·클래스 가져오기, 표준 라이브러리, `urllib.request` |
| 실습 범위 | 사용자 정의 모듈의 함수와 클래스 사용, 난수 생성, 웹 문서 요청 |
| 종합 실습 | 별도 문서 `20_Python_종합실습.md`에서 관리 |
| 문서 형식 | Python Developer-Wiki V2 확정 형식 |

> 이 문서는 내 코드와 강사님 코드 전체를 나열하지 않는다.  
> 모듈을 가져오는 방식별로 필요한 코드만 발췌하고, 실행 결과·사용 목적·주의점·실무형 개선 방향을 함께 설명한다.

---

# 개요

프로그램이 커지면 모든 함수와 클래스를 하나의 파일에 작성하기 어렵다.

```text
하나의 긴 Python 파일
    ↓
함수와 클래스 증가
    ↓
코드 탐색과 수정이 어려워짐
```

이때 관련 기능을 파일별로 나누고 필요한 곳에서 가져와 사용할 수 있다.

```text
계산 기능
→ calculator.py

회원 기능
→ user.py

주문 기능
→ order.py
```

각 Python 파일을 **모듈(Module)**이라고 한다.

```text
모듈 작성
    ↓
import로 가져오기
    ↓
다른 파일에서 함수·클래스 재사용
```

모듈을 사용하면 코드를 역할별로 분리하고, 같은 기능을 여러 파일에서 반복 작성하지 않아도 된다.

---

# 핵심 개념

| 개념 | 핵심 역할 |
| --- | --- |
| 모듈 | 함수·클래스·변수 등을 담은 Python 파일 |
| 패키지 | 여러 모듈을 폴더 단위로 묶은 구조 |
| `import` | 모듈 전체를 가져옴 |
| `from ... import ...` | 모듈에서 특정 이름만 현재 파일로 가져옴 |
| `as` | 모듈·함수·클래스에 별칭을 지정 |
| 표준 라이브러리 | Python 설치 시 함께 제공되는 모듈 모음 |
| 사용자 정의 모듈 | 개발자가 직접 작성한 Python 파일 |
| 서드파티 패키지 | 별도로 설치하여 사용하는 외부 패키지 |

---

# 학습 목표

이 문서를 학습한 뒤 다음 내용을 설명하고 작성할 수 있어야 한다.

- 모듈과 패키지의 차이를 설명할 수 있다.
- 직접 만든 Python 파일을 다른 파일에서 가져올 수 있다.
- 폴더 경로를 점 표기법으로 작성할 수 있다.
- `import 모듈` 방식으로 함수와 클래스를 사용할 수 있다.
- `from 모듈 import 이름` 방식으로 특정 기능만 가져올 수 있다.
- `as`로 모듈과 함수에 별칭을 지정할 수 있다.
- 함수 이름 충돌 가능성을 이해한다.
- 사용자 정의 모듈에서 클래스를 가져와 객체를 생성할 수 있다.
- `random` 같은 표준 라이브러리를 사용할 수 있다.
- `urllib.request.urlopen()`의 기본 흐름을 설명할 수 있다.
- 응답 데이터를 `read()`하고 `decode()`하는 이유를 이해한다.
- import 경로 오류가 발생하는 대표 원인을 구분할 수 있다.
- 모듈 실행 시 최상위 코드가 실행된다는 점을 이해한다.
- `if __name__ == "__main__":`의 목적을 설명할 수 있다.

---

# 1. 모듈이란?

모듈은 Python 코드가 저장된 하나의 `.py` 파일이다.

예를 들어 다음 파일이 있다고 가정한다.

```text
fn/
└─ fn_15_1.py
```

`fn_15_1.py` 안에는 함수와 클래스가 정의되어 있다.

```python
def add(x, y):
    return x + y


def sub(x, y):
    return x - y


class Hero:
    def attack(self):
        print("공격한다")
```

이 파일을 다른 Python 파일에서 가져와 사용할 수 있다.

## 1-1. 모듈로 분리하는 이유

- 관련 기능을 파일별로 나눌 수 있다.
- 같은 코드를 여러 곳에서 재사용할 수 있다.
- 파일 하나의 길이를 줄일 수 있다.
- 기능별 테스트와 수정이 쉬워진다.
- 여러 개발자가 파일을 나누어 작업하기 쉽다.

---

# 2. 모듈과 패키지 구조

수업 파일 구조는 다음과 같다.

```text
workspace_python/
├─ 15_module.py
└─ fn/
   └─ fn_15_1.py
```

여기서:

```text
fn_15_1.py
→ 모듈

fn/
→ 모듈을 담는 폴더
→ 패키지처럼 사용
```

## 2-1. 점 표기법

폴더와 파일의 경로는 점으로 구분한다.

```python
import fn.fn_15_1
```

```text
fn
↓
fn 폴더

.

fn_15_1
↓
fn_15_1.py 모듈
```

> [!IMPORTANT]
> import 경로에서는 `/`나 `\`가 아니라 점(`.`)을 사용한다.

---

# 3. 모듈 이름 규칙

Python 모듈과 패키지 이름은 일반적으로 다음 규칙을 따른다.

- 영문 소문자 사용
- 필요한 경우 밑줄 사용
- 숫자로 시작하지 않음
- 공백 사용하지 않음
- Python 키워드 사용하지 않음

권장:

```text
calculator.py
user_service.py
file_utils.py
```

좋지 않은 예:

```text
15_module.py
user-service.py
class.py
my module.py
```

수업 파일처럼 `15_module.py`로 저장할 수는 있지만, 일반적인 import 대상 모듈 이름은 숫자로 시작하지 않도록 작성하는 것이 좋다.

> [!WARNING]
> `15_module`처럼 숫자로 시작하는 이름은 일반적인 `import 15_module` 문법으로 가져올 수 없다.

---

# 4. `import 모듈`

`import`를 사용하면 모듈 전체를 가져온다.

## 4-1. 기본 방식

```python
import fn.fn_15_1
```

함수를 사용할 때 전체 경로를 함께 작성한다.

```python
result = fn.fn_15_1.add(1, 2)
print(result)
```

## 4-2. 출력 결과

```text
3
```

## 4-3. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `import` | 다른 모듈을 현재 파일에서 사용하기 위해 |
| `fn.fn_15_1` | 패키지와 모듈 경로를 지정하기 위해 |
| `.add` | 모듈 안의 `add()` 함수를 선택하기 위해 |
| `(1, 2)` | 함수에 두 값을 전달하기 위해 |

## 4-4. 장점

전체 경로가 코드에 드러나기 때문에 함수의 출처를 쉽게 알 수 있다.

```python
fn.fn_15_1.add(1, 2)
```

```text
add()
→ fn.fn_15_1 모듈에서 가져온 함수
```

## 4-5. 단점

경로가 길면 호출 코드도 길어진다.

---

# 5. `as`로 모듈 별칭 지정

긴 모듈 경로를 짧은 이름으로 사용할 수 있다.

## 5-1. 내 코드

```python
import fn.fn_15_1 as fn1

result = fn1.add(1, 2)
print(result)
```

## 5-2. 강사님 코드

```python
import fn.fn_15_1 as fn1

result = fn1.add(1, 2)
print(result)
```

## 5-3. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `as fn1` | 긴 모듈 경로에 짧은 별칭을 지정하기 위해 |
| `fn1.add()` | 별칭을 통해 모듈의 함수를 호출하기 위해 |

## 5-4. 출력 결과

```text
3
```

## 5-5. 동작 과정

```text
fn.fn_15_1 모듈 가져오기
    ↓
현재 파일에서는 fn1이라는 이름으로 참조
    ↓
fn1.add(1, 2) 호출
    ↓
3 반환
```

> [!TIP]
> 별칭은 단순히 짧게 만드는 목적뿐 아니라, 프로젝트에서 널리 사용하는 관례를 따를 때도 사용한다.
>
> 예: `import numpy as np`, `import pandas as pd`

---

# 6. `from ... import ...`

모듈 전체 이름을 매번 작성하지 않고 특정 함수만 가져올 수 있다.

## 6-1. 내 코드

```python
from fn.fn_15_1 import sub

result = sub(3, 2)
print(result)
```

## 6-2. 강사님 코드

```python
from fn.fn_15_1 import sub

result = sub(3, 2)
print(result)
```

## 6-3. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `from fn.fn_15_1` | 기능을 가져올 모듈 경로를 지정하기 위해 |
| `import sub` | 모듈에서 `sub` 이름만 현재 파일로 가져오기 위해 |
| `sub(3, 2)` | 모듈 경로 없이 함수를 바로 호출하기 위해 |

## 6-4. 출력 결과

```text
1
```

## 6-5. 장점

호출 코드가 짧고 읽기 쉽다.

```python
sub(3, 2)
```

## 6-6. 주의점

함수 이름만 보면 어느 모듈에서 가져왔는지 바로 알기 어려울 수 있다.

```python
sub(3, 2)
```

또한 현재 파일에 같은 이름이 있으면 충돌할 수 있다.

---

# 7. 여러 이름 가져오기

한 모듈에서 여러 함수나 클래스를 가져올 수 있다.

```python
from fn.fn_15_1 import add, sub, Hero
```

여러 줄로 작성하면 변경 내역을 확인하기 쉽다.

```python
from fn.fn_15_1 import (
    Hero,
    add,
    sub,
)
```

## 7-1. 실행

```python
print(add(5, 3))
print(sub(5, 3))
```

## 7-2. 출력 결과

```text
8
2
```

> [!TIP]
> 가져오는 이름이 많아지면 괄호를 사용해 여러 줄로 나누면 가독성이 좋아진다.

---

# 8. 함수에 별칭 지정

가져온 함수에도 별칭을 붙일 수 있다.

## 8-1. 내 코드

```python
from fn.fn_15_1 import add as addd
from fn.fn_15_1 import sub as subb
```

## 8-2. 강사님 코드

```python
from fn.fn_15_1 import add as addd, sub
```

## 8-3. 실행

```python
print(addd(3, 2))
print(subb(3, 2))
```

## 8-4. 출력 결과

```text
5
1
```

## 8-5. 언제 사용할까?

- 현재 파일의 함수와 이름이 충돌할 때
- 원래 이름이 너무 길 때
- 역할을 더 분명하게 표현하고 싶을 때
- 같은 이름의 함수를 여러 모듈에서 가져올 때

예:

```python
from math import sqrt as math_sqrt
from custom_math import sqrt as custom_sqrt
```

> [!WARNING]
> `addd`, `subb`처럼 단순히 철자를 늘린 별칭은 의미가 분명하지 않다.
>
> 별칭은 기능이나 출처를 더 잘 드러내도록 작성한다.

---

# 9. `import`와 `from import` 비교

| 방식 | 사용 예 | 장점 | 주의점 |
| --- | --- | --- | --- |
| `import module` | `module.add()` | 출처가 명확함 | 호출이 길어질 수 있음 |
| `import module as m` | `m.add()` | 짧고 출처도 표시됨 | 별칭을 알아야 함 |
| `from module import add` | `add()` | 호출이 간결함 | 출처·이름 충돌 주의 |
| `from module import add as plus` | `plus()` | 충돌 방지 가능 | 별칭이 과하면 혼란 |

## 9-1. 메모리 차이에 대한 주의

원본 주석에는 다음 내용이 있다.

```text
import로 하든 from으로 하든 메모리 용량 차이는 없으며
경로를 알려주는 것
```

핵심적으로 Python은 같은 모듈을 처음 가져올 때 실행하고, 이후에는 `sys.modules`에 저장된 모듈 객체를 재사용한다.

하지만 다음 표현이 더 정확하다.

```text
import 방식의 핵심 차이
→ 모듈을 몇 번 새로 실행하느냐가 아니라
→ 현재 파일의 이름 공간에 어떤 이름을 연결하느냐
```

```python
import fn.fn_15_1
```

현재 이름 공간에는 주로 모듈 경로가 연결된다.

```python
from fn.fn_15_1 import add
```

현재 이름 공간에는 `add`라는 이름이 직접 연결된다.

> [!IMPORTANT]
> `import`와 `from import`의 선택 기준을 단순히 메모리 용량으로 판단하지 않는다.
>
> **출처의 명확성, 이름 충돌 가능성, 가독성**을 기준으로 선택한다.

---

# 10. 클래스를 다른 모듈에서 가져오기

함수뿐 아니라 클래스도 가져올 수 있다.

## 10-1. 내 코드

```python
from fn.fn_15_1 import Hero

hero = Hero()
hero.attack()
```

## 10-2. 강사님 코드

```python
from fn.fn_15_1 import Hero

hero = Hero()
hero.attack()
```

## 10-3. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `import Hero` | 다른 모듈에 정의된 클래스를 가져오기 위해 |
| `Hero()` | 가져온 클래스로 객체를 생성하기 위해 |
| `hero.attack()` | 생성한 객체의 인스턴스 메서드를 호출하기 위해 |

## 10-4. 출력 결과

```text
공격한다
```

## 10-5. 동작 과정

```text
fn_15_1.py의 Hero 클래스 가져오기
    ↓
현재 파일에서 Hero 이름 사용 가능
    ↓
Hero() 객체 생성
    ↓
hero.attack() 실행
```

---

# 11. 모듈을 import할 때 실행되는 코드

Python은 모듈을 처음 import할 때 해당 파일의 최상위 코드를 실행한다.

예:

```python
# sample.py

print("sample 모듈 실행")


def add(x, y):
    return x + y
```

다른 파일에서:

```python
import sample
```

출력:

```text
sample 모듈 실행
```

함수를 호출하지 않았지만 최상위 `print()`가 실행된다.

> [!WARNING]
> 모듈 파일의 최상위에 테스트 코드나 네트워크 요청을 작성하면 import하는 순간 실행될 수 있다.

---

# 12. `if __name__ == "__main__":`

모듈을 직접 실행할 때만 테스트 코드가 실행되도록 구분할 수 있다.

```python
def add(x, y):
    return x + y


if __name__ == "__main__":
    print(add(1, 2))
```

## 12-1. 직접 실행

```text
python fn_15_1.py
    ↓
__name__ == "__main__"
    ↓
테스트 코드 실행
```

## 12-2. 다른 파일에서 import

```text
import fn.fn_15_1
    ↓
__name__은 모듈 경로 이름
    ↓
테스트 코드 실행 안 됨
```

## 12-3. 왜 사용할까?

- 모듈 내부 기능을 간단히 테스트할 수 있다.
- 다른 파일에서 import할 때 테스트 코드가 실행되는 것을 막는다.
- 재사용 코드와 직접 실행 코드를 구분할 수 있다.

> [!IMPORTANT]
> import 대상 파일에는 함수·클래스 정의를 중심으로 두고, 직접 실행할 테스트 코드는 `if __name__ == "__main__":` 아래에 둔다.

---

# 13. 표준 라이브러리

Python 설치 시 함께 제공되는 모듈을 표준 라이브러리라고 한다.

예:

- `random`
- `math`
- `datetime`
- `pathlib`
- `json`
- `urllib`
- `traceback`

별도 설치 없이 import하여 사용할 수 있다.

```python
import random
```

> [!TIP]
> 표준 라이브러리는 “직접 만든 모듈”은 아니지만 사용하는 방식은 동일하게 `import`를 사용한다.

---

# 14. `random` 모듈 전체 가져오기

## 14-1. 내 코드

```python
import random

print(random.random())
```

## 14-2. 강사님 코드

```python
import random

print(random.random())
```

## 14-3. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `import random` | 난수 관련 기능이 있는 모듈을 가져오기 위해 |
| `random.random()` | `0.0` 이상 `1.0` 미만의 임의 실수를 얻기 위해 |

## 14-4. 출력 예시

```text
0.428196348273
```

실행할 때마다 값이 달라질 수 있다.

```text
0.0 <= 결과 < 1.0
```

---

# 15. `random()` 함수만 가져오기

## 15-1. 내 코드

```python
from random import random as rand

print(rand())
```

## 15-2. 강사님 코드

```python
from random import random as rand

print(rand())
```

## 15-3. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `from random import random` | `random` 모듈에서 `random()` 함수만 가져오기 위해 |
| `as rand` | 모듈 이름과 함수 이름이 같은 혼동을 줄이기 위해 |
| `rand()` | 별칭으로 난수 함수를 호출하기 위해 |

## 15-4. 출력 예시

```text
0.8317294651
```

## 15-5. 두 방식 비교

```python
import random

random.random()
```

```python
from random import random as rand

rand()
```

첫 번째 방식은 함수가 어느 모듈에서 왔는지 더 분명하다.

두 번째 방식은 호출이 짧다.

---

# 16. 이름 충돌 주의

다음 코드는 읽을 때 혼란을 줄 수 있다.

```python
from random import random

random = random()
```

첫 번째 `random`은 함수였지만, 대입 후에는 실수값을 가리킨다.

```text
random
→ 처음에는 함수
→ 이후에는 float 값
```

권장:

```python
from random import random

random_value = random()
```

또는:

```python
import random

random_value = random.random()
```

> [!WARNING]
> 모듈·함수와 같은 이름을 변수에 사용하면 기존 이름을 덮어쓸 수 있다.

---

# 17. `urllib.request`

`urllib.request`는 URL로 요청을 보내고 응답을 받을 수 있는 표준 라이브러리 모듈이다.

## 17-1. 내 코드

```python
import urllib.request

response = urllib.request.urlopen(
    "http://www.google.co.kr"
)

print(response.read().decode("utf-8"))
```

## 17-2. 강사님 코드

```python
import urllib.request

response = urllib.request.urlopen(
    "http://google.co.kr"
)

print(response.read().decode("utf-8"))
```

두 코드는 주소 표기만 조금 다르고 동작 흐름은 같다.

## 17-3. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `urllib.request` | URL 요청 기능을 사용하기 위해 |
| `urlopen()` | 지정한 주소로 요청을 보내기 위해 |
| `response` | 서버가 반환한 응답 객체를 저장하기 위해 |
| `response.read()` | 응답 본문을 바이트 데이터로 읽기 위해 |
| `.decode("utf-8")` | 바이트 데이터를 문자열로 변환하기 위해 |

---

# 18. 웹 응답 읽기 흐름

```text
urlopen(URL)
    ↓
서버에 요청
    ↓
응답 객체 반환
    ↓
response.read()
    ↓
bytes 데이터
    ↓
decode("utf-8")
    ↓
str 문자열
```

## 18-1. 자료형 확인 예시

```python
import urllib.request

response = urllib.request.urlopen(
    "https://example.com"
)

data = response.read()

print(type(data))
```

출력:

```text
<class 'bytes'>
```

문자열로 변환:

```python
html = data.decode("utf-8")

print(type(html))
```

출력:

```text
<class 'str'>
```

---

# 19. 웹 요청 시 주의점

웹 요청은 항상 성공한다고 보장할 수 없다.

실패 원인:

- 인터넷 연결 없음
- 주소 오타
- 서버 응답 지연
- 접속 거부
- HTTP 상태 오류
- 문자 인코딩 차이
- 리다이렉트 또는 보안 정책

따라서 예외 처리와 함께 사용하는 것이 좋다.

```python
import urllib.error
import urllib.request


try:
    response = urllib.request.urlopen(
        "https://example.com",
        timeout=5,
    )
except urllib.error.URLError as error:
    print("요청 실패:", error)
else:
    html = response.read().decode("utf-8")
    print(html)
```

> [!IMPORTANT]
> 네트워크 요청은 외부 환경에 의존하므로 예외 처리와 제한 시간(`timeout`)을 함께 고려한다.

---

# 20. 응답 객체 닫기

네트워크 응답도 사용 후 닫아주는 것이 좋다.

`with`문을 사용하면 블록이 끝날 때 정리된다.

```python
import urllib.request


with urllib.request.urlopen(
    "https://example.com",
    timeout=5,
) as response:
    html = response.read().decode("utf-8")

print(html)
```

## 20-1. 개선된 점

- 응답 객체가 자동으로 정리된다.
- 코드가 간결하다.
- 예외가 발생해도 자원 정리가 쉽다.

---

# 21. 문자 인코딩 주의

모든 웹 문서가 항상 UTF-8이라고 단정할 수는 없다.

```python
response.read().decode("utf-8")
```

응답의 실제 인코딩이 다르면 `UnicodeDecodeError`가 발생할 수 있다.

기초 단계에서는 UTF-8 예제를 이해하되, 실무에서는 응답 헤더의 문자셋을 확인하거나 전용 HTTP 라이브러리의 기능을 활용한다.

> [!WARNING]
> 웹 응답의 인코딩을 무조건 UTF-8로 가정하면 일부 사이트에서 디코딩 오류가 발생할 수 있다.

---

# 22. import 경로는 어디를 기준으로 찾을까?

Python은 모듈 검색 경로에서 import 대상을 찾는다.

대표적으로 다음 위치가 포함된다.

- 현재 실행 환경의 경로
- 프로젝트에 설정된 경로
- Python 표준 라이브러리 경로
- 설치된 패키지 경로

검색 경로를 확인할 수 있다.

```python
import sys

for path in sys.path:
    print(path)
```

> [!TIP]
> 모듈 파일이 같은 프로젝트에 있어도 실행 위치와 프로젝트 설정에 따라 import 오류가 발생할 수 있다.

---

# 23. `ModuleNotFoundError`

모듈을 찾지 못하면 다음 오류가 발생한다.

```text
ModuleNotFoundError
```

## 23-1. 대표 원인

- 파일명 또는 폴더명 오타
- 현재 프로젝트 밖의 경로
- 실행 위치가 예상과 다름
- 패키지 구조가 올바르지 않음
- 설치되지 않은 외부 패키지
- 모듈 이름이 다른 파일과 충돌

## 23-2. 점검 순서

```text
파일 실제 존재 여부 확인
    ↓
이름 철자 확인
    ↓
폴더 구조 확인
    ↓
실행 위치 확인
    ↓
sys.path 확인
```

---

# 24. `AttributeError`

모듈은 찾았지만 해당 함수나 클래스가 없으면 오류가 발생할 수 있다.

```python
import fn.fn_15_1 as fn1

fn1.multiply(2, 3)
```

`fn_15_1.py`에 `multiply()`가 없다면:

```text
AttributeError
```

확인할 내용:

- 함수명 철자
- 함수가 실제 모듈 최상위에 정의되어 있는지
- 다른 이름으로 변경되지 않았는지
- 잘못된 모듈을 import하지 않았는지

---

# 25. 순환 import

두 모듈이 서로를 import하면 문제가 발생할 수 있다.

```text
a.py
→ import b

b.py
→ import a
```

두 파일이 초기화되는 도중 서로의 아직 정의되지 않은 이름을 사용하면 오류가 발생한다.

## 25-1. 개선 방향

- 공통 기능을 별도 모듈로 분리
- 클래스 책임 재검토
- 함수 내부에서 지연 import가 필요한지 검토
- 모듈 간 의존 방향을 단순하게 유지

> [!WARNING]
> 순환 import는 단순 import 문법 문제가 아니라 모듈의 역할과 의존 관계가 꼬였다는 신호일 수 있다.

---

# 26. `from module import *`를 피하는 이유

다음 문법으로 모듈의 여러 이름을 한꺼번에 가져올 수 있다.

```python
from fn.fn_15_1 import *
```

하지만 일반적으로 권장하지 않는다.

이유:

- 어떤 이름이 들어왔는지 알기 어렵다.
- 현재 파일의 이름과 충돌할 수 있다.
- 자동 완성과 정적 분석이 어려워진다.
- 코드만 보고 함수 출처를 알기 어렵다.

권장:

```python
from fn.fn_15_1 import Hero, add, sub
```

또는:

```python
import fn.fn_15_1 as fn1
```

---

# 27. 사용자 정의 모듈 구조 개선

수업 파일:

```text
fn/
└─ fn_15_1.py
```

기능이 늘어나면 역할별로 나눌 수 있다.

```text
my_app/
├─ main.py
└─ services/
   ├─ calculator.py
   └─ hero.py
```

`calculator.py`:

```python
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y
```

`hero.py`:

```python
class Hero:
    def attack(self):
        print("공격한다")
```

`main.py`:

```python
from services.calculator import add
from services.hero import Hero


print(add(1, 2))

hero = Hero()
hero.attack()
```

## 27-1. 개선된 점

- 계산 함수와 게임 클래스를 분리했다.
- 파일 이름만 보고 역할을 알 수 있다.
- 기능이 커져도 유지보수하기 쉽다.
- 한 모듈이 너무 많은 책임을 갖지 않는다.

---

# 28. 절대 import와 상대 import

프로젝트 내부 패키지에서는 절대 import와 상대 import를 볼 수 있다.

## 28-1. 절대 import

```python
from my_app.services.calculator import add
```

프로젝트 최상위 패키지부터 전체 경로를 작성한다.

## 28-2. 상대 import

```python
from .calculator import add
```

현재 패키지를 기준으로 경로를 작성한다.

## 28-3. 비교

| 방식 | 장점 | 주의점 |
| --- | --- | --- |
| 절대 import | 전체 경로가 명확함 | 경로가 길 수 있음 |
| 상대 import | 같은 패키지 내부 경로가 짧음 | 실행 방식에 따라 혼란 가능 |

초보 단계에서는 프로젝트 구조가 명확히 보이는 절대 import부터 익히는 것이 좋다.

---

# 29. 기존 코드에서 개선 코드로 바꾼 이유

## 29-1. 별칭 이름 개선

기존:

```python
from fn.fn_15_1 import add as addd
```

개선:

```python
from fn.fn_15_1 import add
```

또는 이름 충돌이 있다면:

```python
from fn.fn_15_1 import add as calculate_sum
```

이유:

- `addd`는 의미가 분명하지 않다.
- 별칭은 기능이나 출처를 설명해야 한다.

## 29-2. 함수 이름 개선

기존:

```python
def sub(x, y):
    return x - y
```

개선:

```python
def subtract(x, y):
    return x - y
```

`sub`도 널리 이해할 수 있지만, 학습 문서에서는 전체 단어가 더 명확할 수 있다.

## 29-3. 네트워크 예외 처리 추가

기존:

```python
response = urllib.request.urlopen(url)
```

개선:

```python
try:
    response = urllib.request.urlopen(
        url,
        timeout=5,
    )
except urllib.error.URLError as error:
    print("요청 실패:", error)
```

이유:

- 외부 서버 요청은 실패할 수 있다.
- 응답 지연을 무한정 기다리지 않게 한다.
- 사용자에게 실패 원인을 안내할 수 있다.

## 29-4. `with`문 사용

기존:

```python
response = urllib.request.urlopen(url)
html = response.read()
```

개선:

```python
with urllib.request.urlopen(url) as response:
    html = response.read()
```

이유:

- 응답 객체를 안전하게 정리할 수 있다.

## 29-5. 테스트 코드 분리

기존 모듈 최상위:

```python
print(add(1, 2))
```

개선:

```python
if __name__ == "__main__":
    print(add(1, 2))
```

이유:

- import할 때 테스트 출력이 실행되지 않는다.
- 모듈 재사용성이 높아진다.

---

# 30. 대표 오류로 이해하기

## 30-1. 모듈 경로에 슬래시 사용

잘못된 코드:

```text
import fn/fn_15_1
```

Python import 문법에서는 점을 사용한다.

```python
import fn.fn_15_1
```

---

## 30-2. 존재하지 않는 이름 가져오기

```python
from fn.fn_15_1 import multiply
```

모듈에 `multiply`가 없으면 `ImportError`가 발생한다.

---

## 30-3. 함수 이름 덮어쓰기

```python
from random import random

random = 10
random()
```

`random` 이름이 숫자로 바뀌었기 때문에 호출할 수 없다.

```text
TypeError: 'int' object is not callable
```

---

## 30-4. import 순간 실행되는 코드

```python
# module_a.py
print("실행됨")
```

```python
import module_a
```

함수를 호출하지 않아도 `실행됨`이 출력된다.

테스트 코드는 `if __name__ == "__main__":` 아래로 이동한다.

---

## 30-5. 숫자로 시작하는 모듈 이름

```text
import 15_module
```

문법 오류가 발생한다.

권장 파일명:

```text
module_15.py
module_example.py
```

---

## 30-6. 웹 응답을 바로 문자열로 착각

```python
data = response.read()

print(type(data))
```

`read()` 결과는 일반적으로 `bytes`이므로 문자열 처리가 필요하면 디코딩한다.

```python
text = data.decode("utf-8")
```

---

# 31. 모듈 의존 구조

```text
15_module.py
    ↓ import
fn.fn_15_1
├─ add()
├─ sub()
└─ Hero
   └─ attack()
```

```text
main.py
├─ calculator 모듈 사용
├─ hero 모듈 사용
├─ random 표준 모듈 사용
└─ urllib.request 표준 모듈 사용
```

좋은 의존 구조는 한 방향으로 이해하기 쉽다.

```text
main
→ service
→ utility
```

서로 양방향으로 import하는 구조는 피하는 것이 좋다.

---

# 32. 자주 하는 실수

## 32-1. 파일 경로와 import 경로 혼동

파일 시스템 경로는 `/`, `\`를 사용하지만 import는 점을 사용한다.

## 32-2. 숫자로 시작하는 모듈 이름 사용

일반 import 문법에서 사용할 수 없다.

## 32-3. 별칭을 의미 없이 작성

짧기만 하고 의미가 없는 별칭은 가독성을 떨어뜨린다.

## 32-4. 함수와 같은 이름의 변수 사용

가져온 함수나 모듈을 덮어쓸 수 있다.

## 32-5. `from module import *` 사용

이름 충돌과 출처 확인이 어려워진다.

## 32-6. 모듈 최상위에 실행 코드 작성

import 순간 의도하지 않은 코드가 실행될 수 있다.

## 32-7. import 오류를 파일 부재로만 판단

실행 위치, `sys.path`, 이름 충돌도 확인해야 한다.

## 32-8. 네트워크 요청을 예외 처리 없이 실행

인터넷이나 서버 상태에 따라 프로그램이 중단될 수 있다.

## 32-9. 웹 응답의 인코딩을 항상 UTF-8로 가정

다른 인코딩이면 디코딩 오류가 발생할 수 있다.

## 32-10. 한 모듈에 관련 없는 기능을 모두 작성

계산 함수와 게임 클래스처럼 역할이 다른 코드는 분리하는 것이 좋다.

## 32-11. 순환 import 생성

모듈 초기화 순서 문제와 강한 결합이 발생할 수 있다.

## 32-12. 표준 라이브러리 이름과 같은 파일 생성

프로젝트에 `random.py`, `urllib.py` 같은 파일을 만들면 표준 모듈 대신 현재 파일이 import될 수 있다.

---

# 33. 면접·복습 포인트

## Q1. 모듈이란 무엇인가요?

함수, 클래스, 변수 등을 담아 다른 파일에서 재사용할 수 있는 Python 파일이다.

## Q2. 패키지란 무엇인가요?

관련 모듈을 폴더 단위로 묶은 구조다.

## Q3. `import module`과 `from module import name`의 차이는 무엇인가요?

전자는 모듈을 이름 공간에 연결해 `module.name`으로 사용하고, 후자는 특정 이름을 현재 이름 공간에 직접 연결한다.

## Q4. `as`는 왜 사용하나요?

긴 이름을 줄이거나 이름 충돌을 피하고 역할을 더 분명하게 표현하기 위해 사용한다.

## Q5. `from module import *`를 권장하지 않는 이유는 무엇인가요?

어떤 이름이 들어왔는지 알기 어렵고 이름 충돌과 출처 확인 문제가 생기기 때문이다.

## Q6. 모듈을 import하면 내부 코드가 실행되나요?

처음 import될 때 모듈 최상위 코드가 실행된다.

## Q7. `if __name__ == "__main__":`은 왜 사용하나요?

파일을 직접 실행할 때만 테스트나 실행 코드가 동작하고, import할 때는 실행되지 않도록 구분하기 위해 사용한다.

## Q8. `ModuleNotFoundError`가 발생하는 이유는 무엇인가요?

모듈 경로 오타, 실행 위치, 검색 경로, 설치 여부, 이름 충돌 등의 문제로 모듈을 찾지 못했기 때문이다.

## Q9. `random.random()`은 어떤 값을 반환하나요?

`0.0` 이상 `1.0` 미만의 임의 실수를 반환한다.

## Q10. `response.read()`의 결과는 어떤 자료형인가요?

일반적으로 `bytes`이며 문자열로 사용하려면 적절한 인코딩으로 디코딩해야 한다.

## Q11. 네트워크 요청에 예외 처리가 필요한 이유는 무엇인가요?

인터넷 연결, 서버 상태, 주소 오류, 시간 초과 등 외부 요인으로 실패할 수 있기 때문이다.

## Q12. 순환 import란 무엇인가요?

두 개 이상의 모듈이 서로를 import하여 초기화 순서와 의존 관계 문제가 발생하는 구조다.

---

# 34. 핵심 요약

```text
모듈
→ 함수·클래스·변수를 담은 Python 파일

패키지
→ 여러 모듈을 폴더로 묶은 구조

import module
→ module.name 형태로 사용

from module import name
→ name을 바로 사용

as
→ 모듈이나 함수에 별칭 지정
```

```text
사용자 정의 모듈
→ 직접 만든 Python 파일

표준 라이브러리
→ Python이 기본 제공하는 모듈

urlopen()
→ URL 요청 후 응답 객체 반환

read()
→ 응답 데이터를 bytes로 읽기

decode()
→ bytes를 문자열로 변환
```

---

# 35. 최종 체크리스트

- [ ] 모듈과 패키지의 역할을 구분했는가?
- [ ] 모듈 이름이 숫자로 시작하지 않는가?
- [ ] import 경로에 점 표기법을 사용했는가?
- [ ] `import`와 `from import` 중 출처가 더 명확한 방식을 선택했는가?
- [ ] 별칭이 기능이나 출처를 이해하는 데 도움이 되는가?
- [ ] 가져온 함수·모듈 이름을 변수로 덮어쓰지 않았는가?
- [ ] `from module import *`를 피했는가?
- [ ] import 대상 파일의 테스트 코드를 `__main__` 조건으로 분리했는가?
- [ ] 한 모듈이 하나의 주요 역할을 담당하는가?
- [ ] 순환 import 가능성이 없는가?
- [ ] 네트워크 요청에 예외 처리와 timeout을 적용했는가?
- [ ] 응답 데이터의 자료형과 인코딩을 확인했는가?
- [ ] 표준 라이브러리와 같은 이름의 파일을 만들지 않았는가?

---

# 마무리

모듈의 목적은 단순히 파일을 여러 개로 나누는 것이 아니다.

```text
관련 기능을 역할별로 분리하고
    ↓
명확한 경로로 필요한 기능을 가져오며
    ↓
이름 충돌과 의존 관계를 줄이고
    ↓
여러 파일과 프로젝트에서 코드를 재사용하는 것
```

이 흐름을 이해하면 앞으로 더 큰 Python 프로젝트와 패키지 구조를 훨씬 체계적으로 관리할 수 있다.
