# Python 파일 입출력

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `10_Python_파일입출력.md` |
| 분류 | `04_Python` |
| 권장 선수 학습 | `02_Python_변수와_자료형_연산자.md`, `03_Python_문자열.md`, `04_Python_리스트와_컴프리헨션.md`, `07_Python_딕셔너리와_집합.md`, `09_Python_반복문.md` |
| 다음 학습 | `11_Python_함수.md` |
| 원본 기준 | `workspace_python/10_file.py`, `workspace_teacher/workspace_python/_10_file.py` |
| 핵심 범위 | `open()`, 파일 모드, `read()`, `write()`, `flush()`, `close()`, `with`, 문자 인코딩, 바이너리 파일, `pickle`, 이어 쓰기, 텍스트 분석 |
| 보충 범위 | 파일 객체, 버퍼링, 파일 포인터, `read(size)`, 안전한 파일 관리, 직렬화 주의사항, 경로 처리, 예외 처리 |
| Quiz 처리 | 원본 실습은 본문에서 분석하며, 추가 문제와 상세 풀이 문서는 최종 Quiz 단계에서 별도 제작 |

> 이 문서는 내 코드의 `10_file.py`와 강사님 코드의 `_10_file.py`를 직접 비교해 작성했습니다. 두 파일은 텍스트 파일 생성과 읽기, UTF-8 인코딩, 일정 크기씩 읽기, `with` 문, 리스트 문자열 저장, `pickle`, 이어 쓰기, 단어 검색 실습까지 같은 흐름을 공유합니다. 내 코드는 단어 검색을 `in`, `lower()`, `replace()`로 간결하게 정리했고, 강사님 코드는 `split()`, `find()`, `count()`, `in` 등 여러 접근 방식을 비교해 보여 줍니다.

---

# 학습 목표

- 파일 입출력이 메모리 밖의 데이터를 저장하고 다시 읽는 작업임을 설명할 수 있다.
- `open()`의 기본 구조와 파일 모드를 구분할 수 있다.
- `w`, `r`, `a`, `b`, `+`의 의미를 이해한다.
- 파일을 열고 사용한 뒤 반드시 닫아야 하는 이유를 설명할 수 있다.
- `with open(...) as ...` 문을 이용해 파일을 안전하게 관리할 수 있다.
- `write()`와 `read()`의 역할을 구분할 수 있다.
- `read(size)`가 문자 수를 기준으로 데이터를 읽는다는 점을 이해한다.
- UTF-8, CP949 등 문자 인코딩이 필요한 이유를 설명할 수 있다.
- 텍스트 모드와 바이너리 모드의 차이를 구분할 수 있다.
- `pickle.dump()`와 `pickle.load()`를 이용해 Python 객체를 저장하고 복원할 수 있다.
- 직렬화된 객체는 저장 순서대로 읽어야 함을 이해한다.
- 파일 끝까지 읽은 뒤 다시 `load()`하면 `EOFError`가 발생할 수 있음을 안다.
- 문자열로 저장된 리스트와 실제 리스트 객체가 다르다는 점을 설명할 수 있다.
- 반복문과 문자열 메서드를 결합해 파일 내용을 분석할 수 있다.
- 내 코드와 강사님 코드의 접근 방식 차이를 비교할 수 있다.
- 파일 경로, 인코딩, 모드 오류 등 자주 발생하는 문제를 해결할 수 있다.

---


# 1. 원본 코드

## 1.1 내 코드

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

# 한글

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

import pickle

name = 'eng'
age = 20
address = '한글'
arr = [1,2,3,4]
scores = {
    'k' : 1,
    'k2' : 'val'
}

# dump 함수에는 'wirte'가 내재되어있음
# 실무에서는 dump 1개만 사용함, 여러개로 하면 그 줄을 계속 넘어가야 하기 때문에
with open('pickle.p', 'wb') as f :
    pickle.dump(name, f)
    pickle.dump(age, f)
    pickle.dump(address, f)
    pickle.dump(arr, f)
    pickle.dump(scores, f)

with open('pickle.p', 'rb') as f :
    p1 = pickle.load(f)
    print(p1)
    p2 = pickle.load(f) # 저장 한 'int' 형태가 그대로 돌아옴
    print(p2, type(p2))
    p2 = pickle.load(f) 
    print(p2, type(p2))
    p2 = pickle.load(f) 
    print(p2, type(p2))
    p2 = pickle.load(f) 
    print(p2['k'], type(p2))
    # p2 = pickle.load(f) # EOFError: Ran out of input , 파일을 다 읽었는데 지나갈 때 End of File Error 출력
    # print(p2, type(p2))

    # dump 한 만큼만 꺼낼 수 있다
    # import joblib 는 pickle보다 더 대용량 처리 할 때 사용

