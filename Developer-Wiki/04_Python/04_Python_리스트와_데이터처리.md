# 04. 리스트 — 여러 값을 순서대로 담고 바꾸는 방법

[Python 목차](README.md) · [읽기 안내](00-00_Python_V3_동작_백과_읽기법.md)

점수 세 개를 score1·score2·score3으로 따로 다루면 값이 늘 때마다 코드도 늘어난다. 리스트는 여러 값을 한 이름 아래 순서대로 묶고 필요한 항목을 읽거나 추가·삭제하게 한다. 메서드의 이름보다 현재 리스트가 어떻게 바뀌는지 먼저 따라가 보자.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

리스트의 요소·인덱스·길이를 구별하고 append·extend·insert의 차이를 설명한다. 정렬·뒤집기·삭제의 반환값과 원본 변경을 나누고, 끝 위치의 인덱싱·슬라이싱 차이까지 연결한다.

실제 원본·새 예제·개선안·선택 학습을 구분하고 입력·실행 순서·반환값·출력을 연결한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

리스트는 순서가 있고 내용을 바꿀 수 있는 자료형이다. [80,90,80]은 세 요소이며 같은 값이 중복되어도 된다. 첫 요소의 인덱스는 0, 마지막은 길이에서 1을 뺀 2다. 길이는 요소 수이지 마지막 인덱스가 아니다. 빈 리스트는 [] 또는 list()로 만든다.

```text
scores = [80, 90, 80]
인덱스     0   1   2
길이       3
```

| 작업 | 무엇을 넣거나 찾는가? | 리스트 변경 | 반환값 |
| --- | --- | --- | --- |
| append(x) | 요소 하나 | 끝에 추가 | None |
| extend(xs) | 대상의 각 항목 | 끝에 각각 추가 | None |
| insert(i,x) | 위치와 요소 | 지정 위치에 추가 | None |
| pop() | 마지막 항목 | 제거 | 꺼낸 요소 |
| remove(x) | 값 | 처음 일치 하나 제거 | None, 없으면 오류 |
| sort() | 정렬 규칙 | 현재 리스트 정렬 | None |
| reverse() | 현재 순서 | 반대로 변경 | None |
| index·count | 값 | 조회만 함 | 위치·개수 |

append([9,10])은 리스트 한 개를 요소로 넣어 중첩 구조가 된다. extend([9,10])은 9와 10을 바깥에 각각 넣는다. 무엇을 요소 하나로 세는지를 알아야 길이도 맞게 읽는다.

내용 변경과 반환은 별개다. result=values.sort()는 values를 정렬하지만 result에는 None을 받는다. pop은 꺼낸 값을 돌려주므로 남은 리스트와 꺼낸 값을 따로 쓸 수 있다. reverse는 정렬하지 않고 현재 순서를 뒤집는다. 섞여 있는 값을 뒤집었다고 내림차순 정렬이 되는 것은 아니다.

