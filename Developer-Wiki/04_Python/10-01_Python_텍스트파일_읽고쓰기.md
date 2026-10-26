# 10-01. 텍스트 파일 읽고 쓰기

[Python 목차](README.md) · [이전: 반복 제어](09-02_Python_while과_반복제어.md) · [다음: `pickle`](10-02_Python_pickle과_자료형저장.md)

두 원본 `10_file.py`는 `open`으로 텍스트를 쓰고 읽은 뒤, `with`로 파일을 닫는 방법을 배운다. 실행하면 **현재 작업 폴더**에 파일이 생기거나 기존 파일이 바뀔 수 있으므로, 여기의 원본 발췌는 결과를 이해하는 자료로 읽자.

<!-- chapter-toc -->

- [1. `w`, `r`과 인코딩](#section-1)
- [2. 일부만 읽고, 나눠 읽기](#section-2)
- [3. 바이너리 모드와 `with`](#section-3)
- [4. 뒤에 덧붙이기](#section-4)
- [직접 확인할 질문](#section-5)
- [추가로 알면 좋은 것](#section-6)

<a id="section-1"></a>

## 1. `w`, `r`과 인코딩

### 강사님 코드

출처: `teacher/workspace_python/_10_file.py` 1–24행 · **원본 발췌**

```python
# w : 수정 가능
file = open('hello.txt', 'w')
file.write('eng\n123\n한글')
file.flush() # 버퍼가 꽉 차지 않아도 내보내기
             # 즉시 반영
file.close()


# 한글 캐릭터셋
# utf-8, euc-kr, cp949
file = open('hello2.txt', 'w', encoding='utf-8')
file.write('eng\n123\n한글')
file.close()

# r : 읽기 전용
file = open('hello.txt', 'r')
s = file.read()
file.close()
print(s)

file = open('hello2.txt', 'r', encoding='utf-8')
s = file.read()
file.close()
print(s)
```

### 내 코드

출처: `me/workspace_python/10_file.py` 1–24행 · **원본 발췌**

```python
# w : 수정 가능
file = open('hello.txt', 'w') # 파일이 없으면 만들고, 있다면 그 파일을 엶
file.write('eng\n123\n한글') # write로 쓸 내용 작성
file.flush() # flush는 버퍼가 꽉 차지 않아도 내보내기 (즉시 반영)
file.close()

# 한글 charset 
# 1. utf-8 , 2. euc-kr , 3. cp949
file = open('hello2.txt', 'w', encoding='utf-8') # encoding으로 utf-8등 지정해놓을 수 있음
file.write('eng\n123\n한글') 
file.close()

# r : 읽기 전용(readonly)
file = open('hello.txt', 'r') 
s = file.read()
file.close()
print(s)

# UnicodeDecodeError: 'cp949' codec can't decode byte 0xed in position 10: illegal multibyte sequence
# 윈도우용 한글 인코딩 에러가 발생하기 때문에 읽을때도 encoding 필요
file = open('hello2.txt', 'r', encoding='utf-8') # 기본적으로 euc-kr로 읽기 때문에 에러
s = file.read()
file.close()
print(s)
```

`'w'`는 파일을 쓰기 모드로 열고, 파일이 이미 있으면 **기존 내용을 비우고 새로 쓴다**. `write('eng\n123\n한글')`의 `\n`은 줄바꿈이다. `flush()`는 아직 버퍼에 남은 내용을 내보내고, `close()`는 파일을 닫는다. `'r'`은 읽기 모드이고 `read()`는 남은 텍스트를 읽는다. 강사님은 `hello2.txt`에 쓰고 읽을 때 모두 `encoding='utf-8'`을 지정했다.

내 메모의 “기본적으로 euc-kr로 읽는다”는 설명은 일반 규칙이 아니다. **인코딩을 생략했을 때의 기본값은 실행 환경에 따라 달라진다.** 읽기와 쓰기의 인코딩이 다르면 한글이 깨지거나 디코딩 오류가 날 수 있으므로, 한글 텍스트에서는 같은 인코딩을 명시해 두는 편이 분명하다. 주석에 적힌 `UnicodeDecodeError`는 이 코드가 실행될 때 항상 발생하는 결과가 아니다.

<a id="section-2"></a>

## 2. 일부만 읽고, 나눠 읽기

### 강사님 코드

출처: `teacher/workspace_python/_10_file.py` 26–48행 · **원본 발췌**

```python
print('-'*20)
file = open('hello.txt', 'r')
# s = file.read(6)
s = file.read(10)
file.close()
print(s)

print('-'*20)
file = open('hello.txt', 'r', buffering=1)
s = file.read()
file.close()
print(s)

text = ''
file = open('hello.txt', 'r')
while True :
    chunk = file.read(2)
    if not chunk :
        break
    text += chunk
    print(chunk)
file.close()
print(text)
```

### 내 코드

출처: `me/workspace_python/10_file.py` 26–55행 · **원본 발췌**

```python
print('-'*20)
file = open('hello.txt', 'r') 
s = file.read(10) # 2Byte만 읽도록 인자값을 줄 수 있음
file.close()
print(s)

print('-'*20)
file = open('hello.txt', 'r', buffering=1) 
s = file.read()
file.close()
print(s)

print('-'*20)
text = ''
file = open('hello.txt', 'r') 
while True :
    chunk = file.read(2)
    if not chunk : 
        break
    text += chunk
    print(chunk)
file.close()    
print(text)
# 결과물
# en
# g

# 12
# 3

```

**텍스트 모드**의 `read(10)`은 여기서 최대 **문자 10개**를 읽는다. 내 주석의 “2Byte만”이라는 설명은 인자 `10`과도 맞지 않고, 텍스트 읽기의 단위를 설명하지도 못한다. `read(2)`를 반복하면 파일 끝에서 빈 문자열 `''`을 받으므로 `if not chunk: break`로 멈춘다. 내 주석의 출력 예시는 읽는 단위와 줄바꿈 위치가 섞여 보여 실제로 한 줄씩 읽는다고 오해하기 쉽다. 이 코드는 **한 번에 문자 두 개씩** 읽는다.

`buffering=1`도 원본에 등장한다. 버퍼링 설정을 암기하기보다, 이 코드의 `read()` 결과는 일반 읽기와 같은 텍스트라는 점에 집중하자.

<a id="section-3"></a>

## 3. 바이너리 모드와 `with`

### 강사님 코드

출처: `teacher/workspace_python/_10_file.py` 52–76행 · **원본 발췌**

```python
file = open('a.webp', 'rb')
s = file.read()
file.close()
print(s)

file = open('hello.txt', 'r')
s = file.read()
file.close()
print(s)

with open('hello.txt', 'r') as file :
    s = file.read()
    print(s)

a = [1,2,3,4]
with open('array1.txt', 'w') as file :
    # file.write(str(file))
    file.write(str(a))
print(str(a))

with open('array1.txt', 'r') as file :
    b = file.read()
    print( type(b), b )
    c = list(b)
    print( type(c), c )
```

### 내 코드

출처: `me/workspace_python/10_file.py` 57–84행 · **원본 발췌**

```python

# file = open('a.webp', 'rb') #binary 는 2진수를 뜻 함
# s = file.read()
# file.close()
# print(s)

file = open('hello.txt', 'r') 
s = file.read()
file.close()
print(s)

# with를 쓰면 close를 없앨 수 있음, 끝나면 알아서 종료 됨
with open('hello.txt', 'r') as file :
    s = file.read()
    print(s)

a = [1,2,3,4]

with open('array1.txt', 'w') as file :
    # file.write(str(file))
    file.write(str(a))
print(str(a))

with open('array1.txt', 'r') as file :
    b = file.read()
    print( type(b) , b)
    c = list(b)
    print( type(c) , c) # 리스트로 바꿔 저장하면 '[', '1', ',' 처럼 한개씩 쪼개어 저장됨
```

`'rb'`는 바이너리 읽기 모드다. 강사님 코드는 `a.webp`를 열지만, 제공된 해당 폴더에는 그 파일이 없어서 **파일 전체를 그대로 실행하면 여기서 멈출 수 있다**. 내 대응 줄은 주석 처리되어 있다. 이미지 파일 내용을 텍스트처럼 해석하는 예제가 아니라, **바이트로 읽는 모드**를 보여 주는 예다.

`with open(...) as file:` 블록이 끝나면 파일이 닫힌다. `array1.txt`에는 리스트 `a`를 `str(a)`로 바꾼 **문자열**을 썼다. 다시 읽은 `b`는 리스트가 아닌 문자열이고 `list(b)`는 `'['`, `'1'`, `','`처럼 **문자 한 개씩** 담은 리스트가 된다. 리스트 `[1,2,3,4]` 자체가 복원되는 것은 아니다.

<a id="section-4"></a>

## 4. 뒤에 덧붙이기

### 강사님 코드

출처: `teacher/workspace_python/_10_file.py` 117–125행 · **원본 발췌**

```python
# a 이어 쓰기
with open('hello.txt', 'a') as f :
    f.write('123')
    # f.read()

# +
# 쓰기 계열에 붙어있으면 읽기 가능해짐
# 읽기 계열에 붙어있으면 쓰기 가능해짐

```

### 내 코드

출처: `me/workspace_python/10_file.py` 123–128행 · **원본 발췌**

```python
with open('hello.txt', 'a') as f : # 'a'는 이어 쓰기(append)
    f.write('123')
    # f.read() # io.UnsupportedOperation: not readable / 읽을 수 없다는 에러 발생

# + 가 쓰기 계열에 붙어있으면, 읽기 가능해짐
# + 가 읽기 계열에 붙어있으면, 쓰기 가능해짐
```

`'a'`는 파일 끝에 새 내용을 덧붙인다. 여기서는 `hello.txt` 끝에 `'123'`을 쓰며, 다시 실행하면 같은 글자가 또 붙는다. 두 원본 모두 `'a'` 모드에서 `read()`는 주석으로 막았다. `+`를 붙인 읽기·쓰기 모드는 주석으로 개념만 적혀 있고 **실제 실행 예시는 없다**. 자세한 포인터 위치와 모드 조합은 이 장의 본문 학습 범위로 확대하지 않는다.

<a id="section-5"></a>

## 직접 확인할 질문

1. `w` 모드로 기존 파일을 다시 열면 그 안의 내용은 어떻게 될까?
2. `read(10)`은 왜 여기서 10바이트가 아닌 10문자일까?
3. `list(file.read())`가 원래 리스트를 복원하지 못하는 이유는?

<a id="section-6"></a>

## 추가로 알면 좋은 것

여러 운영체제에서 한글 파일을 공유할 때 인코딩과 줄바꿈을 일관되게 관리하는 방법은 이 원본 밖의 확장이다. 우선 `w`·`r`·`a`의 차이와 `with` 블록을 정확히 읽자.

