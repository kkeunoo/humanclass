---
title: Python 종합 실습
version: v3.0-encyclopedia
last_updated: 2026-08-06
status: Completed
---

# Python 종합 실습

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `20_Python_종합실습.md` |
| 분류 | `04_Python` |
| 권장 선수 학습 | `01~19` Python 문서 |
| 문서 성격 | Python 종합 실습 및 미니 프로젝트 |
| 핵심 범위 | 변수, 자료형, 조건문, 반복문, 함수, 클래스, 예외 처리, 모듈, 파일 입출력, 실무 코딩 스타일 |
| 실습 방식 | 요구사항 → 구현 전 생각 → 완성 예시 → 실행 결과 → 해설 → 확장 과제 |
| 난이도 | 기초 → 중급 → 종합 프로젝트 |
| 문서 형식 | Python Developer-Wiki V2 확정 형식 |

> 이 문서는 정답을 외우는 문제집이 아니다.  
> 지금까지 배운 문법을 조합해 **하나의 프로그램 흐름을 설계하는 연습**을 위한 문서다.

---

# 개요

문법을 각각 이해하는 것과 여러 문법을 조합해 프로그램을 만드는 것은 다르다.

```text
변수
조건문
반복문
함수
클래스
예외 처리
파일 입출력
    ↓
각각은 이해함
    ↓
하나의 프로그램으로 연결하기 어려움
```

종합 실습의 목표는 다음과 같다.

```text
요구사항 읽기
    ↓
필요한 자료형 선택
    ↓
함수와 클래스 역할 구분
    ↓
입력값 검증
    ↓
결과 출력
    ↓
예외 처리
    ↓
기능 확장
```

> [!IMPORTANT]
> 처음부터 완벽한 코드를 만들려고 하지 않는다.
>
> 먼저 동작하는 코드를 만들고, 실행 결과를 확인한 뒤 이름·중복·함수 책임·예외 흐름을 개선한다.

---

# 실습 진행 방법

각 실습은 다음 순서로 진행한다.

```text
1. 실습 목표 확인
2. 요구사항 읽기
3. 사용할 자료형과 함수 생각
4. 직접 코드 작성
5. 완성 예시와 비교
6. 실행 결과 확인
7. 확장 과제 추가
8. 리팩토링
```

완성 예시는 하나의 정답이 아니다.

같은 요구사항도 여러 방식으로 구현할 수 있다.

---

# 난이도 구성

| 단계 | 실습 |
| --- | --- |
| 1단계 | 사용자 목록 분석 |
| 2단계 | 학생 성적 관리 |
| 3단계 | 상품 재고 관리 |
| 4단계 | 카페 주문 관리 |
| 5단계 | 은행 계좌 클래스 |
| 6단계 | 회원 등록과 JSON 저장 |
| 7단계 | 로그 분석기 |
| 최종 프로젝트 | HumanJobs 직원 관리 시스템 |

---

# 공통 코딩 기준

실습 코드는 다음 기준을 지킨다.

- 변수명과 함수명은 역할이 드러나게 작성
- `const` 대신 Python 상수는 대문자 사용
- 인덱스가 필요 없으면 직접 순회
- 인덱스가 필요하면 `enumerate()`
- 함수 하나는 하나의 주요 책임 담당
- 반환값 자료형을 일관되게 유지
- 예외는 구체적으로 처리
- 파일은 `with`문으로 관리
- 경로는 `pathlib.Path` 사용
- 복잡한 로직은 작은 함수로 분리
- 실행 결과를 확인한 뒤 리팩토링

---

# 1. 사용자 목록 분석

## 1-1. 실습 목표

사용자 딕셔너리 목록에서 다음 정보를 구한다.

- 전체 사용자 수
- 활성 사용자 이름
- 성인 사용자 이름
- 최고 점수 사용자
- 모든 사용자가 이메일을 가지고 있는지
- 한 명이라도 비활성 사용자가 있는지

## 1-2. 입력 데이터

```python
users = [
    {
        "id": 1,
        "name": "Kim",
        "age": 21,
        "active": True,
        "email": "kim@example.com",
        "score": 85,
    },
    {
        "id": 2,
        "name": "Lee",
        "age": 17,
        "active": False,
        "email": "lee@example.com",
        "score": 58,
    },
    {
        "id": 3,
        "name": "Park",
        "age": 28,
        "active": True,
        "email": "park@example.com",
        "score": 92,
    },
]
```

## 1-3. 사용할 개념

- 리스트
- 딕셔너리
- 반복문
- 리스트 컴프리헨션
- `len()`
- `max()`
- `any()`
- `all()`
- 함수

## 1-4. 구현 전에 생각하기

