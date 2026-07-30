# Python Quiz 01 - 리스트, 딕셔너리, 조건문, 반복문

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `Quiz_01_리스트_딕셔너리_조건문_반복문.md` |
| 분류 | `04_Python/Quiz` |
| 원본 기준 | `workspace_python/quiz/01_quiz.py` |
| 연결 문서 | `04_Python_리스트와_컴프리헨션.md`, `07_Python_딕셔너리와_집합.md`, `08_Python_조건문.md`, `09_Python_반복문.md` |
| 핵심 범위 | 리스트 순회, 짝수·홀수 판별, 누적 합계, 중첩 딕셔너리, `for`, `while`, `if-elif-else`, 사용자 입력, 로그인 검증, 난수, 투표 집계 |
| 문제 수 | 5개 |

> 이 문서는 `workspace_python/quiz/01_quiz.py`에 작성된 문제와 풀이를 기준으로 구성했습니다. 원본의 문제 순서와 핵심 의도는 유지하고, 주석 처리된 코드와 미완성된 부분은 별도로 구분해 설명합니다.

---

# 학습 목표

- 리스트를 반복하면서 조건에 맞는 값을 새 리스트에 저장할 수 있다.
- 나머지 연산자로 짝수와 홀수를 구분할 수 있다.
- 반복문 안에서 합계를 누적할 수 있다.
- 중첩 딕셔너리에서 원하는 값을 조회할 수 있다.
- 상품 가격과 개수를 이용해 전체 금액을 계산할 수 있다.
- `while`을 사용해 정답을 맞힐 때까지 반복할 수 있다.
- 난수와 사용자 입력을 비교해 UP/DOWN 게임을 구현할 수 있다.
- 딕셔너리의 키 존재 여부와 비밀번호를 단계적으로 검사할 수 있다.
- 반복문과 조건문으로 랜덤 투표 수를 집계할 수 있다.
- 여러 후보의 득표 수를 비교해 최다 득표자를 구할 수 있다.

---

# 1. 원본 문제 구성

```text
문제 1
숫자 리스트에서 짝수 리스트와 홀수 합 구하기

문제 2
중첩 딕셔너리 장바구니의 전체 가격 구하기

문제 3
UP/DOWN 게임과 시도 횟수 출력

문제 4
딕셔너리를 이용한 로그인 검사

문제 5
100번 랜덤 투표 결과와 최다 득표자 구하기
```

문제별 핵심 개념:

| 문제 | 핵심 개념 |
| --- | --- |
| 문제 1 | 리스트, `for`, 인덱스, `%`, `append()`, 누적 합계 |
| 문제 2 | 중첩 딕셔너리, 키 순회, 산술 연산, 누적 합계 |
| 문제 3 | `random`, `while`, 사용자 입력, 조건문, 횟수 집계 |
| 문제 4 | 딕셔너리 조회, `in`, 중첩 조건문, 사용자 입력 |
| 문제 5 | 난수, 반복문, 조건문, 투표 집계, 최댓값 |

---

# 2. 문제 1 - 짝수 리스트와 홀수 합

## 문제

```python
numbers = [3, 7, 10, 15, 22, 8, 13]
```

다음을 구현하세요.

```text
1-1. 짝수만 따로 리스트로 만들어 출력
1-2. 홀수의 합 출력
```

---

## 원본 풀이

```python
numbers = [3, 7, 10, 15, 22, 8, 13]

double = []
single = []
singleResult = 0

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        double.append(numbers[i])
    else:
        single.append(numbers[i])
        singleResult += numbers[i]

print(f'짝수 : {double}, {type(double)}')
print(f'홀수 : {single}, {type(single)}')
print(f'홀수의 합 : {singleResult}')
```

---

## 실행 결과

```text
짝수 : [10, 22, 8], <class 'list'>
홀수 : [3, 7, 15, 13], <class 'list'>
홀수의 합 : 38
```

