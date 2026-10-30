# 14-01. 예외 처리 — 실패한 작업·처리 갈래·반환 결과 나누기

[Python 목차](README.md) · [읽기 안내](00-00_Python_V3_동작_백과_읽기법.md)

오류를 잡았다고 원래 작업이 성공한 것은 아니다. 어느 줄에서 실패했고 어느 except로 갔는지, 그 뒤 호출자가 무엇을 받는지를 함께 읽는다. else·finally·return의 위치도 결과를 바꾼다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

구체적 예외·넓은 처리·예외 객체를 구분한다. 정상 else와 finally, try 안 return의 흐름을 비교하고, 원본의 실제 호출과 주석 호출·실패 대체값을 설명한다.

실제 원본·새 예제·개선안·선택 학습을 구분하고 입력·실행 순서·반환값·출력을 연결한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

try 안에서 예외가 나면 그 줄 뒤의 남은 try 문장을 건너뛰고 맞는 except로 이동한다. 예외 객체를 as error로 받아 메시지를 관찰할 수 있다. except 처리를 마쳤다고 실패한 나눗셈의 결과가 다시 생기지는 않는다.

| 구문 | 실행 조건 | 이 실습의 관찰 |
| --- | --- | --- |
| except ZeroDivisionError | 해당 종류 예외 | 분모 0 |
| except TypeError | 해당 종류 예외 | 맞지 않는 종류의 나눗셈 |
| except Exception | 보통의 넓은 예외 범위 | 모든 BaseException까지는 아님 |
| else | try가 예외 없이 정상 완료 | try 안 return이면 도달하지 않음 |
| finally | 이 예제의 정상·예외·반환 경로 정리 | return 과정에서도 실행 |

종류 없는 except는 매우 넓어 중단 신호까지 잡을 수 있다. 원본을 읽되 모든 실패를 같은 안내로 숨기는 습관으로 일반화하지 않는다. Exception도 KeyboardInterrupt 같은 모든 예외를 포함하는 최상위 이름은 아니다.

원본은 실패할 때 result 초기값 0을 반환한다. 정상 계산 0과 구별하기 어려운 정책이다. 아래 새 예제는 실패를 None으로 표시하여 코드 흐름을 관찰한다. 어떤 반환 정책을 택했는지 호출자와 일치해야 한다.