```text
전체 사용자 수
→ len(users)

활성 사용자
→ active가 True인 사용자 필터

성인 사용자
→ age >= 19

최고 점수
→ max() + key

모든 사용자 이메일
→ all()

비활성 사용자 존재
→ any()
```

## 1-5. 완성 예시

```python
ADULT_AGE = 19


def get_active_user_names(users):
    return [
        user["name"]
        for user in users
        if user["active"]
    ]


def get_adult_user_names(users):
    return [
        user["name"]
        for user in users
        if user["age"] >= ADULT_AGE
    ]


def get_top_user(users):
    if not users:
        return None

    return max(
        users,
        key=lambda user: user["score"],
    )


def print_user_summary(users):
    active_names = get_active_user_names(
        users
    )
    adult_names = get_adult_user_names(
        users
    )
    top_user = get_top_user(users)

    all_have_email = all(
        user.get("email")
        for user in users
    )

    has_inactive_user = any(
        not user["active"]
        for user in users
    )

    print("전체 사용자:", len(users))
    print("활성 사용자:", active_names)
    print("성인 사용자:", adult_names)
    print(
        "최고 점수 사용자:",
        top_user["name"]
        if top_user
        else "없음",
    )
    print(
        "모두 이메일 보유:",
        all_have_email,
    )
    print(
        "비활성 사용자 존재:",
        has_inactive_user,
    )
```

## 1-6. 실행

```python
print_user_summary(users)
```

## 1-7. 실행 결과

```text
전체 사용자: 3
활성 사용자: ['Kim', 'Park']
성인 사용자: ['Kim', 'Park']
최고 점수 사용자: Park
모두 이메일 보유: True
비활성 사용자 존재: True
```

## 1-8. 핵심 해설

- 단순 필터링은 리스트 컴프리헨션으로 처리했다.
- 빈 목록에서 `max()`를 사용하면 오류가 발생하므로 먼저 검사했다.
- 하나라도 참인지 확인할 때 `any()`를 사용했다.
- 모두 참인지 확인할 때 `all()`을 사용했다.

## 1-9. 확장 과제

- 평균 점수 계산
- 점수 60점 이상 사용자 목록
- 이름순 정렬
- 활성 사용자 비율 계산
- 특정 ID 사용자 검색 함수 추가

---

# 2. 학생 성적 관리

## 2-1. 실습 목표

학생 이름과 과목 점수를 관리한다.

기능:

- 학생별 총점
- 학생별 평균
- 합격 여부
- 평균 높은 순 정렬
- 전체 최고 점수 학생 출력

## 2-2. 입력 데이터

```python
students = [
    {
        "name": "Kim",
        "scores": {
            "python": 90,
            "database": 85,
            "html": 88,
        },
    },
    {
        "name": "Lee",
        "scores": {
            "python": 55,
            "database": 62,
            "html": 58,
        },
    },
    {
        "name": "Park",
        "scores": {
            "python": 95,
            "database": 91,
            "html": 97,
        },
    },
]
```

## 2-3. 요구사항

- 평균이 60점 이상이면 합격
- 평균은 소수점 둘째 자리까지 출력
- 학생별 결과를 딕셔너리로 반환
- 원본 데이터는 변경하지 않음

## 2-4. 사용할 개념

- 중첩 딕셔너리
- `sum()`
- `len()`
- 함수 분리
- `sorted()`
- f-string
- 타입 힌트

## 2-5. 완성 예시

```python
PASS_SCORE = 60


def calculate_average(scores):
    if not scores:
        return 0.0

    return (
        sum(scores.values())
        / len(scores)
    )


def create_student_result(student):
    scores = student["scores"]
    total = sum(scores.values())
    average = calculate_average(scores)

    return {
        "name": student["name"],
        "total": total,
        "average": average,
        "passed": average >= PASS_SCORE,
    }


def get_student_results(students):
    return [
        create_student_result(student)
        for student in students
    ]


def sort_results_by_average(results):
    return sorted(
        results,
        key=lambda result: result["average"],
        reverse=True,
    )


def print_student_results(results):
    for number, result in enumerate(
        results,
        start=1,
    ):
        status = (
            "합격"
            if result["passed"]
            else "불합격"
        )

        print(
            f'{number}. {result["name"]} / '
            f'총점 {result["total"]} / '
            f'평균 {result["average"]:.2f} / '
            f'{status}'
        )
```

## 2-6. 실행

```python
results = get_student_results(
    students
)

sorted_results = sort_results_by_average(
    results
)

print_student_results(sorted_results)
```

## 2-7. 실행 결과

```text
1. Park / 총점 283 / 평균 94.33 / 합격
2. Kim / 총점 263 / 평균 87.67 / 합격
3. Lee / 총점 175 / 평균 58.33 / 불합격
```