---

## 풀이 분석

```python
for i in range(len(numbers)):
```

`i`에는 리스트의 인덱스가 차례대로 저장됩니다.

```text
0, 1, 2, 3, 4, 5, 6
```

따라서 현재 값은 다음처럼 조회합니다.

```python
numbers[i]
```

짝수 판별:

```python
numbers[i] % 2 == 0
```

숫자를 `2`로 나눈 나머지가 `0`이면 짝수입니다.

홀수 누적:

```python
singleResult += numbers[i]
```

현재 홀수 값을 기존 합계에 계속 더합니다.

---

## 개선 풀이

값이 필요한 경우 인덱스를 만들지 않고 리스트를 직접 순회할 수 있습니다.

```python
numbers = [3, 7, 10, 15, 22, 8, 13]

even_numbers = []
odd_numbers = []
odd_total = 0

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)
        odd_total += number

print(f"짝수: {even_numbers}")
print(f"홀수: {odd_numbers}")
print(f"홀수의 합: {odd_total}")
```

원본 풀이도 정상적으로 동작하지만, 현재 값만 필요하다면 직접 순회가 더 간결합니다.

---

## 핵심 확인

```text
짝수
→ number % 2 == 0

홀수
→ number % 2 != 0

리스트 추가
→ append()

누적 합계
→ total += value
```

---

# 3. 문제 2 - 장바구니 전체 가격

## 문제

```python
cart = {
    '사과': {
        '가격': 1000,
        '개수': 3
    },
    '바나나': {
        '가격': 2000,
        '개수': 4
    },
    '복숭아': {
        '가격': 1500,
        '개수': 2
    },
    '키위': {
        '가격': 2200,
        '개수': 5
    }
}
```

모든 상품을 구매했을 때의 전체 가격을 구하세요.

---

## 원본 풀이

```python
fruitPrice = 0

for i in cart.keys():
    fruitPrice += cart[i]['가격'] * cart[i]['개수']

print(f'총액 : {fruitPrice}')
```

---

## 실행 결과

```text
총액 : 25000
```

상품별 계산:

| 상품 | 계산 | 금액 |
| --- | --- | ---: |
| 사과 | `1000 × 3` | 3,000원 |
| 바나나 | `2000 × 4` | 8,000원 |
| 복숭아 | `1500 × 2` | 3,000원 |
| 키위 | `2200 × 5` | 11,000원 |
| 합계 |  | 25,000원 |

---

## 풀이 분석

```python
for i in cart.keys():
```

`i`에는 최상위 딕셔너리의 키가 차례대로 들어갑니다.

```text
사과
바나나
복숭아
키위
```

각 상품의 가격 조회:

```python
cart[i]['가격']
```

각 상품의 개수 조회:

```python
cart[i]['개수']
```

상품별 금액:

```python
cart[i]['가격'] * cart[i]['개수']
```

전체 합계:

```python
fruitPrice += ...
```

---

## 개선 풀이

딕셔너리를 직접 순회하면 기본적으로 키가 나옵니다.

```python
total_price = 0

for product_name in cart:
    price = cart[product_name]['가격']
    quantity = cart[product_name]['개수']
    total_price += price * quantity

print(f"총액: {total_price}원")
```

`items()`를 사용하면 상품 이름과 내부 딕셔너리를 함께 받을 수 있습니다.

```python
total_price = 0

for product_name, product in cart.items():
    product_total = product['가격'] * product['개수']
    total_price += product_total

    print(f"{product_name}: {product_total}원")

print(f"총액: {total_price}원")
```

---

## 핵심 확인

```text
cart[상품명]
→ 해당 상품의 내부 딕셔너리

cart[상품명]['가격']
→ 가격

cart[상품명]['개수']
→ 개수

가격 × 개수
→ 상품별 금액
```

---

# 4. 문제 3 - UP/DOWN 게임

## 문제

