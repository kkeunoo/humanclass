# Python 조건문

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `08_Python_조건문.md` |
| 분류 | `04_Python` |
| 권장 선수 학습 | `02_Python_변수와_자료형_연산자.md`, `03_Python_문자열과_포매팅.md`, `04_Python_리스트와_컴프리헨션.md`, `07_Python_딕셔너리와_집합.md` |
| 다음 학습 | `09_Python_반복문.md` |
| 원본 기준 | `workspace_python/08_if.py`, `workspace_teacher/workspace_python/_08_if.py` |
| 핵심 범위 | 비교식, 연속 비교, `if`, 들여쓰기, 중첩 조건문, `pass`, Truthy/Falsy, `if-else`, `if-elif-else`, 입력값 검증, `match-case` |
| 보충 범위 | 조건식 평가, 논리 연산자, 단락 평가, 괄호와 줄 나눔, 자주 발생하는 오류, 조건문 선택 기준 |
| Quiz 처리 | 원본의 평균 점수 및 자판기 예제는 본문에서 분석하며, 추가 문제와 상세 풀이 문서는 최종 Quiz 단계에서 별도 제작 |

> 이 문서는 내 코드의 `08_if.py`와 강사님 코드의 `_08_if.py`를 직접 비교해 작성했습니다. 두 파일은 연속 비교식, `if`와 들여쓰기, 중첩 조건문, `pass`, Truthy/Falsy, 평균 점수 판정, 자판기 분기, `match-case`까지 거의 같은 흐름으로 구성되어 있습니다. 내 코드와 강사님 코드에서 출력 문구나 `match` 예제 값이 다른 부분은 그대로 비교하고, Python 문법과 실제 실행 결과를 기준으로 차이를 설명합니다.

---

# 학습 목표

- 조건문이 조건의 참과 거짓에 따라 실행 흐름을 나누는 문법임을 설명할 수 있다.
- 비교 연산식이 `True` 또는 `False`를 반환한다는 점을 이해한다.
- `3 < a < 20`과 같은 연속 비교식을 작성할 수 있다.
- `if 조건식:`의 기본 구조를 작성할 수 있다.
- 콜론과 들여쓰기가 조건문 블록을 결정한다는 점을 이해한다.
- 같은 들여쓰기 수준의 문장이 같은 블록에 속한다는 점을 설명할 수 있다.
- 잘못된 들여쓰기에서 `IndentationError`가 발생하는 이유를 안다.
- 조건문 안에 조건문을 작성하는 중첩 구조를 이해한다.
- 비어 있는 블록에서 `pass`를 사용할 수 있다.
- Python이 불리언이 아닌 값을 조건식에서 참 또는 거짓으로 평가할 수 있음을 안다.
- 대표적인 Falsy 값을 구분할 수 있다.
- 빈 리스트가 조건식에서 거짓으로 평가됨을 이해한다.
- `if-else`로 두 실행 경로를 구성할 수 있다.
- `if-elif-else`로 여러 조건을 순서대로 검사할 수 있다.
- `and`, `or`, `not`을 사용해 조건식을 결합할 수 있다.
- 여러 점수의 범위를 검증하고 평균에 따라 결과를 분기할 수 있다.
- 역슬래시를 이용한 명시적 줄 연결의 의미와 주의점을 이해한다.
- 괄호를 이용한 줄 나눔이 일반적으로 더 안전하다는 점을 안다.
- `match-case`의 기본 구조를 작성할 수 있다.
- 하나의 `case`에서 `|`로 여러 패턴을 묶을 수 있다.
- `case _`가 기본 분기 역할을 한다는 점을 이해한다.
- `if-elif-else`와 `match-case`의 사용 목적을 구분할 수 있다.
- 내 코드와 강사님 코드의 차이를 실행 결과 관점에서 분석할 수 있다.

---

# 1. 원본 코드

## 1.1 내 코드

```python
a = 10
b = 5
print(3 < a < 20)

if True:
    print(1)
# Indent가 들어가면 들여쓰기 오류
#  print(2) # IndentationError: unindent does not match any outer indentation level
    print(3)

    if True:
        print(4)

if True:
    pass # 아무 일도 하지 않고 넘어가는 것
else:
    pass

if 1:
    print('참')

'''
Python에서 False란?
False, None(JavaScript:null), 0, 0.0,
빈 컨테이너(비어있는 문자열, 리스트, 튜플, 딕셔너리)
'''

a = []
if a:
    print('참')
else:
    print('거짓')

# 교재 174P 문제 평균구하기
'''
국어 = int(input('국어 점수를 입력하세요: '))
영어 = int(input('영어 점수를 입력하세요: '))
수학 = int(input('수학 점수를 입력하세요: '))
과학 = int(input('과학 점수를 입력하세요: '))

result = (국어 + 영어 + 수학 + 과학) / 4

if result >= 80:
    print('합격입니다.')
else:
    print('불합격입니다.')
'''

score = input('점수 4개 입력, 띄어쓰기로 구분 : ')
print(score, score.split(' '))
scores = score.split(' ')
sum = int(scores[0]) + int(scores[1]) + int(scores[2]) + int(scores[3])
avg = sum / len(scores)

# \ 를 쓰게되면 엔터를 없앨 수 있어서, 실제 코드는 한 줄이지만 내릴 때 사용
if (0 <= int(scores[0]) <= 100) \
    and (0 <= int(scores[1]) <= 100) \
    and (0 <= int(scores[2]) <= 100) \
    and (0 <= int(scores[3]) <= 100):

    if avg >= 80:
        print('합격')
    else:
        print('불합격')
else:
    print('잘못된 입력입니다.')

# 교재 178P 자판기 문제
button = int(input('번호를 입력하세요 : '))

if button == 1:
    print('콜라')
elif button == 2:
    print('사이다')
elif button == 3:
    print('환타')
else:
    print('잘못 입력하셨습니다.')

# match, case문 / break 필요 없고 default 대신 case _ : 를 씀
# ~또는(or) 는 |로 구분해서 써줘야 함
# a = '여름'
a = 7
match a:
    case 6 | 7 | 8:
        print('봄')
    case '여름':
        print('여름')
    case _:
        print('그 외')
```

---

## 1.2 강사님 코드

```python
a = 10
b = 5
print(3 < a < 20)

if True:
    print(1)
# print(2)
    print(3)

    if True:
        print(4)

if True:
    pass
else:
    pass

if 1:
    print('참')

'''
파이썬에서 False란?
False,
None,
0, 0.0,
빈 컨테이너(비어있는 문자열, 리스트, 튜플, 딕셔너리)
'''

a = []
if a:
    print('참')
else:
    print('거짓')

# 174p. 문제 14.7
score = input('점수 4개 입력, 띄어쓰기로 구분 : ')
print(score, score.split(' '))
scores = score.split(' ')
sum = int(scores[0]) + int(scores[1]) + int(scores[2]) + int(scores[3])
avg = sum / len(scores)

if (0 <= int(scores[0]) <= 100) \
    and (0 <= int(scores[1]) <= 100) \
    and (0 <= int(scores[2]) <= 100) \
    and (0 <= int(scores[3]) <= 100):

    if avg >= 80:
        print('합격')
    else:
        print('불합격')
else:
    print('잘못된 입력')

# 178p. 1-콜라 2-사이다 3-환타 그 외-메뉴 없음
button = int(input('메뉴를 고르시오'))
if button == 1:
    print('콜라')
elif button == 2:
    print('사이다')
elif button == 3:
    print('환타')
else:
    print('다시 고르시오')

# break 필요 없음
# 또는은 | (파이프)
a = 7
match a:
    case 6 | 7 | 8:
        print('여름')
    case '여름2':
        print('여름2')
    case _:
        print('그 외')
```

---

# 2. 조건문이란?

조건문은 조건의 결과에 따라 실행할 코드를 선택하는 문법입니다.

```text
조건이 참이다
→ 지정한 코드 실행

조건이 거짓이다
→ 해당 코드를 건너뛰거나 다른 코드 실행
```

예:

```python
age = 20

if age >= 19:
    print("성인입니다.")
```

`age >= 19`가 `True`이므로 들여쓰기된 문장이 실행됩니다.

---

# 3. 조건식의 결과

