# 17-04. 메뉴와 Todo — 한 번의 조작 뒤 화면 상태를 맞추기 — 연습문제

[본문](../../17-04_JavaScript_메뉴와_Todo실습.md) · [문제 목차](README.md)

실제 수업 기능을 바탕으로 **새로 구성한 연습문제**다. 강사님 원본 퀴즈와 구분한다. 예상 → 이유 → 수정 순서로 풀고, 정답은 먼저 답한 뒤 펼친다.

## 목표와 실행 조건

한 메뉴만 강조하고 표시가 중복되지 않게 한다. Todo의 생성·개별 삭제·전체 선택·선택 삭제를 연결하며, 공통 버튼은 한 번 등록하고 현재 항목 상태를 다시 계산하는 이유를 설명한다.

[전체 실행 HTML](../책형_복습/17-04_JavaScript_메뉴와_Todo실습.html)과 같은 폴더의 JS를 함께 준비한다. Console을 열고 새로고침하면 처음부터 실행한다. 원본과 별도 파일이므로 기존 변수·타이머·출력 변경 실험의 영향을 섞지 않는다. 실제 입력·현재 시각·난수는 고정 결과와 구별한다.

입력·버튼·키보드·스크롤 예제는 [본문의 3절](../../17-04_JavaScript_메뉴와_Todo실습.md#example)에 적힌 조작 순서대로 결과를 예상한다. 통신 예제는 해당 절의 가상 JSON 파일과 로컬 웹 실행 준비가 필요하며 HTML을 직접 여는 조건과 다르다. Console 출력이 없는 문제는 화면의 값·개수·선택 상태를 답한다.

## 문제 1. 실행 순서와 결과 예상

다음은 **새 설명 예제**다. 출력 전에 어떤 값이 어떤 순서로 만들어지는지 적는다.

**필요한 HTML · 스크립트 앞:**

```html
    <ul id="menu"><li><button type="button">인기순</button></li><li><button type="button">최신순</button></li></ul>
    <label>할 일 <input id="todo"></label><button id="add" type="button">추가</button>
    <p id="warning"></p>
    <label><input id="all" type="checkbox">전체 선택</label>
    <button id="deleteSelected" type="button">선택 삭제</button>
    <div id="list"></div>
```

**필요한 CSS · head의 style:**

```css
.selected { font-weight: bold; } .selected::before { content: "✔ "; } .row { display: flex; gap: 8px; margin: 8px 0; } .done { text-decoration: line-through; }
```

```javascript
const menuButtons = document.querySelectorAll('#menu button');
for (const button of menuButtons) {
    button.addEventListener('click', function () {
        for (const item of menuButtons) item.classList.remove('selected');
        this.classList.add('selected');
    });
}
const list = document.getElementById('list');
const all = document.getElementById('all');
function syncAll() {
    const checks = list.querySelectorAll('.chk');
    const checked = list.querySelectorAll('.chk:checked');
    all.checked = checks.length > 0 && checks.length === checked.length;
}
function paintRow(check) {
    const text = check.parentNode.querySelector('span');
    if (check.checked) text.classList.add('done');
    else text.classList.remove('done');
}
document.getElementById('add').addEventListener('click', function () {
    const input = document.getElementById('todo');
    const warning = document.getElementById('warning');
    if (input.value.trim() === '') {
        warning.textContent = '한 글자 이상 입력';
        return;
    }
    warning.textContent = '';
    const row = document.createElement('div');
    row.classList.add('row');
    const check = document.createElement('input');
    check.type = 'checkbox';
    check.classList.add('chk');
    check.setAttribute('aria-label', '할 일 선택');
    const text = document.createElement('span');
    text.textContent = input.value.trim();
    const del = document.createElement('button');
    del.type = 'button';
    del.textContent = '삭제';
    del.addEventListener('click', function () {
        row.remove();
        syncAll();
    });
    check.addEventListener('click', function () {
        paintRow(check);
        syncAll();
    });
    row.append(check, text, del);
    list.prepend(row);
    input.value = '';
    syncAll();
});
all.addEventListener('click', function () {
    const checks = list.querySelectorAll('.chk');
    for (const check of checks) {
        check.checked = this.checked;
        paintRow(check);
    }
    syncAll();
});
document.getElementById('deleteSelected').addEventListener('click', function () {
    const checks = list.querySelectorAll('.chk:checked');
    for (const check of checks) check.parentNode.remove();
    syncAll();
});
```

<details>
<summary>힌트와 풀이</summary>

**힌트:** 입력·현재 상태·실행 시점·반환값을 따로 표시한다.

```text
빈 입력: 경고, 줄 0개
첫째·둘째 추가: 둘째가 위, 줄 2개
전체 선택 후 둘째 해제: 전체 선택 해제
선택 삭제: 둘째만 남음
남은 줄 삭제: 줄 0개, 전체 선택 해제
```

메뉴의 인기순을 두 번, 최신순을 한 번 눌러도 ✔가 문구에 누적되지 않고 최신순만 강조된다. 빈 입력으로 추가하면 경고만 보이고 줄은 없다. 첫째·둘째를 순서대로 추가하면 prepend 때문에 둘째가 위다. 전체 선택한 뒤 둘째만 해제하면 전체 선택도 풀린다. 선택 삭제는 체크가 남아 있는 첫째만 지운다. 남은 둘째를 개별 삭제하면 빈 목록과 전체 선택 해제가 유지된다. 이 예제는 Console 대신 화면 상태를 확인한다. 새 개선 예제이며 원본 오류를 숨겨 원래 완성 코드였던 것으로 소개하지 않는다.

</details>

## 문제 2. 개념을 자신의 말로 설명

1. 빈 값 검사는 어느 단계보다 먼저 해야 하는가?
2. 전체 선택 리스너를 추가 함수 안에서 등록하면 무엇이 누적되는가?
3. checked를 대입하면 개별 click 리스너가 자동 실행되는가?
4. 전체 0개·선택 0개일 때 왜 별도 조건을 두었는가?

<details>
<summary>풀이</summary>

요소를 만들거나 붙이기 전에 검사한다. 추가할 때마다 공통 버튼의 새 리스너가 쌓인다. checked 대입은 click을 자동 발생시키지 않는다. 빈 목록을 선택 완료로 보이지 않게 하려는 명시적인 화면 규칙 때문이다.

| 상황 | 원본에서 확인한 결과 | 개선 예제의 규칙 |
| --- | --- | --- |
| 메뉴 같은 항목 두 번 | ✔✔ 누적 | 클래스 표시 한 번 |
| 처음부터 빈 Todo | 빈 div 뒤 null 오류 | 생성 전에 종료 |
| 정상 Todo 두 개 | 각각 추가되나 j 오류 발생 | 선언된 반복 변수 사용 |
| 정상 항목 뒤 빈 Todo | 기존 삭제 버튼에 빈 줄 삭제도 연결 가능 | 빈 값은 DOM 변화 없음 |
| 항목 추가 반복 | 공통 버튼 리스너 누적 | 공통 등록 한 번 |

이번 별도 headless 브라우저 검수에서 원본의 네 상황을 확인했다. 정상 항목 두 개 뒤 예전 항목 삭제는 해당 항목을 지웠다. 따라서 “문서 전체 querySelector이므로 정상 입력에서도 언제나 틀린 버튼”이라는 기존 설명은 교정했다. 범위를 좁히는 개선의 근거와 실제 발생한 오류를 나누어 기록한다. D 드라이브 원본은 수정하지 않았다.

</details>

## 문제 3. 한 가지를 바꾸어 확인

먼저 **prepend를 append로**를 바꾸면 무엇이 달라질지 적는다. 그다음 실행 파일에 해당 변경만 적용해 실제 결과와 비교한다. 나머지 실험도 원래 예제로 돌아가 하나씩 수행한다.

<details>
<summary>변경 결과와 막힐 때 확인</summary>

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| prepend를 append로 | 첫째가 위에 남음 | 추가 위치 차이 |
| syncAll의 길이 > 0 조건 제거 | 빈 목록을 전부 체크로 계산 가능 | 0과 0도 같음 |
| 삭제 후 syncAll 제거 | 전체 선택 표시가 오래 남을 수 있음 | 화면 상태 재계산 누락 |
| paintRow 호출 제거 | 직접 checked 대입 때 취소선이 안 맞음 | 속성 변경은 click 실행이 아님 |

빈 줄이 생기면 검사보다 먼저 DOM을 바꿨는지 본다. j 오류는 실행 줄과 변수 선언 범위를 확인한다. 공통 버튼이 여러 번 반응하면 등록이 추가 콜백 안에 있는지 살핀다. 체크와 취소선이 다르면 checked 값 대입 뒤 표시 갱신까지 했는지 확인한다.

</details>

## 채점과 복습

| 점검 | 확인할 것 |
| --- | --- |
| 예측 | 실행 전에 출력·상태를 적었는가? |
| 근거 | 문법·조건·반환·순서로 설명했는가? |
| 수정 | 한 조건만 바꾸었는가? |
| 확인 | 실제 관찰과 코드 기준 예상을 구분했는가? |

틀린 이유를 설명할 수 없다면 [본문](../../17-04_JavaScript_메뉴와_Todo실습.md)의 작은 예제·내 원본 풀이로 돌아간다. TIP의 미학습 기능은 이 문제의 필수 정답이 아니다.
