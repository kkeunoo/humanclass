# 14. 동기·비동기 — setTimeout 0도 현재 실행 다음이다

[JavaScript 목차](README.md) · [이전: 폼 입력](13_JavaScript_DOM_폼요소와_입력값처리.md)

양쪽 `14_async.html`을 기준으로 **함수 호출 순서와 타이머 콜백 실행 순서**를 읽는다. 함수 선언·호출은 [08 함수](08_JavaScript_함수와_콜백_타이머.md), 등록·취소는 [08-03 타이머](08-03_JavaScript_타이머와_취소.md)에 설명했으므로 여기서는 출력 순서에 집중한다.

**동기와 비동기란?** 여기서는 지금 호출한 함수의 일을 마치며 진행하는 흐름과, 타이머에 나중 실행할 함수를 등록해 두고 다음 문장으로 진행하는 흐름을 구분한다. 아래는 원본 발췌가 아닌 **설명용 작은 예제**다.

```javascript
console.log('A');
setTimeout(function () { console.log('B'); }, 0);
console.log('C');
// 출력 순서: A → C → B
```

`0`을 지정해도 B를 출력하는 함수가 이 줄에서 바로 호출되지는 않는다. 원본의 중첩 함수와 두 타이머에서도 같은 원리를 확인한다.

<!-- chapter-toc -->

