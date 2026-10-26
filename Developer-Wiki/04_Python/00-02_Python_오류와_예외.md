# 00-02. Python 오류 읽기 — 어디서 멈췄는지 먼저 찾기

[Python 목차](README.md) · [이전: 실행 방식](00-01_Python_실행방식과_프로그래밍_패러다임.md) · [다음: 출력과 주석](01_Python_출력과_주석.md)

오류 메시지를 전부 외우기보다 **실행한 줄, 오류 종류, 그 줄에 들어간 값**을 차례로 확인한다. 수업 원본의 나눗셈 예제는 같은 문제를 조건문과 예외 처리로 풀어 보인다.

<!-- chapter-toc -->

- [1. 0으로 나누기 전에 검사하기](00-02_Python_오류와_예외.md#section-1)
- [2. 어떤 오류인지 구분해서 처리하기](00-02_Python_오류와_예외.md#section-2)
- [3. 예외가 없을 때와 마지막 정리](00-02_Python_오류와_예외.md#section-3)
- [오류를 볼 때의 세 질문](00-02_Python_오류와_예외.md#section-4)
- [추가로 알면 좋은 것](00-02_Python_오류와_예외.md#section-5)

<a id="section-1"></a>

## 1. 0으로 나누기 전에 검사하기

### 강사님 코드

출처: `teacher/workspace_python/_14_try.py` 2–8행 · **원본 발췌**

```python
def div(x, y):
    result = 0
    if y != 0 :
        result = x / y
    else :
        print('두번째 숫자는 0이 올 수 없습니다')
    return result
```

### 내 코드

출처: `me/workspace_python/14_try.py` 1–7행 · **원본 발췌**

```python
# try, except 사용 전 방법 1
def div(x, y) :
    if y != 0 :
        result = x / y
    else :
        print('두 번째 숫자는 0이 올 수 없습니다')
    return result
```

두 코드 모두 `y != 0`일 때만 나눈다. 다만 **결과가 다른 경우**가 있다. 강사님 코드는 `result = 0`을 먼저 만들었으므로 `div(7, 0)`에서 안내를 출력하고 `0`을 반환한다. 내 코드는 `y == 0`일 때 `result`가 만들어지지 않은 채 `return result`에 도착해 `UnboundLocalError`가 난다. 이 오류는 0으로 나누기 오류를 막은 뒤 생긴 별도 문제다. 강사님처럼 초기값을 주거나, 해당 분기에서 명시적으로 반환해야 한다.

<a id="section-2"></a>

## 2. 어떤 오류인지 구분해서 처리하기

### 강사님 코드

출처: `teacher/workspace_python/_14_try.py` 19–28행 · **원본 발췌**

```python
def div3(x, y):
    result = 0
    try:
        result = x / y
    except ZeroDivisionError:
        print('0으로 나눌 수 없슴다')
    except TypeError:
        print('숫자만 넣어 주세요')

    return result
```

### 내 코드

출처: `me/workspace_python/14_try.py` 18–26행 · **원본 발췌**

```python
def div3(x, y) :
    result = 0
    try : 
        result = x / y 
    except ZeroDivisionError : # Error Type별로 except를 지정해서 예외처리를 할 수 있음
        print('0으로 나눌 수 없습니다.')
    except TypeError : # ZeroDivision이 먼저 발생했다면, if elif처럼 먼저 발생 된 것에서 처리됨
        print('숫자만 넣어주세요.')
    return result
```

`7 / 0`은 `ZeroDivisionError`, 숫자와 맞지 않는 자료형의 나눗셈은 `TypeError`가 날 수 있다. 두 코드 모두 각각 다른 안내를 출력한다. `except`는 발생한 예외 종류와 맞는 분기를 실행한다. 내 주석의 “if elif처럼 먼저 발생된 것”은 **오류 두 개가 차례로 일어난다는 뜻이 아니다**. 한 번의 `try` 실행에서 발생한 예외에 맞는 처리 줄로 이동한다.

<a id="section-3"></a>

## 3. 예외가 없을 때와 마지막 정리

### 강사님 코드

출처: `teacher/workspace_python/_14_try.py` 50–73행 · **원본 발췌**

```python
def div6(x, y):
    result = 0
    try:
        result = x / y
    except Exception as e : # 모든 예외 처리
        print('예외 발생', e)
    else :
        print('문제 없었다')

    return result

def div7(x, y):
    result = 0
    try:
        result = x / y
        return result
    except Exception as e : # 모든 예외 처리
        print('예외 발생', e)
    else :
        print('문제 없었다')
    finally :
        print('무조건 실행') # 무조건 실행
                            # 심지어 return을 해도
    return result
```

### 내 코드

출처: `me/workspace_python/14_try.py` 46–67행 · **원본 발췌**

```python
def div6(x, y) :
    result = 0
    try : 
        result = x / y 
    except Exception as e:
        print('예외 발생', e) 
    else : # try가 문제 없이 실행되었다면 else로 출력 가능
        print('문제 없었음')
    return result

def div7(x, y) :
    result = 0
    try : 
        result = x / y 
        return result # return을 위에 두어도 finally는 실행 됨
    except Exception as e:
        print('예외 발생', e) 
    else : 
        print('문제 없었음')
    finally : # finally는 무슨 일이 있어도 실행 됨, file에서 닫아주거나 할 때도 사용함
        print('무조건 실행완료')
    return result
```

`else`는 `try`에서 예외가 나지 않고 정상적으로 진행했을 때 실행한다. 다만 두 원본의 `div7`처럼 `try` 안에서 **먼저 `return`하면 `else`까지 내려오지 않는다.** `finally`는 이 반환 과정에서도 실행된다. 따라서 원본의 성공 호출에서는 `else`의 “문제 없었다”보다 `finally`의 “무조건 실행”을 보게 된다. 이 차이는 문장의 위치 때문에 생긴다.

<a id="section-4"></a>

## 오류를 볼 때의 세 질문

1. 어느 줄에서 멈췄는가?
2. 그 줄의 변수에는 실제로 어떤 값이 들어 있었는가?
3. 예외를 잡은 뒤에도 반환할 값은 만들어져 있는가?

<a id="section-5"></a>

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/00-02_Python_오류와_예외_연습문제.md)

## 추가로 알면 좋은 것

수업 원본에 나오지 않는 모든 예외 종류를 이 장에 나열하지 않는다. 새 오류를 만났을 때에는 그 오류가 나온 파일과 줄을 기준으로 원인을 찾는다.

