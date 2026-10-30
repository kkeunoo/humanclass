# 12-02. 클래스의 상태와 메서드 — 인스턴스·공통 값·호출 인수

[Python 목차](README.md) · [읽기 안내](00-00_Python_V3_동작_백과_읽기법.md)

각 지점의 이름은 다른데 브랜드는 같을 수 있다. 한 객체가 가진 값과 클래스의 공통 값을 나누고, 메서드가 인스턴스·클래스·일반 인자 중 무엇을 받는지 확인한다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

이중 밑줄 속성의 이름 변경과 별도 속성 대입을 구별한다. 클래스 속성·인스턴스 속성, 인스턴스·정적·클래스 메서드를 비교하고 생성 횟수와 실제 메서드 호출 유무를 추적한다.

실제 원본·새 예제·개선안·선택 학습을 구분하고 입력·실행 순서·반환값·출력을 연결한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

클래스 몸체의 brand는 클래스에 연결한 속성이고 self.name은 각 인스턴스에 대입한 속성이다. 인스턴스에서 같은 이름의 값이 없다면 클래스 속성을 찾아 읽을 수 있다. 공통 값을 읽는 경로와 모든 객체마다 같은 데이터를 별도로 저장하는 것을 구별한다.

| 메서드 | 자동으로 받는 대상 | 원본 예 |
| --- | --- | --- |
| 인스턴스 메서드 | 해당 인스턴스 self | pay·greeting |
| @staticmethod | 인스턴스·클래스 자동 인수 없음 | Calc.add(x,y) |
| @classmethod | 해당 클래스 cls | Person4.print_count(cls) |

@ 표시는 이 메서드의 호출 방식을 정하는 데 사용한 데코레이터다. 새로운 데코레이터를 직접 구현하는 내용까지 배웠다는 뜻은 아니다. staticmethod는 인스턴스 상태가 필요 없는 계산을 클래스와 함께 둘 때 이 원본에서 사용한다.

클래스 안 __money 같은 이름은 이름 변경 규칙의 대상이다. 완전한 비밀 금고처럼 모든 외부 접근을 차단하는 보안 기능은 아니다. 밖에서 a.__money를 대입하면 안에서 쓰던 이름과 다른 속성이 생길 수 있다. 제공된 pay 메서드로 상태를 다루는 의도를 먼저 읽는다.

