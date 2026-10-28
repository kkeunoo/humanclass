# 04-02. 리스트 참조·복사·순회·컴프리헨션

[Python 목차](README.md) · [이전: 리스트 기본](04_Python_리스트와_데이터처리.md)

같은 리스트를 두 이름으로 가리키는 경우와 새 리스트를 만드는 경우를 먼저 비교한다. 그 뒤 `for`·`enumerate`·컴프리헨션으로 값을 읽고 새 리스트를 만드는 연습을 이어간다.

## 먼저: 무엇이 같고 무엇이 새로 만들어지는가?

리스트를 다른 이름에 대입할 때는 **값을 통째로 복사했다고 생각하기 쉽다.** 다음은 수업 문법만 사용한 작은 설명용 예제다.

```python
a = [1, 2]
b = a
b.append(3)
print(a)  # [1, 2, 3]
print(b)  # [1, 2, 3]
```

이름 `a`와 `b`가 **같은 리스트**를 가리키므로 한쪽에서 내용을 바꾸면 다른 이름으로 봐도 바뀐다. `b = a.copy()`로 시작했다면 바깥 리스트가 새로 만들어져, 이 한 단계 숫자 리스트에서는 `a`가 `[1, 2]`로 남는다. `copy()`가 무엇까지 복사하는지는 이 장의 원본 비교와 [00 메모리와 참조](../00_메모리와_참조%28Stack_Heap%29/README.md)에서 연결한다.

두 번째 질문은 **기존 값을 읽는가, 새 결과를 만드는가**다. `for`로 하나씩 읽으며 `append`하면 결과 리스트를 직접 채우고, 컴프리헨션은 새 리스트를 만드는 식으로 같은 목표를 짧게 쓸 수 있다. 둘 중 어느 표현이 적합한지는 결과와 읽기 쉬운 정도를 함께 보자.

<!-- chapter-toc -->

