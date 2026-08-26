# Python 오류와 예외

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `00-02_Python_오류와_예외.md` |
| 분류 | `04_Python` |
| 권장 선수 학습 | `00-01_Python_실행방식과_프로그래밍_패러다임.md` |
| 다음 학습 | `01_Python_출력과_주석.md` |
| 원본 기준 | Python 전체 학습 과정에서 반복해서 참고하는 오류 안내 문서 |
| 핵심 범위 | 오류 메시지, Traceback, 문법 오류, 예외, 주요 예외 클래스, 확인 순서 |

> 이 문서는 특정 실습 파일 하나를 해설하는 문서가 아니라 Python 학습 중 발생하는 오류 메시지를 읽고 해결하기 위한 공통 참고 문서입니다.

---

# 학습 목표

- 오류와 예외의 기본 차이를 이해한다.
- Traceback에서 파일명과 줄 번호를 찾는다.
- 오류 메시지를 아래에서 위로 읽는 방법을 익힌다.
- 예외 클래스와 상세 메시지를 구분한다.
- 자주 발생하는 Python 오류의 원인과 해결 방향을 설명한다.

---

# 1. 오류 메시지는 해결 단서다

오류 메시지는 다음 정보를 제공합니다.

```text
어느 파일에서 발생했는가?
몇 번째 줄에서 발생했는가?
어떤 종류의 오류인가?
왜 발생했는가?
```

오류가 발생하면 메시지를 바로 지우기보다 전체 내용을 먼저 확인합니다.

---

# 2. 문법 오류와 예외

## 2.1 문법 오류

Python 문법에 맞지 않아 코드를 정상적으로 분석할 수 없는 경우입니다.

```python
if True
    print("hello")
```

콜론이 빠졌기 때문에 `SyntaxError`가 발생합니다.

## 2.2 예외

문법 분석은 통과했지만 실행 중 처리할 수 없는 상황이 발생한 경우입니다.

```python
print(10 / 0)
```

0으로 나눌 수 없어 `ZeroDivisionError`가 발생합니다.

---

# 3. Traceback 기본 구조

```text
Traceback (most recent call last):
  File "D:\workspace\quiz\01_quiz.py", line 2, in <module>
    cart = {
TypeError: unhashable type: 'dict'
```

확인 순서:

```text
1. 마지막 줄의 예외 클래스 확인
2. 상세 메시지 확인
3. 바로 위의 실패 코드 확인
4. 파일명과 줄 번호 확인
5. 필요하면 위쪽 호출 흐름 확인
```

구분:

```text
TypeError                 → 예외 클래스
unhashable type: 'dict'   → 상세 메시지
```

---

# 4. Traceback은 아래에서 위로 읽는다

함수가 여러 번 호출되면 Traceback이 길어질 수 있습니다.

```python
def third():
    return 10 / 0

def second():
    return third()

def first():
    return second()

first()
```

```text
마지막 줄 → 실제 예외 종류
그 위 줄   → 직접 실패한 코드
더 위쪽    → 해당 코드에 도달한 호출 경로
```

---

# 5. SyntaxError

문법에 맞지 않을 때 발생합니다.

```python
if True
    print("hello")
```

수정:

```python
if True:
    print("hello")
```

확인 항목:

- 콜론 누락
- 괄호 또는 따옴표 누락
- 잘못된 연산자
- 문장 구조 오류

---

# 6. IndentationError

들여쓰기 규칙이 맞지 않을 때 발생합니다.

```python
print("hello")
    print("world")
```

```text
IndentationError: unexpected indent
```

수정:

```python
print("hello")
print("world")
```

또는 실제 블록 안에 작성합니다.

```python
if True:
    print("world")
```

---

# 7. NameError

정의되지 않은 이름을 사용할 때 발생합니다.

```python
print(user_name)
```

수정:

```python
user_name = "홍길동"
print(user_name)
```

---

# 8. TypeError

현재 자료형에서 지원하지 않는 연산이나 사용 방식을 적용할 때 발생합니다.

```python
print("가격: " + 1000)
```

수정:

```python
print("가격: " + str(1000))
print("가격:", 1000)
```

---