with open('hello.txt', 'a') as f : # 'a'는 이어 쓰기(append)
    f.write('123')
    # f.read() # io.UnsupportedOperation: not readable / 읽을 수 없다는 에러 발생

# + 가 쓰기 계열에 붙어있으면, 읽기 가능해짐
# + 가 읽기 계열에 붙어있으면, 쓰기 가능해짐

# with open('word.txt', 'r') as file :
#     b = str(file.read().split(' ')).replace(',', '')
#     print(b)
#     for value in b :
#         if b.get('c') :
#             value += b
#             print(value,end='')

print('-'*30)
# 단어 중 대소문자 구분없이 c를 포함하는 단어를 출력하시오. 단 , . 은 출력하지 마시오
with open('word.txt', 'r') as file :
    # vf_파일 read하며 반복문에 넣어 바로 대소문자 검사 및 strip으로 ',' '.' 제거 후 출력
    for word in file.read().split(' ') :
        if 'c' in word.lower() :
            print(word.replace(',','').replace('.',''), end=' ')
print()

    # words = file.read().split(' ')
    # word.txt를 읽어오며 공백으로 split하여 words에 저장
    # print(words, type(words)) 

    # v1_range(len(words)) 는 그냥 'words'와 같기에 다음방법
    # print(words[0])
    # for i in range(len(words)) :
    #     if words[i].find('c') != -1 : 
    #         print(words[i].replace(',', ''))

    # v2_words 안에서 검사하되 출력 시 ,과 . replace 진행 + 대소문자 구분위해 lower() 사용
    # for word in words :
    #     if word.lower().find('c') != -1 : # find도 -1반환으로 알 수 있지만 문제풀었던 것 처럼 in 사용
    #         print(word.replace(',','').replace('.',''))

    # v3_words 안에 담긴 ,과 .를 미리 제거한 후 'c' 유효 검사
    # for word in words :
    #     word = word.replace(',','').replace('.','')
    #     if 'c' in word.lower() : # 대소문자 구분위해 lower() 사용
    #         print(word,end=' ')
print('-'*30)

# print('\n','-'*30)
# with open('test.txt', 'w+', encoding='utf-8') as f :
#     a = f.read().split('\n')
#     print(a)

    # f.write('test')
    # b = f.read().split()
    # print(b) 

# a = 7,8,9
# with open('test.txt', 'r+') as f :
#     print(f.read())

#     f.write(str(list(a)))
#     print(f.read())

# a = [1,2,3,4,5]
# print(a)
# print(b)
```

## 1.2 강사님 코드

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

import pickle

name = 'eng'
age = 20
address = '한글'
arr = [1,2,3,4]
score = {
    'k': 1,
    'k2': 'val'
}

with open('pickle.p', 'wb') as f :
    pickle.dump(name, f)
    pickle.dump(age, f)
    pickle.dump(address, f)
    pickle.dump(arr, f)
    pickle.dump(score, f)

with open('pickle.p', 'rb') as f :
    # dump 순서대로 꺼낸다
    p1 = pickle.load(f)
    print(p1)
    p2 = pickle.load(f)
    print(p2, type(p2))
    p2 = pickle.load(f)
    print(p2, type(p2))
    p2 = pickle.load(f)
    print(p2, type(p2))
    p2 = pickle.load(f)
    print(p2, type(p2))
    print(p2['k'])

    # dump한 만큼만 꺼낼 수 있다
    # p2 = pickle.load(f)
    # print(p2, type(p2))

# pickle 보다 대용량에 특화된 라이브러리
# import joblib

# a 이어 쓰기
with open('hello.txt', 'a') as f :
    f.write('123')
    # f.read()

# +
# 쓰기 계열에 붙어있으면 읽기 가능해짐
# 읽기 계열에 붙어있으면 쓰기 가능해짐

# a = 'abc def'

# words.txt를 
# 읽어서
# c가 포함된 단어 찾기
# , . 은 출력하지 않는다

with open('word.txt', 'r') as file :
    txt = file.read()
    print(txt)

    # txt = 'Fortunately, however, for the reputation of Asteroid B-612, a Turkish dictator made a law that his subjects, under pain of death, should change to European costume. So in 1920 the astronomer gave his demonstration all over again, dressed with impressive style and elegance. And this time everybody accepted his report.'
    txt_list = txt.split(' ')
    print(txt_list)
    # for i in range(len(txt_list)) :
    #     print(txt_list[i])

    for word in txt_list :
        # print(word)
        tmp = word.split('c')
        if len(tmp) > 1 :
            a = word.split('.')
            b = ''.join(a)
            c = b.split(',')
            d = ''.join(c)
            print(d)

print('-'*30)
with open('word.txt', 'r') as file :
    txt = file.read()
    print(txt)

    # txt = 'Fortunately, however, for the reputation of Asteroid B-612, a Turkish dictator made a law that his subjects, under pain of death, should change to European costume. So in 1920 the astronomer gave his demonstration all over again, dressed with impressive style and elegance. And this time everybody accepted his report.'
    txt_list = txt.split(' ')
    print(txt_list)
    # for i in range(len(txt_list)) :
    #     print(txt_list[i])

    for word in txt_list :
        # if word.find('c') != -1 :
        # if word.count('c') > 0 :
        # if 'c' in word or 'C' in word :
        if 'c'.lower() in word.lower() :
            a = word.replace(',', '')
            b = a.replace('.', '')
            # b = word.replace(',', '').replace('.', '')
            print(b)

# print([1,2,3].find())
```