## 2-8. 핵심 해설

```text
calculate_average()
→ 점수 평균만 담당

create_student_result()
→ 학생 한 명의 결과 생성

get_student_results()
→ 여러 학생 결과 생성

sort_results_by_average()
→ 정렬만 담당

print_student_results()
→ 출력만 담당
```

## 2-9. 확장 과제

- 과목별 평균 계산
- 과목별 최고 점수 학생
- 점수 범위 검증
- 등급 A~F 추가
- 결과를 JSON 파일로 저장

---

# 3. 상품 재고 관리

## 3-1. 실습 목표

상품 목록에서 재고와 가격을 관리한다.

기능:

- 상품 추가
- 상품 검색
- 재고 입고
- 재고 출고
- 전체 재고 가치 계산
- 재고 부족 상품 출력

## 3-2. 입력 데이터

```python
products = [
    {
        "id": 1,
        "name": "Keyboard",
        "price": 45000,
        "stock": 10,
    },
    {
        "id": 2,
        "name": "Mouse",
        "price": 25000,
        "stock": 3,
    },
]
```

## 3-3. 요구사항

- 상품 ID는 중복될 수 없음
- 가격은 0보다 커야 함
- 재고는 음수가 될 수 없음
- 없는 상품 검색 시 `None` 반환
- 재고 부족 기준은 5개 이하

## 3-4. 완성 예시

```python
LOW_STOCK_LIMIT = 5


def find_product(products, product_id):
    for product in products:
        if product["id"] == product_id:
            return product

    return None


def add_product(
    products,
    product_id,
    name,
    price,
    stock=0,
):
    if find_product(products, product_id):
        raise ValueError(
            "이미 존재하는 상품 ID입니다."
        )

    if price <= 0:
        raise ValueError(
            "가격은 0보다 커야 합니다."
        )

    if stock < 0:
        raise ValueError(
            "재고는 음수일 수 없습니다."
        )

    product = {
        "id": product_id,
        "name": name.strip(),
        "price": price,
        "stock": stock,
    }

    products.append(product)

    return product


def increase_stock(
    products,
    product_id,
    quantity,
):
    if quantity <= 0:
        raise ValueError(
            "입고 수량은 1개 이상이어야 합니다."
        )

    product = find_product(
        products,
        product_id,
    )

    if product is None:
        raise ValueError(
            "상품을 찾을 수 없습니다."
        )

    product["stock"] += quantity

    return product["stock"]


def decrease_stock(
    products,
    product_id,
    quantity,
):
    if quantity <= 0:
        raise ValueError(
            "출고 수량은 1개 이상이어야 합니다."
        )

    product = find_product(
        products,
        product_id,
    )

    if product is None:
        raise ValueError(
            "상품을 찾을 수 없습니다."
        )

    if product["stock"] < quantity:
        raise ValueError(
            "재고가 부족합니다."
        )

    product["stock"] -= quantity

    return product["stock"]


def calculate_inventory_value(products):
    return sum(
        product["price"]
        * product["stock"]
        for product in products
    )


def get_low_stock_products(products):
    return [
        product
        for product in products
        if (
            product["stock"]
            <= LOW_STOCK_LIMIT
        )
    ]
```

## 3-5. 실행

```python
add_product(
    products,
    product_id=3,
    name="Monitor",
    price=210000,
    stock=4,
)

increase_stock(
    products,
    product_id=2,
    quantity=5,
)

decrease_stock(
    products,
    product_id=1,
    quantity=2,
)

print(
    "전체 재고 가치:",
    calculate_inventory_value(
        products
    ),
)

for product in get_low_stock_products(
    products
):
    print(
        "재고 부족:",
        product["name"],
        product["stock"],
    )
```

## 3-6. 실행 결과

```text
전체 재고 가치: 1400000
재고 부족: Monitor 4
```

## 3-7. 확장 과제

- 상품 삭제
- 상품 가격 변경
- 이름 검색
- 재고 가치 높은 순 정렬
- CSV 또는 JSON 저장
- 클래스로 리팩토링

---

# 4. 카페 주문 관리

## 4-1. 실습 목표

메뉴와 주문 목록을 관리한다.

기능:

- 메뉴 선택
- 수량 검증
- 주문 항목 추가
- 총 주문 금액 계산
- 주문 영수증 출력

## 4-2. 입력 데이터

```python
menu = {
    "americano": 4000,
    "latte": 5000,
    "tea": 4500,
}
```

## 4-3. 완성 예시