# 9. 실전 사례: unhashable type: dict

오류 코드:

```python
cart = {
    {"상품명": "사과", "가격": "1000"},
    {"상품명": "바나나", "가격": "2000"}
}
```

가장 바깥쪽 `{}`는 세트로 해석됩니다. 세트의 원소는 해시 가능한 값이어야 하지만 딕셔너리는 변경 가능한 객체이므로 세트 원소로 사용할 수 없습니다.

```text
바깥쪽 { } → set
내부 { }   → dict
set 원소는 hash 가능해야 함
변경 가능한 dict는 hash 불가능
```

여러 딕셔너리를 저장하려면 리스트를 사용합니다.

```python
cart = [
    {"상품명": "사과", "가격": "1000"},
    {"상품명": "바나나", "가격": "2000"}
]
```

---

# 10. ValueError

자료형 변환 방식은 맞지만 값의 내용이 변환 조건에 맞지 않을 때 발생합니다.

```python
number = int("사과")
```

수정:

```python
number = int("100")
```

---

# 11. IndexError

존재하지 않는 인덱스를 사용할 때 발생합니다.

```python
numbers = [10, 20, 30]
print(numbers[3])
```

사용 가능한 인덱스는 `0`, `1`, `2`입니다.

---

# 12. KeyError

딕셔너리에 존재하지 않는 키를 직접 조회할 때 발생합니다.

```python
user = {"name": "홍길동"}
print(user["age"])
```

키 존재 여부를 확인하거나 `get()`을 사용할 수 있습니다.

```python
print(user.get("age"))
print(user.get("age", 0))
```

---

# 13. AttributeError

객체가 가지고 있지 않은 속성이나 메서드를 사용할 때 발생합니다.

```python
numbers = [1, 2, 3]
numbers.upper()
```

`upper()`는 문자열에서 사용합니다.

```python
text = "python"
print(text.upper())
```

---

# 14. ZeroDivisionError

0으로 나누거나 나머지를 구할 때 발생합니다.

```python
print(10 / 0)
```

```python
divisor = 0

if divisor != 0:
    print(10 / divisor)
else:
    print("0으로 나눌 수 없습니다.")
```

---

# 15. ModuleNotFoundError

불러오려는 모듈을 찾을 수 없을 때 발생합니다.

```python
import unknown_module
```

확인 항목:

- 모듈 이름 철자
- 설치 여부
- 현재 Python 환경
- 가상환경 활성화 여부

---

# 16. FileNotFoundError

지정한 경로에 파일이 없을 때 발생합니다.

```python
open("data.txt", "r")
```

확인 항목:

- 파일명과 확장자
- 현재 작업 디렉터리
- 상대 경로 기준
- 파일 존재 여부

---

# 17. 오류 확인 절차

```text
1. 오류 메시지를 전체 확인한다.
2. 마지막 줄에서 예외 클래스를 찾는다.
3. 상세 메시지의 대상 자료형이나 이름을 확인한다.
4. 파일명과 줄 번호로 이동한다.
5. 해당 줄에서 사용한 값과 자료형을 확인한다.
6. 오류 줄 바로 위의 코드도 확인한다.
7. 최소 코드로 다시 실행한다.
8. 수정 후 같은 입력으로 재검증한다.
```

---

# 18. 오류를 숨기는 잘못된 방법

```python
try:
    result = 10 / 0
except:
    pass
```

모든 예외를 무시하면 원인을 찾기 어렵습니다.

```python
try:
    result = 10 / 0
except ZeroDivisionError as error:
    print(error)
```

예외 처리 문법은 이후 학습에서 자세히 다룹니다.

---

# 19. Improvements

| 피해야 할 접근 | 권장 접근 |
| --- | --- |
| 오류 메시지 일부만 확인 | 전체 Traceback 보존 |
| 코드 전체를 무작정 수정 | 실패한 최소 지점부터 확인 |
| 검색 결과를 그대로 복사 | 현재 코드와 자료형에 맞는지 검증 |
| `except:`로 모두 숨김 | 구체적인 예외 클래스 처리 |
| 오류가 사라지면 종료 | 정상 입력과 경계 입력으로 재검증 |

---