---


# 2. 파일 입출력이란?

파일 입출력은 프로그램의 데이터를 파일에 저장하거나 파일의 데이터를 프로그램으로 읽어 오는 작업입니다.

```text
프로그램 메모리
→ 파일에 기록
→ 프로그램 종료
→ 다음 실행에서 파일을 다시 읽음
```

변수는 프로그램이 종료되면 사라지지만, 파일에 기록된 데이터는 저장 장치에 남습니다.

---

# 3. `open()` 기본 구조

```python
file = open("파일경로", "모드", encoding="문자인코딩")
```

주요 인자:

| 인자 | 의미 |
| --- | --- |
| 파일경로 | 열거나 생성할 파일의 위치 |
| 모드 | 읽기, 쓰기, 이어 쓰기, 바이너리 여부 |
| encoding | 텍스트를 문자로 변환할 때 사용할 인코딩 |

---

# 4. 파일 객체

```python
file = open("hello.txt", "r")
```

`open()`은 파일 내용 자체가 아니라 파일을 제어할 수 있는 파일 객체를 반환합니다.

파일 객체를 통해 다음 작업을 수행합니다.

```python
file.read()
file.write("내용")
file.flush()
file.close()
```

---

# 5. 파일 모드

| 모드 | 의미 | 파일이 없을 때 | 기존 내용 |
| --- | --- | --- | --- |
| `r` | 읽기 | 오류 | 유지 |
| `w` | 쓰기 | 새로 생성 | 모두 삭제 후 작성 |
| `a` | 이어 쓰기 | 새로 생성 | 끝에 추가 |
| `x` | 새 파일 생성 | 새로 생성 | 이미 있으면 오류 |
| `b` | 바이너리 | 다른 모드와 결합 | 바이트 단위 |
| `t` | 텍스트 | 기본값 | 문자열 단위 |
| `+` | 읽기와 쓰기 모두 허용 | 기본 모드에 따라 다름 | 기본 모드에 따라 다름 |

---

# 6. 쓰기 모드 `w`

원본:

```python
file = open("hello.txt", "w")
file.write("eng\n123\n한글")
file.close()
```

`w`는 파일이 없으면 새로 만들고, 파일이 있으면 기존 내용을 지운 뒤 처음부터 다시 씁니다.

> 기존 파일 내용을 유지해야 한다면 `w`를 사용하기 전에 반드시 확인해야 합니다.

---

# 7. `write()`

```python
file.write("eng\n123\n한글")
```

`write()`는 문자열을 파일에 기록합니다.

반환값은 일반적으로 기록한 문자 수입니다.

```python
count = file.write("Python")
print(count)
```

---

# 8. 줄바꿈 문자

```python
"eng\n123\n한글"
```

`\n`은 줄바꿈 문자입니다.

파일 내용:

```text
eng
123
한글
```

---

# 9. `flush()`

원본:

```python
file.flush()
```

파일 쓰기는 효율을 위해 데이터를 버퍼에 잠시 모아 두었다가 한 번에 저장할 수 있습니다. `flush()`는 버퍼에 남아 있는 내용을 즉시 운영체제로 전달하도록 요청합니다.

