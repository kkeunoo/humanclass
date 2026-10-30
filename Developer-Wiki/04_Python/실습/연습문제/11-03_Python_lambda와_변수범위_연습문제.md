# 11-03. lambda와 이름의 범위 — 함수 값·정렬 기준·안팎 변수 읽기 — 연습문제

[본문](../../11-03_Python_lambda와_변수범위.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원래 수업 퀴즈·당시 내 풀이와 구별한다. 실행 전 예상 → 이유 설명 → 한 가지 수정 순서로 풀어 본다.

## 목표와 실행 조건

def·lambda·map의 결과와 정렬 key 함수를 연결한다. 지역 대입·전역 읽기·global·nonlocal을 실제 범위에서 설명하고 정의만 한 함수와 호출한 함수를 구분한다.

[전체 Python 파일](../책형_복습/11-03_Python_lambda와_변수범위.py)을 새 파일로 실행한다. 입력·준비 파일·import 조건은 [본문 3절](../../11-03_Python_lambda와_변수범위.md#example)을 먼저 확인한다. 의도적으로 예외를 관찰하는 예제는 오류 종류와 그 전에 나온 출력도 답에 적는다.

## 문제 1. 결과와 실행 순서 예상



```python
def double(number):
    return number * 2
double_short = lambda number: number * 2
print(double(3), double_short(3))
print(list(map(lambda number: number + 10, [1, 2])))
people = [{'age': 25}, {'age': 23}, {'age': 30}]
people.sort(key=lambda person: person['age'])
print([person['age'] for person in people])
x = 10
def local_example():
    x = 20
    print('지역', x)
local_example()
print('밖', x)
def change_global():
    global x
    x = 20
change_global()
print('변경 뒤', x)
def outer():
    x = 10
    y = 20
    def middle():
        x = 30
        def inner():
            nonlocal x, y
            print('가까운 x', x)
            print('찾은 y', y)
        inner()
    middle()
outer()
```

<details>
<summary>힌트와 풀이</summary>

입력·현재 값·실행 순서·반환값·출력 위치를 따로 표시한다.

```text
6 6
[11, 12]
[23, 25, 30]
지역 20
밖 10
변경 뒤 20
가까운 x 30
찾은 y 20
```

double과 double_short는 같은 입력에서 6을 반환한다. sort는 나이를 key로 받아 people의 순서를 바꾼다. local_example의 x는 함수 안 값이라 호출 뒤 바깥 x는 10이다. change_global은 모듈 x를 20으로 바꾼다. 중첩 inner의 x는 middle의 30, y는 middle에 없어 outer의 20을 찾는다. 새 예제에서 nonlocal 이름은 읽기만 하며 별도 숨겨진 저장소나 클래스는 없다.

</details>

## 문제 2. 이유를 자신의 말로 설명

1. lambda를 변수에 넣으면 바로 실행되는가?
2. sort의 key 함수는 무엇을 반환해야 하는가?
3. 지역 x를 바꾸면 모듈 x도 항상 바뀌는가?
4. inner의 y는 왜 outer에서 읽는가?

<details>
<summary>풀이</summary>

호출 전에는 실행하지 않는다. 각 항목의 정렬 기준 값을 반환한다. 지역 대입은 별도다. middle에 y가 없어 둘러싼 outer의 기존 이름을 찾기 때문이다.

| 읽는 위치 | x를 찾은 범위 | 값 |
| --- | --- | --- |
| local_example 본문 | 자기 지역 | 20 |
| 그 호출 뒤 모듈 | 모듈 | 10 |
| global 변경 뒤 모듈 | 모듈 | 20 |
| inner의 nonlocal x | middle | 30 |
| inner의 nonlocal y | outer | 20 |

원본의 지역→전역→오류 메모는 모든 이름 검색 단계의 완전한 목록이 아니다. 둘러싼 함수 범위와 Python 내장 이름도 있어 print를 별도 정의하지 않아도 사용할 수 있다. 이 장은 실제 중첩 함수의 이름마다 어디를 읽는지 먼저 확인한다.

</details>

## 문제 3. 한 가지만 바꾸기

본문의 다음 실험에서 한 행만 골라 결과를 먼저 예상한다. 실행 후 원래 예제로 돌아가 다음 변경을 확인한다.

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| local_example 안 x만 40으로 | 안 40·밖 10 | 지역 이름 분리 |
| middle의 x 제거 | inner가 outer의 x=10을 찾음 | 가까운 기존 함수 범위 |
| key의 age를 다른 키로 | 해당 키가 없으면 오류 | 정렬 기준 조회 |
| 함수 호출만 제거 | 그 본문 출력 없음 | 정의와 실행 차이 |

<details>
<summary>막힐 때 확인할 것</summary>

바깥 값이 안 바뀌면 함수 안의 새 지역 대입인지 본다. nonlocal 오류는 둘러싼 함수에 그 이름이 실제 있는지 확인한다. map에 숫자를 넘겼다면 함수 값과 호출 결과를 구분한다. 정렬 함수는 출력만 하는지 값을 반환하는지 본다.

</details>

## 채점과 복습

값만 맞혔는지보다 어떤 입력·분기·호출로 그 결과가 나왔는지 설명한다. 예외·주석·의도한 동작을 혼동하지 않는다. 모르면 연결된 본문의 개념·작은 예제·내 원본 풀이로 돌아간다. TIP의 선택 학습은 필수 정답이 아니다.