조건식은 일반적으로 `True` 또는 `False`를 반환합니다.

```python
print(10 > 5)
print(10 == 5)
```

출력:

```text
True
False
```

조건문은 이 결과를 이용해 실행 여부를 결정합니다.

---

# 4. 원본의 연속 비교식

공통 원본:

```python
a = 10
b = 5
print(3 < a < 20)
```

`a`가 `3`보다 크고 동시에 `20`보다 작은지 확인합니다.

```text
3 < 10 < 20
→ True
```

변수 `b`는 선언되어 있지만 이 비교식에서는 사용되지 않습니다.

---

# 5. 연속 비교식의 의미

```python
3 < a < 20
```

은 다음 의미와 같습니다.

```python
3 < a and a < 20
```

Python에서는 수학식과 비슷한 형태로 범위를 표현할 수 있습니다.

```python
score = 85
print(0 <= score <= 100)
```

출력:

```text
True
```

---

# 6. 연속 비교식의 장점

일반적인 방식:

```python
score >= 0 and score <= 100
```

연속 비교식:

```python
0 <= score <= 100
```

두 표현은 같은 범위를 검사하지만 연속 비교식이 의도를 더 직접적으로 보여 줍니다.

---

# 7. 연속 비교식에서 경계값

```python
0 <= score <= 100
```

`<=`를 사용했으므로 `0`과 `100`도 유효합니다.

| 값 | 결과 |
| --- | --- |
| `-1` | `False` |
| `0` | `True` |
| `50` | `True` |
| `100` | `True` |
| `101` | `False` |

---

# 8. `if` 기본 구조

```python
if 조건식:
    실행문
```

예:

```python
if True:
    print(1)
```

구성 요소:

```text
if
→ 조건문 시작 키워드

조건식
→ 참 또는 거짓으로 평가되는 표현

:
→ 조건식이 끝나고 블록이 시작됨을 표시

들여쓰기된 문장
→ 조건이 참일 때 실행되는 블록
```

---

# 9. 콜론 누락

잘못된 코드:

```python
if True
    print(1)
```

`if` 조건식 뒤에는 콜론이 필요합니다.

올바른 코드:

```python
if True:
    print(1)
```

---

# 10. `if True`의 실행

공통 원본:

```python
if True:
    print(1)
    print(3)
```

조건이 항상 참이므로 두 문장이 모두 실행됩니다.

출력:

```text
1
3
```

`if True`는 조건문 구조를 확인하거나 임시 테스트를 할 때 사용할 수 있습니다.

---

# 11. `if False`의 실행

```python
if False:
    print("실행되지 않음")

print("조건문 종료")
```

출력:

```text
조건문 종료
```

조건이 거짓이면 해당 블록을 건너뜁니다.

---

# 12. Python의 들여쓰기

Python은 중괄호 대신 들여쓰기로 코드 블록을 구분합니다.

```python
if True:
    print("조건문 내부")

print("조건문 외부")
```

```text
들여쓰기 있음
→ if 블록 내부

들여쓰기 없음
→ if 블록 종료 후 외부
```

---

# 13. 같은 블록의 들여쓰기 수준

```python
if True:
    print(1)
    print(2)
    print(3)
```

세 문장의 들여쓰기 깊이가 같으므로 모두 같은 `if` 블록에 속합니다.

---

# 14. 들여쓰기 깊이가 달라지는 경우

```python
if True:
    print(1)

    if True:
        print(2)
```

두 번째 `if`는 첫 번째 `if` 안에 포함됩니다. 그 안의 `print(2)`는 한 단계 더 들여쓰기됩니다.

---

# 15. 원본의 들여쓰기 주석

내 코드:

```python
#  print(2) # IndentationError: unindent does not match any outer indentation level
```

이 주석은 들여쓰기 수준이 기존 블록과 맞지 않을 때 오류가 발생할 수 있음을 기록합니다.

대표 오류:

```text
IndentationError: unindent does not match any outer indentation level
```

---

# 16. `IndentationError`가 발생하는 이유

다음과 같은 경우 들여쓰기 오류가 발생할 수 있습니다.

```text
탭과 공백을 섞음
같은 블록의 들여쓰기 칸 수가 다름
블록이 필요한 위치에서 들여쓰기하지 않음
블록이 아닌 위치에 예상하지 못한 들여쓰기를 작성함
```

일반적으로 공백 4칸을 사용합니다.

---

# 17. 탭과 공백 혼용

화면상 같은 간격처럼 보여도 탭과 공백은 다른 문자입니다.

```text
Tab
→ 하나의 탭 문자

Space 4회
→ 네 개의 공백 문자
```

편집기에서 공백 4칸으로 통일하는 것이 안전합니다.

---

# 18. 중첩 조건문

공통 원본:

```python
if True:
    print(1)
    print(3)

    if True:
        print(4)
```

외부 조건이 참이고 내부 조건도 참이므로 다음과 같이 출력됩니다.

```text
1
3
4
```

---

# 19. 중첩 조건문의 실행 순서

```text
외부 if 검사
→ 거짓이면 내부 전체를 건너뜀
→ 참이면 외부 블록 실행
→ 내부 if 검사
→ 내부 조건 결과에 따라 내부 블록 실행
```

외부 조건이 거짓이면 내부 조건은 검사할 기회가 없습니다.

---

# 20. 중첩 조건문의 예

```python
is_member = True
age = 20

if is_member:
    if age >= 19:
        print("성인 회원")
```

두 조건이 모두 참일 때만 출력됩니다.

---

# 21. 중첩과 `and` 비교

중첩:

```python
if is_member:
    if age >= 19:
        print("성인 회원")
```

결합:

```python
if is_member and age >= 19:
    print("성인 회원")
```

두 조건을 반드시 함께 만족해야 하고 중간 단계의 별도 처리가 없다면 `and`가 더 간결할 수 있습니다.

---

# 22. 중첩이 필요한 경우

```python
if is_member:
    print("회원 확인 완료")

    if age >= 19:
        print("성인 회원")
```

첫 번째 조건이 참일 때 별도 처리를 수행한 뒤 추가 조건을 검사해야 한다면 중첩 구조가 자연스럽습니다.

---

# 23. `pass`

공통 원본:

```python
if True:
    pass
else:
    pass
```

`pass`는 아무 작업도 하지 않고 문법적으로 블록을 채우는 문장입니다.

---

# 24. `pass`가 필요한 이유

다음 코드는 실행할 문장이 없으므로 문법 오류입니다.

```python
if True:
```

임시로 블록을 비워 두려면:

```python
if True:
    pass
```

를 작성합니다.

---

# 25. `pass`의 사용 사례

```python
if condition:
    pass  # 나중에 구현
```

```python
def future_function():
    pass
```

```python
class FutureClass:
    pass
```

`pass`는 조건문 외에도 함수와 클래스의 임시 본문으로 사용할 수 있습니다.

---

# 26. `pass`는 흐름을 중단하지 않는다

```python
if True:
    pass

print("계속 실행")
```

출력:

```text
계속 실행
```

`pass`는 `break`, `continue`, `return`처럼 실행 흐름을 이동시키지 않습니다.

---

# 27. `if 1`

공통 원본:

```python
if 1:
    print('참')
```

출력:

```text
참
```

숫자 `1`은 조건식에서 참으로 평가됩니다.

---

# 28. 불리언이 아닌 조건값

Python의 `if`에는 반드시 `True` 또는 `False` 리터럴만 작성해야 하는 것은 아닙니다.

```python
if 1:
    print("참")

if "Python":
    print("참")
```

각 값은 불리언 문맥에서 참 또는 거짓으로 평가됩니다.

---

# 29. Truthy와 Falsy

```text
Truthy
→ 불리언 문맥에서 참으로 평가되는 값

Falsy
→ 불리언 문맥에서 거짓으로 평가되는 값
```

`bool()`로 평가 결과를 확인할 수 있습니다.

```python
print(bool(1))
print(bool(0))
```

출력:

```text
True
False
```

---

# 30. 대표적인 Falsy 값

원본 주석:

```text
False
None
0
0.0
빈 컨테이너
```

대표 예:

```python
False
None
0
0.0
""
[]
()
{}
set()
```

---

# 31. `None`과 JavaScript의 `null`

내 코드 주석에는 다음 표현이 있습니다.