일반적인 파일 작업에서는 `close()`나 `with` 블록 종료 시 자동으로 처리되므로 매번 직접 호출할 필요는 없습니다.

---

# 10. `close()`

```python
file.close()
```

열린 파일을 닫습니다.

파일을 닫아야 하는 이유:

- 버퍼에 남은 내용을 반영한다.
- 운영체제의 파일 자원을 반환한다.
- 다른 프로그램이 파일을 사용할 수 있게 한다.
- 파일 손상이나 잠금 문제를 줄인다.

---

# 11. 문자 인코딩

문자는 파일에 그대로 저장되지 않고 바이트로 변환됩니다. 이 변환 규칙이 문자 인코딩입니다.

대표 인코딩:

| 인코딩 | 특징 |
| --- | --- |
| UTF-8 | 웹과 현대 개발 환경에서 가장 널리 사용 |
| CP949 | 한국어 Windows 환경에서 자주 사용 |
| EUC-KR | 과거 한국어 환경에서 사용 |

---

# 12. 쓰기와 읽기의 인코딩 일치

```python
with open("hello2.txt", "w", encoding="utf-8") as file:
    file.write("한글")
```

읽을 때도 같은 인코딩을 지정해야 합니다.

```python
with open("hello2.txt", "r", encoding="utf-8") as file:
    text = file.read()
```

서로 다른 인코딩으로 읽으면 `UnicodeDecodeError`가 발생할 수 있습니다.

---

# 13. 읽기 모드 `r`

```python
file = open("hello.txt", "r")
text = file.read()
file.close()
```

`r`은 파일을 읽기 전용으로 엽니다. 파일이 존재하지 않으면 `FileNotFoundError`가 발생합니다.

---

# 14. `read()`

```python
text = file.read()
```

인자를 전달하지 않으면 현재 파일 포인터 위치부터 끝까지 읽습니다.

반환형은 텍스트 모드에서 `str`, 바이너리 모드에서 `bytes`입니다.

---

# 15. `read(size)`

원본:

```python
text = file.read(10)
```

텍스트 모드에서는 최대 10개의 문자를 읽습니다.

> 원본 주석의 “2Byte만 읽는다”와 같은 설명은 정확하지 않습니다. 텍스트 모드의 `read(size)`는 일반적으로 문자 수를 기준으로 동작합니다. 바이트 단위 처리가 필요하면 바이너리 모드를 사용합니다.

---

# 16. 파일 포인터

파일 객체는 현재 읽거나 쓸 위치를 기억합니다.

```python
with open("hello.txt", "r") as file:
    first = file.read(3)
    second = file.read(3)
```

두 번째 `read()`는 파일 처음이 아니라 첫 번째 읽기가 끝난 위치부터 시작합니다.

---

# 17. 일정 크기씩 읽기

원본:

```python
text = ""

with open("hello.txt", "r") as file:
    while True:
        chunk = file.read(2)

        if not chunk:
            break

        text += chunk
        print(chunk)
```

파일이 크면 전체를 한 번에 메모리에 올리지 않고 일정 크기씩 읽을 수 있습니다.

종료 조건:

```python
if not chunk:
    break
```

파일 끝에 도달하면 빈 문자열이 반환됩니다.

---

# 18. `with` 문

```python
with open("hello.txt", "r") as file:
    text = file.read()
```

`with` 블록이 끝나면 파일이 자동으로 닫힙니다.

권장 이유:

- `close()` 누락 방지
- 예외가 발생해도 파일 정리
- 코드가 짧고 명확함
- 파일 사용 범위가 눈에 보임

---

# 19. 바이너리 모드

강사님 코드:

```python
with open("a.webp", "rb") as file:
    data = file.read()
```

이미지, 음원, 압축 파일 등은 텍스트가 아니라 바이트 데이터이므로 바이너리 모드를 사용합니다.

```text
r + b → rb
w + b → wb
```

반환형:

```python
bytes
```

---

# 20. 문자열로 저장한 리스트

원본:

```python
numbers = [1, 2, 3, 4]

with open("array1.txt", "w") as file:
    file.write(str(numbers))
```

파일에는 실제 리스트가 아니라 다음 문자열이 저장됩니다.

```text
[1, 2, 3, 4]
```

---

# 21. 다시 읽으면 문자열

```python
with open("array1.txt", "r") as file:
    value = file.read()

print(type(value))
```

