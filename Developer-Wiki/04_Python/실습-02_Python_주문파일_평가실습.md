# 실습 02. 주문 파일 평가 — 읽기, 정리, 합계

[Python 목차](README.md) · [이전: 자료형 퀴즈](실습-01b_Python_자료형_퀴즈_난수문제.md)

내 `과제 및 평가/exam.py`와 `exam/99_try.py`·`exam/991_try.py`에는 같은 주문 파일을 처리하는 실제 코드가 있다. 강사님 폴더에는 이 **주문 평가와 직접 대응하는 파일이 없으므로**, 먼저 강사님 `10_file.py`의 파일 읽기·문자열 처리 예시를 **기반 개념**으로 놓고 내 과제를 살펴본다. GPT를 이용한 바이브코딩 시험 폴더와는 다른 실습이다.

<!-- chapter-toc -->

- [1. 강사님 코드에서 연결되는 기반 개념](실습-02_Python_주문파일_평가실습.md#section-1)
- [2. 내 첫 평가 코드의 처리 순서](실습-02_Python_주문파일_평가실습.md#section-2)
- [3. 내가 다시 쓴 두 버전](실습-02_Python_주문파일_평가실습.md#section-3)
- [직접 확인할 질문](실습-02_Python_주문파일_평가실습.md#section-4)
- [추가로 알면 좋은 것](실습-02_Python_주문파일_평가실습.md#section-5)

<a id="section-1"></a>

## 1. 강사님 코드에서 연결되는 기반 개념

### 강사님 코드 — 파일을 읽고 나누기

출처: `teacher/workspace_python/_10_file.py` 133–139행 · **원본 발췌**

```python
with open('word.txt', 'r') as file :
    txt = file.read()
    print(txt)
    
    # txt = 'Fortunately, however, for the reputation of Asteroid B-612, a Turkish dictator made a law that his subjects, under pain of death, should change to European costume. So in 1920 the astronomer gave his demonstration all over again, dressed with impressive style and elegance. And this time everybody accepted his report.'
    txt_list = txt.split(' ')
    print(txt_list)
```

강사님은 `word.txt`를 읽어 공백으로 나누고, 뒤에서 문자열을 검사한다. 내 평가는 입력 파일과 요구 결과가 다르지만, **파일 읽기 → 문자열 분리 → 반복 처리**라는 흐름이 이어진다. 강사님 코드가 주문 평가의 정답을 제시했다고 해석하지 않는다.

<a id="section-2"></a>

## 2. 내 첫 평가 코드의 처리 순서

### 내 코드 — 읽기와 항목 변환

출처: `me/workspace_python/과제 및 평가/exam.py` 45–78행 · **원본 발췌**

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

### 내 코드 — 범위 검사와 합계

출처: `me/workspace_python/과제 및 평가/exam.py` 83–89행 · **원본 발췌**

```python
        if orders[1] >= 0 and 0 <= orders[2] <= 10000 :
            orderResult.append(orders)
            orderPrice += orders[1] * orders[2]

# 결과값은 모두 담겼으니, for문 밖에서 print 진행
print('최종항목 :', orderResult, end='\n\n')
print('전체매출 :', orderPrice)
```

파일의 한 줄은 `상품, 수량, 가격`이다. 코드는 줄을 쉼표로 나누고 각 항목의 앞뒤 공백을 지우며, 가격에서 `원`을 없앤 다음 수량·가격을 `int`로 바꾼다. 그 뒤 **수량이 0 이상, 가격이 0 이상 10,000 이하**인 항목만 `orderResult`에 넣고 `수량 × 가격`을 누적한다. 제공된 `order.txt`에서는 주스(12,000), 우유(-2,000), 수량 -2인 아메리카노가 빠지고, 네 항목의 매출 합계는 **19,000**이다. 이 첫 코드는 제공된 파일 사본을 대상으로 별도 작업 폴더에서 실행해 결과를 확인했다.

조건에는 **0보다 작은** 수량·가격을 제거한다고 적혀 있으므로 0 자체는 남는다. `split('\n')` 뒤 빈 줄이나 잘못된 형식이 있으면 `orders[2]`에서 오류가 날 수 있지만, 제공된 파일에는 그런 줄이 없어 실행됐다. 파일 입력을 완전히 검증하는 코드로 넓혀 설명하지 않는다.

<a id="section-3"></a>

## 3. 내가 다시 쓴 두 버전

### 내 코드 — `exam/99_try.py`

출처: `me/workspace_python/exam/99_try.py` 33–59행 · **원본 발췌**

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

### 내 코드 — `exam/991_try.py`의 중심 부분

출처: `me/workspace_python/exam/991_try.py` 20–63행 · **원본 발췌**

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

두 버전도 제공된 `99_order.txt`에서 **19,000**을 출력한다. `99_try.py`는 항목마다 `strip()`을 호출해 쉼표 뒤 공백도 제거한다. `991_try.py`는 줄 전체에 `strip()`을 적용한 뒤 쉼표로 나누므로 **각 항목 내부의 앞뒤 공백은 그대로 남을 수 있다**. 현재 파일에서는 `int(' 2')`가 숫자로 바뀌고 결과 합계는 같지만, “각 항목의 공백 제거”라는 요구를 정확히 보여 주는 쪽은 앞의 두 버전이다.

<a id="section-4"></a>

## 직접 확인할 질문

1. 왜 주스·우유·두 번째 아메리카노가 결과에서 빠질까?
2. `0`원이나 수량 `0`은 현재 조건에서 통과할까?
3. `orders.strip().split(',')`와 `[i.strip() for i in orders.split(',')]`은 어떤 입력에서 달라질까?

<a id="section-5"></a>

## 추가로 알면 좋은 것

비어 있는 줄이나 숫자가 아닌 가격을 오류 없이 건너뛰는 입력 검증은 이 평가 코드에 구현되지 않았다. 현재는 **주어진 파일에서 실제로 실행된 처리 순서와 결과**를 먼저 복습하자.

