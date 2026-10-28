# 08. 조건문 — 조건에 따라 다른 길로 가기

[Python 목차](README.md) · [이전: 딕셔너리](07_Python_딕셔너리.md)

두 원본 `08_if.py`는 들여쓰기, 참·거짓 판정, 점수 판정, 메뉴 선택, `match`를 순서대로 연습한다. 먼저 **실제로 실행되는 줄**과 주석·설명 문자열을 구분해 읽자.

## 먼저: 조건문은 무엇을 결정하는가?

조건문은 **조건이 참인지에 따라 실행할 문장을 고른다.** Python에서는 들여쓰기가 어느 문장이 그 갈래에 속하는지 표시한다. 다음은 수업 문법으로 만든 작은 설명용 예제다.

```python
score = 82
if score >= 80:
    print('통과')
else:
    print('다시 확인')
# 출력: 통과
```

`score >= 80`은 참이므로 첫 번째 들여쓴 문장만 실행된다. 조건이 거짓이면 `else`의 문장이 실행된다. 먼저 이 두 갈래를 이해한 다음 원본의 `elif`·`match`로 선택지가 늘어난 경우를 읽자.

<!-- chapter-toc -->

- [1. `if`와 들여쓰기](08_Python_조건문.md#section-1)
- [2. 값의 참·거짓 판정](08_Python_조건문.md#section-2)
- [3. 네 점수의 범위와 평균 확인](08_Python_조건문.md#section-3)
- [4. 여러 선택지: `if`·`elif`·`else`](08_Python_조건문.md#section-4)
- [5. `match`·`case`와 한 줄 조건식](08_Python_조건문.md#section-5)
- [직접 확인할 질문](08_Python_조건문.md#section-6)
- [추가로 알면 좋은 것](08_Python_조건문.md#section-7)

<a id="section-1"></a>

## 1. `if`와 들여쓰기

### 강사님 코드

출처: `teacher/workspace_python/_08_if.py` 1–19행 · **원본 발췌**

```python
a = 10
b = 5
print( 3 < a < 20 )

if True :
    print(1)
# print(2)
    print(3)

    if True :
      print(4)

if True :
    pass
else :
    pass

if 1 :
    print('참')
```

### 내 코드

출처: `me/workspace_python/08_if.py` 1–20행 · **원본 발췌**

```python
a = 10
b = 5
print( 3 < a < 20 )

if True :
    print(1)
 #Indent가 들어가면 들여쓰기 오류
#  print(2) # IndentationError: unindent does not match any outer indentation level
    print(3)

    if True :
        print(4)

if True :
    pass # 아무 일도 하지 않고 넘어가는 것
else : 
    pass

if 1 :
    print('참')
```

`3 < a < 20`은 `a=10`일 때 참이다. `if True:` 아래에서 같은 블록만 실행되고, 더 안쪽의 `if True:`는 그 블록 안에서 한 번 더 검사한다. `pass`는 문법상 블록이 필요할 때 아무 동작 없이 자리를 채운다.

내 코드의 앞에 공백이 붙은 `#Indent가...`와 주석 처리된 `# print(2)`는 **실행되지 않는다**. 이 파일을 읽을 때 그 주석 자체가 들여쓰기 오류를 발생시켰다고 오해하면 안 된다. 실제 코드의 블록 들여쓰기는 일관되게 맞춰야 한다.

<a id="section-2"></a>

## 2. 값의 참·거짓 판정

### 강사님 코드

출처: `teacher/workspace_python/_08_if.py` 21–33행 · **원본 발췌**

```python
'''
파이썬에서 False란?
False, 
None, 
0, 0.0, 
빈 컨테이너(비어있는 문자열, 리스트, 튜플, 딕셔너리)
'''

a = []
if a :
    print('참')
else :
    print('거짓')
```

### 내 코드

출처: `me/workspace_python/08_if.py` 22–31행 · **원본 발췌**

```python
'''
Python에서 False란?
False, None(JavaScript:null), 0, 0.0, 빈 컨테이너(비어있는 문자열, 리스트, 튜플, 딕셔너리) 
'''

a = []
if a :
    print('참')
else :
    print('거짓')
```

원본은 `False`, `None`, 숫자 `0`, 빈 문자열·리스트·튜플·딕셔너리를 거짓으로 취급하는 예를 적었다. 여기서 `a=[]`이므로 `if a`는 거짓이 되어 `거짓`이 출력된다. 반대로 위의 `if 1`은 참이다. 설명을 담은 삼중 따옴표 부분은 출력문이 아니며, 그 자체로 예제를 실행하지 않는다.

<a id="section-3"></a>

## 3. 네 점수의 범위와 평균 확인

### 강사님 코드

출처: `teacher/workspace_python/_08_if.py` 35–53행 · **원본 발췌**

```python
# 174p. 문제 14.7
score = input('점수 4개 입력, 띄어쓰기로 구분 : ')
print(score, score.split(' '))
scores = score.split(' ')
sum = int(scores[0]) + int(scores[1]) + int(scores[2]) + int(scores[3])
avg = sum / len(scores)

if (0 <= int(scores[0]) <= 100) \
    and (0 <= int(scores[1]) <= 100) \
    and (0 <= int(scores[2]) <= 100) \
    and (0 <= int(scores[3]) <= 100) :

    if avg >= 80 :
        print('합격')
    else :
        print('불합격')
else :
    print('잘못된 입력')

```

### 내 코드

출처: `me/workspace_python/08_if.py` 48–66행 · **원본 발췌**

```python
score = input('점수 4개 입력, 띄어쓰기로 구분 : ')
print(score, score.split(' '))
scores = score.split(' ')
sum = int(scores[0]) + int(scores[1]) + int(scores[2]) + int(scores[3])
avg = sum / len(scores) 

# \ 를 쓰게되면 엔터를 없앨 수 있어서, 실제 코드는 한 줄이지만 내릴 때 사용
if (0 <= int(scores[0]) <= 100) \
    and (0 <= int(scores[1]) <= 100) \
    and (0 <= int(scores[2]) <= 100) \
    and (0 <= int(scores[3]) <= 100) :

    if avg >= 80 :
        print('합격')
    else :
        print('불합격') 
else :
    print('잘못된 입력입니다.')

```

입력을 공백으로 나눠 네 값을 `int(...)`로 바꾸고 평균을 낸다. 네 점수가 모두 0–100 범위면 `avg >= 80`을 검사해 `합격` 또는 `불합격`을 출력한다. 내 파일에는 점수를 네 번 따로 받는 초기 풀이가 삼중 따옴표 안에 남아 있지만, **실제로 실행되는 경로는 위의 공백 구분 입력**이다.

강사님과 내 코드 모두 **평균 계산이 네 점수의 개수·숫자 여부 확인보다 먼저** 일어난다. 값이 세 개뿐이면 인덱스 오류가 나고, 숫자로 바꿀 수 없는 값이면 변환 오류가 난다. `잘못된 입력` 분기는 이런 경우까지 처리하는 완전한 입력 검증이 아니라, 네 값을 숫자로 바꾸는 데 성공한 뒤 **범위를 벗어난 점수**를 확인한다. `split(' ')`은 공백 한 칸을 기준으로 나누므로 여러 칸 입력에도 유의해야 한다.

<a id="section-4"></a>

## 4. 여러 선택지: `if`·`elif`·`else`

### 강사님 코드

출처: `teacher/workspace_python/_08_if.py` 55–63행 · **원본 발췌**

```python
button = int(input('메뉴를 고르시오'))
if button == 1 :
    print('콜라')
elif button == 2 :
    print('사이다')
elif button == 3 :
    print('환타')
else :
    print('다시 고르시오')
```

### 내 코드

출처: `me/workspace_python/08_if.py` 68–77행 · **원본 발췌**

```python
button = int(input('번호를 입력하세요 : '))

if button == 1 :
    print('콜라')
elif button == 2 :
    print('사이다')
elif button == 3 :
    print('환타')
else :
    print('잘못 입력하셨습니다.')
```

메뉴 번호가 1·2·3이면 해당 음료 이름이 출력된다. 어느 조건에도 맞지 않으면 `else`가 실행된다. `elif`는 앞 조건이 거짓일 때 다음 조건을 검사하므로, 이 코드에서 음료를 중복 출력하지 않는다. 내 코드는 안내 문구와 잘못 입력했을 때의 메시지가 강사님과 다르지만 선택 규칙은 같다.

<a id="section-5"></a>

## 5. `match`·`case`와 한 줄 조건식

### 강사님 코드

출처: `teacher/workspace_python/_08_if.py` 65–77행 · **원본 발췌**

```python
# break 필요 없음
# 또는은 | (파이프)
a = 7
match a :
    case 6 | 7 | 8 :
        print('여름')
    case '여름2' :
        print('여름2')
    case _ :
        print('그 외')

# 표현식
print( 3 if 3 > 2 else 2 if 2 < 3 else 1  )
```

### 내 코드

출처: `me/workspace_python/08_if.py` 78–92행 · **원본 발췌**

```python

# match , case문 / break 필요 없고 default 대신 case _ : 를 씀
# ~또는(or) 는 |로 구분해서 써줘야 함
# a = '여름' 
a = 7 
match a :
    case 6 | 7 | 8 :
        print('봄')
    case '여름' :
        print('여름')
    case _ :
        print('그 외')

# 값이 3 > 2 이면 3 출력, 아니라면 2 출력
print( 3 if 3 > 2 else 2)
```

`match a`에서 `case 6 | 7 | 8`의 `|`는 **여러 패턴 중 하나**를 뜻한다. `a=7`이라 첫 번째 `case`가 실행된다. 강사님 파일은 `여름`, 내 파일은 `봄`을 출력하도록 써 두었으므로 두 코드의 **출력 문자열은 다르다**. 어느 계절이 맞는지는 이 숫자 범위만으로 결정되지 않는다. `case _`는 앞의 어느 패턴에도 맞지 않을 때 실행되는 자리다. 이 예제의 `match`에는 `break`가 필요하지 않다.

마지막 `3 if 3 > 2 else 2`는 조건이 참이므로 `3`을 돌려준다. 강사님은 뒤에 다른 조건식을 한 번 더 연결했고, 나는 한 단계만 썼다. 지금은 간단한 한 단계부터 읽고, 중첩된 식은 **앞 조건이 거짓일 때만** 뒤쪽을 평가한다고 보면 된다.

<a id="section-6"></a>

## 직접 확인할 질문

1. 빈 리스트 `[]`가 들어 있는 `if a`에서는 어느 쪽이 실행될까?
2. 점수를 세 개만 입력했을 때 `잘못된 입력`이 출력될까, 먼저 오류가 날까?
3. `a=7`일 때 두 파일의 `match`가 각각 출력하는 말은 무엇일까?

<a id="section-7"></a>

## 추가로 알면 좋은 것

입력값을 먼저 검사하고 오류 없이 다시 입력받게 하는 흐름은 이 원본에 구현되어 있지 않다. 이 장에서는 현재 코드가 **어디까지 처리하는지**를 구분해서 읽고, 더 견고한 입력 처리는 뒤의 예외 처리 학습과 연결해 보자.

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/08_Python_조건문_연습문제.md) → [09-01. for와 range](09-01_Python_for와_range.md)