```text
None(JavaScript:null)
```

학습 단계에서 둘 다 “값이 없음”을 나타내는 개념으로 연결해 볼 수 있지만, 서로 다른 언어의 별도 값입니다.

```text
Python
→ None

JavaScript
→ null
```

Python 코드에서는 `None`을 사용합니다.

---

# 32. 숫자의 참과 거짓

```python
print(bool(0))
print(bool(0.0))
print(bool(1))
print(bool(-1))
```

출력:

```text
False
False
True
True
```

숫자 `0`은 거짓이며, `0`이 아닌 수는 일반적으로 참입니다.

---

# 33. 문자열의 참과 거짓

```python
print(bool(""))
print(bool(" "))
print(bool("Python"))
```

출력:

```text
False
True
True
```

빈 문자열만 거짓입니다. 공백 한 칸이 들어 있는 문자열은 비어 있지 않으므로 참입니다.

---

# 34. 컨테이너의 참과 거짓

```python
print(bool([]))
print(bool([0]))
print(bool({}))
print(bool({"value": 0}))
```

출력:

```text
False
True
False
True
```

컨테이너 내부 값이 Falsy인지보다 컨테이너가 비어 있는지가 중요합니다.

---

# 35. 원본의 빈 리스트 조건

공통 원본:

```python
a = []

if a:
    print('참')
else:
    print('거짓')
```

빈 리스트는 Falsy이므로 출력은 다음과 같습니다.

```text
거짓
```

---

# 36. 빈 리스트 검사 방식

다음 두 코드는 비슷한 목적으로 사용할 수 있습니다.

```python
if len(items) > 0:
    print("데이터 있음")
```

```python
if items:
    print("데이터 있음")
```

Python에서는 컨테이너 자체를 조건식으로 사용하는 방식이 자연스럽습니다.

---

# 37. 빈 컨테이너 검사

```python
if not items:
    print("비어 있음")
```

`not`은 참과 거짓을 반대로 바꿉니다.

```text
items가 빈 리스트
→ bool(items)는 False
→ not items는 True
```

---

# 38. `if-else`

기본 구조:

```python
if 조건식:
    참일 때 실행
else:
    거짓일 때 실행
```

두 블록 중 하나만 실행됩니다.

---

# 39. `else`의 특징

`else`에는 별도의 조건식을 작성하지 않습니다.

올바른 코드:

```python
if score >= 80:
    print("합격")
else:
    print("불합격")
```

잘못된 형태:

```python
if score >= 80:
    print("합격")
else score < 80:
    print("불합격")
```

---

# 40. 두 분기의 상호 배타성

```python
if score >= 80:
    print("합격")
else:
    print("불합격")
```

```text
score >= 80이 True
→ if 블록만 실행

score >= 80이 False
→ else 블록만 실행
```

두 블록이 동시에 실행되지는 않습니다.

---

# 41. 원본의 개별 점수 입력 예제

내 코드에는 주석 처리된 예제가 있습니다.

```python
국어 = int(input('국어 점수를 입력하세요: '))
영어 = int(input('영어 점수를 입력하세요: '))
수학 = int(input('수학 점수를 입력하세요: '))
과학 = int(input('과학 점수를 입력하세요: '))

result = (국어 + 영어 + 수학 + 과학) / 4

if result >= 80:
    print('합격입니다.')
else:
    print('불합격입니다.')
```

네 과목을 각각 입력받고 평균이 `80` 이상인지 검사합니다.

---

# 42. `input()`의 반환형

```python
score = input("점수 입력: ")
print(type(score))
```

`input()`은 입력값을 문자열로 반환합니다.

```text
<class 'str'>
```

숫자 계산 전에 `int()` 또는 `float()` 변환이 필요합니다.

---

# 43. 한 줄로 여러 점수 입력

공통 원본:

```python
score = input('점수 4개 입력, 띄어쓰기로 구분 : ')
print(score, score.split(' '))
scores = score.split(' ')
```

입력 예:

```text
80 90 70 100
```

분리 결과:

```python
['80', '90', '70', '100']
```

각 요소는 아직 문자열입니다.

---

# 44. `split(' ')`

```python
scores = score.split(' ')
```

문자열을 공백 한 칸 기준으로 분리합니다.

```python
"80 90 70 100".split(' ')
```

결과:

```python
['80', '90', '70', '100']
```

---

# 45. `split()`과 `split(' ')` 차이

```python
text.split()
```

인자를 생략하면 연속된 공백을 하나의 구분처럼 처리합니다.

```python
text.split(' ')
```

공백 한 칸을 정확한 구분자로 사용하므로 연속 공백에서 빈 문자열 요소가 생길 수 있습니다.

예:

```python
text = "80  90"

print(text.split())
print(text.split(' '))
```

출력:

```text
['80', '90']
['80', '', '90']
```

사용자가 공백을 여러 번 입력할 가능성이 있다면 `split()`이 더 안정적일 수 있습니다.

---

# 46. 원본의 합계 계산

공통 원본:

```python
sum = int(scores[0]) + int(scores[1]) + int(scores[2]) + int(scores[3])
```

각 문자열 요소를 정수로 변환해 더합니다.

```text
'80' → 80
'90' → 90
'70' → 70
'100' → 100
```

---

# 47. 변수 이름 `sum`

원본은 다음 변수 이름을 사용합니다.

```python
sum = int(scores[0]) + int(scores[1]) + int(scores[2]) + int(scores[3])
```

Python에는 합계를 계산하는 내장 함수 `sum()`이 있습니다. 변수 이름으로 `sum`을 사용하면 현재 범위에서 내장 함수 이름을 가립니다.

개선 예:

```python
total = int(scores[0]) + int(scores[1]) + int(scores[2]) + int(scores[3])
```

원본 동작에는 문제가 없지만 이후 `sum()`을 사용해야 한다면 다른 변수 이름이 더 적합합니다.

---

# 48. 평균 계산

공통 원본:

```python
avg = sum / len(scores)
```

점수 합계를 점수 개수로 나눕니다.

입력이 정확히 네 개라면:

```text
(80 + 90 + 70 + 100) / 4
→ 85.0
```

`/` 연산 결과는 실수입니다.

---

# 49. 입력 개수에 대한 원본의 전제

원본은 다음 요소에 직접 접근합니다.

```python
scores[0]
scores[1]
scores[2]
scores[3]
```

따라서 점수가 네 개보다 적으면 `IndexError`가 발생할 수 있습니다.

```text
입력: 80 90 70
→ scores[3] 없음
→ IndexError
```

네 개보다 많이 입력하면 합계에는 앞의 네 개만 사용하지만 `len(scores)`에는 전체 개수가 반영되어 평균이 의도와 달라질 수 있습니다.

---

# 50. 입력 자료형에 대한 원본의 전제

```python
int(scores[0])
```

숫자로 변환할 수 없는 값이 들어오면 `ValueError`가 발생합니다.

```text
입력: 80 90 A 100
→ int('A')
→ ValueError
```

현재 원본은 점수 범위는 검사하지만 입력 개수와 숫자 변환 오류까지 처리하지는 않습니다.

---

# 51. 여러 점수의 범위 검사

공통 원본:

```python
if (0 <= int(scores[0]) <= 100) \
    and (0 <= int(scores[1]) <= 100) \
    and (0 <= int(scores[2]) <= 100) \
    and (0 <= int(scores[3]) <= 100):
```

네 점수가 모두 `0` 이상 `100` 이하인지 검사합니다.

---

# 52. `and` 연산자

```python
조건1 and 조건2
```

모든 조건이 참일 때 전체 결과가 참입니다.

| 조건 1 | 조건 2 | 결과 |
| --- | --- | --- |
| `True` | `True` | `True` |
| `True` | `False` | `False` |
| `False` | `True` | `False` |
| `False` | `False` | `False` |

네 점수 중 하나라도 범위를 벗어나면 전체 조건이 거짓입니다.

---

# 53. 점수 검사의 실행 흐름

```text
점수 4개 범위 검사
├─ 모두 0~100
│  └─ 평균 검사
│     ├─ 80 이상 → 합격
│     └─ 80 미만 → 불합격
└─ 하나라도 범위 밖
   └─ 잘못된 입력
```

범위 검사를 통과한 경우에만 평균 판정을 수행합니다.

