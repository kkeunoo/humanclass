---
title: Python 예외 처리
version: v2.0-final
last_updated: 2026-08-06
status: Completed
---

# Python 예외 처리

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `14_Python_예외처리.md` |
| 분류 | `04_Python` |
| 권장 선수 학습 | `08_Python_조건문.md`, `11_Python_함수.md`, `12_Python_클래스.md`, `13_Python_상속과_다형성.md` |
| 다음 학습 | `15_Python_모듈과_import.md` |
| 원본 기준 | `workspace_python/14_try.py`, `workspace_teacher/workspace_python/_14_try.py` |
| 핵심 범위 | `try`, `except`, 예외 종류별 처리, `as e`, `Exception`, `else`, `finally`, `raise`, 사용자 정의 오류 흐름, `traceback` |
| 실습 범위 | 나눗셈 함수, 로그인 검증, 예외 메시지 확인, 오류 추적 |
| 확장 문서 | 이터레이터·제너레이터·정규표현식은 `16~18`번에서 별도 정리 |
| 종합 실습 | 별도 문서 `20_Python_종합실습.md`에서 관리 |
| 문서 형식 | Python Developer-Wiki V2 확정 형식 |

> 이 문서는 내 코드와 강사님 코드 전체를 한 번에 나열하지 않는다.  
> 각 예외 처리 개념에 필요한 부분만 발췌하고, 실행 결과·코드 사용 목적·주의점·개선 방향을 함께 설명한다.

---

# 개요

프로그램은 실행 중 예상하지 못한 값이나 상황을 만날 수 있다.

예:

- 숫자를 `0`으로 나누는 경우
- 숫자가 필요한 곳에 문자열이 들어온 경우
- 존재하지 않는 파일을 여는 경우
- 필수 입력값이 비어 있는 경우
- 네트워크 연결이 실패한 경우

이때 오류를 처리하지 않으면 프로그램이 중단될 수 있다.

```text
오류 발생
    ↓
처리 코드 없음
    ↓
프로그램 중단
```

예외 처리를 사용하면 오류가 발생해도 프로그램 전체가 바로 종료되지 않도록 대응할 수 있다.

```text
오류 발생
    ↓
except에서 예외 처리
    ↓
안내 메시지 출력 또는 대체 동작
    ↓
프로그램 계속 실행
```

> [!IMPORTANT]
> 예외 처리는 오류를 숨기는 기능이 아니다.
>
> 오류가 발생했을 때 **어떤 상황인지 확인하고, 적절한 대응을 실행하기 위한 기능**이다.

---

# 핵심 개념

| 개념 | 핵심 역할 |
| --- | --- |
| 예외(Exception) | 프로그램 실행 중 발생하는 비정상 상황 |
| `try` | 예외가 발생할 수 있는 코드를 실행 |
| `except` | 발생한 예외를 처리 |
| `else` | 예외가 발생하지 않았을 때 실행 |
| `finally` | 예외 발생 여부와 관계없이 실행 |
| `raise` | 개발자가 직접 예외를 발생시킴 |
| `as e` | 발생한 예외 객체를 변수에 저장 |
| `traceback` | 오류가 발생한 전체 호출 경로 확인 |

---

# 학습 목표

이 문서를 학습한 뒤 다음 내용을 설명하고 작성할 수 있어야 한다.

- 오류와 예외의 의미를 구분해 설명할 수 있다.
- 조건문으로 오류를 방지하는 방식의 한계를 이해한다.
- `try`와 `except`의 기본 구조를 작성할 수 있다.
- `ZeroDivisionError`, `TypeError` 등 예외 종류별로 처리할 수 있다.
- 여러 `except`문의 실행 순서를 이해한다.
- `as e`로 예외 메시지를 확인할 수 있다.
- `Exception`으로 넓은 범위의 예외를 처리할 때의 주의점을 안다.
- `else`와 `finally`의 실행 조건을 설명할 수 있다.
- `return`이 있어도 `finally`가 실행되는 흐름을 이해한다.
- `raise`를 이용해 직접 예외를 발생시킬 수 있다.
- 반환 코드 방식과 예외 발생 방식의 차이를 비교할 수 있다.
- 예외 객체와 문자열을 직접 비교하면 안 되는 이유를 이해한다.
- `traceback.print_exc()`와 `traceback.format_exc()`를 구분할 수 있다.
- 실무에서 예외를 너무 넓게 잡지 않아야 하는 이유를 설명할 수 있다.

---

# 1. 예외 처리 전: 조건문으로 오류 방지

예외 처리를 배우기 전에는 조건문으로 잘못된 값을 미리 검사할 수 있다.

## 1-1. 내 코드

```python
def div(x, y):
    if y != 0:
        result = x / y
    else:
        print("두 번째 숫자는 0이 올 수 없습니다.")

    return result
```

## 1-2. 강사님 코드

```python
def div(x, y):
    result = 0

    if y != 0:
        result = x / y
    else:
        print("두 번째 숫자는 0이 올 수 없습니다.")

    return result
```

## 1-3. 코드 비교

