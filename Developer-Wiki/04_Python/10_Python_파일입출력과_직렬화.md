---
title: Python 파일 입출력과 직렬화
version: v3.0-encyclopedia
last_updated: 2026-08-06
status: Completed
---

# Python 파일 입출력과 직렬화

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `10_Python_파일입출력과_직렬화.md` |
| 분류 | `04_Python` |
| 원본 기준 | `workspace_python/10_file.py`, `workspace_teacher/workspace_python/_10_file.py` |
| 핵심 범위 | 파일 열기·닫기, `w`·`r`·`a`·`b`·`+` 모드, 인코딩, `read()`, 버퍼, `with`, `pickle`, 파일 포인터, 텍스트 검색 |
| 실습 범위 | 텍스트 저장·읽기, UTF-8 처리, 청크 단위 읽기, 바이너리 파일, 리스트 저장, 객체 직렬화, 단어 필터링 |
| 문서 형식 | Python Developer-Wiki V2 확정 형식 |

> 이 문서는 내 코드와 강사님 코드 전체를 그대로 나열하지 않는다.  
> 파일 생성·읽기·추가·직렬화에 필요한 핵심 코드만 발췌하고, 파일 모드·인코딩·자원 정리·보안 주의점을 함께 설명한다.

---

# 개요

파일 입출력은 프로그램이 실행을 종료한 뒤에도 데이터를 남기기 위해 사용한다.

```text
프로그램 내부 데이터
    ↓
파일에 저장
    ↓
프로그램 종료
    ↓
다음 실행에서 다시 읽기
```

예를 들어 다음 데이터를 파일에 저장할 수 있다.

- 사용자 설정
- 학습 결과
- 주문 내역
- 로그
- 텍스트 문서
- 이미지와 같은 바이너리 데이터

Python 파일 입출력의 기본 흐름은 다음과 같다.

```text
파일 열기
    ↓
읽기 또는 쓰기
    ↓
파일 닫기
```

실무에서는 `with`문을 사용해 파일이 자동으로 닫히도록 작성하는 것이 기본이다.

---

# 핵심 개념

| 개념 | 핵심 역할 |
| --- | --- |
| `open()` | 파일 열기 |
| `w` | 새로 쓰기, 기존 내용 덮어쓰기 |
| `r` | 읽기 |
| `a` | 기존 내용 뒤에 이어 쓰기 |
| `b` | 바이너리 모드 |
| `+` | 읽기와 쓰기 모두 허용 |
| `encoding` | 문자 인코딩 지정 |
| `read()` | 파일 내용 읽기 |
| `write()` | 문자열 또는 바이트 쓰기 |
| `flush()` | 버퍼 내용을 즉시 파일에 반영 |
| `close()` | 파일 자원 닫기 |
| `with` | 블록 종료 시 자동으로 파일 닫기 |
| 파일 포인터 | 현재 읽기·쓰기 위치 |
| `pickle` | Python 객체를 바이너리 형태로 직렬화 |
| 직렬화 | 객체를 저장 가능한 형태로 변환 |
| 역직렬화 | 저장된 데이터를 객체로 복원 |

---

# 학습 목표

이 문서를 학습한 뒤 다음 내용을 설명하고 작성할 수 있어야 한다.

- `open()`으로 파일을 열 수 있다.
- `w`, `r`, `a` 모드의 차이를 설명할 수 있다.
- 쓰기 모드가 기존 파일 내용을 덮어쓴다는 점을 이해한다.
- `write()`로 문자열을 저장할 수 있다.
- `flush()`와 `close()`의 역할을 설명할 수 있다.
- 텍스트 파일에서 인코딩을 지정할 수 있다.
- 읽기와 쓰기에 같은 인코딩을 사용하는 이유를 이해한다.
- `read(size)`로 일정한 크기만큼 읽을 수 있다.
- 반복문으로 파일을 청크 단위로 읽을 수 있다.
- 텍스트 모드와 바이너리 모드의 차이를 구분할 수 있다.
- `with`문으로 파일 자원을 안전하게 관리할 수 있다.
- 리스트를 문자열로 저장했을 때 원래 자료형이 유지되지 않는 이유를 설명할 수 있다.
- `pickle.dump()`와 `pickle.load()`를 사용할 수 있다.
- `pickle` 파일을 저장 순서대로 읽어야 하는 이유를 이해한다.
- 신뢰할 수 없는 `pickle` 파일을 열면 안 되는 이유를 이해한다.
- `a`, `r+`, `w+`, `a+`의 기본 차이를 설명할 수 있다.
- 파일 포인터 때문에 읽기 결과가 비어 보일 수 있음을 이해한다.
- 파일에서 특정 조건의 단어를 검색할 수 있다.

---

# 1. 파일 열기

파일은 `open()` 함수로 연다.

```python
file = open(
    "hello.txt",
    "w",
)
```

## 1-1. 구성