```text
1부터 100 사이의 정답을 무작위로 생성한다.
사용자가 숫자를 입력한다.
정답보다 작으면 UP을 출력한다.
정답보다 크면 DOWN을 출력한다.
정답을 맞히면 시도 횟수를 출력한다.
```

---

## 원본 풀이

원본에서는 전체 코드가 주석 처리되어 있습니다.

```python
import random

com = random.randint(1, 100)
user = -1
count = 0

while com != user:
    user = int(input('숫자를 입력하세요.'))

    if com > user:
        print('UP 입니다.')
        count += 1
    elif com < user:
        print('DOWN 입니다.')
        count += 1
    elif com == user:
        print(f'정답입니다! 시도횟수 : {count}')
```

---

## 원본 코드의 시도 횟수

원본에서는 오답일 때만 `count += 1`을 실행합니다.

따라서 정답 입력은 횟수에 포함되지 않습니다.

예를 들어 세 번째 입력에서 맞혔다면 원본 결과는:

```text
시도횟수 : 2
```

가 됩니다.

일반적으로 “몇 번째 시도에 맞혔는가”를 출력하려면 정답 입력도 포함해야 합니다.

---

## 개선 풀이

```python
import random

answer = random.randint(1, 100)
count = 0

while True:
    user_number = int(input("1부터 100 사이의 숫자를 입력하세요: "))
    count += 1

    if user_number < answer:
        print("UP입니다.")
    elif user_number > answer:
        print("DOWN입니다.")
    else:
        print(f"정답입니다! {count}번째 시도에 맞혔습니다.")
        break
```

---

## 실행 흐름

```text
정답 생성
→ 사용자 입력
→ 시도 횟수 증가
→ 입력값과 정답 비교
→ 작으면 UP
→ 크면 DOWN
→ 같으면 정답 출력 후 break
```

---

## 입력 범위 검증을 추가한 풀이

```python
import random

answer = random.randint(1, 100)
count = 0

while True:
    user_number = int(input("1부터 100 사이의 숫자를 입력하세요: "))

    if not 1 <= user_number <= 100:
        print("1부터 100 사이의 숫자만 입력하세요.")
        continue

    count += 1

    if user_number < answer:
        print("UP입니다.")
    elif user_number > answer:
        print("DOWN입니다.")
    else:
        print(f"정답입니다! {count}번째 시도에 맞혔습니다.")
        break
```

---

# 5. 문제 4 - 로그인 검사

## 문제

```python
users = {
    "admin": "1234",
    "guest": "guest",
    "user1": "abcd"
}
```

아이디와 비밀번호를 입력받아 다음 중 하나를 출력하세요.

```text
아이디가 틀립니다.
비밀번호가 틀렸습니다.
로그인 성공!
```

---

## 원본의 첫 번째 접근

원본에는 아이디별로 조건을 나누는 코드가 주석 처리되어 있습니다.

```python
if logID in users.keys() and logID == 'admin':
    if logPW in users.values() and logPW == '1234':
        print('당신어드민~로그인 성공~')
    else:
        print('패스워드가 틀렸습니다.')
elif logID in users.keys() and logID == 'guest':
    ...
elif logID in users.keys() and logID == 'user1':
    ...
else:
    print('아이디가 틀렸습니다.')
```

이 방식은 사용자 계정이 추가될 때마다 새로운 `elif`가 필요합니다.

또한 비밀번호가 전체 `values()` 안에 있는지 확인하는 것만으로는 현재 아이디의 비밀번호인지 보장할 수 없습니다.

---

## 원본의 최종 풀이

```python
logID = str(input('ID를 입력하세요 : '))
logPW = str(input('PW를 입력하세요 : '))

if logID in users.keys():
    if logPW == users[logID]:
        print('로그인 성공!')
    else:
        print('비밀번호가 틀렸습니다.')
else:
    print('아이디가 틀렸습니다.')
```