```python
def create_order_item(
    menu,
    item_name,
    quantity,
):
    if item_name not in menu:
        raise ValueError(
            "존재하지 않는 메뉴입니다."
        )

    if quantity <= 0:
        raise ValueError(
            "수량은 1개 이상이어야 합니다."
        )

    unit_price = menu[item_name]

    return {
        "name": item_name,
        "quantity": quantity,
        "unit_price": unit_price,
        "subtotal": (
            unit_price * quantity
        ),
    }


def calculate_order_total(order_items):
    return sum(
        item["subtotal"]
        for item in order_items
    )


def print_receipt(order_items):
    print("=== 주문 영수증 ===")

    for item in order_items:
        print(
            f'{item["name"]} '
            f'x {item["quantity"]} '
            f'= {item["subtotal"]:,}원'
        )

    total = calculate_order_total(
        order_items
    )

    print("-" * 20)
    print(f"총액: {total:,}원")
```

## 4-4. 실행

```python
order_items = [
    create_order_item(
        menu,
        "americano",
        2,
    ),
    create_order_item(
        menu,
        "latte",
        1,
    ),
]

print_receipt(order_items)
```

## 4-5. 실행 결과

```text
=== 주문 영수증 ===
americano x 2 = 8,000원
latte x 1 = 5,000원
--------------------
총액: 13,000원
```

## 4-6. 확장 과제

- 할인 쿠폰
- 포인트 적립
- 주문 취소
- 품절 메뉴
- 주문 시간 저장
- `Order`, `MenuItem` 클래스로 분리

---

# 5. 은행 계좌 클래스

## 5-1. 실습 목표

클래스와 캡슐화, 예외 처리를 이용해 계좌를 구현한다.

기능:

- 계좌 생성
- 입금
- 출금
- 잔액 조회
- 거래 내역 조회
- 계좌 개수 확인

## 5-2. 요구사항

- 계좌번호와 예금주 이름은 필수
- 초기 잔액은 0 이상
- 입금액은 0보다 큼
- 잔액보다 큰 금액은 출금 불가
- 계좌 개수는 클래스 속성으로 관리

## 5-3. 완성 예시

```python
class BankAccount:
    account_count = 0

    def __init__(
        self,
        account_number,
        owner_name,
        balance=0,
    ):
        account_number = (
            account_number.strip()
        )
        owner_name = owner_name.strip()

        if not account_number:
            raise ValueError(
                "계좌번호를 입력해야 합니다."
            )

        if not owner_name:
            raise ValueError(
                "예금주 이름을 입력해야 합니다."
            )

        if balance < 0:
            raise ValueError(
                "초기 잔액은 음수일 수 없습니다."
            )

        self.account_number = (
            account_number
        )
        self.owner_name = owner_name
        self._balance = balance
        self._transactions = []

        type(self).account_count += 1

        if balance > 0:
            self._add_transaction(
                "초기 입금",
                balance,
            )

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError(
                "입금액은 0보다 커야 합니다."
            )

        self._balance += amount
        self._add_transaction(
            "입금",
            amount,
        )

        return self._balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError(
                "출금액은 0보다 커야 합니다."
            )

        if amount > self._balance:
            raise ValueError(
                "잔액이 부족합니다."
            )

        self._balance -= amount
        self._add_transaction(
            "출금",
            -amount,
        )

        return self._balance

    def get_transactions(self):
        return list(
            self._transactions
        )

    def _add_transaction(
        self,
        transaction_type,
        amount,
    ):
        self._transactions.append(
            {
                "type": transaction_type,
                "amount": amount,
                "balance": self._balance,
            }
        )

    @classmethod
    def get_account_count(cls):
        return cls.account_count
```

## 5-4. 실행

```python
account = BankAccount(
    account_number="100-200-300",
    owner_name="Kim",
    balance=10000,
)

account.deposit(5000)
account.withdraw(3000)

print("잔액:", account.balance)

for transaction in (
    account.get_transactions()
):
    print(transaction)

print(
    "전체 계좌 수:",
    BankAccount.get_account_count(),
)
```

## 5-5. 실행 결과

```text
잔액: 12000
{'type': '초기 입금', 'amount': 10000, 'balance': 10000}
{'type': '입금', 'amount': 5000, 'balance': 15000}
{'type': '출금', 'amount': -3000, 'balance': 12000}
전체 계좌 수: 1
```

## 5-6. 핵심 해설

- `_balance`는 클래스 내부에서 관리하는 속성이다.
- 외부에서는 `balance` Property로 읽는다.
- 입출금은 일반 대입이 아니라 메서드를 통해 검증한다.
- 거래 내역은 원본 리스트가 아닌 복사본을 반환한다.
- 계좌 개수는 모든 객체가 공유하므로 클래스 속성을 사용한다.

## 5-7. 확장 과제

