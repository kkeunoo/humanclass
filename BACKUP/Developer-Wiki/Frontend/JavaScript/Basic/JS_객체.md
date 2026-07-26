---
title: JavaScript 객체
version: v1.0
last_updated: 2026-07-22
status: Completed
---

# JavaScript 객체

## 문서 정보

| 항목 | 내용 |
|------|------|
| 문서명 | JavaScript 객체 |
| 분류 | Frontend / JavaScript / Basic |
| 난이도 | Beginner |
| 선수 지식 | 변수, 자료형, 배열, 함수 |
| 핵심 주제 | Object, Property, Key, Value, 객체 생성, 프로퍼티 접근 |
| 버전 | v1.0 |
| 최종 수정일 | 2026-07-22 |

---

# 개요

객체(Object)는 여러 개의 데이터를 하나의 단위로 묶어서 관리하는 자료형이다.

배열은 데이터를 순서대로 저장하고 인덱스로 접근하지만, 객체는 각 데이터에 이름을 붙여 저장한다.

예를 들어 한 명의 회원 정보를 변수로 관리하면 다음과 같이 작성할 수 있다.

```javascript
const name = "홍길동";
const age = 20;
const address = "서울";
```

데이터가 많아질수록 서로 관련된 변수들이 흩어져 관리하기 어려워진다.

객체를 사용하면 관련된 데이터를 하나로 묶을 수 있다.

```javascript
const user = {
    name: "홍길동",
    age: 20,
    address: "서울"
};
```

객체는 사용자 정보, 상품 정보, 게시글, 주문 정보처럼 여러 속성을 가진 데이터를 표현할 때 사용한다.

---

# 객체가 필요한 이유

다음은 상품 정보를 각각의 변수에 저장한 예제이다.

```javascript
const productName = "노트북";
const productPrice = 1500000;
const productBrand = "ABC";
const productStock = 10;
```

변수만 사용해도 데이터를 저장할 수 있지만, 각 변수가 하나의 상품에 대한 정보라는 관계가 코드에 명확하게 드러나지 않는다.

객체를 사용하면 관련된 데이터를 하나의 변수에 모을 수 있다.

```javascript
const product = {
    name: "노트북",
    price: 1500000,
    brand: "ABC",
    stock: 10
};
```

객체를 사용하면 다음과 같은 장점이 있다.

- 관련된 데이터를 하나로 묶을 수 있다.
- 각 데이터의 의미를 이름으로 표현할 수 있다.
- 데이터를 읽고 수정하기 쉽다.
- 함수나 배열과 함께 활용하기 좋다.
- 실제 서비스의 데이터를 구조적으로 표현할 수 있다.

---

# 객체(Object)

객체는 여러 개의 값을 **프로퍼티(Property)** 형태로 저장하는 자료형이다.

기본 문법

```javascript
const 객체명 = {
    키: 값,
    키: 값
};
```

예제

```javascript
const user = {
    name: "홍길동",
    age: 20
};
```

객체는 중괄호 `{}`를 사용하여 생성한다.

객체 내부의 각 데이터는 다음과 같이 구성된다.

```text
키: 값
```

- 키(Key): 데이터의 이름
- 값(Value): 실제 저장된 데이터
- 프로퍼티(Property): 키와 값으로 구성된 하나의 데이터

---

# 프로퍼티(Property)

객체 안에 저장된 각각의 데이터를 프로퍼티라고 한다.

```javascript
const user = {
    name: "홍길동",
    age: 20,
    address: "서울"
};
```

위 객체에는 세 개의 프로퍼티가 있다.

| 키 | 값 |
|----|----|
| `name` | `"홍길동"` |
| `age` | `20` |
| `address` | `"서울"` |

다음 코드는 하나의 프로퍼티이다.

```javascript
name: "홍길동"
```

`name`은 키이고 `"홍길동"`은 값이다.

---

# 키(Key)

키는 객체 안에 저장된 데이터를 구분하는 이름이다.

```javascript
const student = {
    name: "김학생",
    score: 90,
    grade: "A"
};
```

위 객체의 키는 다음과 같다.

```text
name
score
grade
```

키는 보통 데이터의 의미를 알 수 있도록 작성한다.

좋은 예

```javascript
const user = {
    userName: "홍길동",
    userAge: 20,
    userEmail: "user@example.com"
};
```

좋지 않은 예

```javascript
const user = {
    a: "홍길동",
    b: 20,
    c: "user@example.com"
};
```

