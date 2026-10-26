# 04. 리스트 — 여러 값을 순서대로 다루기

[Python 목차](README.md) · [이전: 문자열](03_Python_문자열과_포매팅.md) · [다음: 참조·순회·컴프리헨션](04-02_Python_리스트참조와_컴프리헨션.md)

양쪽 `04_list.py`는 리스트 만들기, 값 추가·삭제, 정렬, 복사, 순회까지 긴 실습이다. 이 장은 **리스트 값을 직접 바꾸는 동작**을 먼저 다루고, 참조와 반복은 다음 문서로 분리한다.

<!-- chapter-toc -->

- [1. 리스트 만들고 값 붙이기](04_Python_리스트와_데이터처리.md#section-1)
- [2. 정렬·뒤집기·삭제](04_Python_리스트와_데이터처리.md#section-2)
- [3. 길이 끝 위치와 슬라이스 추가](04_Python_리스트와_데이터처리.md#section-3)
- [직접 확인할 질문](04_Python_리스트와_데이터처리.md#section-4)
- [추가로 알면 좋은 것](04_Python_리스트와_데이터처리.md#section-5)

<a id="section-1"></a>

## 1. 리스트 만들고 값 붙이기

### 강사님 코드

출처: `teacher/workspace_python/_04_list.py` 1–46행 · **원본 발췌**

```python

a = []
b = list()
print( type(a) )
print( type(b) )

a = [1,2,3]
print(a)

# range
# 전달인자 1개 : 0부터 숫자 바로 앞 까지
c = range(10)
print(c)
print( list(c) )

# 전달인자 2개 : 첫 번째 부터 두 번째 바로 앞
d = range(5, 12)
print(list(d))

e = range(12, 5) # []
print(list(e))

# 전달인자 3개 : 첫 번째 부터, 두 번째 바로 앞까지, 세 번째씩 건너 뛰기
f = range(-4, 10, 2)
print(list(f))

a = [0,1,2,3,4,5]
a = list(range(6))

del a[3]
print(a)

a = a + [6]
print(a)

a += [7]
print(a)

a.append(8)
print(a)

b = [9,10]
a.append(b)
print(a) # [0, 1, 2, 4, 5, 6, 7, 8, [9, 10]]

print('-='*30)
```

### 내 코드

출처: `me/workspace_python/04_list.py` 1–48행 · **원본 발췌**

```python

a = []
b = list()
print(type(a))
print(type(b))

a = [1,2,3]
print(a)

# 전달인자가 하나인 경우, 0번부터 시작해서 숫자 바로 앞까지(0~9)를 만들어라
c = range(10)
print(c)
# list는 배열의 선언보다 배열로 바꾸어주는 것
print(list(c)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 전달인자가 두개인 경우, 첫 번째 두 번째 바로 앞까지
d = range(5, 12)
print(list(d)) # [5, 6, 7, 8, 9, 10, 11]

e = range(12, 5)
print(list(e)) # value: [] 빈 배열

# 전달인자가 세개인 경우 첫 번째 부터, 두 번째 바로 앞까지, 세 번째 값 씩 건너 뛰기(step)
f = range(-4, 10, 2)
print(list(f)) # [-4, -2, 0, 2, 4, 6, 8]
f1 = range(10,0,-1)
print(list(f1)) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

a = [0,1,2,3,4,5]
a = list(range(6))

del a[3]
print( a )

a = a + [6]
print( a )

a += [7]
print( a )
 
a.append(8) # python 에서는 list에 push대신 append로 붙일 수 있음
print( a )

b = [9,10] # concat개념이 아니라, append는 단순하게 하나를 추가하는 것
print( b , type(b) )
a.append(b)
print( a , type(a) ) # [0, 1, 2, 4, 5, 6, 7, 8, [9, 10]] <class 'list'>

```

`[]`와 `list()`는 빈 리스트를 만든다. `range(6)`을 리스트로 바꾸면 `0`부터 `5`까지 담긴다. `a + [6]`은 새 리스트를 만들고 그 결과를 다시 `a`에 넣는다. `append(8)`은 기존 리스트 끝에 한 **요소**를 붙인다. 따라서 `append([9,10])`은 `9`와 `10`을 각각 붙이는 것이 아니라 중첩 리스트 한 개를 추가한다.

<a id="section-2"></a>

## 2. 정렬·뒤집기·삭제

### 강사님 코드

출처: `teacher/workspace_python/_04_list.py` 47–89행 · **원본 발췌**

```python
c = [654,156,964,15,35]
c.sort() # 오름차순
print(c)
c.sort(reverse=True)
print(c)


c = c[::-1]
print(c)

c.reverse()
print(c)

d = c.pop()
print(c, d)

c.insert(0, 100)
print(c)

c.insert(10, 200) # index를 벗어나면 걍 끝에
print(c)

c.extend([1,2]) # 리스트를 합쳐준다
print(c)

a = [1,2,3,4,2]
a.remove(2) # 처음 만나는 값을 찾아서 지운다
print(a)

if 5 in a :
    a.remove(5) # 없는 값은 에러난다

a = [1,2,3,4,2,4]
b = a.index(2)
print(b)
# b = a.index(5) # 없는 값은 에러
c = a.count(4)
print(c)

a.reverse()
print(a)

a.clear()
```

### 내 코드

출처: `me/workspace_python/04_list.py` 49–101행 · **원본 발췌**

```python
print(':='*30)
c = [654,156,964,15,35]
c.sort() # 오름차순 원본이 바뀜, [15, 35, 156, 654, 964]
print( c ) # JavaScript와 다르게 sort는 15 156이 아닌, 숫자 크기대로 정렬해줌
c.sort(reverse=True) # sort의 기본값은 reverse=False (오름차순)
print( c )
print(':='*30)

c = c[::-1] # -1은 원본을 바꾸지 않음, [964, 654, 156, 35, 15]
print( c )

c.reverse() # 내림차순 원본이 바뀜, [15, 35, 156, 654, 964]
print( c )

d = c.pop()
print(c, d)

c.insert(0,100) # 0번째에 100추가
print(c)

c.insert(10,200) # 10번째에 200추가인데, 범위를 넘어서도 끝으로 들어감
print(c)

# extend는 insert, append와 다르게 여러 개의 리스트 값을 원본에 추가해줌
c.extend([1,2])
print(c)

# remove는 처음 만나는 값을 찾아서 지워준다
a = [1,2,3,4,2]
a.remove(2)
print(a)

if 5 in a : # in으로 값이 있을 때 실행하도록 진행
    a.remove(5) # 없는 값의 경우 에러 발생

a = [1,2,3,4,2,4]
b = a.index(2)
print(b)
# b = a.index(5) # 없는 값의 경우 에러 발생
# b = a.find(5) # 리스트에서 find는 사용할 수 없음

# stack과 queue란?
# stack은 프링글스통 기존 스택 설명과 같이 넣을 때 뒤로가고 뺄 때도 뒤에서
# queue는 넣을 때 뒤로가고 뺄 때는 제일 앞에서
c = a.count(4)
print(c)

a.reverse()
print(a)
b = reversed(a)
print(b)

a.clear() # a = [] 는 동일하게 사용할 수 있음
```

`sort()`와 `reverse()`는 현재 리스트를 바꾼다. `c[::-1]`은 거꾸로 읽은 새 리스트를 만들고, 원본 코드처럼 **`c = c[::-1]`로 다시 대입하면** 그 뒤의 `c`는 새 리스트를 가리킨다. `pop()`은 마지막 요소를 빼면서 그 요소를 돌려주고, `insert`는 지정한 위치에 넣는다. `extend([1,2])`는 두 값을 각각 끝에 붙인다.

`remove(2)`는 첫 번째로 만난 `2` 하나를 지운다. 없는 값을 지우는 코드는 원본에서 주석 처리되어 있다. `index(5)`도 없는 값을 찾으면 오류가 나므로 주석이다. `count(4)`는 `4`가 몇 개 있는지 센다.

내 `a.clear() # a = [] 는 동일` 주석은 **최종 변수 a가 빈 리스트가 된다는 결과만 같다.** 다른 변수가 같은 리스트를 가리키면 `clear()`는 그 변수에도 빈 상태가 보이지만 `a = []`는 a만 새 리스트를 가리키게 된다. 이 차이는 다음 문서의 참조 예제와 연결된다.

<a id="section-3"></a>

## 3. 길이 끝 위치와 슬라이스 추가

### 강사님 코드

출처: `teacher/workspace_python/_04_list.py` 91–100행 · **원본 발췌**

```python
a = []

a = [1,2,3]
print( a[len(a):] )
# print( a[3] )
print( a[3:] )

# a[3:] = 4 #TypeError: must assign iterable to extended slice
a[3:] = [4,5,6]
print(a)
```

### 내 코드

출처: `me/workspace_python/04_list.py` 104–118행 · **원본 발췌**

```python
a = [1,2,3]
print( a[len(a):] )
# print( a[3] ) # a[3] 으로 하면 IndexError: list index out of range 발생
print( a[3:] ) # :을 넣으면 에러는 나지 않음

# a[3:] = 4 # TypeError: must assign iterable to extended slice 에러는 반복될 수 있는 배열같은 것이 필요
a[3:] = [4,5,6] # extend처럼 비슷하게 사용할 수 있음, append는 단독 1개이기 때문에 다름
print(a)

a[len(a):] = [500] # a의 길이는 3이고 3: (3부터)라는 뜻이기 때문에, index 3에 500추가
print(a)

f = [] # 비어있으면 False
print( len(f) ) # False
print( not len(f) ) # True
```

리스트 길이가 3일 때 `a[3]`은 존재하지 않는 요소 하나를 읽으려 해 오류가 나지만, `a[3:]`는 비어 있는 부분 리스트를 돌려준다. `a[3:] = [4,5,6]`은 끝에 세 값을 넣는다. 내 코드에서 이어지는 `a[len(a):] = [500]` 시점에는 `a` 길이가 **이미 6**이다. “길이는 3”이라는 주석은 이전 상태를 가리킨 설명으로, 그 줄의 실제 상태와 다르다.

빈 리스트 `f`에 대해 `len(f)`의 결과는 `False`가 아니라 **정수 0**이다. `not len(f)`는 0이 거짓으로 평가되어 `True`가 된다. 값과 진리값 해석을 구분한다.

<a id="section-4"></a>

## 직접 확인할 질문

1. `append([9,10])`과 `extend([9,10])` 뒤 리스트의 마지막 부분은 어떻게 다를까?
2. `a[3]`과 `a[3:]`는 왜 결과가 다를까?
3. `len([])`와 `not len([])`는 자료형과 값이 각각 무엇일까?

<a id="section-5"></a>

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/04_Python_리스트와_데이터처리_연습문제.md)

## 추가로 알면 좋은 것

리스트를 큐나 스택 자료구조로 본격 설계하는 내용은 이 파일의 간단한 `append`·`pop` 관찰보다 넓다. 먼저 수업에서 실행한 메서드가 원본을 바꾸는지 확인한다.