| 구분 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| `result` 초기화 | 조건 안에서만 대입 | 함수 시작 시 `0`으로 초기화 |
| `y == 0`일 때 | `result`가 생성되지 않음 | `0` 반환 |
| 발생 가능 오류 | `UnboundLocalError` | 없음 |

내 코드에서는 `y == 0`이면 `result`가 만들어지지 않은 상태에서 `return result`가 실행된다.

## 1-4. 잘못된 실행

```python
print(div(7, 0))
```

## 1-5. 발생 결과

```text
두 번째 숫자는 0이 올 수 없습니다.
UnboundLocalError
```

## 1-6. 오류 원인

```text
y == 0
    ↓
if 블록 실행 안 됨
    ↓
result에 값이 대입되지 않음
    ↓
return result 실행
    ↓
UnboundLocalError
```

## 1-7. 조건문 방식 개선

```python
def div(x, y):
    if y == 0:
        print("두 번째 숫자는 0이 올 수 없습니다.")
        return None

    return x / y
```

### 실행

```python
print(div(7, 3))
print(div(7, 0))
```

### 출력 결과

```text
2.3333333333333335
두 번째 숫자는 0이 올 수 없습니다.
None
```

> [!TIP]
> 조건문으로 미리 검사할 수 있는 값은 먼저 검사하는 것이 좋다.
>
> 하지만 모든 예외 상황을 조건문만으로 처리하기는 어렵기 때문에 `try`와 `except`가 필요하다.

---

# 2. `try`와 `except` 기본 구조

## 2-1. 기본 문법

```python
try:
    risky_task()
except:
    handle_error()
```

## 2-2. 내 코드

```python
def div2(x, y):
    result = 0

    try:
        result = x / y
    except:
        print("예외 발생")

    return result
```

## 2-3. 강사님 코드

```python
def div2(x, y):
    result = 0

    try:
        result = x / y
    except:
        print("예외 발생")

    return result
```

## 2-4. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `try` | 예외가 발생할 수 있는 나눗셈을 실행하기 위해 |
| `x / y` | 실제 계산을 수행하기 위해 |
| `except` | 계산 중 예외가 발생했을 때 대응하기 위해 |
| `result = 0` | 계산 실패 시 반환할 기본값을 준비하기 위해 |

## 2-5. 실행

```python
print(div2(7, 0))
```

## 2-6. 출력 결과

```text
예외 발생
0
```

## 2-7. 동작 과정

```text
try 실행
    ↓
7 / 0 실행
    ↓
ZeroDivisionError 발생
    ↓
try의 남은 코드 중단
    ↓
except 실행
    ↓
예외 발생 출력
    ↓
result의 기본값 0 반환
```

> [!IMPORTANT]
> 예외가 발생한 줄 이후의 `try` 블록 코드는 실행되지 않고 바로 대응하는 `except`로 이동한다.

---

# 3. 빈 `except`의 문제점

다음 코드는 모든 예외를 한 번에 처리한다.

```python
try:
    risky_task()
except:
    print("예외 발생")
```

하지만 어떤 오류가 발생했는지 구분할 수 없다.

```python
div2(7, 0)
div2(7, "a")
```

두 경우 모두 같은 메시지만 출력된다.

```text
예외 발생
예외 발생
```

실제로는 서로 다른 오류다.

| 입력 | 발생 예외 |
| --- | --- |
| `7 / 0` | `ZeroDivisionError` |
| `7 / "a"` | `TypeError` |

> [!WARNING]
> 빈 `except:`는 `KeyboardInterrupt`, `SystemExit`처럼 일반적인 프로그램 종료 흐름까지 잡을 수 있어 사용 범위가 지나치게 넓다.
>
> 가능한 경우 처리하려는 예외 종류를 명시한다.

---

# 4. 예외 종류별 처리

## 4-1. 내 코드

```python
def div3(x, y):
    result = 0

    try:
        result = x / y
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")
    except TypeError:
        print("숫자만 넣어주세요.")

    return result
```

## 4-2. 강사님 코드

```python
def div3(x, y):
    result = 0

    try:
        result = x / y
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")
    except TypeError:
        print("숫자만 넣어 주세요.")

    return result
```

## 4-3. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `ZeroDivisionError` | 0으로 나눈 경우만 처리하기 위해 |
| `TypeError` | 숫자가 아닌 자료형으로 계산한 경우를 처리하기 위해 |
| 여러 `except` | 예외 종류별로 다른 안내를 제공하기 위해 |

## 4-4. 실행

```python
div3(7, 0)
div3(7, "a")
```

## 4-5. 출력 결과

```text
0으로 나눌 수 없습니다.
숫자만 넣어주세요.
```

## 4-6. 동작 과정

```text
div3(7, 0)
    ↓
ZeroDivisionError 발생
    ↓
except ZeroDivisionError 실행

div3(7, "a")
    ↓
TypeError 발생
    ↓
except TypeError 실행
```

> [!TIP]
> 예외 종류를 구분하면 사용자에게 더 정확한 안내를 제공하고, 오류 원인에 맞는 복구 작업을 실행할 수 있다.

---

# 5. 여러 `except`의 순서

예외 클래스도 상속 관계를 가진다.

