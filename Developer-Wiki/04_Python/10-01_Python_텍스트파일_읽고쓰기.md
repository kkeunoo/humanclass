# 10-01. 텍스트 파일 — 열기·읽는 위치·쓰기·닫기 연결하기

[Python 목차](README.md) · [읽기 안내](00-00_Python_V3_동작_백과_읽기법.md)

파일을 읽은 결과는 경로와 모드, 인코딩, 현재 읽은 위치에 따라 달라진다. open과 read를 한 줄 암기하는 대신 어떤 파일의 어떤 상태를 다루는지 순서대로 확인한다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

w·r·a와 텍스트·바이너리 모드를 구분한다. read의 문자 단위와 파일 끝, with의 닫기, 문자열로 저장한 리스트가 자동 복원되지 않는 이유를 설명한다.

실제 원본·새 예제·개선안·선택 학습을 구분하고 입력·실행 순서·반환값·출력을 연결한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

파일은 프로그램이 끝난 뒤에도 내용을 남길 수 있는 저장 대상이다. open은 해당 파일을 지정한 모드로 열고 파일 객체를 반환한다. 파일 객체에 read·write를 호출하여 내용을 다룬다. 상대 경로는 현재 작업 폴더를 기준으로 읽으므로 .py 파일이 있는 곳과 실행 작업 폴더를 구별해야 한다.

| 모드·호출 | 역할 | 확인할 조건 |
| --- | --- | --- |
| w | 쓰기, 기존 내용 비움 | 기존 파일 보존 목적과 다름 |
| r | 읽기 | 파일이 존재해야 함 |
| a | 끝에 이어 쓰기 | 반복하면 덧붙인 내용도 누적 |
| rb·wb | 바이트 읽기·쓰기 | 텍스트 인코딩 인수와 구분 |
| read(n) | 텍스트에서 최대 n문자 읽기 | 다음 호출은 그 다음 위치 |
| read() | 남은 내용 읽기 | 이미 읽은 앞부분을 자동 재독하지 않음 |

텍스트 모드는 문자를 읽고 바이너리 모드는 바이트를 읽는다. 한글 한 글자가 UTF-8에서 여러 바이트가 될 수 있어 두 단위를 혼동하지 않는다. 텍스트 파일 끝에서 read는 빈 문자열을 준다. 이것은 숫자 0이나 문자열 '0'과 다르며 if not chunk로 끝을 검사할 수 있다.

with open(...) as file은 블록 동안 파일을 사용하고 나갈 때 닫는 흐름을 묶는다. flush는 Python 버퍼의 데이터를 아래 계층으로 내보내는 작업이며 전원 장애까지 포함한 영구 저장 완료를 무조건 보장하는 말은 아니다. 첫 학습에서는 읽기·쓰기 후 닫기와 인코딩 일치를 먼저 확인한다.