| 요소 | 의미 |
| --- | --- |
| `"hello.txt"` | 파일 경로 |
| `"w"` | 쓰기 모드 |
| `file` | 열린 파일 객체 |

파일 객체를 이용해 읽기와 쓰기 작업을 수행한다.

> [!IMPORTANT]
> `open()`으로 연 파일은 작업이 끝난 뒤 반드시 닫아야 한다.

---

# 2. 쓰기 모드 `w`

## 2-1. 내 코드

```python
file = open(
    "hello.txt",
    "w",
)

file.write(
    "eng\n123\n한글"
)

file.flush()
file.close()
```

## 2-2. 강사님 코드

```python
file = open(
    "hello.txt",
    "w",
)

file.write(
    "eng\n123\n한글"
)

file.flush()
file.close()
```

두 코드는 동일한 흐름이다.

## 2-3. 저장 결과

```text
eng
123
한글
```

## 2-4. `w` 모드 특징

```text
파일 없음
→ 새 파일 생성

파일 있음
→ 기존 내용 삭제 후 새로 작성
```

> [!WARNING]
> 기존 파일을 `w` 모드로 열면 이전 내용이 사라진다.
>
> 기존 내용 뒤에 추가하려면 `a` 모드를 사용한다.

---

# 3. `write()`

`write()`는 문자열을 파일에 기록한다.

```python
file.write(
    "Python"
)
```

반환값은 작성한 문자 수다.

```python
with open(
    "hello.txt",
    "w",
    encoding="utf-8",
) as file:
    written_count = file.write(
        "Python"
    )

print(written_count)
```

출력:

```text
6
```

> [!IMPORTANT]
> 텍스트 모드의 `write()`에는 문자열을 전달해야 한다.

---

# 4. 줄바꿈 저장

`write()`는 자동으로 줄을 바꾸지 않는다.

```python
with open(
    "hello.txt",
    "w",
    encoding="utf-8",
) as file:
    file.write("첫 번째 줄\n")
    file.write("두 번째 줄")
```

파일 내용:

```text
첫 번째 줄
두 번째 줄
```

줄바꿈이 필요하면 `\n`을 직접 작성한다.

---

# 5. `flush()`

파일 쓰기는 성능을 위해 버퍼에 임시로 저장될 수 있다.

```text
write()
    ↓
버퍼에 임시 저장
    ↓
버퍼가 차거나 파일이 닫힘
    ↓
실제 파일에 반영
```

`flush()`는 버퍼가 가득 차지 않았더라도 내용을 즉시 운영체제에 전달한다.

```python
file.flush()
```

일반적인 파일 작업에서는 `close()` 또는 `with`문 종료 시 자동으로 처리되므로 매번 직접 호출할 필요는 없다.

---

# 6. `close()`

`close()`는 파일 자원을 닫는다.

```python
file.close()
```

닫힌 파일에는 추가 작업을 할 수 없다.

```python
file = open(
    "hello.txt",
    "w",
)

file.close()
file.write("Python")
```

발생 결과:

```text
ValueError: I/O operation on closed file
```

---

# 7. 문자 인코딩

문자열은 파일에 저장될 때 바이트로 변환된다.

이때 어떤 규칙으로 문자를 바이트로 바꿀지 정하는 것이 인코딩이다.

원본에서 다룬 대표 인코딩:

- UTF-8
- EUC-KR
- CP949

```python
file = open(
    "hello2.txt",
    "w",
    encoding="utf-8",
)
```

> [!TIP]
> 특별한 요구사항이 없다면 UTF-8을 우선 사용하는 것이 일반적이다.

---

# 8. UTF-8로 쓰기

## 8-1. 내 코드와 강사님 코드

```python
file = open(
    "hello2.txt",
    "w",
    encoding="utf-8",
)

file.write(
    "eng\n123\n한글"
)

file.close()
```

파일 내용:

```text
eng
123
한글
```

한글이 포함된 텍스트는 인코딩을 명확하게 지정하는 것이 안전하다.

---

# 9. 읽기 모드 `r`

## 9-1. 원본 코드

```python
file = open(
    "hello.txt",
    "r",
)

text = file.read()

file.close()

print(text)
```

## 9-2. 출력 결과

```text
eng
123
한글
```

## 9-3. `r` 모드 특징

```text
파일 존재
→ 읽기 가능

파일 없음
→ FileNotFoundError
```

---

# 10. 인코딩을 맞춰 읽기

UTF-8로 저장한 파일은 읽을 때도 UTF-8을 지정한다.

```python
file = open(
    "hello2.txt",
    "r",
    encoding="utf-8",
)

text = file.read()

file.close()

print(text)
```

인코딩이 맞지 않으면 `UnicodeDecodeError`가 발생할 수 있다.

> [!IMPORTANT]
> 저장할 때 사용한 인코딩과 읽을 때 사용한 인코딩이 일치해야 한다.

---

# 11. 기본 인코딩 주의