출력:

```text
<class 'str'>
```

`list(value)`를 사용하면 원래 리스트가 복원되는 것이 아니라 문자를 하나씩 나눈 리스트가 만들어집니다.

```python
['[', '1', ',', ' ', '2', ...]
```

---

# 22. 직렬화

직렬화는 Python 객체를 파일에 저장 가능한 형태로 변환하는 과정입니다.

역직렬화는 저장된 데이터를 다시 Python 객체로 복원하는 과정입니다.

```text
Python 객체
→ 직렬화
→ 파일 저장
→ 역직렬화
→ Python 객체
```

---

# 23. `pickle`

```python
import pickle
```

`pickle`은 Python 객체를 직렬화하고 역직렬화하는 표준 라이브러리입니다.

저장 가능한 예:

- 문자열
- 숫자
- 리스트
- 튜플
- 딕셔너리
- 사용자 정의 객체

---

# 24. `pickle.dump()`

```python
with open("pickle.p", "wb") as file:
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(scores, file)
```

`dump()`는 객체를 바이너리 형태로 직렬화해 파일에 저장합니다.

---

# 25. `pickle.load()`

```python
with open("pickle.p", "rb") as file:
    name = pickle.load(file)
    age = pickle.load(file)
    scores = pickle.load(file)
```

저장한 순서와 같은 순서로 읽어야 합니다.

---

# 26. 여러 객체를 따로 저장할 때의 단점

원본은 여러 객체를 순서대로 `dump()`합니다.

```python
pickle.dump(name, file)
pickle.dump(age, file)
pickle.dump(address, file)
```

이 방식은 읽을 때 개수와 순서를 정확히 알아야 합니다.

실무에서는 관련 데이터를 하나의 딕셔너리로 묶는 편이 관리하기 쉽습니다.

```python
data = {
    "name": "eng",
    "age": 20,
    "address": "한글",
    "numbers": [1, 2, 3, 4],
}

with open("pickle.p", "wb") as file:
    pickle.dump(data, file)
```

---

# 27. `EOFError`

저장된 객체를 모두 읽은 뒤 다시 `pickle.load()`를 실행하면 다음 오류가 발생할 수 있습니다.

```text
EOFError: Ran out of input
```

파일 끝까지 읽었다는 의미입니다.

---

# 28. `pickle` 보안 주의

신뢰할 수 없는 `pickle` 파일을 `load()`하면 위험할 수 있습니다. 역직렬화 과정에서 임의 코드가 실행될 가능성이 있기 때문입니다.

> 출처를 알 수 없는 `pickle` 파일은 열지 않습니다.

외부 데이터 교환에는 JSON 같은 형식을 더 자주 사용합니다.

---

# 29. 이어 쓰기 모드 `a`

```python
with open("hello.txt", "a") as file:
    file.write("123")
```

`a`는 기존 내용을 유지한 채 파일 끝에 내용을 추가합니다.

---

# 30. `+` 모드

`+`는 기본 모드에 반대 기능을 추가합니다.

| 모드 | 의미 |
| --- | --- |
| `r+` | 읽기 + 쓰기, 파일이 있어야 함 |
| `w+` | 쓰기 + 읽기, 기존 내용 삭제 |
| `a+` | 이어 쓰기 + 읽기 |

파일 포인터 위치 때문에 쓰기 직후 읽으려면 `seek()`가 필요할 수 있습니다.

---

# 31. 단어 검색 실습

문제:

```text
word.txt에서 대소문자를 구분하지 않고
c가 포함된 단어를 출력한다.
쉼표와 마침표는 출력하지 않는다.
```

내 코드:

```python
with open("word.txt", "r") as file:
    for word in file.read().split():
        if "c" in word.lower():
            cleaned = word.replace(",", "").replace(".", "")
            print(cleaned)
```

---

# 32. 내 코드의 장점

- `split()`으로 단어를 직접 순회한다.
- `lower()`로 대소문자를 통일한다.
- `in` 연산자로 포함 여부를 명확하게 검사한다.
- `replace()`를 연결해 구두점을 제거한다.
- 중간 리스트와 인덱스 반복을 줄였다.
- Python다운 간결한 흐름이다.

---

# 33. 강사님 코드의 장점

강사님 코드는 여러 방법을 비교합니다.

```python
word.find("c")
word.count("c")
"c" in word
```

학습자가 문자열 검색 방법의 차이를 비교할 수 있습니다.

---