---

# 54. 중첩 `if`를 사용한 이유

원본:

```python
if 모든_점수가_유효함:
    if avg >= 80:
        print('합격')
    else:
        print('불합격')
else:
    print('잘못된 입력')
```

첫 번째 조건은 입력값의 유효성을 검사하고, 두 번째 조건은 유효한 입력에 대해서만 합격 여부를 판단합니다.

```text
검증
→ 판정
```

의 두 단계가 중첩 구조로 표현됩니다.

---

# 55. 범위 밖 점수

입력:

```text
80 90 110 100
```

세 번째 점수의 조건:

```python
0 <= 110 <= 100
```

은 `False`입니다. `and` 전체 결과도 거짓이므로 다음 문구가 출력됩니다.

내 코드:

```text
잘못된 입력입니다.
```

강사님 코드:

```text
잘못된 입력
```

---

# 56. 평균 경계값

원본 조건:

```python
if avg >= 80:
```

`>=`를 사용하므로 평균이 정확히 `80`이어도 합격입니다.

| 평균 | 결과 |
| --- | --- |
| `79.9` | 불합격 |
| `80` | 합격 |
| `80.0` | 합격 |
| `95` | 합격 |

---

# 57. 역슬래시를 이용한 줄 연결

내 코드 주석:

```text
\ 를 쓰게되면 엔터를 없앨 수 있어서, 실제 코드는 한 줄이지만 내릴 때 사용
```

원본:

```python
if condition1 \
    and condition2 \
    and condition3:
```

줄 끝의 `\`는 다음 줄과 현재 줄을 하나의 논리적 문장으로 연결합니다.

---

# 58. 역슬래시 사용 시 주의

역슬래시 뒤에는 불필요한 문자나 공백을 두지 않는 것이 안전합니다.

```python
if condition1 \  # 주석
    and condition2:
```

처럼 작성하면 문법 문제가 발생할 수 있습니다.

---

# 59. 괄호를 이용한 줄 나눔

Python은 괄호 내부에서 자연스럽게 줄을 나눌 수 있습니다.

```python
if (
    0 <= scores[0] <= 100
    and 0 <= scores[1] <= 100
    and 0 <= scores[2] <= 100
    and 0 <= scores[3] <= 100
):
    print("유효한 점수")
```

역슬래시를 생략할 수 있고 수정 과정에서 실수할 가능성이 줄어듭니다.

---

# 60. 점수를 먼저 숫자로 변환하는 방식

원본은 비교할 때마다 `int()`를 호출합니다.

```python
int(scores[0])
int(scores[1])
```

먼저 변환하면 조건식이 단순해집니다.

```python
scores = [
    int(scores[0]),
    int(scores[1]),
    int(scores[2]),
    int(scores[3]),
]
```

이후:

```python
if (
    0 <= scores[0] <= 100
    and 0 <= scores[1] <= 100
    and 0 <= scores[2] <= 100
    and 0 <= scores[3] <= 100
):
    ...
```

---

# 61. 반복문 학습 전 단계의 코드

현재 원본은 아직 반복문 학습 전이므로 네 개의 요소를 직접 작성합니다.

```python
int(scores[0]) + int(scores[1]) + int(scores[2]) + int(scores[3])
```

다음 문서에서 반복문과 관련 함수를 학습하면 여러 점수를 더 일반적인 방식으로 처리할 수 있습니다.

```python
numbers = [int(score) for score in scores]
total = sum(numbers)
```

현재 문서에서는 원본 흐름을 기준으로 직접 인덱스 접근 방식을 이해합니다.

---

# 62. `or` 연산자

```python
조건1 or 조건2
```

하나 이상의 조건이 참이면 전체 결과가 참입니다.

| 조건 1 | 조건 2 | 결과 |
| --- | --- | --- |
| `True` | `True` | `True` |
| `True` | `False` | `True` |
| `False` | `True` | `True` |
| `False` | `False` | `False` |

예:

```python
if button == 1 or button == 2:
    print("탄산음료")
```

---

# 63. `not` 연산자

```python
not 조건식
```

조건 결과를 반대로 바꿉니다.

```python
items = []

if not items:
    print("목록이 비어 있습니다.")
```

빈 리스트는 거짓이므로 `not items`는 참입니다.

---

# 64. 논리 연산자 우선순위

일반적인 우선순위:

```text
not
→ and
→ or
```

복잡한 조건식은 괄호로 의도를 명확히 표현하는 것이 좋습니다.

```python
if is_member and (age >= 19 or has_permission):
    ...
```

---

# 65. 단락 평가

`and`와 `or`는 결과가 결정되면 나머지 표현식을 평가하지 않을 수 있습니다.

```python
value = 0

if value != 0 and 10 / value > 2:
    print("조건 만족")
```

첫 번째 조건이 거짓이므로 `10 / value`는 평가되지 않아 0으로 나누는 오류가 발생하지 않습니다.

---

# 66. `and`의 단락 평가

```text
왼쪽이 False
→ 전체 결과는 이미 False
→ 오른쪽 평가 생략 가능
```

예:

```python
user = None

if user is not None and user.get("name"):
    print(user["name"])
```

`user`가 `None`이면 오른쪽의 `get()`을 호출하지 않습니다.

---

# 67. `or`의 단락 평가

```text
왼쪽이 True
→ 전체 결과는 이미 True
→ 오른쪽 평가 생략 가능
```

예:

```python
is_admin = True

if is_admin or check_permission():
    print("접근 허용")
```

`is_admin`이 참이면 `check_permission()`은 호출되지 않을 수 있습니다.

---

# 68. `if-elif-else`

기본 구조:

```python
if 조건1:
    실행문1
elif 조건2:
    실행문2
elif 조건3:
    실행문3
else:
    기본 실행문
```

위에서부터 조건을 검사하고 처음 참이 된 한 블록만 실행합니다.

---

# 69. `elif`의 의미

`elif`는 `else if`를 줄인 Python 키워드입니다.

```text
if
→ 첫 번째 조건

elif
→ 앞 조건이 거짓일 때 검사할 추가 조건

else
→ 모든 앞 조건이 거짓일 때 실행
```

---

# 70. 원본의 자판기 예제

공통 구조:

```python
button = int(input('번호를 입력하세요 : '))

if button == 1:
    print('콜라')
elif button == 2:
    print('사이다')
elif button == 3:
    print('환타')
else:
    print('잘못 입력하셨습니다.')
```

입력 번호에 따라 하나의 메뉴를 출력합니다.

---

# 71. 자판기 실행 흐름

```text
button == 1 ?
├─ True  → 콜라
└─ False → button == 2 ?
           ├─ True  → 사이다
           └─ False → button == 3 ?
                      ├─ True  → 환타
                      └─ False → 잘못된 입력
```

---

# 72. 첫 번째 참 조건만 실행

```python
number = 10

if number > 0:
    print("양수")
elif number > 5:
    print("5보다 큼")
```

두 조건이 모두 참이지만 첫 번째 `if` 블록이 실행된 후 나머지 `elif`는 검사하지 않습니다.

출력:

```text
양수
```

---

# 73. 조건 순서의 중요성

범위를 분류할 때는 더 구체적이거나 높은 기준부터 검사해야 할 수 있습니다.

잘못된 예:

```python
score = 95

if score >= 60:
    print("통과")
elif score >= 90:
    print("우수")
```

`score >= 60`이 먼저 참이므로 `우수`는 출력되지 않습니다.

개선:

```python
if score >= 90:
    print("우수")
elif score >= 60:
    print("통과")
```

---

# 74. 여러 개의 독립 `if`

```python
number = 10

if number > 0:
    print("양수")

if number > 5:
    print("5보다 큼")
```

각 `if`는 독립적으로 검사되므로 두 문장이 모두 출력됩니다.

---

# 75. `if` 여러 개와 `elif`의 차이

```text
독립 if 여러 개
→ 모든 조건을 각각 검사
→ 여러 블록 실행 가능