원본 메모에는 Python이 기본적으로 EUC-KR로 읽는다고 적혀 있지만, 정확히는 운영체제와 실행 환경의 기본 인코딩을 사용한다.

Windows의 한국어 환경에서는 CP949가 기본값으로 선택될 수 있다.

정확한 방식:

```python
with open(
    "hello2.txt",
    "r",
    encoding="utf-8",
) as file:
    text = file.read()
```

인코딩을 코드에 명시하면 실행 환경 차이를 줄일 수 있다.

---

# 12. `read()`

`read()`는 파일 전체 내용을 문자열로 반환한다.

```python
with open(
    "hello.txt",
    "r",
    encoding="utf-8",
) as file:
    text = file.read()

print(type(text))
```

출력:

```text
<class 'str'>
```

텍스트 파일을 읽으면 문자열이 반환된다.

---

# 13. `read(size)`

## 13-1. 원본 코드

```python
file = open(
    "hello.txt",
    "r",
)

text = file.read(10)

file.close()

print(text)
```

`read(10)`은 텍스트 모드에서 최대 10개의 문자를 읽는다.

> [!IMPORTANT]
> 원본 주석의 “2Byte만 읽는다”는 설명은 정확하지 않다.
>
> 텍스트 모드의 `read(size)`는 일반적으로 문자 수를 기준으로 읽는다. 바이너리 모드에서는 바이트 수를 기준으로 읽는다.

---

# 14. 청크 단위 읽기

## 14-1. 원본 코드

```python
text = ""

file = open(
    "hello.txt",
    "r",
)

while True:
    chunk = file.read(2)

    if not chunk:
        break

    text += chunk
    print(chunk)

file.close()

print(text)
```

## 14-2. 실행 흐름

```text
2문자 읽기
    ↓
읽은 값이 비어 있는가?
    ├─ 아니오 → 출력·누적
    └─ 예 → 반복 종료
```

## 14-3. 왜 사용할까?

파일 전체를 한 번에 메모리에 올리기 어려운 큰 파일은 일정한 크기로 나누어 읽을 수 있다.

---

# 15. 파일 끝과 빈 문자열

파일 끝에 도달하면 `read()`는 빈 문자열을 반환한다.

```python
chunk = file.read(2)

if not chunk:
    break
```

```text
읽을 데이터 있음
→ 문자열 반환

파일 끝
→ ""
```

빈 문자열은 Falsy이므로 반복 종료 조건으로 사용할 수 있다.

---

# 16. 버퍼링

원본에는 다음 코드가 있다.

```python
file = open(
    "hello.txt",
    "r",
    buffering=1,
)
```

`buffering`은 파일 입출력의 버퍼링 방식을 설정한다.

다만 `buffering=1`의 줄 단위 버퍼링은 주로 텍스트 쓰기 상황에서 의미가 크다.

일반적인 학습 코드에서는 기본 버퍼 설정을 사용하는 것으로 충분하다.

> [!TIP]
> 버퍼 크기를 직접 조절하기 전에는 실제 성능 문제가 있는지 먼저 확인한다.

---

# 17. 바이너리 모드 `b`

텍스트가 아닌 이미지·영상·압축 파일은 바이너리 모드로 읽는다.

## 17-1. 강사님 코드

```python
file = open(
    "a.webp",
    "rb",
)

data = file.read()

file.close()

print(data)
```

## 17-2. 반환 자료형

```text
<class 'bytes'>
```

## 17-3. 텍스트와 비교

| 모드 | 반환값 |
| --- | --- |
| `"r"` | 문자열 `str` |
| `"rb"` | 바이트 `bytes` |
| `"w"` | 문자열 기록 |
| `"wb"` | 바이트 기록 |

---

# 18. `with`문

## 18-1. 원본 코드

```python
with open(
    "hello.txt",
    "r",
) as file:
    text = file.read()
    print(text)
```

## 18-2. 장점

블록이 끝나면 파일이 자동으로 닫힌다.

```text
with 블록 시작
    ↓
파일 열기
    ↓
파일 작업
    ↓
블록 종료
    ↓
자동 close()
```

> [!IMPORTANT]
> 파일 작업은 특별한 이유가 없다면 `with`문을 기본으로 사용한다.

---

# 19. 예외가 발생해도 닫히는 이유

```python
with open(
    "hello.txt",
    "r",
    encoding="utf-8",
) as file:
    text = file.read()
    raise ValueError(
        "테스트 오류"
    )
```

블록 안에서 오류가 발생해도 컨텍스트 관리자가 파일 정리를 처리한다.

이 때문에 직접 `open()`·`close()`를 반복하는 방식보다 안전하다.

---

# 20. 리스트를 문자열로 저장

## 20-1. 원본 코드

```python
numbers = [
    1,
    2,
    3,
    4,
]

with open(
    "array1.txt",
    "w",
) as file:
    file.write(
        str(numbers)
    )
```

파일 내용:

```text
[1, 2, 3, 4]
```