---

## 풀이 분석

아이디 존재 검사:

```python
logID in users.keys()
```

딕셔너리에서 `in`은 기본적으로 키를 검사하므로 다음처럼 작성해도 같습니다.

```python
logID in users
```

현재 아이디의 비밀번호 조회:

```python
users[logID]
```

입력 비밀번호 비교:

```python
logPW == users[logID]
```

---

## 개선 풀이

```python
users = {
    "admin": "1234",
    "guest": "guest",
    "user1": "abcd",
}

login_id = input("ID를 입력하세요: ")
login_password = input("PW를 입력하세요: ")

if login_id not in users:
    print("아이디가 틀렸습니다.")
elif login_password != users[login_id]:
    print("비밀번호가 틀렸습니다.")
else:
    print("로그인 성공!")
```

중첩 조건문 대신 `if-elif-else`로도 동일한 흐름을 표현할 수 있습니다.

---

## `str(input())`가 필요한가?

```python
logID = str(input(...))
```

`input()`은 원래 문자열을 반환하므로 `str()` 변환은 생략할 수 있습니다.

```python
logID = input(...)
```

---

# 6. 문제 5 - 랜덤 투표 시스템

## 문제

```text
후보 a, b, c 중 한 명에게 무작위로 투표한다.
총 100번 투표한다.
각 후보의 득표 수를 출력한다.
가장 많은 표를 받은 후보 이름과 득표 수를 출력한다.
```

---

## 원본 풀이

```python
import random

keys = input('나나')
key = keys.split(' ')

a = 0
b = 0
c = 0

for i in range(0, 100):
    vote = random.randint(1, 3)

    if vote == 1:
        a += 1
    elif vote == 2:
        b += 1
    elif vote == 3:
        c += 1

print(a, b, c)
print(keys)
print(key)
print(vote)
```

---

## 원본 구현 상태

원본은 다음 부분까지 구현되어 있습니다.

```text
100번 반복
1~3 사이의 난수 생성
후보별 득표 수 증가
각 후보의 최종 득표 수 출력
```

하지만 다음 요구 사항은 아직 완성되지 않았습니다.

```text
가장 많은 표를 받은 후보 이름 출력
최다 득표 수 출력
동점 처리
```

또한 다음 입력은 투표 집계와 직접 연결되어 있지 않습니다.

```python
keys = input('나나')
key = keys.split(' ')
```

마지막의:

```python
print(vote)
```

는 100번째 반복에서 생성된 마지막 난수만 출력합니다.

---

## 기본 완성 풀이

```python
import random

votes = {
    "a": 0,
    "b": 0,
    "c": 0,
}

candidates = list(votes.keys())

for _ in range(100):
    selected = random.choice(candidates)
    votes[selected] += 1

winner = max(votes, key=votes.get)

print(f"투표 결과: {votes}")
print(f"최다 득표자: {winner}")
print(f"득표 수: {votes[winner]}")
```

---

## 원본 구조를 유지한 완성 풀이

```python
import random

a = 0
b = 0
c = 0

for _ in range(100):
    vote = random.randint(1, 3)

    if vote == 1:
        a += 1
    elif vote == 2:
        b += 1
    else:
        c += 1

results = {
    "a": a,
    "b": b,
    "c": c,
}

winner = max(results, key=results.get)

print(f"a: {a}표")
print(f"b: {b}표")
print(f"c: {c}표")
print(f"최다 득표자: {winner}, {results[winner]}표")
```

---

## 동점 처리 풀이

`max()`만 사용하면 최댓값을 가진 첫 번째 후보 하나만 반환합니다.

동점 후보를 모두 찾으려면 다음처럼 작성할 수 있습니다.

