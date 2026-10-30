# 실습 02. 주문 파일 평가 — 문자가 숫자와 매출이 되는 과정

[Python 목차](README.md) · [읽기 안내](00-00_Python_V3_동작_백과_읽기법.md)

실제 평가에서 푼 주문 파일을 다시 읽는다. 결과가 19,000인지만 확인하지 않고, 어느 항목을 남겼으며 공백·단위·자료형을 어떤 순서로 처리했는지 설명한다. 제공 파일에서 성공한 코드와 입력 형식이 달라졌을 때의 개선안을 구별한다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

읽은 문자열을 줄·항목으로 나누고 가격 단위 제거와 정수 변환을 추적한다. 수량·가격의 경계 조건, 항목별 공백 제거, 잘못된 입력을 다루는 새 개선안의 범위를 구분한다.

실제 원본·새 예제·개선안·선택 학습을 구분하고 입력·실행 순서·반환값·출력을 연결한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

파일 안의 3000은 처음부터 정수가 아니다. read가 돌려준 큰 문자열에서 한 줄을 얻고, 쉼표로 나눠 얻은 3000도 문자열이다. 수량×가격을 계산하려면 필요한 칸을 int로 바꿔야 한다. 상품 이름은 문자열로 유지한다.

| 단계 | 예시 상태 | 이유 |
| --- | --- | --- |
| 한 줄 | 사과, 2, 3000원 | 파일에서 읽은 문자열 |
| split 후 | 세 문자열의 목록 | 칸의 위치 확보 |
| 각 칸 strip | 사과 / 2 / 3000원 | 앞뒤 공백 제거 |
| 가격 단위 제거 | 사과 / 2 / 3000 | 숫자 변환 준비 |
| 수량·가격 int | 문자열 / 정수 / 정수 | 계산 가능 |
| 범위 검사 | 수량≥0, 0≤가격≤10000 | 과제에서 정한 조건 |
| append와 누적 | 주문 목록 / 합계 | 남길 자료와 계산 결과 |

검사 순서에도 이유가 있다. 칸 수를 모르는데 parts[2]부터 읽으면 IndexError가 날 수 있다. 원래 평가는 정해진 형식의 제공 파일을 전제로 한다. 아래 새 예제는 이미 배운 len·try/except를 합쳐 형식 오류를 건너뛰도록 보완한다. 당시 제출 코드가 처음부터 이 처리를 했다고 해석하지 않는다.