리스트 자체가 저장된 것이 아니라 리스트를 표현한 문자열이 저장된다.

---

# 21. 문자열을 `list()`로 변환할 때

## 21-1. 원본 코드

```python
with open(
    "array1.txt",
    "r",
) as file:
    text = file.read()
    values = list(text)

    print(type(text), text)
    print(type(values), values)
```

## 21-2. 출력 결과 형태

```text
<class 'str'> [1, 2, 3, 4]
<class 'list'> ['[', '1', ',', ' ', '2', ',', ...]
```

`list(text)`는 문자열을 문자 단위로 나눈다.

원래 정수 리스트로 복원하지 않는다.

> [!IMPORTANT]
> `str(list)`로 저장한 문자열을 `list()`로 감싸도 원래 리스트 자료형으로 돌아가지 않는다.

---

# 22. 구조화된 텍스트 저장

문자열·숫자·리스트·딕셔너리를 안전하게 텍스트로 저장하려면 JSON을 사용할 수 있다.

```python
import json

numbers = [
    1,
    2,
    3,
    4,
]

with open(
    "array.json",
    "w",
    encoding="utf-8",
) as file:
    json.dump(
        numbers,
        file,
        ensure_ascii=False,
        indent=2,
    )
```

읽기:

```python
with open(
    "array.json",
    "r",
    encoding="utf-8",
) as file:
    numbers = json.load(file)
```

JSON은 다른 언어와도 데이터를 주고받기 좋다.

---

# 23. 직렬화란?

직렬화는 메모리의 객체를 파일에 저장하거나 전송할 수 있는 형태로 바꾸는 과정이다.

```text
Python 객체
    ↓ 직렬화
파일에 저장 가능한 데이터
    ↓ 역직렬화
Python 객체
```

원본에서는 `pickle` 모듈을 이용해 문자열·정수·리스트·딕셔너리를 저장한다.

---

# 24. `pickle.dump()`

## 24-1. 원본 코드

```python
import pickle

name = "eng"
age = 20
address = "한글"
numbers = [
    1,
    2,
    3,
    4,
]
scores = {
    "k": 1,
    "k2": "val",
}

with open(
    "pickle.p",
    "wb",
) as file:
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(numbers, file)
    pickle.dump(scores, file)
```

`pickle.dump()`는 객체를 직렬화해 바이너리 파일에 기록한다.

## 24-2. 왜 `wb`일까?

`pickle` 결과는 텍스트 문자열이 아니라 바이너리 데이터이므로 `wb` 모드를 사용한다.

---

# 25. `pickle.load()`

```python
with open(
    "pickle.p",
    "rb",
) as file:
    loaded_name = (
        pickle.load(file)
    )
    loaded_age = (
        pickle.load(file)
    )

print(loaded_name)
print(loaded_age)
print(type(loaded_age))
```

출력:

```text
eng
20
<class 'int'>
```

문자열로 변환되지 않고 원래 자료형으로 복원된다.

---

# 26. 저장 순서와 읽기 순서

여러 객체를 각각 `dump()`했다면 같은 순서와 횟수로 `load()`해야 한다.

```text
dump(name)
dump(age)
dump(address)
    ↓
load() → name
load() → age
load() → address
```

원본 메모처럼 저장한 횟수보다 많이 읽으면 다음 오류가 발생한다.

```text
EOFError: Ran out of input
```

---

# 27. 객체 하나로 묶어 저장

여러 객체를 각각 저장하기보다 하나의 딕셔너리나 리스트로 묶으면 관리하기 쉽다.

```python
data = {
    "name": "eng",
    "age": 20,
    "address": "한글",
    "numbers": [
        1,
        2,
        3,
        4,
    ],
    "scores": {
        "k": 1,
        "k2": "val",
    },
}

with open(
    "pickle.p",
    "wb",
) as file:
    pickle.dump(
        data,
        file,
    )
```

읽기:

```python
with open(
    "pickle.p",
    "rb",
) as file:
    loaded_data = (
        pickle.load(file)
    )
```

---

# 28. `pickle` 보안 주의

> [!WARNING]
> 신뢰할 수 없는 출처의 `pickle` 파일을 `load()`하면 안 된다.
>
> 역직렬화 과정에서 악성 코드가 실행될 수 있다.

`pickle`은 다음 상황에 적합하다.

- 자신이 만든 Python 프로그램 내부 데이터
- 신뢰할 수 있는 파일
- Python 객체 구조를 그대로 복원해야 하는 경우

외부 데이터 교환에는 JSON 같은 안전하고 범용적인 형식을 우선 검토한다.

---

# 29. 추가 모드 `a`

## 29-1. 원본 코드

```python
with open(
    "hello.txt",
    "a",
) as file:
    file.write("123")
```

기존 내용 뒤에 `"123"`이 추가된다.

```text
기존 내용 유지
    ↓
파일 끝으로 이동
    ↓
새 내용 추가
```

---

