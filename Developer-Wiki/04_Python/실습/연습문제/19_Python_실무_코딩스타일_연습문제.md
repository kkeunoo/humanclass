# 19. 실무 코딩스타일 — 이름·처리 단계·반환값으로 의도를 보이기 — 연습문제

[본문](../../19_Python_실무_코딩스타일.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원래 수업 퀴즈·당시 내 풀이와 구별한다. 실행 전 예상 → 이유 설명 → 한 가지 수정 순서로 풀어 본다.

## 목표와 실행 조건

값을 계산하는 함수와 출력 위치를 구분한다. 의미 있는 이름·작은 처리 단계·일관된 공백으로 읽기 쉽게 만들고, 스타일 변경과 입력 검증 추가처럼 동작이 바뀌는 변경을 나눈다.

[전체 Python 파일](../책형_복습/19_Python_실무_코딩스타일.py)을 새 파일로 실행한다. 입력·준비 파일·import 조건은 [본문 3절](../../19_Python_실무_코딩스타일.md#example)을 먼저 확인한다. 의도적으로 예외를 관찰하는 예제는 오류 종류와 그 전에 나온 출력도 답에 적는다.

## 문제 1. 결과와 실행 순서 예상



```python
def parse_order(line):
    parts = [part.strip() for part in line.split(',')]
    if len(parts) != 3:
        return None
    try:
        quantity = int(parts[1])
        price = int(parts[2].replace('원', ''))
    except ValueError:
        return None
    if quantity < 0 or price < 0 or price > 10000:
        return None
    return [parts[0], quantity, price]

def collect_orders(lines):
    accepted = []
    sales = 0
    for line in lines:
        order = parse_order(line)
        if order is None:
            continue
        accepted.append(order)
        sales += order[1] * order[2]
    return accepted, sales

rows = [' 사과 , 2, 3000원', '배, -1, 4000원', '귤, 3, 2000원']
orders, total = collect_orders(rows)
print(orders)
print(total)
```

<details>
<summary>힌트와 풀이</summary>

입력·현재 값·실행 순서·반환값·출력 위치를 따로 표시한다.

```text
[['사과', 2, 3000], ['귤', 3, 2000]]
12000
```

collect_orders가 첫 줄을 parse_order에 넘기면 사과·2·3000의 목록이 돌아온다. 이를 accepted에 넣고 6000을 더한다. 배는 범위 검사에서 None을 반환하므로 continue로 건너뛴다. 귤을 처리한 뒤 두 결과를 튜플로 돌려주고 바깥에서 orders·total에 나눠 받는다. 함수 안에서는 출력하지 않아 계산 결과를 다른 코드에서도 사용할 수 있다. 원본 과제를 새 함수로 재구성한 개선 예제이며 당시 코드가 아니다.

</details>

## 문제 2. 이유를 자신의 말로 설명

1. parse_order가 잘못된 행에 돌려주는 값은?
2. collect_orders 반환은 두 번 일어나는가?
3. 이름 변경과 잘못된 행 제외는 모두 스타일 변경인가?
4. 함수 안 print만으로 sales에 더할 값을 받을 수 있는가?

<details>
<summary>풀이</summary>

None이다. 한 번에 두 항목 튜플을 반환한다. 잘못된 행 제외는 처리 동작을 보완한 것이다. print만 하는 함수는 보통 None을 반환하므로 숫자를 return해야 한다.

| 호출 | 입력 | 반환 | 다음 처리 |
| --- | --- | --- | --- |
| parse_order | 사과 한 줄 | [사과,2,3000] | 저장·6000 누적 |
| parse_order | 배 음수 수량 | None | 다음 줄 |
| parse_order | 귤 한 줄 | [귤,3,2000] | 저장·6000 누적 |
| collect_orders | 세 줄 | 목록과 12000 | 나눠 받아 출력 |

</details>

## 문제 3. 한 가지만 바꾸기

본문의 다음 실험에서 한 행만 골라 결과를 먼저 예상한다. 실행 후 원래 예제로 돌아가 다음 변경을 확인한다.

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| rows를 빈 목록으로 | 빈 주문·0원 | 누적 초기값 유지 |
| 배 수량을 1로 | 배도 유지·합계 16000 | 조건 통과 |
| parse_order의 정상 return을 print로 | 호출 결과 None | 계산 결과 전달이 끊김 |
| quantity 이름만 일관되게 변경 | 출력 동일 | 이름 변경 |

<details>
<summary>막힐 때 확인할 것</summary>

NoneType 관련 오류면 반환이 빠진 경로를 본다. 함수 안에서 print가 나왔다고 호출한 곳에 값이 전달됐다고 판단하지 않는다. 이름을 바꿀 때 정의만 바꾸고 사용 부분을 남기지 않았는지 확인한다. 예외를 전부 숨기기보다 숫자 변환처럼 실패가 예상되는 작은 범위에서 처리한다.

</details>

## 채점과 복습

값만 맞혔는지보다 어떤 입력·분기·호출로 그 결과가 나왔는지 설명한다. 예외·주석·의도한 동작을 혼동하지 않는다. 모르면 연결된 본문의 개념·작은 예제·내 원본 풀이로 돌아간다. TIP의 선택 학습은 필수 정답이 아니다.
