# 03. 문자열과 포매팅 — 글자를 만들고 찾아 바꾸기

[Python 목차](README.md) · [이전: 변수와 연산자](02_Python_변수와_연산자_입출력.md)

양쪽 `03_string.py`의 실제 연습 순서를 따라간다. 먼저 숫자를 문자열에 넣어 출력하고, 그 뒤 검색·분리·치환·공백 정리·자릿수 표시를 배운다. 기존 Wiki에만 있는 수많은 문자열 메서드를 필수 표로 펼치지 않는다.

## 먼저: 문자열이란 무엇인가?

문자열은 글자의 순서를 나타내는 값이다. `'32.5'`와 숫자 `32.5`는 화면에 비슷하게 보여도 **자료형이 다르다.** 숫자를 문장에 붙일 때는 문자열로 바꾸거나, 수업의 f-string처럼 값을 문장 안에 넣는다.

```python
# 수업 문법으로 만든 설명용 재구성
temperature = 32.5
print('온도: ' + str(temperature))  # 온도: 32.5
print(f'온도: {temperature}')       # 온도: 32.5
```

두 줄의 **화면 결과는 같지만 작성 방식은 다르다.** 원본을 볼 때는 어떤 방식이 같은 문장을 만드는지 확인하고, 메서드로 새 문자열을 만든 뒤 그 값을 다시 사용했는지도 따라가자.

<!-- chapter-toc -->

