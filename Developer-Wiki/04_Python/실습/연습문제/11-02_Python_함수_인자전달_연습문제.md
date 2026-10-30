# 11-02. 함수 인자 전달 — 풀어서 보내기와 모아서 받기 — 연습문제

[본문](../../11-02_Python_함수_인자전달.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원래 수업 퀴즈·당시 내 풀이와 구별한다. 실행 전 예상 → 이유 설명 → 한 가지 수정 순서로 풀어 본다.

## 목표와 실행 조건

위치·키워드·기본값을 구분한다. 호출의 *·** 풀기와 정의의 *args·**kwargs 모으기를 설명하고, 딕셔너리의 키 전달과 이름에 맞춘 값 전달을 비교한다.

[전체 Python 파일](../책형_복습/11-02_Python_함수_인자전달.py)을 새 파일로 실행한다. 입력·준비 파일·import 조건은 [본문 3절](../../11-02_Python_함수_인자전달.md#example)을 먼저 확인한다. 의도적으로 예외를 관찰하는 예제는 오류 종류와 그 전에 나온 출력도 답에 적는다.

## 문제 1. 결과와 실행 순서 예상



```python
def minus(x, y):
    return x - y
def show_numbers(*values):
    print(values, type(values))
def info(age, name):
    print(age, name)
def show_keywords(**values):
    for key, value in values.items():
        print(key, value)
def greet(name, address='비공개'):
    print(name, address)
print(minus(5, 2))
print(minus(y=5, x=2))
numbers = [1, 2, 3]
show_numbers(*numbers)
show_numbers()
profile = {'name': '민지', 'age': 20}
info(*profile)
info(**profile)
show_keywords(**profile)
greet('민지')
greet('민지', '서울')
```

<details>
<summary>힌트와 풀이</summary>

입력·현재 값·실행 순서·반환값·출력 위치를 따로 표시한다.

```text
3
-3
(1, 2, 3) <class 'tuple'>
() <class 'tuple'>
name age
20 민지
name 민지
age 20
민지 비공개
민지 서울
```

numbers를 풀어 호출한 뒤 show_numbers가 다시 튜플로 모은다. 인자가 없으면 빈 튜플이다. info(*profile)은 키 이름 두 개를 위치 순서로 넣어 name age를 출력한다. info(**profile)은 실제 나이 20·이름 민지를 이름에 맞춰 넣는다. greet의 주소는 생략할 때만 비공개다. 모든 함수 정의와 호출을 한 파일에 보여 주어 외부 정의를 추측할 필요가 없다.

</details>

## 문제 2. 이유를 자신의 말로 설명

1. 정의의 *와 호출의 * 역할은?
2. dict에 *를 쓰면 값이 나오는가?
3. minus(y=5,x=2)는?
4. 기본값은 언제 쓰는가?

<details>
<summary>풀이</summary>

정의는 모으고 호출은 푼다. 딕셔너리의 *는 키를 전달한다. -3이다. 해당 인자를 생략했을 때 기본값을 사용한다.

| 호출 | 연결 | 결과 |
| --- | --- | --- |
| minus(5,2) | x=5,y=2 | 3 |
| minus(y=5,x=2) | x=2,y=5 | -3 |
| info(*profile) | age='name',name='age' | 키 문자열 출력 |
| info(**profile) | age=20,name='민지' | 값 출력 |

풀어 보낼 항목 수와 이름이 함수 정의에 맞아야 한다. 같은 매개변수에 위치·키워드로 중복 값을 주거나 없는 키워드를 주면 TypeError가 날 수 있다. 기본값은 정의에 정한 규칙이지 누락된 필수 인자 전체를 채우는 기능이 아니다.

</details>

## 문제 3. 한 가지만 바꾸기

본문의 다음 실험에서 한 행만 골라 결과를 먼저 예상한다. 실행 후 원래 예제로 돌아가 다음 변경을 확인한다.

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| info의 **를 *로 | 키 문자열이 위치로 들어감 | 전달 규칙 변경 |
| profile 키 age를 years로 | 예상 못한 키워드 오류 | 매개변수 이름 불일치 |
| greet 주소를 명시 | 기본값 대신 전달값 | 생략하지 않은 인자 |
| show_numbers에 리스트를 풀지 않고 전달 | 튜플 안에 리스트 한 개 | 위치 인자 수 차이 |

<details>
<summary>막힐 때 확인할 것</summary>

인자가 부족하면 목록 하나와 여러 값 전달을 구분한다. 출력이 키 이름이면 *와 **를 본다. 기본값이 적용 안 되면 이미 그 자리에 값을 전달했는지 확인한다. 오류 메시지의 매개변수 이름과 실제 def를 나란히 본다.

</details>

## 채점과 복습

값만 맞혔는지보다 어떤 입력·분기·호출로 그 결과가 나왔는지 설명한다. 예외·주석·의도한 동작을 혼동하지 않는다. 모르면 연결된 본문의 개념·작은 예제·내 원본 풀이로 돌아간다. TIP의 선택 학습은 필수 정답이 아니다.
