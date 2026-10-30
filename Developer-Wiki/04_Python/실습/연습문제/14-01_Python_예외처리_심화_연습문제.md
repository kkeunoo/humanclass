# 14-01. 예외 처리 — 실패한 작업·처리 갈래·반환 결과 나누기 — 연습문제

[본문](../../14-01_Python_예외처리_심화.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원래 수업 퀴즈·당시 내 풀이와 구별한다. 실행 전 예상 → 이유 설명 → 한 가지 수정 순서로 풀어 본다.

## 목표와 실행 조건

구체적 예외·넓은 처리·예외 객체를 구분한다. 정상 else와 finally, try 안 return의 흐름을 비교하고, 원본의 실제 호출과 주석 호출·실패 대체값을 설명한다.

[전체 Python 파일](../책형_복습/14-01_Python_예외처리_심화.py)을 새 파일로 실행한다. 입력·준비 파일·import 조건은 [본문 3절](../../14-01_Python_예외처리_심화.md#example)을 먼저 확인한다. 의도적으로 예외를 관찰하는 예제는 오류 종류와 그 전에 나온 출력도 답에 적는다.

## 문제 1. 결과와 실행 순서 예상



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

<details>
<summary>힌트와 풀이</summary>

입력·현재 값·실행 순서·반환값·출력 위치를 따로 표시한다.

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

첫 호출은 성공하여 else 뒤 finally, 결과 3.5 반환이다. 0과 문자열 분모는 각 except로 이동해 안내 뒤 finally를 거쳐 None을 반환한다. early_return은 try에서 반환을 시작해 else로 내려오지 않지만 finally는 실행한다. 새 예제의 None 정책은 원본의 0 반환과 구분한 개선·관찰용 선택이다.

</details>

## 문제 2. 이유를 자신의 말로 설명

1. except를 실행하면 실패한 계산이 성공으로 바뀌는가?
2. try 안 return이면 else는?
3. 그 반환 중 finally는?
4. Exception이 KeyboardInterrupt도 모두 잡는가?

<details>
<summary>풀이</summary>

아니다. 오류에 맞춘 처리를 한 것이다. else는 건너뛴다. 이 예제에서는 finally가 실행된다. Exception은 모든 최상위 예외를 포함하지 않는다.

| 원본 함수·입력 | 처리·정상 갈래 | 반환·마지막 작업 |
| --- | --- | --- |
| div3(7,0) | ZeroDivisionError | 0 |
| div4(7,'a') | TypeError 메시지 | 0 |
| div6(7,2) | else | 3.5 |
| div7(7,2) | try 안 return, else 없음 | finally 후 3.5 |
| div7(7,0) | except | finally 후 0 |

except의 순서도 중요하다. 더 넓은 Exception을 앞에 두면 그 안에 속한 구체 예외의 뒤 처리문은 선택되지 않을 수 있다. 모든 오류를 잡는 대신 현재 실패에 맞는 범위를 생각한다.

</details>

## 문제 3. 한 가지만 바꾸기

본문의 다음 실험에서 한 행만 골라 결과를 먼저 예상한다. 실행 후 원래 예제로 돌아가 다음 변경을 확인한다.

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| 분모를 2에서 0으로 | except, else 없음 | 실패 경로 |
| try 안에 return 배치 | 정상이어도 else 건너뜀 | 이미 함수 반환 진행 |
| 넓은 except를 앞에 추가 | 구체 처리문까지 안 갈 수 있음 | 첫 맞는 처리 선택 |
| 실패 초기값을 0으로 변경 | 원본 같은 대체값 정책 | 정상 0과 구분 주의 |

<details>
<summary>막힐 때 확인할 것</summary>

안내 뒤 None이나 0을 받으면 오류 처리와 반환 정책을 함께 본다. else가 안 나오면 예외뿐 아니라 앞의 return도 확인한다. finally 뒤 결과는 대입·return 위치를 따라간다. 중단 신호를 잡으려고 종류 없는 except를 기계적으로 추가하지 않는다.

</details>

## 채점과 복습

값만 맞혔는지보다 어떤 입력·분기·호출로 그 결과가 나왔는지 설명한다. 예외·주석·의도한 동작을 혼동하지 않는다. 모르면 연결된 본문의 개념·작은 예제·내 원본 풀이로 돌아간다. TIP의 선택 학습은 필수 정답이 아니다.
