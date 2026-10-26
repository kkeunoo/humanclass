# 14-01. 예외 처리 이어 읽기 — 오류 메시지와 범위

[Python 목차](README.md) · [이전: 상속](13-02_Python_메서드재정의와_추상클래스.md) · [다음: 로그인과 오류 추적](14-02_Python_예외발생과_오류추적.md)

[00-02 오류 읽기](00-02_Python_오류와_예외.md)에서 `div`·`div3`·`div6`·`div7`의 중요한 차이를 먼저 봤다. 같은 코드를 다시 길게 싣지 않고, 여기서는 원본의 **남은 `div2`·`div4`·`div5`**가 예외를 어떤 범위로 잡는지 비교한다.

<!-- chapter-toc -->

- [1. 종류를 지정하지 않은 `except`](#section-1)
- [2. 예외 객체의 메시지 읽기](#section-2)
- [3. 실제 호출에서 볼 차이](#section-3)
- [직접 확인할 질문](#section-4)
- [추가로 알면 좋은 것](#section-5)

<a id="section-1"></a>

## 1. 종류를 지정하지 않은 `except`

### 강사님 코드

출처: `teacher/workspace_python/_14_try.py` 10–17행 · **원본 발췌**

```python
def div2(x, y):
    result = 0
    try:
        result = x / y
    except:
        print('예외 발생')

    return result
```

### 내 코드

출처: `me/workspace_python/14_try.py` 10–16행 · **원본 발췌**

```python
def div2(x, y) :
    result = 0
    try : # Error가 발생하면, 정지하지 않고 except로 내려감
        result = x / y # y에서 Error가 났기 때문에 result로 넘어가지 않고 내려 간 상태
    except :
        print('예외 발생')
    return result
```

두 함수 모두 `try`에서 `x / y`를 계산한다. 실패하면 종류를 지정하지 않은 `except`로 내려가 `예외 발생`을 출력하고, 처음 만들어 둔 `result=0`을 돌려준다. 하지만 **두 원본의 실행 구간에서는 `div2(7,0)` 호출이 주석 처리**되어 있어 함수 정의를 읽는 예제다. 이 방식은 어떤 문제가 났는지 구별하기 어렵다.

<a id="section-2"></a>

## 2. 예외 객체의 메시지 읽기

### 강사님 코드

출처: `teacher/workspace_python/_14_try.py` 30–49행 · **원본 발췌**

```python
def div4(x, y):
    result = 0
    try:
        result = x / y
    except ZeroDivisionError as e: # 예외 메세지
        print('0으로 나눌 수 없슴다', e)
    except TypeError as e:
        print('숫자만 넣어 주세요', e)

    return result

def div5(x, y):
    result = 0
    try:
        result = x / y
    except Exception as e : # 모든 예외 처리
        print('예외 발생', e)

    return result

```

### 내 코드

출처: `me/workspace_python/14_try.py` 28–45행 · **원본 발췌**

```python
def div4(x, y) :
    result = 0
    try : 
        result = x / y 
    except ZeroDivisionError as e: # as e 처럼 e에 넣어둔다면, 예외 Error 메세지도 출력 됨
        print('0으로 나눌 수 없습니다.', e) 
    except TypeError as e: 
        print('숫자만 넣어주세요.', e)
    return result

def div5(x, y) :
    result = 0
    try : 
        result = x / y 
    except Exception as e: # Exception은 모든 Error의 부모 / 단, KeyboardInterrupt 등 ctrl+c 같은건 별개로 지정필요
        print('예외 발생', e) 
    return result

```

`div4`는 `ZeroDivisionError`와 `TypeError`를 따로 잡고, `as e`로 해당 예외의 메시지를 함께 출력한다. `div5`는 `Exception as e`로 더 넓은 범위의 보통 오류를 잡는다. 내 주석에도 적혀 있듯 `KeyboardInterrupt`처럼 `Exception`에 포함되지 않는 예외까지 **전부 잡는다는 뜻은 아니다**. 또한 오류를 잡아 출력만 하고 `0`을 돌려주므로, 호출한 쪽에서는 그 0이 정상 계산인지 오류의 대체값인지 구분하기 어렵다. 이 예제에서는 각 방식의 동작을 비교하는 데 집중한다.

<a id="section-3"></a>

## 3. 실제 호출에서 볼 차이

### 강사님 코드

출처: `teacher/workspace_python/_14_try.py` 75–97행 · **원본 발췌**

```python
a = div(7, 3)
print(a)

a = div(7, 0)
# a = div2(7, 0)
# a = div(7, '3')
print(a)

div3(7, 0)
div3(7, 'a')

div4(7, 0)
div4(7, 'a')

div5(7, 0)
div5(7, 'a')

div6(7, 0)
div6(7, 2)

div7(7, 0)
div7(7, 2)

```

### 내 코드

출처: `me/workspace_python/14_try.py` 69–90행 · **원본 발췌**

```python
a = div(7, 3)
print(a)

# a = div(7, 0)
# a = div2(7, 0)
# a = div(7, '3')
print(a)

div3(7, 0)
div3(7, 'a')

div4(7, 0)
div4(7, 'a')

div5(7, 0)
div5(7, 'a')

div6(7, 0)
div6(7, 2)

div7(7, 0)
div7(7, 2)
```

강사님은 `div(7,0)`을 실제로 호출해 안내 뒤 0을 받는다. 내 코드는 그 줄을 주석 처리했다. [00-02 오류 읽기](00-02_Python_오류와_예외.md)에서 확인했듯 내 `div`는 이 경우 초기화되지 않은 `result`를 반환하려 해 오류가 나므로, 전체 파일을 실행할 때 막아 둔 것이 의미가 있다. 두 파일 모두 `div3`부터 `div7`까지 다양한 성공·실패 호출을 해 본다. 숫자 `7/2`는 정상 흐름이고 `7/0`, `7/'a'`는 서로 다른 예외를 시험한다.

<a id="section-4"></a>

## 직접 확인할 질문

1. `div4(7,0)`과 `div4(7,'a')`는 어떤 `except`로 갈까?
2. `div5`가 오류를 출력한 뒤 0을 반환하면, 호출자는 무엇을 추가로 알아야 할까?

<a id="section-5"></a>

## 추가로 알면 좋은 것

오류를 단순히 출력하는 데서 나아가 호출자에게 명확히 전달하는 설계는 원본에 구현되어 있지 않다. 이 장에서는 **어떤 예외를 잡고 무슨 값을 돌려주는지**를 실제 코드로 확인한다.

