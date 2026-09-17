# Python 오류와 예외

## 이 문서에서 바로 찾기

- [학습 목표](#py-00-02-section-2)
- [개념에서 실제 실행까지 — 예외란? — 값이 들어오고 실패 지점이 생기는 과정](#py-00-02-section-3)
- [22. Problems](#py-00-02-section-25)
- [23. Answers](#py-00-02-section-26)
- [25. Key Summary](#py-00-02-section-28)

<details>
<summary>상세 목차 전체 펼치기</summary>

- [문서 정보](#py-00-02-section-1)
- [학습 목표](#py-00-02-section-2)
- [개념에서 실제 실행까지 — 예외란? — 값이 들어오고 실패 지점이 생기는 과정](#py-00-02-section-3)
- [1. 오류 메시지는 해결 단서다](#py-00-02-section-4)
- [2. 문법 오류와 예외](#py-00-02-section-5)
- [3. Traceback 기본 구조](#py-00-02-section-6)
- [4. Traceback은 아래에서 위로 읽는다](#py-00-02-section-7)
- [5. SyntaxError](#py-00-02-section-8)
- [6. IndentationError](#py-00-02-section-9)
- [7. NameError](#py-00-02-section-10)
- [8. TypeError](#py-00-02-section-11)
- [9. 실전 사례: unhashable type: dict](#py-00-02-section-12)
- [10. ValueError](#py-00-02-section-13)
- [11. IndexError](#py-00-02-section-14)
- [12. KeyError](#py-00-02-section-15)
- [13. AttributeError](#py-00-02-section-16)
- [14. ZeroDivisionError](#py-00-02-section-17)
- [15. ModuleNotFoundError](#py-00-02-section-18)
- [16. FileNotFoundError](#py-00-02-section-19)
- [17. 오류 확인 절차](#py-00-02-section-20)
- [18. 오류를 숨기는 잘못된 방법](#py-00-02-section-21)
- [19. Improvements](#py-00-02-section-22)
- [20. Common Mistakes](#py-00-02-section-23)
- [21. Interview / Review](#py-00-02-section-24)
- [22. Problems](#py-00-02-section-25)
- [23. Answers](#py-00-02-section-26)
- [24. Final Checklist](#py-00-02-section-27)
- [25. Key Summary](#py-00-02-section-28)
- [V3 동작 백과 보강 — 오류가 만들어지고 전달되는 과정](#py-00-02-section-29)

</details>

---

<a id="py-00-02-section-1"></a>

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

<a id="py-00-02-section-2"></a>

## 학습 목표

- 오류 종류·실패 값·호출 경로를 함께 확인한다.
- 예제의 입력·처리·출력과 대표 실패 조건을 직접 확인한다.

---

<a id="py-00-02-section-3"></a>

## 개념에서 실제 실행까지 — 예외란? — 값이 들어오고 실패 지점이 생기는 과정

### 무엇이며 왜 배워야 할까?

오류 메시지는 Python이 어떤 작업을 완수하지 못했는지 알려 주는 진단 정보다. 문법 오류는 실행을 준비하는 단계에서, 실행 예외는 유효한 문장을 실제 값에 적용하는 단계에서 발생한다. 정상 종료해도 평균이나 집계가 틀리면 논리 오류이므로 Traceback이 없다는 이유만으로 정답이라고 판단하면 안 된다.

키보드에서 들어온 abc는 문자열이다. int는 이 문자열을 정수로 해석하려 하지만 숫자 형식이 아니므로 ValueError를 발생시킨다. int(None)처럼 그 변환을 지원하지 않는 자료형을 전달하는 경우의 TypeError와 원인을 구분한다. 예외를 처리하는 블록이 없으면 호출 경로를 거슬러 전달되어 실행이 중단된다. 실패 다음 줄의 print는 실행되지 않는다.

Traceback에서는 마지막 예외 종류와 메시지를 먼저 보고, 바로 위의 실패 줄과 그 위의 호출 경로를 확인한다. 긴 파일 전체를 고치기 전에 repr(raw), type(raw), len(raw)를 찍어 실제 입력을 좁히는 것이 효과적이다. 다만 비밀번호·토큰 등 민감한 값은 출력하지 않는다.

### 독립 실행 예제: 입력에서 결과까지

다음 코드는 앞 문서의 변수 없이 새 .py 파일에서 실행할 수 있는 보충 예제다. 직접 적은 입력값을 사용하므로 같은 조건에서 아래 출력과 비교할 수 있다.

```python
raw = 'abc'
print('입력', repr(raw), type(raw).__name__)
try:
    number = int(raw)
except ValueError as error:
    print(type(error).__name__)
print('계속 실행')
```

예상 출력:

```text
입력 'abc' str
ValueError
계속 실행
```

### 실행 순서를 한 단계씩 따라가기

1. raw는 소스 리터럴에서 들어온 str 'abc'다. repr로 따옴표까지 관찰한다.
2. int(raw)가 실행되며 숫자 형식 변환에 실패한다.
3. ValueError를 잡는 except로 이동하여 종류를 출력한다.
4. 처리 블록이 끝난 뒤 다음 문장으로 진행한다. int 뒤의 성공 문장을 실행했다는 뜻은 아니다.

### 원본에서 어디에 사용했을까?


#### 내 코드: `14_try.py` 1~7행

문맥 확인용 원본 발췌다. 이 조각만 독립 실행할 수 있다는 뜻은 아니다. 주석의 설명은 아래 실제 동작 해설과 대조한다.

```python
# try, except 사용 전 방법 1
def div(x, y) :
    if y != 0 :
        result = x / y
    else :
        print('두 번째 숫자는 0이 올 수 없습니다')
    return result
```

<a id="index-section-10"></a>

#### 강사님 코드: `_14_try.py` 12~18행

문맥 확인용 원본 발췌다. 이 조각만 독립 실행할 수 있다는 뜻은 아니다. 주석의 설명은 아래 실제 동작 해설과 대조한다.

```python
    try:
        result = x / y
    except:
        print('예외 발생')

    return result
```

예외를 잡은 뒤 계속 진행할 수 있는지 판단해야 한다. 필수 데이터가 없으면 경고만 출력하고 잘못된 계산을 계속하기보다 중단하거나 호출자에게 실패를 전달한다.

<a id="index-section-11"></a>

### 실무에서 판단할 기준과 디버깅

정상 입력에서 결과가 나오는 것뿐 아니라 아래 본문의 오류·경계 입력도 확인한다. 화면 출력, 반환값, 원본 객체의 변경은 서로 다른 관찰 대상이다. 문제가 생기면 실패 문장에 쓰인 값의 출처와 자료형을 먼저 확인한 뒤 같은 입력으로 다시 실행한다.

### 이해 확인 실습과 해설

1. try 안의 int 뒤에 print('성공')을 넣으면 abc 입력에서 실행될까?
2. int(None), int('abc'), [1][2]의 예외를 각각 예상하라.

<details>
<summary>정답과 이유 보기 — 먼저 출력·상태를 예측한 뒤 펼치기</summary>

1. 실행되지 않는다. 실패 시 except로 이동하고 처리 후 try 문장 다음으로 진행한다.
2. TypeError, ValueError, IndexError다. 실제 값의 자료형·내용·인덱스 범위가 각각 원인이다.

</details>

### 이 주제를 다시 사용할 수 있는지 확인

- [ ] 이 개념이 무엇이며 언제 필요한지 내 말로 설명한다.
- [ ] 예제의 입력 출처, 자료형, 처리 순서, 결과를 설명한다.
- [ ] 원본과 보충 예제의 조건이 같은지 구분한다.
- [ ] 오류 사례와 경계 입력을 바꾸어 직접 확인한다.

---

<a id="py-00-02-section-4"></a>

## 1. 오류 메시지는 해결 단서다

오류 메시지는 다음 정보를 제공합니다.

```text
어느 파일에서 발생했는가?
몇 번째 줄에서 발생했는가?
어떤 종류의 오류인가?
왜 발생했는가?
```

오류가 발생하면 메시지를 바로 지우기보다 전체 내용을 먼저 확인합니다.

---

<a id="py-00-02-section-5"></a>

## 2. 문법 오류와 예외

### 2.1 문법 오류

Python 문법에 맞지 않아 코드를 정상적으로 분석할 수 없는 경우입니다.

```python
if True
    print("hello")
```

콜론이 빠졌기 때문에 `SyntaxError`가 발생합니다.

<a id="index-section-17"></a>

### 2.2 예외

문법 분석은 통과했지만 실행 중 처리할 수 없는 상황이 발생한 경우입니다.

```python
print(10 / 0)
```

0으로 나눌 수 없어 `ZeroDivisionError`가 발생합니다.

---

<a id="py-00-02-section-6"></a>

## 3. Traceback 기본 구조

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

<a id="py-00-02-section-7"></a>

## 4. Traceback은 아래에서 위로 읽는다

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

<a id="py-00-02-section-8"></a>

## 5. SyntaxError

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

<a id="py-00-02-section-9"></a>

## 6. IndentationError

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

<a id="py-00-02-section-10"></a>

## 7. NameError

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

<a id="py-00-02-section-11"></a>

## 8. TypeError

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

<a id="py-00-02-section-12"></a>

## 9. 실전 사례: unhashable type: dict

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

<a id="py-00-02-section-13"></a>

## 10. ValueError

자료형 변환 방식은 맞지만 값의 내용이 변환 조건에 맞지 않을 때 발생합니다.

```python
number = int("사과")
```

수정:

```python
number = int("100")
```

---

<a id="py-00-02-section-14"></a>

## 11. IndexError

존재하지 않는 인덱스를 사용할 때 발생합니다.

```python
numbers = [10, 20, 30]
print(numbers[3])
```

사용 가능한 인덱스는 `0`, `1`, `2`입니다.

---

<a id="py-00-02-section-15"></a>

## 12. KeyError

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

<a id="py-00-02-section-16"></a>

## 13. AttributeError

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

<a id="py-00-02-section-17"></a>

## 14. ZeroDivisionError

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

<a id="py-00-02-section-18"></a>

## 15. ModuleNotFoundError

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

<a id="py-00-02-section-19"></a>

## 16. FileNotFoundError

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

<a id="py-00-02-section-20"></a>

## 17. 오류 확인 절차

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

<a id="py-00-02-section-21"></a>

## 18. 오류를 숨기는 잘못된 방법

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

<a id="py-00-02-section-22"></a>

## 19. Improvements

| 피해야 할 접근 | 권장 접근 |
| --- | --- |
| 오류 메시지 일부만 확인 | 전체 Traceback 보존 |
| 코드 전체를 무작정 수정 | 실패한 최소 지점부터 확인 |
| 검색 결과를 그대로 복사 | 현재 코드와 자료형에 맞는지 검증 |
| `except:`로 모두 숨김 | 구체적인 예외 클래스 처리 |
| 오류가 사라지면 종료 | 정상 입력과 경계 입력으로 재검증 |

---

<a id="py-00-02-section-23"></a>

## 20. Common Mistakes

- Traceback의 마지막 예외를 확인하지 않습니다.
- 오류 줄만 보고 그 값을 만든 이전 코드는 확인하지 않습니다.
- `TypeError`와 `ValueError`를 같은 오류로 생각합니다.
- 인덱스와 원소 개수를 혼동합니다.
- 딕셔너리 키가 항상 존재한다고 가정합니다.
- 모든 예외를 하나의 `except:`로 처리합니다.

---

<a id="py-00-02-section-24"></a>

## 21. Interview / Review

### Q1. Traceback은 어느 방향으로 읽나요?

마지막 줄에서 예외 클래스와 상세 메시지를 먼저 확인하고 위쪽으로 올라갑니다.

### Q2. TypeError와 ValueError의 차이는 무엇인가요?

`TypeError`는 자료형이나 연산 방식이 맞지 않을 때, `ValueError`는 자료형은 사용할 수 있지만 값의 내용이 조건에 맞지 않을 때 주로 발생합니다.

<a id="index-section-39"></a>

### Q3. 딕셔너리가 세트 원소가 될 수 없는 이유는 무엇인가요?

딕셔너리는 변경 가능한 객체이며 해시 가능하지 않기 때문입니다.

---

<a id="py-00-02-section-25"></a>

## 22. Problems

### 문제 1

다음 메시지에서 예외 클래스와 상세 메시지를 구분하세요.

```text
ValueError: invalid literal for int() with base 10: 'python'
```

### 문제 2

다음 코드의 오류를 예상하세요.

```python
numbers = [1, 2, 3]
print(numbers[5])
```

### 문제 3

다음 코드가 오류를 발생시키는 이유를 설명하세요.

```python
user = {"name": "kim"}
print(user["age"])
```

---

<a id="py-00-02-section-26"></a>

## 23. Answers

### 정답 1

```text
예외 클래스: ValueError
상세 메시지: invalid literal for int() with base 10: 'python'
```

### 정답 2

```text
IndexError
```

### 정답 3

딕셔너리에 `age` 키가 없는데 대괄호로 직접 조회했기 때문에 `KeyError`가 발생합니다.

---

<a id="py-00-02-section-27"></a>

## 24. Final Checklist

- [ ] Traceback의 마지막 줄에서 예외 종류를 찾을 수 있다.
- [ ] 파일명과 줄 번호를 확인할 수 있다.
- [ ] SyntaxError와 실행 중 예외를 구분할 수 있다.
- [ ] 주요 예외 클래스의 대표 원인을 설명할 수 있다.
- [ ] `unhashable type: 'dict'`의 원인을 설명할 수 있다.

---

<a id="py-00-02-section-28"></a>

## 25. Key Summary

```text
오류 메시지는 문제 해결을 위한 정보다.
Traceback은 마지막 예외부터 확인한다.
예외 클래스와 상세 메시지를 구분한다.
오류 줄뿐 아니라 그 값을 만든 이전 코드도 확인한다.
구체적인 예외를 이해하고 최소 코드로 재현한다.
```

<a id="py-00-02-section-29"></a>

## V3 동작 백과 보강 — 오류가 만들어지고 전달되는 과정

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