```text
BaseException
└─ Exception
   ├─ ArithmeticError
   │  └─ ZeroDivisionError
   └─ TypeError
```

넓은 범위의 예외를 먼저 작성하면 아래의 구체적인 예외 처리가 실행되지 않을 수 있다.

## 5-1. 좋지 않은 순서

```python
try:
    result = x / y
except Exception:
    print("모든 일반 예외 처리")
except ZeroDivisionError:
    print("0으로 나눌 수 없음")
```

`ZeroDivisionError`도 `Exception`의 자식이므로 첫 번째 `except`에서 먼저 처리된다.

## 5-2. 권장 순서

```python
try:
    result = x / y
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except TypeError:
    print("숫자만 넣어주세요.")
except Exception:
    print("그 밖의 예외가 발생했습니다.")
```

```text
구체적인 예외
    ↓
더 넓은 예외
```

> [!IMPORTANT]
> 여러 `except`를 사용할 때는 **구체적인 예외를 위에**, 넓은 범위의 예외를 아래에 작성한다.

---

# 6. `as e`로 예외 객체 확인

`as e`를 사용하면 발생한 예외 객체를 변수에 저장할 수 있다.

## 6-1. 내 코드

```python
def div4(x, y):
    result = 0

    try:
        result = x / y
    except ZeroDivisionError as e:
        print("0으로 나눌 수 없습니다.", e)
    except TypeError as e:
        print("숫자만 넣어주세요.", e)

    return result
```

## 6-2. 강사님 코드

```python
def div4(x, y):
    result = 0

    try:
        result = x / y
    except ZeroDivisionError as e:
        print("0으로 나눌 수 없습니다.", e)
    except TypeError as e:
        print("숫자만 넣어 주세요.", e)

    return result
```

## 6-3. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `as e` | 발생한 예외 객체를 `e`에 저장하기 위해 |
| `print(..., e)` | Python이 제공하는 실제 예외 메시지도 확인하기 위해 |

## 6-4. 실행

```python
div4(7, 0)
div4(7, "a")
```

## 6-5. 출력 예시

```text
0으로 나눌 수 없습니다. division by zero
숫자만 넣어주세요. unsupported operand type(s) for /: 'int' and 'str'
```

> [!TIP]
> `e`는 단순 문자열이 아니라 예외 객체다.
>
> 화면에 출력하면 예외 메시지처럼 보이지만, 내부적으로는 `ZeroDivisionError`, `TypeError` 같은 객체다.

---

# 7. `Exception`으로 일반 예외 처리

## 7-1. 내 코드

```python
def div5(x, y):
    result = 0

    try:
        result = x / y
    except Exception as e:
        print("예외 발생", e)

    return result
```

## 7-2. 강사님 코드

```python
def div5(x, y):
    result = 0

    try:
        result = x / y
    except Exception as e:
        print("예외 발생", e)

    return result
```

`Exception`은 대부분의 일반적인 실행 예외의 부모 클래스다.

## 7-3. 실행

```python
div5(7, 0)
div5(7, "a")
```

## 7-4. 출력 예시

```text
예외 발생 division by zero
예외 발생 unsupported operand type(s) for /: 'int' and 'str'
```

## 7-5. 언제 사용할까?

- 여러 예외를 같은 방식으로 처리할 때
- 최종 단계에서 예상하지 못한 일반 예외를 기록할 때
- 로그를 남기고 다시 예외를 전달할 때

## 7-6. 언제 주의해야 할까?

다음 코드는 오류를 숨길 수 있다.

```python
try:
    important_task()
except Exception:
    pass
```

오류가 발생해도 아무 기록 없이 넘어간다.

> [!WARNING]
> `except Exception`을 사용하더라도 예외 메시지를 기록하거나, 복구할 수 없는 예외는 다시 발생시키는 것이 좋다.

---

# 8. `else`

`else`는 `try` 블록에서 예외가 발생하지 않았을 때 실행된다.

## 8-1. 내 코드

```python
def div6(x, y):
    result = 0

    try:
        result = x / y
    except Exception as e:
        print("예외 발생", e)
    else:
        print("문제 없었음")

    return result
```

## 8-2. 강사님 코드

```python
def div6(x, y):
    result = 0

    try:
        result = x / y
    except Exception as e:
        print("예외 발생", e)
    else:
        print("문제 없었다")

    return result
```

## 8-3. 실행

```python
div6(7, 0)
div6(7, 2)
```

## 8-4. 출력 결과

```text
예외 발생 division by zero
문제 없었음
```

## 8-5. 실행 흐름

```text
예외 발생
try → except
else 실행 안 됨
```

```text
예외 없음
try 완료
    ↓
else 실행
```

## 8-6. 왜 사용할까?

예외 처리 대상 코드와 성공했을 때 실행할 코드를 분리할 수 있다.

```python
try:
    number = int(user_input)
except ValueError:
    print("숫자를 입력하세요.")
else:
    print(f"입력한 숫자: {number}")
```

> [!TIP]
> `try` 블록에는 예외가 발생할 가능성이 있는 코드만 최소한으로 넣고, 성공 후 실행할 코드는 `else`로 분리하면 오류 범위를 파악하기 쉽다.