# 34. 개선된 단어 정리

쉼표와 마침표뿐 아니라 문자열 양끝의 여러 구두점을 제거하려면 `strip()`을 사용할 수 있습니다.

```python
with open("word.txt", "r", encoding="utf-8") as file:
    for raw_word in file.read().split():
        word = raw_word.strip(".,!?;:")

        if "c" in word.lower():
            print(word)
```

---

# 35. 경로 문제

상대 경로:

```python
open("hello.txt", "r")
```

현재 작업 디렉터리를 기준으로 파일을 찾습니다. 실행 위치가 달라지면 파일을 찾지 못할 수 있습니다.

`pathlib`을 사용하면 경로를 명확하게 관리할 수 있습니다.

```python
from pathlib import Path

file_path = Path(__file__).parent / "hello.txt"

with file_path.open("r", encoding="utf-8") as file:
    text = file.read()
```

---

# 36. 예외 처리

```python
from pathlib import Path

file_path = Path("hello.txt")

try:
    with file_path.open("r", encoding="utf-8") as file:
        text = file.read()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
except UnicodeDecodeError:
    print("파일 인코딩을 확인하세요.")
else:
    print(text)
```

---

# 37. 실무형 텍스트 저장 함수

```python
from pathlib import Path


def write_text_file(
    file_path: str,
    content: str,
) -> None:
    path = Path(file_path)

    path.write_text(
        content,
        encoding="utf-8",
    )
```

---

# 38. 실무형 텍스트 읽기 함수

```python
from pathlib import Path


def read_text_file(
    file_path: str,
) -> str:
    path = Path(file_path)

    return path.read_text(
        encoding="utf-8",
    )
```

---

# 39. 자주 하는 실수

### 39.1 `w` 모드로 기존 파일 열기

기존 내용이 모두 지워질 수 있습니다.

### 39.2 파일을 닫지 않기

버퍼 반영과 자원 해제가 늦어질 수 있습니다.

### 39.3 쓰기와 읽기의 인코딩 불일치

`UnicodeDecodeError`가 발생할 수 있습니다.

### 39.4 텍스트 파일을 바이너리 모드로 읽고 문자열처럼 사용

`bytes`와 `str`은 다른 자료형입니다.

### 39.5 `str(list)`를 저장한 뒤 `list()`로 원래 리스트 복원 시도

문자 단위 리스트가 만들어집니다.

### 39.6 `pickle.load()`를 저장 개수보다 많이 호출

`EOFError`가 발생합니다.

### 39.7 출처를 모르는 Pickle 파일 열기

보안 위험이 있습니다.

### 39.8 상대 경로를 실행 파일 위치로 착각

상대 경로는 현재 작업 디렉터리를 기준으로 해석됩니다.

---

# 40. 면접·복습 포인트

### Q1. `w`와 `a`의 차이는 무엇인가요?

`w`는 기존 내용을 지우고 처음부터 쓰며, `a`는 기존 내용 뒤에 추가합니다.

### Q2. `with` 문을 권장하는 이유는 무엇인가요?

블록이 끝날 때 파일을 자동으로 닫고, 예외가 발생해도 자원을 안전하게 정리하기 때문입니다.

### Q3. 인코딩은 왜 필요한가요?

문자와 바이트 사이의 변환 규칙을 결정하기 위해 필요합니다.

### Q4. 텍스트 모드와 바이너리 모드의 차이는 무엇인가요?

텍스트 모드는 문자열을, 바이너리 모드는 바이트를 읽고 씁니다.

### Q5. `pickle`은 무엇인가요?

Python 객체를 직렬화해 파일에 저장하고 다시 복원하는 라이브러리입니다.

### Q6. `pickle` 사용 시 주의할 점은 무엇인가요?

신뢰할 수 없는 파일을 역직렬화하면 보안 문제가 생길 수 있습니다.

### Q7. 내 단어 검색 코드가 강사님 초기 코드보다 간결한 이유는 무엇인가요?

단어를 직접 순회하고 `lower()`, `in`, `replace()`를 사용해 불필요한 인덱스와 중간 분해 과정을 줄였기 때문입니다.

---

# 최종 정리

```text
open()으로 파일을 연다.
→ 모드와 인코딩을 결정한다.
→ read() 또는 write()로 작업한다.
→ with 문으로 안전하게 닫는다.
→ 객체 자체를 저장해야 하면 직렬화를 고려한다.
→ 파일 경로와 예외를 함께 관리한다.
```
