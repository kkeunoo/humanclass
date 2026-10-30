# 04. 리스트 — 여러 값을 순서대로 담고 바꾸는 방법 — 연습문제

[본문](../../04_Python_리스트와_데이터처리.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원래 수업 퀴즈·당시 내 풀이와 구별한다. 실행 전 예상 → 이유 설명 → 한 가지 수정 순서로 풀어 본다.

## 목표와 실행 조건

리스트의 요소·인덱스·길이를 구별하고 append·extend·insert의 차이를 설명한다. 정렬·뒤집기·삭제의 반환값과 원본 변경을 나누고, 끝 위치의 인덱싱·슬라이싱 차이까지 연결한다.

[전체 Python 파일](../책형_복습/04_Python_리스트와_데이터처리.py)을 새 파일로 실행한다. 입력·준비 파일·import 조건은 [본문 3절](../../04_Python_리스트와_데이터처리.md#example)을 먼저 확인한다. 의도적으로 예외를 관찰하는 예제는 오류 종류와 그 전에 나온 출력도 답에 적는다.

## 문제 1. 결과와 실행 순서 예상



```python
numbers = [3, 1, 2, 1]
print(numbers[0], len(numbers))
numbers.append([9, 10])
print(numbers, len(numbers))
inside = numbers.pop()
print('꺼낸 값', inside)
numbers.extend([4, 5])
result = numbers.sort()
print(numbers, result)
last = numbers.pop()
numbers.insert(0, 100)
numbers.remove(1)
print(numbers, last)
numbers.reverse()
print(numbers)
print(numbers.index(1), numbers.count(1))
print(numbers[len(numbers):])
numbers[len(numbers):] = [500]
print(numbers)
numbers.clear()
print(numbers, len(numbers), not len(numbers))
```

<details>
<summary>힌트와 풀이</summary>

입력·현재 값·실행 순서·반환값·출력 위치를 따로 표시한다.

```text
3 4
[3, 1, 2, 1, [9, 10]] 5
꺼낸 값 [9, 10]
[1, 1, 2, 3, 4, 5] None
[100, 1, 2, 3, 4] 5
[4, 3, 2, 1, 100]
3 1
[]
[4, 3, 2, 1, 100, 500]
[] 0 True
```

중첩 리스트를 하나 append하여 길이는 5가 된다. 이를 pop으로 다시 꺼낸 뒤 숫자만 남은 리스트를 extend·sort한다. 정렬 결과는 numbers에 있고 반환값 result는 None이다. 이후 5를 꺼내고 100을 앞에 넣은 뒤 첫 1만 지운다. reverse 후의 값은 내림차순이 아니라 현재 순서의 반대다. 마지막 clear 뒤 len은 정수 0이고 not len은 boolean True다.

</details>

## 문제 2. 이유를 자신의 말로 설명

1. append([9,10]) 뒤 길이는 두 개 늘어나는가?
2. sort의 반환값과 바뀐 리스트는 같은가?
3. reverse는 항상 내림차순인가?
4. len([])와 not len([])는 각각 무엇인가?

<details>
<summary>풀이</summary>

한 요소가 추가되어 하나 늘어난다. sort는 리스트를 바꾸고 None을 반환한다. reverse는 현재 순서를 뒤집는다. 각각 정수 0과 boolean True다.

| 원본에서 진행한 작업 | 바로 뒤의 상태 | 주의점 |
| --- | --- | --- |
| list(range(6)) | [0,1,2,3,4,5] | 6 제외 |
| del a[3] | [0,1,2,4,5] | 인덱스 3의 값 삭제 |
| +[6]·+=[7]·append(8) | [0,1,2,4,5,6,7,8] | 새 리스트와 변경 구별 |
| append([9,10]) | 마지막 요소가 [9,10] | 바깥 길이 9 |

길이 3일 때 a[3]은 존재하지 않는 요소라 IndexError지만 a[3:]은 빈 구간 []다. a[3:]=[4,5,6]은 끝에 세 항목을 붙인다. 슬라이스가 범위를 벗어나도 여기서 잘린 구간을 줄 수 있다는 사실과 모든 인덱싱이 안전하다는 주장은 다르다. 리스트의 find는 없으며 없는 값의 index·remove는 ValueError다.

</details>

## 문제 3. 한 가지만 바꾸기

본문의 다음 실험에서 한 행만 골라 결과를 먼저 예상한다. 실행 후 원래 예제로 돌아가 다음 변경을 확인한다.

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| append를 extend로 변경 | 9·10이 각각 바깥 요소 | 추가 단위 차이 |
| sort 대신 reverse | 크기순 보장 안 됨 | 현재 순서 뒤집기 |
| 없는 값 remove | ValueError | 일치하는 항목 없음 |
| 빈 리스트에서 pop | IndexError | 꺼낼 요소 없음 |

<details>
<summary>막힐 때 확인할 것</summary>

None이 출력되면 원래 리스트 대신 변경 메서드의 반환값을 출력했는지 본다. 길이를 셀 때 안쪽 리스트가 바깥 요소 하나임을 확인한다. 위치 오류는 길이와 마지막 인덱스를 비교한다. 정렬 오류가 나면 서로 비교할 수 있는 종류의 값인지도 확인한다.

</details>

## 채점과 복습

값만 맞혔는지보다 어떤 입력·분기·호출로 그 결과가 나왔는지 설명한다. 예외·주석·의도한 동작을 혼동하지 않는다. 모르면 연결된 본문의 개념·작은 예제·내 원본 풀이로 돌아간다. TIP의 선택 학습은 필수 정답이 아니다.
