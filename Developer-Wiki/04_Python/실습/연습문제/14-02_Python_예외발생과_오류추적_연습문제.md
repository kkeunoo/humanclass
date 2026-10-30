# 14-02. raise와 traceback — 반환 대신 오류를 올리고 위치를 읽기 — 연습문제

[본문](../../14-02_Python_예외발생과_오류추적.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원래 수업 퀴즈·당시 내 풀이와 구별한다. 실행 전 예상 → 이유 설명 → 한 가지 수정 순서로 풀어 본다.

## 목표와 실행 조건

return 상태와 raise 전파를 비교한다. 구체 예외 우선 처리·str(e) 비교·누락된 반환 갈래를 설명하고 print_exc와 format_exc의 출력·반환 차이를 연결한다.

[전체 Python 파일](../책형_복습/14-02_Python_예외발생과_오류추적.py)을 새 파일로 실행한다. 입력·준비 파일·import 조건은 [본문 3절](../../14-02_Python_예외발생과_오류추적.md#example)을 먼저 확인한다. 의도적으로 예외를 관찰하는 예제는 오류 종류와 그 전에 나온 출력도 답에 적는다.

## 문제 1. 결과와 실행 순서 예상



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

<details>
<summary>힌트와 풀이</summary>

입력·현재 값·실행 순서·반환값·출력 위치를 따로 표시한다.

```text
아이디 안내
객체 직접 비교 False
메시지 비교 True
비밀번호 안내
입력 확인 True
division by zero
종류가 기록됨 True
```

새 예제는 인증이 아니라 두 필드의 입력 여부만 확인한다. 빈 아이디는 일반 예외 갈래, 빈 비밀번호는 앞의 TypeError 갈래다. 예외 객체 자체와 문자열의 비교는 False지만 str(error)의 메시지 비교는 True다. 마지막은 추적 문자열에 오류 종류가 들어 있음을 확인하여 경로·줄 번호가 다른 환경에서도 핵심을 관찰한다. 원본의 오류 종류 선택을 읽기 위한 예제이며 빈 비밀번호가 보편적으로 TypeError라는 규칙은 아니다.

</details>

## 문제 2. 이유를 자신의 말로 설명

1. 예외 객체 e와 str(e)는 같은 종류인가?
2. loginCheck의 빠진 실패 갈래는 무엇을 반환하는가?
3. print_exc와 format_exc의 차이는?
4. print로 alert 문구를 쓰면 실제 창이 뜨는가?

<details>
<summary>풀이</summary>

객체와 문자열로 다르다. 반환문 없이 끝나 None이다. 앞은 추적 출력, 뒤는 추적 문자열 반환이다. 문구만 출력하며 실제 alert 호출은 아니다.

| 입력·상황 | 원본 경로 | 관찰 |
| --- | --- | --- |
| admin·1234 | loginCheck 성공 | 0 반환·이동 문구 출력 |
| 비지 않은 ID·틀린 비밀번호 | 다른 갈래 없음 | None |
| 내 login2의 빈 비밀번호 | TypeError | code:2만, 안내 조건 거짓 |
| 강사님 login2의 빈 비밀번호 | TypeError | code:2와 안내 |
| 빈 아이디 | Exception | 객체와 문자열 비교 교정 필요 |

traceback의 파일 경로·줄 번호·소스 문장은 실행 환경과 파일 편집에 따라 바뀐다. 이를 고정 정답으로 복사하기보다 마지막 예외 종류와 어느 함수 호출에서 올라왔는지를 설명한다.

</details>

## 문제 3. 한 가지만 바꾸기

본문의 다음 실험에서 한 행만 골라 결과를 먼저 예상한다. 실행 후 원래 예제로 돌아가 다음 변경을 확인한다.

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| str(error)를 error로 비교 | 메시지 조건 실패 | 객체와 글자 구분 |
| 넓은 Exception 처리문을 먼저 | TypeError도 먼저 잡힘 | 상위 종류가 포함 |
| check_fields 성공 return 제거 | 정상 출력 값 None | 정상 반환 정책 차이 |
| format_exc를 print_exc로 대체해 저장 | 변수에 같은 문자열이 안 담김 | 출력 함수와 반환 함수 |

<details>
<summary>막힐 때 확인할 것</summary>

메시지는 보이는데 조건이 안 맞으면 객체와 문자열을 비교했는지 본다. 안내 글자가 터미널에 보이는 것을 실제 브라우저 이동으로 생각하지 않는다. 추적 정보를 저장하려면 format_exc의 반환값을 사용한다. 빠진 실패 갈래는 입력별 반환표로 찾는다.

</details>

## 채점과 복습

값만 맞혔는지보다 어떤 입력·분기·호출로 그 결과가 나왔는지 설명한다. 예외·주석·의도한 동작을 혼동하지 않는다. 모르면 연결된 본문의 개념·작은 예제·내 원본 풀이로 돌아간다. TIP의 선택 학습은 필수 정답이 아니다.
