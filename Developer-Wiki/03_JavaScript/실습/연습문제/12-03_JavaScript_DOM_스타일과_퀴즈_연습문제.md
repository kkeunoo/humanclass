# 12-03. DOM 스타일과 퀴즈 — 단위 문자열과 클래스 조건 — 연습문제

[본문](../../12-03_JavaScript_DOM_스타일과_퀴즈.md) · [문제 목차](README.md)

실제 수업 기능을 바탕으로 **새로 구성한 연습문제**다. 강사님 원본 퀴즈와 구분한다. 예상 → 이유 → 수정 순서로 풀고, 정답은 먼저 답한 뒤 펼친다.

## 목표와 실행 조건

style과 계산된 스타일을 비교한다. px분리·숫자 계산·단위 재결합을 설명하고 클래스 개수·글자·빈값 퀴즈를 검토한다.

[전체 실행 HTML](../책형_복습/12-03_JavaScript_DOM_스타일과_퀴즈.html)과 같은 폴더의 JS를 함께 준비한다. Console을 열고 새로고침하면 처음부터 실행한다. 원본과 별도 파일이므로 기존 변수·타이머·출력 변경 실험의 영향을 섞지 않는다. 실제 입력·현재 시각·난수는 고정 결과와 구별한다.

입력·버튼·키보드·스크롤 예제는 [본문의 3절](../../12-03_JavaScript_DOM_스타일과_퀴즈.md#example)에 적힌 조작 순서대로 결과를 예상한다. 통신 예제는 해당 절의 가상 JSON 파일과 로컬 웹 실행 준비가 필요하며 HTML을 직접 여는 조건과 다르다. Console 출력이 없는 문제는 화면의 값·개수·선택 상태를 답한다.

## 문제 1. 실행 순서와 결과 예상

다음은 **새 설명 예제**다. 출력 전에 어떤 값이 어떤 순서로 만들어지는지 적는다.

**필요한 HTML · 스크립트 앞:**

```html
    <div id="box">크기 관찰</div>
    <div class="quiz q2">퀴즈2</div>
    <div class="quiz q2">   </div>
    <div class="quiz q2-1">다른 클래스</div>
```

**필요한 CSS · head의 style:**

```css
        #box { height: 66px; }
```

```javascript
const box = document.getElementById('box');
console.log(`인라인=[${box.style.height}]`);
const height = getComputedStyle(box).getPropertyValue('height');
console.log(height);
box.style.height = parseInt(height) + 5 + 'px';
console.log(box.style.height);
const quizzes = document.querySelectorAll('.quiz');
let count = 0;
for (let i = 0; i < quizzes.length; i++) {
    if (quizzes[i].classList.contains('q2')) {
        count++;
    }
    if (quizzes[i].textContent.trim() === '') {
        quizzes[i].textContent = '비어있음';
    }
}
console.log(count);
console.log(quizzes[1].textContent);
```

<details>
<summary>힌트와 풀이</summary>

**힌트:** 입력·현재 상태·실행 시점·반환값을 따로 표시한다.

```text
인라인=[]
66px
71px
2
비어있음
```

높이를 CSS 규칙으로만 주어 인라인값은 빈 문자열이지만 계산된 높이는66px다. 숫자로 읽어5 더하고 px를 붙여 인라인71px로 쓴다. q2는 두 개이고 q2-1은 세지 않는다. 두 번째 quiz의 공백은 trim 뒤 비어 있어 글자를 채운다. 원본 여섯 요소를 세 개로 줄인 새 예제임을 구분한다.

</details>

## 문제 2. 개념을 자신의 말로 설명

1. style.height가 비었으면 실제 높이도0인가?
2. q2-1에 contains(q2)는 참인가?
3. 공백만 있는 textContent를 비었다고 검사하려면?

<details>
<summary>풀이</summary>

반드시0은 아니며 인라인값이 없을 수 있다. 정확한 항목이 다르면 false다. trim 후 빈 문자열과 비교할 수 있다.

| 내 원본 퀴즈 | 결과·판단 |
| --- | --- |
| q1 문장 추가 |기존 문장 뒤 새 글자 |
| div.quiz 중 q2 |6개 중2개 |
| q2 글자 읽기 |퀴즈2와 공백3칸 |
| 빈 글자 채우기 |일반 표시 상태의 공백 요소에 비어있음 |

강사님 문제 주석의 예상 문구 퀴즈2-1과 실제 q2 요소 글자는 다르다. 내 결과를 틀린 주석에 맞추지 않는다. 공백 검사는 실제 표시 기준인지, 양끝을 제거한 텍스트 기준인지 요구사항으로 정한다.

</details>

## 문제 3. 한 가지를 바꾸어 확인

먼저 **CSS높이만80px**를 바꾸면 무엇이 달라질지 적는다. 그다음 실행 파일에 해당 변경만 적용해 실제 결과와 비교한다. 나머지 실험도 원래 예제로 돌아가 하나씩 수행한다.

<details>
<summary>변경 결과와 막힐 때 확인</summary>

| 한 가지 변경 | 예상 | 이유 |
| --- | --- | --- |
| CSS높이만80px |계산80·새인라인85px |입력크기변경 |
| 두번째class를q2-2로 |q2개수1 |정확한항목비교 |
| 원래빈값검사trim만제거 |공백요소를안채움 |공백은빈문자열아님 |

style에 값이 없다고 선택 실패와 혼동하지 않는다. 높이 계산이 NaN이면 단위가 붙은 문자열을 Number로 바로 읽었는지 본다. 클래스 일부가 같아도 contains는 다른 항목이면 false다.

</details>

## 채점과 복습

| 점검 | 확인할 것 |
| --- | --- |
| 예측 | 실행 전에 출력·상태를 적었는가? |
| 근거 | 문법·조건·반환·순서로 설명했는가? |
| 수정 | 한 조건만 바꾸었는가? |
| 확인 | 실제 관찰과 코드 기준 예상을 구분했는가? |

틀린 이유를 설명할 수 없다면 [본문](../../12-03_JavaScript_DOM_스타일과_퀴즈.md)의 작은 예제·내 원본 풀이로 돌아간다. TIP의 미학습 기능은 이 문제의 필수 정답이 아니다.
