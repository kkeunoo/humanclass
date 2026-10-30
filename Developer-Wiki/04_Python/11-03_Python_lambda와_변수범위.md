# 11-03. lambda와 이름의 범위 — 함수 값·정렬 기준·안팎 변수 읽기

[Python 목차](README.md) · [읽기 안내](00-00_Python_V3_동작_백과_읽기법.md)

짧은 함수를 한 줄로 표현해도 함수라는 성질은 그대로다. 어디에 함수를 전달하고 어떤 값을 반환하는지 먼저 읽고, 함수 안팎의 같은 이름이 어느 값인지 별도로 추적한다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

def·lambda·map의 결과와 정렬 key 함수를 연결한다. 지역 대입·전역 읽기·global·nonlocal을 실제 범위에서 설명하고 정의만 한 함수와 호출한 함수를 구분한다.

실제 원본·새 예제·개선안·선택 학습을 구분하고 입력·실행 순서·반환값·출력을 연결한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

lambda는 표현식의 결과를 반환하는 짧은 함수를 만든다. lambda x:x+10은 x를 받아 10을 더한다. 함수 객체를 만들거나 변수에 저장한 것만으로 본문을 호출한 것은 아니다. map에 넘길 때도 ten2라는 함수 값과 ten2(5)라는 호출 결과를 구별한다.

| 사용 | 함수가 받을 것 | 함수가 돌려줄 것 |
| --- | --- | --- |
| map(int,목록) | 각 항목 | 변환한 정수 |
| map(lambda x:x+10,목록) | 각 숫자 | 10을 더한 값 |
| sort(key=lambda person:person['age']) | 각 사람 객체 | 정렬에 쓸 나이 |

정렬 key 함수는 사람을 직접 출력하는 함수가 아니다. 비교에 사용할 값을 반환한다. 나이를 출력만 하고 None을 돌려주는 함수를 같은 역할로 넘기지 않는다. map 결과는 원본처럼 list로 만들어 관찰한다.

함수 안에서 x=20이라고 대입하면 보통 그 함수의 지역 이름이다. 바깥 x=10과 별도로 존재할 수 있다. global x는 모듈 범위의 x를 사용하도록 하고, nonlocal은 둘러싼 함수 범위의 기존 이름을 가리킨다. 바로 바깥 한 단계에 무조건 같은 값이 있다는 뜻이 아니다. 중첩 구조에서 이름별로 가장 가까운 해당 함수 범위를 찾아야 한다.