키의 이름만 보아도 어떤 데이터인지 알 수 있도록 작성하는 것이 좋다.

---

# 값(Value)

객체의 값에는 다양한 자료형을 저장할 수 있다.

```javascript
const user = {
    name: "홍길동",
    age: 20,
    isMember: true,
    address: null
};
```

객체의 값으로 사용할 수 있는 자료형은 다음과 같다.

- 문자열
- 숫자
- Boolean
- `null`
- 배열
- 객체
- 함수

현재 문서에서는 문자열, 숫자, Boolean과 같은 기본적인 값을 중심으로 학습한다.

배열, 객체, 함수를 값으로 사용하는 방법은 뒤에서 살펴본다.

---

# 객체 생성

객체는 중괄호 `{}`를 사용하여 생성한다.

```javascript
const 객체명 = {};
```

빈 객체 생성

```javascript
const user = {};

console.log(user);
```

결과

```text
{}
```

객체를 생성하면서 프로퍼티를 함께 작성할 수도 있다.

```javascript
const user = {
    name: "홍길동",
    age: 20
};
```

---

# 여러 개의 프로퍼티 작성

객체 안에 여러 개의 프로퍼티를 작성할 때는 쉼표 `,`로 구분한다.

```javascript
const product = {
    name: "키보드",
    price: 50000,
    stock: 20
};
```

마지막 프로퍼티 뒤의 쉼표는 생략할 수 있다.

```javascript
const product = {
    name: "키보드",
    price: 50000,
    stock: 20,
};
```

마지막에도 쉼표를 작성하면 이후 프로퍼티를 추가하거나 순서를 변경할 때 편리한 경우가 있다.

---

# 점 표기법

객체의 프로퍼티에 접근하는 가장 일반적인 방법은 점 표기법이다.

기본 문법

```javascript
객체명.키
```

예제

```javascript
const user = {
    name: "홍길동",
    age: 20
};

console.log(user.name);
console.log(user.age);
```

결과

```text
홍길동
20
```

`user.name`은 `user` 객체의 `name` 프로퍼티에 접근한다는 의미이다.

---

# 대괄호 표기법

객체의 프로퍼티는 대괄호 표기법으로도 접근할 수 있다.

기본 문법

```javascript
객체명["키"]
```

예제

```javascript
const user = {
    name: "홍길동",
    age: 20
};

console.log(user["name"]);
console.log(user["age"]);
```

결과

```text
홍길동
20
```

대괄호 안의 키는 문자열로 작성한다.

```javascript
user["name"]
```

다음처럼 따옴표를 생략하면 `name`이라는 변수를 찾게 된다.

```javascript
user[name]
```

`name` 변수가 선언되어 있지 않다면 오류가 발생할 수 있다.

---

# 점 표기법과 대괄호 표기법 비교

```javascript
const user = {
    name: "홍길동",
    age: 20
};

console.log(user.name);
console.log(user["name"]);
```

두 코드는 같은 값을 반환한다.

```text
홍길동
홍길동
```

| 표기법 | 문법 |
|--------|------|
| 점 표기법 | `객체명.키` |
| 대괄호 표기법 | `객체명["키"]` |

일반적인 경우에는 점 표기법이 더 간단하고 읽기 쉽다.

대괄호 표기법은 키를 변수로 전달하거나 특수한 키 이름을 사용할 때 필요하다.

---

# 변수에 저장된 키로 접근하기

대괄호 표기법을 사용하면 변수에 저장된 값으로 프로퍼티에 접근할 수 있다.

```javascript
const user = {
    name: "홍길동",
    age: 20
};

const key = "name";

console.log(user[key]);
```

결과

```text
홍길동
```

`key` 변수에는 `"name"`이 저장되어 있으므로 다음 코드와 같은 의미이다.

```javascript
console.log(user["name"]);
```

점 표기법에서는 변수의 값을 키로 사용할 수 없다.

```javascript
console.log(user.key);
```

위 코드는 `key` 변수의 값을 사용하는 것이 아니라, 이름이 `key`인 프로퍼티를 찾는다.

---

# 존재하지 않는 프로퍼티

객체에 존재하지 않는 프로퍼티에 접근하면 `undefined`가 반환된다.

```javascript
const user = {
    name: "홍길동",
    age: 20
};

console.log(user.address);
```

결과

```text
undefined
```

존재하지 않는 프로퍼티에 접근했다고 해서 바로 오류가 발생하는 것은 아니다.

하지만 반환된 `undefined`를 이용해 다른 작업을 수행할 때 문제가 생길 수 있으므로 주의해야 한다.

