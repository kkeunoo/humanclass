# 08-02. 함수 참조와 콜백 — 괄호 하나가 바꾸는 것

[JavaScript 목차](README.md) · [이전: 함수](08_JavaScript_함수와_콜백_타이머.md) · [다음: 타이머](08-03_JavaScript_타이머와_취소.md)

<!-- chapter-toc -->

- [1. 함수 자체를 변수에 담기](08-02_JavaScript_함수참조와_콜백.md#section-1)
- [2. test1과 test1() 비교](08-02_JavaScript_함수참조와_콜백.md#section-2)
- [3. console.log 변경 실험 읽기](08-02_JavaScript_함수참조와_콜백.md#section-3)
- [4. 짧은 복습](08-02_JavaScript_함수참조와_콜백.md#section-4)
- [추가로 알면 좋은 것](08-02_JavaScript_함수참조와_콜백.md#section-5)

<a id="section-1"></a>

## 1. 함수 자체를 변수에 담기

원본 `let noName = function() { ... }`은 함수 값을 변수에 담는 함수 표현식이다. `let noName2 = noName`은 같은 함수를 다른 이름으로 가리킨다. 본문을 복사해서 새 함수를 정의한 것이 아니다. 원본처럼 할당 이후에 호출하면 동작하지만, 함수 선언문과 모든 면에서 동일한 문법이라고 설명하지 않는다.

### 강사님 코드

출처: `teacher/workspace_html/javascript/08_function.html` 120–127행 · **원본 발췌**

```javascript
    function test( fn ){
        console.log('test 실행중')
        console.log(typeof fn)
        if (typeof fn == 'function'){
            fn()
        }
    }
    test( noName )
```

### 내 코드

출처: `me/workspace_html/javascript/08_function.html` 144–152행 · **원본 발췌**

```javascript
            // fn이 noName 함수를 인자로 받았는데, 이럴 때 fn을 '콜백함수'라고 부른다.
            function test( fn ) {
                console.log('test 실행중')
                console.log(typeof fn)
                if (typeof fn == 'function') {
                    fn()
                }
            }
            test( noName )
```

같은 구조다. noName을 fn으로 받아 함수인지 확인한 뒤 fn()으로 실행한다. 다른 함수에 전달해 실행을 맡긴 함수를 콜백이라고 한다. **콜백이 반드시 나중에 비동기로 실행되는 것은 아니다.** 여기서는 test가 호출되는 동안 즉시 fn을 실행한다.

<a id="section-2"></a>

## 2. test1과 test1() 비교

### 강사님 코드

출처: `teacher/workspace_html/javascript/08_function.html` 161–180행 · **원본 발췌**

```javascript
    function test1(){
        console.log('test1')
        return 3
    }

    function test2( a ){
        console.log('test2')
        console.log(a)
    }

    test2( test1() )
    // 즉
    x = test1()
    test2(x)


    test2( test1 )
    // 즉
    x = test1
    test2(x)
```

### 내 코드

출처: `me/workspace_html/javascript/08_function.html` 191–204행 · **원본 발췌**

```javascript
            function test1() {
                console.log('test1')
                return 3
            }
            function test2( a ) {
                console.log('test2')
                console.log(a)
            }

            // ()가 있으면 실행의 결과물을 주는것이고, 괄호가 없으면 함수의 내용 자체가 들어감
            test2( test1() )
            // 즉 x = test1()_실행 > test2(x) 가 된 것
            test2 ( test1 )
            // x = test1 함수 내용만 넣기 > text2(x)
```

| 호출 | test2에 전달하는 값 | test1 본문 실행 |
| --- | --- | --- |
| test2(test1()) | test1이 반환한 숫자 3 | 먼저 실행 |
| test2(test1) | 함수 자체 | 이 전달만으로 실행되지 않음 |

이 test2는 받은 값을 출력할 뿐 a()로 호출하지 않는다. 따라서 함수 전달 예제이며, 실제 콜백 호출은 위 test의 fn()에서 확인한다. 강사님은 중간 변수 x로 같은 흐름을 다시 실행하므로 파일 전체를 열면 설명용 중복 출력이 생긴다. 내 코드는 그 재실행을 주석으로 설명하여 출력이 덜 반복된다.

<a id="section-3"></a>

## 3. console.log 변경 실험 읽기

양쪽 파일은 원래 console.log를 c1에 저장한 뒤 console.log=3으로 덮고, 다시 함수를 넣는다. 이는 함수도 값이고 객체 속성도 바꿀 수 있다는 실험이다. console.log가 숫자 3인 순간 호출하면 함수가 아니므로 오류가 난다. 해당 호출 줄은 원본에서 주석 처리되어 있다.

새 console.log 안에서 다시 console.log를 호출하면 같은 새 함수를 반복 호출한다. 원본은 c1을 호출하여 이 문제를 피한다. 출력되는 ‘해킹된거임’은 실습 문자열이며 실제 침입을 증명하는 메시지가 아니다. 파일 뒤쪽의 출력에는 이 문구가 추가되므로 함수 반환 문제와 출력 변경을 구분한다. 독립 복습을 위해 원래 상태로 돌리려면 `console.log = c1`을 실행할 수 있다. 이 복구 줄은 설명용 수정이다.

또한 원본 desc(arr)의 sort().reverse()는 원본 배열을 바꾸며 일반 숫자 내림차순을 보장하지 않는다. [배열 정렬 설명](06_JavaScript_배열과_배열메서드.md)과 연결한다. 같은 경고와 정렬 함수를 여러 장에 반복 정의하지 않는다.

<a id="section-4"></a>

## 4. 짧은 복습

1. 함수를 나중에 호출하도록 전달하려면 fn과 fn() 중 무엇을 전달하는가?
2. 콜백은 반드시 비동기인가?

<details>
<summary>정답 확인</summary>

1. fn이다. fn()은 지금 호출한 결과를 전달한다.
2. 아니다. 원본 test는 콜백을 즉시 호출한다.

</details>

<a id="section-5"></a>

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/08-02_JavaScript_함수참조와_콜백_연습문제.md)

## 추가로 알면 좋은 것

this·바인딩·고급 함수 조합·범용 래퍼 설계는 별도 확장이다. 여기서는 원본 함수 참조와 호출 순서에 집중한다.