if-elif-else
→ 위에서부터 검사
→ 처음 참인 한 블록만 실행
```

목적에 따라 구조를 선택해야 합니다.

---

# 76. 자판기 입력 변환 오류

원본:

```python
button = int(input('번호를 입력하세요 : '))
```

사용자가 숫자가 아닌 값을 입력하면 `int()` 변환에서 `ValueError`가 발생합니다.

```text
입력: cola
→ int('cola')
→ ValueError
```

`else`는 숫자로 변환된 뒤 메뉴 번호가 일치하지 않는 경우를 처리합니다. 숫자 변환 자체의 오류를 처리하는 문법은 예외 처리 문서에서 다룹니다.

---

# 77. 내 코드와 강사님 코드의 출력 문구 차이

| 상황 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 점수 범위 오류 | `잘못된 입력입니다.` | `잘못된 입력` |
| 자판기 기본 분기 | `잘못 입력하셨습니다.` | `다시 고르시오` |
| 자판기 입력 안내 | `번호를 입력하세요 : ` | `메뉴를 고르시오` |

문법과 분기 구조는 같고 사용자에게 보여 주는 문구만 다릅니다.

---

# 78. `match-case`

기본 구조:

```python
match 값:
    case 패턴1:
        실행문1
    case 패턴2:
        실행문2
    case _:
        기본 실행문
```

`match` 대상 값을 각 `case` 패턴과 비교해 일치하는 분기를 실행합니다.

---

# 79. 원본의 `match-case`

내 코드:

```python
a = 7

match a:
    case 6 | 7 | 8:
        print('봄')
    case '여름':
        print('여름')
    case _:
        print('그 외')
```

강사님 코드:

```python
a = 7

match a:
    case 6 | 7 | 8:
        print('여름')
    case '여름2':
        print('여름2')
    case _:
        print('그 외')
```

---

# 80. `match` 대상

```python
match a:
```

변수 `a`의 값을 각 `case` 패턴과 비교합니다.

현재 값:

```python
a = 7
```

따라서 숫자 `7`과 일치하는 패턴을 찾습니다.

---

# 81. `|`를 사용한 OR 패턴

공통 원본:

```python
case 6 | 7 | 8:
```

숫자 `6`, `7`, `8` 중 하나와 일치하면 해당 블록이 실행됩니다.

```text
6 또는 7 또는 8
```

조건식의 논리 연산자 `or`가 아니라 패턴을 묶는 `|`를 사용합니다.

---

# 82. `case`에서 `or`를 사용할 수 없는 형태

다음은 원본 의도에 맞는 패턴 문법이 아닙니다.

```python
case 6 or 7 or 8:
```

여러 대안 패턴을 묶을 때는:

```python
case 6 | 7 | 8:
```

를 사용합니다.

---

# 83. `case _`

공통 원본:

```python
case _:
    print('그 외')
```

앞의 어떤 패턴에도 일치하지 않을 때 실행되는 기본 분기입니다.

`if-elif-else`의 `else`와 비슷한 역할을 합니다.

---

# 84. `case _`의 위치

기본 분기는 마지막에 작성합니다.

```python
match value:
    case 1:
        print("하나")
    case 2:
        print("둘")
    case _:
        print("그 외")
```

`_`는 모든 값과 일치하는 와일드카드 패턴이므로 앞에 두면 뒤 패턴이 의미를 잃습니다.

---

# 85. `match-case`에는 `break`가 필요 없다

원본 주석:

```text
break 필요 없음
```

Python의 `match-case`는 일치한 하나의 `case` 블록을 실행한 뒤 자동으로 다음 `case`까지 이어서 실행하지 않습니다.

```python
match 1:
    case 1:
        print("하나")
    case 2:
        print("둘")
```

출력:

```text
하나
```

---

# 86. `case`와 자료형

숫자 `7`과 문자열 `'7'`은 다른 값입니다.

```python
value = 7

match value:
    case '7':
        print("문자열")
    case 7:
        print("정수")
```

출력:

```text
정수
```

원본에서도 숫자 패턴과 문자열 패턴을 구분합니다.

---

# 87. 내 코드의 계절 출력

내 코드:

```python
case 6 | 7 | 8:
    print('봄')
```

값 `a`가 `7`이므로 실제 출력은:

```text
봄
```

입니다.

다만 일반적인 계절 구분에서 `6`, `7`, `8`은 여름으로 분류하는 경우가 많고 강사님 코드는 `여름`을 출력합니다. 따라서 내 코드의 `봄`은 문법 오류는 아니지만 예제 의미상 오타로 보입니다.

---

# 88. 강사님 코드의 계절 출력

강사님 코드:

```python
case 6 | 7 | 8:
    print('여름')
```

`a = 7`이므로 출력은:

```text
여름
```

입니다.

패턴과 출력 의미가 서로 일치합니다.

---

# 89. 문자열 패턴 차이

내 코드:

```python
case '여름':
    print('여름')
```

강사님 코드:

```python
case '여름2':
    print('여름2')
```

현재 `a`는 정수 `7`이므로 두 문자열 패턴은 실행되지 않습니다. 각 파일에서 문자열 패턴도 사용할 수 있음을 보여 주는 별도 예입니다.

---

# 90. `if-elif-else`로 같은 로직 작성

```python
a = 7

if a == 6 or a == 7 or a == 8:
    print('여름')
elif a == '여름2':
    print('여름2')
else:
    print('그 외')
```

단순한 값 일치 분기는 `if-elif-else`와 `match-case` 모두로 표현할 수 있습니다.

---

# 91. 멤버십 연산자를 사용한 표현

```python
a = 7

if a in (6, 7, 8):
    print('여름')
elif a == '여름2':
    print('여름2')
else:
    print('그 외')
```

여러 값 중 하나인지 검사할 때 `in`을 사용할 수도 있습니다.

---

# 92. `if`가 적합한 경우

다음과 같은 조건은 `if`가 자연스럽습니다.

```python
if score >= 80:
    print("합격")
```

```python
if 0 <= score <= 100 and is_submitted:
    print("처리")
```

```text
범위 비교
부등식
여러 논리 조건 결합
함수 호출 결과 검사
```

---

# 93. `match-case`가 적합한 경우

하나의 값을 여러 명확한 패턴과 비교할 때 읽기 좋을 수 있습니다.

```python
match command:
    case "start":
        print("시작")
    case "stop":
        print("정지")
    case "pause":
        print("일시 정지")
    case _:
        print("알 수 없는 명령")
```

---

# 94. 조건식에서 대입과 비교 구분

잘못된 코드:

```python
if button = 1:
    print("콜라")
```

비교에는 `==`를 사용합니다.

```python
if button == 1:
    print("콜라")
```

```text
=
→ 대입

==
→ 값이 같은지 비교
```

---

# 95. 문자열과 숫자 비교

```python
button = input("번호: ")

if button == 1:
    print("콜라")
```

`input()` 결과는 문자열이므로 문자열 `'1'`과 정수 `1`은 같지 않습니다.

방법 1:

```python
button = int(input("번호: "))
if button == 1:
    ...
```

방법 2:

```python
button = input("번호: ")
if button == '1':
    ...
```

---

# 96. `True`와 문자열 `'True'`

```python
print(bool('False'))
```

출력:

```text
True
```

문자열 내용이 `False`라는 단어여도 비어 있지 않은 문자열이므로 Truthy입니다.

```text
False
→ 불리언 거짓

'False'
→ 비어 있지 않은 문자열, 참
```

---

# 97. `None` 비교

`None` 여부를 확인할 때는 일반적으로 `is`를 사용합니다.

```python
value = None

if value is None:
    print("값이 없음")
```

반대 조건:

```python
if value is not None:
    print("값이 있음")
```

---

# 98. 조건문 블록 밖의 변수

```python
score = 90

if score >= 80:
    result = "합격"

print(result)
```

현재 값에서는 실행되지만, 조건이 거짓이면 `result`가 생성되지 않아 오류가 발생할 수 있습니다.

안전한 방식:

```python
result = "불합격"

if score >= 80:
    result = "합격"

print(result)
```

또는:

```python
if score >= 80:
    result = "합격"
else:
    result = "불합격"
```

---

# 99. 조건식이 너무 길 때

복잡한 조건식을 한 줄에 모두 작성하면 읽기 어려울 수 있습니다.

```python
is_valid_score = (
    0 <= score1 <= 100
    and 0 <= score2 <= 100
    and 0 <= score3 <= 100
    and 0 <= score4 <= 100
)

if is_valid_score:
    ...