---

# 객체 출력

객체 전체를 확인할 때는 `console.log()`를 사용할 수 있다.

```javascript
const user = {
    name: "홍길동",
    age: 20,
    address: "서울"
};

console.log(user);
```

브라우저 개발자 도구에서는 객체 내부의 프로퍼티를 펼쳐서 확인할 수 있다.

특정 프로퍼티만 확인하려면 다음처럼 작성한다.

```javascript
console.log(user.name);
console.log(user.age);
```

---

# 객체와 배열 비교

배열과 객체는 여러 개의 데이터를 저장할 수 있다는 공통점이 있다.

하지만 데이터를 관리하는 방식이 다르다.

## 배열

```javascript
const user = [
    "홍길동",
    20,
    "서울"
];
```

배열은 인덱스를 이용하여 값에 접근한다.

```javascript
console.log(user[0]);
console.log(user[1]);
```

인덱스만 보아서는 각 값이 어떤 의미인지 바로 알기 어렵다.

---

## 객체

```javascript
const user = {
    name: "홍길동",
    age: 20,
    address: "서울"
};
```

객체는 키를 이용하여 값에 접근한다.

```javascript
console.log(user.name);
console.log(user.age);
```

키의 이름을 통해 각 값의 의미를 쉽게 파악할 수 있다.

---

## 배열과 객체의 주요 차이

| 구분 | 배열 | 객체 |
|------|------|------|
| 데이터 관리 방식 | 순서 | 이름 |
| 접근 방법 | 인덱스 | 키 |
| 기본 문법 | `[]` | `{}` |
| 적합한 데이터 | 목록 | 하나의 대상에 대한 정보 |
| 예시 | 상품 목록, 점수 목록 | 회원, 상품, 게시글 |

배열은 같은 성격의 데이터 목록을 저장할 때 적합하다.

객체는 하나의 대상을 구성하는 여러 정보를 저장할 때 적합하다.

---

---

# 프로퍼티 값 수정

객체에 저장된 프로퍼티 값은 점 표기법 또는 대괄호 표기법을 이용하여 수정할 수 있다.

## 점 표기법으로 수정

```javascript
const user = {
    name: "홍길동",
    age: 20
};

user.age = 21;

console.log(user);
```

결과

```text
{
    name: "홍길동",
    age: 21
}
```

기존에 존재하는 프로퍼티에 새로운 값을 대입하면 값이 변경된다.

---

## 대괄호 표기법으로 수정

```javascript
const user = {
    name: "홍길동",
    age: 20
};

user["name"] = "김철수";

console.log(user);
```

결과

```text
{
    name: "김철수",
    age: 20
}
```

점 표기법과 대괄호 표기법 모두 프로퍼티 값을 수정할 수 있다.

---

# 새로운 프로퍼티 추가

객체에 존재하지 않는 프로퍼티에 값을 대입하면 새로운 프로퍼티가 추가된다.

```javascript
const user = {
    name: "홍길동",
    age: 20
};

user.address = "서울";

console.log(user);
```

결과

```text
{
    name: "홍길동",
    age: 20,
    address: "서울"
}
```

객체를 처음 생성할 때 모든 프로퍼티를 작성하지 않아도 나중에 추가할 수 있다.

---

## 대괄호 표기법으로 추가

```javascript
const user = {
    name: "홍길동"
};

user["email"] = "user@example.com";

console.log(user);
```

결과

```text
{
    name: "홍길동",
    email: "user@example.com"
}
```

---

# 프로퍼티 추가와 수정의 구분

객체에 프로퍼티 값을 대입하는 문법은 같다.

```javascript
객체명.키 = 값;
```

해당 키가 이미 존재하면 값이 수정된다.

해당 키가 존재하지 않으면 새로운 프로퍼티가 추가된다.

```javascript
const product = {
    name: "키보드",
    price: 50000
};

// 기존 프로퍼티 수정
product.price = 45000;

// 새로운 프로퍼티 추가
product.stock = 10;

console.log(product);
```

결과

```text
{
    name: "키보드",
    price: 45000,
    stock: 10
}
```

---

# 프로퍼티 삭제

객체의 프로퍼티를 삭제할 때는 `delete` 연산자를 사용한다.

기본 문법

```javascript
delete 객체명.키;
```

예제

```javascript
const user = {
    name: "홍길동",
    age: 20,
    address: "서울"
};

delete user.address;

console.log(user);
```

결과

