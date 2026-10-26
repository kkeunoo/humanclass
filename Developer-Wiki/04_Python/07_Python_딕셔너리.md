# 07. 딕셔너리 — 이름표로 값을 찾기

[Python 목차](README.md) · [이전: 시퀀스](06_Python_시퀀스와_슬라이싱.md)

두 원본 `07_dict.py`는 **키(key)와 값(value)**을 묶어 저장하고, 조회·수정·삭제·순회하는 연습이다. 리스트의 위치 번호 대신 `'이름'`, `'스킬'` 같은 키로 값을 찾는다는 점부터 읽자. 여기서는 강사님 예시의 중복 키와 내 주석의 부정확한 설명도 실행 결과와 나란히 확인한다.

<!-- chapter-toc -->

- [1. 만들기와 중복 키](#section-1)
- [2. `[]`와 `get()`으로 값 찾기](#section-2)
- [3. 값 바꾸기, 새 키 넣기, 포함 여부](#section-3)
- [4. 키·값·쌍 보기](#section-4)
- [5. 여러 항목 수정하고 삭제하기](#section-5)
- [6. 키 목록으로 만들고 순회하기](#section-6)
- [직접 확인할 질문](#section-7)
- [추가로 알면 좋은 것](#section-8)

<a id="section-1"></a>

## 1. 만들기와 중복 키

### 강사님 코드

출처: `teacher/workspace_python/_07_dict.py` 3–20행 · **원본 발췌**

```python
a = {}
a = dict()
print( type(a) )

b = {
    '이름': '호랑이심장',
    '직업': '마법사',
    '직업': '마법사2',
    '스킬': {
        '공격': '고백',
        '방어': '철벽남',
        'javascript': '상'
    }
}
print(b)

c = dict(a=10, b=20)
print(c)
```

### 내 코드

출처: `me/workspace_python/07_dict.py` 3–22행 · **원본 발췌**

```python
a = {}
a = dict()
print(type(a))

b = {
    # key는 javascript와 다르게 ''를 써줘야 함 (웬만해선 str)
    # 중복된 key값이 2개일 경우, 뒤에 오는 value를 가져옴
    '이름': '홍길동',
    '직업': '도적',
    '스킬': {
        '공격': '훔치기',
        '방어': '도망가기',
        'javascript': '중'
    }
}

print(b)

c = dict(a=10, b=20)
print(c)
```

`{}`와 `dict()`는 모두 빈 딕셔너리를 만든다. 위 강사님 코드에서 `'직업'`을 두 번 적으면 뒤의 `'마법사2'`가 남는다. 내 코드에는 중복 키가 없지만, 주석으로 같은 규칙을 기억해 두었다. `dict(a=10, b=20)`의 결과는 `{'a': 10, 'b': 20}`이다.

내 주석의 “키는 JavaScript와 다르게 따옴표를 써야 한다”는 **문자열 키를 딕셔너리 리터럴로 직접 쓸 때**에 해당한다. 모든 키가 문자열이어야 한다는 뜻은 아니다. 이 장의 핵심은 **같은 키가 한 딕셔너리에 두 번 남지 않는다**는 것이다.

<a id="section-2"></a>

## 2. `[]`와 `get()`으로 값 찾기

### 강사님 코드

출처: `teacher/workspace_python/_07_dict.py` 22–37행 · **원본 발췌**

```python
# b.이름
print( b['이름'] )
# print( b['이름2'] )

print( b.get('이름') )
print( b.get('이름2') ) # 없으면 None
print( b.get('이름2', '이름없음') ) # 없으면 두번째 값으로 대체

d = b['스킬']
d['공격']
b['스킬']['공격']
print(b['스킬']['공격'])

print( b.get('스킬').get('공격') )

print( b.get('스킬2', {}).get('공격', 0) )
```

### 내 코드

출처: `me/workspace_python/07_dict.py` 24–39행 · **원본 발췌**

```python
# b.이름
print( b['이름'] )
# print( b['이름2'] ) # 없는 key일 경우 KeyError: '이름2'

print( b.get('이름') )
print( b.get('이름2') ) # get으로 받을 경우 'None'이 나옴, 더 안전한 방법
print( b.get('이름2', '이름없음') ) # 있으면 그 값이 나오고, 없을 경우 두 번째 인자값이 나옴

d = b['스킬']
d['공격']
b['스킬']['공격']
print( b['스킬']['공격'] )

print( b.get('스킬').get('공격') )
# print( b.get('스킬2').get('공격') ) # AttributeError: 'NoneType' object has no attribute 'get'
print( b.get('스킬2', {}).get('공격', 0) ) # 스킬2라는 key가 없어도 에러가 나지 않도록 빈 dict 생성
```

`b['이름']`과 `b.get('이름')`은 여기서 같은 값을 읽는다. 없는 키를 `b['이름2']`로 읽으면 `KeyError`가 나므로 양쪽 파일 모두 그 줄을 주석 처리했다. `b.get('이름2')`는 `None`, `b.get('이름2', '이름없음')`은 지정한 기본값 `'이름없음'`을 돌려준다.

중첩 딕셔너리는 `b['스킬']['공격']`처럼 단계별로 읽는다. 내 파일의 주석처럼 `b.get('스킬2').get('공격')`은 첫 조회에서 `None`을 받은 뒤 `.get`을 호출하므로 오류가 난다. 강사님과 내 코드가 사용한 `b.get('스킬2', {}).get('공격', 0)`은 **첫 키가 없을 때 빈 딕셔너리**에서 다시 조회해 `0`을 받는다. 실제 데이터에서 값이 `None`일 수도 있으므로 “`get`이면 항상 안전하다”로 외우지는 말자.

<a id="section-3"></a>

## 3. 값 바꾸기, 새 키 넣기, 포함 여부

### 강사님 코드

출처: `teacher/workspace_python/_07_dict.py` 39–50행 · **원본 발췌**

```python
b['직업'] = '도적'
print( b )

b['직업2'] = '도적2' # 없으면 key 만들어 줌
print( b )

print( '스킬' in b )
print( '공격' in b  )
print( '공격' in b['스킬'] )
print( '공격' not in b['스킬'] )

print( len(b) ) # key의 개수
```

### 내 코드

출처: `me/workspace_python/07_dict.py` 41–52행 · **원본 발췌**

```python
b['직업'] = '전사' # dict key에 value 할당하기
print( b )

b['직업2'] = '전사2' # 가지고 올 때만 없으면 안 되는 것이고, 없으면 추가함
print( b )

print( '스킬' in b ) # True
print( '공격' in b['스킬']) # True
print( '공격' not in b['스킬']) # False
print( '공격' in b.get('스킬')) # True

print( len(b) ) # key의 개수를 알 수 있음
```

기존 키 `b['직업']`에 대입하면 값이 바뀌고, 없던 키 `b['직업2']`에 대입하면 새 항목이 생긴다. `'스킬' in b`는 바깥 딕셔너리의 **키**를 검사한다. `'공격' in b['스킬']`은 안쪽 딕셔너리의 키를 검사한다. 따라서 강사님 코드의 `'공격' in b`는 거짓이지만 `'공격' in b['스킬']`은 참이다. `len(b)`는 이 시점의 바깥 키 수인 **4**다.

내 코드의 `b.get('스킬')`은 실제로 딕셔너리를 돌려주므로 `'공격' in b.get('스킬')`도 실행된다. 그러나 존재하지 않는 키를 `get`으로 조회한 결과에 곧바로 `in`을 쓰는 예로 일반화하면 안 된다.

<a id="section-4"></a>

## 4. 키·값·쌍 보기

### 강사님 코드

출처: `teacher/workspace_python/_07_dict.py` 52–66행 · **원본 발췌**

```python
e = b.keys()
print( e )
f = b.values()
print( f )
print( list(f)[0] )

g = b.items()
print( g )

a = 'hello'
print( list(a) )
print( set(a) ) # {'h', 'e', 'o', 'l'}
# set
#   중복을 제거해서 관리한다
#   순서는 보장하지 않는다
```

### 내 코드

출처: `me/workspace_python/07_dict.py` 54–70행 · **원본 발췌**

```python
e = b.keys() # dict_keys(['이름', '직업', '스킬', '직업2']), 유사배열로 나옴 (list형변환 해서 사용)
print( e )

f = b.values() # dict_values(['홍길동', '전사', {'공격': '훔치기', '방어': '도망가기', 'javascript': '중'}, '전사2'])
print( f )
# print( f[0] ) # 배열이 아니기 때문에 못 씀
print( list(f)[0] ) 

g = b.items() # key,value를 tuple로 저장해줌
print( g )

# b['스킬']['버프'] = '힐'
# print(b)

a = 'hello'
print( list(a) ) # ['h', 'e', 'l', 'l', 'o']
print( set(a) ) # {'o', 'e', 'l', 'h'} , 중복은 제거하지만 순서는 중요하지 않음 (jason key값이 set으로 관리되기 때문에 중복 없음)
```

`keys()`는 키, `values()`는 값, `items()`는 `(키, 값)` 쌍을 보여 준다. 내 코드의 `f[0]`은 주석 처리되어 있다. `dict_values` 결과를 바로 정수 인덱스로 읽을 수 없어 `list(f)[0]`으로 바꾼 것이다. 이 장의 결과를 읽는 데 내부 구현을 외울 필요는 없다.

양쪽 파일의 `set('hello')`는 **중복 글자를 제거**한다. 표시 순서는 고정된 출력 예시로 외우지 않는다. 내 주석에 있는 “JSON 키가 set으로 관리되기 때문”이라는 설명은 이 예제의 근거가 아니다. 여기서는 문자열을 `list`와 `set`으로 각각 바꿔 결과의 중복 여부만 비교하면 된다.

<a id="section-5"></a>

## 5. 여러 항목 수정하고 삭제하기

### 강사님 코드

출처: `teacher/workspace_python/_07_dict.py` 69–91행 · **원본 발췌**

```python
b = {
    '이름': '호랑이심장',
    '직업': '마법사',
    '직업': '마법사2',
    '스킬': {
        '공격': '고백',
        '방어': '철벽남',
        'javascript': '상'
    }
}
b.update(이름='타이거', 직업='강사')
b.update(이름='타이거', 직업='강사', 나이=20)
print(b)
c = b.pop('나이')
print(b)
print(c)
# c = b.pop('나이') # 없으면 에러
c = b.pop('나이', 0) # 없으면 두번째 값을 사용
print(c)
# c = b.pop() # 전달인자 필수
c = b.popitem()
print(c)
print(b)
```

### 내 코드

출처: `me/workspace_python/07_dict.py` 72–96행 · **원본 발췌**

```python
b = {
    '이름': '홍길동',
    '직업': '도적',
    '스킬': {
        '공격': '훔치기',
        '방어': '도망가기',
        'javascript': '중'
    }
}
# update(키='값') 으로 바로 변경할 수 있고, 없으면 만들어 넣어 줌
b.update(이름='타이거', 직업='호랑이')
b.update(이름='타이거', 직업='호랑이', 나이='30')
print(b)

# pop을 사용하면 key는 없애고 해당 index에 있던 value를 반환받음
c = b.pop('나이') 
print(b)
print(c)
# c = b.pop('나이') # 없으면 에러 발생 KeyError: '나이'
c = b.pop('나이', 0) #  없으면 두 번째 값을 사용
print(c)
# c = b.pop() # TypeError: pop expected at least 1 argument, got 0 , 적어도 1개의 전달인자 필요
c = b.popitem() # popitem으로 임의의 키-값 쌍으로 삭제할 수 있음
print(c)
print(b)
```

`update()`는 전달된 키의 값을 바꾸거나 새 키를 추가한다. 강사님은 `나이=20`, 나는 `나이='30'`을 넣었다. 같은 키라도 **강사님 값은 정수, 내 값은 문자열**이다. `pop('나이')`는 키를 삭제하고 기존 값을 돌려준다. 다시 지운 키를 `pop('나이', 0)`으로 읽으면 오류 대신 기본값 `0`을 받는다.

내 주석은 `pop`의 반환값을 “해당 index에 있던 value”라고 썼지만, 딕셔너리는 이 코드에서 **키**로 찾는다. `popitem()`도 값을 하나 지우고 `(키, 값)` 쌍을 돌려준다. 내 주석의 “임의의 키-값 쌍”은 현대 Python의 동작을 설명하기에 부정확하다. 이 코드에서는 **마지막으로 추가된 항목**을 지운다. 두 파일 모두 그 결과를 출력한다.

<a id="section-6"></a>

## 6. 키 목록으로 만들고 순회하기

### 강사님 코드

출처: `teacher/workspace_python/_07_dict.py` 93–113행 · **원본 발췌**

```python
a = ['a', 'b', 'c']
b = {
    'a':0,
    'b':0,
    'c':0
}
b = {}
b.clear()
b[a[0]] = 0
b[a[1]] = 0

c = dict.fromkeys(a)
print(c)

# key만 나온다
for i in c :
    print(i)
    print(c[i])

for k, v in c.items() :
    print(k, v)
```

### 내 코드

출처: `me/workspace_python/07_dict.py` 98–116행 · **원본 발췌**

```python
a = ['a', 'b', 'c']
b = {
    'a' : 0, 
    'b' : 0, 
    'c' : 0, 
}
b = {}
b[a[0]] = 0
b[a[1]] = 0

c = dict.fromkeys(a)
print(c)

for i in c : 
    print(i)
    print(c[i])

for key, value in c.items() :
    print(key, value)
```

`dict.fromkeys(['a','b','c'])`는 각 키의 값을 `None`으로 둔 새 딕셔너리를 만든다. `for i in c`는 **키**를 차례대로 돌고, `c[i]`로 그 키의 값을 찾는다. `for key, value in c.items()`는 한 쌍을 바로 나누어 받는다. 내 파일은 `b = {}`로 앞의 딕셔너리를 다시 지정하므로 그 아래에서 실제로 들어간 것은 `'a'`와 `'b'` 두 키다. 강사님 파일에는 `b.clear()`가 있는데, 바로 앞에서 새 빈 딕셔너리로 다시 지정한 상태이므로 지울 항목은 없다.

강사님은 같은 파일 끝에 `numbers`·장바구니·로그인·투표 등의 **문제 문구**와 `users.items()`를 `enumerate`로 출력하는 짧은 예시를 남겼다. 내 대응 파일에는 이 문제의 풀이가 없다. 따라서 이 장에서는 문제를 완성한 기능으로 소개하지 않는다. `enumerate`를 써서 순서와 항목을 함께 읽는 법은 [리스트 참조·순회](04-02_Python_리스트참조와_컴프리헨션.md)에서 이미 다뤘다.

<a id="section-7"></a>

## 직접 확인할 질문

1. 없는 키를 `[]`와 `get()`으로 읽으면 각각 어떻게 될까?
2. `'공격' in b`와 `'공격' in b['스킬']`이 다른 이유는?
3. 강사님 `나이=20`과 내 `나이='30'`은 출력할 때 왜 비슷해 보여도 다른 자료형일까?

<a id="section-8"></a>

## 추가로 알면 좋은 것

키로 쓸 수 있는 자료형의 자세한 규칙, 딕셔너리의 내부 저장 방식, 복잡한 중첩 데이터 검증은 이 파일에서 다룬 범위를 넘어간다. 우선 이 장의 **키 조회 → 값 수정 → 키·값 순회**가 각 원본에서 어떤 결과를 내는지 확인하자.