```

조건의 의미를 변수 이름으로 표현하면 본문이 명확해집니다.

---

# 100. 중첩 깊이 줄이기

중첩이 지나치게 깊으면 실행 흐름을 추적하기 어려워집니다.

```python
if condition1:
    if condition2:
        if condition3:
            print("실행")
```

모든 조건이 같은 수준의 필수 조건이라면:

```python
if condition1 and condition2 and condition3:
    print("실행")
```

처럼 정리할 수 있습니다.

---

# 101. 조건문의 실행 순서 확인

```python
print("1")

if True:
    print("2")

print("3")
```

출력:

```text
1
2
3
```

조건문도 프로그램의 위에서 아래 실행 흐름 안에서 평가됩니다.

---

# 102. 조건문 안의 출력과 괄호

내 코드의 주석 처리 예에는 다음 형태가 있습니다.

```python
(print('합격입니다.'))
```

바깥 괄호는 불필요합니다.

```python
print('합격입니다.')
```

로 작성해도 같은 결과입니다.

---

# 103. 자주 하는 실수: 콜론 누락

```python
if score >= 80
    print("합격")
```

개선:

```python
if score >= 80:
    print("합격")
```

---

# 104. 자주 하는 실수: 블록 들여쓰기 누락

```python
if score >= 80:
print("합격")
```

개선:

```python
if score >= 80:
    print("합격")
```

---

# 105. 자주 하는 실수: `else` 정렬 오류

잘못된 예:

```python
if score >= 80:
    print("합격")
    else:
        print("불합격")
```

`else`는 연결되는 `if`와 같은 들여쓰기 수준이어야 합니다.

```python
if score >= 80:
    print("합격")
else:
    print("불합격")
```

---

# 106. 자주 하는 실수: 조건 순서 오류

```python
if score >= 60:
    print("통과")
elif score >= 90:
    print("우수")
```

높은 점수도 첫 번째 조건에서 처리됩니다.

개선:

```python
if score >= 90:
    print("우수")
elif score >= 60:
    print("통과")
else:
    print("재시험")
```

---

# 107. 자주 하는 실수: 범위 조건에 `or` 사용

잘못된 의도:

```python
if score >= 0 or score <= 100:
    print("유효")
```

대부분의 숫자에서 둘 중 하나는 참이므로 범위 검사가 되지 않습니다.

개선:

```python
if score >= 0 and score <= 100:
    print("유효")
```

또는:

```python
if 0 <= score <= 100:
    print("유효")
```

---

# 108. 자주 하는 실수: `or` 축약 오류

잘못된 코드:

```python
if button == 1 or 2:
    print("선택")
```

`2` 자체가 Truthy이므로 조건이 항상 참처럼 동작합니다.

개선:

```python
if button == 1 or button == 2:
    print("선택")
```

또는:

```python
if button in (1, 2):
    print("선택")
```

---

# 109. 자주 하는 실수: 빈 리스트와 `None` 혼동

```python
value = []

if value is None:
    print("값 없음")
```

빈 리스트는 `None`이 아닙니다.

```text
value is None
→ 정확히 None인지 확인

not value
→ Falsy인지 확인
```

목적에 따라 구분합니다.

---

# 110. 자주 하는 실수: 문자열 숫자 범위 비교

```python
score = input("점수: ")

if 0 <= score <= 100:
    ...
```

문자열과 정수는 이 방식으로 크기를 비교할 수 없습니다.

개선:

```python
score = int(input("점수: "))

if 0 <= score <= 100:
    ...
```

---

# 111. 자주 하는 실수: 입력 개수 미검사

원본 방식은 네 개의 입력을 전제로 합니다.

```python
scores[3]
```

최소한 개수를 먼저 확인하려면:

```python
if len(scores) == 4:
    print("점수 개수 정상")
else:
    print("점수 4개를 입력해야 합니다.")
```

다만 숫자 변환 가능 여부는 별도로 확인해야 합니다.

---

# 112. 자주 하는 실수: 내장 함수 이름 사용

```python
sum = 100
```

이후:

```python
sum([1, 2, 3])
```

을 호출할 수 없게 됩니다.

대안:

```python
total = 100
```

---

# 113. 자주 하는 실수: `match`에서 `or` 사용

```python
match value:
    case 1 or 2:
        print("하나 또는 둘")
```

대안 패턴은 파이프를 사용합니다.

```python
match value:
    case 1 | 2:
        print("하나 또는 둘")
```

---

# 114. 자주 하는 실수: `case _` 누락

`case _`는 필수는 아니지만 일치하지 않는 값을 처리해야 한다면 작성하는 것이 좋습니다.

```python
match command:
    case "start":
        print("시작")
    case _:
        print("지원하지 않는 명령")
```

누락하면 어떤 패턴에도 일치하지 않을 때 아무 블록도 실행되지 않습니다.

---

# 115. 자주 하는 실수: `match-case`의 계절 문구 불일치

내 코드:

```python
case 6 | 7 | 8:
    print('봄')
```

Python 문법상 정상 실행되지만 숫자 패턴과 출력 의미를 함께 검토해야 합니다. 강사님 코드처럼:

```python
case 6 | 7 | 8:
    print('여름')
```

이 예제의 의도에 더 잘 맞습니다.

---

# 116. 조건문 작성 순서

조건문을 작성할 때 다음 순서로 생각할 수 있습니다.

```text
1. 무엇을 판단할지 정한다.
2. 조건식의 참과 거짓을 확인한다.
3. 참일 때 실행할 코드를 작성한다.
4. 거짓일 때 처리가 필요한지 결정한다.
5. 여러 분기가 있다면 우선순위를 정한다.
6. 경계값을 확인한다.
7. 입력 자료형과 오류 가능성을 확인한다.
```

---

# 117. 경계값 확인

```python
if avg >= 80:
```

다음 값을 직접 확인합니다.

```text
79
80
81
```

범위 조건:

```python
0 <= score <= 100
```

에서는 다음 값을 확인합니다.

```text
-1
0
100
101
```

경계값 테스트는 비교 연산자 실수를 찾는 데 유용합니다.

---

# 118. 조건문과 데이터 검증

원본 평균 예제는 다음 두 역할을 분리합니다.

```text
입력 검증
→ 점수가 0~100인지 확인

업무 판정
→ 평균이 80 이상인지 확인
```

유효하지 않은 데이터로 결과를 계산하지 않도록 먼저 검증하는 구조입니다.

---

# 119. 조건문의 결과를 변수에 저장

```python
if avg >= 80:
    result = "합격"
else:
    result = "불합격"

print(result)
```

분기마다 직접 출력하는 대신 결과를 변수에 저장한 뒤 공통 출력할 수 있습니다.

---

# 120. 조건 표현식

간단한 두 값 선택은 조건 표현식으로 작성할 수도 있습니다.

```python
result = "합격" if avg >= 80 else "불합격"
```

기본 구조:

```python
참일_때_값 if 조건식 else 거짓일_때_값
```

복잡한 로직에는 일반 `if-else`가 더 읽기 좋습니다.

---

# 121. 조건 표현식과 일반 조건문 비교

일반 조건문:

```python
if avg >= 80:
    result = "합격"
else:
    result = "불합격"