- 계좌 이체
- 거래 일시 저장
- 출금 한도
- 계좌 정지 상태
- 사용자 정의 예외
- JSON 파일 저장

---

# 6. 회원 등록과 JSON 저장

## 6-1. 실습 목표

입력 데이터를 검증하고 JSON 파일에 저장한다.

기능:

- 이름 검증
- 이메일 검증
- 나이 검증
- 기존 사용자 불러오기
- ID 자동 생성
- 사용자 저장

## 6-2. 사용할 개념

- 함수 분리
- 예외 처리
- `pathlib.Path`
- `json`
- 파일 입출력
- 리스트·딕셔너리

## 6-3. 완성 예시

```python
import json
from pathlib import Path


DATA_FILE = Path(
    "data/users.json"
)


def validate_name(name):
    name = name.strip()

    if not name:
        raise ValueError(
            "이름을 입력해야 합니다."
        )

    return name


def validate_email(email):
    email = email.strip()

    if not email:
        raise ValueError(
            "이메일을 입력해야 합니다."
        )

    if "@" not in email:
        raise ValueError(
            "이메일 형식이 올바르지 않습니다."
        )

    return email


def validate_age(age):
    if age < 0:
        raise ValueError(
            "나이는 음수일 수 없습니다."
        )

    return age


def load_users(file_path):
    if not file_path.exists():
        return []

    with file_path.open(
        "r",
        encoding="utf-8",
    ) as file:
        return json.load(file)


def save_users(
    file_path,
    users,
):
    file_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with file_path.open(
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            users,
            file,
            ensure_ascii=False,
            indent=2,
        )


def get_next_user_id(users):
    if not users:
        return 1

    return max(
        user["id"]
        for user in users
    ) + 1


def register_user(
    users,
    name,
    email,
    age,
):
    normalized_email = validate_email(
        email
    )

    if any(
        user["email"]
        == normalized_email
        for user in users
    ):
        raise ValueError(
            "이미 등록된 이메일입니다."
        )

    user = {
        "id": get_next_user_id(users),
        "name": validate_name(name),
        "email": normalized_email,
        "age": validate_age(age),
        "active": True,
    }

    users.append(user)

    return user
```

## 6-4. 실행

```python
users = load_users(DATA_FILE)

try:
    user = register_user(
        users,
        name="Kim",
        email="kim@example.com",
        age=21,
    )
except ValueError as error:
    print("등록 실패:", error)
else:
    save_users(
        DATA_FILE,
        users,
    )
    print("등록 완료:", user)
```

## 6-5. 출력 예시

```text
등록 완료: {'id': 1, 'name': 'Kim', 'email': 'kim@example.com', 'age': 21, 'active': True}
```

## 6-6. 확장 과제

- 사용자 수정
- 사용자 삭제
- 비활성 처리
- 이메일 정규표현식 검사
- JSON 오류 처리
- 모듈 분리

---

# 7. 로그 분석기

## 7-1. 실습 목표

로그 문자열에서 날짜, 로그 레벨, 메시지를 추출한다.

예시 로그:

```text
2026-08-06 10:30:15 INFO Login success
2026-08-06 10:31:10 ERROR Database connection failed
2026-08-06 10:32:40 WARNING Slow response
```

## 7-2. 사용할 개념

- 정규표현식
- 함수
- 제너레이터
- 딕셔너리
- 집계
- 예외 처리

## 7-3. 완성 예시

```python
import re


LOG_PATTERN = re.compile(
    r"(?P<date>\d{4}-\d{2}-\d{2})\s+"
    r"(?P<time>\d{2}:\d{2}:\d{2})\s+"
    r"(?P<level>[A-Z]+)\s+"
    r"(?P<message>.+)"
)


def parse_log_line(line):
    match = LOG_PATTERN.fullmatch(
        line.strip()
    )

    if match is None:
        return None

    return match.groupdict()


def parse_logs(lines):
    for line in lines:
        log = parse_log_line(line)

        if log is not None:
            yield log


def count_log_levels(logs):
    counts = {}

    for log in logs:
        level = log["level"]

        counts[level] = (
            counts.get(level, 0)
            + 1
        )

    return counts
```

## 7-4. 실행

```python
lines = [
    (
        "2026-08-06 10:30:15 "
        "INFO Login success"
    ),
    (
        "2026-08-06 10:31:10 "
        "ERROR Database connection failed"
    ),
    (
        "2026-08-06 10:32:40 "
        "WARNING Slow response"
    ),
    "잘못된 로그",
]

logs = list(parse_logs(lines))

for log in logs:
    print(log)

print(
    "레벨별 개수:",
    count_log_levels(logs),
)
```

## 7-5. 실행 결과

