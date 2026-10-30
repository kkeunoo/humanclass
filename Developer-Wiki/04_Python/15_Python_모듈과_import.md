# 15. 모듈과 import — 정의가 있는 파일에서 호출한 곳까지

[Python 목차](README.md) · [읽기 안내](00-00_Python_V3_동작_백과_읽기법.md)

함수를 다른 파일로 옮기면 복사해서 붙이지 않고도 불러 사용할 수 있다. 하지만 import 한 줄만 보여 주면 함수가 무엇을 받거나 반환하는지 알기 어렵다. 정의 파일·가져오는 이름·실제 호출을 함께 읽는다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

모듈 전체·일부 이름·별칭을 구분한다. 함수·클래스 정의를 가져와 호출하는 두 파일 흐름을 설명하고 표준 모듈·설치 패키지·직접 작성한 파일을 나눈다.

실제 원본·새 예제·개선안·선택 학습을 구분하고 입력·실행 순서·반환값·출력을 연결한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

모듈은 함수·클래스·일반 문장을 담은 Python 코드 단위다. 이 실습에서는 .py 파일을 모듈로 사용한다. import book_tools as tools를 쓰면 tools가 그 모듈을 가리키므로 tools.add로 함수를 찾는다. from book_tools import sub는 현재 파일에서 sub 이름을 바로 사용하게 한다.

| 문장 | 현재 파일에 연결된 이름 | 호출 모양 |
| --- | --- | --- |
| import book_tools | 모듈 book_tools | book_tools.add(1,2) |
| import book_tools as tools | 모듈 별칭 tools | tools.add(1,2) |
| from book_tools import sub | 함수 sub | sub(3,2) |
| from book_tools import Hero | 클래스 Hero | Hero() 뒤 메서드 |

from으로 가져왔다고 함수의 본문 실행까지 자동으로 대신하지 않는다. 가져온 모듈 자체에 일반 실행 문장이 있다면 처음 읽는 과정에서 실행될 수 있지만, 여기 보조 파일은 정의만 있으므로 attack 문구는 객체 메서드를 호출할 때 나온다.

random·urllib.request는 Python 표준 라이브러리의 예이고 requests는 별도 설치하는 패키지다. 직접 쓴 fn/fn_15_1.py도 다른 종류의 모듈 근거다. 가상환경 폴더 안에 실제 작성한 test1/main.py가 있다는 이유로 그 수업 코드를 제외하지 않는다. 설치 생성물과 내 소스 파일을 구분한다.