```text
{
    name: "홍길동",
    age: 20
}
```

---

## 대괄호 표기법으로 삭제

```javascript
const user = {
    name: "홍길동",
    age: 20
};

delete user["age"];

console.log(user);
```

결과

```text
{
    name: "홍길동"
}
```

---

# const 객체의 값 변경

`const`로 선언한 변수는 다른 값으로 다시 대입할 수 없다.

```javascript
const user = {
    name: "홍길동"
};

user = {
    name: "김철수"
};
```

위 코드는 `user` 변수에 새로운 객체를 다시 대입하려고 했기 때문에 오류가 발생한다.

하지만 객체 내부의 프로퍼티는 변경할 수 있다.

```javascript
const user = {
    name: "홍길동",
    age: 20
};

user.name = "김철수";
user.age = 30;

console.log(user);
```

결과

```text
{
    name: "김철수",
    age: 30
}
```

`const`는 객체 내부를 변경하지 못하게 하는 것이 아니라, 변수에 저장된 객체 자체를 다른 값으로 다시 대입하지 못하게 한다.

---

# 객체 안에 배열 저장하기

객체의 값으로 배열을 저장할 수 있다.

```javascript
const student = {
    name: "김학생",
    subjects: [
        "HTML",
        "CSS",
        "JavaScript"
    ]
};
```

배열에 접근하려면 먼저 객체의 프로퍼티에 접근한 뒤 인덱스를 사용한다.

```javascript
console.log(student.subjects);
console.log(student.subjects[0]);
console.log(student.subjects[1]);
```

결과

```text
["HTML", "CSS", "JavaScript"]
HTML
CSS
```

---

## 객체 안의 배열 요소 추가

객체 안에 저장된 배열에도 배열 메서드를 사용할 수 있다.

```javascript
const student = {
    name: "김학생",
    subjects: [
        "HTML",
        "CSS"
    ]
};

student.subjects.push("JavaScript");

console.log(student.subjects);
```

결과

```text
["HTML", "CSS", "JavaScript"]
```

---

# 객체 안에 객체 저장하기

객체의 값으로 또 다른 객체를 저장할 수 있다.

이를 중첩 객체라고 한다.

```javascript
const user = {
    name: "홍길동",
    address: {
        city: "서울",
        district: "강남구"
    }
};
```

중첩된 객체의 프로퍼티는 점 표기법을 연속으로 사용하여 접근한다.

```javascript
console.log(user.address);
console.log(user.address.city);
console.log(user.address.district);
```

결과

```text
{
    city: "서울",
    district: "강남구"
}
서울
강남구
```

---

## 중첩 객체 값 수정

```javascript
const user = {
    name: "홍길동",
    address: {
        city: "서울",
        district: "강남구"
    }
};

user.address.district = "서초구";

console.log(user.address.district);
```

결과

```text
서초구
```

---

# 배열 안에 객체 저장하기

배열의 요소로 객체를 저장할 수 있다.

```javascript
const users = [
    {
        name: "홍길동",
        age: 20
    },
    {
        name: "김철수",
        age: 25
    },
    {
        name: "이영희",
        age: 30
    }
];
```

배열 안의 객체에 접근하려면 먼저 인덱스로 배열 요소에 접근한 뒤 객체의 프로퍼티에 접근한다.

```javascript
console.log(users[0]);
console.log(users[0].name);
console.log(users[1].age);
```

결과

```text
{
    name: "홍길동",
    age: 20
}
홍길동
25
```

---

# 배열 안의 객체 값 수정

```javascript
const products = [
    {
        name: "키보드",
        price: 50000
    },
    {
        name: "마우스",
        price: 30000
    }
];

products[0].price = 45000;

console.log(products[0]);
```

결과

```text
{
    name: "키보드",
    price: 45000
}
```

---

# 객체 배열과 반복문

배열 안에 여러 객체가 저장되어 있다면 반복문을 이용하여 순서대로 처리할 수 있다.

```javascript
const users = [
    {
        name: "홍길동",
        age: 20
    },
    {
        name: "김철수",
        age: 25
    },
    {
        name: "이영희",
        age: 30
    }
];

for (let i = 0; i < users.length; i++) {

    console.log(users[i].name);
    console.log(users[i].age);

}
```

결과

```text
홍길동
20
김철수
25
이영희
30
```

실무에서는 사용자 목록, 상품 목록, 게시글 목록처럼 여러 데이터를 관리할 때 객체 배열을 자주 사용한다.

---

# 객체와 배열 조합 정리

