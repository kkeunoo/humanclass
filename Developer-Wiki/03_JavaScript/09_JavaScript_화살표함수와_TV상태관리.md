# 09. 화살표 함수 — 짧게 쓸 때도 반환값 확인하기

[JavaScript 목차](README.md) · [이전: 타이머](08-03_JavaScript_타이머와_취소.md) · [다음: TV 실습](09-02_JavaScript_TV상태관리.md)

기준은 양쪽 `09_arrow.html`이다. 원래 같은 장에 있던 TV 예제는 별도 실습으로 나누었다. TV 원본은 일반 function을 사용하며, 화살표 함수로 전면 재작성한 프로젝트로 바꾸지 않는다.

<!-- chapter-toc -->

- [1. 기본형과 짧은 표현](09_JavaScript_화살표함수와_TV상태관리.md#section-1)
- [2. return a, b는 두 값 반환이 아니다](09_JavaScript_화살표함수와_TV상태관리.md#section-2)
- [3. 원본을 통째로 실행하면 중단되는 이유](09_JavaScript_화살표함수와_TV상태관리.md#section-3)
- [4. 짧은 복습](09_JavaScript_화살표함수와_TV상태관리.md#section-4)
- [추가로 알면 좋은 것](09_JavaScript_화살표함수와_TV상태관리.md#section-5)

<a id="section-1"></a>

## 1. 기본형과 짧은 표현

### 강사님 코드

출처: `teacher/workspace_html/javascript/09_arrow.html` 42–50행 · **원본 발췌**

```javascript
    const fn5 = (a, b)=>{
        return a + b
    }
    // 실행문 안에 return만 있는 경우
    // {}, return 을 생략 할 수 있다
    // {}를 생략한 경우 return도 생략해야 한다
    const fn6 = (a, b) => a + b

    const fn7 = a => a + 100
```

### 내 코드

출처: `me/workspace_html/javascript/09_arrow.html` 45–51행 · **원본 발췌**

```javascript
            const fn5 = (a, b) => {
                return a + b
            }
            // 실행문 안에 return만 있는 경우 실행 블럭의 {}중괄호, return 생략 가능
            // {}를 생략한 경우 return도 반드시 생략해야 함
            const fn6 = (a, b) => a + b
            const fn7 = a => a + 100
```

같은 실험이다. fn5와 fn6를 (2,3)으로 호출하면 5, fn7을 (2)로 호출하면 102다. 이 발췌에는 선언만 있으며 결과를 보기 위해서는 호출이 필요하다.

| 형식 | 의미 |
| --- | --- |
| (a,b) => { return a+b; } | 블록 안의 return으로 반환 |
| (a,b) => a+b | 식 결과를 곧바로 반환 |
| a => a+100 | 단순 매개변수 하나이므로 매개변수 괄호 생략 |
| () => { ... } | 매개변수가 없어도 괄호 필요 |

중괄호를 쓰면서 return을 빼면 그 안에서 계산한 값이 자동 반환되지 않는다. 본문이 식 하나일 때만 중괄호·return을 함께 생략하는 형태로 이해한다. 일반 function과 this 등의 동작이 모두 같은 것은 아니며 그 상세는 추가 학습으로 둔다. [MDN 화살표 함수](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)

<a id="section-2"></a>

## 2. return a, b는 두 값 반환이 아니다

양쪽 fn1·fn2는 `return a, b`를 사용한다. 이는 쉼표 연산자로 마지막 값 b 하나를 반환한다. fn1(1,2)의 결과는 2다. console.log(a,b)가 두 값을 출력하는 것과 반환을 구분한다. 여러 값을 한 결과로 돌려주려면 이미 배운 배열을 사용하여 `return [a,b]`처럼 쓸 수 있지만, 이는 **원본을 바꾼 설명 예제**다. [MDN 쉼표 연산자](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comma_operator)

내 주석의 ‘return은 1번만 써야 한다’도 교정한다. 조건별로 return 문을 여러 곳에 쓸 수 있다. 다만 한 호출은 실행 중 return을 만나면 끝나므로 그 뒤의 같은 경로는 실행하지 않는다.

<a id="section-3"></a>

## 3. 원본을 통째로 실행하면 중단되는 이유

### 강사님 코드

출처: `teacher/workspace_html/javascript/09_arrow.html` 12–21행 · **원본 발췌**

```javascript
    const fn1 = function(a, b){
        console.log(a, b)
        return a, b
    }
    fn1(1, 2)

    (function(a, b){
        console.log(a, b)
        return a, b
    })(1,2)
```

### 내 코드

출처: `me/workspace_html/javascript/09_arrow.html` 12–24행 · **원본 발췌**

```javascript
            const fn1 = function(a, b) {
                console.log(a, b)
                return a, b
                // return은 1번만 써야 한다
                // return a, b
            }
            fn1(1, 2)
            
            // 아래와 같은 형태로 변수 선언 없이 실행하게도 할 수 있음
            (function(a, b) {
                console.log(a, b)
                return a, b
            })(1, 2) // ()는 실행의 괄호이기 때문에 앞에 있는 것 실행
```

두 파일 모두 fn1(1,2) 다음 문장이 괄호로 시작한다. 앞 호출 뒤 세미콜론이 없어 줄바꿈만으로 문장이 끝나지 않고, 반환값 2를 다시 함수처럼 호출하려 한다. 따라서 TypeError로 중단되어 뒤의 화살표 선언까지 정상적으로 진행하지 못한다. **fn1(1,2);처럼 세미콜론을 붙여 경계를 명시하면 교정된다.** 수정 파일의 성공 결과와 원본 실패를 구분한다.

원본의 fn4는 매개변수가 없으면서 a를 읽는다. 이 파일에 외부 a가 없어, 앞 오류를 고친 뒤 fn4를 호출하면 ReferenceError가 난다. fn4도 원본에서는 선언만 되어 있다. 인수 없는 함수를 설명하려면 외부 변수 없이 고정 문구를 출력하도록 바꾸거나 매개변수 a를 받아야 한다.

<a id="section-4"></a>

## 4. 짧은 복습

1. `(a,b) => { a+b; }`를 (2,3)으로 호출하면?
2. 원본 fn1(1,2)가 반환하는 값은?
3. 앞 호출과 괄호 시작 문장을 분리하려면?

<details>
<summary>정답 확인</summary>

1. return이 없어 undefined다.
2. 2다.
3. 앞 호출 끝에 세미콜론을 명시한다.

</details>

<a id="section-5"></a>

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/09_JavaScript_화살표함수와_TV상태관리_연습문제.md)

## 추가로 알면 좋은 것

this·arguments·생성자와 화살표 함수의 상세 차이, 고급 즉시 실행 패턴은 확장이다. 본문은 원본에 이미 있는 반환·호출·문장 경계의 오류를 이해하는 범위다.