```text
{'date': '2026-08-06', 'time': '10:30:15', 'level': 'INFO', 'message': 'Login success'}
{'date': '2026-08-06', 'time': '10:31:10', 'level': 'ERROR', 'message': 'Database connection failed'}
{'date': '2026-08-06', 'time': '10:32:40', 'level': 'WARNING', 'message': 'Slow response'}
레벨별 개수: {'INFO': 1, 'ERROR': 1, 'WARNING': 1}
```

## 7-6. 확장 과제

- 특정 날짜만 필터
- ERROR 로그만 추출
- 파일 한 줄씩 읽기
- 결과 JSON 저장
- 가장 많이 발생한 로그 레벨 출력
- 잘못된 로그 별도 저장

---

# 8. 최종 프로젝트: HumanJobs 직원 관리 시스템

## 8-1. 프로젝트 목표

지금까지 배운 내용을 하나의 프로그램으로 연결한다.

기능:

- 직원 등록
- 직원 조회
- 직원 수정
- 직원 비활성 처리
- 부서별 직원 조회
- 급여 높은 순 정렬
- 파일 저장·불러오기
- 입력값 검증
- 예외 처리
- 통계 출력

## 8-2. 활용 개념

- 변수와 자료형
- 리스트·딕셔너리
- 조건문
- 반복문
- 함수
- 클래스
- Property
- 클래스 메서드
- 예외 처리
- 모듈
- 파일 입출력
- 정규표현식
- 실무 코딩 스타일

---

# 9. 직원 데이터 모델

## 9-1. 요구사항

직원은 다음 값을 가진다.

- 직원 ID
- 이름
- 이메일
- 부서
- 급여
- 활성 상태

## 9-2. 완성 예시

```python
class Employee:
    def __init__(
        self,
        employee_id,
        name,
        email,
        department,
        salary,
        active=True,
    ):
        if employee_id <= 0:
            raise ValueError(
                "직원 ID는 1 이상이어야 합니다."
            )

        name = name.strip()
        email = email.strip()
        department = department.strip()

        if not name:
            raise ValueError(
                "이름을 입력해야 합니다."
            )

        if "@" not in email:
            raise ValueError(
                "이메일 형식이 올바르지 않습니다."
            )

        if not department:
            raise ValueError(
                "부서를 입력해야 합니다."
            )

        if salary < 0:
            raise ValueError(
                "급여는 음수일 수 없습니다."
            )

        self.employee_id = employee_id
        self.name = name
        self.email = email
        self.department = department
        self._salary = salary
        self.active = active

    @property
    def salary(self):
        return self._salary

    def change_salary(self, salary):
        if salary < 0:
            raise ValueError(
                "급여는 음수일 수 없습니다."
            )

        self._salary = salary

    def deactivate(self):
        self.active = False

    def to_dict(self):
        return {
            "employee_id": (
                self.employee_id
            ),
            "name": self.name,
            "email": self.email,
            "department": (
                self.department
            ),
            "salary": self.salary,
            "active": self.active,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            employee_id=data[
                "employee_id"
            ],
            name=data["name"],
            email=data["email"],
            department=data[
                "department"
            ],
            salary=data["salary"],
            active=data.get(
                "active",
                True,
            ),
        )
```

---

# 10. 직원 관리자 클래스

```python
class EmployeeManager:
    def __init__(self):
        self._employees = []

    def add_employee(self, employee):
        if self.find_by_id(
            employee.employee_id
        ):
            raise ValueError(
                "이미 존재하는 직원 ID입니다."
            )

        if self.find_by_email(
            employee.email
        ):
            raise ValueError(
                "이미 등록된 이메일입니다."
            )

        self._employees.append(
            employee
        )

    def find_by_id(self, employee_id):
        for employee in self._employees:
            if (
                employee.employee_id
                == employee_id
            ):
                return employee

        return None

    def find_by_email(self, email):
        for employee in self._employees:
            if employee.email == email:
                return employee

        return None

    def get_active_employees(self):
        return [
            employee
            for employee
            in self._employees
            if employee.active
        ]

    def get_by_department(
        self,
        department,
    ):
        return [
            employee
            for employee
            in self._employees
            if (
                employee.department
                == department
            )
        ]

    def sort_by_salary(
        self,
        reverse=True,
    ):
        return sorted(
            self._employees,
            key=lambda employee: (
                employee.salary
            ),
            reverse=reverse,
        )

    def get_average_salary(self):
        if not self._employees:
            return 0.0

        return (
            sum(
                employee.salary
                for employee
                in self._employees
            )
            / len(self._employees)
        )

    def to_dict_list(self):
        return [
            employee.to_dict()
            for employee
            in self._employees
        ]
```

---

# 11. 파일 저장과 불러오기