## 객체 안의 배열

```javascript
const user = {
    hobbies: [
        "영화",
        "운동"
    ]
};
```

접근

```javascript
console.log(user.hobbies[0]);
```

---

## 객체 안의 객체

```javascript
const user = {
    address: {
        city: "서울"
    }
};
```

접근

```javascript
console.log(user.address.city);
```

---

## 배열 안의 객체

```javascript
const users = [
    {
        name: "홍길동"
    }
];
```

접근

```javascript
console.log(users[0].name);
```

---

# 객체 작성 시 주의사항

- 각 프로퍼티는 쉼표로 구분한다.
- 점 표기법에서는 키 이름에 따옴표를 사용하지 않는다.
- 대괄호 표기법에서는 일반적으로 키를 문자열로 작성한다.
- 존재하지 않는 프로퍼티에 접근하면 `undefined`가 반환된다.
- `const` 객체도 내부 프로퍼티는 수정할 수 있다.
- 객체와 배열을 함께 사용할 때 접근 순서를 정확히 확인해야 한다.
- 중첩 구조가 깊어질수록 점과 대괄호의 위치를 주의해야 한다.

---

---

# 객체의 프로퍼티 값으로 함수 저장하기

객체의 프로퍼티 값에는 함수도 저장할 수 있다.

```javascript
const user = {
    name: "홍길동",
    greeting: function() {
        console.log("안녕하세요.");
    }
};
```

함수가 저장된 프로퍼티를 실행하려면 괄호 `()`를 붙인다.

```javascript
user.greeting();
```

결과

```text
안녕하세요.
```

객체 안에 저장된 함수를 일반적으로 **메서드(Method)** 라고 한다.

---

# 메서드(Method)

메서드는 객체가 가지고 있는 함수이다.

```javascript
const calculator = {
    add: function(a, b) {
        return a + b;
    }
};
```

메서드 호출

```javascript
const result = calculator.add(10, 20);

console.log(result);
```

결과

```text
30
```

메서드를 호출할 때는 객체 이름과 프로퍼티 이름을 함께 작성한다.

```javascript
객체명.메서드명();
```

---

# 일반 프로퍼티와 메서드 비교

```javascript
const user = {
    name: "홍길동",
    age: 20,
    greeting: function() {
        console.log("안녕하세요.");
    }
};
```

위 객체에서 다음은 일반 프로퍼티이다.

```javascript
name: "홍길동"
age: 20
```

다음은 함수가 저장된 프로퍼티이므로 메서드이다.

```javascript
greeting: function() {
    console.log("안녕하세요.");
}
```

| 구분 | 값 |
|------|----|
| 일반 프로퍼티 | 문자열, 숫자, Boolean 등 |
| 메서드 | 함수 |

---

# 메서드에 매개변수 사용하기

객체의 메서드도 일반 함수처럼 매개변수를 사용할 수 있다.

```javascript
const calculator = {
    add: function(a, b) {
        return a + b;
    },
    subtract: function(a, b) {
        return a - b;
    }
};
```

메서드 호출

```javascript
console.log(calculator.add(10, 5));
console.log(calculator.subtract(10, 5));
```

결과

```text
15
5
```

---

# 메서드에서 객체의 프로퍼티 사용하기

객체의 메서드에서는 같은 객체 안에 있는 프로퍼티를 사용할 수 있다.

```javascript
const user = {
    name: "홍길동",
    age: 20,
    introduce: function() {
        console.log("이름: " + this.name);
        console.log("나이: " + this.age);
    }
};
```

메서드 호출

```javascript
user.introduce();
```

결과

```text
이름: 홍길동
나이: 20
```

여기서 `this`는 현재 메서드를 가지고 있는 객체를 가리킨다.

---

# this 기초

객체의 메서드 안에서 `this`는 일반적으로 해당 메서드를 호출한 객체를 가리킨다.

```javascript
const student = {
    name: "김학생",
    score: 90,
    printInfo: function() {
        console.log(this.name);
        console.log(this.score);
    }
};

student.printInfo();
```

결과

```text
김학생
90
```

위 코드에서 `this`는 `student` 객체를 의미한다.

따라서 다음 코드는

```javascript
this.name
```

다음 코드와 비슷한 의미로 이해할 수 있다.

```javascript
student.name
```

---

# this를 사용하는 이유

객체 이름을 직접 작성하면 객체 이름이 변경되었을 때 메서드 내부도 수정해야 할 수 있다.