> 📚 **출처 · 본문 설명 확인:** [Python 파일 읽고 쓰기](https://docs.python.org/ko/3/tutorial/inputoutput.html#reading-and-writing-files), [예외 처리](https://docs.python.org/ko/3/tutorial/errors.html#handling-exceptions). 실제 배운 문법의 의미를 확인한 근거다. 예제·표·풀이 자체는 수업 자료를 바탕으로 새로 구성했다. 외부 문장을 직접 인용하지 않았다. 이번 문법 확인 기간: 2026-10-28~29.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 코드.** [실행 파일](실습/책형_복습/실습-02_Python_주문파일_평가실습.py)을 제공한다. 원본 order.txt와 다른 이름인 book_orders.txt를 새 작업 폴더에 만들고 읽는다. 현재 폴더에 같은 이름의 개인 파일이 없는지 확인하고 실행한다. 자료 생성부터 결과까지 아래 코드에 포함되어 있다.



```python
text = '사과, 2, 3000원\n귤, 3, 2000\n우유, 1, -2000\n주스, 1, 12000\n잘못된줄\n물, 여러개, 1000\n'
with open('book_orders.txt', 'w', encoding='utf-8') as file:
    file.write(text)
orders = []
total = 0
skipped = 0
with open('book_orders.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if not line.strip():
            continue
        parts = [part.strip() for part in line.split(',')]
        if len(parts) != 3:
            skipped += 1
            continue
        try:
            quantity = int(parts[1])
            price = int(parts[2].replace('원', ''))
        except ValueError:
            skipped += 1
            continue
        if quantity >= 0 and 0 <= price <= 10000:
            orders.append([parts[0], quantity, price])
            total += quantity * price
        else:
            skipped += 1
print(orders)
print(total)
print('제외', skipped)
```

사과는 2×3000으로 6000을, 귤은 3×2000으로 6000을 더한다. 우유·주스는 범위에서 빠지고 잘못된줄은 칸 수, 물은 정수 변환에서 빠진다. 마지막 줄바꿈은 추가 주문이 아니다. 파일을 한 줄씩 순회하므로 읽을 줄이 더 없으면 끝난다. continue는 해당 줄 처리를 끝내고 다음 줄로 간다. ValueError만 처리하여 숫자 형식 문제와 다른 종류의 문제를 구별한다.

**예상 출력 또는 관찰:**

```text
[['사과', 2, 3000], ['귤', 3, 2000]]
12000
제외 4
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본 발췌다. 주석의 잘못된 설명도 원문을 보존하고 풀이에서 교정한다. 필요한 선언·호출·다른 파일의 정의는 다음 절까지 연결해 읽는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/과제 및 평가/exam.py` 45–78행

```python
with open('order.txt', 'r', encoding='utf-8') as file :
    orderResult = [] # 완성 결과물 저장용 Result
    orderPrice = 0 # 완성 결과물 전체 매출 저장용 Price

    # '주문은 엔터로 구분되어 있습니다' 참고하여 '\n' 으로 split
    order = file.read().split('\n')
    # print(order) # 제대로 split되어 list로 반환되었는지 확인

    for orders in order :
        # 조건3-1_각 항목의 앞뒤 공백 제거
        # split으로 ,로 구분하여 하나씩 가져온 뒤에 strip으로 공백제거한 값 delBlank에 저장
        # delBlank에 저장 후 orders에 저장 (한 줄로 해도 되지만, 차분히 단계별로)
        delBlank = [i.strip() for i in orders.split(',')]
        orders = delBlank
        # print(orders)
        # print('' in orders) # 공백 있는지 재확인 용 print(False면 Okay)

        # 조건3-2_가격에서 “원” 제거
        # '단, 내용은 상품, 수량, 가격 순서대로 적혀있고' 이니 가격에서만 제거해야 하기 때문에
        # 2번 index(가격)에서만 '원' 제거 
        delOne = orders[2].replace('원','')
        orders[2] = delOne
        # print(orders)

        # 조건3-3_수량과 가격은 정수형으로 변환
        # 수량(1번 index)과 가격(2번 index) int로 변환하여 다시 저장
        # int 변환도 줄 수를 줄일 수 있지만 변수를 잘 써보기 위해 단계별로 진행
        changeInt = int(orders[1])
        orders[1] = changeInt
        changeInt = int(orders[2])
        orders[2] = changeInt
        # orders에 있는 수량과 가격이 모두 int형으로 변환 되었는지 확인용 출력
        # print(orders[0], type(orders[0]), orders[1], type(orders[1]), orders[2], type(orders[2]), end='\n\n')

```

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/과제 및 평가/exam.py` 83–89행

```python
        if orders[1] >= 0 and 0 <= orders[2] <= 10000 :
            orderResult.append(orders)
            orderPrice += orders[1] * orders[2]

# 결과값은 모두 담겼으니, for문 밖에서 print 진행
print('최종항목 :', orderResult, end='\n\n')
print('전체매출 :', orderPrice)
```

**발췌 바로 풀이:** 파일의 한 줄은 `상품, 수량, 가격`이다. 코드는 줄을 쉼표로 나누고 각 항목의 앞뒤 공백을 지우며, 가격에서 `원`을 없앤 다음 수량·가격을 `int`로 바꾼다. 그 뒤 **수량이 0 이상, 가격이 0 이상 10,000 이하**인 항목만 `orderResult`에 넣고 `수량 × 가격`을 누적한다. 제공된 `order.txt`에서는 주스(12,000), 우유(-2,000), 수량 -2인 아메리카노가 빠지고, 네 항목의 매출 합계는 **19,000**이다. 이 첫 코드는 제공된 파일 사본을 대상으로 별도 작업 폴더에서 실행해 결과를 확인했다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/exam/99_try.py` 33–59행

```python
with open('exam/99_order.txt', 'r', encoding='utf-8') as file :
    orderResult = []
    orderPrice = 0

    order = file.read().split('\n')

    for orders in order :
        # delBlank = orders.replace(' ','').split(',')
        # delBlank = orders.strip().split(',')
        orders = [delBlank.strip() for delBlank in orders.split(',')]
        # print(orders)

        delOne = orders[2].replace('원','')
        orders[2] = delOne
        # print(orders)

        orders[1] = int(orders[1])
        orders[2] = int(orders[2])
        # print(orders)
        # print(orders[0], type(orders[0]), orders[1], type(orders[1]), orders[2], type(orders[2]), end='\n\n')

        if orders[1] >= 0 and 0 <= orders[2] <= 10000 :
            orderResult.append(orders)
            orderPrice += orders[1] * orders[2]

    print(orderResult, '' in orderResult)
    print(orderPrice)
```

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/exam/991_try.py` 20–63행

```python
print('-'*30)
orderResult = []
orderPrice = 0

with open('./exam/99_order.txt', 'r', encoding='utf-8') as file :
    # '주문은 '엔터' 로 구분되어 있습니다' > \n 로 split하여 리스트로 반환
    order = file.read().split('\n')

    for orders in order :
        # 조건 3-1_각 항목의 앞뒤 공백 제거 
        # replace? strip? 앞 뒤 공백이면 strip이 나을 것 같음
        isBlank = orders.strip().split(',')
        orders = isBlank
        print(orders)

        # 조건 3-2_가격에서 '원' 제거
        # 사용자의 입장에서 생각. '원'이 다른곳에도 있다면? 다 바뀌니까 2번 index 가격란만 변경
        isOne = orders[2].replace('원','')
        orders[2] = isOne

        # 조건 3-3_수량과 가격 정수형으로 변환
        # 0번 index는 'str'로 유지해야 하기 때문에 수량, 가격 index 값만 'int'로 변환작업
        isInt = int(orders[1])
        orders[1] = isInt
        isInt = int(orders[2])
        orders[2] = isInt
        # 각 값 별로 type 제대로 바뀌었는지 리체크 단계
        # print(orders,'-'*30)
        # print(orders[0], type(orders[0]), orders[1], type(orders[1]), orders[2],type(orders[2]),end='\n\n')

        # 조건 2_이상치를 제거하세요
        # 2번 index 가격이 0보다 작거나 10000보다 커야하니 0보다 크거나 같고, 10000보다 작거나 같다
        # 1번 index 개수가 0보다 작아야 하니 0보다 크거나 같다
        if 0 <= orders[2] <= 10000 \
        and orders[1] >= 0 :
            # 맞는 값만 골라왔는지 append로 리스트에 넣어 추가 확인 작업
            orderResult.append(orders)
            # 이상치를 제거한 대상 전체 매출을 orderPrice에 누적
            orderPrice += orders[1] * orders[2]

    # 결과 : 아메리카노, 2, 3000 / 카페라떼, 1, 4500 / 물, 1, 1000 / 탄산음료, 3, 2500 나와야 함
    print('최종결과 : ', orderResult, type(orderResult))
    # 가격 : 19000원
    print('최종가격 : ', orderPrice, type(orderPrice))
```

**발췌 바로 풀이:** 두 버전도 제공된 `99_order.txt`에서 **19,000**을 출력한다. `99_try.py`는 항목마다 `strip()`을 호출해 쉼표 뒤 공백도 제거한다. `991_try.py`는 줄 전체에 `strip()`을 적용한 뒤 쉼표로 나누므로 **각 항목 내부의 앞뒤 공백은 그대로 남을 수 있다**. 현재 파일에서는 `int(' 2')`가 숫자로 바뀌고 결과 합계는 같지만, “각 항목의 공백 제거”라는 요구를 정확히 보여 주는 쪽은 앞의 두 버전이다.

첫 exam.py는 read().split으로 모든 줄을 만든 뒤 각 칸을 strip한다. 가격 칸에만 replace를 적용해 상품명에 들어간 원 글자를 보존한다. 두 정수 변환 뒤 범위를 검사하고 목록과 전체 매출을 따로 갱신한다. 99_try.py도 각 칸을 정리한다. 991_try.py는 줄 전체만 strip한 뒤 나누므로 쉼표 뒤 공백이 상품명 등에 남을 수 있다. int가 숫자 앞 공백을 허용해 현재 합계가 맞더라도 모든 문자열 칸이 정리됐다는 뜻은 아니다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

별도 import 함수는 없다. 파일 읽기 → 한 줄 문자열 → 세 칸 → 수량·가격 정수 → 조건 → 목록과 합계 → 반복 밖 출력의 흐름이다. 원본 첫 파일은 같은 작업 위치의 order.txt를, 두 재작성 파일은 exam/99_order.txt를 읽는다. 파일 경로를 맞추지 않고 파이썬 파일만 옮겨 실행하면 FileNotFoundError가 날 수 있다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 과제 조건을 주석으로 나누고 가격 칸만 단위를 제거했으며, 항목 보존과 매출 누적을 구별했다. 복습할 때 각 중간값을 출력할 수 있도록 흔적을 남긴 것도 도움이 된다.

**실제 요구와 어긋날 수 있는 부분:** 991_try의 줄 전체 strip은 각 칸 공백 제거를 대신하지 못한다. **제공 형식에 의존한 부분:** 세 칸인지와 정수로 바뀌는지 확인하지 않아 빈 줄·잘못된 칸 수·숫자가 아닌 값에는 실패할 수 있다. 이는 현재 정상 제공 파일의 계산 오류와는 다르다.

**점검 문장 교정:** 99_try의 `'' in orderResult`는 바깥 목록에 빈 문자열이라는 요소가 있는지 검사한다. 내부 주문의 상품명까지 전부 검사하지 않는다. **새 개선안:** 칸 수·변환 오류·업무 범위를 나누면 왜 제외했는지 더 쉽게 추적한다. 빈 상품명이나 가격의 원 글자 위치까지 엄격히 검사하는 완성형 입력기는 아직 아니다.

개선안은 D 드라이브 원본을 수정한 결과가 아니다. 실제 오류·수업용 단순화·목적에 따른 선택을 구별한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



강사님 폴더에는 이 주문 평가의 직접 대응 풀이가 없다. 강사님 파일 읽기 수업은 기반 문법이지 주문 평가의 정답 코드가 아니다. 내 세 버전을 비교할 때 같은 합계뿐 아니라 항목별 공백 처리라는 요구 충족 여부를 확인한다. 비교 목적을 충족하므로 강사님 파일 읽기 코드를 다시 길게 인용하지 않는다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 제공 원본 항목 | 처리 | 매출 |
| --- | --- | --- |
| 아메리카노 2×3000 | 유지 | 6000 |
| 카페라떼 1×4500 | 유지 | 4500 |
| 주스 5×12000 | 가격 상한 초과 | 제외 |
| 물 1×1000 | 유지 | 1000 |
| 우유 1×-2000 | 음수 가격 | 제외 |
| 아메리카노 -2×3000 | 음수 수량 | 제외 |
| 탄산음료 3×2500 | 유지 | 7500 |

원본 두 데이터 파일은 같은 일곱 줄이며 남은 네 항목의 합은 19,000이다. 새 예제의 데이터·합계 12,000과 구별한다. 원본을 읽어 이 표를 계산했고, 원본 파일을 덮어쓰지 않는다.

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| 사과 수량을 0으로 | 목록 유지·매출 0 | 조건은 0 이상 |
| 가격을 10000으로 | 유지 | 상한 포함 |
| 가격을 10001로 | 제외 | 상한 초과 |
| 상품명을 원두로 | 원두 유지 | 가격 칸에만 replace |
| 물 수량을 2로 | 정상 항목 추가 | int 변환 성공 |

정수 변환 오류면 원본 문자열 칸을 먼저 출력한다. 인덱스 오류면 split 결과의 길이를 본다. 합계는 맞지만 이름이 다르면 각 칸 strip 여부를 확인한다. 합계가 반복해서 더해진다면 total 초기화가 반복 밖인지, 조건 안에서만 더하는지 본다. 쉼표가 들어간 상품명은 이 단순 형식의 처리 범위가 아니다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 쉼표·따옴표가 섞인 실제 CSV 형식은 csv 모듈로 다루는 방법을 별도로 배울 수 있다. 오류 사유별 기록·빈 상품명 검사·금액 표현 규칙·입력과 계산 함수 분리도 확장할 수 있다. [csv 공식 문서](https://docs.python.org/ko/3/library/csv.html)를 참고하되 이 평가에서 csv를 배웠다는 뜻은 아니다.

TIP은 기본 문제의 필수 조건이 아니다. 배운 문법을 확인한 📚 출처와 선택 확장을 구별한다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. 원본 파일 합계는?
2. 0원 항목을 원본 조건이 제거하는가?
3. 줄 strip과 칸 strip은 같은가?
4. 바깥 목록의 빈 문자열 검사로 내부 상품명을 검사할 수 있는가?

<details>
<summary>풀이 — 먼저 자신의 답을 적은 뒤 펼치기</summary>

19,000이다. 0은 허용한다. 줄 전체 앞뒤 공백과 각 칸 앞뒤 공백은 다르다. 바깥 목록에 목록들이 들어 있으므로 빈 문자열 포함 검사만으로 내부 상품명을 점검할 수 없다.

</details>

| 확인할 순서 | 핵심 |
| --- | --- |
| 형식 | 줄·칸 수 |
| 자료형 | 문자열→정수 |
| 범위 | 0·상한 포함 여부 |
| 누적 | 남긴 항목만 합산 |

[장별 연습문제](실습/연습문제/실습-02_Python_주문파일_평가실습_연습문제.md) · [실무 코딩스타일](19_Python_실무_코딩스타일.md)에서 처리 순서와 함수 분리를 이어 본다.

<!-- 이전 명시 앵커 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
