# 12-02. 요소 생성과 삽입 — 만들기·채우기·연결하기 — 연습문제

[본문](../../12-02_JavaScript_DOM_요소생성과_삽입.md) · [문제 목차](README.md)

실제 수업 기능을 바탕으로 **새로 구성한 연습문제**다. 강사님 원본 퀴즈와 구분한다. 예상 → 이유 → 수정 순서로 풀고, 정답은 먼저 답한 뒤 펼친다.

## 목표와 실행 조건

요소 생성·연결·이동을 구분한다. 자식 앞뒤와 형제 앞뒤를 비교하고 배열의 한 행이 tr·td로 만들어지는 과정을 설명한다.

[전체 실행 HTML](../책형_복습/12-02_JavaScript_DOM_요소생성과_삽입.html)과 같은 폴더의 JS를 함께 준비한다. Console을 열고 새로고침하면 처음부터 실행한다. 원본과 별도 파일이므로 기존 변수·타이머·출력 변경 실험의 영향을 섞지 않는다. 실제 입력·현재 시각·난수는 고정 결과와 구별한다.

입력·버튼·키보드·스크롤 예제는 [본문의 3절](../../12-02_JavaScript_DOM_요소생성과_삽입.md#example)에 적힌 조작 순서대로 결과를 예상한다. 통신 예제는 해당 절의 가상 JSON 파일과 로컬 웹 실행 준비가 필요하며 HTML을 직접 여는 조건과 다르다. Console 출력이 없는 문제는 화면의 값·개수·선택 상태를 답한다.

## 문제 1. 실행 순서와 결과 예상

다음은 **새 설명 예제**다. 출력 전에 어떤 값이 어떤 순서로 만들어지는지 적는다.

**필요한 HTML · 스크립트 앞:**

```html
    <div id="log"></div>
    <table>
        <thead><tr><th>제목</th><th>작성자</th></tr></thead>
        <tbody id="board"></tbody>
    </table>
```

```javascript
const log = document.getElementById('log');
const item = document.createElement('p');
item.textContent = '새 문장';
log.append(item);
log.append('<b>글자</b>');
log.append(item);
console.log(log.querySelectorAll('p').length);
console.log(log.textContent);
const rows = [['제목1', '작성자1'], ['제목2', '작성자2']];
const board = document.getElementById('board');
for (let i = 0; i < rows.length; i++) {
    const tr = document.createElement('tr');
    const title = document.createElement('td');
    const writer = document.createElement('td');
    title.textContent = rows[i][0];
    writer.textContent = rows[i][1];
    tr.append(title);
    tr.append(writer);
    board.append(tr);
}
console.log(board.querySelectorAll('tr').length);
console.log(board.querySelectorAll('tr')[0].querySelector('td').textContent);
console.log(board.querySelectorAll('tr')[1].querySelector('td').textContent);
```

<details>
<summary>힌트와 풀이</summary>

**힌트:** 입력·현재 상태·실행 시점·반환값을 따로 표시한다.

```text
1
<b>글자</b>새 문장
2
제목1
제목2
```

item을 두 번 붙여도 p는 하나다. 문자열을 붙인 뒤 같은item을 다시 끝으로 옮겨 글자 순서가 태그 모양 문자열 → 새 문장이 된다. 표는 두 행을 새로 만들어 순서대로 연결한다. 데이터와 부모 요소를 함께 준비한 전체 스크립트이므로 숨은 rows 선언이 없다.

</details>

## 문제 2. 개념을 자신의 말로 설명

1. createElement만 하면 문서 화면에 연결되는가?
2. 같은 요소를 두 번 append하면 몇 개인가?
3. before는 첫 자식에 넣는가?

<details>
<summary>풀이</summary>

아직 연결되지 않는다. 같은 객체 하나가 이동한다. before는 이전 형제이며 첫 자식은 prepend다.

| 원본 위치·방식 | 최종 순서 |
| --- | --- |
| board에 행 append |제목1→제목2→…→제목5 |
| board2의 html+기존HTML |제목5→…→제목2→제목1 |
| str=i+str를0~4반복 |43210 |
| 같은요소두번append |한개가끝으로이동 |

문자열을 앞에 붙이는 것은 기존 요소 자체를 prepend하는 것과 다르다. innerHTML 대입은 기존 내용을 다시 해석해 교체한다. 결과 모양이 같아도 기존 자식 객체를 그대로 이동한 작업과 구분한다. appendChild에 문자열을 넣는 원본 줄은 주석이며 켜면 TypeError다.

</details>

## 문제 3. 한 가지를 바꾸어 확인

먼저 **board.append만prepend로**를 바꾸면 무엇이 달라질지 적는다. 그다음 실행 파일에 해당 변경만 적용해 실제 결과와 비교한다. 나머지 실험도 원래 예제로 돌아가 하나씩 수행한다.

<details>
<summary>변경 결과와 막힐 때 확인</summary>

| 한 가지 변경 | 예상 | 이유 |
| --- | --- | --- |
| board.append만prepend로 |표제목2→제목1 |매회앞에삽입 |
| item의마지막append만제거 |새문장→태그모양글자 |재이동없음 |
| rows에한행추가 |표3행 |length만큼반복 |

만든 요소가 안 보이면 부모에 연결했는지 확인한다. 두 번 붙였는데 개수가 늘지 않으면 같은 객체인지 본다. 위치가 엉뚱하면 자식 앞·뒤인지 형제 앞·뒤인지 나누어 그린다. 표는 tr·td의 부모를 확인한다.

</details>

## 채점과 복습

| 점검 | 확인할 것 |
| --- | --- |
| 예측 | 실행 전에 출력·상태를 적었는가? |
| 근거 | 문법·조건·반환·순서로 설명했는가? |
| 수정 | 한 조건만 바꾸었는가? |
| 확인 | 실제 관찰과 코드 기준 예상을 구분했는가? |

틀린 이유를 설명할 수 없다면 [본문](../../12-02_JavaScript_DOM_요소생성과_삽입.md)의 작은 예제·내 원본 풀이로 돌아간다. TIP의 미학습 기능은 이 문제의 필수 정답이 아니다.