- [1. 값을 문자열에 넣기](03_Python_문자열과_포매팅.md#section-1)
- [2. 위치 찾기와 바꾸기](03_Python_문자열과_포매팅.md#section-2)
- [3. 합치기·나누기와 대소문자](03_Python_문자열과_포매팅.md#section-3)
- [4. 앞뒤 공백과 자릿수](03_Python_문자열과_포매팅.md#section-4)
- [직접 확인할 질문](03_Python_문자열과_포매팅.md#section-5)
- [추가로 알면 좋은 것](03_Python_문자열과_포매팅.md#section-6)

<a id="section-1"></a>

## 1. 값을 문자열에 넣기

### 강사님 코드

출처: `teacher/workspace_python/_03_string.py` 18–36행 · **원본 발췌**

```python
b = 32.5
c = "지금 온도는 "+ str(b) +"도 입니다"
print(c)

d = f"지금 온도는 {b}도 입니다"
print(d)

e = "지금 온도는 {0}도 입니다".format(b)
print(e)

f = f'''
<div>
    지금 온도는 {b}도 입니다
</div>
'''
g = '지금 온도는 %d도 입니다' % b
print(g)
h = '지금 온도는 %f도 입니다' % b
print(h)
```

### 내 코드

출처: `me/workspace_python/03_string.py` 15–40행 · **원본 발췌**

```python
# c = "지금 온도는 " + b +"도 입니다." # 이것처럼 하면 str + int + str이기에 안 됨
c = "지금 온도는 " + str(b) +"도 입니다."
print(c)

# f를 사용하면 벡틱처럼 사용할 수 있음(fomentic)
d = f"지금 온도는 {b}도 입니다."
print(d)

# 아래처럼 {index}를 사용하고 해당 자리에 format(index)이 들어가도록 사용 가능
e = "지금 온도는 {0}도 입니다".format(b)
print(e)

f = f'''
<div>
    지금 온도는 {b}도 입니다
</div>
'''
print(f)

# 정수로 값이 나옴
g = '지금 온도는 %d도 입니다' % b
print(g)

# float으로 선언 가능
h = '지금 온도는 %f도 입니다' % b
print(h)
```

숫자 `b`와 문자열을 `+`로 이어 붙이려면 먼저 `str(b)`로 바꾼다. f-string의 `{b}`는 현재 값을 글자 안에 넣고, `.format(b)`도 자리 표시자에 값을 넣는다. 오래된 `%d`, `%f` 방식도 두 원본에 있으므로 **읽을 수 있게** 다룬다. `%d`는 이 예제의 `32.5`를 정수 모양으로 표시하므로 f-string 출력과 같다고 생각하지 않는다. HTML 모양의 여러 줄 f-string `f`는 양쪽 모두 만들었지만 **강사님은 출력하지 않고, 나는 `print(f)`로 출력했다.**

<a id="section-2"></a>

## 2. 위치 찾기와 바꾸기

### 강사님 코드

출처: `teacher/workspace_python/_03_string.py` 38–54행 · **원본 발췌**

```python
i = '_hello'
print(len(i))

print( i.count('l') )
print( i.find('l') ) # indexOf
print( i.find('z') ) # 없으면 -1

print( i.index('l') )
# print( i.index('z') ) # 없으면 에러

print( i.rfind('l') ) # right 뒤에서부터 indexOf

print( i.replace('l', 'w') ) # 모두 바꿔 줌

j = '그럼 저기서 하나만 바꾸고 싶으면요?'
k = j.split()
print(k)
```

### 내 코드

출처: `me/workspace_python/03_string.py` 43–60행 · **원본 발췌**

```python
print(len(i))

# 'l' 이 몇 개인지 셀 수 있음
print( i.count('l') )
print( i.find('l') ) # find는 indexOf처럼 자리수를 볼 수 있음
print( i.find('z') ) # indexOf와 동일하게 값이 없을 때 -1 반환

print( i.index('l') )
# print( i.index('z') ) # index는 없으면 err msg가 나옴, ValueError: substring not found

print( i.rfind('l') ) # right 우측부터 indexOf

print( i.replace('l','w') ) # replace는 모두 바꿔줌

j = '그럼 저기서 하나만 바꾸고 싶으면요?'
k = j.split()
print(k)

```

`len`은 글자 수를 세고 `count`는 찾는 글자의 횟수를 센다. `find('z')`는 없을 때 `-1`을 돌려주지만, `index('z')`를 실행하면 오류가 나므로 원본에서는 주석 처리됐다. `rfind`는 오른쪽에서부터 찾되 **돌려주는 인덱스는 여전히 문자열의 왼쪽부터 센 위치**다. `replace('l','w')`는 바뀐 문자열을 돌려주며 원래 문자열 `i`를 자동 변경하지 않는다. `split()`은 여기서 공백을 기준으로 단어를 나눈다.

<a id="section-3"></a>

## 3. 합치기·나누기와 대소문자

### 강사님 코드

출처: `teacher/workspace_python/_03_string.py` 56–77행 · **원본 발췌**

```python
m = [1,2,3]
a, b, c = m

a = ['a','b','c','d','e']
b = '-'.join(a)
a = [1,2,3,4,5]
'-'.join(map(str, a))
'-'.join( str(data) for data in a )

print(b)
c = b.split('-')
print(c)

a = "Don't Look Back in Anger"
b = a.find('back')
print(b)

c = a.upper()
print(c)

d = a.upper().find('back'.upper())
print(d)
```

### 내 코드

출처: `me/workspace_python/03_string.py` 61–81행 · **원본 발췌**

```python
m = [1,2,3]
a,b,c = m

a = ['a','b','c','d','e']
b = '-'.join(a) # b = '-'.join(map(str, a))
'-'.join( str(data) for data in a )

print(b)
c = b.split('-')
print(c)

# 대소문자 구분 없이 검색할 때 upper,lower를 주로 사용 함
a = "Don't Look Back is Anger"
b = a.find('back')
print(b)

c = a.upper()
print(c)

d = a.upper().find('back'.upper())
print(d)
```

문자열 배열 `['a','b','c','d','e']`는 `'-'.join(a)`로 `a-b-c-d-e`가 된다. 그 결과에 `.split('-')`를 쓰면 다시 문자열 배열이 된다. 숫자 배열은 그대로 `join`할 수 없어 두 원본 모두 숫자를 문자열로 바꾼 뒤 합치는 **짧은 예시 표현식**을 넣었다. 이 표현식 결과는 변수에 저장하거나 출력하지 않으므로 화면에는 추가 결과가 보이지 않는다. `map`이나 제너레이터의 상세 구현을 이 장의 선행 학습으로 요구하지 않는다.

`a.find('back')`은 대문자 `Back`을 그대로 찾지 못한다. 양쪽을 `upper()`로 맞춘 뒤 찾으면 위치를 얻을 수 있다. **원본 문자열을 바꾸는 것이 아니라** 새 문자열을 만들어 비교하는 흐름이다.

<a id="section-4"></a>

## 4. 앞뒤 공백과 자릿수

### 강사님 코드

출처: `teacher/workspace_python/_03_string.py` 79–95행 · **원본 발췌**

```python
a = '  a b  '
print(a.strip())

print( '35'.zfill(4) )
print( '35000'.zfill(4) )

a = 7
print( f'{a:03}' )
print( f'{a:3}' )
print( f'..{a:<3}..' )
print( f'..{a:^10}..' )

a = 3.14
print( f'{a:08.3f}' )

a = 15000
print( f'{a:,}' )
```

### 내 코드

출처: `me/workspace_python/03_string.py` 83–104행 · **원본 발췌**

```python
# strip을 사용하면 양 쪽 공백을 제거해 줌
a = '   a b   '
print(a.strip())
print(a.strip().replace(' ',''))

# zfill을 사용하면 앞에 '0'을 추가할 수 있음
# 모자르면 채워주고, 자리수가 넘으면 그대로 둠
print('35'.zfill(4))
print('35000'.zfill(4))

a = 7
print( f'{a:03}' ) # 007
print( f'..{a:3}..' ) # ..  7.. [3자리로 만들어줌]
print( f'..{a:<3}..' ) # ..7  .. [좌측에 정렬]
print( f'..{a:>3}..' ) # ..  7.. [우측에 정렬]
print( f'..{a:^10}..' ) # ..    7     .. [가운데 정렬]

a = 3.14
print( f'{a:08.3f}' ) # 0003.140

a = 15000
print( f'{a:,}' ) # 15,000 [3자리마다 , 찍어줌]
```

`strip()`은 양끝 공백을 없애고, 내 코드는 이어 `replace(' ','')`로 중간 공백도 지워 본다. `zfill(4)`는 글자 길이가 4보다 짧을 때 왼쪽을 `0`으로 채운다. 이미 긴 `'35000'`은 줄이지 않는다. f-string의 폭·정렬 지정은 출력 모양을 맞추는 연습이다. `f'{a:08.3f}'`는 실수를 소수 셋째 자리까지 표시하고, `f'{a:,}'`는 큰 정수에 쉼표를 넣는다.

<a id="section-5"></a>

## 직접 확인할 질문

1. `find`와 `index`는 찾는 글자가 없을 때 어떻게 다를까?
2. 숫자 배열을 `join`하기 전에 값을 왜 문자열로 바꿔야 할까?
3. `'  a b  '.strip()`과 그 결과에 `.replace(' ','')`를 쓴 값은 무엇일까?

<a id="section-6"></a>

## 추가로 알면 좋은 것

기존 Wiki에만 있는 `casefold` 등 이 원본에 없는 메서드는 필요할 때 찾아보는 참고 내용으로 둔다. 기본 복습은 이 파일의 `find`·`split`·`join`·`strip`·포매팅부터 확인한다.

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/03_Python_문자열과_포매팅_연습문제.md) → [다음: 리스트](04_Python_리스트와_데이터처리.md)

