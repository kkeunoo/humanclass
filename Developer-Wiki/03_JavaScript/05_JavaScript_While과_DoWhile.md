# 05. while과 do-while — 다시 입력받고, 조건에 맞으면 끝내기

[JavaScript 목차](README.md) · [이전: for와 배열 순회](04_JavaScript_반복문과_배열순회.md) · [다음: 배열](06_JavaScript_배열과_배열메서드.md)

기준은 양쪽 `05_while.html`이다. 강사님 파일은 메뉴 반복을 실행하지만 **내 파일의 JavaScript는 모두 주석 처리**되어 있다. 아래 주석 원본은 학습 기록이며 파일을 열기만 하면 실행되는 코드가 아니다. 개선 예제는 별도 표시한다.

<!-- chapter-toc -->

- [1. 반복 전에 검사할까, 한 번 실행한 뒤 검사할까](#section-1)
- [2. 메뉴를 다시 받는 위치](#section-2)
- [3. 배운 문법으로 메뉴 교정하기](#section-3)
- [4. 내가 작성한 입출금·주사위·업다운](#section-4)
- [5. 짧은 복습](#section-5)
- [추가로 알면 좋은 것](#section-6)

<a id="section-1"></a>

## 1. 반복 전에 검사할까, 한 번 실행한 뒤 검사할까

| 문법 | 조건 확인 시점 | 본문 실행 횟수 |
| --- | --- | --- |
| while (조건) { 본문 } | 실행 전 | 처음부터 거짓이면 0회 |
| do { 본문 } while (조건); | 실행 후 | 해당 문장에 도달하면 최소 1회 |

횟수가 정해진 반복은 for, 입력을 받을 때까지 계속하는 반복은 while로 표현하면 읽기 쉬운 경우가 많다. 기능의 절대적인 구분은 아니다. ‘for로 쓰면 비효율적’이라는 내 주석을 실행 성능의 일반 법칙으로 외우지 않는다. do-while의 조건 확인 순서는 [MDN do...while](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/do...while)과 같다.

### 강사님: 1부터 10까지

출처: `teacher/workspace_html/javascript/05_while.html` 8–12행 · **원본 발췌**

```javascript
    let i = 1
    while(i <= 10){
        console.log(i)
        i++
    }
```

### 내 기록

출처: `me/workspace_html/javascript/05_while.html` 10–14행 · **원본 발췌**

```javascript
            // let i=1;
            // while(i <= 10) {
            //     console.log(i)
            //     i++
            // }
```

주석을 해제하면 같은 흐름이다. i=1에서 시작해 조건 확인 → 출력 → i 증가를 반복한다. 10을 출력한 뒤 i가 11이 되어 끝난다. i++를 없애면 i가 계속 1이므로 종료 조건에 도달하지 못한다.

<a id="section-2"></a>

## 2. 메뉴를 다시 받는 위치

### 강사님 코드

출처: `teacher/workspace_html/javascript/05_while.html` 28–46행 · **원본 발췌**

```javascript
    menu = prompt('1:커피, 2:홍차, 0:종료')
    while(menu != 0){
    // while(true){
            
        // menu = prompt('1:커피, 2:홍차, 0:종료')

        if(menu == 1){
            console.log('커피 드릴께요')
        } else if(menu == 2){
            console.log('홍차 드릴께요')
        } else if(menu == 0){
            console.log('종료합니다')
            break
        } else {
            console.log('정확히 입력해 주세요')
        }

        menu = prompt('1:커피, 2:홍차, 0:종료')
    }
```

### 내 기록

출처: `me/workspace_html/javascript/05_while.html` 34–50행 · **원본 발췌**

```javascript
            // menu = prompt('1:커피, 2:홍차, 0:종료')
            // while(menu != 0) {
            // // while(true) {
                
            //     if(menu == 1) {
            //         console.log('커피 드릴게요')
            //     } else if(menu == 2) {
            //         console.log('홍차 드릴게요')
            //     } else if(menu == 0) {
            //         console.log('종료합니다.')
            //         // while에 true값을 주고 break을 따로 줄 수도 있지만, 안에있는 break을 찾기 어려움
            //         break;
            //     } else {
            //         console.log('정확히 입력해 주세요.')
            //     }
            //     menu = prompt('1:커피, 2:홍차, 0:종료')
            // }
```

핵심 구조는 같다. 첫 입력은 while 바깥, 다음 입력은 본문 마지막에서 받는다. 첫 입력 '1'이면 커피 문구를 출력하고 다시 입력받는다. **'0'이면 while 조건이 거짓이라 본문에 들어가지 않는다.** 따라서 이 구조의 `else if(menu == 0)` 안 종료 문구는 실행되지 않는다. 종료 문구를 while 뒤에 두면 정상 종료 때 한 번 보여 줄 수 있다.

prompt 취소의 결과는 null, 빈칸으로 확인하면 빈 문자열이다. null은 느슨한 비교로 0과 같지 않아 이 원본에서 취소해도 다시 입력받는다. 빈 문자열은 0과 동등 비교되므로 반복을 끝낸다. 이 차이는 메뉴 의도와 별개로 실제 코드가 만드는 결과다. [MDN prompt](https://developer.mozilla.org/en-US/docs/Web/API/Window/prompt)

### 강사님 do-while 코드

출처: `teacher/workspace_html/javascript/05_while.html` 49–62행 · **원본 발췌**

```javascript
    do {
        menu = prompt('1:커피, 2:홍차, 0:종료')
        
        if(menu == 1){
            console.log('커피 드릴께요')
        } else if(menu == 2){
            console.log('홍차 드릴께요')
        } else if(menu == 0){
            console.log('종료합니다')
            break
        } else {
            console.log('정확히 입력해 주세요')
        }
    } while(menu != 0)
```

### 내 기록

출처: `me/workspace_html/javascript/05_while.html` 55–68행 · **원본 발췌**

```javascript
            // do-while은 while과 다르게 우선 1회 진행하고나서 조건에 맞았을 때 추가 진행여부 확인
            // do {
            //     menu = prompt('1:커피, 2:홍차, 0:종료')
            //     if(menu == 1) {
            //         console.log('커피 드릴게요')
            //     } else if(menu == 2) {
            //         console.log('홍차 드릴게요')
            //     } else if(menu == 0) {
            //         console.log('종료합니다.')
            //         break;
            //     } else {
            //         console.log('정확히 입력해 주세요.')
            //     }
            // } while(menu != 0)
```

입력이 본문 첫 줄에 있어 입력 코드를 한 번만 쓴다. 이번에는 '0'을 받은 뒤에도 현재 본문의 조건문이 실행되어 종료 문구를 출력하고 break한다. 다만 취소·빈 입력 문제는 그대로다. while(true)가 웹페이지나 서버를 계속 운영하는 일반적인 방법이라는 내 주석은 적절하지 않다. 브라우저에서 종료되지 않는 동기 반복은 다른 화면 작업을 막을 수 있다.

<a id="section-3"></a>

## 3. 배운 문법으로 메뉴 교정하기

다음은 **원본의 종료·취소 처리를 수정한 독립 실행 예제**다. 입력을 숫자로 바꾸지 않고 '1'·'2'·'0'과 비교한다.

```javascript
while (true) {
    let menu = prompt('1:커피, 2:홍차, 0:종료');
    if (menu === null || menu === '0') {
        console.log('종료합니다');
        break;
    }
    if (menu === '1') {
        console.log('커피 드릴게요');
    } else if (menu === '2') {
        console.log('홍차 드릴게요');
    } else {
        console.log('정확히 입력해 주세요');
    }
}
```

| 입력 | 교정 예제 결과 |
| --- | --- |
| '1' → '2' → '0' | 커피 → 홍차 → 종료 |
| 취소 | 종료 |
| 빈 문자열 | 안내 후 다시 입력 |
| '3' | 안내 후 다시 입력 |

<a id="section-4"></a>

## 4. 내가 작성한 입출금·주사위·업다운

강사님 파일 68–87행에는 정사각형 테두리와 업다운 문제 조건이 있다. 입출금과 주사위의 직접 대응 풀이는 이 강사님 파일에서 확인되지 않는다. 학생 파일의 실습으로 소개하며 강사님 완성 답이라고 붙이지 않는다.

### 입출금: 금액 범위와 정수 여부는 다르다

출처: `me/workspace_html/javascript/05_while.html` 84–92행 · **원본 발췌**

```javascript
            //         let input = prompt('얼마를 입금하시겠습니까?')
            //         bank_input = Number(input)
            //         // bank_input에 값이 들어왔을 때 정수이면 bank_money 총 잔액에 저장하고,
            //         // 그 외 다른값이 들어왔을 때 방어할 수 있도록 else에 입력한 값과 같이 출력
            //         if(bank_input >= 0) {
            //             bank_money += bank_input
            //         } else {
            //             console.log(`입금 금액을 확인하세요.\n입력하신 금액 : ${bank_input}`)
            //         }
```

bank_input >= 0은 음수가 아닌지 확인한다. 주석처럼 정수인지 확인하는 조건은 아니므로 1.5도 통과한다. Number 변환 전에 취소·빈 입력을 확인하지 않으면 둘 다 0으로 처리된다. 출금의 `bank_output <= bank_money && bank_output >= 0`은 잔액 초과를 막는 장점이 있다. 메뉴에서 4를 입력하면 끝나지만 null을 종료로 처리하는 조건은 없다. 이 실습을 완전한 금액 검증 도구로 소개하지 않는다.

### 주사위: 횟수 증가 위치

내 123–143행은 주사위를 던질 때마다 cnt를 증가시키고 3이면 break한다. 3이 나온 시도도 횟수에 포함한다. 주사위 값을 while 밖에서 한 번만 뽑으면 같은 값만 검사하므로, 이 문제에서는 난수 생성이 안쪽에 있어야 한다.

### 강사님 업다운 문제

출처: `teacher/workspace_html/javascript/05_while.html` 83–87행 · **원본 발췌**

```javascript
    // 업다운 게임
    // 1~100까지 임의의 정답이 있을 때
    // 정답보다 낮은 숫자 : "UP"
    // 정답보다 높은 숫자 : "DOWN"
    // 정답까지 걸린 시도 횟수 출력
```

### 내 업다운 풀이의 핵심

출처: `me/workspace_html/javascript/05_while.html` 157–182행 · **원본 발췌**

```javascript
            // // prompt로 받을 값을 저장할 변수와, 몇 번 시도했는지 count하기 위한 변수 설정
            // let result = 0;
            // let updown_cnt = 0;
            // while(true) {
            //     // 밖에서 컴퓨터의 랜덤 정답을 숫자로 변환하였기 때문에, 사용자에게 받은 값도 숫자로 변환 및 카운트
            //     let value = prompt(`업다운게임! 숫자를 입력하세요.\n종료하려면 '0'입력 또는 취소를 눌러주세요.`)
            //     result = Number(value)
            //     updown_cnt++

            //     // 우선, 1~100까지의 값만 받기 위해 그 사이 값일 경우에만 동작하게 if로 조건을 주고
            //     // 그 외 값이 들어왔을 땐 동작되지 않게 하기 위해서 else에 오류문 출력
            //     if(result >= 0 && result <= 100){
            //         // if는 상위부터 우선순위가 들어가기 때문에 0이 들어오거나 취소 버튼을 눌렀을 때
            //         // 게임이 종료되도록 if에 취소(null) 또는 0을 or로 조건문을 추가하고 그 아래에는 
            //         // else if로 한 번에 맞췄을 때, 못 맞추었을 때 up,down을 출력하게끔 구성
            //         if(result == null || result == 0) {
            //             console.log('게임을 취소했어요!')
            //             break;
            //         } else if(updown_result == result){
            //             // 정답과 몇 번 시도했는지 확인하기 위해 while문 처음에 추가한 count값 출력
            //             console.log(`정답은 [${updown_result}]\n${updown_cnt++}번만에 맞추셨습니다!`)
            //             break;
            //         } else if(updown_result > result) {
            //             console.log(`${result} 거의 다 왔어요! UP!`)
            //         } else if(updown_result < result) {
            //             console.log(`${result} 거의 다 왔어요! DOWN!`)
```

정답을 반복문 밖에서 한 번 정한 점이 좋다. 숫자 비교 때마다 정답이 바뀌면 같은 문제를 풀 수 없기 때문이다. 다음 네 부분은 설명을 고친다.

1. parseInt로 만든 정답은 이미 숫자이므로 Number로 다시 변환할 필요가 없다.
2. value를 Number로 바꾼 result는 취소 시 null이 아니라 0이다. result==null은 취소를 잡지 못하고 뒤의 result==0이 종료시킨다. 빈 입력도 같은 이유로 종료된다.
3. updown_cnt는 유효한 입력인지 확인하기 전에 증가하여 잘못된 입력도 센다.
4. 정답 문구의 updown_cnt++는 현재 횟수를 출력한 뒤 한 번 더 증가시킨다. 표시된 숫자가 반드시 1 크게 나오는 것은 아니다. 다만 저장된 횟수는 불필요하게 늘어난다.

### 업다운 교정 예제

다음은 **배운 while·조건·변환·나머지로 재작성한 복습 예제**다. 유효한 1–100 정수 추측만 횟수로 센다. 원본에서 사용한 전역 isNaN은 숫자 변환을 포함해 검사한다. Number.isNaN과 다른 함수이며 새로 배운 API인 것처럼 바꾸지 않는다. [MDN isNaN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/isNaN)

```javascript
let answer = parseInt(Math.random() * 100) + 1;
let count = 0;
while (true) {
    let input = prompt('1~100 정수 입력, 0 또는 취소로 종료');
    if (input === null) break;
    if (input === '') {
        console.log('숫자를 입력하세요');
        continue;
    }
    let guess = Number(input);
    if (guess === 0) break;
    if (isNaN(guess) || guess < 1 || guess > 100 || guess % 1 !== 0) {
        console.log('1~100 정수를 입력하세요');
        continue;
    }
    count++;
    if (guess === answer) {
        console.log(`정답! ${count}번 만에 맞췄습니다`);
        break;
    } else if (guess < answer) {
        console.log('UP');
    } else {
        console.log('DOWN');
    }
}
```

빈 문자열은 재입력하지만 공백만 입력하면 Number가 0으로 바꾸어 종료한다. 이 예제의 범위를 명시한 것이며, 공백 정리는 뒤 문자열 장의 trim을 배운 뒤 적용할 수 있다. 취소를 숫자 변환보다 먼저 확인하는 순서는 여기서 기억한다.

<a id="section-5"></a>

## 5. 짧은 복습

1. while과 do-while에서 첫 조건이 거짓이면 본문 실행 횟수는?
2. 위 교정 업다운에서 정답 50, 입력 'abc' → '30' → '50'이면 결과와 횟수는?
3. 원본 정사각형 테두리 문제에서 한 칸이 테두리인 조건은?

<details>
<summary>정답 확인</summary>

1. while은 0회, do-while은 한 번 실행한 뒤 검사한다.
2. 재입력 안내 → UP → 정답 2회다.
3. 행이 첫째/마지막이거나 열이 첫째/마지막이면 테두리다. 이 조건을 중첩 반복과 ||로 표현할 수 있다. 강사님 파일은 문제만 제시하므로 원본 완성 풀이와 혼동하지 않는다.

</details>

<a id="section-6"></a>

## 추가로 알면 좋은 것

Number.isInteger 등 별도 검증 API, 비동기 입력 UI, 저장 가능한 은행·재고 앱은 확장으로 분리한다. 이 장의 목표는 입력 → 검사 → 처리 → 다음 입력·종료의 순서를 읽는 것이다.

