# 06. 시퀀스와 슬라이싱 — 원하는 위치를 잘라 읽기

[Python 목차](README.md) · [이전: 튜플](05_Python_튜플과_불변자료형.md)

두 원본 `06_sequence.py`는 리스트·문자열·튜플에서 **값 포함 여부, 길이, 위치, 일부 구간**을 읽는다. 앞 장의 리스트 메서드를 다시 나열하지 않고 슬라이싱의 시작·끝·간격을 집중해서 본다.

<!-- chapter-toc -->

- [1. 포함 여부·연결·길이](#section-1)
- [2. 인덱스와 수정 가능 여부](#section-2)
- [3. 시작·끝·간격으로 자르기](#section-3)
- [4. 잘라 낸 위치에 새 값 넣기](#section-4)
- [직접 확인할 질문](#section-5)
- [추가로 알면 좋은 것](#section-6)

<a id="section-1"></a>

## 1. 포함 여부·연결·길이

### 강사님 코드

출처: `teacher/workspace_python/_06_sequence.py` 3–27행 · **원본 발췌**

```python
print( 20 in a )
print( 200 in a ) # False
print( not (200 in a) )
print( 200 not in a )

a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)

a = 'hello'
b = 'world'
c = a+b
print(c)

# c = a + 3
c = a + str(3)
print(c)

print('-' * 10)

print( len(a) )

hello = '안녕하세요'
b = hello.encode('utf-8')
```

### 내 코드

출처: `me/workspace_python/06_sequence.py` 2–31행 · **원본 발췌**

```python
a = [0, 10, 20, 30, 40] 
print( 20 in a  ) #True
print( 200 in a  ) #False
print( not ( 200 in a  ) ) # !대신 not 사용
print( 200 not in a )

a = [1,2,3]
b = [4,5,6]
c = a + b # range + range는 불가하지만, list나 tuple로 바꾸면 합칠 수 있음
print( c )

a = 'hello'
b = 'world'
c = a+b
print(c)

# javascript에서는 가능하지만, python은 sequence 끼리만 가능함
# c = a + 3 
c = a + str(3) 
print(c)

print('-' * 10)

print( len(a) ) # len으로 감싸면 길이를 구할 수 있다(문자,숫자,튜플 등)

hello = '안녕하세요'
b = hello.encode('utf-8')
print( len(b) )
print(b)
print(hello[0]) # '안'
```

`20 in a`는 값이 있는지 확인하고 `200 not in a`는 값이 없으면 참이다. 리스트끼리 `+`로 이어 붙이면 새 리스트가 되고, 문자열끼리 이어 붙이면 새 문자열이 된다. `'hello' + 3`은 그대로 실행할 수 없어 두 원본은 `str(3)`으로 바꾼다. `'-' * 10`은 같은 문자열을 열 번 반복한다.

`len(a)`는 이 자리의 **문자열** 길이를 잰다. 내 주석의 “문자, 숫자, 튜플 등” 중 **정수 하나에 `len`을 직접 쓰는 것**은 맞지 않는다. `hello.encode('utf-8')`는 문자열을 바이트로 변환한다. 한글 글자 수와 인코딩된 바이트 길이가 다를 수 있어 `len(b)`와 `len(hello)`를 같은 뜻으로 읽지 않는다.

<a id="section-2"></a>

## 2. 인덱스와 수정 가능 여부

### 강사님 코드

출처: `teacher/workspace_python/_06_sequence.py` 29–39행 · **원본 발췌**

```python
print(b)
print(hello[0])

a = [1,2,3,4]
print(a[0])
print(a[-2])
a[0] = 2
# print(a[100]) # IndexError

a = (1,2,3)
print(a[0])
```

### 내 코드

출처: `me/workspace_python/06_sequence.py` 33–46행 · **원본 발췌**

```python
a = [1,2,3,4]
print(a[0]) # 1
print(a[-2]) # 3 (-는 뒤에서 몇 번째 index)

# IndexError: list index out of range
# print(a[100]) # 배열의 범위를 벗어나면 error발생, javascript만 undefined

a = (1,2,3)
print(a[0])
# tuple은 'readonly' 형태기 때문에 값은 바꿀 수 없다
# a[0] = 3 # TypeError: 'tuple' object does not support item assignment
a = [1,2,3]
del a[0]
print(a)
```

`a[0]`은 첫 값이고 `a[-2]`는 뒤에서 두 번째 값이다. 리스트는 `a[0] = 2`처럼 해당 위치의 값을 바꿀 수 있다. 튜플은 읽을 수 있지만 그 위치에 대입하는 줄은 주석 처리됐다. 내 코드는 `del a[0]`으로 리스트 첫 요소를 삭제하는 연습도 했다. 범위를 벗어난 단일 인덱스 `a[100]`은 오류가 나므로 원본에서는 주석이다.

<a id="section-3"></a>

## 3. 시작·끝·간격으로 자르기

### 강사님 코드

출처: `teacher/workspace_python/_06_sequence.py` 41–61행 · **원본 발췌**

```python

a = [0,1,2,3,4,5,6,7,8,9]
print( a[1:4] )
print( a[4:-1] )
print( a[4:100] ) # 범위를 벗어나도 에러 없음

print( a[1:9:2] )

print( a[:7] )
print( a[5:] )
print( a[:] )

print( a[7:3] )
print( a[7:3:-1] )
print( a[8:4:-1] )

print( a[-4:8] )
print( a[-4:-2] )

print( a )
a[2:5] = ['a', 'b', 'c']
```

### 내 코드

출처: `me/workspace_python/06_sequence.py` 48–64행 · **원본 발췌**

```python
a = [0,1,2,3,4,5,6,7,8,9]
print( a[1:4] ) # index 1~4 앞까지 새 리스트로 생성 (slice)
print( a[4:-1] )
print( a[4:100] ) # 범위를 벗어나도 에러는 없음

print( a[1:9:2] ) # [시작INDEX,끝INDEX,반복INDEX]

print( a[:7] ) # 처음부터 [:끝INDEX] 까지
print( a[5:] ) # [시작INDEX] 부터 끝까지
print( a[:] ) # 배열에 있는 전체 다

print( a[7:3] ) # 이건 값이 나오지 않음
print( a[7:3:-1] ) # 여기서 -1은, -1씩 뒤부터 출력
print( a[8:4:-1] ) # 여기서 -1은, -1씩 뒤부터 출력

print( a[-4:8] ) # 결과값 6,7 : 뒤의 4번째부터 8바로 앞까지
print( a[-4:-2] ) # 결과값 6,7 : 뒤의 4번째부터 뒤의 2번째까지
```

`a[1:4]`는 1번부터 **4번 직전**까지인 `[1,2,3]`을 만든다. `a[1:9:2]`의 마지막 `2`는 두 칸씩 이동하라는 **간격**이다. 내 주석의 ‘반복 INDEX’보다 간격이라고 읽는 편이 정확하다. `a[4:100]`은 끝을 넘어도 있는 부분까지만 돌려준다. 단일 `a[100]`과 다른 점이다.

앞으로 읽는 기본 간격에서 `a[7:3]`은 비어 있다. `a[7:3:-1]`은 뒤로 한 칸씩 이동하므로 `7,6,5,4`가 된다. `a[-4:-2]`는 이 리스트에서 `6,7`이다.

<a id="section-4"></a>

## 4. 잘라 낸 위치에 새 값 넣기

### 강사님 코드

출처: `teacher/workspace_python/_06_sequence.py` 63–80행 · **원본 발췌**

```python

print(a[2:5])
a[2:5] = [10,20,30,40,50]
print( a )

ko = ['책', '알약', '철판']
en = ['book', 'pill', 'plate']

view = ko
view = en

print( view[0] )

a = 'hello' # olleh
# a = 'TENET'
print( a[::-1] )


```

### 내 코드

출처: `me/workspace_python/06_sequence.py` 66–84행 · **원본 발췌**

```python
print( a )
a[2:5] = ['a', 'b', 'c']
print( a )

print( a[2:5] )
a[2:5] = [10, 20, 30, 40, 50] # 원하는 자리에 원하는 값으로 바꿀 수 있음
print( a )

ko = ['책', '알약', '철판']
en = ['book', 'pill', 'plate']

# 같은 key에 번역 된 말을 써놓고 몇 번째 자리인지 비교해서 교차하기도 함
view = ko
view = en

print( view[0] ) 

a = 'hello'
print( a[::-1] )
```

`a[2:5] = ['a','b','c']`는 세 위치를 새 값으로 바꾼다. 뒤에서 다섯 값으로 대입하면 리스트 길이도 늘어난다. 내 코드의 `view = ko` 바로 다음 `view = en`은 `view`를 영어 리스트로 다시 지정하므로 `print(view[0])`은 **`book`**이다. 이 두 줄만으로 한국어 단어와 영어 단어의 대응 관계를 찾아 출력하는 기능이 만들어지지는 않는다.

문자열 `'hello'[::-1]`은 거꾸로 읽은 새 문자열 `'olleh'`를 돌려준다. 원래 변수 `a`의 문자열을 바꾸지는 않는다.

<a id="section-5"></a>

## 직접 확인할 질문

1. `a[7:3]`과 `a[7:3:-1]`의 결과는 왜 다를까?
2. `'안녕하세요'`의 글자 수와 UTF-8 바이트 길이는 왜 다를까?
3. `view = ko; view = en` 뒤 `view[0]`은 어느 리스트에서 읽을까?

<a id="section-6"></a>

## 추가로 알면 좋은 것

슬라이스를 사용해 새 페이지 처리 도구를 설계하는 내용은 이 원본 밖의 확장이다. 먼저 시작·끝·간격과 단일 인덱스의 차이를 예측해 보자.