> 📚 **출처 · 본문 설명 확인:** [Python 파일 읽고 쓰기](https://docs.python.org/ko/3/tutorial/inputoutput.html#reading-and-writing-files), [open](https://docs.python.org/ko/3/library/functions.html#open). 실제 배운 문법의 의미를 확인한 근거다. 예제·표·풀이 자체는 수업 자료를 바탕으로 새로 구성했다. 외부 문장을 직접 인용하지 않았다. 이번 문법 확인 기간: 2026-10-28~29.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 코드.** [실행 파일](실습/책형_복습/10-01_Python_텍스트파일_읽고쓰기.py)을 제공한다. 별도 빈 복습 폴더에 .py 파일로 저장해 실행한다. 현재 작업 폴더에 book_text.txt를 새로 쓰며 같은 이름의 기존 연습 파일은 처음 w에서 비운다. 원본 수업 파일명이 아닌 별도 예제 이름을 사용한다.



```python
with open('book_text.txt', 'w', encoding='utf-8') as file:
    written = file.write('가나다라')
print('쓴 문자', written)
with open('book_text.txt', 'r', encoding='utf-8') as file:
    print('첫 읽기', file.read(2))
    print('다음 읽기', file.read(2))
    print('끝 [' + file.read(2) + ']')
with open('book_text.txt', 'a', encoding='utf-8') as file:
    file.write('\n마')
with open('book_text.txt', 'r', encoding='utf-8') as file:
    text = ''
    while True:
        chunk = file.read(2)
        if not chunk:
            break
        text += chunk
print(text)
print(type(text))
```

첫 write는 네 문자를 썼다는 수 4를 반환한다. read(2)를 두 번 호출하면 가나·다라를 이어서 읽고 다음 호출은 파일 끝의 빈 문자열이다. 대괄호 사이가 빈 결과로 보인다. a로 줄바꿈과 마를 이어 쓴 뒤 새로 r로 열면 처음부터 읽는다. 두 문자씩 이어 붙여 전체 문자열을 만들었다. 프로그램을 다시 실행하면 맨 앞 w가 기존 파일을 비우므로 마만 무한 누적하는 예제가 아니다.

**예상 출력 또는 관찰:**

```text
쓴 문자 4
첫 읽기 가나
다음 읽기 다라
끝 []
가나다라
마
<class 'str'>
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본 발췌다. 주석의 잘못된 설명도 원문을 보존하고 풀이에서 교정한다. 필요한 선언·호출·다른 파일의 정의는 다음 절까지 연결해 읽는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/10_file.py` 1–24행

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

**발췌 바로 풀이:** `'w'`는 파일을 쓰기 모드로 열고, 파일이 이미 있으면 **기존 내용을 비우고 새로 쓴다**. `write('eng\n123\n한글')`의 `\n`은 줄바꿈이다. `flush()`는 아직 버퍼에 남은 내용을 내보내고, `close()`는 파일을 닫는다. `'r'`은 읽기 모드이고 `read()`는 남은 텍스트를 읽는다. 강사님은 `hello2.txt`에 쓰고 읽을 때 모두 `encoding='utf-8'`을 지정했다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/10_file.py` 26–55행

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

**발췌 바로 풀이:** **텍스트 모드**의 `read(10)`은 여기서 최대 **문자 10개**를 읽는다. 내 주석의 “2Byte만”이라는 설명은 인자 `10`과도 맞지 않고, 텍스트 읽기의 단위를 설명하지도 못한다. `read(2)`를 반복하면 파일 끝에서 빈 문자열 `''`을 받으므로 `if not chunk: break`로 멈춘다. 내 주석의 출력 예시는 읽는 단위와 줄바꿈 위치가 섞여 보여 실제로 한 줄씩 읽는다고 오해하기 쉽다. 이 코드는 **한 번에 문자 두 개씩** 읽는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/10_file.py` 57–84행

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

**발췌 바로 풀이:** `'rb'`는 바이너리 읽기 모드다. 강사님 코드는 `a.webp`를 열지만, 제공된 해당 폴더에는 그 파일이 없어서 **파일 전체를 그대로 실행하면 여기서 멈출 수 있다**. 내 대응 줄은 주석 처리되어 있다. 이미지 파일 내용을 텍스트처럼 해석하는 예제가 아니라, **바이트로 읽는 모드**를 보여 주는 예다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/10_file.py` 123–128행

```python
with open('hello.txt', 'a') as f : # 'a'는 이어 쓰기(append)
    f.write('123')
    # f.read() # io.UnsupportedOperation: not readable / 읽을 수 없다는 에러 발생

# + 가 쓰기 계열에 붙어있으면, 읽기 가능해짐
# + 가 읽기 계열에 붙어있으면, 쓰기 가능해짐
```

**발췌 바로 풀이:** `'a'`는 파일 끝에 새 내용을 덧붙인다. 여기서는 `hello.txt` 끝에 `'123'`을 쓰며, 다시 실행하면 같은 글자가 또 붙는다. 두 원본 모두 `'a'` 모드에서 `read()`는 주석으로 막았다. `+`를 붙인 읽기·쓰기 모드는 주석으로 개념만 적혀 있고 **실제 실행 예시는 없다**. 자세한 포인터 위치와 모드 조합은 이 장의 본문 학습 범위로 확대하지 않는다.

내 첫 w 주석은 파일이 있으면 여는 것으로만 적었지만 기존 내용 비우기가 중요하다. 한글을 utf-8로 쓰고 읽는 부분은 맞다. 인코딩 생략의 기본값을 언제나 euc-kr이라고 설명하지 않는다. read(10)에 2Byte라는 주석은 인수와 단위 모두 맞지 않는다. 내 이미지 rb 부분은 주석이며 강사님은 a.webp를 실제 열지만 제공 폴더의 그 파일이 없으면 전체 실행이 여기서 멈출 수 있다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

open의 반환 파일 객체 → write 또는 read 메서드 → 반환값 사용 → close 또는 with 종료 순서다. read(2) 반복은 chunk를 받고 빈 문자열이면 break한다. 원본 str(a)를 array1.txt에 쓰고 다시 읽은 b는 문자열이다. list(b)는 문자열의 각 문자를 나열하여 대괄호·쉼표까지 항목으로 담는다. 다음 pickle 장의 자료형 복원과 비교한다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 내 코드가 명시 인코딩·with·파일 끝 검사까지 연결했다. **주석 교정:** 문자와 바이트, 모드 w의 효과, 기본 인코딩을 분명히 한다. **실행 조건:** 원본 전체는 여러 파일을 만들고 외부 이미지도 요구하므로 작은 예제의 성공을 원본 전체 성공으로 바꾸어 보고하지 않는다. **개선:** 자원 사용 구간은 with로 읽기 쉽게 묶고 텍스트 의도를 인코딩으로 드러낸다.

개선안은 D 드라이브 원본을 수정한 결과가 아니다. 실제 오류·수업용 단순화·목적에 따른 선택을 구별한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



핵심 텍스트 처리는 같아서 강사님 전체 코드를 반복하지 않는다. 이미지 읽기는 강사님 활성·내 주석이라는 차이가 있고 원본 실행 조건도 다르다. + 모드 조합은 양쪽 주석에만 있어 실제 상세 실습으로 확대하지 않는다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 상태 | 읽은 결과 | 다음 위치 |
| --- | --- | --- |
| 처음 r로 열기 | 아직 안 읽음 | 처음 |
| read(2) | 가나 | 다 앞 |
| read(2) | 다라 | 끝 |
| read(2) | 빈 문자열 | 끝 |
| 닫고 새로 r | 다시 처음부터 읽음 | 새 읽기 흐름 |

buffering=1이 원본에 있다고 read(1)과 같은 한 글자 단위가 되는 것은 아니다. 원본은 같은 본문을 read로 읽는다. 버퍼의 내부 최적화와 반환 텍스트의 단위를 나누어 설명한다.

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| read(2)를 read(1)로 | 한 번에 한 문자 | 읽기 단위 변경 |
| 첫 w를 a로 | 기존 내용에 누적 | 파일 여는 효과 변경 |
| write의 줄바꿈 제거 | 가나다라마 한 줄 | 저장 글자 자체 차이 |
| 다음 read 앞에서 다시 open | 처음 가나부터 읽음 | 새 파일 객체의 시작 위치 |

파일을 못 찾으면 작업 폴더와 이름을 확인한다. 한글 오류면 쓰기·읽기의 인코딩을 비교한다. 두 번째 읽기가 비면 이미 끝까지 읽었는지 본다. 줄바꿈은 read가 한 줄씩 보장해서가 아니라 저장한 문자열 안의 글자이기도 하다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 경로 도구·다양한 개행 처리·+ 모드의 포인터 상세·fsync 등 저장 보장과 대용량 파일 전략은 추가 학습이다. 기본은 실제 모드·문자 읽기·with·끝 검사다.

TIP은 기본 문제의 필수 조건이 아니다. 배운 문법을 확인한 📚 출처와 선택 확장을 구별한다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. 텍스트 read(10)은 이 예제에서 무엇 10개인가?
2. 파일 끝 read는 무엇을 주는가?
3. w와 a의 기존 내용 처리는?
4. list(file.read())는 저장 전 숫자 리스트를 복원하는가?

<details>
<summary>풀이 — 먼저 자신의 답을 적은 뒤 펼치기</summary>

최대 문자 10개다. 파일 끝은 빈 문자열이다. w는 비우고 a는 끝에 덧붙인다. list는 읽은 문자열을 문자별 리스트로 만들 뿐 원래 숫자 구조를 복원하지 않는다.

</details>

| 확인 | 질문 |
| --- | --- |
| 대상 | 어느 작업 폴더의 파일인가? |
| 모드 | 비움·읽기·덧붙임 중 무엇인가? |
| 단위 | 문자·바이트 중 무엇인가? |
| 상태 | 읽은 위치와 닫기 |

[장별 연습문제](실습/연습문제/10-01_Python_텍스트파일_읽고쓰기_연습문제.md) · 다음은 [pickle 저장](10-02_Python_pickle과_자료형저장.md)이다.

<!-- 이전 명시 앵커 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
<a id="section-6"></a>
