# 04. 반복문과 배열 순회 — 변하는 값과 반복할 일을 찾기

[JavaScript 목차](README.md) · [이전: 조건문](03_JavaScript_조건문과_Switch.md)

기준은 양쪽 `04_for.html`, `04_1_pyramid.html`이다. 배열 콜백은 원본에 이미 나오므로 학습 본문에 포함한다. 함수의 자세한 문법은 뒤의 함수 장에서, 배열 추가·삭제는 배열 장에서 다룬다.

**반복문**은 같은 작업을 정해진 조건 동안 다시 실행한다. 먼저 **설명용 예제**를 보자.

```javascript
let sum = 0;
for (let i = 1; i <= 3; i++) {
    sum += i;
}
console.log(sum); // 6
```

`i`가 1·2·3일 때 각각 더해 `sum`은 0 → 1 → 3 → 6이 된다. 원본은 같은 원리로 1부터 5까지 더한다. 시작값·조건·변화·반복할 문장을 나누어 읽는다.

<!-- chapter-toc -->

- [1. for 실행 순서와 누적](04_JavaScript_반복문과_배열순회.md#section-1)
- [2. 중첩 반복: 바깥은 묶음, 안쪽은 묶음 안의 항목](04_JavaScript_반복문과_배열순회.md#section-2)
- [3. break와 continue](04_JavaScript_반복문과_배열순회.md#section-3)
- [4. 배열을 순회할 때 받는 것](04_JavaScript_반복문과_배열순회.md#section-4)
- [5. 피라미드: 줄마다 문자열을 새로 쌓기](04_JavaScript_반복문과_배열순회.md#section-5)
- [6. 짧은 복습](04_JavaScript_반복문과_배열순회.md#section-6)
- [추가로 알면 좋은 것](04_JavaScript_반복문과_배열순회.md#section-7)

<a id="section-1"></a>

## 1. for 실행 순서와 누적

`for (초기화식; 조건식; 증감식)`의 순서는 초기화 한 번 → 조건 확인 → 본문 → 증감 → 다시 조건 확인이다. 내 원본 9행의 설명에는 증감식 뒤 세미콜론이 하나 더 있지만 실제 문법에는 구분용 세미콜론이 **두 개**다. 조건 생략은 참으로 취급되지만, break 등으로 끝낼 수도 있으므로 반드시 무한히 실행된다고 단정하지 않는다.

### 강사님 코드

출처: `teacher/workspace_html/javascript/04_for.html` 32–36행 · **원본 발췌**

```javascript
    sum = 0;
    for(let i=1; i<=5; i++){
        sum = sum + i
    }
    console.log(sum)
```

### 내 코드

출처: `me/workspace_html/javascript/04_for.html` 33–37행 · **원본 발췌**

```javascript
           sum = 0;
           for(let i=1; i<=5; i++) {
                sum += i
           }
           console.log(sum)
```

sum은 앞에서 선언한 변수다. 둘 다 0 → 1 → 3 → 6 → 10 → 15가 되고 마지막에 15를 한 번 출력한다. 내 +=는 같은 누적을 짧게 쓴 것으로 적절하다. sum=0을 반복문 안에 넣으면 매번 누적값이 지워진다.

| 수업 실험 | 시작·조건·변화 | 결과 |
| --- | --- | --- |
| 1–10 출력 | i=1, i<=10, i++ | 10번 출력 |
| 5–1 출력 | i=5, i>=1, i-- | 5번 출력 |
| 1–10 홀수 세기 | 홀수일 때 count 증가 | 5 |
| 구구단 2–9단 | 바깥 8회 × 안쪽 9회 | 72개 곱셈 출력 |
| 주사위 두 개 | 바깥 6회 × 안쪽 6회 | 순서 있는 36쌍 |

<a id="section-2"></a>

## 2. 중첩 반복: 바깥은 묶음, 안쪽은 묶음 안의 항목

### 강사님 코드

출처: `teacher/workspace_html/javascript/04_for.html` 185–202행 · **원본 발췌**

```javascript
    let hap9 = ""
    for(let k=2; k<=12; k++){
        console.log('=-=-= 합이 '+k+'인 것 =-=-=')
        // 주사위 두개 도는 곳
        for(let j=1; j<=6; j++){
            for(let i=1; i<=6; i++){
                // 합이 k인 것만 출력
                if(j+i == k){
                    console.log('['+j+','+i+'] ')
                    if(k == 9){
                        hap9 += '['+j+','+i+'] '
                    }
                }
            }
        }
        console.log()
    }
    console.log('합 9 :'+ hap9)
```

### 내 코드

출처: `me/workspace_html/javascript/04_for.html` 168–178행 · **원본 발췌**

```javascript
            for(let r=2; r<=12; r++) {
                let value = `합계 ${r} `
                for(let p=1; p<=6; p++) {
                    for(let q=1; q<=6; q++) {
                        if(p+q == r) {
                            value += `[${p}, ${q}]`;
                        }
                    }
                }
                console.log(value)
            }
```

강사님은 조합을 한 쌍씩 출력하면서 합 9의 문자열을 따로 보관한다. 내 코드는 각 합의 조합을 value 한 줄에 모아 출력한다. 한 합의 모든 경우를 눈으로 비교할 때는 내 출력이 편하다. 합 9는 [3,6], [4,5], [5,4], [6,3] 네 쌍이다. value를 바깥 반복의 안쪽에서 새로 만들기 때문에 다음 합에 이전 조합이 섞이지 않는다.

원본의 ‘로또’ 반복은 1–45 난수를 여섯 번 출력한다. 이전 값과 중복인지 검사하지 않으므로 실제 로또처럼 서로 다른 여섯 수를 보장하지 않는다. Set을 새로 도입해 고친 예제를 이 장의 원본 풀이로 넣지 않는다.

<a id="section-3"></a>

## 3. break와 continue

break는 가장 가까운 반복문을 끝낸다. continue는 이번 본문의 남은 부분을 건너뛰고 다음 반복으로 간다. for의 continue 뒤에도 증감식은 실행된다.

원본은 i=11에서 종료 문구를 출력하고 break한다. 따라서 숫자만 출력하는 줄은 1–10에서 실행되고, 11에서는 ‘종료합니다’가 붙은 별도 출력이 나온다. continue 예제는 짝수일 때 출력을 건너뛰어 1·3·5·7·9를 출력한다.

중첩 반복을 모두 끝내는 원본은 안쪽에서 flag=true와 break, 바깥에서 flag 검사와 break를 쓴다. cnt가 17일 때 i=2, j=7이다. 강사님 원본에는 안쪽 break 직전에 j++가 있지만 종료 판정에 필요하지 않다. 내 코드는 이 불필요한 증가가 빠져 있어 흐름이 더 간단하다.

<a id="section-4"></a>

## 4. 배열을 순회할 때 받는 것

배열은 여러 값을 순서대로 담는 자료다. `[1,2,3,4,5,6,7]`의 첫 인덱스는 0, 마지막 인덱스는 6, length는 7이다.

| 방법 | 수업 예제에서 받는 것 | 기억할 차이 |
| --- | --- | --- |
| for...in | '0'~'6' 같은 속성 이름 | 값은 arr[i]로 읽음 |
| for...of | 1–7 값 | 값 자체가 필요할 때 명확 |
| forEach | 값, 인덱스, 배열을 콜백에 전달 | forEach 호출의 반환은 undefined |
| map | 각 값으로 만든 새 결과 | 새 배열 반환 |
| filter | 조건이 참인 원소 | 통과한 원소의 새 배열 반환 |
| sort | 두 원소를 비교 | 원본 배열 순서 변경 |

콜백은 지금 바로 호출하는 대신 다른 함수에 전달하여 필요할 때 실행하게 하는 함수다. 원본 `function(element, index, array)`는 forEach가 원소마다 호출한다. 네 번째 매개변수 d를 써도 네 번째 인자가 전달되는 것은 아니므로 d는 undefined다. forEach 안에서 일반 for처럼 break를 쓸 수는 없다.

for...in은 배열 전용 인덱스 반복문이 아니다. 열거 가능한 다른 속성도 대상이 될 수 있으므로 이 원본 배열의 결과와 일반 규칙을 구분한다. [MDN for...in](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in)

### 강사님 map 코드

출처: `teacher/workspace_html/javascript/04_for.html` 293–301행 · **원본 발췌**

```javascript
    let r2 = arr.map(function(el, i, a){
        console.log(el, i, a)
        if(el %2 == 0){
            return '짝'
        } else {
            return '홀'
        }
    })
    console.log(r2) // undefined
```

### 내 map 코드

출처: `me/workspace_html/javascript/04_for.html` 270–281행 · **원본 발췌**

```javascript
            let r2 = arr.map(function(el, i, a) {
                console.log(el, i, a)
                // return i
                // return el
                // return a
                if(el %2 == 0) {
                    return '짝'
                } else {
                    return '홀'
                }
            })
            console.log(r2) // retrurn이 없으면 undefined array
```

앞에서 만든 arr를 사용한다. 실제 r2는 `['홀','짝','홀','짝','홀','짝','홀']`이다. **강사님 마지막 주석의 undefined는 잘못된 설명**이다. 내 주석은 return이 없는 경우를 이야기하지만 현재 코드는 양쪽 갈래 모두 return이 있다. return을 없애면 배열 자체가 undefined가 되는 것이 아니라, 이 원본처럼 빈칸 없는 배열에서는 각 결과 원소가 undefined인 새 배열이 된다. [MDN map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)

movie.map은 제목을 제목 길이로 바꾼 새 배열을 만든다. filter는 길이가 4 이상인 제목만 남긴다. sort의 매개변수 이름이 y,x라고 하여 의미가 뒤집히는 것은 아니다. 첫 인자에서 둘째를 빼는 y-x는 이 숫자 예제에서 오름차순, 둘째에서 첫째를 빼는 x-y는 내림차순이다. 마지막 원소를 읽는 `r3[r3.length-1]`이 최댓값인 것은 바로 앞에서 오름차순 정렬했기 때문이다.

<a id="section-5"></a>

## 5. 피라미드: 줄마다 문자열을 새로 쌓기

### 강사님 문제

출처: `teacher/workspace_html/javascript/04_1_pyramid.html` 182–189행 · **원본 발췌**

```javascript
		// 10단계
		/*
			  ____+
			  ___+++
			  __+++++
			  _+++++++
			  +++++++++
		  */
```

이 위치는 목표 모양이며 완성 풀이가 아니다. 같은 파일의 앞부분에는 문자열 누적과 중첩 반복 실험이 있다.

### 내 풀이

출처: `me/workspace_html/javascript/04_1_pyramid.html` 207–217행 · **원본 발췌**

```javascript
            console.log('- - - - - 10단계-1 - - - - -')
            for(let j=1; j<=5; j++) {
                string = ''
                for(let i=1; i<=5-j; i++) {
                    string += '_'
                }
                for(let k=1; k<=2*j-1; k++) {
                    string += '+'
                }
                console.log(string)
            }
```

바깥 j는 줄 번호 1–5다. 각 줄에서 string을 비우고, 밑줄 5-j개 뒤에 더하기 기호 2*j-1개를 붙인다. j=1이면 밑줄 4개·기호 1개, j=3이면 밑줄 2개·기호 5개, j=5이면 밑줄 없이 기호 9개다. 내 앞선 복잡한 10단계 풀이보다 이 10단계-1의 개수 식이 목표 모양을 더 직접적으로 설명한다.

원본 11단계는 오른쪽에도 밑줄 5-j개를 붙이고, 12단계는 높이 5를 입력값으로 바꾼다. 높이에 소수나 취소를 넣는 상황까지 검증한 코드로 간주하지 않는다. 내 `04_2_복습.html`은 별도 복습 기록이며 대표 설명은 중복하지 않고 이 장에 모은다.

<a id="section-6"></a>

## 6. 짧은 복습

1. sum 초기화를 반복문 안으로 옮기면 1–5 누적 결과는?
2. 주사위 두 개의 합이 12인 쌍은?
3. 피라미드 네 번째 줄은?

<details>
<summary>정답 확인</summary>

1. 매번 0에서 시작하므로 마지막은 5다.
2. [6,6] 한 쌍이다.
3. 밑줄 1개와 + 7개인 `_+++++++`다.

</details>

<a id="section-7"></a>

## 추가로 알면 좋은 것

Set 중복 제거, repeat로 피라미드 만들기, 별도의 반복 성능 최적화는 확장이다. 기본 복습에서는 원본의 for·조건문·문자열 누적으로 풀어 본다.

---

[장별 연습문제 풀기](실습/연습문제/04_JavaScript_반복문과_배열순회_연습문제.md) · [다음: while과 do-while](05_JavaScript_While과_DoWhile.md)