> 📚 **출처 · 본문 설명 확인:** [Python lambda](https://docs.python.org/ko/3/tutorial/controlflow.html#lambda-expressions), [클래스 문서의 범위·이름 공간](https://docs.python.org/ko/3/tutorial/classes.html#python-scopes-and-namespaces). 실제 배운 문법의 의미를 확인한 근거다. 예제·표·풀이 자체는 수업 자료를 바탕으로 새로 구성했다. 외부 문장을 직접 인용하지 않았다. 이번 문법 확인 기간: 2026-10-28~29.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 코드.** [실행 파일](실습/책형_복습/11-03_Python_lambda와_변수범위.py)을 제공한다. Python이 설치된 환경에서 새 .py 파일로 저장해 실행한다. 터미널은 그 파일이 있는 폴더에서 열고 `python 파일이름.py`를 실행한다. VS Code의 Python 실행 기능을 사용해도 된다. 결과는 터미널에 표시된다.



```python
def double(number):
    return number * 2
double_short = lambda number: number * 2
print(double(3), double_short(3))
print(list(map(lambda number: number + 10, [1, 2])))
people = [{'age': 25}, {'age': 23}, {'age': 30}]
people.sort(key=lambda person: person['age'])
print([person['age'] for person in people])
x = 10
def local_example():
    x = 20
    print('지역', x)
local_example()
print('밖', x)
def change_global():
    global x
    x = 20
change_global()
print('변경 뒤', x)
def outer():
    x = 10
    y = 20
    def middle():
        x = 30
        def inner():
            nonlocal x, y
            print('가까운 x', x)
            print('찾은 y', y)
        inner()
    middle()
outer()
```

double과 double_short는 같은 입력에서 6을 반환한다. sort는 나이를 key로 받아 people의 순서를 바꾼다. local_example의 x는 함수 안 값이라 호출 뒤 바깥 x는 10이다. change_global은 모듈 x를 20으로 바꾼다. 중첩 inner의 x는 middle의 30, y는 middle에 없어 outer의 20을 찾는다. 새 예제에서 nonlocal 이름은 읽기만 하며 별도 숨겨진 저장소나 클래스는 없다.

**예상 출력 또는 관찰:**

```text
6 6
[11, 12]
[23, 25, 30]
지역 20
밖 10
변경 뒤 20
가까운 x 30
찾은 y 20
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본 발췌다. 주석의 잘못된 설명도 원문을 보존하고 풀이에서 교정한다. 필요한 선언·호출·다른 파일의 정의는 다음 절까지 연결해 읽는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/11_fn.py` 140–165행

```python
def ten(x) :
    return x + 10
print( ten(5) )

ten2 = lambda x: x + 10 # 람다표현식으로 사용할 수 있음
print( ten2(5) )
print( (lambda x: x + 10)(5) )

a = ['1','2']
b = [int(a[0]), int(a[1])]
c = list(map(int, a))
print(a, b, c)

d = list(map(ten2,c)) # 아래와 같이 lambda식을 바로 넣을 수 있음
print(d)

e = list(map(lambda x: x + 10,c)) 
print(e)


sqr = lambda x: x ** 2
print(sqr(3))

sum = lambda x, y: x + y
print(sum(3,5))

```

**발췌 바로 풀이:** `lambda x: x+10`은 값을 하나 받아 10을 더해 **돌려주는 짧은 함수**다. `map(int, ['1','2'])`은 각 문자열에 `int`를 적용하고, 원본은 `list(...)`로 결과를 확인한다. `map(ten2, c)`는 각 숫자에 10을 더한다. 강사님은 `square`, `sum` 함수를 `lambda` 버전과 비교하고, 나는 `sqr`, `sum`을 `lambda`로 직접 작성했다. 여기서 `sum`이라는 이름은 Python의 기본 제공 `sum`도 가리킬 수 있어, 학습 예시에서는 **이름이 겹친다**는 점을 알아 두면 좋다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/11_fn.py` 166–195행

```python
info = [{
        'name' : '이름1',
        'age' : 25
    }, {
        'name' : '이름2',
        'age' : 23
    }, {
        'name' : '이름3',
        'age' : 30
    }]
#함수로 나이만 출력

# print(*info[0].values())

def age(info) :
    for i in info :
        print(*i.values())

age(info)

def print_age(info) :
    for p in info :
        print(p['age'])
print_age(info)

print_age2 = lambda info : [p['age'] for p in info]
print(print_age2(info))

info.sort(key = lambda x : x['age'])
print(info)
```

**발췌 바로 풀이:** `print_age(info)`는 각 딕셔너리의 `'age'` 값을 출력한다. `print_age2 = lambda info: [p['age'] for p in info]`는 나이 목록을 **반환**하므로, 두 코드 모두 `print(print_age2(info))`처럼 결과를 출력한다. 강사님은 `info.sort(key=age)`와 `key=lambda ...`를 둘 다 실행하고, 나는 `lambda` 버전만 실행한다. 둘 다 `'age'` 값으로 오름차순 정렬하므로 결과는 23, 25, 30세 순서다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/11_fn.py` 197–255행

```python
x = 10
def foo() :
    x = 20
    print('foo 안에서 x:', x) # 안에 선언 된 지역변수가 있으면, 해당 값을 가져옴
foo()
print('foo 밖에서 x:', x) # 전역변수를 가져오기 때문에, 10이 됨

def foo2() :
    print('foo 안에서 선언없음 x:', x) # 안에 선언 된 지역변수가 없으면, 전역변수 값을 가져옴
foo2()

def foo3() :
    global x # global로 전역변수 값을 바꿀 수 있음
    x = 20
foo3()
print('foo3 이후의 x:', x)

# 함수 안에서 변수 우선 순위
'''
    1. 먼저 지역 변수 찾기
    2. 없으면 전역 변수 찾기
    3. 없으면 에러(not defined)
'''

x = 10
def test(z) :
    return z + 2
x = test(x)

def test2() :
    global x
    x = x+2

x = 10
y = 20
def test3() :
    global x, y # global 함수에 2개도 지정할 수 있음
    x = 11 
    y = 12
test3()
print(x, y)

# nonlocal로 윗 부모에게 찾아갈 수 있음
def A():
    x = 10
    y = 20

    def B():
        x = 30

        def C():
            nonlocal x, y
            print(x)
            print(y)
        C()

    B()

A()
```

**발췌 바로 풀이:** 처음 `x=10`일 때 `foo()` 안의 `x=20`은 **별도의 지역 변수**라서 함수 밖 `x`는 여전히 10이다. `foo2()`는 함수 안에 `x`를 새로 지정하지 않아 밖의 값을 읽는다. `foo3()`는 `global x`를 써서 밖의 `x`를 20으로 바꾼다.

내 ten·ten2·직접 lambda 호출은 모두 5에 10을 더해 15다. print_age는 각 나이를 출력하고 print_age2는 나이 리스트를 반환하므로 출력하려면 바깥 print가 필요하다. 내 age 함수는 values 전체를 풀어 이름과 나이도 출력하므로 이름이 age라고 나이만 출력하는 것은 아니다. 뒤 test3은 내 코드에서 실제 호출하지만 강사님은 정의만 한다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

lambda 정의 → 함수 값을 map 또는 sort의 key에 전달 → 각 항목이 매개변수로 들어감 → 표현식 반환 → 새 결과 목록 또는 정렬에 사용 순서다. A가 B를 정의하고 호출하며 B가 C를 정의하고 호출한다. 따라서 C가 읽는 둘러싼 범위를 원본의 중첩 모양대로 따라갈 수 있다. 함수 이름이 대문자 A라고 자동 클래스가 되는 것은 아니다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 내 코드는 일반 함수와 lambda 결과, 지역·전역 이름을 직접 비교했다. **교정:** print_age2는 출력 함수가 아니라 목록 반환 함수다. nonlocal을 바로 부모만 보는 규칙으로 축소하지 않는다. **이름 개선:** 내 sum=lambda는 내장 sum을 가리던 이름을 덮으므로 add처럼 목적을 구별하면 혼동이 줄어든다. **선택:** 한 줄로 줄여 더 어려워지면 def로 쓰는 편이 낫다.

개선안은 D 드라이브 원본을 수정한 결과가 아니다. 실제 오류·수업용 단순화·목적에 따른 선택을 구별한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



양쪽 주요 정렬 결과는 나이 23·25·30 순서로 같다. 강사님은 일반 key 함수와 lambda를 모두 정렬에 사용하고 내 코드는 lambda를 사용한다. test3의 호출 유무는 실제 전역 값 변경 차이이므로 구분한다. 정의만 한 함수를 실행한 결과에 섞지 않는다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 읽는 위치 | x를 찾은 범위 | 값 |
| --- | --- | --- |
| local_example 본문 | 자기 지역 | 20 |
| 그 호출 뒤 모듈 | 모듈 | 10 |
| global 변경 뒤 모듈 | 모듈 | 20 |
| inner의 nonlocal x | middle | 30 |
| inner의 nonlocal y | outer | 20 |

원본의 지역→전역→오류 메모는 모든 이름 검색 단계의 완전한 목록이 아니다. 둘러싼 함수 범위와 Python 내장 이름도 있어 print를 별도 정의하지 않아도 사용할 수 있다. 이 장은 실제 중첩 함수의 이름마다 어디를 읽는지 먼저 확인한다.

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| local_example 안 x만 40으로 | 안 40·밖 10 | 지역 이름 분리 |
| middle의 x 제거 | inner가 outer의 x=10을 찾음 | 가까운 기존 함수 범위 |
| key의 age를 다른 키로 | 해당 키가 없으면 오류 | 정렬 기준 조회 |
| 함수 호출만 제거 | 그 본문 출력 없음 | 정의와 실행 차이 |

바깥 값이 안 바뀌면 함수 안의 새 지역 대입인지 본다. nonlocal 오류는 둘러싼 함수에 그 이름이 실제 있는지 확인한다. map에 숫자를 넘겼다면 함수 값과 호출 결과를 구분한다. 정렬 함수는 출력만 하는지 값을 반환하는지 본다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 클로저의 고급 활용·상태 캡슐화·복잡한 중첩 이름 충돌·함수형 설계는 추가 학습이다. 기본은 실제 map·key·global·nonlocal 예제를 설명하는 수준이다.

TIP은 기본 문제의 필수 조건이 아니다. 배운 문법을 확인한 📚 출처와 선택 확장을 구별한다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. lambda를 변수에 넣으면 바로 실행되는가?
2. sort의 key 함수는 무엇을 반환해야 하는가?
3. 지역 x를 바꾸면 모듈 x도 항상 바뀌는가?
4. inner의 y는 왜 outer에서 읽는가?

<details>
<summary>풀이 — 먼저 자신의 답을 적은 뒤 펼치기</summary>

호출 전에는 실행하지 않는다. 각 항목의 정렬 기준 값을 반환한다. 지역 대입은 별도다. middle에 y가 없어 둘러싼 outer의 기존 이름을 찾기 때문이다.

</details>

| 구분 | 확인 |
| --- | --- |
| 함수 | 값 전달과 호출 |
| map | 항목별 변환 결과 |
| key | 정렬 기준 반환 |
| 범위 | 이름마다 정의·대입 위치 |

[장별 연습문제](실습/연습문제/11-03_Python_lambda와_변수범위_연습문제.md) · 다음은 [클래스·인스턴스](12-01_Python_클래스와_인스턴스.md)다.

<!-- 이전 명시 앵커 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
