# 12-02. 클래스의 상태와 메서드 — 인스턴스·공통 값·호출 인수 — 연습문제

[본문](../../12-02_Python_클래스속성과_메서드.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원래 수업 퀴즈·당시 내 풀이와 구별한다. 실행 전 예상 → 이유 설명 → 한 가지 수정 순서로 풀어 본다.

## 목표와 실행 조건

이중 밑줄 속성의 이름 변경과 별도 속성 대입을 구별한다. 클래스 속성·인스턴스 속성, 인스턴스·정적·클래스 메서드를 비교하고 생성 횟수와 실제 메서드 호출 유무를 추적한다.

[전체 Python 파일](../책형_복습/12-02_Python_클래스속성과_메서드.py)을 새 파일로 실행한다. 입력·준비 파일·import 조건은 [본문 3절](../../12-02_Python_클래스속성과_메서드.md#example)을 먼저 확인한다. 의도적으로 예외를 관찰하는 예제는 오류 종류와 그 전에 나온 출력도 답에 적는다.

## 문제 1. 결과와 실행 순서 예상



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

<details>
<summary>힌트와 풀이</summary>

입력·현재 값·실행 순서·반환값·출력 위치를 따로 표시한다.

```text
7000
4000
천안 아산 연습 빵집
3
3
```

밖에서 wallet.__money에 큰 수를 대입해도 pay가 다루는 내부 값은 7000에서 4000으로 감소한다. Shop의 지점명은 두 인스턴스에 따로 있고 brand는 클래스에서 읽는다. Calc.add는 인스턴스를 만들지 않고 호출한다. Counter는 세 번 초기화하여 클래스 count가 3이다. 원본은 남은 돈과 count를 메서드 안에서 출력하지만 새 예제는 값을 반환하여 바깥 print에서 관찰하도록 구별했다.

</details>

## 문제 2. 이유를 자신의 말로 설명

1. 밖의 __money 대입 뒤 다음 잔액은?
2. 정적 메서드에 self가 자동 들어오는가?
3. classmethod의 cls는 무엇인가?
4. count 3은 살아 있는 객체가 반드시 3개라는 뜻인가?

<details>
<summary>풀이</summary>

현재 원본은 4000이다. 정적 메서드는 해당 자동 인수를 받지 않는다. cls는 호출에 연결된 클래스다. 원본 count는 생성 때만 증가하여 현재 생존 수를 보장하지 않는다.

| 원본 순간 | 실제 내부 값·상태 |
| --- | --- |
| Person3(10000) | 내부 __money 10000 |
| pay(3000) | 내부 7000, __study 실행 |
| 밖에서 a.__money 대입 | 별도 속성 추가 |
| 다시 pay(3000) | 내부 4000 |
| Person4 세 개 | count 3 |
| Account 생성만 | 내부 잔액 0, 조회 출력 없음 |

Count는 현재 실습에서 생성 호출 수를 세는 값이지 지금 살아 있는 객체 수가 아니다. 객체가 더 이상 사용되지 않는 경우까지 count를 자동 감소시키는 코드는 없다. 클래스 메서드가 모든 객체의 속성을 자동 순회하는 것도 아니다.

</details>

## 문제 3. 한 가지만 바꾸기

본문의 다음 실험에서 한 행만 골라 결과를 먼저 예상한다. 실행 후 원래 예제로 돌아가 다음 변경을 확인한다.

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| Counter를 하나 더 생성 | count 4 | 초기화의 증가 |
| 밖의 __money 대입 제거 | pay 결과 동일 | 별도 이름을 건드린 것 |
| 정적 add에 self 인자를 그냥 추가 | 기존 호출과 개수 불일치 | 자동 인수가 없는 방식 |
| brand만 변경 | 공통 클래스 값 읽기에 반영 | 인스턴스 지점과 별개 |

<details>
<summary>막힐 때 확인할 것</summary>

비공개 이름이 안 보이면 철자와 클래스 내부 이름 변경을 구별한다. 메서드 인수 오류는 데코레이터와 첫 인수 규칙을 본다. count가 기대와 다르면 실제로 인스턴스를 몇 번 만들었는지 확인한다. 정의만 한 setter를 실행한 것으로 가정하지 않는다.

</details>

## 채점과 복습

값만 맞혔는지보다 어떤 입력·분기·호출로 그 결과가 나왔는지 설명한다. 예외·주석·의도한 동작을 혼동하지 않는다. 모르면 연결된 본문의 개념·작은 예제·내 원본 풀이로 돌아간다. TIP의 선택 학습은 필수 정답이 아니다.
