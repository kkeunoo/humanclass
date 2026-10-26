# 08-03. 타이머와 취소 — 함수 실행을 예약하기

[JavaScript 목차](README.md) · [이전: 콜백](08-02_JavaScript_함수참조와_콜백.md)

기준은 양쪽 `08_function.html`의 타이머 부분이다. 지연값의 단위는 밀리초이며 1000ms=1초다. 이 장의 반환 식별자 설명은 **브라우저 환경** 기준이다.

<!-- chapter-toc -->

- [1. 한 번 예약하고 취소하기](08-03_JavaScript_타이머와_취소.md#section-1)
- [2. 반복 예약과 종료](08-03_JavaScript_타이머와_취소.md#section-2)
- [3. 양쪽 재귀 예제의 오류](08-03_JavaScript_타이머와_취소.md#section-3)
- [4. 짧은 복습](08-03_JavaScript_타이머와_취소.md#section-4)
- [추가로 알면 좋은 것](08-03_JavaScript_타이머와_취소.md#section-5)

<a id="section-1"></a>

## 1. 한 번 예약하고 취소하기

setTimeout(함수, 지연값)은 함수를 한 번 실행하도록 예약한다. 지연값은 정확한 실행 시각을 보장하지 않는다. 현재 실행 중인 코드나 브라우저 상황에 따라 더 늦을 수 있다. 호출은 기다리지 않고 식별자를 반환한다. [MDN setTimeout](https://developer.mozilla.org/en-US/docs/Web/API/Window/setTimeout)

### 강사님 코드

출처: `teacher/workspace_html/javascript/08_function.html` 198–207행 · **원본 발췌**

```javascript
    // setTimeout의 return은 예약 번호다
    let idx = setTimeout(
        function(){
            console.log("야호!!!!!!!!!!")
        }, 
        1000
    )
    console.log(idx)
    // 예약 취소
    clearTimeout(idx)
```

### 내 코드

출처: `me/workspace_html/javascript/08_function.html` 218–225행 · **원본 발췌**

```javascript
            // setTimeout의 return은 예약번호이고, clearTimeout으로 해당 번호를 받아 취소할 수 있음
            let idx = setTimeout(
                function() { console.log("야호!!!!!!!!!!!")}, 
                1000
            )
            console.log(idx)
            // 예약 취소 clearTimeout
            clearTimeout(idx)
```

둘 다 1초 예약의 식별자를 idx에 저장한 뒤 즉시 clearTimeout으로 취소한다. 따라서 해당 느낌표 많은 야호는 출력되지 않는다. 앞에서 따로 예약한 3초·4초의 야호까지 모두 취소되는 것은 아니다. 예약마다 식별자가 다르기 때문이다. 식별자 숫자 자체는 환경·예약 순서에 따라 달라져 고정 정답으로 적지 않는다.

<a id="section-2"></a>

## 2. 반복 예약과 종료

### 강사님 코드

출처: `teacher/workspace_html/javascript/08_function.html` 224–231행 · **원본 발췌**

```javascript
    let idx2 = setInterval(function(){
        console.log('인터발')
    }, 1000*2)
    // clearInterval(idx2)
    // 10초 있다가 '인터발' 출력 끄기
    setTimeout(function(){
        clearInterval(idx2)
    }, 1000*10)
```

### 내 코드

출처: `me/workspace_html/javascript/08_function.html` 243–252행 · **원본 발췌**

```javascript
            // 지정한 시간마다 자동으로 반복되게끔 할 수 있음
            let idx2 = setInterval(function() {
                console.log('인터발')
            }, 1000*2)
            // clearInterval(idx2)
            // 10초 있다가 '인터발' 출력 끄기
            // 전달인자 안에 함수를 넣을 수 있으므로, clearInterval을 함수로 하여 초와 같이 넣음
            setTimeout(function(){
                clearInterval(idx2)
            }, 1000*10)
```

같은 구조다. 2초 간격의 반복 예약을 만들고 10초 후 해제를 예약한다. 일반적으로 2·4·6·8초 무렵의 실행을 기대하지만, 실제 실행 지연과 10초 경계의 예약 처리 때문에 정확한 출력 횟수를 계약처럼 단정하지 않는다. clearInterval은 이후 반복을 중지하며 이미 실행된 일을 되돌리지 않는다. [MDN setInterval](https://developer.mozilla.org/en-US/docs/Web/API/Window/setInterval)

<a id="section-3"></a>

## 3. 양쪽 재귀 예제의 오류

### 강사님 코드

출처: `teacher/workspace_html/javascript/08_function.html` 215–222행 · **원본 발췌**

```javascript
    function 기계_1초후_한번더( 함수 ){
        함수()

        setTimeout(
            기계_1초후_한번더( 함수 )
            ,1000
        )
    }
```

### 내 코드

출처: `me/workspace_html/javascript/08_function.html` 233–241행 · **원본 발췌**

```javascript
            // 리커시브, 재귀호출이라고 함(반복)
            function 기계_1초후_한번더( 함수 ) {
                함수()
                
                setTimeout(
                    기계_1초후_한번더( 함수 ),
                    1000
                )
            }
```

양쪽 모두 같은 문제다. setTimeout에 넘길 인수를 계산하면서 `기계_1초후_한번더(함수)`를 즉시 다시 호출한다. 이를 호출하면 1초 간격 예약이 아니라 동기 재귀가 계속되어 호출 스택 한계를 만날 수 있다. **원본 파일에는 이 함수의 바깥 호출이 없으므로 파일을 여는 것만으로 이 오류가 발생하는 것은 아니다.**

원본 rc(cb)는 cb()를 즉시 한 번 호출하고 setTimeout(cb,1000)으로 한 번 더 예약한다. 재귀적으로 계속 반복하는 함수가 아니며 rc도 원본에서 선언만 되어 있다. 기본 복습에는 이미 배운 setInterval·clearInterval을 사용하고, 취소 가능한 재귀 타이머 전체 구현은 추가편으로 분리한다.

<a id="section-4"></a>

## 4. 짧은 복습

1. clearTimeout(idx)은 모든 타이머를 취소하는가?
2. setTimeout(fn(),1000)은 fn을 1초 후 실행하는 코드인가?
3. 재귀 함수 정의에 오류가 있어도 원본이 즉시 멈추지 않는 이유는?

<details>
<summary>정답 확인</summary>

1. 해당 식별자의 예약을 취소한다.
2. 아니다. fn()을 먼저 실행하고 그 반환값을 넘긴다.
3. 해당 함수가 호출되지 않아 잘못된 재귀 경로가 실행되지 않았기 때문이다.

</details>

<a id="section-5"></a>

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/08-03_JavaScript_타이머와_취소_연습문제.md)

## 추가로 알면 좋은 것

취소 가능한 재귀 타이머 도구, 프레임 기반 애니메이션, 정밀 시간 보정과 이벤트 루프 내부 큐 상세는 확장이다. 기본은 예약·식별자 저장·해제의 관계다.

