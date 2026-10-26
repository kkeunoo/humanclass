# 02. 연산자 — 식의 결과와 변수의 변화를 나누어 읽기

[JavaScript 목차](README.md) · [이전: 변수와 자료형](01_JavaScript_변수와_자료형.md)

이 장의 기준은 양쪽 `02_op.html`이다. 산술·증감·비교·논리·삼항 연산과 실제 계산 문제를 다룬다. 문자열 변환은 앞 장을 먼저 읽는다.

<!-- chapter-toc -->

- [1. 자주 쓰는 기호](#section-1)
- [2. 전위·후위: 무엇을 식에 전달하는가](#section-2)
- [3. 비교·논리·삼항](#section-3)
- [4. 실제 계산 문제 비교](#section-4)
- [5. 짧은 복습](#section-5)
- [추가로 알면 좋은 것](#section-6)

<a id="section-1"></a>

## 1. 자주 쓰는 기호

| 종류 | 기호 | 원본에서 쓰는 의미 |
| --- | --- | --- |
| 산술 | + - * / % | 더하기·빼기·곱하기·나누기·나머지 |
| 대입 | = += | 값을 저장·기존 값에 더해 저장 |
| 증감 | ++ -- | 변수 값을 1 증가·감소 |
| 비교 | == != === !== | 동등·부등·엄격 동등·엄격 부등 |
| 논리 | && \|\| ! | 둘 다 참·하나라도 참·참거짓 반전 |
| 조건 선택 | 조건 ? 참일 때 : 거짓일 때 | 두 값 중 하나 선택 |

`/`는 정수끼리 계산해도 소수 결과를 낼 수 있다. `%`는 나머지를 구한다. `+`는 문자열이 섞이면 연결이 될 수 있으므로 입력 자료형을 확인한다. 논리 연산 표는 원본의 불리언 값 기준 설명이다. &&·||가 모든 상황에서 반드시 true/false만 반환하는 것은 아니다.

<a id="section-2"></a>

## 2. 전위·후위: 무엇을 식에 전달하는가

### 강사님 코드

출처: `teacher/workspace_html/javascript/02_op.html` 25–43행 · **원본 발췌**

```javascript
        k = 10;
        console.log('k++', k++)
        console.log('k', k)

        k = 10;
        console.log('++k', ++k)
        console.log('k', k)

        k = 10
        let m = k++ + 1;
        // m? 11, k? 11
        k = 10
        m = ++k + k++
        // m?   , k?
        console.log(`m: ${m}, k: ${k}`)

        k = 10
        m = k-- + ++k - --k
        console.log(`m: ${m}, k: ${k}`)
```

### 내 코드

출처: `me/workspace_html/javascript/02_op.html` 25–49행 · **원본 발췌**

```javascript
            //단항(++k_더하기를 먼저 함), 이항(k++_더하기를 뒤에 함)연상자의 차이
            // ex) -5(단항), 7-5(이항)
            k = 10;
            console.log('k++', k++)
            console.log('k', k)

            k = 10;
            console.log('++k', ++k)
            console.log('k', k)

            k = 10;
            let m = k++ + 1;

            //++k에서 k가 11이 된 이후에 값이 뒤로 넘어가기때문에 뒤에 있는 k도 11이 되어있고
            //k가 11인 상태에서 ++하기 떄문에 12가 출력됨
            k = 10;
            m = ++k + k++
            console.log(`m: ${m}, k: ${k}`)
            
            //--나 ++는 계산할 때 우선으로 바로 적용하고, 뒤에++ 또는 --는 계산 후 그 다음값에 적용
            //k가 10에서 뒷--가 되어 9로 넘어간 상태에서 앞++하여 10, 그 다음에 앞--되어 9가 됨
            k = 10;
            m = k-- + ++k - --k
            10 + 10 - 9
            console.log(`m: ${m}, k: ${k}`)
```

내 주석은 계산 과정을 따라가려는 점이 좋다. 다만 25행의 ‘단항/이항 차이’는 **전위/후위 차이**로 바로잡아야 한다. ++k와 k++는 둘 다 피연산자가 하나인 단항 연산자다. 또한 후위도 변수를 즉시 변경한다. 다만 식에 제공하는 값이 변경 전 값이다. 식 전체가 끝날 때까지 변수 변경을 미루는 것으로 이해하면 틀린다. [MDN 증감 연산자](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Increment)

| 시작 k | 표현 | 식에 제공되는 값 | 계산 후 k |
| --- | --- | --- | --- |
| 10 | k++ | 10 | 11 |
| 10 | ++k | 11 | 11 |

`m = ++k + k++`는 k를 10으로 시작한다. 왼쪽 ++k가 k를 11로 만들고 11을 준다. 오른쪽 k++는 11을 주고 k를 12로 만든다. 따라서 **m=22, k=12**다.

`m = k-- + ++k - --k`는 다시 k=10에서 시작한다. 식에 제공되는 값은 차례대로 10, 10, 9다. 따라서 **m=11, k=9**다. 내 코드의 별도 줄 `10 + 10 - 9`는 계산만 하고 저장·출력하지 않는다. 설명 메모로 남기려면 주석으로 쓰는 편이 의도가 분명하다.

이런 복합 증감식은 실행 순서 연습용이다. 실제 계산에서는 한 줄에 변화를 여러 번 섞기보다 대입 단계를 나누면 다시 읽기 쉽다.

<a id="section-3"></a>

## 3. 비교·논리·삼항

### 강사님 코드

출처: `teacher/workspace_html/javascript/02_op.html` 64–76행 · **원본 발췌**

```javascript
        let n = 3
        let o = "3"
        console.log("n == o", n == o)
        console.log( typeof n )
        console.log( typeof o )
        console.log("n === o", n === o)
        console.log("n !== o", n !== o)

        console.log( typeof o == 'string')

        let num = 2
        result = (num % 2) == 0 ? '짝수' : '홀수';
        console.log(result)
```

### 내 코드

출처: `me/workspace_html/javascript/02_op.html` 73–93행 · **원본 발췌**

```javascript
            let n = 3
            let o = "3"
            //javascript 한정으로 숫자와 문자여도 값이 같다고 인식함
            console.log("n == o", n == o)
            console.log("n != o", n != o)
            console.log( typeof n )
            console.log( typeof o )
            //===은 값도 같고 형식도 같은가를 확인 (문자, 숫자 등)
            console.log("n === o", n === o)
            console.log("n !== o", n !== o)

            console.log( typeof o == 'string')

            //삼항 조건 연산자는 ? 앞의 값이 참이면 :왼쪽, 거짓이면 :오른쪽
            let num = 2
            result = (num % 2) == 0 ? '짝수' : '홀수';
            console.log(result) 

            num = 1
            result = (num % 2) == 0 ? '짝수' : '홀수';
            console.log(result) 
```

3과 '3'은 `==`로 비교하면 true, `===`로 비교하면 false다. 이 예제에서 ==는 형 변환을 거쳐 비교한다. ‘숫자와 문자열이면 항상 같음’이라는 뜻은 아니다. typeof 결과는 각각 'number', 'string'이다. 내 코드에는 !=와 홀수 num=1 실험이 추가되어 있어 참·거짓 양쪽 결과를 확인하기 좋다.

`true && false`는 false, `true || false`는 true, `!true`는 false다. 짝수 판정 `(num % 2) == 0`이 참이면 '짝수', 거짓이면 '홀수'를 선택한다. 삼항은 출력 기능이 아니라 **값을 선택하는 식**이다. 선택된 문자열을 result에 저장한 뒤 console.log로 출력한다.

<a id="section-4"></a>

## 4. 실제 계산 문제 비교

### 강사님: 중간값으로 버림 과정 설명

출처: `teacher/workspace_html/javascript/02_op.html` 94–111행 · **원본 발췌**

```javascript
        // 문제3
        // 1234를 10의 자리 이하 버림
        // 결과 : 1200
        let q3_value = 1234
        let q3_1 = q3_value / 100 // 12.34
        let q3_2 = parseInt(q3_1) // 12
        let q3_3 = q3_2 * 100
        let q3_4 = parseInt(q3_value / 100) * 100
        console.log(q3_3)

        // 문제4
        // 두 값 1000, 794가 있을 때
        // 1000 / 794의 결과를 소수점 2자리 까지만 출력
        // 결과 : 1.25
        let q4_val_1 = 1000
        let q4_val_2 = 794
        let q4 = parseInt((q4_val_1 / q4_val_2) * 100) / 100
        console.log(q4)
```

1234 / 100 → 12.34 → parseInt 결과 12 → 다시 100을 곱해 1200이라는 과정을 변수로 나눴다. 처음 배우는 사람이 어디서 값이 달라지는지 확인하기에는 이 방식이 더 읽기 쉽다. q3_4는 같은 과정을 한 식으로 쓴 비교 예다.

### 내 풀이

출처: `me/workspace_html/javascript/02_op.html` 112–123행 · **원본 발췌**

```javascript
            // 문제3
            // 1234를 10의 자리 이하를 버림
            // 결과: 1200
            let q3_value = 1234
            console.log(`결과값 : ${parseInt(q3_value / 100) * 100}`)

            // 문제4
            // 두 값 1000, 794가 있을 때 1000 / 794의 결과를 소수점 2자리 까지만 출력
            // 결과 : 1.25
            let q4_value1 = 1000
            let q4_value2 = 794
            console.log(`결과값 : ${parseInt(q4_value1 / q4_value2 * 100) / 100}`)
```

계산 결과는 같다. 내 코드는 출력 문구와 계산을 한곳에 모아 짧다. 결과가 이상하면 강사님처럼 중간 변수를 두고 나누어 확인하면 좋다. 소수 둘째 자리 예제는 반올림이 아니라 **버림**이다. 1000 / 794에 100을 곱하고 정수 부분을 얻은 뒤 다시 100으로 나누어 1.25를 만든다.

### 강사님: 구매·할인·지폐

출처: `teacher/workspace_html/javascript/02_op.html` 82–92행 · **원본 발췌**

```javascript
        let q1_money = 10000
        let q1_pay = 4800
        console.log( parseInt(q1_money / q1_pay) )
        console.log( q1_money % q1_pay )

        // 문제2
        // 올리브영에 꿀홍차가 8000원입니다
        // 15% 세일!! 그렇다면 가격은?
        let q2_money = 8000
        let q2_per = 15
        console.log(  q2_money - (q2_money * q2_per / 100)  )
```

출처: `teacher/workspace_html/javascript/02_op.html` 118–121행 · **원본 발췌**

```javascript
        let q5_money = 17000
        let q5_5000 = parseInt(q5_money / 5000)
        let q5_money2 = (q5_money % 5000)
        let q5_1000 = parseInt(q5_money2 / 1000)
```

### 내 풀이

출처: `me/workspace_html/javascript/02_op.html` 101–110행 · **원본 발췌**

```javascript
            let q1_money = 10000
            let q1_pay = 4800
            console.log(`구매가능 : ${parseInt(q1_money / q1_pay)}잔, 남는 돈 : ${q1_money % q1_pay}원`)

            // 문제2
            // 올리브영에 꿀홍차가 8,000원 입니다
            // 오늘 15% 세일!! 그렇다면 가격은?
            let q2_honey = 8000
            let q2_percent = 15
            console.log(`세일가 : ${q2_honey - ((q2_honey / 100) * q2_percent)}원`)
```

출처: `me/workspace_html/javascript/02_op.html` 128–131행 · **원본 발췌**

```javascript
            let q5_pay = 17000
            let q5_money1 = 5000
            let q5_money2 = 1000
            console.log(`5천원 : ${parseInt((q5_pay / q5_money1))}장 , 1천원 : ${(q5_pay % q5_money1) / q5_money2}장`)
```

| 문제 | 결과 | 비교 |
| --- | --- | --- |
| 10,000원으로 4,800원 음료 | 2잔, 400원 남음 | 같은 계산. 내 코드는 잔·원 표시가 있어 읽기 쉬움 |
| 8,000원에서 15% 할인 | 6,800원 | 할인액 1,200원을 빼는 같은 계산 |
| 17,000원을 5천원부터 지급 | 5천원 3장, 천원 2장 | 강사님은 중간값 저장, 내 코드는 권종 변수와 실제 출력 포함 |

천원 단위가 아닌 금액으로 문제를 바꾸면 내 마지막 식이 소수 장수를 낼 수 있다. 예를 들어 17,500원이면 남은 2,500 / 1,000 = 2.5다. 원래 17,000원 조건의 정답과 다른 입력의 한계를 구분하자. 일반화하려면 천원 몫과 최종 나머지도 따로 계산한다.

<a id="section-5"></a>

## 5. 짧은 복습

1. k=10에서 m=k++ + 1을 실행하면 m과 k는?
2. num=7일 때 원본 삼항식의 결과는?
3. 17,500원을 5천원·천원 지폐로 최대한 주면 각 몇 장이고 얼마가 남는가?

<details>
<summary>정답 확인</summary>

1. m=11, k=11이다.
2. '홀수'다.
3. 5천원 3장, 천원 2장, 500원이 남는다. 원본 문제 조건을 바꾼 복습이다.

</details>

<a id="section-6"></a>

## 추가로 알면 좋은 것

nullish coalescing(??), Number.isInteger를 활용한 새 할인 앱, 일반적인 금액 처리 체계는 원본 범위를 넘어서는 확장이다. 기본 문제에는 요구하지 않는다. parseInt의 일반적 한계는 [변환 설명](01_JavaScript_변수와_자료형.md)을 참고한다.

