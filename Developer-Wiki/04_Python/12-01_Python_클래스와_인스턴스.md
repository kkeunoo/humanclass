# 12-01. 클래스와 인스턴스 — 설계와 각각의 상태 구별하기

[Python 목차](README.md) · [읽기 안내](00-00_Python_V3_동작_백과_읽기법.md)

같은 코드로 사람 두 명을 만들었는데 이름과 나이가 다르게 남는 이유는 무엇일까? 클래스의 정의와 실제 만든 인스턴스, 그 인스턴스의 속성과 메서드를 나누면 객체 코드의 흐름을 읽을 수 있다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

class·인스턴스·속성·메서드·self를 구분한다. __init__ 초기화와 실제 호출 순서, 인스턴스별 값·별칭·동적 속성, 속성과 메서드 이름 충돌을 설명한다.

실제 원본·새 예제·개선안·선택 학습을 구분하고 입력·실행 순서·반환값·출력을 연결한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

클래스는 데이터와 동작을 함께 정의하는 새 객체 종류다. Person 클래스로 만든 a·b는 그 클래스의 인스턴스다. 같은 종류여도 각 인스턴스는 자기 이름·나이 같은 상태를 가질 수 있다. 속성은 객체에 연결한 값이고 메서드는 객체의 동작을 정의한 함수다.

| 표현 | 역할 | 실행 시점 |
| --- | --- | --- |
| class Person | 클래스 정의 | 정의 코드에 도달할 때 |
| Person('민지',20) | 인스턴스를 만들고 초기화 | 호출할 때 |
| __init__ | 새 인스턴스의 초기 상태 준비 | 생성 과정에서 자동 호출 |
| self.name | 해당 인스턴스의 속성 | 그 객체 상태를 읽거나 대입 |
| a.greeting() | a의 메서드 호출 | 인스턴스 a를 self로 받아 실행 |

__init__을 클래스가 정의되는 순간 실행하는 함수라고 읽지 않는다. 인스턴스를 만들 때 초기화하는 메서드이며 객체 생성 자체의 내부 단계 전체를 이 함수 하나로 설명하지 않는다. 인스턴스 두 개를 만들면 각각 초기화가 진행된다.

self는 현재 메서드를 호출한 인스턴스를 받는 매개변수다. 보통의 인스턴스 메서드를 a.greeting()으로 호출하면 a가 전달된다. 정적·클래스 메서드까지 모든 함수에 self가 무조건 있다는 규칙은 아니며 다음 장에서 구별한다.

