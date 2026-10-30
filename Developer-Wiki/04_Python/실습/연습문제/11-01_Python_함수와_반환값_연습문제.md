# 11-01. 함수와 반환값 — 화면에 보인 값과 돌려받은 값 나누기 — 연습문제

[본문](../../11-01_Python_함수와_반환값.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원래 수업 퀴즈·당시 내 풀이와 구별한다. 실행 전 예상 → 이유 설명 → 한 가지 수정 순서로 풀어 본다.

## 목표와 실행 조건

def와 호출, 인자·매개변수·return을 연결한다. None·여러 값의 튜플 반환·함수 참조·중첩 호출·가변 리스트 변경과 반환의 차이를 설명한다.

[전체 Python 파일](../책형_복습/11-01_Python_함수와_반환값.py)을 새 파일로 실행한다. 입력·준비 파일·import 조건은 [본문 3절](../../11-01_Python_함수와_반환값.md#example)을 먼저 확인한다. 의도적으로 예외를 관찰하는 예제는 오류 종류와 그 전에 나온 출력도 답에 적는다.

## 문제 1. 결과와 실행 순서 예상



```python
def show_sum(a, b):
    "두 값의 합을 화면에 출력한다."
    print(a + b)
def return_sum(a, b):
    return a + b
def add_sub(a, b):
    return a + b, a - b
def append_four(items):
    items.append(4)
def times_ten(value):
    return value * 10
shown = show_sum(2, 3)
returned = return_sum(2, 3)
print('출력 함수 결과', shown)
print('반환 함수 결과', returned, returned * 2)
pair = add_sub(1, 2)
left, right = pair
print(pair, left, right)
numbers = [1, 2, 3]
changed = append_four(numbers)
print(numbers, changed)
print(times_ten(return_sum(2, 3)))
function_value = return_sum
print(function_value(4, 5))
print(show_sum.__doc__)
```

<details>
<summary>힌트와 풀이</summary>

입력·현재 값·실행 순서·반환값·출력 위치를 따로 표시한다.

```text
5
출력 함수 결과 None
반환 함수 결과 5 10
(3, -1) 3 -1
[1, 2, 3, 4] None
50
9
두 값의 합을 화면에 출력한다.
```

show_sum이 5를 출력한 뒤 shown은 None이다. return_sum의 5는 returned에 담겨 곱셈에 쓸 수 있다. append_four는 None을 돌려주지만 같은 리스트에 붙인 4는 남는다. 중첩 호출은 안쪽 합 5를 먼저 받아 times_ten에 넣어 50을 만든다. return_sum은 괄호 없이 function_value에 전달하고 그 이름으로 나중 호출한다. 함수 첫 문자열은 docstring이며 # 주석이 아니다.

</details>

## 문제 2. 이유를 자신의 말로 설명

1. print만 한 함수의 호출 결과는?
2. return x,y를 하나로 받으면 자료형은?
3. 반환이 None이어도 리스트가 바뀔 수 있는가?
4. fn2(fn1(10))은 어느 함수가 먼저 결과를 만드는가?

<details>
<summary>풀이</summary>

별도 반환이 없으면 None이다. 튜플이다. 같은 리스트 내용을 바꾸면 반환과 별개로 변경이 남는다. 안쪽 fn1이 먼저다.

| 식 | 함수 안에서 일어남 | 호출한 곳에서 받음 |
| --- | --- | --- |
| add(1,2) | 3 출력 | None |
| add2(1,2) | 3 계산·반환 | 3 |
| not_ten(10) | 즉시 값 없이 종료 | None |
| add_sub(1,2) | 합·차 계산 | (3,-1) |
| 내 ref(b) | 같은 리스트 append | None, b 변경은 남음 |

함수 이름만 출력하면 함수를 실행하지 않는다. 함수의 정의가 있다는 사실과 호출 지점에 도달했다는 사실도 다르다. 지역 이름 a2는 local_var 안에서 준비하므로 함수 밖에서 그 이름을 바로 읽을 수 없다.

</details>

## 문제 3. 한 가지만 바꾸기

본문의 다음 실험에서 한 행만 골라 결과를 먼저 예상한다. 실행 후 원래 예제로 돌아가 다음 변경을 확인한다.

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| show_sum에 return 추가 | shown에도 합 | 출력과 반환 둘 다 수행 |
| append_four에서 items를 새 []로 대입 | 원래 numbers는 그대로 | 내용 변경과 이름 재대입 차이 |
| 함수 참조에 괄호 추가 | 즉시 호출 결과를 저장 | 함수 값과 반환값 차이 |
| return 뒤 print 추가 | 그 줄은 안 실행 | 함수 종료 |

<details>
<summary>막힐 때 확인할 것</summary>

None으로 계산하다 오류가 나면 함수가 무엇을 반환하는지 본다. 화면이 비면 반환만 하고 출력하지 않았는지 확인한다. 리스트가 함께 바뀌면 같은 객체 변경인지 본다. NameError는 정의 순서와 이름의 범위를 확인한다.

</details>

## 채점과 복습

값만 맞혔는지보다 어떤 입력·분기·호출로 그 결과가 나왔는지 설명한다. 예외·주석·의도한 동작을 혼동하지 않는다. 모르면 연결된 본문의 개념·작은 예제·내 원본 풀이로 돌아간다. TIP의 선택 학습은 필수 정답이 아니다.