> 📚 **출처 · 본문 설명 확인:** [Python 예외 처리·else·finally](https://docs.python.org/ko/3/tutorial/errors.html), [예외 계층](https://docs.python.org/ko/3/library/exceptions.html#exception-hierarchy). 실제 배운 문법의 의미를 확인한 근거다. 예제·표·풀이 자체는 수업 자료를 바탕으로 새로 구성했다. 외부 문장을 직접 인용하지 않았다. 이번 문법 확인 기간: 2026-10-28~29.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 코드.** [실행 파일](실습/책형_복습/14-01_Python_예외처리_심화.py)을 제공한다. Python이 설치된 환경에서 새 .py 파일로 저장해 실행한다. 터미널은 그 파일이 있는 폴더에서 열고 `python 파일이름.py`를 실행한다. VS Code의 Python 실행 기능을 사용해도 된다. 결과는 터미널에 표시된다.



```python
def divide(x, y):
    result = None
    try:
        result = x / y
    except ZeroDivisionError as error:
        print('0 나눗셈 처리')
    except TypeError as error:
        print('종류 오류 처리')
    else:
        print('정상 else')
    finally:
        print('정리 finally')
    return result
for x, y in [(7, 2), (7, 0), (7, 'a')]:
    print('반환', divide(x, y))
def early_return():
    try:
        return 10
    except Exception:
        print('예외')
    else:
        print('여기 else는 실행 안 됨')
    finally:
        print('반환 중 finally')
print(early_return())
```

첫 호출은 성공하여 else 뒤 finally, 결과 3.5 반환이다. 0과 문자열 분모는 각 except로 이동해 안내 뒤 finally를 거쳐 None을 반환한다. early_return은 try에서 반환을 시작해 else로 내려오지 않지만 finally는 실행한다. 새 예제의 None 정책은 원본의 0 반환과 구분한 개선·관찰용 선택이다.

**예상 출력 또는 관찰:**

```text
정상 else
정리 finally
반환 3.5
0 나눗셈 처리
정리 finally
반환 None
종류 오류 처리
정리 finally
반환 None
반환 중 finally
10
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본 발췌다. 주석의 잘못된 설명도 원문을 보존하고 풀이에서 교정한다. 필요한 선언·호출·다른 파일의 정의는 다음 절까지 연결해 읽는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/14_try.py` 10–16행

```python
def div2(x, y) :
    result = 0
    try : # Error가 발생하면, 정지하지 않고 except로 내려감
        result = x / y # y에서 Error가 났기 때문에 result로 넘어가지 않고 내려 간 상태
    except :
        print('예외 발생')
    return result
```

**발췌 바로 풀이:** 두 함수 모두 `try`에서 `x / y`를 계산한다. 실패하면 종류를 지정하지 않은 `except`로 내려가 `예외 발생`을 출력하고, 처음 만들어 둔 `result=0`을 돌려준다. 하지만 **두 원본의 실행 구간에서는 `div2(7,0)` 호출이 주석 처리**되어 있어 함수 정의를 읽는 예제다. 이 방식은 어떤 문제가 났는지 구별하기 어렵다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/14_try.py` 18–26행

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

**발췌 바로 풀이:** 두 except는 한 번에 차례로 모두 실행되는 것이 아니다. try에서 발생한 예외에 맞는 갈래로 이동한다. result를 0으로 준비하여 실패한 경우 그 초기값을 반환한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/14_try.py` 28–45행

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

**발췌 바로 풀이:** `div4`는 `ZeroDivisionError`와 `TypeError`를 따로 잡고, `as e`로 해당 예외의 메시지를 함께 출력한다. `div5`는 `Exception as e`로 더 넓은 범위의 보통 오류를 잡는다. 내 주석에도 적혀 있듯 `KeyboardInterrupt`처럼 `Exception`에 포함되지 않는 예외까지 **전부 잡는다는 뜻은 아니다**. 또한 오류를 잡아 출력만 하고 `0`을 돌려주므로, 호출한 쪽에서는 그 0이 정상 계산인지 오류의 대체값인지 구분하기 어렵다. 이 예제에서는 각 방식의 동작을 비교하는 데 집중한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/14_try.py` 46–67행

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

**발췌 바로 풀이:** div6은 성공 시 else에 도달한다. div7은 성공 시 try 안 return으로 else를 건너뛰고 finally를 실행한다. 같은 try가 있다고 성공 경로의 문장이 모두 실행되는 것은 아니다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/14_try.py` 69–90행

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

**발췌 바로 풀이:** 강사님은 `div(7,0)`을 실제로 호출해 안내 뒤 0을 받는다. 내 코드는 그 줄을 주석 처리했다. [00-02 오류 읽기](00-02_Python_오류와_예외.md)에서 확인했듯 내 `div`는 이 경우 초기화되지 않은 `result`를 반환하려 해 오류가 나므로, 전체 파일을 실행할 때 막아 둔 것이 의미가 있다. 두 파일 모두 `div3`부터 `div7`까지 다양한 성공·실패 호출을 해 본다. 숫자 `7/2`는 정상 흐름이고 `7/0`, `7/'a'`는 서로 다른 예외를 시험한다.

내 div2는 넓은 except로 같은 안내를, div4는 두 종류와 메시지를, div5는 Exception으로 넓게 잡는다. div3·div6·div7 정의도 이 장에서 함께 읽도록 가져왔다. 이전 오류 입문 장에는 div의 초기화 차이만 남겼으므로 함수를 다른 장에서 이미 다 봤다고 생략하지 않았다. 실제 호출 구간에서 내 div(7,0)은 주석이며 div(7,3)의 기존 a를 다음 print에서 다시 출력한다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

호출 인자 → 함수의 초기값 → try 계산 → 예외라면 해당 except, 정상 완료면 else → finally → 반환 → 바깥 print 순서다. div7처럼 try 안 return이면 반환 과정에 finally가 끼고 else는 생략된다. 원본 함수 정의와 실제 div3~div7 호출을 함께 보여 주어 입력별 경로를 연결한다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 내 코드는 예외 종류·메시지·정상 else·finally를 서로 다른 함수로 비교했다. **교정:** 오류가 y 자체에서 났다기보다 x/y 연산 중 발생하여 result 대입을 완료하지 못한 것이다. **반환 정책의 한계:** 잡고 0을 주면 호출자는 정상 0과 실패를 모를 수 있다. **설명 범위:** finally의 무조건이라는 말을 프로세스 강제 종료까지 모든 상황을 보장하는 표현으로 확대하지 않는다.

개선안은 D 드라이브 원본을 수정한 결과가 아니다. 실제 오류·수업용 단순화·목적에 따른 선택을 구별한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



두 원본의 div2~div7 원리는 같아 반복 인용하지 않는다. 강사님은 div(7,0)을 실제 호출해 0을 받으며 내 함수는 초기값이 없어 그 호출을 실행하면 다른 예외가 난다. 해당 호출은 내 파일에서 주석이다. 원본 전체의 실행 경로와 별도 함수 실험의 입력을 구분한다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 원본 함수·입력 | 처리·정상 갈래 | 반환·마지막 작업 |
| --- | --- | --- |
| div3(7,0) | ZeroDivisionError | 0 |
| div4(7,'a') | TypeError 메시지 | 0 |
| div6(7,2) | else | 3.5 |
| div7(7,2) | try 안 return, else 없음 | finally 후 3.5 |
| div7(7,0) | except | finally 후 0 |

except의 순서도 중요하다. 더 넓은 Exception을 앞에 두면 그 안에 속한 구체 예외의 뒤 처리문은 선택되지 않을 수 있다. 모든 오류를 잡는 대신 현재 실패에 맞는 범위를 생각한다.

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| 분모를 2에서 0으로 | except, else 없음 | 실패 경로 |
| try 안에 return 배치 | 정상이어도 else 건너뜀 | 이미 함수 반환 진행 |
| 넓은 except를 앞에 추가 | 구체 처리문까지 안 갈 수 있음 | 첫 맞는 처리 선택 |
| 실패 초기값을 0으로 변경 | 원본 같은 대체값 정책 | 정상 0과 구분 주의 |

안내 뒤 None이나 0을 받으면 오류 처리와 반환 정책을 함께 본다. else가 안 나오면 예외뿐 아니라 앞의 return도 확인한다. finally 뒤 결과는 대입·return 위치를 따라간다. 중단 신호를 잡으려고 종류 없는 except를 기계적으로 추가하지 않는다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 사용자 정의 예외 계약·복구와 재시도·예외 체이닝·로깅 전략은 추가 학습이다. 기본은 실제 try·except·else·finally와 반환의 연결이다.

TIP은 기본 문제의 필수 조건이 아니다. 배운 문법을 확인한 📚 출처와 선택 확장을 구별한다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. except를 실행하면 실패한 계산이 성공으로 바뀌는가?
2. try 안 return이면 else는?
3. 그 반환 중 finally는?
4. Exception이 KeyboardInterrupt도 모두 잡는가?

<details>
<summary>풀이 — 먼저 자신의 답을 적은 뒤 펼치기</summary>

아니다. 오류에 맞춘 처리를 한 것이다. else는 건너뛴다. 이 예제에서는 finally가 실행된다. Exception은 모든 최상위 예외를 포함하지 않는다.

</details>

| 단계 | 질문 |
| --- | --- |
| 실패 | 어떤 연산·종류인가? |
| 처리 | 어느 except인가? |
| 정상 | else에 도달했나? |
| 결과 | finally와 반환의 순서 |

[장별 연습문제](실습/연습문제/14-01_Python_예외처리_심화_연습문제.md) · 다음은 [예외 발생·추적](14-02_Python_예외발생과_오류추적.md)이다.

<!-- 이전 명시 앵커 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
