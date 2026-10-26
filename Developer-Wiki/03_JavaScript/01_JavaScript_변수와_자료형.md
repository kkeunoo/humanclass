# 01. 변수와 자료형 — 이름에 값을 담고 계산하기

[JavaScript 목차](README.md) · [다음: 연산자](02_JavaScript_연산자.md)

이 장에서는 값을 저장하고 바꾸는 방법, 문자열과 숫자를 구분하는 방법을 익힌다. 원본 `01_var.html`은 `<script>` 안에서 실행하므로 화면 본문보다 개발자 도구의 Console에서 결과를 확인한다. 주석 처리한 줄은 실행되지 않는다.

<!-- chapter-toc -->

- [1. 선언·대입·출력을 구분하기](#section-1)
- [2. 값이 없거나 계산이 안 될 때](#section-2)
- [3. 문자열을 숫자로 바꾸기](#section-3)
- [4. 입력·문자열 출력·수업 계산](#section-4)
- [5. 짧은 복습](#section-5)
- [추가로 알면 좋은 것](#section-6)

<a id="section-1"></a>

## 1. 선언·대입·출력을 구분하기

`let d = 60`은 이름 d를 선언하면서 값 60을 넣는다. `d = 65`는 이미 있는 변수에 새 값을 대입한다. `console.log(d)`는 그 순간의 값을 출력한다. `=`는 같다는 질문이 아니라 오른쪽 값을 왼쪽에 저장하는 연산자다.

| 선언 | 같은 범위에서 같은 이름 재선언 | 다른 값으로 재대입 |
| --- | --- | --- |
| var | 가능 | 가능 |
| let | 불가 | 가능 |
| const | 불가 | 불가 |

여기서 범위는 이름을 사용할 수 있는 영역이다. let·const는 중괄호 블록을 기준으로 범위가 생긴다. var는 함수 범위를 가지므로 이후 반복문·함수에서 차이를 다시 관찰한다. const의 재대입 금지는 객체 내부까지 모두 고정한다는 의미가 아니다. 객체 내용 변경은 객체를 다루는 장에서 연결한다.

### 강사님 코드

출처: `teacher/workspace_html/javascript/01_var.html` 43–59행 · **원본 발췌**

```javascript
        // 선언 방법 3
        let d = 60
        console.log('d : '+ d);

        // 같은 변수 명으로 다시 선언하는 것을 막아준다
        // let d = 70
        d = 65
        console.log('d : '+ d);

        // 선언 방법 4
        const e = 70
        console.log('e : '+ e)
        // const e = 80
        // e = 75

        d = '문자'
        console.log('d : '+ d);
```

d는 60 → 65 → '문자'로 바뀐다. JavaScript 변수에 숫자형이라는 고정 선언을 붙인 것이 아니므로 다른 자료형의 값을 대입할 수 있다. 주석 속 `let d = 70`을 같은 범위에서 실행하면 재선언 오류가 난다.

### 내 코드

출처: `me/workspace_html/javascript/01_var.html` 43–59행 · **원본 발췌**

```javascript
        // 선언 방법 3
        let d = 60
        console.log('d : '+ d);

        // 같은 변수 명으로 다시 선언하는 것을 막아준다
        // let d = 70
        d = 65
        console.log('d : '+ d);

        // 선언 방법 4
        const e = 70
        console.log('e : '+ e)
        // const e = 80
        // e = 75

        d = '문자'
        console.log('d : '+ d);
```

이 부분은 양쪽이 같다. 강사님 방식으로 바꿀 필요가 없다. 실행되는 줄과 주석 처리한 오류 실험을 구분하며 읽으면 된다.

### 원본 주석에서 바로잡을 것

양쪽 38–41행의 `c = 50`에는 ‘타입 없음’이라고 적혀 있다. 이는 **선언 키워드를 쓰지 않은 대입**이다. 값 50의 자료형은 number다. 원본 같은 일반 스크립트에서는 의도치 않은 전역 이름을 만들 수 있으므로 새로 작성할 때는 `let c = 50`처럼 선언한다. 또한 앞의 `a = 15`는 뒤에 같은 스크립트의 `var a`가 있다는 점에서 c와 상황이 다르다. 먼저 선언하고 사용하는 순서로 연습하면 혼동이 줄어든다.

<a id="section-2"></a>

## 2. 값이 없거나 계산이 안 될 때

| 원본에서 보는 표현 | 결과·의미 |
| --- | --- |
| let y; 이후 y 출력 | undefined: 선언했지만 아직 값을 넣지 않음 |
| 선언하지 않은 z 출력 | ReferenceError: 찾을 수 없는 이름 |
| 7 / 0 | Infinity |
| 7 * '문자' | NaN: 숫자 계산 결과를 만들 수 없음 |
| true / false | 참 / 거짓 값. 문자열 'true'와 구별 |

`typeof`는 값의 자료형을 문자열로 알려 준다. `typeof 3`은 'number', `typeof '3'`은 'string'이다. 비교 원본은 다음 연산자 장에 있다. `console.error`는 오류처럼 보이는 메시지를 출력하지만, 그 호출 자체가 예외를 던져 실행을 중단하는 것은 아니다.

<a id="section-3"></a>

## 3. 문자열을 숫자로 바꾸기

### 강사님 코드

출처: `teacher/workspace_html/javascript/01_var.html` 96–108행 · **원본 발췌**

```javascript
        let strA = "10.1"
        let strB = "10개"
        console.log( strA + 2 ) // "10.12"
        let numA = Number(strA) + 2
        console.log(numA)
        console.log( Number(strB) )

        numA = parseInt( strA )
        console.log('numA :', numA)
        console.log( parseInt(strB) )

        console.log( String(numA) )
        console.log( ''+numA )
```

### 내 코드

출처: `me/workspace_html/javascript/01_var.html` 96–108행 · **원본 발췌**

```javascript
        let strA = "10.1"
        let strB = "10개"
        console.log( strA + 2 ) // "10.12"
        let numA = Number(strA) + 2
        console.log(numA)
        console.log( Number(strB) )

        numA = parseInt( strA )
        console.log('numA :', numA)
        console.log( parseInt(strB) )

        console.log( String(numA) )
        console.log( ''+numA )
```

동일한 예제다. 핵심은 따옴표로 감싼 값은 숫자 모양이어도 문자열이라는 점이다.

| 표현 | 결과 | 읽는 순서 |
| --- | --- | --- |
| strA + 2 | '10.12' | 문자열에 2를 이어 붙임 |
| Number(strA) + 2 | 12.1 | 문자열 전체를 숫자로 바꾼 뒤 더함 |
| Number(strB) | NaN | '10개' 전체는 숫자로 바꿀 수 없음 |
| parseInt(strA) | 10 | 앞에서부터 정수로 읽을 수 있는 부분 해석 |
| parseInt(strB) | 10 | 숫자 뒤의 '개'부터 읽지 않음 |
| String(numA) | '10' | 앞에서 numA를 10으로 바꾼 뒤 문자열 변환 |

parseInt는 입력 전체가 올바른 숫자인지 검사하는 함수가 아니다. 숫자 값을 소수점 버림 도구처럼 쓰는 원본 계산은 작은 양수 예제에서는 맞지만, 모든 크기의 수에 일반화하지 않는다. 자세한 동작은 [MDN parseInt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt)를 참고한다.

<a id="section-4"></a>

## 4. 입력·문자열 출력·수업 계산

`alert`는 안내 창, `confirm`은 확인/취소에 따라 true/false, `prompt`는 입력 문자열 또는 취소 시 null을 돌려준다. 원본에서 이 호출 상당수는 주석 처리되어 있다. prompt로 받은 '10'을 더할 때는 숫자 변환 여부를 먼저 판단한다. Number(null)과 Number('')는 모두 0이므로 취소·빈 입력을 구분하려면 변환 전 값을 확인해야 한다.

문자열은 `+`로 연결하거나 백틱 안의 `${값}`으로 넣을 수 있다. 원본 평 환산은 1평을 3.3㎡로 둔 수업용 근사 계산이다. 10평이면 33㎡, 82㎡를 평으로 바꾸려면 82를 3.3으로 나눈다. 원본의 ‘밭’이라는 변수만으로 입력 단위가 정해지는 것은 아니므로 계산식과 단위를 함께 읽는다.

### 강사님 회식비 문제

출처: `teacher/workspace_html/javascript/01_var.html` 134–139행 · **원본 발췌**

```javascript
        /*
            9명이 회식을 했고 비용이 100000만원이 나왔다
            인당?
        */
        console.log("인당 : " )
        console.log("주최자가 조금 더 낼 때 얼마?")
```

문제와 출력 제목만 있고 실제 계산은 비어 있다. 주석의 ‘100000만원’은 내 풀이의 조건인 100,000원과 구분해야 한다. 아래에서는 **총액 100,000원**을 기준으로 비교한다.

### 내 풀이

출처: `me/workspace_html/javascript/01_var.html` 135–142행 · **원본 발췌**

```javascript
        // `
        // 9명이 회식을 했고 비용이 100,000원이 나왔다
        // `
        
        console.log( '나머지 : ', 100000 % 9 )
        console.log( '인당 : ', parseInt(100000 / 9) )

        console.log( '주최자 : ', parseInt(100000 / 9) + (100000 % 9) )
```

9명 중 8명은 11,111원씩, 주최자는 11,112원을 내면 합계 100,000원이 된다. 몫과 나머지를 실제 답까지 연결한 점이 좋다. `parseInt(100000 / 9)`가 각자의 기본 부담이고 `% 9`의 결과 1원이 주최자에게 더해진다. 여기서는 강사님 파일의 빈 계산보다 내 풀이가 더 완성되어 있다.

원본 잔고 예제는 `잔고 = 잔고 + 번돈`과 `잔고 += 번돈`을 둘 다 실행한다. 두 줄은 같은 방식의 대입을 보여 주지만, 함께 실행하면 한 번이 아니라 **두 번 입금**되어 215,000원이 된다.

<a id="section-5"></a>

## 5. 짧은 복습

1. let으로 만든 숫자 변수에 문자열을 넣을 수 있는가?
2. '10' + 2와 Number('10') + 2는 어떻게 다른가?
3. 100,000원을 9명이 나누고 주최자가 나머지를 부담할 때 합계가 맞는지 계산하라.

<details>
<summary>정답 확인</summary>

1. 가능하다. const는 자료형 때문이 아니라 재대입 자체가 금지된다.
2. 문자열 '102'와 숫자 12다.
3. 11,111 × 8 + 11,112 = 100,000이다.

</details>

<a id="section-6"></a>

## 추가로 알면 좋은 것

strict mode 상세, 호이스팅·초기화 전 접근의 내부 원리, Number.isNaN·Number.isInteger를 사용하는 별도 검증 체계는 이 장의 필수 학습에서 분리한다. 선언 규칙을 더 확인하려면 [MDN let](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)을 참고한다.