---

# 9. `finally`

`finally`는 예외 발생 여부와 관계없이 실행된다.

## 9-1. 내 코드

```python
def div7(x, y):
    result = 0

    try:
        result = x / y
        return result
    except Exception as e:
        print("예외 발생", e)
    else:
        print("문제 없었음")
    finally:
        print("무조건 실행완료")

    return result
```

## 9-2. 강사님 코드

```python
def div7(x, y):
    result = 0

    try:
        result = x / y
        return result
    except Exception as e:
        print("예외 발생", e)
    else:
        print("문제 없었다")
    finally:
        print("무조건 실행")

    return result
```

## 9-3. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `return result` | 계산 결과를 함수 밖으로 반환하기 위해 |
| `finally` | 반환 또는 예외 여부와 관계없이 정리 코드를 실행하기 위해 |

## 9-4. 실행

```python
print(div7(7, 2))
print(div7(7, 0))
```

## 9-5. 출력 결과

```text
무조건 실행완료
3.5
예외 발생 division by zero
무조건 실행완료
0
```

## 9-6. `else`가 출력되지 않는 이유

`try` 안에서 `return result`가 실행되면 함수 반환을 준비한다.

그 전에 `finally`가 실행되고, 이후 함수가 종료된다.

따라서 이 구조에서는 `else`에 도달하지 않는다.

```text
try에서 return 준비
    ↓
finally 실행
    ↓
함수 반환
```

> [!IMPORTANT]
> `return`이 실행되어도 함수가 완전히 종료되기 전에 `finally`가 먼저 실행된다.

---

# 10. `finally`는 언제 사용할까?

주로 반드시 정리해야 하는 자원이 있을 때 사용한다.

예:

- 파일 닫기
- 데이터베이스 연결 종료
- 네트워크 연결 해제
- 잠금 해제
- 임시 상태 복구

```python
file = None

try:
    file = open("data.txt", "r", encoding="utf-8")
    content = file.read()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
finally:
    if file is not None:
        file.close()
```

다만 파일은 `with`문을 사용하는 편이 더 간결하다.

```python
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

> [!TIP]
> `finally`는 “무조건 실행해야 하는 정리 작업”에 적합하다.
>
> 파일 작업처럼 더 안전한 전용 문법이 있다면 `with`문을 우선 고려한다.

---

# 11. `try`·`except`·`else`·`finally` 실행 순서

## 11-1. 예외가 없는 경우

```text
try
    ↓
else
    ↓
finally
```

## 11-2. 예외가 발생한 경우

```text
try
    ↓
except
    ↓
finally
```

## 11-3. `return`이 있는 경우

```text
try 또는 except에서 return 준비
    ↓
finally 실행
    ↓
실제 반환
```

## 11-4. 비교표

| 블록 | 실행 조건 |
| --- | --- |
| `try` | 항상 먼저 실행 |
| `except` | 지정한 예외가 발생했을 때 |
| `else` | 예외가 발생하지 않았을 때 |
| `finally` | 예외 발생 여부와 관계없이 |

---

# 12. `raise`

`raise`는 개발자가 직접 예외를 발생시키는 키워드다.

```python
raise Exception("메시지")
```

## 12-1. 왜 직접 예외를 발생시킬까?

문법상 실행은 가능하지만 프로그램 규칙상 허용하지 않는 값을 차단하기 위해 사용한다.

```python
def set_age(age):
    if age < 0:
        raise ValueError("나이는 음수일 수 없습니다.")

    return age
```

## 12-2. 실행

```python
print(set_age(20))
print(set_age(-1))
```

## 12-3. 출력 결과

```text
20
ValueError: 나이는 음수일 수 없습니다.
```

## 12-4. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `if age < 0` | 잘못된 입력값인지 검사하기 위해 |
| `raise` | 잘못된 상태를 즉시 예외로 알리기 위해 |
| `ValueError` | 값 자체가 올바르지 않음을 표현하기 위해 |

> [!IMPORTANT]
> `raise`는 단순 메시지 출력과 다르다.
>
> 예외를 발생시키면 현재 실행 흐름이 중단되고, 호출한 쪽의 `except`에서 처리할 수 있다.

---

# 13. 반환 코드 방식의 로그인 검증

## 13-1. 내 코드

```python
def login_check(user_id, password):
    if user_id == "admin" and password == "1234":
        print("로그인 성공")
        return 0
    elif user_id == "":
        print("아이디를 입력해주세요")
        return 1
```

원본에서는 매개변수 이름으로 `id`를 사용했지만, `id()`는 Python 내장 함수이므로 `user_id`처럼 작성하는 것이 좋다.

## 13-2. 호출 코드

```python
def login():
    user_id = "admin"
    password = "1234"

    result = login_check(user_id, password)

    if result == 0:
        print("메인 페이지로 이동")
    elif result == 1:
        print("alert(아이디를 입력하세요)")