```javascript
const user = {
    name: "홍길동",
    introduce: function() {
        console.log(user.name);
    }
};
```

`this`를 사용하면 현재 메서드를 호출한 객체를 기준으로 프로퍼티에 접근할 수 있다.

```javascript
const user = {
    name: "홍길동",
    introduce: function() {
        console.log(this.name);
    }
};
```

현재 단계에서는 `this`를 다음과 같이 이해하면 충분하다.

> 객체의 메서드 안에서 현재 객체의 프로퍼티에 접근할 때 사용하는 키워드

`this`의 동작 방식은 호출 방법에 따라 달라질 수 있으며, 이후 JavaScript 심화 과정에서 자세히 학습한다.

---

# 객체 메서드로 값 변경하기

메서드 안에서 객체의 프로퍼티 값을 변경할 수 있다.

```javascript
const user = {
    name: "홍길동",
    age: 20,
    birthday: function() {
        this.age = this.age + 1;
    }
};

user.birthday();

console.log(user.age);
```

결과

```text
21
```

메서드를 이용하면 객체의 데이터와 관련된 기능을 하나의 객체 안에서 관리할 수 있다.

---

# 객체 메서드로 값 반환하기

객체의 메서드도 `return`을 사용하여 값을 반환할 수 있다.

```javascript
const product = {
    name: "키보드",
    price: 50000,
    getPrice: function() {
        return this.price;
    }
};

const result = product.getPrice();

console.log(result);
```

결과

```text
50000
```

---

# 객체를 함수의 매개변수로 전달하기

객체는 함수의 매개변수로 전달할 수 있다.

```javascript
const user = {
    name: "홍길동",
    age: 20
};

function printUser(userInfo) {
    console.log(userInfo.name);
    console.log(userInfo.age);
}

printUser(user);
```

결과

```text
홍길동
20
```

함수는 전달받은 객체의 프로퍼티에 접근하여 데이터를 사용할 수 있다.

---

# 함수에서 객체 반환하기

함수는 객체를 반환할 수도 있다.

```javascript
function createUser(name, age) {
    const user = {
        name: name,
        age: age
    };

    return user;
}

const user1 = createUser("홍길동", 20);
const user2 = createUser("김철수", 25);

console.log(user1);
console.log(user2);
```

결과

```text
{
    name: "홍길동",
    age: 20
}

{
    name: "김철수",
    age: 25
}
```

같은 구조의 객체를 여러 개 생성해야 할 때 함수와 객체를 함께 사용할 수 있다.

---

# 객체 생성 함수 기초 예제

다음 함수는 상품 정보를 객체로 만들어 반환한다.

```javascript
function createProduct(name, price, stock) {
    const product = {
        name: name,
        price: price,
        stock: stock
    };

    return product;
}
```

함수 호출

```javascript
const keyboard = createProduct(
    "키보드",
    50000,
    10
);

const mouse = createProduct(
    "마우스",
    30000,
    20
);

console.log(keyboard);
console.log(mouse);
```

객체를 만드는 코드를 함수로 작성하면 같은 구조를 반복해서 작성하지 않아도 된다.

---

# 객체 배열 활용 패턴

실무에서는 배열 안에 여러 객체를 저장하는 구조를 자주 사용한다.

```javascript
const products = [
    {
        name: "키보드",
        price: 50000,
        stock: 10
    },
    {
        name: "마우스",
        price: 30000,
        stock: 20
    },
    {
        name: "모니터",
        price: 300000,
        stock: 5
    }
];
```

---

## 객체 배열 전체 출력

```javascript
for (let i = 0; i < products.length; i++) {

    console.log(products[i].name);
    console.log(products[i].price);
    console.log(products[i].stock);

}
```

---

## 특정 조건의 객체 출력

가격이 `50000` 이상인 상품만 출력하는 예제이다.

```javascript
for (let i = 0; i < products.length; i++) {

    if (products[i].price >= 50000) {

        console.log(products[i].name);

    }

}
```

결과

```text
키보드
모니터
```

---

## 재고가 있는 상품 출력

```javascript
for (let i = 0; i < products.length; i++) {

    if (products[i].stock > 0) {

        console.log(products[i].name);

    }

}
```

---

## 객체 배열의 값 수정

```javascript
for (let i = 0; i < products.length; i++) {

    if (products[i].name === "키보드") {

        products[i].price = 45000;

    }

}
```

조건에 맞는 객체를 찾은 뒤 해당 객체의 프로퍼티를 수정할 수 있다.

---

