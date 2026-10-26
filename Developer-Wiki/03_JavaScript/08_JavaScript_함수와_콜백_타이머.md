# 08. 함수 — 전달한 값으로 일하고 결과 돌려주기

[JavaScript 목차](README.md) · [이전: 날짜](07_JavaScript_Date와_날짜처리.md) · [다음: 함수 참조와 콜백](08-02_JavaScript_함수참조와_콜백.md)

원래 08번 주제를 **함수 → 참조·콜백 → 타이머** 순으로 나누었다. 기준 원본은 모두 양쪽 `08_function.html`이다. 이 장은 선언·호출·매개변수·반환·범위에 집중한다.

<!-- chapter-toc -->

- [1. 선언과 호출](#section-1)
- [2. 안쪽 호출부터 결과 전달하기](#section-2)
- [3. 범위와 가려짐](#section-3)
- [4. 생략한 인수와 기본값](#section-4)
- [5. 짧은 복습](#section-5)
- [추가로 알면 좋은 것](#section-6)

<a id="section-1"></a>

## 1. 선언과 호출

`function hello() { ... }`는 함수를 정의한다. `hello()`는 실행 요청이다. 정의만 했다고 본문이 곧바로 실행되지는 않는다. 함수 이름을 부를 때 붙이는 괄호와 함수 선언의 괄호를 구분하자.

| 말 | 예 | 의미 |
| --- | --- | --- |
| 매개변수 | width, height | 함수 안에서 전달값을 받을 이름 |
| 인수 | 10, 20 | 호출할 때 전달하는 값 |
| return | return area | 호출한 쪽에 결과를 돌려주고 해당 호출 종료 |
| 지역변수 | 함수 안 let area | 그 범위 안에서 사용하는 이름 |

### 강사님 코드

출처: `teacher/workspace_html/javascript/08_function.html` 17–31행 · **원본 발췌**

```javascript
    function getArea(width, height){
        console.log(`width: ${width}, height: ${height}`)
        let area = width * height
        console.log('면적: ', area)
    }
    getArea(10, 20)

    function getArea2(width, height){
        console.log(`width: ${width}, height: ${height}`)
        let area = width * height
        return area
    }

    let result = getArea2(10, 20)
    console.log(result)
```

### 내 코드

출처: `me/workspace_html/javascript/08_function.html` 18–35행 · **원본 발췌**

```javascript
            function getArea(width, height) {
                console.log(`width: ${width}, height: ${height}`)
                let area = width * height;
                console.log('면적 : ', area);
            }
            
            getArea(10, 20);
            
            // 함수는 이름이 같을 경우 아래것을 덮어쓰게 됨
            function getArea2(width, height) {
                console.log(`width: ${width}, height: ${height}`)
                let area = width * height;
                return area;
            }

            // 200을 리턴했으니 아래 getArea2가 200이라는 값을 가지게 됨
            let result = getArea2(10, 20);
            console.log(result)
```

같은 비교다. getArea는 면적 200을 **출력**하지만 값을 반환하지 않아 호출 결과는 undefined다. getArea2는 200을 반환하므로 result에 저장해 다음 계산에 쓸 수 있다. 내 주석의 ‘getArea2가 200이라는 값을 가짐’은 **getArea2(10,20) 호출 결과가 200**이라는 뜻으로 읽는다. 함수 자체가 숫자 200으로 바뀌지는 않는다.

<a id="section-2"></a>

## 2. 안쪽 호출부터 결과 전달하기

강사님 46행 `plus(2, plus(5,6))`은 안쪽 결과 11을 바깥 y에 전달하여 13을 반환한다. 내 54행 `plus(2, plus(result,6))`은 앞의 result=5를 사용하여 같은 결과 13이다. 다만 앞의 result가 달라지면 결과도 바뀌므로 항상 같은 식인 것은 아니다.

console.log는 화면에 정보를 보여 주는 역할이고 return은 다음 계산에 값을 전달하는 역할이다. 숫자 13을 출력했다는 이유만으로 그 함수가 13을 반환한다고 판단하지 않는다. 원본 plus의 내부 const z와 바깥 const z는 서로 다른 범위의 이름이다.

<a id="section-3"></a>

## 3. 범위와 가려짐

양쪽 중괄호 실습에서 안쪽은 바깥 a를 읽을 수 있지만 바깥은 안쪽 b를 읽지 못한다. 내 파일에는 안쪽에 같은 이름 a를 새로 선언하는 실험이 주석으로 추가되어 있다. 안쪽 a가 있다면 그 블록에서는 바깥 a가 가려진다. 선언 전에 안쪽 a를 읽으면 오류가 난다는 주석을 **현재 실행 중인 코드의 오류**로 혼동하지 않는다. 현재 해당 선언은 주석이다.

같은 함수 이름 print를 두 번 선언한 일반 스크립트 예제는 두 번째 함수가 사용된다. 이것을 let으로 같은 이름을 두 번 선언해도 된다는 규칙으로 확대하지 않는다. 함수 선언과 let 함수 표현식은 선언 방식이 다르다.

<a id="section-4"></a>

## 4. 생략한 인수와 기본값

### 강사님 코드

출처: `teacher/workspace_html/javascript/08_function.html` 86–105행 · **원본 발췌**

```javascript
    // 전달인자의 값이 undefined일 때 기본 값 지정
    // 전달 받은 값이 있으면 사용하고 없으면 기본값 사용
    function plus3(x, y=0){
        console.log('x :', x)
        console.log('y :', y)
        if(y == undefined){
            y = 0
        }

        const z = x + y
        return z
    }
    // 전달인자를 적게 줘도 에러 없음
    // 값은 undefined
    a = plus3(2)
    console.log( a )

    // 전달인자를 많이 줘도 에러 없음
    // 받을 만큼만 가져간다
    a = plus3(2, 3, 4)
```

### 내 코드

출처: `me/workspace_html/javascript/08_function.html` 107–129행 · **원본 발췌**

```javascript
            // 전달인자의 값이 undefined 일 때 기본 값 지정
            // 전달 받은 값이 있으면 사용하고, 없으면 기본 값 사용
            function plus3(x, y=0) {
                console.log('x : ', x)
                console.log('y : ', y)
                // if(y == undefined) y = 0
                if(y == undefined) {
                    y = 0
                }

                const z = x + y
                return z;
            }

            // 전달인자를 적게 줘도 에러는 나지 않음
            // 기본값을 지정해주지 않으면 undefined로 나옴
            a = plus3(2)
            console.log(a)

            // 인수가 2개가 들어가야 하는데, 3개를 주면 3번째 인수는 무시함
            // 받을 만큼만 가져감 (아래에서 4는 없어지는 값)
            a = plus3(2, 3, 4)
            console.log(a)
```

같은 동작이며 내 코드는 인수 셋을 준 결과도 출력한다. y=0은 y가 undefined일 때 적용되는 기본값이다. plus3(2)는 2, plus3(2,3,4)는 이 함수 본문이 x·y만 사용하므로 5다. 추가 인수가 언어 차원에서 반드시 ‘사라진다’는 뜻은 아니다. 이 본문에서 사용하지 않는다고 설명한다. [MDN 기본 매개변수](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters)

원본 안의 `if(y == undefined)`는 기본 매개변수와 완전히 같은 판정이 아니다. ==는 null도 undefined와 같게 본다. 따라서 plus3(2,null)의 경우 기본 매개변수는 null을 유지하지만 본문의 if가 y를 0으로 바꾼다. ‘기본값이 null까지 처리했다’고 설명하지 않는다. 원본 plus2도 같은 느슨한 비교를 사용한다.

‘인수가 부족해도 호출할 수 있음’은 어떤 함수든 오류 없이 처리한다는 보장이 아니다. 이 예제에서는 없는 값이 undefined이고 기본값·조건문이 보완한다. 값의 메서드를 바로 호출하는 다른 함수에서는 오류가 날 수 있다.

<a id="section-5"></a>

## 5. 짧은 복습

1. 값을 console.log만 하는 함수의 반환값은?
2. `plus(2, plus(5,6))`에서 바깥 plus가 받는 두 값은?
3. 기본 매개변수 y=0 자체가 null도 0으로 바꾸는가?

<details>
<summary>정답 확인</summary>

1. 명시적인 반환이 없다면 undefined다.
2. 2와 11이다.
3. 아니다. 원본에서는 별도 if가 null을 0으로 바꾼다.

</details>

<a id="section-6"></a>

## 추가로 알면 좋은 것

인수 전체를 처리하는 고급 패턴, 함수 내부 동작·호이스팅의 상세 모델, 별도 유틸리티 설계는 추가 학습이다. 본문은 원본에 있는 범위와 기본 매개변수까지 다룬다.