```

조건 표현식:

```python
result = "합격" if avg >= 80 else "불합격"
```

단순한 값 선택에는 조건 표현식이 간결하지만 여러 실행문을 포함해야 한다면 일반 조건문을 사용합니다.

---

# 122. 복습 질문 1

## 조건문이란 무엇인가?

조건문은 조건식의 평가 결과에 따라 특정 코드 블록을 실행하거나 건너뛰도록 프로그램의 실행 흐름을 나누는 문법입니다.

---

# 123. 복습 질문 2

## Python에서 코드 블록은 어떻게 구분하는가?

콜론 뒤에 작성되는 들여쓰기 수준으로 구분합니다. 같은 수준으로 들여쓰기된 문장들이 같은 블록에 속합니다.

---

# 124. 복습 질문 3

## `3 < a < 20`은 무엇을 의미하는가?

`a`가 `3`보다 크고 `20`보다 작은지 동시에 확인하는 연속 비교식입니다. `3 < a and a < 20`과 같은 의미입니다.

---

# 125. 복습 질문 4

## Falsy 값의 대표 예는 무엇인가?

`False`, `None`, 숫자 `0`, `0.0`, 빈 문자열, 빈 리스트, 빈 튜플, 빈 딕셔너리, 빈 집합 등이 있습니다.

---

# 126. 복습 질문 5

## `pass`는 무엇을 하는가?

아무 동작도 하지 않습니다. 문법적으로 실행문이 필요한 블록을 임시로 비워 둘 때 사용합니다.

---

# 127. 복습 질문 6

## `if-elif-else`에서 여러 조건이 참이면 어떻게 되는가?

위에서부터 검사해 처음 참이 된 블록 하나만 실행하고 나머지 분기는 건너뜁니다.

---

# 128. 복습 질문 7

## `and`와 `or`의 차이는 무엇인가?

`and`는 모든 조건이 참일 때 참이고, `or`는 하나 이상의 조건이 참일 때 참입니다.

---

# 129. 복습 질문 8

## `case 6 | 7 | 8`은 무엇을 의미하는가?

`match` 대상이 `6`, `7`, `8` 중 하나와 일치할 때 해당 `case` 블록을 실행한다는 의미입니다.

---

# 130. 복습 질문 9

## `case _`는 어떤 역할을 하는가?

앞의 어떤 패턴에도 일치하지 않는 나머지 모든 값을 처리하는 기본 분기입니다.

---

# 131. 복습 질문 10

## `match-case`에서 `break`가 필요하지 않은 이유는 무엇인가?

일치한 하나의 `case` 블록을 실행한 뒤 다른 `case` 블록으로 자동 진행하지 않기 때문입니다.

---

# 132. My Code vs Teacher Code

## 132.1 전체 흐름 비교

| 항목 | 내 코드 | 강사님 코드 | 분석 |
| --- | --- | --- | --- |
| 연속 비교 | `3 < a < 20` | 동일 | 같은 범위 비교 예제 |
| 기본 `if` | `if True` | 동일 | 들여쓰기 블록 확인 |
| 들여쓰기 주석 | 구체적인 `IndentationError` 기록 | `print(2)`만 주석 처리 | 내 코드가 오류 원인을 더 상세히 기록 |
| 중첩 `if` | 포함 | 포함 | 같은 실행 흐름 |
| `pass` | 설명 주석 포함 | 주석 없음 | 동작은 동일 |
| Truthy/Falsy | `None(JavaScript:null)` 비교 설명 | Python 값만 나열 | 내 코드가 JavaScript와 연결해 기록 |
| 빈 리스트 | `a = []` | 동일 | 둘 다 `거짓` 출력 |
| 개별 과목 입력 | 주석 처리 예제 포함 | 없음 | 내 코드에만 이전 풀이 흔적 존재 |
| 한 줄 점수 입력 | 포함 | 포함 | 구조 동일 |
| 범위 검증 | 연속 비교와 `and` | 동일 | 구조 동일 |
| 평균 판정 | `80` 이상 합격 | 동일 | 구조 동일 |
| 오류 문구 | `잘못된 입력입니다.` | `잘못된 입력` | 출력 문구만 다름 |
| 자판기 입력 문구 | `번호를 입력하세요` | `메뉴를 고르시오` | 안내 문구 차이 |
| 자판기 기본 문구 | `잘못 입력하셨습니다.` | `다시 고르시오` | 출력 문구 차이 |
| `match` 숫자 패턴 | `6 | 7 | 8` | 동일 | 같은 OR 패턴 |
| 숫자 패턴 출력 | `봄` | `여름` | 내 코드가 예제 의미상 오타로 보임 |
| 문자열 패턴 | `'여름'` | `'여름2'` | 서로 다른 테스트 문자열 |
| 기본 패턴 | `case _` | 동일 | 같은 기본 분기 |

---

## 132.2 공통적으로 잘 작성된 부분

두 파일은 다음 핵심 개념을 같은 순서로 학습합니다.

```text
비교식
→ if 기본 구조
→ 들여쓰기
→ 중첩 if
→ pass
→ Truthy/Falsy
→ if-else
→ 입력값 검증
→ if-elif-else
→ match-case
```

단순 문법 확인에서 실제 입력 예제로 자연스럽게 확장됩니다.

---

## 132.3 내 코드에서 보강된 부분

내 코드에는 다음 설명이 추가되어 있습니다.

```text
들여쓰기 오류 메시지
pass의 의미
None과 JavaScript null의 연결
개별 과목 입력 방식
역슬래시 줄 연결 설명
match-case의 default 역할
|를 이용한 OR 패턴 설명
```

수업 중 이해한 내용을 주석으로 정리한 흔적입니다.

---

## 132.4 강사님 코드에서 확인되는 기준

강사님 코드는 다음 결과를 명확히 보여 줍니다.

```python
case 6 | 7 | 8:
    print('여름')
```

숫자 `6`, `7`, `8`과 계절 출력이 자연스럽게 연결됩니다. 내 코드의 `봄`은 Python 실행에는 문제가 없지만 강사님 원본과 예제 의미를 기준으로 수정할 수 있습니다.

---

## 132.5 원본에서 공통으로 전제하는 사항

점수 예제는 다음 입력을 전제로 합니다.

```text
정확히 네 개의 값 입력
각 값은 int()로 변환 가능
공백 한 칸으로 구분
```

따라서 다음 상황은 현재 원본 범위를 넘어섭니다.

```text
점수 개수 부족 또는 초과
문자 입력
연속 공백 입력
빈 입력
```

현재 문서에서는 원본 동작을 우선 이해하고, 이러한 제한도 함께 기록합니다.

---

# 133. Problems

## 문제 1

변수 `age`가 `19` 이상이면 `성인입니다.`를 출력하는 조건문을 작성하세요.

---

## 문제 2

변수 `number`가 양수이면 `양수`, 그렇지 않으면 `0 또는 음수`를 출력하세요.

---

## 문제 3

변수 `score`가 `0` 이상 `100` 이하인지 연속 비교식으로 검사하세요.

---

## 문제 4

빈 리스트 `items = []`를 조건식으로 사용해 `비어 있음`을 출력하세요.

---

## 문제 5

변수 `score`가 `90` 이상이면 `A`, `80` 이상이면 `B`, `70` 이상이면 `C`, 그 외에는 `D`를 출력하세요.

---

## 문제 6

변수 `button`이 `1`이면 `콜라`, `2`이면 `사이다`, `3`이면 `환타`, 그 외에는 `메뉴 없음`을 출력하세요.

---

## 문제 7

변수 `month`가 `6`, `7`, `8` 중 하나이면 `여름`을 출력하도록 `match-case`를 작성하세요.

---

## 문제 8

다음 코드가 항상 참처럼 동작하는 이유를 설명하고 수정하세요.

```python
if button == 1 or 2:
    print("선택")
```

---

## 문제 9

다음 점수 범위 검사가 잘못된 이유를 설명하고 수정하세요.

```python
if score >= 0 or score <= 100:
    print("유효")
```

---

## 문제 10

`pass`를 사용해 아직 구현하지 않은 `if` 블록을 문법 오류 없이 작성하세요.

---

## 문제 11

다음 입력을 공백 기준으로 나누고 네 점수의 평균을 계산하세요.

```text
80 90 70 100
```

---

## 문제 12

네 점수가 모두 `0` 이상 `100` 이하일 때만 평균을 판정하도록 중첩 조건문을 작성하세요. 평균이 `80` 이상이면 합격입니다.

---

## 문제 13

`case _`의 역할을 한 문장으로 설명하세요.

---

## 문제 14

독립된 `if` 두 개와 `if-elif` 구조의 실행 차이를 설명하세요.

---

## 문제 15

다음 코드에서 `score = 95`일 때 `우수`가 출력되지 않는 이유를 설명하고 조건 순서를 수정하세요.

```python
if score >= 60:
    print("통과")
elif score >= 90:
    print("우수")