```python
import random

votes = {
    "a": 0,
    "b": 0,
    "c": 0,
}

for _ in range(100):
    selected = random.choice(list(votes))
    votes[selected] += 1

max_votes = max(votes.values())
winners = []

for candidate, count in votes.items():
    if count == max_votes:
        winners.append(candidate)

print(f"투표 결과: {votes}")
print(f"최다 득표 수: {max_votes}표")
print(f"최다 득표자: {winners}")
```

---

# 7. 원본 코드에서 확인할 부분

## 7.1 문제 1의 변수명

```python
double
single
singleResult
```

동작에는 문제가 없지만 의미를 더 명확하게 표현하려면 다음과 같이 작성할 수 있습니다.

```python
even_numbers
odd_numbers
odd_total
```

---

## 7.2 문제 2의 `keys()`

```python
for i in cart.keys():
```

정상적인 코드입니다.

다만 딕셔너리를 직접 순회해도 키가 반환됩니다.

```python
for i in cart:
```

---

## 7.3 문제 3의 시도 횟수

```python
count += 1
```

이 문장이 오답 분기 안에만 있으므로 정답 입력 횟수가 제외됩니다.

“몇 번째 시도”를 출력하려면 입력 직후 증가시키는 편이 자연스럽습니다.

---

## 7.4 문제 4의 `keys()`와 `values()`

```python
logID in users.keys()
```

은 사용할 수 있지만 다음 표현이 더 간결합니다.

```python
logID in users
```

비밀번호 검사는 전체 값 목록이 아니라 현재 아이디의 값과 비교해야 합니다.

```python
logPW == users[logID]
```

---

## 7.5 문제 5의 미완성 부분

원본은 후보별 득표 수까지 계산하지만 최다 득표자 선택은 구현되지 않았습니다.

```python
max(results, key=results.get)
```

또는 최댓값과 반복문을 조합해 완성할 수 있습니다.

---

# 8. 종합 문제

## 문제 1

다음 리스트에서 짝수의 합과 홀수 리스트를 구하세요.

```python
numbers = [12, 7, 5, 20, 9, 14]
```

---

## 문제 2

다음 장바구니의 전체 수량과 전체 가격을 구하세요.

```python
cart = {
    "연필": {"가격": 500, "개수": 4},
    "노트": {"가격": 1500, "개수": 3},
    "지우개": {"가격": 700, "개수": 2},
}
```

---

## 문제 3

UP/DOWN 게임에서 사용자가 범위를 벗어난 숫자를 입력하면 시도 횟수에 포함하지 않도록 작성하세요.

---

## 문제 4

다음 사용자 정보로 로그인을 검사하세요.

```python
users = {
    "kim": "1111",
    "lee": "2222",
    "park": "3333",
}
```

아이디가 없을 때, 비밀번호가 다를 때, 로그인에 성공했을 때를 구분하세요.

---

## 문제 5

후보 이름을 공백으로 입력받고, 입력된 후보 중 한 명에게 총 200번 무작위 투표하도록 작성하세요.

입력 예:

```text
철수 영희 민수
```

출력 항목:

```text
후보별 득표 수
최다 득표 수
최다 득표 후보 전체
```

---

# 9. 종합 문제 정답

## 정답 1

```python
numbers = [12, 7, 5, 20, 9, 14]

even_total = 0
odd_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_total += number
    else:
        odd_numbers.append(number)

print(even_total)
print(odd_numbers)
```

---

## 정답 2

```python
cart = {
    "연필": {"가격": 500, "개수": 4},
    "노트": {"가격": 1500, "개수": 3},
    "지우개": {"가격": 700, "개수": 2},
}

total_quantity = 0
total_price = 0

for product in cart.values():
    total_quantity += product["개수"]
    total_price += product["가격"] * product["개수"]

print(f"전체 수량: {total_quantity}")
print(f"전체 가격: {total_price}원")
```

---

## 정답 3

