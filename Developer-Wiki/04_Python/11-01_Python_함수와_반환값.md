# 11-01. 함수와 반환값 — 화면에 보인 값과 돌려받은 값 나누기

[Python 목차](README.md) · [읽기 안내](00-00_Python_V3_동작_백과_읽기법.md)

함수는 이름 붙인 작업을 호출할 때 실행하는 단위다. 화면에 숫자가 보였다는 사실만으로 그 숫자를 다음 계산에서 사용할 수 있는 것은 아니다. 출력·반환·객체 변경을 따로 확인한다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

def와 호출, 인자·매개변수·return을 연결한다. None·여러 값의 튜플 반환·함수 참조·중첩 호출·가변 리스트 변경과 반환의 차이를 설명한다.

실제 원본·새 예제·개선안·선택 학습을 구분하고 입력·실행 순서·반환값·출력을 연결한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

def가 실행되면 함수가 정의되어 이름으로 호출할 수 있다. 본문은 호출할 때 실행한다. 호출의 괄호 안 값은 인자이고 함수 정의의 받는 이름은 매개변수다. return은 호출한 자리로 값을 돌려주면서 현재 함수를 끝낸다.

| 함수의 작업 | 화면 | 호출 결과 | 원래 리스트 |
| --- | --- | --- | --- |
| print(a+b)만 | 합이 보임 | None | 관련 없음 |
| return a+b | 별도 print 없으면 안 보임 | 합 | 관련 없음 |
| items.append(값) | 출력 없으면 안 보임 | 별도 return 없으면 None | 내용 변경 |

값 없는 return이나 끝까지 진행한 함수의 결과는 None이다. None은 오류 메시지나 문자열 'None'이 아니라 돌려줄 값이 없음을 나타내는 값이다. 화면 출력은 사람이 보는 통로이고 반환값은 코드가 재사용하는 통로다.

return x,y는 두 값을 튜플로 묶어 반환한다. result로 받으면 튜플 하나이며 left,right로 나누어 받으면 각 값을 얻는다. 함수 안 지역 변수 이름과 바깥에서 반환값을 받는 이름이 같아도 그 지역 변수를 직접 꺼내는 것은 아니다.

