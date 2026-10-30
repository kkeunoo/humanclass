# 23. 실무 코딩 스타일 — 읽기 좋은 이름보다 먼저 동작의 책임 나누기 — 연습문제

[본문](../../23_JavaScript_실무_코딩스타일.md) · [문제 목차](README.md)

실제 수업 기능을 바탕으로 **새로 구성한 연습문제**다. 강사님 원본 퀴즈와 구분한다. 예상 → 이유 → 수정 순서로 풀고, 정답은 먼저 답한 뒤 펼친다.

## 목표와 실행 조건

입력 검사 전에 화면을 바꾸지 않고, 함수 이름에서 하는 일을 찾을 수 있게 구성한다. 필요한 DOM 범위만 다루고, 수정 후에도 확인할 동작 목록을 만든다. 팀의 취향과 실제 오류를 구분한다.

[전체 실행 HTML](../책형_복습/23_JavaScript_실무_코딩스타일.html)과 같은 폴더의 JS를 함께 준비한다. Console을 열고 새로고침하면 처음부터 실행한다. 원본과 별도 파일이므로 기존 변수·타이머·출력 변경 실험의 영향을 섞지 않는다. 실제 입력·현재 시각·난수는 고정 결과와 구별한다.

입력·버튼·키보드·스크롤 예제는 [본문의 3절](../../23_JavaScript_실무_코딩스타일.md#example)에 적힌 조작 순서대로 결과를 예상한다. 통신 예제는 해당 절의 가상 JSON 파일과 로컬 웹 실행 준비가 필요하며 HTML을 직접 여는 조건과 다르다. Console 출력이 없는 문제는 화면의 값·개수·선택 상태를 답한다.

## 문제 1. 실행 순서와 결과 예상

다음은 **새 설명 예제**다. 출력 전에 어떤 값이 어떤 순서로 만들어지는지 적는다.

**필요한 HTML · 스크립트 앞:**

```html
    <form id="todoForm"><label>할 일 <input id="todoInput"></label><button type="submit">추가</button></form>
    <p id="warning"></p><p>현재 항목 <span id="count">0</span>개</p><ul id="list"></ul>
```

```javascript
const form = document.getElementById('todoForm');
const input = document.getElementById('todoInput');
const list = document.getElementById('list');
const count = document.getElementById('count');
const warning = document.getElementById('warning');
function updateCount() {
    count.textContent = list.querySelectorAll('li').length;
}
form.addEventListener('submit', function (event) {
    event.preventDefault();
    const title = input.value.trim();
    if (title === '') {
        warning.textContent = '내용을 입력하세요';
        return;
    }
    warning.textContent = '';
    const row = document.createElement('li');
    const text = document.createElement('span');
    text.textContent = title;
    const removeButton = document.createElement('button');
    removeButton.type = 'button';
    removeButton.textContent = '삭제';
    removeButton.addEventListener('click', function () {
        row.remove();
        updateCount();
    });
    row.append(text, removeButton);
    list.append(row);
    input.value = '';
    updateCount();
});
```

<details>
<summary>힌트와 풀이</summary>

**힌트:** 입력·현재 상태·실행 시점·반환값을 따로 표시한다.

```text
공백 제출 → 경고·0개
A·B 추가 → 2개
A 삭제 → B만 남고 1개
```

공백으로 제출한 뒤 A·B를 추가하고 A를 삭제한다. DOM을 바꾸기 전에 검사하므로 첫 실패는 빈 li도 만들지 않는다. 추가 뒤와 삭제 뒤 모두 updateCount를 호출하여 현재 li 수를 표시한다. 제목 글자는 textContent로 넣는다. 삭제 버튼은 생성한 removeButton에 직접 등록하므로 다른 항목을 문서 전체에서 다시 찾지 않는다. 이 코드의 구조는 새 연습이며 수업 원본을 몰래 덮어쓴 결과가 아니다.

</details>

## 문제 2. 개념을 자신의 말로 설명

1. 검사식이 있어도 빈 줄이 생길 수 있는 이유는?
2. updateCount는 왜 두 곳에서 호출하는가?
3. 세미콜론을 통일하면 j 미선언 오류도 해결되는가?

<details>
<summary>풀이</summary>

검사보다 먼저 DOM을 바꾸면 실패해도 흔적이 남는다. 추가·삭제 모두 항목 수를 바꾸므로 같은 규칙을 호출한다. 형식 통일과 변수 선언 오류는 별개다.

| 확인 항목 | 기대하는 동작 | 실패하면 볼 위치 |
| --- | --- | --- |
| 공백 제출 | DOM 변화 없음 | 검사와 생성 순서 |
| 항목 두 개 추가 | 서로 다른 두 줄 | 요소 생성 위치 |
| 첫 항목 삭제 | 해당 줄만 삭제 | 참조한 row |
| 삭제 뒤 개수 | 실제 목록과 일치 | updateCount 호출 |
| 연속 추가 | 제출당 한 번 추가 | 폼 등록 위치 |

실무에서도 “한 번 실행됐는가”만 확인하지 않는다. 빈 입력·반복 입력·삭제 뒤 상태처럼 이전 동작이 남기는 영향을 함께 확인한다. 이 표는 이번 작은 화면에 필요한 회귀 확인 목록이며 모든 프로젝트에 같은 항목 수의 검사를 강요하는 규칙은 아니다.

</details>

## 문제 3. 한 가지를 바꾸어 확인

먼저 **삭제 뒤 updateCount 제거**를 바꾸면 무엇이 달라질지 적는다. 그다음 실행 파일에 해당 변경만 적용해 실제 결과와 비교한다. 나머지 실험도 원래 예제로 돌아가 하나씩 수행한다.

<details>
<summary>변경 결과와 막힐 때 확인</summary>

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| 삭제 뒤 updateCount 제거 | 목록과 개수가 어긋남 | 화면 요약 갱신 누락 |
| 검사 전에 list.append 이동 | 빈 줄이 남을 수 있음 | 실패 전 부수 효과 |
| textContent 대신 입력을 innerHTML에 넣기 | 태그 모양 글자의 해석 차이 | 글자와 HTML 구분 |

함수가 많아져도 어떤 효과가 있는지 모르면 이름과 호출 지점을 다시 적는다. 삭제 대상이 다르면 선택 범위를 좁히거나 생성한 요소 참조를 사용한다. 코드 형식을 정리한 뒤에도 동일 조작 순서로 결과를 확인해야 실제 동작 보존을 판단할 수 있다.

</details>

## 채점과 복습

| 점검 | 확인할 것 |
| --- | --- |
| 예측 | 실행 전에 출력·상태를 적었는가? |
| 근거 | 문법·조건·반환·순서로 설명했는가? |
| 수정 | 한 조건만 바꾸었는가? |
| 확인 | 실제 관찰과 코드 기준 예상을 구분했는가? |

틀린 이유를 설명할 수 없다면 [본문](../../23_JavaScript_실무_코딩스타일.md)의 작은 예제·내 원본 풀이로 돌아간다. TIP의 미학습 기능은 이 문제의 필수 정답이 아니다.