> 📚 **출처 · 본문 설명 확인:** [Python 모듈 입문](https://docs.python.org/ko/3/tutorial/modules.html), [urllib.request](https://docs.python.org/ko/3/library/urllib.request.html), [Requests 공식 빠른 시작](https://requests.readthedocs.io/en/latest/user/quickstart/). 실제 배운 문법의 의미를 확인한 근거다. 예제·표·풀이 자체는 수업 자료를 바탕으로 새로 구성했다. 외부 문장을 직접 인용하지 않았다. 이번 문법 확인 기간: 2026-10-28~29.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 코드.** [실행 파일](실습/책형_복습/15_Python_모듈과_import.py)을 제공한다. 아래 실행 파일과 보조 파일 book_tools.py를 같은 폴더에 저장한다. 링크된 두 파일을 함께 제공하며 외부 네트워크·별도 패키지는 필요하지 않다. 실행 파일 쪽을 Python으로 실행한다. 보조 파일만 실행하면 정의만 읽고 끝나 출력이 없다.

**같은 폴더에 준비할 파일 [book_tools.py](실습/책형_복습/book_tools.py):**

```python
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

class Hero:
    def attack(self):
        print('공격한다')
```

```python
import book_tools as tools
from book_tools import sub as subtract, Hero
print(tools.add(2, 3))
print(subtract(5, 2))
hero = Hero()
hero.attack()
```

tools.add가 보조 파일의 add(2,3)을 호출해 5를 반환하고 바깥 print가 출력한다. subtract는 sub 함수에 붙인 현재 파일의 별칭이라 5-2의 3을 반환한다. Hero를 가져와 객체를 만들고 attack을 호출할 때 공격한다가 출력된다. 보조 파일의 모든 정의를 위에 실었으므로 어디서 계산하거나 출력하는지 한 줄씩 연결할 수 있다.

**예상 출력 또는 관찰:**

```text
5
3
공격한다
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본 발췌다. 주석의 잘못된 설명도 원문을 보존하고 풀이에서 교정한다. 필요한 선언·호출·다른 파일의 정의는 다음 절까지 연결해 읽는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/fn/fn_15_1.py` 2–10행

```python
def add(x, y) :
    return x + y

def sub(x, y) :
    return x - y

class Hero :
    def attack(self) :
        print('공격한다')
```

**발췌 바로 풀이:** 두 파일 모두 `add(1,2)`는 3, `sub(3,2)`는 1을 돌려주고, `Hero().attack()`은 `공격한다`를 출력한다. 이 파일 자체에는 외부 페이지 요청이나 다른 기능이 없다. 다음의 `15_module.py`가 이 이름들을 가져다 쓴다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/15_module.py` 1–28행

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

**발췌 바로 풀이:** `import fn.fn_15_1 as fn1`을 쓰면 `fn1.add(1,2)`처럼 **모듈 이름을 붙여** 호출한다. `from fn.fn_15_1 import sub`는 가져온 이름 `sub(3,2)`을 바로 호출한다. 강사님은 `add as addd, sub`를 한 줄에서 가져오고, 나는 `add as addd`, `sub as subb`를 가져온 뒤 `sub`를 한 번 더 가져왔다. `addd`와 `subb`는 정의만 가져왔을 뿐 아래에서 호출하지 않는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/15_module.py` 30–32행

```python
import urllib.request
response = urllib.request.urlopen('http://www.google.co.kr')
print(response.read().decode('utf-8'))
```

**발췌 바로 풀이:** 두 파일 모두 `urllib.request.urlopen(...)`으로 주소를 열어 응답을 읽고 UTF-8 문자열로 바꿔 출력하는 **실제 실행 코드**가 있다. 강사님 주소는 `http://google.co.kr`, 내 주소는 `http://www.google.co.kr`다. 이 장에서는 모듈을 불러 호출하는 **수업 예제**로 설명하고, 외부 사이트의 현재 응답 내용까지 학습 결과로 고정하지 않는다. 앞의 로컬 `fn` 모듈 동작과 이 외부 요청은 성격이 다르므로, 문서 검증 과정에서 원본 전체 파일을 그대로 실행하지 않았다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/test1/main.py` 1–3행

```python
import requests
r = requests.get('http://www.google.co.kr')
print(r.text)
```

**발췌 바로 풀이:** 별도 `test1/main.py`에도 양쪽 모두 `import requests`와 `requests.get(...)`가 있다. 이 **실제 작성한 모듈 사용 예**는 위의 `urllib.request`와 함께 읽되, 외부 페이지의 내용이나 HTTP 세부 동작을 이 장의 필수 선행 지식으로 늘리지 않는다. 이 코드도 검증을 위해 외부 주소에 다시 접속하지 않았다.

내 원본은 fn.fn_15_1을 fn1으로 가져와 add를 호출하고, sub도 직접 가져와 호출한다. addd·subb 별칭도 가져왔지만 실제 호출하지 않는다. Hero를 가져와 객체를 만든 뒤 attack을 호출한다. random.random과 rand는 모듈 접근과 함수 별칭 접근을 각각 관찰한다. 마지막 urllib.request와 test1의 requests는 외부 웹페이지를 읽는 실제 코드이며 이번 검수에서 원본 전체를 실행하지 않았다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

fn/fn_15_1.py의 add·sub·Hero 정의 → 15_module.py의 import → fn1.add 또는 sub → 반환값을 현재 파일에서 print → Hero 생성 → attack 본문 출력 순서다. 원본의 폴더 경로는 점으로 연결한 fn.fn_15_1이고 새 예제는 두 파일 연결에 집중하려고 같은 폴더의 book_tools로 재구성했다. 원본과 다른 파일 이름을 썼음을 명시한다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 내 코드는 모듈 별칭·함수 별칭·클래스를 모두 실제 호출과 연결했다. **주석 교정:** import는 단순 경로 안내만이 아니라 이름 연결과 모듈 로딩 과정이다. import와 from의 메모리 용량이 언제나 같다는 것은 이 실습의 측정 결과가 아니다. **이름 개선:** 사용하지 않는 별칭은 목적에 맞게 정리하면 읽는 사람이 실제 호출을 찾기 쉽다. **조건:** requests를 사용할 환경에는 그 패키지가 설치되어 있어야 한다.

개선안은 D 드라이브 원본을 수정한 결과가 아니다. 실제 오류·수업용 단순화·목적에 따른 선택을 구별한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



helper의 add·sub·Hero 동작은 양쪽 같아서 강사님 코드를 반복하지 않는다. 내 코드는 subb를 가져온 뒤 sub를 다시 가져오고 실제 sub만 호출한다. 두 원본 외부 주소의 www 유무 차이를 성공 응답 차이로 단정하지 않는다. 현재 응답은 재실행하지 않았으며 모듈 사용 범위를 기준으로 읽는다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 원본 호출 | 정의 위치 | 효과 |
| --- | --- | --- |
| fn1.add(1,2) | fn/fn_15_1.py | 3 반환 |
| sub(3,2) | 같은 보조 파일 | 1 반환 |
| Hero().attack() | 보조 파일 클래스 | 공격한다 출력 |
| random.random()·rand() | 표준 모듈 | 각각 난수 반환 |
| urlopen(...).read().decode(...) | 표준 urllib | 바이트 응답을 문자열로 해석 |
| requests.get(...).text | 설치 패키지 | 응답의 텍스트 관찰 |

난수 값·웹페이지 본문은 고정 정답이 아니다. urlopen 결과를 read하면 바이트를 받고 decode에서 문자열로 해석한다. 이 원본은 utf-8을 지정했지만 모든 웹페이지가 그 인코딩이라고 확대하지 않는다. 로컬 helper 검증과 외부 요청 성공은 구분했다.

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| tools.add 인자 변경 | 반환 합 변경 | 보조 파일 함수 실행 |
| 별칭만 바꾸고 호출은 그대로 | 이름 오류 가능 | 현재 파일 이름 연결 |
| helper를 다른 폴더로 이동 | 찾는 경로가 맞지 않으면 실패 | 모듈 탐색 조건 |
| attack 호출 제거 | 공격 문구 없음 | 정의·생성과 실제 호출은 별개 |

ModuleNotFoundError면 파일명·폴더·실행 환경을 먼저 본다. 가져온 함수가 안 보이면 import 방식에 맞는 이름으로 호출했는지 확인한다. helper만 실행해 출력이 없다고 실패로 판단하지 않는다. random.py 같은 이름을 내 파일에 쓰면 표준 모듈 이름과 충돌할 수 있으므로 목적 이름을 고른다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 패키지 배포·검색 경로의 상세 규칙·__name__ 진입점·순환 import·웹 요청의 실패와 응답 상태·헤더 처리는 추가 학습이다. 본문은 실제 정의 파일과 호출 연결을 완성하는 데 집중한다.

TIP은 기본 문제의 필수 조건이 아니다. 배운 문법을 확인한 📚 출처와 선택 확장을 구별한다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. tools.add와 subtract의 앞부분이 다른 이유는?
2. helper의 정의만 읽으면 attack 문구가 나오는가?
3. 원본 addd·subb는 실제 호출되는가?
4. requests는 Python 표준 모듈인가?

<details>
<summary>풀이 — 먼저 자신의 답을 적은 뒤 펼치기</summary>

모듈 별칭 접근과 직접 가져온 함수 별칭이기 때문이다. 메서드를 호출해야 나온다. 원본에서는 가져오기만 했다. requests는 별도 설치 패키지다.

</details>

| 단계 | 확인 |
| --- | --- |
| 정의 | 어느 파일의 함수·클래스인가? |
| 연결 | 모듈·일부 이름·별칭 |
| 호출 | 실제 인자와 반환·출력 |
| 환경 | 로컬·표준·설치 패키지 |

[장별 연습문제](실습/연습문제/15_Python_모듈과_import_연습문제.md) · [Python 목차](README.md)에서 원본 과제와 종합 복습으로 이어 간다.

<!-- 이전 명시 앵커 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