> 📚 **출처 · 본문 설명 확인:** [Python 함수 정의·반환](https://docs.python.org/ko/3/tutorial/controlflow.html#defining-functions), [return 문](https://docs.python.org/ko/3/reference/simple_stmts.html#the-return-statement). 실제 배운 문법의 의미를 확인한 근거다. 예제·표·풀이 자체는 수업 자료를 바탕으로 새로 구성했다. 외부 문장을 직접 인용하지 않았다. 이번 문법 확인 기간: 2026-10-28~29.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 코드.** [실행 파일](실습/책형_복습/11-01_Python_함수와_반환값.py)을 제공한다. Python이 설치된 환경에서 새 .py 파일로 저장해 실행한다. 터미널은 그 파일이 있는 폴더에서 열고 `python 파일이름.py`를 실행한다. VS Code의 Python 실행 기능을 사용해도 된다. 결과는 터미널에 표시된다.



```python
def show_sum(a, b):
    "두 값의 합을 화면에 출력한다."
    print(a + b)
def return_sum(a, b):
    return a + b
def add_sub(a, b):
    return a + b, a - b
def append_four(items):
    items.append(4)
def times_ten(value):
    return value * 10
shown = show_sum(2, 3)
returned = return_sum(2, 3)
print('출력 함수 결과', shown)
print('반환 함수 결과', returned, returned * 2)
pair = add_sub(1, 2)
left, right = pair
print(pair, left, right)
numbers = [1, 2, 3]
changed = append_four(numbers)
print(numbers, changed)
print(times_ten(return_sum(2, 3)))
function_value = return_sum
print(function_value(4, 5))
print(show_sum.__doc__)
```

show_sum이 5를 출력한 뒤 shown은 None이다. return_sum의 5는 returned에 담겨 곱셈에 쓸 수 있다. append_four는 None을 돌려주지만 같은 리스트에 붙인 4는 남는다. 중첩 호출은 안쪽 합 5를 먼저 받아 times_ten에 넣어 50을 만든다. return_sum은 괄호 없이 function_value에 전달하고 그 이름으로 나중 호출한다. 함수 첫 문자열은 docstring이며 # 주석이 아니다.

**예상 출력 또는 관찰:**

```text
5
출력 함수 결과 None
반환 함수 결과 5 10
(3, -1) 3 -1
[1, 2, 3, 4] None
50
9
두 값의 합을 화면에 출력한다.
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본 발췌다. 주석의 잘못된 설명도 원문을 보존하고 풀이에서 교정한다. 필요한 선언·호출·다른 파일의 정의는 다음 절까지 연결해 읽는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/11_fn.py` 1–25행

```python
# NameError: name 'hello' is not defined. Did you mean: 'help'?
# 선언되기 전에 함수를 먼저 실행하면 Name 에러 발생 (인터프리터로 위부터 한 줄씩 진행되기 때문에)
# hello() 

def hello() :
    print('hello world')

hello()

def add(a, b) :
    "a + b를 출력함"
    print( a + b )
    "a + b를 출력함2"

add(1,2)
print(add.__doc__) # doc는 document의 함수 첫 줄 string을 출력할 수 있음

def add2(a, b) :
    return a + b

c = add2(1, 2)
print(c)

def 아낌없이주는함수() :
    return 100
```

**발췌 바로 풀이:** `hello()`는 `def hello()`가 실행되어 이름이 만들어진 **뒤에** 호출한다. 내 파일 첫머리의 `# hello()`는 호출 전이었다면 이름 오류가 날 수 있음을 남긴 **주석**이다. `add`는 합을 `print`하지만 반환문이 없어 호출 결과는 `None`이다. `add2`는 합을 `return`하므로 호출한 자리에서 값 `3`을 받을 수 있다. 함수 첫 부분의 문자열은 `add.__doc__`로 읽는다. 내 함수의 두 번째 문자열은 함수 설명의 첫 문자열을 바꾸지 않는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/11_fn.py` 27–48행

```python
def not_ten(a) :
    if a == 10 :
        return # return 값이 없을 때 'none' 반환, else처럼 사용할 수 있음
    print(a)

b = not_ten(10)
print('b : ', b)

def add_sub(a,b) :
    x = a + b
    y = a - b
    return x, y

c = add_sub(1, 2) 
print(c, type(c)) # 하나에 받았을 경우 튜플로 반환 됨 (return x,y 가 튜플이기 때문)

d, e = add_sub(1,2)
print(d, type(d), e, type(e)) # 두 곳에 나누어 받았을 땐 튜플이 아닌, 해당 자료형

x = add_sub(1,2) # add_sub에 있는 지역변수이기 때문에 사용할 수 있음
# x = add_sub(1,2,3) # TypeError: add_sub() takes 2 positional arguments but 3 were given 전달인자가 넘었을 때 발생
print(x)
```

**발췌 바로 풀이:** `not_ten(10)`은 `return`만 만나 함수가 끝나므로 `b`는 `None`이다. `add_sub(1,2)`는 `1+2=3`, `1-2=-1`을 **튜플 `(3, -1)`**로 반환한다. `d, e = add_sub(1,2)`는 그 두 값을 나누어 받는다. 내 코드의 `x = add_sub(1,2)`는 함수 안의 지역 변수 `x`를 직접 꺼내 온 것이 아니라 **함수의 반환값 튜플을 새로운 바깥 변수 `x`에 대입**한 것이다. 이 차이를 기억하면 지역 변수 설명과 충돌하지 않는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/11_fn.py` 109–138행

```python
def local_var() :
    a2 = 10
    print(a2)

local_var()
# print(a2) # local_var의 지역변수이기 때문에 사용 불가

def ref(a) :
    a.append(4)

b = [1,2,3]
ref(b) # 전달인자 또는 =으로 가게되면 stack의 주소값이 들어감 + 원본 변경
print(b)

def fn1(a) :
    return a + 10
def fn2(a) :
    return a * 10

c = 10
b = fn1(c) # 20
print(b)
d = fn2(b) # 200
print(d)

e = fn2( fn1(c) )
print(e)

# 전달인자에 함수 자체만 주었을 때 변수 취급하며 껍데기가 나옴( <function fn1 at 0x0000021CF3C13CC0> )
print(fn1)
```

**발췌 바로 풀이:** `local_var()` 안의 `a2`는 함수 밖에서 바로 읽을 수 없다. 반면 `ref(b)`는 **같은 리스트 객체에 `append(4)`**를 하므로 호출 뒤 `b`는 `[1,2,3,4]`다. 강사님 함수는 바뀐 리스트를 `return`까지 하지만 호출한 자리에서 그 반환값을 저장하지 않는다. 내 함수에는 반환문이 없지만 `append`의 변경은 남는다. 이 현상은 내 주석의 “주소값이 들어간다”보다 **같은 변경 가능한 리스트를 참조한다**고 설명하는 편이 분명하다.

내 hello 앞 호출은 주석이므로 현재 NameError를 발생시키지 않는다. add는 print만 하고 add2는 합을 반환한다. add 안 첫 문자열은 __doc__로 읽으며 뒤쪽 문자열이 첫 설명을 바꾸지 않는다. not_ten(10)은 값 없는 return으로 None을 돌려준다. x=add_sub(1,2)는 반환 튜플을 새 바깥 x에 받는 것이지 함수 내부 x에 직접 접근하는 코드가 아니다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

add2 정의 → add2(1,2) 호출 → a=1·b=2 → 합 3 → return → 호출 식이 3이 됨 → c에 대입 → print(c) 순서다. fn2(fn1(c))는 fn1의 반환이 fn2 인자가 된다. ref의 정의도 원본에 함께 실었다. 매개변수 a와 호출한 b가 같은 리스트를 보므로 append 변경이 b에서도 보인다. 함수 객체 출력의 주소 모양은 실행마다 달라질 수 있어 고정 숫자로 외우지 않는다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 내 원본은 출력·반환·튜플 분해·리스트 변경을 실제 호출로 비교한다. **교정:** 참조 전달을 메모리 영역 주소 암기로 설명하기보다 같은 객체를 가리키고 무엇을 바꾸는지 관찰한다. **중요한 차이:** ref에 return이 없어도 변경은 남는다. **개선 방향:** 다른 계산에서 쓸 값이면 반환으로, 사용자 관찰만 필요하면 출력으로 역할을 정하고 함수 이름·설명도 그 역할에 맞춘다.

개선안은 D 드라이브 원본을 수정한 결과가 아니다. 실제 오류·수업용 단순화·목적에 따른 선택을 구별한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



강사님 ref는 바뀐 리스트를 return하고 내 ref는 반환문이 없다. 실제 호출 ref(b)는 양쪽 모두 반환값을 저장하지 않아 b의 변화는 같다. 그러나 result=ref(b)로 바꾸면 강사님은 리스트, 내 코드는 None이므로 별도 입력 조건에서 차이가 드러난다. 같은 결과와 같은 함수 계약은 구별한다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 식 | 함수 안에서 일어남 | 호출한 곳에서 받음 |
| --- | --- | --- |
| add(1,2) | 3 출력 | None |
| add2(1,2) | 3 계산·반환 | 3 |
| not_ten(10) | 즉시 값 없이 종료 | None |
| add_sub(1,2) | 합·차 계산 | (3,-1) |
| 내 ref(b) | 같은 리스트 append | None, b 변경은 남음 |

함수 이름만 출력하면 함수를 실행하지 않는다. 함수의 정의가 있다는 사실과 호출 지점에 도달했다는 사실도 다르다. 지역 이름 a2는 local_var 안에서 준비하므로 함수 밖에서 그 이름을 바로 읽을 수 없다.

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| show_sum에 return 추가 | shown에도 합 | 출력과 반환 둘 다 수행 |
| append_four에서 items를 새 []로 대입 | 원래 numbers는 그대로 | 내용 변경과 이름 재대입 차이 |
| 함수 참조에 괄호 추가 | 즉시 호출 결과를 저장 | 함수 값과 반환값 차이 |
| return 뒤 print 추가 | 그 줄은 안 실행 | 함수 종료 |

None으로 계산하다 오류가 나면 함수가 무엇을 반환하는지 본다. 화면이 비면 반환만 하고 출력하지 않았는지 확인한다. 리스트가 함께 바뀌면 같은 객체 변경인지 본다. NameError는 정의 순서와 이름의 범위를 확인한다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 타입 힌트로 함수 계약 표현하기·복잡한 함수형 구성·세부 메모리 구현은 추가 학습이다. 기본은 정의→호출→반환과 출력·변경을 나누는 것이다.

TIP은 기본 문제의 필수 조건이 아니다. 배운 문법을 확인한 📚 출처와 선택 확장을 구별한다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. print만 한 함수의 호출 결과는?
2. return x,y를 하나로 받으면 자료형은?
3. 반환이 None이어도 리스트가 바뀔 수 있는가?
4. fn2(fn1(10))은 어느 함수가 먼저 결과를 만드는가?

<details>
<summary>풀이 — 먼저 자신의 답을 적은 뒤 펼치기</summary>

별도 반환이 없으면 None이다. 튜플이다. 같은 리스트 내용을 바꾸면 반환과 별개로 변경이 남는다. 안쪽 fn1이 먼저다.

</details>

| 구분 | 질문 |
| --- | --- |
| 정의 | 언제 이름이 생기나? |
| 호출 | 어떤 값을 넣나? |
| 반환 | 무엇을 받나? |
| 효과 | 출력·객체 변경은 별개인가? |

[장별 연습문제](실습/연습문제/11-01_Python_함수와_반환값_연습문제.md) · 다음은 [인자 전달](11-02_Python_함수_인자전달.md)이다.

<!-- 이전 명시 앵커 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