> 📚 **출처 · 본문 설명 확인:** [Python 공식 자료 구조: 리스트 메서드](https://docs.python.org/ko/3/tutorial/datastructures.html#more-on-lists). 실제 배운 문법의 의미를 확인한 근거다. 예제·표·풀이 자체는 수업 자료를 바탕으로 새로 구성했다. 외부 문장을 직접 인용하지 않았다. 이번 문법 확인 기간: 2026-10-28~29.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 코드.** [실행 파일](실습/책형_복습/04_Python_리스트와_데이터처리.py)을 제공한다. Python이 설치된 환경에서 새 .py 파일로 저장해 실행한다. 터미널은 그 파일이 있는 폴더에서 열고 `python 파일이름.py`를 실행한다. VS Code의 Python 실행 기능을 사용해도 된다. 결과는 터미널에 표시된다.



```python
numbers = [3, 1, 2, 1]
print(numbers[0], len(numbers))
numbers.append([9, 10])
print(numbers, len(numbers))
inside = numbers.pop()
print('꺼낸 값', inside)
numbers.extend([4, 5])
result = numbers.sort()
print(numbers, result)
last = numbers.pop()
numbers.insert(0, 100)
numbers.remove(1)
print(numbers, last)
numbers.reverse()
print(numbers)
print(numbers.index(1), numbers.count(1))
print(numbers[len(numbers):])
numbers[len(numbers):] = [500]
print(numbers)
numbers.clear()
print(numbers, len(numbers), not len(numbers))
```

중첩 리스트를 하나 append하여 길이는 5가 된다. 이를 pop으로 다시 꺼낸 뒤 숫자만 남은 리스트를 extend·sort한다. 정렬 결과는 numbers에 있고 반환값 result는 None이다. 이후 5를 꺼내고 100을 앞에 넣은 뒤 첫 1만 지운다. reverse 후의 값은 내림차순이 아니라 현재 순서의 반대다. 마지막 clear 뒤 len은 정수 0이고 not len은 boolean True다.

**예상 출력 또는 관찰:**

```text
3 4
[3, 1, 2, 1, [9, 10]] 5
꺼낸 값 [9, 10]
[1, 1, 2, 3, 4, 5] None
[100, 1, 2, 3, 4] 5
[4, 3, 2, 1, 100]
3 1
[]
[4, 3, 2, 1, 100, 500]
[] 0 True
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본 발췌다. 주석의 잘못된 설명도 원문을 보존하고 풀이에서 교정한다. 필요한 선언·호출·다른 파일의 정의는 다음 절까지 연결해 읽는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/04_list.py` 1–48행

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

**발췌 바로 풀이:** `[]`와 `list()`는 빈 리스트를 만든다. `range(6)`을 리스트로 바꾸면 `0`부터 `5`까지 담긴다. `a + [6]`은 새 리스트를 만들고 그 결과를 다시 `a`에 넣는다. `append(8)`은 기존 리스트 끝에 한 **요소**를 붙인다. 따라서 `append([9,10])`은 `9`와 `10`을 각각 붙이는 것이 아니라 중첩 리스트 한 개를 추가한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/04_list.py` 49–101행

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

**발췌 바로 풀이:** `sort()`와 `reverse()`는 현재 리스트를 바꾼다. `c[::-1]`은 거꾸로 읽은 새 리스트를 만들고, 원본 코드처럼 **`c = c[::-1]`로 다시 대입하면** 그 뒤의 `c`는 새 리스트를 가리킨다. `pop()`은 마지막 요소를 빼면서 그 요소를 돌려주고, `insert`는 지정한 위치에 넣는다. `extend([1,2])`는 두 값을 각각 끝에 붙인다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/04_list.py` 104–118행

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

**발췌 바로 풀이:** 리스트 길이가 3일 때 `a[3]`은 존재하지 않는 요소 하나를 읽으려 해 오류가 나지만, `a[3:]`는 비어 있는 부분 리스트를 돌려준다. `a[3:] = [4,5,6]`은 끝에 세 값을 넣는다. 내 코드에서 이어지는 `a[len(a):] = [500]` 시점에는 `a` 길이가 **이미 6**이다. “길이는 3”이라는 주석은 이전 상태를 가리킨 설명으로, 그 줄의 실제 상태와 다르다.

내 range(10,0,-1)은 10부터 1까지이며 stop인 0은 들어가지 않는다. list는 빈 리스트를 만들거나 다른 반복 가능한 값에서 리스트를 만드는 데 사용한다. list는 배열로 바꾸는 역할만 있다는 메모로 제한하지 않는다. a+[6]은 새 리스트 결과를 a에 대입하고 a+=[7]과 append는 이 리스트의 내용을 바꾼다. 원본의 append(b)는 b 전체를 요소 하나로 담는다. 뒤의 정렬·삭제와 끝 슬라이스도 각 줄의 현재 리스트를 기준으로 읽는다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

리스트 생성 → 요소 조회·길이 확인 → 메서드 호출 → 원본 변화 확인 → 반환값 저장 → 이후 호출 순서다. c=c[::-1]은 뒤집은 새 리스트를 만든 뒤 c를 그 결과에 다시 연결한다. 이후 reverse는 새 c의 현재 순서를 바꾼다. 리스트를 가리키는 이름이 둘인 경우 clear와 새 [] 대입의 차이는 다음 참조 장에서 연결한다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 내 append 주석은 “여러 항목 펼치기와 요소 하나 추가”를 구분하고, in 검사로 없는 값 삭제를 피한다. **교정:** reverse를 내림차순 정렬이라고 부르지 않는다. 끝 슬라이스에 [4,5,6]을 넣은 뒤에는 길이가 이미 6이라 다음 len(a)도 6이다. len([])의 결과는 False가 아니라 정수 0이다. **설명 개선:** clear와 a=[]는 a 하나의 최종 모양만 같을 수 있고 같은 리스트를 보는 다른 이름의 관찰은 다르다.

개선안은 D 드라이브 원본을 수정한 결과가 아니다. 실제 오류·수업용 단순화·목적에 따른 선택을 구별한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



양쪽 리스트 메서드의 주요 흐름은 같아 강사님 코드를 반복하지 않는다. 내 감소 range와 빈 길이 실험은 추가 관찰로 설명한다. 반대로 원본 주석의 값이 앞 단계 상태와 어긋난 경우에는 현재 실행 줄을 기준으로 교정한다. 긴 코드를 썼다는 이유보다 값과 효과를 얼마나 분명히 확인했는지를 평가한다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 원본에서 진행한 작업 | 바로 뒤의 상태 | 주의점 |
| --- | --- | --- |
| list(range(6)) | [0,1,2,3,4,5] | 6 제외 |
| del a[3] | [0,1,2,4,5] | 인덱스 3의 값 삭제 |
| +[6]·+=[7]·append(8) | [0,1,2,4,5,6,7,8] | 새 리스트와 변경 구별 |
| append([9,10]) | 마지막 요소가 [9,10] | 바깥 길이 9 |

길이 3일 때 a[3]은 존재하지 않는 요소라 IndexError지만 a[3:]은 빈 구간 []다. a[3:]=[4,5,6]은 끝에 세 항목을 붙인다. 슬라이스가 범위를 벗어나도 여기서 잘린 구간을 줄 수 있다는 사실과 모든 인덱싱이 안전하다는 주장은 다르다. 리스트의 find는 없으며 없는 값의 index·remove는 ValueError다.

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| append를 extend로 변경 | 9·10이 각각 바깥 요소 | 추가 단위 차이 |
| sort 대신 reverse | 크기순 보장 안 됨 | 현재 순서 뒤집기 |
| 없는 값 remove | ValueError | 일치하는 항목 없음 |
| 빈 리스트에서 pop | IndexError | 꺼낼 요소 없음 |

None이 출력되면 원래 리스트 대신 변경 메서드의 반환값을 출력했는지 본다. 길이를 셀 때 안쪽 리스트가 바깥 요소 하나임을 확인한다. 위치 오류는 길이와 마지막 인덱스를 비교한다. 정렬 오류가 나면 서로 비교할 수 있는 종류의 값인지도 확인한다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** deque와 성능을 고려한 큐 설계, 깊은 복사 도구와 복잡한 정렬 키 설계는 추가 학습이다. 원본의 스택·큐 비유는 끝에서 넣고 빼는 동작 이해에 쓰고 별도 자료구조 구현까지 배웠다고 확장하지 않는다.

TIP은 기본 문제의 필수 조건이 아니다. 배운 문법을 확인한 📚 출처와 선택 확장을 구별한다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. append([9,10]) 뒤 길이는 두 개 늘어나는가?
2. sort의 반환값과 바뀐 리스트는 같은가?
3. reverse는 항상 내림차순인가?
4. len([])와 not len([])는 각각 무엇인가?

<details>
<summary>풀이 — 먼저 자신의 답을 적은 뒤 펼치기</summary>

한 요소가 추가되어 하나 늘어난다. sort는 리스트를 바꾸고 None을 반환한다. reverse는 현재 순서를 뒤집는다. 각각 정수 0과 boolean True다.

</details>

| 질문 | 확인 |
| --- | --- |
| 무엇을 세나? | 바깥 요소 수 |
| 무엇을 넣나? | 하나와 여러 항목 구분 |
| 무엇이 바뀌나? | 리스트 내용 |
| 무엇을 받나? | 반환값·None·꺼낸 요소 |

[장별 연습문제](실습/연습문제/04_Python_리스트와_데이터처리_연습문제.md) · 다음은 [리스트 참조·컴프리헨션](04-02_Python_리스트참조와_컴프리헨션.md)이다.

<!-- 이전 명시 앵커 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