# 객체 작성 원칙

객체를 작성할 때는 다음 원칙을 지키는 것이 좋다.

- 하나의 객체에는 하나의 대상에 대한 정보를 저장한다.
- 키 이름만 보아도 값의 의미를 알 수 있도록 작성한다.
- 서로 관련된 데이터만 하나의 객체로 묶는다.
- Boolean 값은 상태를 알 수 있도록 이름을 작성한다.
- 객체 구조가 지나치게 깊어지지 않도록 주의한다.
- 반복되는 객체 구조는 함수를 활용하여 생성할 수 있다.

---

# 좋은 객체 키 이름

좋은 예

```javascript
const user = {
    userName: "홍길동",
    userAge: 20,
    isMember: true
};
```

좋지 않은 예

```javascript
const user = {
    a: "홍길동",
    b: 20,
    c: true
};
```

Boolean 값은 다음과 같이 상태가 드러나는 이름을 사용하는 것이 좋다.

```javascript
const product = {
    isSoldOut: false,
    isVisible: true
};
```

---

# 실무 활용 예제

## 회원 정보 관리

```javascript
const member = {
    name: "홍길동",
    email: "user@example.com",
    isLogin: false,
    login: function() {
        this.isLogin = true;
    },
    logout: function() {
        this.isLogin = false;
    }
};
```

로그인 처리

```javascript
member.login();

console.log(member.isLogin);
```

결과

```text
true
```

로그아웃 처리

```javascript
member.logout();

console.log(member.isLogin);
```

결과

```text
false
```

---

## 상품 재고 관리

```javascript
const product = {
    name: "키보드",
    stock: 10,
    sell: function() {

        if (this.stock > 0) {

            this.stock = this.stock - 1;

        }

    }
};

product.sell();

console.log(product.stock);
```

결과

```text
9
```

객체에 데이터와 관련 기능을 함께 저장하면 하나의 대상에 대한 상태와 동작을 한곳에서 관리할 수 있다.

---

# 객체 사용 시 주의사항

- 메서드를 호출할 때는 괄호 `()`를 작성해야 한다.
- `this`를 객체 이름과 같은 단순 변수라고 생각하지 않는다.
- 존재하지 않는 메서드를 호출하면 오류가 발생한다.
- 프로퍼티와 메서드의 이름이 중복되지 않도록 주의한다.
- 객체 배열을 순회할 때 배열 인덱스와 객체 키의 접근 순서를 구분한다.
- 중첩된 값에 접근할 때 중간 프로퍼티가 존재하는지 확인해야 한다.
- 객체를 함수에 전달하면 객체 내부 값이 변경될 수 있으므로 주의한다.

---

---

# 실무 예제 프로젝트

다음은 여러 명의 회원 정보를 객체 배열로 관리하는 예제이다.

## HTML

```html
<h2>회원 목록</h2>

<ul id="memberList"></ul>
```

---

## JavaScript

```javascript
const members = [
    {
        name: "홍길동",
        age: 20
    },
    {
        name: "김철수",
        age: 25
    },
    {
        name: "이영희",
        age: 30
    }
];

const memberList = document.querySelector("#memberList");

let html = "";

for (let i = 0; i < members.length; i++) {

    html += `
        <li>
            이름 : ${members[i].name}<br>
            나이 : ${members[i].age}
        </li>
    `;

}

memberList.innerHTML = html;
```

실행 결과

```text
이름 : 홍길동
나이 : 20

이름 : 김철수
나이 : 25

이름 : 이영희
나이 : 30
```

객체와 배열을 함께 사용하면 여러 개의 데이터를 구조적으로 관리할 수 있다.

실무에서는 회원 목록, 상품 목록, 게시글 목록 등을 대부분 이러한 형태로 관리한다.

---

## 학습한 내용

- 객체(Object)
- 프로퍼티(Property)
- 키(Key)
- 값(Value)
- 객체 생성
- 점 표기법
- 대괄호 표기법
- 프로퍼티 추가
- 프로퍼티 수정
- 프로퍼티 삭제
- 메서드(Method)
- `this`
- 객체 안의 배열
- 배열 안의 객체

---

# 실무 활용

## 1. 회원 정보 관리

```javascript
const user = {
    name: "홍길동",
    age: 20,
    email: "user@example.com"
};

console.log(user.name);
```

---

## 2. 상품 정보 관리

```javascript
const product = {
    name: "키보드",
    price: 50000,
    stock: 10
};

console.log(product.stock);
```

---

## 3. 로그인 상태 관리

