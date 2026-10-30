# 11-02. 함수 인자 전달 — 풀어서 보내기와 모아서 받기

[Python 목차](README.md) · [읽기 안내](00-00_Python_V3_동작_백과_읽기법.md)

같은 * 기호도 정의할 때와 호출할 때 역할이 반대다. 코드를 쓰는 위치부터 구분하고 실제 값이 어느 매개변수에 들어가는지 표로 맞춰 보자.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

위치·키워드·기본값을 구분한다. 호출의 *·** 풀기와 정의의 *args·**kwargs 모으기를 설명하고, 딕셔너리의 키 전달과 이름에 맞춘 값 전달을 비교한다.

실제 원본·새 예제·개선안·선택 학습을 구분하고 입력·실행 순서·반환값·출력을 연결한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

매개변수는 def에서 받을 이름이고 인자는 호출에서 넣는 값이다. 위치 인자는 순서로, 키워드 인자는 이름으로 연결한다. minus(y=5,x=2)는 함수의 x에 2·y에 5를 넣으므로 계산은 2-5다.

| 위치 | 표현 | 역할 |
| --- | --- | --- |
| 호출 | function(*values) | 항목을 여러 위치 인자로 풀기 |
| 정의 | def function(*values) | 남는 위치 인자를 튜플로 모으기 |
| 호출 | function(**mapping) | 키 이름에 맞춰 키워드 인자로 풀기 |
| 정의 | def function(**mapping) | 키워드 인자를 딕셔너리로 모으기 |

딕셔너리에 *를 하나 쓰면 키들이 나온다. **를 쓰면 키를 매개변수 이름으로 하여 값을 전달한다. info(age,name)에 name·age 순서의 딕셔너리를 *로 넣으면 문자열 키 name이 age 매개변수에 들어갈 수 있다. 실행된다고 의도한 인자 연결인 것은 아니다.

기본값은 해당 인자를 생략했을 때 사용한다. 기본값이 있다고 실제 전달 값의 종류를 자동 검사하는 것은 아니다. 원본의 info3(1,2)는 이름 자리에 숫자를 넣어도 함수에 별도 검사가 없어 그대로 출력한다.