# 30. `a` 모드에서는 읽을 수 없다

```python
with open(
    "hello.txt",
    "a",
) as file:
    file.read()
```

발생 결과:

```text
io.UnsupportedOperation: not readable
```

`a`는 추가 쓰기 전용 모드다.

읽기도 필요하면 `a+`를 사용할 수 있다.

---

# 31. `+` 모드

원본에는 다음 메모가 있다.

```text
쓰기 계열에 +가 붙으면 읽기 가능
읽기 계열에 +가 붙으면 쓰기 가능
```

대표 모드:

| 모드 | 기본 동작 |
| --- | --- |
| `r+` | 읽기·쓰기, 파일이 있어야 함 |
| `w+` | 읽기·쓰기, 기존 내용 삭제 |
| `a+` | 읽기·추가 쓰기, 없으면 생성 |

> [!WARNING]
> `w+`도 기존 파일 내용을 삭제한다.

---

# 32. 파일 포인터

파일에는 현재 읽기·쓰기 위치를 나타내는 파일 포인터가 있다.

```python
with open(
    "test.txt",
    "w+",
    encoding="utf-8",
) as file:
    file.write("test")
    content = file.read()

    print(content)
```

출력:

```text

```

쓰기 후 파일 포인터가 파일 끝에 있기 때문에 읽을 내용이 없다.

---

# 33. `seek()`

파일 포인터를 이동하려면 `seek()`를 사용한다.

```python
with open(
    "test.txt",
    "w+",
    encoding="utf-8",
) as file:
    file.write("test")
    file.seek(0)

    content = file.read()

    print(content)
```

출력:

```text
test
```

## 33-1. 구성

| 코드 | 의미 |
| --- | --- |
| `file.write()` | 파일 끝까지 쓰며 포인터 이동 |
| `file.seek(0)` | 파일 처음으로 이동 |
| `file.read()` | 처음부터 읽기 |

---

# 34. `tell()`

현재 파일 포인터 위치는 `tell()`로 확인할 수 있다.

```python
with open(
    "test.txt",
    "r",
    encoding="utf-8",
) as file:
    print(file.tell())

    file.read(2)

    print(file.tell())
```

텍스트 모드에서 반환되는 위치값은 내부 인코딩 처리와 관련된 위치 정보이므로 단순 문자 인덱스와 항상 같다고 가정하면 안 된다.

---

# 35. 파일을 줄 단위로 순회

텍스트 파일은 직접 반복할 수 있다.

```python
with open(
    "hello.txt",
    "r",
    encoding="utf-8",
) as file:
    for line in file:
        print(
            line.rstrip()
        )
```

큰 텍스트 파일을 한 줄씩 처리할 때 `read()`로 전체를 한 번에 읽는 것보다 메모리 사용을 줄일 수 있다.

---

# 36. `readline()`과 `readlines()`

```python
with open(
    "hello.txt",
    "r",
    encoding="utf-8",
) as file:
    first_line = (
        file.readline()
    )
```

`readline()`은 한 줄을 읽는다.

```python
with open(
    "hello.txt",
    "r",
    encoding="utf-8",
) as file:
    lines = file.readlines()
```

`readlines()`는 모든 줄을 리스트로 반환한다.

> [!TIP]
> 큰 파일은 직접 반복하거나 `readline()`을 사용해 한 줄씩 처리하는 것이 좋다.

---

# 37. 단어 검색 실습 요구사항

원본 실습의 요구사항은 다음과 같다.

```text
word.txt 읽기
    ↓
대소문자 구분 없이 c가 포함된 단어 검색
    ↓
쉼표와 마침표 제거
    ↓
조건에 맞는 단어 출력
```

---

# 38. 내 코드의 최종 방식

```python
with open(
    "word.txt",
    "r",
) as file:
    for word in (
        file.read().split()
    ):
        cleaned_word = (
            word
            .replace(",", "")
            .replace(".", "")
        )

        if "c" in (
            cleaned_word.lower()
        ):
            print(
                cleaned_word,
                end=" ",
            )
```

## 38-1. 동작 과정

```text
파일 전체 읽기
    ↓
공백 기준 단어 분리
    ↓
쉼표·마침표 제거
    ↓
소문자로 변환
    ↓
c 포함 여부 확인
    ↓
출력
```

---

# 39. 강사님 코드 방식

강사님 코드는 두 가지 방식으로 접근한다.

첫 번째 방식:

```text
split("c")
    ↓
나눈 결과 길이가 1보다 큰지 확인
    ↓
구두점 제거
```

두 번째 방식:

```python
if "c".lower() in word.lower():
    cleaned_word = (
        word
        .replace(",", "")
        .replace(".", "")
    )

    print(cleaned_word)
```

두 번째 방식이 의도를 더 직접적으로 표현한다.

---

# 40. 구두점 제거 개선

원본 문제는 쉼표와 마침표만 제거한다.

```python
cleaned_word = (
    word
    .replace(",", "")
    .replace(".", "")
)
```