```javascript
const member = {
    id: "hong",
    isLogin: false
};

member.isLogin = true;
```

Boolean 프로퍼티를 이용하여 상태를 관리할 수 있다.

---

## 4. 게시글 목록 관리

```javascript
const posts = [
    {
        title: "첫 번째 글",
        writer: "홍길동"
    },
    {
        title: "두 번째 글",
        writer: "김철수"
    }
];

console.log(posts[0].title);
```

---

## 5. 객체 배열 반복 처리

```javascript
const products = [
    {
        name: "키보드",
        price: 50000
    },
    {
        name: "마우스",
        price: 30000
    }
];

for (let i = 0; i < products.length; i++) {

    console.log(products[i].name);

}
```

객체 배열은 반복문과 함께 사용하는 경우가 매우 많다.

---

# 이번 문서에서 새롭게 배운 내용

- 객체는 여러 데이터를 하나의 단위로 관리하는 자료형이다.
- 객체는 키(Key)와 값(Value)의 쌍으로 데이터를 저장한다.
- 객체의 각 데이터는 프로퍼티(Property)라고 한다.
- 점 표기법과 대괄호 표기법으로 프로퍼티에 접근할 수 있다.
- 새로운 프로퍼티를 추가하거나 기존 값을 수정할 수 있다.
- `delete`를 이용하여 프로퍼티를 삭제할 수 있다.
- 객체의 값으로 함수를 저장하면 메서드(Method)가 된다.
- 메서드 내부에서는 `this`를 사용하여 현재 객체의 프로퍼티에 접근할 수 있다.
- 객체와 배열을 함께 사용하면 실제 서비스 데이터를 효율적으로 표현할 수 있다.

---

# 자주 하는 실수

- 배열과 객체를 같은 개념으로 생각한다.
- 점 표기법과 대괄호 표기법을 혼동한다.
- 대괄호 표기법에서 문자열 키를 따옴표 없이 작성한다.
- 존재하지 않는 프로퍼티를 사용할 때 `undefined`를 고려하지 않는다.
- `const` 객체는 내부 값도 변경할 수 없다고 생각한다.
- 메서드를 호출하면서 괄호 `()`를 생략한다.
- `this`를 일반 변수처럼 이해한다.
- 객체 배열에서 인덱스와 프로퍼티 접근 순서를 혼동한다.

---

# 면접 포인트

### 객체(Object)란?

여러 개의 데이터를 하나의 단위로 관리하기 위한 자료형이다.

관련된 데이터를 키(Key)와 값(Value)의 형태로 저장한다.

---

### 배열과 객체의 차이는?

- 배열은 순서가 있는 데이터를 저장한다.
- 객체는 이름이 있는 데이터를 저장한다.

배열은 인덱스로 접근하고, 객체는 키로 접근한다.

---

### 프로퍼티(Property)란?

객체 안에 저장된 하나의 데이터이다.

`키(Key)`와 `값(Value)`으로 구성된다.

---

### 점 표기법과 대괄호 표기법의 차이는?

- 점 표기법은 일반적인 경우에 사용한다.
- 대괄호 표기법은 변수에 저장된 키를 사용할 때 또는 특수한 키 이름에 접근할 때 사용한다.

---

### 메서드(Method)란?

객체의 프로퍼티 값으로 저장된 함수이다.

객체의 데이터와 관련된 기능을 함께 관리할 수 있다.

---

### `this`란?

객체의 메서드 안에서 현재 메서드를 호출한 객체를 가리키는 키워드이다.

기초 단계에서는 **현재 객체의 프로퍼티에 접근하기 위한 키워드**로 이해하면 충분하다.

---

# 핵심 정리

- 객체는 여러 데이터를 하나의 변수에 구조적으로 저장한다.
- 객체는 키(Key)와 값(Value)의 형태로 데이터를 관리한다.
- 프로퍼티는 객체를 구성하는 하나의 데이터이다.
- 점 표기법과 대괄호 표기법으로 프로퍼티에 접근한다.
- 객체는 프로퍼티를 추가·수정·삭제할 수 있다.
- 객체의 프로퍼티 값으로 함수를 저장하면 메서드가 된다.
- `this`는 현재 객체의 프로퍼티를 참조할 때 사용한다.
- 객체와 배열은 함께 사용하는 경우가 매우 많다.

---

# 변경 이력

| Version | 날짜 | 변경 내용 |
|---------|------|----------|
| v1.0 | 2026-07-22 | 최초 작성 |