```

## 13-3. 실행 결과

```text
로그인 성공
메인 페이지로 이동
```

## 13-4. 반환 코드 방식

```text
0 → 성공
1 → 아이디 누락
```

호출한 함수가 반환값을 확인해 분기한다.

## 13-5. 한계

- 코드 숫자의 의미를 따로 기억해야 한다.
- 처리하지 않은 경우 `None`이 반환될 수 있다.
- 오류 종류가 늘어나면 조건문이 복잡해진다.
- 정상 반환값과 오류 코드를 혼동할 수 있다.

---

# 14. `raise`를 이용한 로그인 검증

## 14-1. 내 코드

```python
def login_check2(user_id, password):
    if user_id == "admin" and password == "1234":
        print("로그인 성공")
        return 0
    elif user_id == "":
        print("아이디를 입력해주세요")
        raise Exception("code:1")
    elif password == "":
        print("비밀번호를 입력해주세요")
        raise TypeError("code:2")
```

## 14-2. 강사님 코드

```python
def login_check2(user_id, password):
    if user_id == "admin" and password == "1234":
        print("로그인 성공")
        return 0
    elif user_id == "":
        print("아이디를 입력해주세요")
        raise Exception("code:1")
    elif password == "":
        print("비밀번호를 입력해주세요")
        raise TypeError("code:2")
```

## 14-3. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `raise Exception("code:1")` | 아이디 누락을 예외 흐름으로 전달하기 위해 |
| `raise TypeError("code:2")` | 비밀번호 누락을 다른 예외 종류로 구분하기 위해 |
| `except TypeError` | 비밀번호 관련 예외를 먼저 처리하기 위해 |
| `except Exception` | 그 밖의 일반 예외를 처리하기 위해 |

## 14-4. 실행 흐름

```text
login_check2() 실행
    ↓
입력값 검사
    ↓
문제 없음 → 0 반환
문제 있음 → raise로 예외 발생
    ↓
login2()의 except에서 처리
```

---

# 15. 예외 객체와 문자열 비교 오류

원본 코드에는 다음 형태가 있다.

```python
try:
    login_check2("guest", "")
except TypeError as e:
    if e == "code:2":
        print("alert(비밀번호를 입력하세요)")
```

이 비교는 의도대로 동작하지 않는다.

## 15-1. 왜 동작하지 않을까?

`e`는 문자열이 아니라 `TypeError` 예외 객체다.

```text
e
→ TypeError("code:2") 객체

"code:2"
→ str 객체
```

따라서 다음 비교는 일반적으로 `False`다.

```python
e == "code:2"
```

## 15-2. 문자열 메시지를 비교하려면

```python
if str(e) == "code:2":
    print("alert(비밀번호를 입력하세요)")
```

## 15-3. 더 나은 방식

예외 종류 자체로 이미 분기했다면 메시지를 다시 비교하지 않아도 된다.

```python
def login2():
    user_id = "guest"
    password = ""

    try:
        result = login_check2(user_id, password)

        if result == 0:
            print("메인 페이지로 이동")
    except TypeError as e:
        print(e)
        print("alert(비밀번호를 입력하세요)")
    except Exception as e:
        print(e)
        print("alert(아이디를 입력하세요)")
```

> [!IMPORTANT]
> 예외 객체의 메시지가 필요하면 `str(e)`를 사용한다.
>
> 그러나 가능하면 문자열 코드에 의존하기보다 예외 종류를 명확하게 나누는 편이 좋다.

---

# 16. 내장 예외 종류를 의미에 맞게 사용하기

원본에서는 비밀번호 누락에 `TypeError`를 사용한다.

```python
raise TypeError("code:2")
```

하지만 비밀번호가 빈 문자열인 것은 자료형이 잘못된 상황이 아니다.

```text
password == ""
→ 자료형은 str로 정상
→ 값이 비어 있는 것이 문제
```

이 경우 `ValueError`가 더 자연스럽다.

```python
raise ValueError("비밀번호를 입력해주세요.")
```

## 16-1. 대표 예외 선택 기준

| 예외 | 사용 상황 |
| --- | --- |
| `ValueError` | 자료형은 맞지만 값이 잘못됨 |
| `TypeError` | 지원하지 않는 자료형이 전달됨 |
| `KeyError` | 딕셔너리에 없는 키 접근 |
| `IndexError` | 범위를 벗어난 인덱스 접근 |
| `FileNotFoundError` | 파일을 찾을 수 없음 |
| `ZeroDivisionError` | 0으로 나눔 |

> [!TIP]
> 예외 종류는 오류 상황의 의미와 맞게 선택해야 호출하는 쪽에서도 원인을 쉽게 파악할 수 있다.

---

# 17. 사용자 정의 예외

로그인 오류처럼 프로그램만의 의미가 필요한 경우 사용자 정의 예외를 만들 수 있다.

```python
class LoginError(Exception):
    pass


class EmptyUserIdError(LoginError):
    pass


class EmptyPasswordError(LoginError):
    pass
```

## 17-1. 검증 함수

```python
def validate_login(user_id, password):
    if not user_id:
        raise EmptyUserIdError("아이디를 입력해주세요.")

    if not password:
        raise EmptyPasswordError("비밀번호를 입력해주세요.")

    if user_id != "admin" or password != "1234":
        raise LoginError("아이디 또는 비밀번호가 올바르지 않습니다.")

    return True