> 📚 **출처 · 본문 설명 확인:** [Python 기본값·키워드·인자 목록 풀기](https://docs.python.org/ko/3/tutorial/controlflow.html#more-on-defining-functions). 실제 배운 문법의 의미를 확인한 근거다. 예제·표·풀이 자체는 수업 자료를 바탕으로 새로 구성했다. 외부 문장을 직접 인용하지 않았다. 이번 문법 확인 기간: 2026-10-28~29.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 코드.** [실행 파일](실습/책형_복습/11-02_Python_함수_인자전달.py)을 제공한다. Python이 설치된 환경에서 새 .py 파일로 저장해 실행한다. 터미널은 그 파일이 있는 폴더에서 열고 `python 파일이름.py`를 실행한다. VS Code의 Python 실행 기능을 사용해도 된다. 결과는 터미널에 표시된다.



```python
def minus(x, y):
    return x - y
def show_numbers(*values):
    print(values, type(values))
def info(age, name):
    print(age, name)
def show_keywords(**values):
    for key, value in values.items():
        print(key, value)
def greet(name, address='비공개'):
    print(name, address)
print(minus(5, 2))
print(minus(y=5, x=2))
numbers = [1, 2, 3]
show_numbers(*numbers)
show_numbers()
profile = {'name': '민지', 'age': 20}
info(*profile)
info(**profile)
show_keywords(**profile)
greet('민지')
greet('민지', '서울')
```

numbers를 풀어 호출한 뒤 show_numbers가 다시 튜플로 모은다. 인자가 없으면 빈 튜플이다. info(*profile)은 키 이름 두 개를 위치 순서로 넣어 name age를 출력한다. info(**profile)은 실제 나이 20·이름 민지를 이름에 맞춰 넣는다. greet의 주소는 생략할 때만 비공개다. 모든 함수 정의와 호출을 한 파일에 보여 주어 외부 정의를 추측할 필요가 없다.

**예상 출력 또는 관찰:**

```text
3
-3
(1, 2, 3) <class 'tuple'>
() <class 'tuple'>
name age
20 민지
name 민지
age 20
민지 비공개
민지 서울
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본 발췌다. 주석의 잘못된 설명도 원문을 보존하고 풀이에서 교정한다. 필요한 선언·호출·다른 파일의 정의는 다음 절까지 연결해 읽는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/11_fn.py` 50–76행

```python
def print_numbers(a, b, c) :
    print(a)
    print(b)
    print(c)
print_numbers(10, 20, 30)

a = [1,2,3]
print(a)
print(*a) # 1, 2, 3 이 들어간 것과 같음
# print_numbers(a) # TypeError: print_numbers() missing 2 required positional arguments: 'b' and 'c'
print_numbers(*a)

# 전달인자에 *를 붙일 경우 'tuple'로 반환해 줌, '가변인수'라고 부름
def print_numbers2(*a) :
    print(type(a), a)
    for b in a :
        print(b)

print_numbers2(1)
print_numbers2(1,2,3,4)

# def print_numbers3(*a, c) : # 어디까지가 c인지 분간이 어렵기 때문에, *은 뒤에
def print_numbers3(c, *a) :
    print(c)
    for b in a :
        print(b)
print_numbers3(1,2,3,4)
```

**발췌 바로 풀이:** `print_numbers(a,b,c)`는 세 값을 요구한다. `print_numbers(*[1,2,3])`의 `*`는 **리스트의 세 값을 각각 인자로 풀어** 넣는다. 반대로 `def print_numbers2(*a)`의 `*a`는 전달된 여러 위치 인자를 **튜플로 모은다**. 내 주석의 “전달인자에 `*`를 붙이면 튜플로 반환”은 정의할 때와 호출할 때의 역할을 섞어 쓴 것이다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/11_fn.py` 78–105행

```python
def minus(x, y) :
    print(x - y)

minus(5,2)
minus(y=5,x=2) # keyword를 지정하면 순서에 상관없이 넣을 수 있음

x = {
    'name' : '정근욱',
    'age' : 30
}

def info(age, name) :
    print(age,name)

# info(x) # 전달인자가 1개이기 때문에 불가
info(*x) # 딕셔너리의 경우 list와 tuple처럼 * 한개를 쓰면 key값만 나옴 (.keys()와 같다)
info(**x) # key=value 형태로 출력 됨

def info2(**a) :
    for k, v in a.items() :
        print(k,v)

info2(**x)

def info3(name, age, addr='비공개') : # 함수에 기본값을 지정할 수 있음
    print(name, age, addr)
info3(1,2,3)
info3(1,2) # 기본값을 지정해두었을 때 전달인자를 안 줘도 오류 없이 기본값 출력
```

**발췌 바로 풀이:** `minus(y=5, x=2)`는 이름을 붙여 보내므로 선언 순서와 관계없이 `2-5=-3`을 출력한다. 딕셔너리 `x`를 `info(*x)`로 넣으면 **키 이름 두 개**가 위치 인자로 전달되어 `age='name'`, `name='age'`처럼 들어간다. `info(**x)`는 키를 **매개변수 이름**에 맞춰 전달해 실제 나이와 이름을 넣는다. `def info2(**a)`는 이렇게 전달된 여러 키워드 인자를 딕셔너리로 모은다.

내 print_numbers는 a·b·c 세 인자가 필요하다. 리스트 하나를 그대로 넣은 주석 호출은 인자가 한 개라 나머지 둘이 없다. *a로 풀면 세 항목이 각각 들어간다. 내 주석의 튜플로 반환한다는 말은 함수 정의에서 모으는 것과 호출에서 푸는 것을 섞었다. info2의 **a는 키워드 인자를 딕셔너리로 받으며, 그 안 items 반복은 실제 키·값을 출력한다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

호출 값 준비 → * 또는 **로 전달 형태 결정 → 매개변수 이름과 연결 → 함수 본문 → 반환 또는 출력 순서다. 기본값은 연결할 인자를 받지 않은 자리에 사용한다. 원본의 print_numbers3(c,*a)는 첫 위치를 c에, 나머지를 튜플 a에 받는다. 주석의 def print_numbers3(*a,c)도 문법상 가능하지만 c를 키워드로 전달해야 하는 다른 규칙이다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 내 코드가 리스트·딕셔너리 풀기와 기본값을 실제 출력으로 나누었다. **교정:** *은 항상 뒤에만 놓아야 한다는 문법 금지로 외우지 않는다. 원본의 쉬운 위치 인자 예제와 키워드 전용 규칙은 별개다. **개선:** 호출에 무엇이 들어가는지 적어 잘못된 키 문자열 전달을 찾는다. 인자 수 오류를 피하려고 불필요하게 모든 함수를 가변 인자로 바꾸지 않는다.

개선안은 D 드라이브 원본을 수정한 결과가 아니다. 실제 오류·수업용 단순화·목적에 따른 선택을 구별한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



양쪽 전달 원리는 같고 이름·나이 값만 다르므로 중복 인용하지 않는다. 강사님은 빈 print_numbers2()도 호출하고 내 원본은 해당 호출이 없다. 새 예제의 빈 호출을 내 원본 결과로 섞지 않는다. info2는 강사님만 1을 반환하지만 두 호출 모두 반환값을 저장하지 않는다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 호출 | 연결 | 결과 |
| --- | --- | --- |
| minus(5,2) | x=5,y=2 | 3 |
| minus(y=5,x=2) | x=2,y=5 | -3 |
| info(*profile) | age='name',name='age' | 키 문자열 출력 |
| info(**profile) | age=20,name='민지' | 값 출력 |

풀어 보낼 항목 수와 이름이 함수 정의에 맞아야 한다. 같은 매개변수에 위치·키워드로 중복 값을 주거나 없는 키워드를 주면 TypeError가 날 수 있다. 기본값은 정의에 정한 규칙이지 누락된 필수 인자 전체를 채우는 기능이 아니다.

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| info의 **를 *로 | 키 문자열이 위치로 들어감 | 전달 규칙 변경 |
| profile 키 age를 years로 | 예상 못한 키워드 오류 | 매개변수 이름 불일치 |
| greet 주소를 명시 | 기본값 대신 전달값 | 생략하지 않은 인자 |
| show_numbers에 리스트를 풀지 않고 전달 | 튜플 안에 리스트 한 개 | 위치 인자 수 차이 |

인자가 부족하면 목록 하나와 여러 값 전달을 구분한다. 출력이 키 이름이면 *와 **를 본다. 기본값이 적용 안 되면 이미 그 자리에 값을 전달했는지 확인한다. 오류 메시지의 매개변수 이름과 실제 def를 나란히 본다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 위치 전용·키워드 전용 인자의 상세 API 설계와 가변 기본값 함정은 추가 학습이다. 본문은 실제 호출한 위치·키워드·풀기·모으기를 먼저 익힌다.

TIP은 기본 문제의 필수 조건이 아니다. 배운 문법을 확인한 📚 출처와 선택 확장을 구별한다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. 정의의 *와 호출의 * 역할은?
2. dict에 *를 쓰면 값이 나오는가?
3. minus(y=5,x=2)는?
4. 기본값은 언제 쓰는가?

<details>
<summary>풀이 — 먼저 자신의 답을 적은 뒤 펼치기</summary>

정의는 모으고 호출은 푼다. 딕셔너리의 *는 키를 전달한다. -3이다. 해당 인자를 생략했을 때 기본값을 사용한다.

</details>

| 구분 | 확인 |
| --- | --- |
| 위치 | 순서로 연결 |
| 키워드 | 이름으로 연결 |
| 별표 | 정의·호출 위치 구분 |
| 기본값 | 생략한 자리 |

[장별 연습문제](실습/연습문제/11-02_Python_함수_인자전달_연습문제.md) · 다음은 [lambda·변수 범위](11-03_Python_lambda와_변수범위.md)다.

<!-- 이전 명시 앵커 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