# 20. Common Mistakes

- Traceback의 마지막 예외를 확인하지 않습니다.
- 오류 줄만 보고 그 값을 만든 이전 코드는 확인하지 않습니다.
- `TypeError`와 `ValueError`를 같은 오류로 생각합니다.
- 인덱스와 원소 개수를 혼동합니다.
- 딕셔너리 키가 항상 존재한다고 가정합니다.
- 모든 예외를 하나의 `except:`로 처리합니다.

---

# 21. Interview / Review

## Q1. Traceback은 어느 방향으로 읽나요?

마지막 줄에서 예외 클래스와 상세 메시지를 먼저 확인하고 위쪽으로 올라갑니다.

## Q2. TypeError와 ValueError의 차이는 무엇인가요?

`TypeError`는 자료형이나 연산 방식이 맞지 않을 때, `ValueError`는 자료형은 사용할 수 있지만 값의 내용이 조건에 맞지 않을 때 주로 발생합니다.

## Q3. 딕셔너리가 세트 원소가 될 수 없는 이유는 무엇인가요?

딕셔너리는 변경 가능한 객체이며 해시 가능하지 않기 때문입니다.

---

# 22. Problems

## 문제 1

다음 메시지에서 예외 클래스와 상세 메시지를 구분하세요.

```text
ValueError: invalid literal for int() with base 10: 'python'
```

## 문제 2

다음 코드의 오류를 예상하세요.

```python
numbers = [1, 2, 3]
print(numbers[5])
```

## 문제 3

다음 코드가 오류를 발생시키는 이유를 설명하세요.

```python
user = {"name": "kim"}
print(user["age"])
```

---

# 23. Answers

## 정답 1

```text
예외 클래스: ValueError
상세 메시지: invalid literal for int() with base 10: 'python'
```

## 정답 2

```text
IndexError
```

## 정답 3

딕셔너리에 `age` 키가 없는데 대괄호로 직접 조회했기 때문에 `KeyError`가 발생합니다.

---

# 24. Final Checklist

- [ ] Traceback의 마지막 줄에서 예외 종류를 찾을 수 있다.
- [ ] 파일명과 줄 번호를 확인할 수 있다.
- [ ] SyntaxError와 실행 중 예외를 구분할 수 있다.
- [ ] 주요 예외 클래스의 대표 원인을 설명할 수 있다.
- [ ] `unhashable type: 'dict'`의 원인을 설명할 수 있다.

---

# 25. Key Summary

```text
오류 메시지는 문제 해결을 위한 정보다.
Traceback은 마지막 예외부터 확인한다.
예외 클래스와 상세 메시지를 구분한다.
오류 줄뿐 아니라 그 값을 만든 이전 코드도 확인한다.
구체적인 예외를 이해하고 최소 코드로 재현한다.
```

# V3 동작 백과 보강 — 오류가 만들어지고 전달되는 과정

| 종류 | 발생 시점 | 예 | 확인할 것 |
|---|---|---|---|
| 문법 오류 | 실행 준비 단계 | 괄호·콜론·들여쓰기 오류 | 표시된 줄과 바로 윗줄 |
| 실행 예외 | 문장을 실행하는 중 | `int("abc")` | 예외 클래스, 메시지, 값의 출처 |
| 논리 오류 | 정상 종료하지만 결과가 틀림 | 평균 계산식 오류 | 중간값, 조건식, 자료형 |

```python
raw = "abc"
print("변환 전:", raw, type(raw))
number = int(raw)
print("변환 후:", number)
```

첫 번째 `print()`는 `변환 전: abc <class 'str'>`를 출력한다. 다음 줄에서 `int`가 숫자로 해석할 수 없는 문자열을 받아 `ValueError`를 만든다. 처리하는 `try-except`가 없으므로 호출 경로를 거슬러 전달되고 프로그램이 멈춰 마지막 `print()`는 실행되지 않는다.

**원본 연결:** 번호형 Python 원본 전반의 실행 오류를 읽기 위한 공통 문서다. 구체적인 `try-except` 작성은 내 코드 `workspace_python/14_try.py`, 강사님 코드 `workspace_python/_14_try.py`와 연결한다.