```

## 17-2. 실행

```python
try:
    validate_login("admin", "")
except EmptyUserIdError as e:
    print(e)
except EmptyPasswordError as e:
    print(e)
except LoginError as e:
    print(e)
```

## 17-3. 출력 결과

```text
비밀번호를 입력해주세요.
```

## 17-4. 왜 사용할까?

- 숫자 코드보다 의미가 명확하다.
- 예외 종류만 보고 오류 원인을 구분할 수 있다.
- 호출하는 쪽의 처리 코드가 읽기 쉬워진다.

> [!TIP]
> 초보 단계에서는 내장 예외를 먼저 정확히 사용하는 것이 우선이다.
>
> 사용자 정의 예외는 프로그램 고유의 오류 의미가 필요할 때 사용한다.

---

# 18. `traceback`

`traceback` 모듈은 예외가 발생한 위치와 호출 경로를 확인할 때 사용한다.

## 18-1. 원본 코드

```python
import traceback

try:
    result = 3 / 0
except Exception as e:
    print(e)
    traceback.print_exc()

    error_text = traceback.format_exc()

    print("-" * 30)
    print(error_text)
```

## 18-2. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `import traceback` | 오류 추적 기능을 사용하기 위해 |
| `traceback.print_exc()` | 전체 오류 추적 정보를 바로 출력하기 위해 |
| `traceback.format_exc()` | 전체 오류 추적 정보를 문자열로 받기 위해 |

## 18-3. 출력 형태

```text
division by zero
Traceback (most recent call last):
  ...
ZeroDivisionError: division by zero
------------------------------
Traceback (most recent call last):
  ...
ZeroDivisionError: division by zero
```

## 18-4. `print_exc()`와 `format_exc()` 비교

| 함수 | 결과 |
| --- | --- |
| `traceback.print_exc()` | 오류 추적 정보를 바로 출력 |
| `traceback.format_exc()` | 오류 추적 정보를 문자열로 반환 |

`format_exc()`로 받은 문자열은 파일이나 로그 시스템에 저장할 수 있다.

```python
error_text = traceback.format_exc()
```

---

# 19. `traceback`은 사용자 화면에 보여줘야 할까?

일반 사용자에게 전체 traceback을 그대로 보여주면 안 되는 경우가 많다.

이유:

- 내부 파일 경로가 노출될 수 있다.
- 코드 구조가 드러날 수 있다.
- 사용자가 이해하기 어렵다.
- 보안상 민감한 정보가 포함될 수 있다.

```text
개발자 로그
→ 상세 traceback 기록

사용자 화면
→ 이해하기 쉬운 오류 안내
```

예:

```python
try:
    result = 3 / 0
except ZeroDivisionError:
    traceback.print_exc()
    print("계산 중 문제가 발생했습니다.")
```

> [!WARNING]
> traceback은 개발자 확인용 로그에 적합하다.
>
> 사용자에게는 필요한 정보만 정리해서 보여주는 것이 좋다.

---

# 20. 예외를 처리한 뒤 다시 발생시키기

현재 함수에서 로그만 남기고 상위 호출자에게 다시 예외를 전달할 수 있다.

```python
try:
    result = 3 / 0
except ZeroDivisionError:
    print("나눗셈 오류를 기록합니다.")
    raise
```

`raise` 뒤에 예외 객체를 쓰지 않으면 현재 처리 중인 예외를 다시 발생시킨다.

```text
예외 발생
    ↓
현재 except에서 로그 기록
    ↓
raise
    ↓
상위 호출자에게 예외 전달
```

이 방식은 현재 함수가 오류를 완전히 해결할 수 없을 때 사용한다.

---

# 21. 예외 처리 범위는 작게 유지하기

좋지 않은 예:

```python
try:
    user = get_user()
    order = create_order(user)
    payment = pay(order)
    send_email(user)
except Exception:
    print("오류 발생")
```

어느 단계에서 오류가 발생했는지 파악하기 어렵다.

개선:

```python
try:
    user = get_user()
except UserNotFoundError:
    print("사용자를 찾을 수 없습니다.")
```

```python
try:
    order = create_order(user)
except OrderError:
    print("주문 생성에 실패했습니다.")
```

> [!TIP]
> `try` 블록에는 실제로 예외를 처리하려는 코드만 넣는다.
>
> 범위가 작을수록 어떤 코드에서 오류가 발생했는지 파악하기 쉽다.

---

# 22. 예외를 무시해도 되는 경우

일부 상황에서는 특정 예외를 의도적으로 무시할 수 있다.

```python
try:
    cache.remove("old_key")
except KeyError:
    pass
```

하지만 이유가 분명해야 한다.

```python
try:
    cache.remove("old_key")
except KeyError:
    # 이미 없는 키라면 원하는 최종 상태와 같으므로 무시한다.
    pass
```

> [!WARNING]
> 이유 없이 `except: pass`를 사용하면 실제 버그까지 숨길 수 있다.

---

# 23. 예외 처리와 반환값

오류가 발생했을 때 무조건 `0`, 빈 문자열, 빈 리스트를 반환하면 정상 결과와 구분하기 어려울 수 있다.

```python
def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return 0
```

실제 계산 결과가 `0`인 경우와 오류가 난 경우를 구분하기 어렵다.

더 명확한 방식:

```python
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("0으로 나눌 수 없습니다.")

    return x / y