```python
import json
from pathlib import Path


def save_employees(
    file_path,
    manager,
):
    file_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with file_path.open(
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            manager.to_dict_list(),
            file,
            ensure_ascii=False,
            indent=2,
        )


def load_employees(file_path):
    manager = EmployeeManager()

    if not file_path.exists():
        return manager

    with file_path.open(
        "r",
        encoding="utf-8",
    ) as file:
        data = json.load(file)

    for item in data:
        employee = Employee.from_dict(
            item
        )
        manager.add_employee(employee)

    return manager
```

---

# 12. 프로젝트 실행 예시

```python
DATA_FILE = Path(
    "data/employees.json"
)

manager = load_employees(
    DATA_FILE
)

if not manager.find_by_id(1):
    manager.add_employee(
        Employee(
            employee_id=1,
            name="Kim",
            email="kim@humanjobs.com",
            department="개발",
            salary=3500000,
        )
    )

if not manager.find_by_id(2):
    manager.add_employee(
        Employee(
            employee_id=2,
            name="Lee",
            email="lee@humanjobs.com",
            department="디자인",
            salary=3200000,
        )
    )

if not manager.find_by_id(3):
    manager.add_employee(
        Employee(
            employee_id=3,
            name="Park",
            email="park@humanjobs.com",
            department="개발",
            salary=4100000,
        )
    )

save_employees(
    DATA_FILE,
    manager,
)

print("=== 활성 직원 ===")

for employee in (
    manager.get_active_employees()
):
    print(
        employee.name,
        employee.department,
        f"{employee.salary:,}원",
    )

print("=== 급여 높은 순 ===")

for employee in (
    manager.sort_by_salary()
):
    print(
        employee.name,
        f"{employee.salary:,}원",
    )

print(
    "평균 급여:",
    f"{manager.get_average_salary():,.0f}원",
)
```

## 12-1. 실행 결과

```text
=== 활성 직원 ===
Kim 개발 3,500,000원
Lee 디자인 3,200,000원
Park 개발 4,100,000원
=== 급여 높은 순 ===
Park 4,100,000원
Kim 3,500,000원
Lee 3,200,000원
평균 급여: 3,600,000원
```

---

# 13. 최종 프로젝트 구조 분리

처음에는 하나의 파일에서 작성해도 된다.

기능이 안정되면 다음처럼 나눌 수 있다.

```text
human_jobs/
├─ main.py
├─ models/
│  └─ employee.py
├─ services/
│  └─ employee_manager.py
├─ repositories/
│  └─ employee_repository.py
└─ data/
   └─ employees.json
```

역할:

```text
employee.py
→ 직원 데이터와 동작

employee_manager.py
→ 직원 검색·정렬·통계

employee_repository.py
→ 파일 저장·불러오기

main.py
→ 프로그램 실행 흐름
```

> [!TIP]
> 처음부터 파일을 과도하게 나누지 않는다.
>
> 기능이 동작하고 책임이 분명해진 뒤 모듈로 분리한다.

---

# 14. 최종 프로젝트 확장 과제

## 14-1. 기능 확장

- 직원 이름 검색
- 급여 범위 검색
- 부서 변경
- 이메일 변경
- 직원 삭제
- 비활성 직원만 조회
- 부서별 평균 급여
- 최고 급여 직원
- 직원 수 통계
- CSV 내보내기

## 14-2. 예외 처리 확장

- 사용자 정의 `EmployeeError`
- 중복 이메일 예외
- 존재하지 않는 직원 예외
- JSON 형식 오류
- 파일 접근 오류

## 14-3. 구조 확장

- CLI 메뉴
- 모듈 분리
- 테스트 코드
- 로그 기록
- 설정 파일
- 데이터베이스 연결

---

# 15. 리팩토링 체크 과정

종합 실습을 작성한 뒤 다음 순서로 검토한다.

```text
1. 요구사항을 모두 구현했는가?
2. 실행 결과가 예상과 같은가?
3. 변수명과 함수명이 역할을 설명하는가?
4. 중복 조건이 있는가?
5. 함수 하나에 여러 책임이 있는가?
6. 원본 데이터를 의도하지 않게 변경하는가?
7. 반환값이 일관적인가?
8. 예외 종류가 상황에 맞는가?
9. 파일 자원이 안전하게 닫히는가?
10. 기능을 추가하기 쉬운 구조인가?
```

---

# 16. 실습 파일을 직접 만들 때 권장 방식

각 프로젝트는 별도 폴더로 작성할 수 있다.

```text
workspace_python/
└─ projects/
   ├─ user_analysis/
   │  └─ main.py
   ├─ student_grade/
   │  └─ main.py
   ├─ inventory/
   │  └─ main.py
   ├─ cafe_order/
   │  └─ main.py
   ├─ bank_account/
   │  └─ main.py
   └─ human_jobs/
      ├─ main.py
      └─ data/
```