여러 구두점을 제거해야 한다면 `strip()` 또는 `translate()`를 고려할 수 있다.

```python
import string

cleaned_word = (
    word.strip(
        string.punctuation
    )
)
```

> [!TIP]
> 요구사항이 쉼표와 마침표만 제거하는 것이라면 단순 `replace()`도 충분하다.

---

# 41. 대소문자 구분 없는 검색

```python
if "c" in word.lower():
    ...
```

검색 기준과 대상 모두 같은 형태로 맞추는 것이 핵심이다.

더 일반적인 형태:

```python
keyword = "c"

if keyword.casefold() in (
    word.casefold()
):
    ...
```

영문 검색에는 `lower()`도 충분한 경우가 많다.

---

# 42. `pathlib.Path`

문자열 경로 대신 `Path` 객체를 사용할 수 있다.

```python
from pathlib import Path

file_path = Path(
    "data/hello.txt"
)

with file_path.open(
    "r",
    encoding="utf-8",
) as file:
    text = file.read()
```

## 42-1. 장점

- 운영체제 경로 차이를 줄인다.
- 경로 조합이 쉽다.
- 파일 존재 여부를 확인할 수 있다.
- 부모 폴더를 생성할 수 있다.

```python
file_path.parent.mkdir(
    parents=True,
    exist_ok=True,
)
```

---

# 43. 파일 존재 여부 확인

```python
from pathlib import Path

file_path = Path(
    "hello.txt"
)

if file_path.exists():
    print("파일이 있습니다.")
else:
    print("파일이 없습니다.")
```

읽기 전에 파일이 있는지 확인할 수 있다.

다만 파일 존재 확인과 실제 열기 사이에 상태가 바뀔 수 있으므로, 중요한 작업에서는 예외 처리도 함께 사용한다.

---

# 44. 파일 모드 선택 기준

```text
새로 저장
→ w

기존 파일 읽기
→ r

기존 내용 뒤에 추가
→ a

이미지·pickle
→ b 추가

읽기와 쓰기 모두 필요
→ + 검토
```

> [!IMPORTANT]
> 모드를 선택할 때 기존 내용을 유지해야 하는지 먼저 확인한다.

---

# 45. 내 코드와 강사님 코드 비교

| 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 파일 쓰기 | 모드·인코딩 설명 메모 상세 | 핵심 코드 중심 |
| `read(size)` | 바이트 단위라고 메모 | 크기 지정 예제 |
| 인코딩 | CP949 오류 원인 기록 | UTF-8 지정 중심 |
| 청크 읽기 | 결과 예시와 누적 설명 | 기본 반복 코드 |
| 바이너리 읽기 | 이미지 코드를 주석 처리 | 실제 `rb` 실행 |
| `with` | 자동 종료 설명 | 기본 사용 |
| 리스트 저장 | 문자 단위 변환 문제 설명 | 동일한 실습 |
| `pickle` | 여러 자료형과 EOF 오류 기록 | 저장 순서 중심 |
| 파일 모드 | `a`, `+` 메모 추가 | 기본 개념 설명 |
| 단어 검색 | 여러 버전을 실험한 뒤 단순화 | 두 가지 풀이 제시 |

## 45-1. 내 코드의 장점

- 인코딩 오류와 `UnicodeDecodeError`를 실제 상황과 연결했다.
- 청크 단위 읽기와 파일 끝 조건을 직접 확인했다.
- 리스트를 문자열로 저장했을 때의 한계를 기록했다.
- `pickle`의 자료형 복원과 EOF 오류를 직접 실습했다.
- 단어 검색 문제를 여러 방식으로 개선했다.

## 45-2. 내 코드의 개선점

- `read(10)`은 텍스트 모드에서 10바이트가 아니라 최대 10문자를 읽는다.
- 기본 인코딩은 항상 EUC-KR이 아니라 실행 환경에 따라 달라진다.
- 파일 객체 변수명은 `file`보다 역할이 드러나는 이름을 사용할 수 있다.
- 여러 객체를 각각 `pickle.dump()`하기보다 하나의 구조로 묶으면 관리하기 쉽다.
- 파일 읽기·쓰기는 가능한 한 `with`문을 기본으로 사용한다.

## 45-3. 강사님 코드의 장점

- 텍스트·바이너리 파일과 여러 모드를 한 흐름으로 실습한다.
- `pickle`이 자료형을 유지해 복원한다는 점을 확인할 수 있다.
- 단어 검색 문제를 단계적으로 개선한다.
- `a`와 `+` 모드의 개념을 함께 설명한다.

## 45-4. 강사님 코드의 보충점

- `pickle`의 보안 위험 설명이 필요하다.
- 파일 포인터와 `seek()`가 없으면 `+` 모드를 이해하기 어렵다.
- 인코딩 기본값은 운영체제에 따라 달라질 수 있다는 보충이 필요하다.
- JSON과 `pickle`의 선택 기준을 추가하면 좋다.