```

호출하는 쪽에서 처리한다.

```python
try:
    result = divide(7, 0)
except ZeroDivisionError as e:
    print(e)
```

---

# 24. 대표 오류로 이해하기

## 24-1. 정의되지 않은 지역 변수 반환

```python
def div(x, y):
    if y != 0:
        result = x / y

    return result
```

`y == 0`이면 `result`가 없으므로 `UnboundLocalError`가 발생한다.

---

## 24-2. 예외 객체를 문자열과 직접 비교

```python
try:
    login_check2("guest", "")
except TypeError as e:
    if e == "code:2":
        print("비밀번호 누락")
```

`e`는 예외 객체이므로 문자열과 직접 비교하지 않는다.

개선:

```python
if str(e) == "code:2":
    print("비밀번호 누락")
```

더 나은 방식:

```python
try:
    validate_login("admin", "")
except EmptyPasswordError:
    print("비밀번호 누락")
```

---

## 24-3. 넓은 예외를 먼저 작성

```python
try:
    int("abc")
except Exception:
    pass
except ValueError:
    pass
```

`ValueError`도 `Exception`에 포함되므로 두 번째 블록은 사실상 실행되지 않는다.

---

## 24-4. 오류를 완전히 숨김

```python
try:
    important_task()
except Exception:
    pass
```

프로그램은 계속 실행되지만 실제 문제를 찾기 어려워진다.

---

## 24-5. `finally`에서 새 예외 발생

```python
try:
    result = 1 / 0
finally:
    print(undefined_name)
```

원래의 `ZeroDivisionError`보다 `NameError`가 눈에 띄게 되어 원인 파악이 어려워질 수 있다.

> [!WARNING]
> `finally`에는 실패 가능성이 낮은 단순 정리 코드를 작성한다.

---

# 25. 예외 처리 구조

```text
함수 호출
    ↓
try에서 작업 실행
    ├─ 성공
    │   ↓
    │  else
    │   ↓
    │  finally
    │
    └─ 예외 발생
        ↓
       일치하는 except
        ↓
       finally
```

```text
raise
→ 현재 흐름 중단
→ 호출 스택을 따라 위로 전달
→ 일치하는 except에서 처리
```

---

# 26. 기존 코드에서 개선 코드로 바꾼 이유

## 26-1. `id` 이름 변경

기존:

```python
def login_check(id, pw):
    pass
```

개선:

```python
def login_check(user_id, password):
    pass
```

이유:

- `id()` 내장 함수를 가리지 않는다.
- 변수 의미가 더 분명하다.
- 축약형보다 읽기 쉽다.

## 26-2. `TypeError`를 `ValueError`로 변경

기존:

```python
raise TypeError("비밀번호를 입력해주세요.")
```

개선:

```python
raise ValueError("비밀번호를 입력해주세요.")
```

이유:

- 비밀번호는 문자열 자료형으로 정상이다.
- 빈 문자열이라는 값이 잘못된 것이므로 `ValueError`가 의미에 맞다.

## 26-3. 문자열 오류 코드 제거

기존:

```python
raise Exception("code:1")
```

개선:

```python
raise EmptyUserIdError("아이디를 입력해주세요.")
```

이유:

- 숫자·문자 코드의 의미를 외울 필요가 없다.
- 예외 클래스 이름만으로 상황을 알 수 있다.
- 문자열 비교 오류를 줄일 수 있다.

## 26-4. `try` 범위 축소

기존:

```python
try:
    user = get_user()
    order = create_order(user)
    payment = pay(order)
except Exception:
    print("하나의 오류 메시지")
```

개선:

```text
처리하려는 작업별로 try 범위를 분리
→ 더 구체적인 예외 처리
→ 오류 위치 확인 쉬움
```

---

# 27. 자주 하는 실수

## 27-1. 빈 `except:` 사용

어떤 예외가 발생했는지 구분하기 어렵고 종료 신호까지 잡을 수 있다.

## 27-2. `except Exception`으로 모든 문제를 숨김

예외를 기록하지 않으면 버그를 찾기 어렵다.

## 27-3. 넓은 예외를 구체적인 예외보다 먼저 작성

구체적인 `except`가 실행되지 않을 수 있다.

## 27-4. 예외 객체와 문자열을 직접 비교

`str(e)`를 사용하거나 예외 종류 자체로 구분한다.

## 27-5. 의미에 맞지 않는 예외 종류 사용

빈 문자열 입력은 일반적으로 `TypeError`보다 `ValueError`에 가깝다.

## 27-6. `try` 블록에 너무 많은 코드 작성

어느 줄에서 예외가 발생했는지 파악하기 어렵다.

## 27-7. `finally`에서 반환값을 덮어씀

```python
def test():
    try:
        return 1
    finally:
        return 2