기능이 커지면 모듈을 분리한다.

---

# 17. 자주 하는 실수

## 17-1. 요구사항을 읽자마자 코드부터 작성

필요한 데이터 구조와 함수 역할을 먼저 생각한다.

## 17-2. 모든 코드를 하나의 함수에 작성

검증·계산·저장·출력 책임을 분리한다.

## 17-3. 입력값 검증 누락

빈 문자열, 음수, 중복 ID를 확인한다.

## 17-4. 정상 흐름과 오류 흐름 혼합

예외 처리 또는 Guard Clause로 분리한다.

## 17-5. 원본 데이터 의도하지 않게 변경

변경 목적이 아니라면 새 객체를 반환한다.

## 17-6. 파일 저장 전 폴더 생성 누락

`Path.mkdir(parents=True, exist_ok=True)`를 사용한다.

## 17-7. JSON 파일이 없을 때 바로 열기

파일 존재 여부를 확인한다.

## 17-8. 모든 기능을 처음부터 클래스화

단순 기능은 함수로 시작하고 상태가 필요할 때 클래스를 고려한다.

## 17-9. 실행 결과를 확인하지 않고 리팩토링

현재 결과를 먼저 고정한 뒤 구조를 변경한다.

## 17-10. 완성 예시를 그대로 복사하고 끝냄

변수명, 기능, 데이터 구조를 직접 바꿔 다시 작성한다.

---

# 18. 핵심 요약

```text
종합 실습
→ 문법을 하나의 프로그램으로 연결

요구사항
→ 데이터와 기능으로 분해

함수
→ 검증·계산·검색·출력 분리

클래스
→ 상태와 동작을 함께 관리

예외 처리
→ 잘못된 입력과 실패 흐름 관리

파일 입출력
→ 프로그램 상태 저장
```

```text
먼저 동작
    ↓
결과 확인
    ↓
이름 개선
    ↓
중복 제거
    ↓
함수 분리
    ↓
예외 처리
    ↓
모듈 분리
```

---

# 19. 최종 체크리스트

- [ ] 요구사항을 작은 기능으로 나누었는가?
- [ ] 적절한 자료형을 선택했는가?
- [ ] 함수 이름만 보고 역할을 이해할 수 있는가?
- [ ] 한 함수가 하나의 주요 책임을 가지는가?
- [ ] 입력값 검증을 수행하는가?
- [ ] 중복 ID·이메일을 확인하는가?
- [ ] 반환값이 일관적인가?
- [ ] 빈 목록과 없는 값을 처리하는가?
- [ ] 예외 종류가 상황에 맞는가?
- [ ] 파일은 `with`문으로 처리하는가?
- [ ] 경로는 `Path`를 사용하는가?
- [ ] 원본 데이터를 의도하지 않게 변경하지 않는가?
- [ ] 클래스가 실제로 필요한 구조인가?
- [ ] 실행 결과를 확인했는가?
- [ ] 확장 기능을 추가하기 쉬운가?
- [ ] 리팩토링 전후 결과가 동일한가?

---

# 마무리

Python 종합 실습의 목적은 정답 코드를 암기하는 것이 아니다.

```text
문제를 작은 단위로 나누고
    ↓
적절한 자료형과 문법을 선택하고
    ↓
함수와 클래스의 책임을 구분하고
    ↓
오류와 파일 저장 흐름을 관리하고
    ↓
동작하는 코드를 유지보수 가능한 코드로 개선하는 것
```

완성 예시를 그대로 사용하는 것보다, 이름·데이터·요구사항을 바꾸어 직접 확장할 때 더 많은 내용을 배울 수 있다.

# V3 동작 백과 보강 — 종합실습 실행 기록법

1. 요구사항을 입력·처리·출력·오류로 나눈다.
2. 입력 출처와 최초 자료형을 쓴다.
3. 함수·클래스별 반환값과 변경 상태를 쓴다.
4. 정상값, 경계값, 잘못된 입력의 결과를 각각 남긴다.
5. 예외 종류와 처리 위치를 정한다.
6. 내 코드와 강사님 코드의 차이를 실행 결과로 비교한다.

```text
[입력] 메뉴 번호 "1"(str) → [변환] int("1") → [분기] 기능 호출
→ [상태] 목록 변경 → [출력] 성공 메시지 → [저장] 파일 기록
```

`print`로 보인 값과 `return`으로 돌려준 값을 구분하고 재실행 시 저장 데이터가 복구되는지도 확인한다. 특정 한 파일에 없는 통합 설계는 **Wiki 종합 확장**으로 구분한다.
