# 14-02. raise와 traceback — 반환 대신 오류를 올리고 위치를 읽기

[Python 목차](README.md) · [읽기 안내](00-00_Python_V3_동작_백과_읽기법.md)

함수가 정상 값으로 상태를 알려 주는 방법과 예외를 발생시키는 방법은 실행 경로가 다르다. 수업의 로그인 모양 예제를 통해 호출자에게 무엇이 전달되는지, 예외 객체와 문자열 메시지가 왜 다른지를 확인한다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

return 상태와 raise 전파를 비교한다. 구체 예외 우선 처리·str(e) 비교·누락된 반환 갈래를 설명하고 print_exc와 format_exc의 출력·반환 차이를 연결한다.

실제 원본·새 예제·개선안·선택 학습을 구분하고 입력·실행 순서·반환값·출력을 연결한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

return False나 return 1은 정상 반환이다. raise는 그 자리에서 정상 진행을 떠나 맞는 예외 처리 경로를 찾게 한다. 함수 안에서 raise해도 호출한 곳의 try·except가 받을 수 있다. 그 호출 다음의 일반 문장은 예외가 처리되기 전 그대로 진행하지 않는다.

| 값·호출 | 종류 | 역할 |
| --- | --- | --- |
| e | 예외 객체 | 예외 종류·메시지 등 담음 |
| str(e) | 문자열 | 사람이 읽을 메시지 표현 |
| e=='code:2' | 다른 종류의 직접 비교 | 원본의 의도한 메시지 비교가 아님 |
| traceback.print_exc() | 현재 예외 추적 출력 | 보통 표준 오류 출력으로 표시 |
| traceback.format_exc() | 추적 정보 문자열 반환 | 변수에 저장하여 사용 가능 |

print_exc는 문자열을 반환해 변수에 담는 함수가 아니다. format_exc는 문자열을 만든다. 출력 채널이나 실행 도구에 따라 일반 print와 오류 출력이 합쳐 보이는 순서는 다를 수 있으므로 화면 위아래만으로 실행 순서를 단정하지 않는다.

로그인이라는 이름이 붙어도 이 원본은 고정 문자열과 조건으로 정상·예외 경로를 실험한 코드다. 실제 인증·서버 이동·브라우저 alert를 구현한 것은 아니다. print('alert(...)')는 그 글자를 터미널에 출력한다.