```

> 위 문제들의 상세 정답과 해설은 전체 Python 학습 문서가 완성된 뒤 `04_Python/Quiz/` 문서에서 별도로 정리합니다.

---

# 134. Final Checklist

- [ ] 조건문이 실행 흐름을 분기하는 문법임을 설명할 수 있다.
- [ ] 조건식이 참 또는 거짓으로 평가됨을 안다.
- [ ] 비교 연산식의 결과가 `bool`임을 확인할 수 있다.
- [ ] `3 < a < 20` 형태의 연속 비교식을 이해한다.
- [ ] 연속 비교식과 `and` 결합식의 관계를 설명할 수 있다.
- [ ] 범위 조건에서 경계값 포함 여부를 구분할 수 있다.
- [ ] `if 조건식:`의 기본 구조를 작성할 수 있다.
- [ ] 조건식 뒤에 콜론이 필요함을 안다.
- [ ] Python이 들여쓰기로 블록을 구분함을 설명할 수 있다.
- [ ] 같은 블록에서 들여쓰기 수준을 통일할 수 있다.
- [ ] 탭과 공백 혼용이 오류를 만들 수 있음을 안다.
- [ ] `IndentationError`가 발생하는 대표 원인을 설명할 수 있다.
- [ ] 중첩 `if`를 작성할 수 있다.
- [ ] 외부 조건이 거짓이면 내부 조건문도 실행되지 않음을 안다.
- [ ] 중첩 조건문과 `and` 결합 조건을 구분해 사용할 수 있다.
- [ ] `pass`의 역할을 설명할 수 있다.
- [ ] `pass`가 실행 흐름을 중단하지 않음을 안다.
- [ ] `if 1`이 참으로 평가되는 이유를 안다.
- [ ] Truthy와 Falsy의 의미를 설명할 수 있다.
- [ ] `False`, `None`, `0`, `0.0`이 Falsy임을 안다.
- [ ] 빈 문자열과 빈 컨테이너가 Falsy임을 안다.
- [ ] 비어 있지 않은 컨테이너가 내부 값과 관계없이 Truthy일 수 있음을 안다.
- [ ] 빈 리스트를 `if items:` 방식으로 검사할 수 있다.
- [ ] `not items`로 빈 컨테이너를 검사할 수 있다.
- [ ] `None`과 빈 컨테이너가 서로 다른 값임을 안다.
- [ ] `if-else`로 두 경로를 구성할 수 있다.
- [ ] `else`에는 조건식을 작성하지 않음을 안다.
- [ ] `if`와 `else` 중 하나만 실행됨을 안다.
- [ ] `input()`이 문자열을 반환함을 안다.
- [ ] 숫자 계산 전에 `int()` 변환이 필요함을 안다.
- [ ] `split(' ')`으로 공백 기준 문자열을 나눌 수 있다.
- [ ] `split()`과 `split(' ')`의 차이를 설명할 수 있다.
- [ ] 리스트 요소를 인덱스로 조회할 수 있다.
- [ ] 입력 개수 부족에서 `IndexError`가 발생할 수 있음을 안다.
- [ ] 숫자 변환 불가 입력에서 `ValueError`가 발생할 수 있음을 안다.
- [ ] 변수 이름 `sum`이 내장 함수 이름을 가릴 수 있음을 안다.
- [ ] 합계와 평균을 계산할 수 있다.
- [ ] `/` 연산 결과가 실수임을 안다.
- [ ] `and`로 여러 필수 조건을 결합할 수 있다.
- [ ] `or`로 여러 대안 조건을 결합할 수 있다.
- [ ] `not`으로 조건 결과를 반대로 바꿀 수 있다.
- [ ] `and`, `or`, `not`의 기본 우선순위를 안다.
- [ ] 단락 평가의 의미를 이해한다.
- [ ] 네 점수의 유효 범위를 검사할 수 있다.
- [ ] 입력 검증 후 업무 판정을 수행하는 구조를 이해한다.
- [ ] 평균 `80`이 합격에 포함됨을 확인할 수 있다.
- [ ] 역슬래시를 이용한 명시적 줄 연결을 이해한다.
- [ ] 괄호 안에서 더 안전하게 줄을 나눌 수 있음을 안다.
- [ ] `if-elif-else`의 기본 구조를 작성할 수 있다.
- [ ] `elif` 조건을 위에서부터 검사함을 안다.
- [ ] 처음 참이 된 분기 하나만 실행됨을 안다.
- [ ] 여러 독립 `if`는 각각 검사된다는 점을 안다.
- [ ] 조건 순서가 결과에 영향을 줄 수 있음을 안다.
- [ ] 자판기 메뉴 분기를 작성할 수 있다.
- [ ] `=`와 `==`의 차이를 구분할 수 있다.
- [ ] 문자열 숫자와 정수 숫자를 구분할 수 있다.
- [ ] `button == 1 or 2`가 잘못된 이유를 설명할 수 있다.
- [ ] 범위 검사에 잘못된 `or`를 사용하면 안 되는 이유를 안다.
- [ ] `match-case`의 기본 구조를 작성할 수 있다.
- [ ] `match` 대상과 `case` 패턴의 관계를 설명할 수 있다.
- [ ] `case 6 | 7 | 8` 형태의 OR 패턴을 작성할 수 있다.
- [ ] `case` 패턴에서 `or` 대신 `|`를 사용함을 안다.
- [ ] `case _`가 기본 분기임을 안다.
- [ ] `match-case`에 `break`가 필요하지 않음을 안다.
- [ ] 숫자 패턴과 문자열 패턴을 구분할 수 있다.
- [ ] `if-elif-else`와 `match-case`의 사용 목적을 비교할 수 있다.
- [ ] 내 코드의 `6 | 7 | 8 → 봄`이 문법 오류가 아닌 의미상 오타임을 설명할 수 있다.
- [ ] 내 코드와 강사님 코드의 출력 문구 차이를 구분할 수 있다.
- [ ] 원본 점수 예제가 전제하는 입력 형식을 설명할 수 있다.
- [ ] 조건문의 경계값을 테스트할 수 있다.
- [ ] 복잡한 조건식을 의미 있는 변수로 분리할 수 있다.
- [ ] 지나치게 깊은 중첩을 논리 연산자로 줄일 수 있다.
- [ ] 간단한 값 선택에서 조건 표현식을 사용할 수 있다.
- [ ] 추가 문제의 상세 풀이가 최종 Quiz 문서에서 진행됨을 확인했다.

---

# 135. Key Summary

조건문의 기본 구조:

```python
if condition:
    print("조건이 참일 때 실행")
```

두 경로:

```python
if condition:
    print("참")
else:
    print("거짓")
```

여러 분기:

```python
if condition1:
    print("첫 번째")
elif condition2:
    print("두 번째")
else:
    print("기본")
```

연속 비교:

```python
0 <= score <= 100
```

```text
0 이상이고 100 이하
```

논리 연산자:

```python
condition1 and condition2
condition1 or condition2
not condition
```

```text
and
→ 모든 조건이 참

or
→ 하나 이상 참

not
→ 참과 거짓 반전
```

대표 Falsy 값:

```python
False
None
0
0.0
""
[]
()
{}
set()
```

빈 리스트 검사:

```python
items = []

if items:
    print("데이터 있음")
else:
    print("비어 있음")
```

중첩 조건문:

```python
if is_valid:
    if avg >= 80:
        print("합격")
    else:
        print("불합격")
else:
    print("잘못된 입력")
```

점수 범위 검사:

```python
if (
    0 <= score1 <= 100
    and 0 <= score2 <= 100
    and 0 <= score3 <= 100
    and 0 <= score4 <= 100
):
    print("유효한 점수")
```

`pass`:

```python
if condition:
    pass
```

```text
아무 동작도 하지 않음
문법적으로 빈 블록을 채움
```

`match-case`:

```python
match value:
    case 1:
        print("하나")
    case 2 | 3:
        print("둘 또는 셋")
    case _:
        print("그 외")
```

```text
|
→ 여러 대안 패턴

case _
→ 기본 분기

break
→ 필요 없음
```

원본 핵심 흐름:

```text
비교식
→ if
→ 들여쓰기
→ 중첩 if
→ pass
→ Truthy/Falsy
→ if-else
→ 입력값 검증
→ if-elif-else
→ match-case
```

조건문은 단순히 코드를 나누는 문법이 아니라, 데이터가 유효한지 확인하고 상황에 맞는 하나의 실행 경로를 선택하는 도구입니다. 조건의 범위, 자료형, 검사 순서, 경계값을 함께 확인해야 의도한 결과를 만들 수 있습니다.
