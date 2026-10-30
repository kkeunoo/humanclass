# 05. while과 do-while — 검사·처리·다음 입력·종료

[JavaScript 목차](README.md) · [읽기 안내](00_JavaScript_V3_동작_백과_읽기법.md)

반복 횟수보다 ‘계속할 조건’이 중요한 경우가 있다. 메뉴를 다시 입력받거나 정답을 맞힐 때까지 시도하는 코드에서는 조건을 언제 검사하고 어떤 값을 다음에 바꾸는지 읽어야 한다.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

while의 사전 검사와 do-while의 사후 검사를 구분한다. 원본의 주석 상태·도달하지 못하는 종료 문구·숫자 변환과 횟수 증가 위치를 설명한다.

입력·현재 상태·실행 순서·결과를 분리해 설명한다. 실제 수업 원본은 아래에 표시하고, 원본에 없는 선택 학습은 9절 TIP에 둔다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

while은 본문 실행 전에 조건을 검사하므로 처음부터 거짓이면0회다. do-while은 본문 뒤에서 검사하므로 그 문장에 도달하면 최소1회 실행한다. 횟수를 알면 for, 조건 중심이면 while이 읽기 좋은 경우가 많지만 절대적인 기능·성능 구분은 아니다.

```text
while:    조건 → 본문 → 조건 → …
do-while: 본문 → 조건 → 본문 → …
```

끝나려면 조건에 영향을 주는 입력·변수 변경이나 break가 있어야 한다. i<=10인데 i를 계속1로 두면 같은 조건을 반복한다. 브라우저의 끝나지 않는 동기 반복은 다른 화면 작업을 막을 수 있으므로 웹페이지를 계속 운영하는 일반 해법으로 소개하지 않는다.

입력을 반복할 때는 입력 → 취소·빈값 확인 → 숫자 변환 → 범위·정수 조건 → 처리 → 다음 입력 순서를 생각한다. prompt 취소는null, 빈 입력은''이다. Number 변환 후에는 둘 다0이어서 원래 상태를 잃을 수 있다. `값>=0`은 음수가 아닌지 묻는 조건이며 정수 검사가 아니다.