- [1. 중첩 호출은 순서대로 실행한다](14_JavaScript_동기비동기와_이벤트루프.md#section-1)
- [2. 양쪽 원본의 실제 출력 순서](14_JavaScript_동기비동기와_이벤트루프.md#section-2)
- [3. 이벤트 루프는 이 정도 흐름부터](14_JavaScript_동기비동기와_이벤트루프.md#section-3)
- [4. 이전 실험과 비교하기](14_JavaScript_동기비동기와_이벤트루프.md#section-4)
- [5. 복습](14_JavaScript_동기비동기와_이벤트루프.md#section-5)
- [추가로 알면 좋은 것](14_JavaScript_동기비동기와_이벤트루프.md#section-6)

<a id="section-1"></a>

## 1. 중첩 호출은 순서대로 실행한다

fn1을 호출하면 fn1의 출력 후 fn2를 호출한다. fn2는 자신의 출력을 하고 fn3를 두 번 호출한다. fn3가 끝나면 호출한 위치로 돌아와 다음 문장을 실행한다. ‘한 번에 같이 실행’은 동시에 여러 함수가 실행된다는 뜻으로 읽으면 안 된다.

### 강사님 코드

출처: `teacher/workspace_html/javascript/14_async.html` 8–33행 · **원본 발췌**

```javascript
        function fn1(){
            console.log('fn1 실행')

            fn2()
        }
        function fn2(){
            console.log('fn2 실행')
            
            fn3()
            fn3()

            console.log('1')
            setTimeout( function(){
                console.log('2')
            }, 0)
            // console.log('3')
            setTimeout( function(){
                console.log('3')
            }, 0)
            console.log('마지막')
        }
        function fn3(){
            console.log('fn3 실행')
        }

        fn1()
```

### 내 코드

출처: `me/workspace_html/javascript/14_async.html` 11–46행 · **원본 발췌**

```javascript
            function fn1() {
                console.log('fn1 실행')

                fn2()
            }
            function fn2() {
                console.log('fn2 실행')

                fn3()
                fn3()

                console.log('1')
                // 3이 먼저 나오는 이유는 setTimeout은 '0초 이후' 라는 개념이기 때문에,
                // 1-3-2 순서로 출력되게 됨 (이 모습이 동기화가 안 되어있는 것)
                // setTimeout( function() {
                //     console.log('2')
                // }, 0)
                // console.log('3')

                // 아래와 같이 주었을 때는 같은 setTimeout이기 때문에,
                // '마지막'이 먼저 나오고 2, 3 순으로 나오게 됨
                // 이러한 것 때문에 지연함수라고 부르며, 두 번째 인자값을 주는 것
                // 같은 setTimeout 0 이라면 두개는 동기화가 된 것
                setTimeout( function() {
                    console.log('2')
                }, 0)
                setTimeout( function() {
                    console.log('3')
                }, 0)
                console.log('마지막')
            }
            function fn3() {
                console.log('fn3 실행')
            }

            fn1()
```

실제로 활성화된 문장은 양쪽이 같은 흐름이다. 내 주석에는 이전 실험인 1→3→2 설명도 있지만 그 부분의 코드 두 줄은 주석 처리되어 있다. **현재 활성 코드와 이전 실험의 주석을 구분**해야 한다.

<a id="section-2"></a>

## 2. 양쪽 원본의 실제 출력 순서

```text
fn1 실행
fn2 실행
fn3 실행
fn3 실행
1
마지막
2
3
```

| 단계 | 실행하는 일 | 바로 출력되는가 |
| --- | --- | --- |
| fn1 → fn2 → fn3 두 번 | 일반 함수 호출 | 순서대로 출력 |
| console.log('1') | 일반 문장 | 출력 |
| 첫 setTimeout | '2'를 출력할 콜백 등록 | 아직 '2'는 출력하지 않음 |
| 두 번째 setTimeout | '3'을 출력할 콜백 등록 | 아직 '3'은 출력하지 않음 |
| console.log('마지막') | 현재 함수의 다음 문장 | 출력 |
| 현재 호출 흐름이 끝난 뒤 | 타이머 콜백 실행 | '2', '3' 순서 |

0은 콜백을 현재 줄에서 즉시 실행하라는 뜻이 아니다. 등록한 콜백은 현재 실행 중인 JavaScript가 끝나고 실행 가능한 차례가 와야 실행된다. 이 예제에서는 같은 지연으로 차례로 등록한 타이머가 2→3 순서로 실행된다. 그렇다고 두 콜백이 동기 함수 호출로 바뀌거나 동시에 실행되는 것은 아니다. 내 ‘같은 setTimeout 0이면 동기화’ 주석은 이 설명으로 고쳐 읽는다.

<a id="section-3"></a>

## 3. 이벤트 루프는 이 정도 흐름부터

```text
현재 함수 호출과 문장 실행
    ↓ 끝남
실행할 차례가 된 콜백 실행
    ↓ 끝남
다음 콜백 실행
```

여기서 동기는 호출한 함수의 실행을 마친 뒤 다음 문장으로 진행하는 흐름이다. 타이머에서는 콜백을 등록하고 다음 문장으로 먼저 진행한다. 이벤트 루프는 이런 실행 차례를 이어 주는 구조로 우선 이해한다. 0ms라도 정확한 시각이나 즉시 실행을 보장하지 않는다. [MDN setTimeout](https://developer.mozilla.org/en-US/docs/Web/API/Window/setTimeout)

<a id="section-4"></a>

## 4. 이전 실험과 비교하기

**원본 주석 속 실험을 분리한 재구성 예제 — 전체 원본의 현재 실행과 다름**

```javascript
console.log('1')
setTimeout(function () {
    console.log('2')
}, 0)
console.log('3')
```

이 예제만 따로 실행하면 1→3→2다. 3을 일반 문장으로 출력했기 때문이다. 원본의 활성 코드는 3도 타이머 콜백 안에 있으므로 앞 절의 전체 출력과 구별한다.

<a id="section-5"></a>

## 5. 복습

1. 원본에서 '마지막'이 '2'보다 먼저 출력되는 이유는?
2. 지연값 0은 콜백의 즉시 실행을 뜻하는가?
3. 두 타이머가 2→3으로 출력되면 동기 호출이 된 것인가?
4. 위 재구성 예제에서 3을 두 번째 타이머 콜백에 넣으면?

<details>
<summary>정답</summary>

1. '마지막'은 현재 실행 흐름의 일반 문장이고 '2'는 나중에 실행할 콜백에 있기 때문이다.
2. 아니다. 현재 실행과 콜백의 차례를 기다린다.
3. 아니다. 순서가 관찰된다는 것과 동기 호출인 것은 다르다.
4. 이 짧은 예제에서는 1→2→3이다. 전체 원본과 달리 '마지막' 출력문이 없다는 것도 확인한다.

</details>

<a id="section-6"></a>

## 추가로 알면 좋은 것

microtask, queueMicrotask, 엔진의 큐 구조 상세는 추가 학습으로 분리한다. Promise·then의 실제 수업 사용은 이후 AJAX 장에서 해당 원본과 함께 다룬다. 지금 기본 문제에 새 Promise 예제를 넣어 학습 범위를 늘리지 않는다.

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/14_JavaScript_동기비동기와_이벤트루프_연습문제.md) → [다음: DOM 이벤트](15_JavaScript_DOM이벤트와_키보드스크롤제어.md)