> 📚 **출처 · 본문 설명 확인:** [Python 클래스·인스턴스·메서드](https://docs.python.org/ko/3/tutorial/classes.html#a-first-look-at-classes). 실제 배운 문법의 의미를 확인한 근거다. 예제·표·풀이 자체는 수업 자료를 바탕으로 새로 구성했다. 외부 문장을 직접 인용하지 않았다. 이번 문법 확인 기간: 2026-10-28~29.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 코드.** [실행 파일](실습/책형_복습/12-01_Python_클래스와_인스턴스.py)을 제공한다. Python이 설치된 환경에서 새 .py 파일로 저장해 실행한다. 터미널은 그 파일이 있는 폴더에서 열고 `python 파일이름.py`를 실행한다. VS Code의 Python 실행 기능을 사용해도 된다. 결과는 터미널에 표시된다.



```python
class Person:
    def __init__(self, name, age):
        print('초기화', name)
        self.name = name
        self.age = age
    def greeting(self):
        print(f'{self.name}, {self.age}세')
print('만들기 전')
a = Person('민지', 20)
b = Person('준호', 30)
print('만들기 뒤')
a.greeting()
b.greeting()
a.name = '수정한 이름'
print(a.name, b.name)
c = a
c.age = 21
print(a.age, c is a, a is b)
b.address = '천안'
print(b.address)
```

클래스 정의만 있을 때는 초기화 출력이 없다. Person을 두 번 호출한 사이에 초기화 문구가 나오고 각 name·age를 저장한다. a의 이름 변경은 b에 영향을 주지 않는다. 반면 c=a는 같은 인스턴스의 별칭이라 c.age 변경이 a에도 보인다. b.address는 b에 새 속성을 추가한 것이며 a에 같은 속성을 만든 것은 아니다.

**예상 출력 또는 관찰:**

```text
만들기 전
초기화 민지
초기화 준호
만들기 뒤
민지, 20세
준호, 30세
수정한 이름 준호
21 True False
천안
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본 발췌다. 주석의 잘못된 설명도 원문을 보존하고 풀이에서 교정한다. 필요한 선언·호출·다른 파일의 정의는 다음 절까지 연결해 읽는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/12_class.py` 6–25행

```python
class Person:
    # __init__ 은 클래스가 생성될 때 자동으로 먼저 실행 되는 메소드
    def __init__(self) : 
        print(1)
        self.hello = '안녕하세요'

    def greeting(self): # class안에 def일 때 첫 번째 인자는 self가 필수
        # print('Hello Class')
        print(self.hello)

    def hello(self):
        self.greeting()

print(0)
james = Person()
print(2)
james.greeting()
# james.hello()

print(james)
```

**발췌 바로 풀이:** `print(0)` 뒤 `james = Person()`에서 `__init__` 안의 `print(1)`이 나오고, 그 다음 `print(2)`가 나온다. `james.greeting()`은 `self.hello`의 문자열 `'안녕하세요'`를 출력한다. `self`는 이 메서드를 호출한 **해당 인스턴스**를 가리키는 매개변수다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/12_class.py` 28–52행

```python
class Person2:
    def __init__(self, name, age) : 
        print('__init__실행')
        self.hello = '안녕하세요'
        self.name = name
        self.age = age

    def greeting(self): 
        print(f'{self.hello}! 저는 {self.name}이고 나이는 {self.age}입니다')

a = Person2('이름', 20) # Person2 class는 heap영역에 있고 a는 주소값을 가지고 있음
a.greeting()

print(a.hello) # 전달 인자가 없더라도, class내 존재하기 때문에 사용 가능
print(a.name)
print(a.age)

b = Person2('다른이름', 30) # a와는 다른 Person2를 바라보고 있는 것
b.greeting()
print(b.name)

b.addr = '천안' # 없는 항목을 추가해서 임시로 사용할 수도 있음
print(b.addr)
# print(a.addr) # a 에는 당연하게 값이 없음. a와 b는 다른 영역이기 때문

```

**발췌 바로 풀이:** `Person2('이름', 20)`의 값은 `a.name`, `a.age`에 저장되고, 다른 호출로 만든 `b`에는 별도의 `name`, `age`가 저장된다. `b.addr='천안'`은 **b에만** 속성을 추가한다. `a.addr`를 읽는 줄은 주석 처리된 이유가 있다. 마지막 `b.__init__(1,2)`는 생성자를 **직접 다시 호출**해 `b.name`, `b.age`를 1과 2로 바꾸지만, `b.addr`를 지우지는 않는다. 원래의 정상적인 사용은 객체를 만들 때 자동 호출되는 것이다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/12_class.py` 53–53행

```python
b.__init__(1,2) # 실행 됨, 다만 자동으로 실행되기 때문에 별도 실행 필요 없음
```

**발췌 바로 풀이:** 원본은 이 줄도 실제 호출한다. b의 __init__을 다시 실행해 name·age를 1·2로 덮지만 b.addr을 지우는 코드는 없으므로 그 주소는 남는다. 새 객체를 하나 더 만드는 호출은 아니며 일반적인 초기화 사용법으로 권장하는 예제가 아니다.

내 Person 주변은 print(0) → Person 호출 중 print(1) → print(2) → greeting의 안녕하세요 순서다. 원본은 self.hello 문자열 속성과 hello 메서드를 같은 이름으로 둔다. 초기화 뒤 james.hello는 문자열 속성을 찾으므로 james.hello()를 실행하면 문자열 호출 오류가 난다. 해당 호출은 내 원본에서 주석이다. Person2의 a·b는 별도 인스턴스이며 b.addr 추가는 b에만 보인다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

Person2 정의 → Person2에 이름·나이 전달 → __init__의 self는 새 인스턴스 → self.name·age 저장 → 반환된 인스턴스를 a 또는 b에 연결 → greeting 호출 때 해당 인스턴스 사용 순서다. self.name과 매개변수 name은 역할이 다르다. 오른쪽 name은 받은 값, 왼쪽 self.name은 저장할 객체 속성이다. 내 메모의 메모리 영역 이름보다 어떤 두 이름이 같은 객체를 가리키는지 먼저 관찰한다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 내 코드는 인스턴스 두 개와 한쪽에만 새 속성을 넣는 실험을 했다. **공통 이름 충돌:** hello 속성과 hello 메서드가 겹쳐 의도한 호출을 가린다. **개선:** 저장 문자열은 message, 동작은 greeting처럼 역할을 나눈다. **주석 교정:** __init__은 클래스 정의 시 실행이 아니라 인스턴스 초기화다. 객체 출력에 보이는 주소 모양은 실행마다 달라질 수 있어 고정 정답이 아니다.

개선안은 D 드라이브 원본을 수정한 결과가 아니다. 실제 오류·수업용 단순화·목적에 따른 선택을 구별한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



양쪽 초기화와 greeting 흐름은 같아 중복 인용하지 않는다. 내 추가 age 출력과 __init__ 직접 재호출은 실제 원본에 있으므로 상태 변화까지 설명한다. 서로 다른 인스턴스라는 말과 같은 인스턴스에 별칭을 붙인 경우를 구분한다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 원본 동작 | a | b |
| --- | --- | --- |
| Person2 생성 | 이름·20 | 다른이름·30 |
| b.addr 대입 | addr 없음 | 천안 추가 |
| b.__init__(1,2) | 그대로 | name=1·age=2, addr 유지 |

초기화 메서드를 다시 호출했다고 자동으로 새 인스턴스가 생기거나 모든 속성이 초기 상태로 삭제되는 것은 아니다. 해당 본문이 실제 대입하는 속성만 바뀐다. 일반 사용은 인스턴스 생성 때 자동 초기화를 이용하고, 원본의 재호출은 동작 관찰 실험으로 읽는다.

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| c=a 대신 새 Person 생성 | c.age 변경이 a에 안 보임 | 별도 인스턴스 |
| b에만 주소 추가 후 a.address 조회 | AttributeError | a에는 속성 없음 |
| 이름 인자 생략 | 필요한 인자 오류 | __init__ 정의와 불일치 |
| 속성과 메서드를 같은 이름으로 | 호출 대상을 가릴 수 있음 | 객체의 이름 충돌 |

self 관련 오류는 보통 인스턴스 메서드의 첫 매개변수와 호출 방식을 확인한다. 속성이 없으면 어느 인스턴스에 대입했는지 본다. 문자열을 호출할 수 없다는 오류는 메서드 이름을 같은 이름의 데이터가 가렸는지 확인한다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** __new__·디스크립터·객체의 메모리 배치·자동 데이터 클래스는 추가 학습이다. self라는 관례 이름을 바꿔 쓰는 실험보다 실제 인스턴스의 상태와 호출 연결을 먼저 익힌다.

TIP은 기본 문제의 필수 조건이 아니다. 배운 문법을 확인한 📚 출처와 선택 확장을 구별한다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. class를 정의하면 __init__ 출력이 바로 나오는가?
2. b.addr 대입이 a에도 속성을 만드는가?
3. c=a는 새 인스턴스 생성인가?
4. 원본 james.hello()는 왜 문제가 되는가?

<details>
<summary>풀이 — 먼저 자신의 답을 적은 뒤 펼치기</summary>

Person 호출 과정에서 초기화한다. b에만 추가한다. c는 같은 객체의 다른 이름이다. 같은 이름의 문자열 속성이 메서드를 가려 문자열을 호출하려 하기 때문이다.

</details>

| 구분 | 질문 |
| --- | --- |
| 설계 | 어느 class인가? |
| 객체 | 어느 인스턴스인가? |
| 상태 | self의 어떤 속성인가? |
| 호출 | 데이터와 메서드 이름이 겹치나? |

[장별 연습문제](실습/연습문제/12-01_Python_클래스와_인스턴스_연습문제.md) · 다음은 [속성·정적·클래스 메서드](12-02_Python_클래스속성과_메서드.md)다.

<!-- 이전 명시 앵커 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
