# 14-02. 직접 예외 만들기와 오류 위치 추적

[Python 목차](README.md) · [이전: 예외 처리 심화](14-01_Python_예외처리_심화.md)

두 원본의 뒤쪽은 로그인 예제로 **반환값으로 상태를 알리는 방법**과 **`raise`로 예외를 발생시키는 방법**을 비교한다. 마지막에는 `traceback`으로 오류가 발생한 위치를 확인한다.

<!-- chapter-toc -->

- [1. 숫자 반환값으로 상태 알리기](14-02_Python_예외발생과_오류추적.md#section-1)
- [2. `raise`로 오류를 발생시키기](14-02_Python_예외발생과_오류추적.md#section-2)
- [3. `traceback`으로 발생 위치 보기](14-02_Python_예외발생과_오류추적.md#section-3)
- [직접 확인할 질문](14-02_Python_예외발생과_오류추적.md#section-4)
- [추가로 알면 좋은 것](14-02_Python_예외발생과_오류추적.md#section-5)

<a id="section-1"></a>

## 1. 숫자 반환값으로 상태 알리기

### 강사님 코드

출처: `teacher/workspace_python/_14_try.py` 101–120행 · **원본 발췌**

```python
def loginCheck(id, pw):
    if id == 'admin' and pw == '1234' :
        print('로그인 성공')
        return 0

    elif id == '' :
        print('아이디를 입력해주세요')
        return 1

def login():
    id = 'admin'
    pw = '1234'
    result = loginCheck(id, pw)

    if result == 0 :
        print('메인 페이지로 이동')
    elif result == 1 :
        print('alert(아이디를 입력하세요)')

login()
```

### 내 코드

출처: `me/workspace_python/14_try.py` 94–112행 · **원본 발췌**

```python
def loginCheck(id, pw) :
    if id == 'admin' and pw == '1234' :
        print('로그인 성공')
        return 0
    elif id == '' :
        print('아이디를 입력해주세요')
        return 1

def login() :
    id = 'admin'
    pw = '1234'
    result = loginCheck(id, pw)

    if result == 0 :
        print('메인 페이지로 이동')
    elif result == 1 :
        print('alert(아이디를 입력하세요)')

login()
```

`loginCheck('admin','1234')`는 성공을 출력하고 `0`을 돌려준다. `login()`은 그 0을 받아 `메인 페이지로 이동`을 출력한다. 빈 아이디이면 `1`을 돌려주도록 했지만, **두 원본의 실제 `login()` 호출은 성공 값으로 고정**되어 있다. 아이디가 비어 있지 않은데 비밀번호만 틀리면 이 함수에는 해당 분기가 없어 `None`을 돌려준다. 따라서 이 코드는 모든 로그인 실패를 구분하는 완성된 로그인 기능이 아니다.

<a id="section-2"></a>

## 2. `raise`로 오류를 발생시키기

### 강사님 코드

출처: `teacher/workspace_python/_14_try.py` 123–151행 · **원본 발췌**

```python
def loginCheck2(id, pw):
    if id == 'admin' and pw == '1234' :
        print('로그인 성공')
        return 0

    elif id == '' :
        print('아이디를 입력해주세요')
        raise Exception('code:1')

    elif pw == '' :
        print('비밀번호를 입력해주세요')
        raise TypeError('code:2')

def login2():
    id = 'asdf'
    pw = ''
    try:
        result = loginCheck2(id, pw)
        if result == 0 :
            print('메인 페이지로 이동')
    except TypeError as e:
        print(e)
        print('alert(비밀번호를 입력하세요)')
    except Exception as e:
        print(1111, e)
        if e == 'code:1':
            print('alert(아이디를 입력하세요)')

login2()
```

### 내 코드

출처: `me/workspace_python/14_try.py` 114–142행 · **원본 발췌**

```python
def loginCheck2(id, pw) :
    if id == 'admin' and pw == '1234' :
        print('로그인 성공')
        return 0
    elif id == '' :
        print('아이디를 입력해주세요')
        raise Exception('code:1') # code:1 처럼 별도의 ErrMsg를 작성해서 그것으로도 판단할 수 있음
    
    elif pw == '' :
        print('비밀번호를 입력해주세요')
        raise TypeError('code:2')

def login2() :
    id = '111'
    pw = ''
    try : 
        result = loginCheck2(id, pw)
        if result == 0 :
            print('메인 페이지로 이동')
    except TypeError as e: # Exception이 더 큰 범위이기 때문에, TypeError가 있다면 위로 올려줌
        print(e)
        if e == 'code:2' :
            print('alert(비밀번호를 입력하세요)')
    except Exception as e:
        print(e)
        if e == 'code:1' :
            print('alert(아이디를 입력하세요)')

login2()
```

두 파일의 `loginCheck2`는 빈 아이디에서 `Exception('code:1')`, 빈 비밀번호에서 `TypeError('code:2')`를 발생시킨다. `login2()`가 이를 `try`로 호출하고, **더 구체적인 `TypeError` 처리문을 먼저** 배치했다. 강사님 `login2()`의 입력은 `id='asdf', pw=''`여서 `code:2`가 출력되고 `alert(비밀번호를 입력하세요)`도 출력된다.

내 `login2()`도 아이디는 빈 값이 아니고 비밀번호만 비어 있어 `TypeError('code:2')`에 들어간다. 하지만 내 코드의 `if e == 'code:2'`는 **예외 객체와 문자열을 직접 비교**하므로 거짓이다. 그래서 오류 메시지 `code:2`는 출력되지만, 의도한 `alert(...)`는 나오지 않는다. 강사님 코드의 빈 아이디 처리에도 `if e == 'code:1'` 비교가 있으므로 그 분기를 실제로 시험하면 같은 문제가 있다. 두 원본의 차이를 “강사님 것은 모두 완성”으로 단순화하지 말고, **실행해 본 경로와 실행하지 않은 경로**를 구분하자.

<a id="section-3"></a>

## 3. `traceback`으로 발생 위치 보기

### 강사님 코드

출처: `teacher/workspace_python/_14_try.py` 154–163행 · **원본 발췌**

```python
import traceback
try:
    a = 3 / 0
except Exception as e :
    print(e)
    traceback.print_exc()
    a = traceback.format_exc()
    print('-'*30)
    print(a)

```

### 내 코드

출처: `me/workspace_python/14_try.py` 144–153행 · **원본 발췌**

```python
import traceback
try:
    a = 3 / 0
except Exception as e :
    print(e)
    traceback.print_exc() # 원래의 Error msg를 text로 담아와주는 모듈
    a = traceback.format_exc() # 변수에 Error msg를 변수에 담아둘 수 있음
    print('-'*30)
    print(a)

```

`3/0`에서 발생한 오류를 잡아 `print(e)`로 메시지를 보여 준다. `traceback.print_exc()`는 현재 예외의 위치와 호출 흐름을 바로 출력하고, `traceback.format_exc()`는 비슷한 내용을 **문자열로 만들어** `a`에 담는다. 그래서 두 코드는 오류 정보를 한 번은 직접 출력하고, 한 번은 구분선 뒤에 문자열로 다시 출력한다. 이 예제의 `traceback`은 실제 실행 코드이며, 내 파일 끝의 이터레이터·제너레이터·정규표현식은 **간단한 학습 메모**일 뿐 상세 구현이 아니다.

<a id="section-4"></a>

## 직접 확인할 질문

1. `loginCheck`에서 비밀번호만 틀리면 반환값은 무엇일까?
2. 내 `login2()`에서 `code:2`가 보이는데 `alert(...)`가 나오지 않는 이유는?
3. `print_exc()`와 `format_exc()`는 결과를 각각 어떻게 사용하나?

<a id="section-5"></a>

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/14-02_Python_예외발생과_오류추적_연습문제.md)

## 추가로 알면 좋은 것

예외를 문자열 코드로 구분하는 방식보다 명확한 구조를 설계하는 방법은 이 수업 코드에 구현되어 있지 않다. 이 장에서는 **원본의 `raise`와 `except`가 실제로 연결되는지**를 판단하는 데 머문다.