---

# 46. 기존 코드에서 개선 코드로 바꾼 이유

## 46-1. `with`문 사용

기존:

```python
file = open(
    "hello.txt",
    "r",
)

text = file.read()

file.close()
```

개선:

```python
with open(
    "hello.txt",
    "r",
    encoding="utf-8",
) as file:
    text = file.read()
```

이유:

- 예외가 발생해도 파일이 닫힌다.
- `close()` 누락 가능성을 줄인다.

## 46-2. 인코딩 명시

기존:

```python
open(
    "hello.txt",
    "r",
)
```

개선:

```python
open(
    "hello.txt",
    "r",
    encoding="utf-8",
)
```

이유:

- 실행 환경에 따른 문자 깨짐을 줄인다.

## 46-3. 직렬화 객체 묶기

기존:

```python
pickle.dump(name, file)
pickle.dump(age, file)
pickle.dump(scores, file)
```

개선:

```python
pickle.dump(
    {
        "name": name,
        "age": age,
        "scores": scores,
    },
    file,
)
```

## 46-4. 의미 있는 변수명

기존:

```python
s = file.read()
b = file.read()
```

개선:

```python
text = file.read()
loaded_data = (
    pickle.load(file)
)
```

---

# 47. 실무형 예제: 사용자 설정 저장

JSON 파일에 사용자 설정을 저장하고 다시 읽는 예제다.

```python
import json
from pathlib import Path

settings_file = Path(
    "data/settings.json"
)

settings = {
    "theme": "dark",
    "language": "ko",
    "font_size": 16,
}

settings_file.parent.mkdir(
    parents=True,
    exist_ok=True,
)

with settings_file.open(
    "w",
    encoding="utf-8",
) as file:
    json.dump(
        settings,
        file,
        ensure_ascii=False,
        indent=2,
    )

with settings_file.open(
    "r",
    encoding="utf-8",
) as file:
    loaded_settings = (
        json.load(file)
    )

print(loaded_settings)
```

## 47-1. 출력 결과

```text
{'theme': 'dark', 'language': 'ko', 'font_size': 16}
```

## 47-2. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `Path` | 파일 경로 관리 |
| `mkdir()` | 부모 폴더 생성 |
| `with` | 파일 자동 닫기 |
| UTF-8 | 한글 설정값 안전하게 저장 |
| `json.dump()` | 딕셔너리를 JSON 파일에 저장 |
| `json.load()` | JSON을 Python 객체로 복원 |

---

# 48. 대표 오류로 이해하기

## 48-1. 없는 파일 읽기

```python
open(
    "missing.txt",
    "r",
)
```

발생 결과:

```text
FileNotFoundError
```

---

## 48-2. 잘못된 인코딩

UTF-8 파일을 다른 인코딩으로 읽으면 다음 오류가 발생할 수 있다.

```text
UnicodeDecodeError
```

---

## 48-3. 텍스트 모드에 바이트 쓰기

```python
with open(
    "hello.txt",
    "w",
) as file:
    file.write(b"Python")
```

발생 결과:

```text
TypeError
```

---

## 48-4. 바이너리 모드에 문자열 쓰기

```python
with open(
    "data.bin",
    "wb",
) as file:
    file.write("Python")
```

발생 결과:

```text
TypeError
```

---

## 48-5. 닫힌 파일 사용

```python
file = open(
    "hello.txt",
    "r",
)

file.close()
file.read()
```

발생 결과:

```text
ValueError
```

---

## 48-6. `pickle.load()` 초과 호출

저장한 객체 수보다 많이 읽으면 다음 오류가 발생한다.

```text
EOFError
```

---

# 49. 자주 하는 실수

## 49-1. `w` 모드가 기존 내용을 유지한다고 생각

기존 파일 내용을 삭제하고 새로 쓴다.

## 49-2. 파일을 닫지 않음

자원 누수나 저장 지연이 발생할 수 있다.

## 49-3. 읽기와 쓰기 인코딩을 다르게 사용

문자 깨짐 또는 `UnicodeDecodeError`가 발생할 수 있다.

## 49-4. `read(size)`의 크기를 항상 바이트로 이해

텍스트 모드와 바이너리 모드의 기준이 다르다.

## 49-5. 문자열 파일을 읽으면 원래 리스트가 복원된다고 생각

텍스트로 저장하면 다시 파싱해야 한다.

## 49-6. `list(text)`가 문자열 표현을 원래 리스트로 변환한다고 생각

문자 단위 리스트를 만든다.

## 49-7. `pickle` 파일을 외부에서 받아 그대로 열기

악성 코드가 실행될 수 있다.

## 49-8. `a` 모드에서 읽기 시도

읽기 기능이 없어 `UnsupportedOperation`이 발생한다.

## 49-9. `w+`가 기존 내용을 유지한다고 생각

파일을 비운 뒤 읽기·쓰기를 허용한다.