- [1. 같은 리스트를 가리키는가?](04-02_Python_리스트참조와_컴프리헨션.md#section-1)
- [2. 값과 위치를 함께 읽기](04-02_Python_리스트참조와_컴프리헨션.md#section-2)
- [3. 반복문과 컴프리헨션 비교](04-02_Python_리스트참조와_컴프리헨션.md#section-3)
- [직접 확인할 질문](04-02_Python_리스트참조와_컴프리헨션.md#section-4)
- [추가로 알면 좋은 것](04-02_Python_리스트참조와_컴프리헨션.md#section-5)

<a id="section-1"></a>

## 1. 같은 리스트를 가리키는가?

### 강사님 코드

출처: `teacher/workspace_python/_04_list.py` 102–115행 · **원본 발췌**

```python
a = [1,2,3,4,5]
b = a
b[2] = 30
print(b)
print(a)

a = [1,2,3,4,5]
b = a.copy()
b[2] = 30
print(b)
print(a)



```

### 내 코드

출처: `me/workspace_python/04_list.py` 120–135행 · **원본 발췌**

```python
a = [1,2,3,4,5]
b = a # 이렇게 넣으면 a = b의 주소값이 동일해지기 때문에, index값을 바꾸면 두개가 모두 바뀜
b[2] = 30
print(b)
print(a)

a = [1,2,3,4,5]
b = a.copy() # copy를 이용하면 모든 요소를 아예 복사해오기 때문에, 이럴 땐 주소값이 달라져 개별 값만 바꿔짐
b[2] = 30
print(b)
print(a)

a = [1,2,3,4,5]
b = a.copy() 
print( a is b ) # False (주소값이 다르기 때문에 주소까지 전부 같지 않음)
print( a == b ) # True (안에 있는 값은 같음)
```

`b = a`는 새 리스트를 만들지 않으므로 `b[2] = 30`을 실행하면 `a[2]`도 30으로 보인다. `b = a.copy()`는 바깥 리스트를 새로 만들어 여기서처럼 숫자 요소만 있는 예제에서는 `b[2]`를 바꿔도 `a[2]`는 그대로다. 그래서 마지막의 `a is b`는 `False`, `a == b`는 `True`다.

내 주석의 “모든 요소를 아예 복사”는 **중첩 리스트의 안쪽까지 새로 만드는 깊은 복사**로 이해하면 안 된다. 이 실습의 `copy()`는 바깥 리스트를 복사하는 단계다. 같은 값인지 `==`, 같은 객체인지 `is`로 구분한다.

<a id="section-2"></a>

## 2. 값과 위치를 함께 읽기

값만 필요하면 `for value in a`, 위치도 필요하면 `for index, value in enumerate(a)`를 쓴다. 다음 출력은 코드의 두 이름이 무엇을 받는지 보여 주는 **설명용 재구성**이다.

```python
colors = ['빨강', '파랑']
for index, value in enumerate(colors, start=100):
    print(index, value)
# 100 빨강
# 101 파랑
print(colors[0])  # 빨강
```

`start=100`은 출력에 쓰는 **번호**를 바꿀 뿐 `colors[0]`의 실제 위치를 100으로 옮기지 않는다. 아래의 원본도 같은 차이를 확인한다.

### 강사님 코드

출처: `teacher/workspace_python/_04_list.py` 120–140행 · **원본 발췌**

```python
a, b = (1,2)

a = [10,20,30]
for i in a :
    print(i)

# 이번 턴의 index, value를 한번에 뽑아 줌 
for index, value in enumerate(a) :
    print(index, value)

# 시작 인덱스 지정 가능
for index, value in enumerate(a, start=100) :
    print(index, value)

b = 7
a = [7, 3, 5, 8, 4]
# 가장 큰 수 찾기
a.sort()
print(a[len(a)-1])
print(a[-1])

```

### 내 코드

출처: `me/workspace_python/04_list.py` 143–171행 · **원본 발췌**

```python
a, b = (1,2)
print(a, b)

a = [10,20,30]
for i in a :
    print(i)

# enumerate(인자)는 index, value를 같이 뽑아낼 수 있는 함수
for index, value in enumerate(a) :
    print(index, value)

# 아래처럼 인자와 ,를 쓰게되면 start로 시작 index를 조절할 수 있음
for index, value in enumerate(a, start=100) :
    print(index, value)

# 제일 큰 값을 찾기 위해 오름차순으로 정렬
a = [7,3,5,8,4]
a.sort()
print(a[len(a)-1])
print(a[-1])

# index, value 한 번 더 확인
# for index, value in enumerate(a) :
#     print(index, value)

# a의 len만큼 i를 돌게하고, 만약 i가 리스트의 마지막 일 때 그 값 출력
for i in range(len(a)) :
    if i == len(a)-1 :
        print(a[i])
```

`for i in a`는 리스트의 값만 차례로 꺼낸다. `enumerate(a)`는 위치와 값을 함께 준다. `start=100`은 **보여 주는 번호**를 100부터 시작하게 하며 리스트 안의 실제 인덱스를 바꾸지 않는다. 내 코드에서는 정렬한 리스트의 마지막 값을 `a[-1]` 또는 길이를 이용한 위치로 읽어 본다.

<a id="section-3"></a>

## 3. 반복문과 컴프리헨션 비교

컴프리헨션을 처음 볼 때는 `[**결과에 넣을 값** for **현재 값** in **대상** if **조건**]`으로 나누어 읽는다. `if`가 없는 가장 작은 예부터 확인하자.

```python
# 두 코드는 이 숫자 조건에서 같은 결과를 만든다 — 설명용 재구성
by_loop = []
for number in range(4):
    by_loop.append(number * 2)
by_comprehension = [number * 2 for number in range(4)]
print(by_loop)           # [0, 2, 4, 6]
print(by_comprehension)  # [0, 2, 4, 6]
```

먼저 `range(4)`의 값 0·1·2·3을 꺼내고, 각 값을 두 배로 만들어 결과에 넣는다. 원본의 더 긴 코드에서 `if i % 2 == 0`이 붙으면 **짝수만 통과**한다. 코드를 짧게 썼다는 이유로 앞서 만든 리스트까지 자동으로 바뀌는 것은 아니다.

### 강사님 코드

출처: `teacher/workspace_python/_04_list.py` 142–167행 · **원본 발췌**

```python
a = []
for i in range(10):
    a.append(i)
a = [ i for i in range(10) ]
a = [ i*2 for i in range(10) ]
for i in range(10):
    a.append(i*2)
# a = [0, 2, 4]

a = []
for i in range(10):
    if i%2 == 0 :
        a.append(i)

a = list(   f'2x{i}={2*i}' for i in range(10) if i%2 == 0  )
print(a)

a = [1.2, 2.5, 3.7, 4.6, -3.5]
for i, value in enumerate(a) :
    a[i] = int(value)
print(a)

# 두 번째 반복되는 것을 하나씩 꺼내서
# 첫 번째 함수에 넣고
# 결과를 배열로 만들어 준다
a = list(map(int, a))
```

### 내 코드

출처: `me/workspace_python/04_list.py` 173–203행 · **원본 발췌**

```python
# a 배열에 0~9를 넣음

a = []
for i in range(10) :
    a.append(i)
print(a)

# for i in range(10)의 i를 배열로 만들어라
a = [ i for i in range(10) ] 
print(a)

a = []
for i in range(10) :
    if i % 2 == 0 :
        a.append(i)
print(a)

a = list( i for i in range(10) if i % 2 == 0 )
print(a)

# 값을 int로 바꿔서 저장
a = [1.2, 2.5, 3.7, 4.6, -3.5]
for i, value in enumerate(a) :
    a[i] = int(value)
print(a)

# 두번째 반복되는 것을 하나씩 꺼내서, 첫 번째 함수에 넣고
# 결과를 배열로 만들어 주는 것이 map과 int
a = [1.2, 2.5, 3.7, 4.6, -3.5]
a = list(map(int, a))
print(a)
```

`for`로 빈 리스트에 `append`하는 방법과 `[i for i in range(10)]`은 이 예제에서 같은 0–9 값을 만든다. `if i % 2 == 0`을 붙이면 짝수만 남긴다. 내 `list(i for i in range(10) if i % 2 == 0)`도 결과를 리스트로 만드는 짧은 사용 예다. 이터레이터·제너레이터의 내부 구현은 사용자가 개념과 간단 사용만 배웠다고 확인했으므로 이 장의 기본 문제로 요구하지 않는다.

실수 배열에서 `int(value)`로 정수로 바꾸는 반복문과 `list(map(int, a))`도 같은 학습 목표를 비교한다. `int(-3.5)`는 `-3`이며 단순히 아래 정수 `-4`로 내리는 연산과 다르다.

<a id="section-4"></a>

## 직접 확인할 질문

1. `b = a`와 `b = a.copy()` 뒤에 b의 한 위치를 고치면 a는 어떻게 될까?
2. `enumerate(a, start=100)`의 첫 번호와 실제 `a[0]`의 인덱스는 같은가?
3. `range(10)`에서 짝수만 담는 원본의 두 표현은 무엇인가?

<details>
<summary>답과 이유 — 먼저 적고 펼치기</summary>

1. `b = a`라면 같은 리스트이므로 `a`에서도 변경이 보인다. `b = a.copy()`라면 숫자만 담긴 이 예제에서 `a`는 그대로다.
2. 첫 출력 번호는 100이어도 `a[0]`의 인덱스는 여전히 0이다.
3. 빈 리스트에 `for`·`if`·`append`로 넣거나, `[i for i in range(10) if i % 2 == 0]`처럼 새 리스트를 만든다. 내 원본의 `list(i for i in range(10) if ...)`도 실제 사용했지만, 내부 제너레이터 구현까지 기본 문제로 요구하지 않는다.

</details>

<a id="section-5"></a>

## 추가로 알면 좋은 것

> [!TIP]
> 중첩 리스트까지 독립적으로 복사하는 방법이나 제너레이터의 상세 구현은 별도 확장 학습이다. 사용자가 이터레이터·제너레이터는 **개념과 간단한 사용만 배웠다**고 확인했다. 이 장의 기본 문제는 바깥 리스트의 참조·복사, `enumerate`, 단순 컴프리헨션을 설명하는 데 집중한다.

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/04-02_Python_리스트참조와_컴프리헨션_연습문제.md) → [다음: 튜플](05_Python_튜플과_불변자료형.md)

