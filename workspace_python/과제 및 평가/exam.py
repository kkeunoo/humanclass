'''
조건1. order.txt 파일을 읽기 모드로 읽으세요. 단, 내용은 상품, 수량, 가격 
순서대로 적혀있고 주문은 엔터로 구분되어 있습니다
   조건2. 이상치를 제거하세요
         * 가격이 0보다 작은 경우
         * 가격이 10000보다 큰 경우
         * 개수가 0보다 작은 경우
   조건3. 텍스트 클렌징을 적용하세요
         * 각 항목의 앞뒤 공백 제거
         * 가격에서 “원” 제거
         * 수량과 가격은 정수형으로 변환
   조건4. 전체 매출을 출력하세요
'''
'''
아메리카노, 2, 3000
카페라떼, 1, 4500
주스, 5, 12000
물, 1, 1000
우유, 1, -2000
아메리카노, -2, 3000원
탄산음료, 3, 2500

- 가격이 0보다 작은 경우 제거
아메리카노, 2, 3000
카페라떼, 1, 4500
주스, 5, 12000
물, 1, 1000
아메리카노, -2, 3000원
탄산음료, 3, 2500

- 가격이 10000보다 큰 경우 제거
아메리카노, 2, 3000
카페라떼, 1, 4500
물, 1, 1000
아메리카노, -2, 3000원
탄산음료, 3, 2500

- 개수가 0보다 작은 경우 제거
아메리카노, 2, 3000
카페라떼, 1, 4500
물, 1, 1000
탄산음료, 3, 2500
'''

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

        # 조건2_이상치 제거
        # 가격이 0보다 작은 경우 → 0보다 크거나 같은경우
        # 가격이 10000보다 큰 경우 → 10000보다 작거나 같은경우
        # 개수가 0보다 작은 경우 → 0보다 크거나 같은경우
        if orders[1] >= 0 and 0 <= orders[2] <= 10000 :
            orderResult.append(orders)
            orderPrice += orders[1] * orders[2]

# 결과값은 모두 담겼으니, for문 밖에서 print 진행
print('최종항목 :', orderResult, end='\n\n')
print('전체매출 :', orderPrice)