```python
import random

answer = random.randint(1, 100)
count = 0

while True:
    user_number = int(input("숫자 입력: "))

    if not 1 <= user_number <= 100:
        print("범위를 벗어났습니다.")
        continue

    count += 1

    if user_number < answer:
        print("UP")
    elif user_number > answer:
        print("DOWN")
    else:
        print(f"정답! {count}번째 시도")
        break
```

---

## 정답 4

```python
users = {
    "kim": "1111",
    "lee": "2222",
    "park": "3333",
}

login_id = input("ID: ")
login_password = input("PW: ")

if login_id not in users:
    print("아이디가 틀립니다.")
elif users[login_id] != login_password:
    print("비밀번호가 틀렸습니다.")
else:
    print("로그인 성공!")
```

---

## 정답 5

```python
import random

candidate_input = input("후보 이름을 공백으로 구분해 입력하세요: ")
candidates = candidate_input.split()

votes = {}

for candidate in candidates:
    votes[candidate] = 0

for _ in range(200):
    selected = random.choice(candidates)
    votes[selected] += 1

max_votes = max(votes.values())
winners = []

for candidate, count in votes.items():
    if count == max_votes:
        winners.append(candidate)

print(f"투표 결과: {votes}")
print(f"최다 득표 수: {max_votes}")
print(f"최다 득표 후보: {winners}")
```

---

# 10. Final Checklist

- [ ] 리스트의 값을 반복문으로 순회할 수 있다.
- [ ] `% 2`로 짝수와 홀수를 구분할 수 있다.
- [ ] 조건에 맞는 값을 `append()`로 새 리스트에 추가할 수 있다.
- [ ] 반복문에서 합계를 누적할 수 있다.
- [ ] 중첩 딕셔너리에서 가격과 개수를 조회할 수 있다.
- [ ] 가격과 개수를 곱해 상품별 금액을 계산할 수 있다.
- [ ] 여러 상품의 금액을 누적해 전체 가격을 구할 수 있다.
- [ ] `random.randint()`로 정수 난수를 만들 수 있다.
- [ ] `while`로 정답을 맞힐 때까지 반복할 수 있다.
- [ ] `break`로 반복문을 종료할 수 있다.
- [ ] `continue`로 현재 반복을 건너뛸 수 있다.
- [ ] 시도 횟수를 정확한 위치에서 증가시킬 수 있다.
- [ ] 딕셔너리에서 아이디 존재 여부를 검사할 수 있다.
- [ ] 현재 아이디에 연결된 비밀번호를 조회할 수 있다.
- [ ] 아이디 오류와 비밀번호 오류를 구분할 수 있다.
- [ ] 난수 결과에 따라 후보별 득표 수를 증가시킬 수 있다.
- [ ] `max()`로 최다 득표 수 또는 후보를 찾을 수 있다.
- [ ] 최댓값이 같은 동점 후보를 모두 찾을 수 있다.
- [ ] 원본 코드의 미완성 부분을 구분하고 보완할 수 있다.

---

# 11. Key Summary

```text
문제 1
리스트 순회
→ 짝수는 새 리스트에 추가
→ 홀수는 합계에 누적

문제 2
중첩 딕셔너리 순회
→ 가격 × 개수
→ 전체 금액 누적

문제 3
난수 생성
→ 입력 반복
→ UP/DOWN 판정
→ 정답이면 반복 종료

문제 4
아이디가 키로 존재하는지 검사
→ 존재하면 해당 아이디의 비밀번호와 비교

문제 5
100번 무작위 투표
→ 후보별 수 누적
→ 최댓값과 최다 득표자 확인
```

Quiz 01은 하나의 문법만 연습하는 파일이 아니라 리스트와 딕셔너리에 저장된 데이터를 조건문과 반복문으로 처리하는 종합 실습입니다. 자료를 저장하는 방법, 필요한 값을 조회하는 방법, 조건에 따라 분기하는 방법, 반복해서 결과를 누적하는 방법을 함께 연결해야 문제를 완성할 수 있습니다.