> 📚 **출처 · 본문 설명 확인:** [Python 클래스 속성·비공개 이름](https://docs.python.org/ko/3/tutorial/classes.html), [staticmethod·classmethod](https://docs.python.org/ko/3/library/functions.html). 실제 배운 문법의 의미를 확인한 근거다. 예제·표·풀이 자체는 수업 자료를 바탕으로 새로 구성했다. 외부 문장을 직접 인용하지 않았다. 이번 문법 확인 기간: 2026-10-28~29.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 코드.** [실행 파일](실습/책형_복습/12-02_Python_클래스속성과_메서드.py)을 제공한다. Python이 설치된 환경에서 새 .py 파일로 저장해 실행한다. 터미널은 그 파일이 있는 폴더에서 열고 `python 파일이름.py`를 실행한다. VS Code의 Python 실행 기능을 사용해도 된다. 결과는 터미널에 표시된다.



```python
class Wallet:
    def __init__(self, money):
        self.__money = money
    def pay(self, price):
        self.__money -= price
        return self.__money
wallet = Wallet(10000)
print(wallet.pay(3000))
wallet.__money = 9999999
print(wallet.pay(3000))
class Shop:
    brand = '연습 빵집'
    def __init__(self, branch):
        self.branch = branch
a = Shop('천안')
b = Shop('아산')
print(a.branch, b.branch, Shop.brand)
class Calc:
    @staticmethod
    def add(x, y):
        return x + y
print(Calc.add(1, 2))
class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1
    @classmethod
    def get_count(cls):
        return cls.count
p1 = Counter()
p2 = Counter()
p3 = Counter()
print(Counter.get_count())
```

밖에서 wallet.__money에 큰 수를 대입해도 pay가 다루는 내부 값은 7000에서 4000으로 감소한다. Shop의 지점명은 두 인스턴스에 따로 있고 brand는 클래스에서 읽는다. Calc.add는 인스턴스를 만들지 않고 호출한다. Counter는 세 번 초기화하여 클래스 count가 3이다. 원본은 남은 돈과 count를 메서드 안에서 출력하지만 새 예제는 값을 반환하여 바깥 print에서 관찰하도록 구별했다.

**예상 출력 또는 관찰:**

```text
7000
4000
천안 아산 연습 빵집
3
3
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본 발췌다. 주석의 잘못된 설명도 원문을 보존하고 풀이에서 교정한다. 필요한 선언·호출·다른 파일의 정의는 다음 절까지 연결해 읽는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/12_class.py` 55–81행

```python
class Person3:
    def __init__(self, money) : 
        self.hello = '안녕하세요'
        self.__money = money
        self.___money = money

    def pay(self, price) :
        self.__money -= price
        print('남은 돈 : ', self.__money)
        self.__study()

    def __study(self) :
        print('히히 나 혼자 레벨 업')

a = Person3(10000)
a.pay(3000)

print(a.hello)
# print(a.money) # __속성을 하면 비공개로 전환되어 속성이 없다고 에러가 출력됨
a.__money = 9999999 # 비공개여서 없다고 뜨지만, 추가되는 것
a.pay(3000)
# a.__study() # AttributeError: 'Person3' object has no attribute '__study'

# __붙은 변수나 함수는 내부에서는 접근 가능하나, 외부에서는 노출되지 않는다
# 캡슐화 뜨는 은닉화
# print(a.___money) # 이미 __가 있기 때문에 뒤에 더 붙인다고 해도 오류 남 (__ + _money)

```

**발췌 바로 풀이:** `a=Person3(10000)` 뒤 `a.pay(3000)`을 두 번 실행하면 `__money`는 **7000, 4000** 순으로 줄어든다. 중간의 `a.__money=...`는 클래스 안에서 쓰는 기존 `__money`를 바꾼 것이 아니라, **별도의 새 속성**을 인스턴스에 붙인다. 그래서 두 번째 `pay` 계산에 그 큰 숫자가 쓰이지 않는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/12_class.py` 84–125행

```python
class Knotted :
    # 입구에서 선언하면 모든 Knotted라는 class가 공통적으로 가지고 있게 됨
    # 정적속성(static attribute) : 클래스를 생성하지 않고 사용이 가능하기 때문에, 메모리의 static영역에 존재(self 사용 못 함)
    # self는 생성 된 이후에나 사용이 가능하기 때문
    brand = '노티드-디저트맛집'

    def __init__(self, name, addr) :
        # self.brand = '노티드-디저트맛집'
        self.name = name
        self.addr = addr
    def info(self): # 공통적으로 쓰는 것 중에는, static 또는 method 영역이라고 불리는 공간이 있음
        print(self.name)

k1 = Knotted('천안점', '천안') # @staticmethod를 사용하면, 이것처럼 생성 없이 사용할 순 있으나,
k2 = Knotted('아산점', '아산') # 메모리에 바로 올라가있기 때문에 낭비가 될 순 있음 (각 장점, 단점)

print(k1.name, k1.brand) # 이렇게 하면 brand가 공통이라도, k1의 주소를 거쳐 지나감
print(k2.name, k2.brand) 

print(k1.name, Knotted.brand) # 이 방식이 더욱 빠르게 공통 영역에 접근할 수 있음
print(k2.name, Knotted.brand)

print('-'*30)
class Calc :
    PI = 3.141592

    def __init__(self) :
        self.meat = 200

    # 공통으로 사용할 수 있도록 선언, 데코레이터라고 부름
    # self는 생성을 해야 사용할 수 있는 것이기 때문에, 클래스나 스태틱으로 선언을 해두면 미사용
    @staticmethod 
    def add(x, y) :
    # def add(self, x, y) :
        # print(self.meat)
        return x + y

    def plus(self, x, y) :
        return self.add(x, y) # == return Calc.add(x, y)

print( Calc.add(1,2) * Calc.PI ) # class명.함수 로 접근하면 정적메소드
# print( Calc.add(Calc(), 1,2) * Calc.PI ) # add에 self를 넣었을 때 첫 번째 인자에 생성을 해줘야 사용 가능
```

**발췌 바로 풀이:** `Knotted.brand`는 클래스에 정의된 **공통 속성**이다. `k1.name`과 `k2.name`은 각각 다르지만 두 인스턴스에서 읽은 `brand`는 같다. 내 주석의 “static 영역에 있다”, “클래스 이름으로 접근하면 더 빠르다”는 말은 이 예제로 확인한 결과가 아니다. 우선 **클래스에 속한 값과 인스턴스마다 다른 값**을 구분하자.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/12_class.py` 127–153행

```python
class Person4 :
    count = 0

    def __init__(self) :
        Person4.count += 1

    @classmethod
    def print_count(cls) :
        print(f'{cls.count}명 생성됨')

p1 = Person4()
p2 = Person4()
p3 = Person4()
Person4.print_count()

class Account :
    def __init__(self) :
        self.__balance = 0

    def setBalance(self, money) :
        self.__balance = money

    def getBalance(self) :
        return self.__balance

a1 = Account()
# a1.balance = 99999
```

**발췌 바로 풀이:** `Person4.count`는 클래스에 저장한 생성 수다. 세 번 `Person4()`를 호출하면 `__init__`에서 1씩 늘어 **3**이 된다. `@classmethod`가 붙은 `print_count(cls)`는 클래스의 `count`를 읽어 출력한다. 두 파일의 출력 문구는 조금 다르지만 카운트 방식은 같다. 아래 `Account`는 `setBalance()`와 `getBalance()`를 정의하지만, 두 원본 모두 `a1=Account()`까지만 실행한다. **잔액을 변경하거나 조회하는 호출은 없다.**

내 Person3는 __money·___money를 준비하고 pay에서 __money를 줄인 뒤 __study를 호출한다. 밖의 __money 대입은 다른 속성이라 다음 pay는 4000이다. Knotted는 클래스 brand와 인스턴스 name·addr를 나누고 Calc는 정적 add와 일반 plus를 연결한다. Person4 세 개 생성 뒤 print_count를 호출한다. Account는 setter·getter를 정의했지만 원본은 생성까지만 하여 잔액 변경·조회 결과를 출력한 것으로 설명하지 않는다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

Person3 생성 → 인스턴스 안 상태 준비 → pay(self,price) → 같은 인스턴스의 __study 호출이다. Calc.plus는 내 코드에서 self.add로, 강사님은 Calc.add로 정적 메서드를 호출한다. 두 표현은 이 예제의 같은 함수를 부른다. Person4 생성 때 Person4.count 증가 → classmethod 호출 때 cls로 클래스 전달 → count 읽기의 흐름이다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 내 원본이 인스턴스별 지점·공통 브랜드·세 가지 호출 방식을 실제로 비교한다. **교정:** static 메모리 영역에 있어 빠르다는 설명은 이 코드의 확인 결과가 아니다. 클래스 속성은 클래스에 둔 값이라는 관계로 읽는다. **공통 한계:** Person3 pay는 잔액·음수 금액 검사가 없는 단순 실습이다. 이를 완성 결제 모델이라고 소개하지 않는다. **개선:** 상태를 다루는 메서드가 허용할 입력과 변경 규칙을 명확히 할 수 있다.

개선안은 D 드라이브 원본을 수정한 결과가 아니다. 실제 오류·수업용 단순화·목적에 따른 선택을 구별한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



핵심 결과는 같아 반복 인용하지 않는다. plus의 self.add와 Calc.add는 현재 Calc만 쓰는 상황에서 같은 덧셈이다. 상속이 들어왔을 때까지 언제나 완전히 같은 설계라고 확대하지 않는다. 강사님과 내 __money에 대입한 큰 숫자가 달라도 실제 내부 pay 결과는 7000·4000이다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 원본 순간 | 실제 내부 값·상태 |
| --- | --- |
| Person3(10000) | 내부 __money 10000 |
| pay(3000) | 내부 7000, __study 실행 |
| 밖에서 a.__money 대입 | 별도 속성 추가 |
| 다시 pay(3000) | 내부 4000 |
| Person4 세 개 | count 3 |
| Account 생성만 | 내부 잔액 0, 조회 출력 없음 |

Count는 현재 실습에서 생성 호출 수를 세는 값이지 지금 살아 있는 객체 수가 아니다. 객체가 더 이상 사용되지 않는 경우까지 count를 자동 감소시키는 코드는 없다. 클래스 메서드가 모든 객체의 속성을 자동 순회하는 것도 아니다.

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| Counter를 하나 더 생성 | count 4 | 초기화의 증가 |
| 밖의 __money 대입 제거 | pay 결과 동일 | 별도 이름을 건드린 것 |
| 정적 add에 self 인자를 그냥 추가 | 기존 호출과 개수 불일치 | 자동 인수가 없는 방식 |
| brand만 변경 | 공통 클래스 값 읽기에 반영 | 인스턴스 지점과 별개 |

비공개 이름이 안 보이면 철자와 클래스 내부 이름 변경을 구별한다. 메서드 인수 오류는 데코레이터와 첫 인수 규칙을 본다. count가 기대와 다르면 실제로 인스턴스를 몇 번 만들었는지 확인한다. 정의만 한 setter를 실행한 것으로 가정하지 않는다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 이름 변경의 세부 접근·상속과 메서드 탐색·property·직접 만드는 데코레이터·수명 기반 객체 카운터는 추가 학습이다. 기본은 실제 공통 값과 호출 인수를 구별하는 것이다.

TIP은 기본 문제의 필수 조건이 아니다. 배운 문법을 확인한 📚 출처와 선택 확장을 구별한다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. 밖의 __money 대입 뒤 다음 잔액은?
2. 정적 메서드에 self가 자동 들어오는가?
3. classmethod의 cls는 무엇인가?
4. count 3은 살아 있는 객체가 반드시 3개라는 뜻인가?

<details>
<summary>풀이 — 먼저 자신의 답을 적은 뒤 펼치기</summary>

현재 원본은 4000이다. 정적 메서드는 해당 자동 인수를 받지 않는다. cls는 호출에 연결된 클래스다. 원본 count는 생성 때만 증가하여 현재 생존 수를 보장하지 않는다.

</details>

| 구분 | 확인 |
| --- | --- |
| 데이터 | 클래스인가 인스턴스인가? |
| 이름 | 내부 이름과 밖의 대입 |
| 호출 | self·cls·자동 인수 없음 |
| 실행 | 정의만 했나 실제 불렀나? |

[장별 연습문제](실습/연습문제/12-02_Python_클래스속성과_메서드_연습문제.md) · 다음은 [클래스 과제 비교](12-03_Python_클래스_과제비교.md)다.

<!-- 이전 명시 앵커 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