> 📚 **출처 · 본문 설명 확인:** [MDN while](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while), [do...while](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/do...while), [prompt](https://developer.mozilla.org/en-US/docs/Web/API/Window/prompt). 배운 기능의 뜻을 확인한 근거다. 예제·표·풀이 흐름은 수업 코드를 바탕으로 새로 작성했으며 외부 문장을 직접 인용하지 않았다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 스크립트.** [HTML 실행 파일](실습/책형_복습/05_JavaScript_While과_DoWhile.html)과 같은 폴더의 [JS 파일](실습/책형_복습/05_JavaScript_While과_DoWhile.js)을 함께 내려받는다. HTML을 브라우저로 열고 Console에서 결과를 확인한다. script는 필요한 HTML 뒤에 연결한다. 콘솔 출력은 페이지 본문에 자동으로 쓰이지 않는다.

```javascript
let first = 0;
while (first > 0) {
    console.log('while 본문');
    first--;
}
console.log('while 끝', first);
let second = 0;
do {
    console.log('do 본문', second);
    second--;
} while (second > 0);
console.log('do 끝', second);
```

첫 조건0>0은 거짓이어서 while 본문은 건너뛴다. do는0을 출력하고 second를-1로 바꾼 뒤 조건을 검사해 끝난다. 실행 횟수의 차이를 보기 위해 입력 창과 난수를 제거한 새 예제다. 실제 메뉴 원본에 이 출력이 있었다는 뜻은 아니다.

**예상 출력 또는 관찰:**

```text
while 끝 0
do 본문 0
do 끝 -1
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본의 일부다. 원본에 의존하는 앞 선언·HTML·함수는 다음 절의 연결까지 읽는다. 주석의 잘못된 표현도 원문대로 보존하고 설명에서 교정한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/05_while.html` 10–14행

```javascript
            // let i=1;
            // while(i <= 10) {
            //     console.log(i)
            //     i++
            // }
```

**발췌 바로 풀이:** 주석을 해제하면 같은 흐름이다. i=1에서 시작해 조건 확인 → 출력 → i 증가를 반복한다. 10을 출력한 뒤 i가 11이 되어 끝난다. i++를 없애면 i가 계속 1이므로 종료 조건에 도달하지 못한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/05_while.html` 34–50행

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

**발췌 바로 풀이:** 핵심 구조는 같다. 첫 입력은 while 바깥, 다음 입력은 본문 마지막에서 받는다. 첫 입력 '1'이면 커피 문구를 출력하고 다시 입력받는다. **'0'이면 while 조건이 거짓이라 본문에 들어가지 않는다.** 따라서 이 구조의 `else if(menu == 0)` 안 종료 문구는 실행되지 않는다. 종료 문구를 while 뒤에 두면 정상 종료 때 한 번 보여 줄 수 있다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/05_while.html` 55–68행

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

**발췌 바로 풀이:** 입력이 본문 첫 줄에 있어 입력 코드를 한 번만 쓴다. 이번에는 '0'을 받은 뒤에도 현재 본문의 조건문이 실행되어 종료 문구를 출력하고 break한다. 다만 취소·빈 입력 문제는 그대로다. while(true)가 웹페이지나 서버를 계속 운영하는 일반적인 방법이라는 내 주석은 적절하지 않다. 브라우저에서 종료되지 않는 동기 반복은 다른 화면 작업을 막을 수 있다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/05_while.html` 84–92행

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

**발췌 바로 풀이:** bank_input >= 0은 음수가 아닌지 확인한다. 주석처럼 정수인지 확인하는 조건은 아니므로 1.5도 통과한다. Number 변환 전에 취소·빈 입력을 확인하지 않으면 둘 다 0으로 처리된다. 출금의 `bank_output <= bank_money && bank_output >= 0`은 잔액 초과를 막는 장점이 있다. 메뉴에서 4를 입력하면 끝나지만 null을 종료로 처리하는 조건은 없다. 이 실습을 완전한 금액 검증 도구로 소개하지 않는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/05_while.html` 157–182행

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

**발췌 바로 풀이:** 정답을 반복문 밖에서 한 번 정한 점이 좋다. 숫자 비교 때마다 정답이 바뀌면 같은 문제를 풀 수 없기 때문이다.

내 파일의 JavaScript는 모두 주석 처리되어 있다. 아래 발췌도 실행 결과가 아닌 학습 기록이다. 1~10 반복은 i가11이 된 뒤 종료한다. 메뉴 while은 첫 입력을 밖에서 받고 본문 끝에서 다시 받는다. menu가'0'이면 조건이 거짓이라 본문에 들어가지 않아 안쪽 종료 문구는 실행되지 않는다. do-while은 입력 뒤 현재 본문의 조건문까지 실행하므로'0'에서 종료 문구를 보여 줄 수 있다.

입출금의 bank_input>=0은1.5도 통과한다. 출금에서 잔액 이하·0이상 검사한 점은 좋지만 취소·빈입력·정수 검증은 별도다. 이 사례에는 같은 강사님 완성 풀이가 없어 학생의 실습으로 소개한다.

주사위는 매 시도 난수를 안에서 새로 뽑고 횟수를 올린다. 반대로 업다운 정답은 밖에서 한 번 정해야 같은 문제를 계속 맞힐 수 있다. 내 업다운은 입력 검증 전에 횟수를 올리고 정답 출력에도 cnt++가 있어 저장 횟수가 한 번 더 늘어날 수 있다. 후위는 현재 횟수를 출력하므로 화면 숫자가 반드시1큰 것은 아니다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

원본 menu·bank_money·updown_result는 앞에서 준비한 상태다. 발췌만 읽을 때도 그 초기값을 찾아야 한다. 업다운에서 prompt의 value를 Number로 바꾼 result는 취소 시null이 아니라0이다. result==null보다 뒤 result==0이 종료시킨다. 정답 parseInt 결과는 이미 숫자라 다시 Number로 변환할 필요가 없다. 호출·변환·상태 변경의 순서를 한 줄씩 적는다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 업다운 정답을 반복 밖에 두고 출금에 잔액 제한을 썼다. **교정:** 범위 검사를 정수 검사라고 부르지 않는다. while의 안쪽 종료 갈래는 도달 가능한지 확인한다. **개선 방향:** 취소를 변환 전 확인하고, 유효한 추측만 count++한다. 원본이 주석이라 조용히 열린다는 사실과 주석을 해제했을 때 올바른 동작인지는 다른 판단이다.

개선안은 원본을 수정한 결과가 아니다. 실제 오류, 수업용 단순화, 목적에 따른 선택을 구별해 판단한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



강사님 파일은 메뉴를 실행하지만 내 파일은 주석 기록이다. 주석을 해제한 같은 부분의 핵심 흐름은 같아 중복 인용하지 않는다. 강사님 업다운은 문제 조건만 제시하므로 내 풀이를 강사님 완성 답으로 붙이지 않는다. 정사각형 테두리도 행·열이 처음 또는 마지막이라는 조건을 푸는 별도 문제다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 원본 while 메뉴 입력 | 결과 | 이유 |
| --- | --- | --- |
| '1' |커피 후 다음 입력 |본문 실행 |
| '0' |본문 진입 안 함 |느슨한 비교로0과 같음 |
| 취소null |안내 후 재입력 가능 |null은0과 동등하지 않음 |
| 빈문자열 |종료 조건으로 빠짐 |빈문자열과0의 느슨한 비교 |

**새 개선 흐름:** menu를문자열로 두고 null 또는'0'을 먼저 종료 처리하면 취소와 빈값을 구별할 수 있다. 업다운에서는 변환 전null·''확인 → Number →0종료 → isNaN·1~100·나머지%1로정수검사 →count++ →정답/UP/DOWN 순서다. 정답50에'abc'→'30'→'50'이면 안내→UP→정답2회다. 공백만 입력한 경우를 다루려면 뒤 문자열 장의 trim을 배운 뒤 별도 정책을 정한다.

| 한 가지 변경 | 예상 | 이유 |
| --- | --- | --- |
| first만1로 |while 본문1회 |감소 후0 |
| 원래second만2로 |do 본문2·1 출력 |두번 실행 |
| 원래while 조건만first>=0으로 |본문0에서1회 |감소해-1로종료 |

화면이 멈춘다면 종료 조건에 도달하는 값 변경이 있는지 본다. 무한 반복을 시험하려고 안전한 예제의 증감식을 무턱대고 지우지 않는다. 메뉴가 종료 문구 없이 끝났다면 본문 전 검사인지부터 확인한다. 입력 유효성·성공 횟수·반복 종료는 서로 다른 조건이다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** Number.isInteger 등 별도 검증 API·비동기 입력 UI·저장 가능한 은행 앱은 추가 학습이다. 원본의 전역 isNaN과 Number.isNaN은 서로 다른 함수다.



이 절의 확장은 기본 문제의 필수 조건이 아니다. 📚 출처가 있다는 것과 수업 밖 기능이라는 것은 다른 구분이다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. 처음 조건이 거짓이면 두 반복은 몇 번 실행하는가?
2. 0이상 검사는 정수 검사인가?
3. 업다운 정답은 반복 안에서 계속 바꾸는가?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

while은0회, do-while은 최소1회다.0이상은 소수도 통과한다. 업다운은 같은 문제를 맞혀야 하므로 정답을 밖에서 한 번 정한다.

</details>

| 질문 | 확인 |
| --- | --- |
| 먼저/나중 검사 | while/do-while |
| 끝날 수 있나 | 입력·증감·break |
| 취소는 어디서 | Number변환전 |
| 횟수는 언제 | 유효입력후 |

[장별 연습문제](실습/연습문제/05_JavaScript_While과_DoWhile_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [배열](06_JavaScript_배열과_배열메서드.md)이다.

<!-- 이전 색인 이동 주소 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
<a id="section-6"></a>

[이 장의 목차](#chapter-toc)에서 현재 설명을 찾는다.