```

최종 반환값은 `2`가 된다.

> [!WARNING]
> `finally`에서 `return`을 사용하면 기존 반환값이나 예외를 덮어쓸 수 있으므로 피하는 것이 좋다.

## 27-8. 예외 발생 후 무조건 기본값 반환

정상 결과와 오류 결과를 구분하기 어려울 수 있다.

## 27-9. traceback을 사용자 화면에 그대로 노출

내부 구현 정보가 노출될 수 있다.

## 27-10. 예외 처리를 정상 흐름 제어에 과도하게 사용

단순한 조건 확인은 `if`가 더 읽기 쉬울 수 있다.

---

# 28. 면접·복습 포인트

## Q1. 예외 처리란 무엇인가요?

프로그램 실행 중 발생한 비정상 상황을 감지하고 적절한 대응을 실행하는 기능이다.

## Q2. `try`와 `except`의 역할은 무엇인가요?

`try`는 예외가 발생할 수 있는 코드를 실행하고, `except`는 지정한 예외가 발생했을 때 처리한다.

## Q3. 빈 `except:`를 권장하지 않는 이유는 무엇인가요?

처리 범위가 지나치게 넓어 예상하지 못한 예외와 프로그램 종료 신호까지 잡을 수 있기 때문이다.

## Q4. 여러 `except`는 어떤 순서로 작성해야 하나요?

구체적인 예외를 위에, 넓은 범위의 예외를 아래에 작성한다.

## Q5. `else`는 언제 실행되나요?

`try` 블록에서 예외가 발생하지 않았을 때 실행된다.

## Q6. `finally`는 언제 실행되나요?

예외 발생 여부나 `return` 여부와 관계없이 실행된다.

## Q7. `raise`는 왜 사용하나요?

프로그램 규칙상 허용하지 않는 상황을 예외로 알리고 호출한 쪽에서 처리할 수 있게 하기 위해 사용한다.

## Q8. `as e`의 `e`는 문자열인가요?

아니다. 발생한 예외 객체다. 메시지는 `str(e)`로 확인할 수 있다.

## Q9. `Exception`은 언제 사용하나요?

예상하지 못한 일반 예외를 최종적으로 기록하거나 공통 처리할 때 사용할 수 있지만, 구체적인 예외 처리를 우선해야 한다.

## Q10. `traceback.print_exc()`와 `format_exc()`의 차이는 무엇인가요?

`print_exc()`는 바로 출력하고, `format_exc()`는 traceback 내용을 문자열로 반환한다.

## Q11. `finally`에서 `return`을 피해야 하는 이유는 무엇인가요?

기존 반환값이나 발생한 예외를 덮어쓸 수 있기 때문이다.

## Q12. 사용자 정의 예외는 언제 사용하나요?

프로그램 고유의 오류 의미를 내장 예외만으로 충분히 표현하기 어려울 때 사용한다.

---

# 29. 핵심 요약

```text
try
→ 예외가 발생할 수 있는 코드 실행

except
→ 지정한 예외 처리

else
→ 예외가 없을 때 실행

finally
→ 성공·실패·return과 관계없이 실행

raise
→ 개발자가 직접 예외 발생

as e
→ 예외 객체 확인

Exception
→ 일반 예외의 넓은 부모 클래스

traceback
→ 오류 발생 위치와 호출 경로 확인
```

```text
구체적인 예외부터 처리
    ↓
try 범위는 작게 유지
    ↓
예외를 숨기지 말고 기록
    ↓
복구할 수 없으면 다시 raise
```

---

# 30. 최종 체크리스트

- [ ] 예외가 발생할 가능성이 있는 코드만 `try`에 넣었는가?
- [ ] 빈 `except:` 대신 처리할 예외 종류를 명시했는가?
- [ ] 구체적인 예외를 넓은 예외보다 위에 작성했는가?
- [ ] 예외 객체와 문자열을 직접 비교하지 않았는가?
- [ ] 오류 상황에 맞는 예외 종류를 사용했는가?
- [ ] `except Exception`에서 오류를 완전히 숨기지 않았는가?
- [ ] `finally`에는 반드시 실행해야 하는 정리 코드만 작성했는가?
- [ ] `finally`에서 `return`으로 기존 결과를 덮어쓰지 않았는가?
- [ ] traceback은 개발자용 로그로 관리하고 있는가?
- [ ] 사용자에게는 이해하기 쉬운 오류 메시지를 제공하는가?
- [ ] 반환 코드보다 예외가 더 적절한 상황인지 검토했는가?
- [ ] 사용자 정의 예외가 실제로 필요한 상황인지 확인했는가?

---

# 마무리

예외 처리의 목적은 프로그램을 무조건 계속 실행시키는 것이 아니다.

```text
오류 가능성이 있는 작업을 구분하고
    ↓
발생한 예외의 종류를 정확히 파악하고
    ↓
복구할 수 있는 경우 적절히 처리하며
    ↓
복구할 수 없는 경우 상위 호출자에게 전달하고
    ↓
필요한 정리 작업은 반드시 실행하는 것
```

이 흐름을 이해하면 파일 입출력, 네트워크, 데이터베이스, 사용자 입력처럼 실패 가능성이 있는 작업을 더 안전하게 작성할 수 있다.