> 📚 **출처 · 본문 설명 확인:** [Python 예외 발생시키기](https://docs.python.org/ko/3/tutorial/errors.html#raising-exceptions), [traceback 공식 문서](https://docs.python.org/ko/3/library/traceback.html). 실제 배운 문법의 의미를 확인한 근거다. 예제·표·풀이 자체는 수업 자료를 바탕으로 새로 구성했다. 외부 문장을 직접 인용하지 않았다. 이번 문법 확인 기간: 2026-10-28~29.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 코드.** [실행 파일](실습/책형_복습/14-02_Python_예외발생과_오류추적.py)을 제공한다. Python이 설치된 환경에서 새 .py 파일로 저장해 실행한다. 터미널은 그 파일이 있는 폴더에서 열고 `python 파일이름.py`를 실행한다. VS Code의 Python 실행 기능을 사용해도 된다. 결과는 터미널에 표시된다.



```python
import traceback
def check_fields(user, password):
    if user == '':
        raise Exception('code:1')
    if password == '':
        raise TypeError('code:2')
    return True
for user, password in [('', 'practice'), ('student', ''), ('student', 'practice')]:
    try:
        print('입력 확인', check_fields(user, password))
    except TypeError as error:
        print('객체 직접 비교', error == 'code:2')
        print('메시지 비교', str(error) == 'code:2')
        print('비밀번호 안내')
    except Exception as error:
        if str(error) == 'code:1':
            print('아이디 안내')
try:
    result = 3 / 0
except ZeroDivisionError as error:
    trace = traceback.format_exc()
    print(str(error))
    print('종류가 기록됨', 'ZeroDivisionError' in trace)
```

새 예제는 인증이 아니라 두 필드의 입력 여부만 확인한다. 빈 아이디는 일반 예외 갈래, 빈 비밀번호는 앞의 TypeError 갈래다. 예외 객체 자체와 문자열의 비교는 False지만 str(error)의 메시지 비교는 True다. 마지막은 추적 문자열에 오류 종류가 들어 있음을 확인하여 경로·줄 번호가 다른 환경에서도 핵심을 관찰한다. 원본의 오류 종류 선택을 읽기 위한 예제이며 빈 비밀번호가 보편적으로 TypeError라는 규칙은 아니다.

**예상 출력 또는 관찰:**

```text
아이디 안내
객체 직접 비교 False
메시지 비교 True
비밀번호 안내
입력 확인 True
division by zero
종류가 기록됨 True
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본 발췌다. 주석의 잘못된 설명도 원문을 보존하고 풀이에서 교정한다. 필요한 선언·호출·다른 파일의 정의는 다음 절까지 연결해 읽는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/14_try.py` 94–112행

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

**발췌 바로 풀이:** `loginCheck('admin','1234')`는 성공을 출력하고 `0`을 돌려준다. `login()`은 그 0을 받아 `메인 페이지로 이동`을 출력한다. 빈 아이디이면 `1`을 돌려주도록 했지만, **두 원본의 실제 `login()` 호출은 성공 값으로 고정**되어 있다. 아이디가 비어 있지 않은데 비밀번호만 틀리면 이 함수에는 해당 분기가 없어 `None`을 돌려준다. 따라서 이 코드는 모든 로그인 실패를 구분하는 완성된 로그인 기능이 아니다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/14_try.py` 114–142행

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

**발췌 바로 풀이:** 두 파일의 `loginCheck2`는 빈 아이디에서 `Exception('code:1')`, 빈 비밀번호에서 `TypeError('code:2')`를 발생시킨다. `login2()`가 이를 `try`로 호출하고, **더 구체적인 `TypeError` 처리문을 먼저** 배치했다. 강사님 `login2()`의 입력은 `id='asdf', pw=''`여서 `code:2`가 출력되고 `alert(비밀번호를 입력하세요)`도 출력된다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/14_try.py` 144–153행

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

**발췌 바로 풀이:** `3/0`에서 발생한 오류를 잡아 `print(e)`로 메시지를 보여 준다. `traceback.print_exc()`는 현재 예외의 위치와 호출 흐름을 바로 출력하고, `traceback.format_exc()`는 비슷한 내용을 **문자열로 만들어** `a`에 담는다. 그래서 두 코드는 오류 정보를 한 번은 직접 출력하고, 한 번은 구분선 뒤에 문자열로 다시 출력한다. 이 예제의 `traceback`은 실제 실행 코드이며, 내 파일 끝의 이터레이터·제너레이터·정규표현식은 **간단한 학습 메모**일 뿐 상세 구현이 아니다.

내 loginCheck는 성공이면 0, 빈 아이디면 1이며 나머지 잘못된 자격에는 반환 갈래가 없어 None이다. login2는 빈 비밀번호로 TypeError(code:2)를 발생시키지만 if e==문자열 비교가 거짓이라 메시지만 출력하고 의도한 안내는 안 나온다. 강사님 빈 비밀번호 갈래는 안내를 바로 출력하지만 빈 아이디 갈래에는 같은 객체 비교 문제가 남아 있다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

login 호출 → loginCheck의 반환값 → 0·1 조건 → 터미널 안내다. login2 호출 → try 안 loginCheck2 → 함수의 raise → 호출자 except TypeError 또는 Exception → 메시지 확인 순서다. traceback은 import한 모듈이 제공하며 원본의 두 함수 호출과 새 예제의 format_exc 사용을 구별한다. 예외 이름과 파일·줄·호출 흐름을 함께 읽어 원인을 좁힌다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 내 코드는 구체 TypeError를 넓은 Exception보다 먼저 두고 실제 예외 메시지를 관찰했다. **실제 오류:** 예외 객체와 문자열을 직접 비교한 조건은 의도한 메시지 비교가 아니다. **공통 한계:** 실패 갈래가 빠진 loginCheck와 문자열 코드 정책은 완성 인증이 아니다. **개선:** 오류 종류로 이미 구별했다면 바로 해당 안내를 하거나 str(e)로 의도한 메시지를 비교한다. traceback 출력과 반환도 정확히 이름 붙인다.

개선안은 D 드라이브 원본을 수정한 결과가 아니다. 실제 오류·수업용 단순화·목적에 따른 선택을 구별한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



강사님을 전체 정답으로 묶지 않는다. 빈 비밀번호 실행 경로는 강사님이 안내까지 출력하고 내 코드는 비교 때문에 못 한다. 빈 아이디 경로의 예외 객체와 code:1 문자열 직접 비교는 강사님도 같은 문제다. 실제 실행한 고정 입력과 새로 시험할 다른 입력을 구분하여 비교한다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 입력·상황 | 원본 경로 | 관찰 |
| --- | --- | --- |
| admin·1234 | loginCheck 성공 | 0 반환·이동 문구 출력 |
| 비지 않은 ID·틀린 비밀번호 | 다른 갈래 없음 | None |
| 내 login2의 빈 비밀번호 | TypeError | code:2만, 안내 조건 거짓 |
| 강사님 login2의 빈 비밀번호 | TypeError | code:2와 안내 |
| 빈 아이디 | Exception | 객체와 문자열 비교 교정 필요 |

traceback의 파일 경로·줄 번호·소스 문장은 실행 환경과 파일 편집에 따라 바뀐다. 이를 고정 정답으로 복사하기보다 마지막 예외 종류와 어느 함수 호출에서 올라왔는지를 설명한다.

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| str(error)를 error로 비교 | 메시지 조건 실패 | 객체와 글자 구분 |
| 넓은 Exception 처리문을 먼저 | TypeError도 먼저 잡힘 | 상위 종류가 포함 |
| check_fields 성공 return 제거 | 정상 출력 값 None | 정상 반환 정책 차이 |
| format_exc를 print_exc로 대체해 저장 | 변수에 같은 문자열이 안 담김 | 출력 함수와 반환 함수 |

메시지는 보이는데 조건이 안 맞으면 객체와 문자열을 비교했는지 본다. 안내 글자가 터미널에 보이는 것을 실제 브라우저 이동으로 생각하지 않는다. 추적 정보를 저장하려면 format_exc의 반환값을 사용한다. 빠진 실패 갈래는 입력별 반환표로 찾는다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 업무별 사용자 정의 예외·메시지 대신 구조화한 코드·로깅·인증과 비밀번호 처리 설계는 추가 학습이다. 현재는 실제 raise·except·traceback의 연결과 비교 오류를 이해한다.

TIP은 기본 문제의 필수 조건이 아니다. 배운 문법을 확인한 📚 출처와 선택 확장을 구별한다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. 예외 객체 e와 str(e)는 같은 종류인가?
2. loginCheck의 빠진 실패 갈래는 무엇을 반환하는가?
3. print_exc와 format_exc의 차이는?
4. print로 alert 문구를 쓰면 실제 창이 뜨는가?

<details>
<summary>풀이 — 먼저 자신의 답을 적은 뒤 펼치기</summary>

객체와 문자열로 다르다. 반환문 없이 끝나 None이다. 앞은 추적 출력, 뒤는 추적 문자열 반환이다. 문구만 출력하며 실제 alert 호출은 아니다.

</details>

| 구분 | 확인 |
| --- | --- |
| 상태 | return 값인가 raise인가? |
| 처리 | 구체 종류가 먼저인가? |
| 비교 | 객체인가 메시지인가? |
| 추적 | 출력과 문자열 반환 |

[장별 연습문제](실습/연습문제/14-02_Python_예외발생과_오류추적_연습문제.md) · 다음은 [모듈과 import](15_Python_모듈과_import.md)다.

<!-- 이전 명시 앵커 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
