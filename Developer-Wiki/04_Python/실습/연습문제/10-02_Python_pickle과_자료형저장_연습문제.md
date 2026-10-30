# 10-02. pickle — 문자열 모양이 아니라 Python 값을 저장하기 — 연습문제

[본문](../../10-02_Python_pickle과_자료형저장.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원래 수업 퀴즈·당시 내 풀이와 구별한다. 실행 전 예상 → 이유 설명 → 한 가지 수정 순서로 풀어 본다.

## 목표와 실행 조건

문자열 저장과 직렬화의 차이를 설명한다. import·dump·load·wb·rb를 연결하고 여러 값을 순서대로 읽는 흐름, 파일 끝과 원본 주석의 과도한 일반화를 구별한다.

[전체 Python 파일](../책형_복습/10-02_Python_pickle과_자료형저장.py)을 새 파일로 실행한다. 입력·준비 파일·import 조건은 [본문 3절](../../10-02_Python_pickle과_자료형저장.md#example)을 먼저 확인한다. 의도적으로 예외를 관찰하는 예제는 오류 종류와 그 전에 나온 출력도 답에 적는다.

## 문제 1. 결과와 실행 순서 예상



```python
import pickle
numbers = [1, 2]
profile = {'이름': '민지', '나이': 20}
with open('book_values.p', 'wb') as file:
    pickle.dump(numbers, file)
    pickle.dump(profile, file)
with open('book_values.p', 'rb') as file:
    first = pickle.load(file)
    second = pickle.load(file)
print(first, type(first))
print(second, type(second))
print(second['나이'], type(second['나이']))
text = str(numbers)
print(text, type(text))
print(list(text))
```

<details>
<summary>힌트와 풀이</summary>

입력·현재 값·실행 순서·반환값·출력 위치를 따로 표시한다.

```text
[1, 2] <class 'list'>
{'이름': '민지', '나이': 20} <class 'dict'>
20 <class 'int'>
[1, 2] <class 'str'>
['[', '1', ',', ' ', '2', ']']
```

numbers를 먼저 저장하고 profile을 다음에 저장했으므로 first는 리스트, second는 딕셔너리다. 숫자 나이는 정수로 돌아온다. 반면 str(numbers)의 화면 모양이 같아도 type은 str이며 list(text)는 글자별 목록이다. 현재 예제는 두 값 저장·두 번 읽기를 확인하며 파일의 바이너리 바이트 모양을 고정 정답으로 적지는 않는다.

</details>

## 문제 2. 이유를 자신의 말로 설명

1. 저장한 .p 이름만으로 리스트가 복원되는가?
2. 읽을 변수 이름 age를 쓰면 정수를 골라 읽는가?
3. str(리스트)와 pickle 복원의 종류는?
4. 저장 횟수보다 더 load하면?

<details>
<summary>풀이</summary>

pickle.load가 형식을 읽어야 한다. 변수 이름은 검색 조건이 아니며 파일 순서대로 읽는다. 앞은 문자열이고 pickle 예제는 리스트를 복원한다. 파일 끝이면 EOFError가 날 수 있다.

| 원본 load 차례 | 저장 당시 값 | 읽은 종류 |
| --- | --- | --- |
| 1 | name='eng' | 문자열 |
| 2 | age=20 | 정수 |
| 3 | address='한글' | 문자열 |
| 4 | arr=[1,2,3,4] | 리스트 |
| 5 | scores 딕셔너리 | 딕셔너리 |

여섯 번째 load는 저장한 값이 더 없어 EOFError가 날 수 있다. 원본은 그 줄을 주석으로 두었다. 파일 끝이라고 자동으로 None을 반환하는 일반 조회로 이해하지 않는다. 새로 rb로 열면 다시 처음 값부터 읽는다.

</details>

## 문제 3. 한 가지만 바꾸기

본문의 다음 실험에서 한 행만 골라 결과를 먼저 예상한다. 실행 후 원래 예제로 돌아가 다음 변경을 확인한다.

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| 저장 순서만 교환 | first가 딕셔너리 | 읽는 변수명이 종류를 고르지 않음 |
| load 한 번 추가 | EOFError | 저장 단위를 모두 읽음 |
| profile 나이를 문자열로 | 복원 뒤 str | 저장한 자료형 차이 |
| 두 값을 하나의 dict로 묶어 dump | 한 번 읽은 뒤 키로 구별 | 별도 개선한 저장 약속 |

<details>
<summary>막힐 때 확인할 것</summary>

자료형이 예상과 다르면 dump 순서를 본다. 바이너리 파일을 텍스트 read로 읽는 오류와 pickle 자체의 load를 구별한다. EOFError는 읽은 횟수와 파일 내용을 확인한다. 파일 이름을 바꾸었다면 저장과 읽기 경로도 같은지 확인한다.

</details>

## 채점과 복습

값만 맞혔는지보다 어떤 입력·분기·호출로 그 결과가 나왔는지 설명한다. 예외·주석·의도한 동작을 혼동하지 않는다. 모르면 연결된 본문의 개념·작은 예제·내 원본 풀이로 돌아간다. TIP의 선택 학습은 필수 정답이 아니다.
