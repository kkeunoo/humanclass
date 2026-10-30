# 17-02. 이벤트 전파와 위임 — 자식 클릭을 부모가 처리하는 이유 — 연습문제

[본문](../../17-02_JavaScript_이벤트전파와_위임.md) · [문제 목차](README.md)

실제 수업 기능을 바탕으로 **새로 구성한 연습문제**다. 강사님 원본 퀴즈와 구분한다. 예상 → 이유 → 수정 순서로 풀고, 정답은 먼저 답한 뒤 펼친다.

## 목표와 실행 조건

target·currentTarget을 구별하고 버블링 경로를 설명한다. 전파 중단과 기본 동작 취소를 나누며, 표와 행의 중복 처리·체크박스의 독립 처리를 추적한다.

[전체 실행 HTML](../책형_복습/17-02_JavaScript_이벤트전파와_위임.html)과 같은 폴더의 JS를 함께 준비한다. Console을 열고 새로고침하면 처음부터 실행한다. 원본과 별도 파일이므로 기존 변수·타이머·출력 변경 실험의 영향을 섞지 않는다. 실제 입력·현재 시각·난수는 고정 결과와 구별한다.

입력·버튼·키보드·스크롤 예제는 [본문의 3절](../../17-02_JavaScript_이벤트전파와_위임.md#example)에 적힌 조작 순서대로 결과를 예상한다. 통신 예제는 해당 절의 가상 JSON 파일과 로컬 웹 실행 준비가 필요하며 HTML을 직접 여는 조건과 다르다. Console 출력이 없는 문제는 화면의 값·개수·선택 상태를 답한다.

## 문제 1. 실행 순서와 결과 예상

다음은 **새 설명 예제**다. 출력 전에 어떤 값이 어떤 순서로 만들어지는지 적는다.

**필요한 HTML · 스크립트 앞:**

```html
    <div id="parent">
        <button id="child1" type="button">전파 중단</button>
        <button id="child2" type="button">부모로 전달</button>
    </div>
    <table id="board"><tbody><tr>
        <td><input class="chk" type="checkbox" value="1" aria-label="첫 글 선택"></td>
        <td class="title">제목1</td><td writer="w1">작성자1</td>
    </tr></tbody></table>
```

```javascript
document.getElementById('parent').addEventListener('click', function (event) {
    console.log('부모', event.target.id, event.currentTarget.id);
});
document.getElementById('child1').addEventListener('click', function (event) {
    event.stopPropagation();
    console.log('자식1');
});
const board = document.getElementById('board');
board.addEventListener('click', function (event) {
    if (event.target.classList.contains('title')) {
        console.log('제목', event.target.textContent);
    }
    if (event.target.hasAttribute('writer')) {
        console.log('작성자', event.target.getAttribute('writer'));
    }
});
board.querySelector('input.chk').addEventListener('click', function (event) {
    event.stopPropagation();
    const row = this.parentNode.parentNode;
    console.log('체크', this.checked, row.querySelector('.title').textContent);
});
```

<details>
<summary>힌트와 풀이</summary>

**힌트:** 입력·현재 상태·실행 시점·반환값을 따로 표시한다.

```text
자식1
부모 child2 parent
제목 제목1
작성자 w1
체크 true 제목1
체크 false 제목1
```

전파 중단 버튼, 부모로 전달 버튼, 제목, 작성자를 차례로 누르고 체크박스를 두 번 누른다. 자식1은 부모 출력을 만들지 않는다. 자식2의 클릭은 부모가 받지만 target은 child2이고 currentTarget은 parent다. 체크박스의 전파만 막았으므로 체크와 해제는 계속 일어나며 두 번 모두 제목을 출력한다. 새 예제는 표 한 곳에 위임을 모으고 checked 관찰을 추가한 설명 예제다. 원본의 이중 등록을 그대로 둔 결과와 다르다.

</details>

## 문제 2. 개념을 자신의 말로 설명

1. 자식2를 누른 부모 리스너의 target과 currentTarget은?
2. 내 원본에서 제목이 두 번 출력되는 이유는?
3. 체크박스의 전파 중단은 체크 전환도 막는가?

<details>
<summary>풀이</summary>

child2와 parent다. tr과 table의 두 리스너가 같은 클릭 경로에서 처리하기 때문이다. stopPropagation은 기본 체크 전환을 취소하지 않는다.

| 클릭 | 내 원본에서 실행 | 구별할 것 |
| --- | --- | --- |
| 자식1 | 자식1 리스너 | 부모로 전파 중단 |
| 자식2 | 부모 리스너 | target은 자식2로 유지 |
| 제목 | 행 → 표 | 같은 제목이 두 번 기록 |
| 체크박스 | 체크박스 리스너 | 기본 체크 전환은 유지 |

전파 중단은 이미 실행한 상위 캡처 리스너의 일을 되돌리지 않는다. 같은 요소의 다른 리스너를 모두 지우는 호출도 아니다. title 안에 별도 자식 태그가 생기면 실제 target의 클래스가 title이 아닐 수 있으므로 단순한 현재 표에서 관찰한 결과를 복잡한 구조까지 확대하지 않는다.

</details>

## 문제 3. 한 가지를 바꾸어 확인

먼저 **자식1의 stopPropagation 제거**를 바꾸면 무엇이 달라질지 적는다. 그다음 실행 파일에 해당 변경만 적용해 실제 결과와 비교한다. 나머지 실험도 원래 예제로 돌아가 하나씩 수행한다.

<details>
<summary>변경 결과와 막힐 때 확인</summary>

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| 자식1의 stopPropagation 제거 | 자식1 다음 부모 출력 | 버블링 경로 유지 |
| 원본 table 등록만 제거 | 제목 중복이 한 번으로 줄음 | tr 등록은 남아 있음 |
| 체크 콜백에 this.checked 조건 추가 | 체크할 때만 제목 출력 | 해제 상태를 제외 |

한 번 눌렀는데 두 번 나오면 경로의 등록 대상을 확인한다. 제목이 안 잡히면 target이 실제로 어떤 요소인지 본다. this가 기대와 다르면 일반 함수인지 화살표 함수인지와 주변 this를 확인한다. 체크가 계속 바뀌는 것은 stopPropagation의 실패가 아니라 기본 동작을 취소하지 않은 결과다.

</details>

## 채점과 복습

| 점검 | 확인할 것 |
| --- | --- |
| 예측 | 실행 전에 출력·상태를 적었는가? |
| 근거 | 문법·조건·반환·순서로 설명했는가? |
| 수정 | 한 조건만 바꾸었는가? |
| 확인 | 실제 관찰과 코드 기준 예상을 구분했는가? |

틀린 이유를 설명할 수 없다면 [본문](../../17-02_JavaScript_이벤트전파와_위임.md)의 작은 예제·내 원본 풀이로 돌아간다. TIP의 미학습 기능은 이 문제의 필수 정답이 아니다.