## 49-10. 쓰기 직후 `read()`하면 처음부터 읽힌다고 생각

파일 포인터가 끝에 있으므로 `seek(0)`이 필요할 수 있다.

## 49-11. 큰 파일을 무조건 `read()`로 전체 읽기

청크 또는 줄 단위 처리를 검토한다.

## 49-12. 단어 검색에서 대소문자를 그대로 비교

검색 기준과 대상의 대소문자를 정규화한다.

---

# 50. 핵심 요약

```text
w
→ 새로 쓰기·덮어쓰기

r
→ 읽기

a
→ 이어 쓰기

b
→ 바이너리

+
→ 읽기·쓰기
```

```text
write()
→ 데이터 기록

read()
→ 전체 읽기

read(size)
→ 일부 읽기

flush()
→ 버퍼 즉시 반영

close()
→ 파일 닫기
```

```text
with
→ 자동 자원 정리

encoding
→ 문자 변환 규칙

seek()
→ 파일 포인터 이동

tell()
→ 현재 위치 확인
```

```text
pickle.dump()
→ 객체 직렬화

pickle.load()
→ 객체 복원

json.dump()
→ JSON 저장

json.load()
→ JSON 복원
```

---

# 51. 최종 체크리스트

- [ ] `open()`으로 파일을 열 수 있는가?
- [ ] `w`, `r`, `a` 모드를 구분할 수 있는가?
- [ ] `w` 모드가 기존 내용을 삭제함을 이해했는가?
- [ ] `write()`로 문자열을 저장할 수 있는가?
- [ ] 줄바꿈이 필요할 때 `\n`을 작성할 수 있는가?
- [ ] `flush()`와 `close()`의 역할을 설명할 수 있는가?
- [ ] UTF-8 인코딩을 명시할 수 있는가?
- [ ] 읽기와 쓰기에 같은 인코딩을 사용할 수 있는가?
- [ ] `read()`와 `read(size)`를 사용할 수 있는가?
- [ ] 파일 끝에서 빈 문자열이 반환됨을 이해했는가?
- [ ] 청크 단위로 파일을 읽을 수 있는가?
- [ ] 텍스트 모드와 바이너리 모드를 구분할 수 있는가?
- [ ] `with`문으로 파일을 자동으로 닫을 수 있는가?
- [ ] 문자열 저장과 객체 직렬화의 차이를 설명할 수 있는가?
- [ ] JSON으로 리스트·딕셔너리를 저장할 수 있는가?
- [ ] `pickle.dump()`와 `pickle.load()`를 사용할 수 있는가?
- [ ] `pickle`의 저장 순서와 보안 위험을 이해했는가?
- [ ] `r+`, `w+`, `a+`의 기본 차이를 이해했는가?
- [ ] `seek()`로 파일 포인터를 이동할 수 있는가?
- [ ] 파일을 줄 단위로 순회할 수 있는가?
- [ ] 특정 단어를 대소문자 구분 없이 검색할 수 있는가?
- [ ] 파일 경로에 `pathlib.Path`를 사용할 수 있는가?

---

# 마무리

파일 입출력의 핵심은 단순히 파일을 열고 닫는 것에서 끝나지 않는다.

```text
적절한 모드로 파일을 열고
    ↓
인코딩과 자료형을 맞추고
    ↓
필요한 크기만큼 안전하게 읽고 쓰고
    ↓
with문으로 자원을 정리하고
    ↓
데이터 목적에 맞는 저장 형식을 선택하는 것
```

이 흐름을 이해하면 이후 모듈·예외 처리·클래스에서 프로그램 데이터를 더 안정적으로 저장하고 불러올 수 있다.

# V3 동작 백과 보강 — 경로에서 Python 객체까지

상대 경로는 소스 파일 위치가 아니라 현재 작업 폴더를 기준으로 해석된다. `open()`은 운영체제에 파일 열기를 요청하고 파일 객체를 반환한다. 읽기 메서드는 디스크의 바이트를 지정 인코딩으로 해석해 문자열로 돌려준다. `with` 블록을 벗어나면 예외 여부와 관계없이 파일을 닫는다.

```python
from pathlib import Path

path = Path("memo.txt")
with path.open("w", encoding="utf-8") as file:
    file.write("Python\n")
with path.open("r", encoding="utf-8") as file:
    text = file.read()
print(repr(text))
```

```text
'Python\n'
```

파일이 없으면 `FileNotFoundError`, 권한이 없으면 `PermissionError`, 인코딩이 맞지 않으면 `UnicodeDecodeError`가 날 수 있다. JSON은 언어 간 교환에 유리하고, pickle은 Python 객체 복원에 편하지만 신뢰하지 않는 파일을 읽으면 안 된다.

**원본 연결:** 내 코드 `workspace_python/10_file.py`, 강사님 코드 `workspace_python/_10_file.py`의 텍스트·바이너리 파일, `with`, pickle/JSON 예제를 기반으로 한다.
