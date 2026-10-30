# JavaScript 종합실습 — 메뉴·입력·목록을 연결하는 작은 앱

[과목 목차](README.md) · [실무 스타일](23_JavaScript_실무_코딩스타일.md) · [전체 실행 HTML](실습/메뉴_Todo_복습.html)

이 장은 원본의 별도 24번 수업 프로젝트가 아니라, 실제 배운 폼·DOM·이벤트·클래스·dataset을 연결해 새로 만든 종합 연습이다. 먼저 요구사항을 읽고 작성한 뒤 아래 해설을 펼친다. 실제 수업 퀴즈와 당시 내 풀이 비교는 [17-04](17-04_JavaScript_메뉴와_Todo실습.md)에 있다.

## 1. 목표와 먼저 알아야 할 것

조건문·배열 순회·함수·DOM 생성·value와 checked·submit·이벤트 위임을 연결한다. [13장](13_JavaScript_DOM_폼요소와_입력값처리.md), [17장](17_JavaScript_폼이벤트와_이벤트전파_실전문제.md), [17-02](17-02_JavaScript_이벤트전파와_위임.md)를 먼저 읽는다. 화면을 만들 수 있을 뿐 아니라 어떤 조작 뒤 왜 그 항목이 보이는지 설명하는 것이 목표다.

## 2. 만들 화면과 성공 기준

전체·할 일·완료 보기, 할 일 입력 폼, 목록, 전체 개수 표시를 만든다. 공백만 제출하면 경고를 보이고 항목을 만들지 않는다. 한 번 제출하면 한 줄만 추가한다. 체크는 완료 상태, 삭제는 해당 항목 제거다. 메뉴는 선택 하나만 강조하며 현재 보기에 맞게 숨기고 보여 준다.

| 동작 | 기대 결과 |
| --- | --- |
| A·B·C 추가 | 순서대로 세 항목, 전체 3 |
| B 삭제 | A·C, 전체 2 |
| A 체크 뒤 할 일 보기 | C만 보임, 전체 2 |
| 완료 보기 | A만 보임, 전체 2 |
| 완료 보기에서 A 삭제 | C는 숨겨진 채 남음, 전체 1 |
| 전체 보기 | C가 다시 보임 |

전체 개수는 숨긴 항목도 포함한다. 보기 변경은 삭제가 아니다. 저장 기능은 요구하지 않으며 새로고침하면 초기화된다.

## 3. 설계 — 입력·상태·화면을 나누기

| 정보 | 보관·조회 위치 | 갱신 시점 |
| --- | --- | --- |
| 입력 제목 | input.value.trim() | 제출 순간 |
| 현재 보기 | currentView 문자열 | 메뉴 클릭 |
| 완료 여부 | 각 체크박스.checked | 체크 변경 |
| 항목 수 | 현재 li 목록 길이 | refresh 호출 |

refresh는 현재 목록을 다시 조회하여 개수·취소선·표시 여부를 맞춘다. 항목을 추가하거나 삭제한 뒤, 체크나 보기를 바꾼 뒤 같은 함수를 호출한다. 메뉴의 data-name은 화면 이름과 실제 조건 문자열을 연결한다. 버튼 안에 별도 자식 태그가 없는 현재 HTML을 가정한다.

## 4. 작은 흐름으로 먼저 예측하기

```text
A(완료), C(미완료), currentView='active'
  → A는 none, C는 기본 표시
  → 목록에는 두 li가 있으므로 전체 개수 2
```

표시 여부 조건은 `(할 일 보기이고 완료됨) 또는 (완료 보기이고 미완료)`일 때 숨긴다는 뜻이다. 두 조건 사이의 OR와 각 조건 안의 AND를 말로 먼저 읽는다. CSS로 숨긴 요소가 DOM에서도 삭제됐다고 생각하지 않는다.

## 5. 전체 실행 파일과 함수 풀이

위 [전체 실행 HTML](실습/메뉴_Todo_복습.html)을 브라우저에서 연다. 외부 호출이 없고 원본 폴더의 파일도 필요하지 않다. 아래 HTML을 body에, CSS를 head의 style에, JavaScript를 body 마지막 script에 넣으면 같은 구조다.

<details>
<summary>HTML·CSS·JavaScript 전체와 해설</summary>

```html
<h1>메뉴와 Todo 복습</h1>
  <p>수업에서 배운 폼, DOM, 이벤트 위임, <code>dataset</code>을 연결한 새 연습 예시입니다. 원본 제출 코드가 아닙니다.</p>
  <ul id="menu">
    <li><button type="button" data-name="all" class="selected">전체</button></li>
    <li><button type="button" data-name="active">할 일</button></li>
    <li><button type="button" data-name="done">완료</button></li>
  </ul>
  <p>현재 보기: <strong id="selected-name">전체</strong></p>
  <form id="todo-form">
    <label for="todo-input">할 일</label>
    <input id="todo-input" name="todo">
    <button type="submit">추가</button>
  </form>
  <p id="todo-warning"></p>
  <p>전체 항목: <strong id="todo-count">0</strong></p>
  <ul id="todo-list"></ul>
```

```css
body { font-family: sans-serif; max-width: 38rem; margin: 2rem auto; padding: 0 1rem; line-height: 1.5; }
#menu { display: flex; gap: .5rem; padding: 0; list-style: none; }
#menu button { padding: .4rem .8rem; }
#menu button.selected { background: #163d6b; color: white; }
#todo-list { padding-left: 1.5rem; }
#todo-list li { margin: .5rem 0; }
#todo-list li.done span { text-decoration: line-through; }
```

```javascript
const menu = document.querySelector('#menu');
const selectedName = document.querySelector('#selected-name');
const form = document.querySelector('#todo-form');
const input = document.querySelector('#todo-input');
const list = document.querySelector('#todo-list');
const count = document.querySelector('#todo-count');
let currentView = 'all';

function refresh() {
  const items = list.querySelectorAll('li');
  count.textContent = items.length;
  items.forEach((item) => {
    const done = item.querySelector('.todo-check').checked;
    if (done) item.classList.add('done');
    else item.classList.remove('done');
    if (currentView === 'active' && done || currentView === 'done' && !done) {
      item.style.display = 'none';
    } else {
      item.style.display = '';
    }
  });
}

menu.addEventListener('click', (event) => {
  const button = event.target;
  if (!button.hasAttribute('data-name')) return;
  menu.querySelectorAll('button').forEach((item) => item.classList.remove('selected'));
  button.classList.add('selected');
  currentView = button.dataset.name;
  selectedName.textContent = button.textContent;
  refresh();
});

form.addEventListener('submit', (event) => {
  event.preventDefault();
  const title = input.value.trim();
  const warning = document.querySelector('#todo-warning');
  if (!title) {
    warning.textContent = '할 일을 입력하세요';
    return;
  }
  warning.textContent = '';
  const item = document.createElement('li');
  const checkbox = document.createElement('input');
  const checkboxLabel = document.createElement('label');
  const label = document.createElement('span');
  const removeButton = document.createElement('button');
  checkbox.type = 'checkbox';
  checkbox.classList.add('todo-check');
  label.textContent = title;
  removeButton.type = 'button';
  removeButton.classList.add('todo-delete');
  removeButton.textContent = '삭제';
  checkboxLabel.append(checkbox, ' ', label);
  item.append(checkboxLabel, ' ', removeButton);
  list.append(item);
  input.value = '';
  refresh();
});

list.addEventListener('change', (event) => {
  if (event.target.classList.contains('todo-check')) refresh();
});
list.addEventListener('click', (event) => {
  if (!event.target.classList.contains('todo-delete')) return;
  event.target.parentElement.remove();
  refresh();
});
```

submit 함수는 기본 제출을 막고 검사 후에만 요소를 만든다. 제목은 span의 textContent에 넣고 체크박스·글자를 label로 묶어 클릭 범위를 연결한다. 목록의 change 리스너는 체크 상태가 바뀌면 refresh를 호출한다. click 리스너는 삭제 버튼인지 확인한 뒤 해당 li를 제거한다. 메뉴는 기존 selected를 모두 지우고 현재 버튼만 표시한 뒤 currentView를 바꾸어 refresh를 호출한다.

함수 선언만으로 화면이 바뀌는 것이 아니다. 위 네 동작에서 호출한 refresh가 현재 DOM과 currentView를 읽어 결과를 만든다. 삭제 버튼에 type=button을 명시하여 제출 버튼 역할과 구분했다.

</details>

## 6. 직접 확인할 실험과 결과

위 성공 기준을 순서대로 확인하고 같은 메뉴를 두 번 눌러도 표시가 중복되지 않는지 본다. 공백 제출은 항목 수를 바꾸지 않아야 한다. `<b>복습</b>`를 입력하면 굵은 태그가 아니라 글자 자체로 보여야 한다. 이 점은 textContent를 사용했기 때문이다.

| 한 가지만 변경 | 예상 |
| --- | --- |
| 삭제 뒤 refresh 제거 | 개수 표시가 이전 값으로 남을 수 있음 |
| 숨김을 remove로 변경 | 전체 보기로 돌아가도 항목이 복구되지 않음 |
| 검사보다 생성 먼저 실행 | 빈 항목이 남을 수 있음 |
| 현재 보기 초기값 변경 | 메뉴 표시도 함께 맞춰야 상태 일치 |

## 7. 원본에서 가져온 점과 주의점

강사님 메뉴의 이전 강조 제거, 내 Todo의 빈 값 검사·취소선 의도를 살린 새 구성이다. 원본의 공통 리스너 누적·j 미선언·빈 입력 뒤 DOM 변경은 가져오지 않았다. 항목별 생성 코드와 목록의 위임 처리 역할을 분명히 했다.

이 예제는 화면 상태를 연결하는 작은 복습이다. 대량 목록 최적화나 영구 저장까지 완성한 앱은 아니다. 새로운 도구를 쓰지 않아도 배운 개념을 조합하여 동작 규칙을 유지할 수 있다는 점을 확인한다.

## 8. 문제와 복습·다음 학습

1. A를 숨겨도 전체 수가 줄지 않는 이유를 설명한다.
2. B 삭제 뒤 count가 3으로 남았다면 어떤 함수 호출을 먼저 확인할까?
3. 전체 보기에서 완료 항목의 취소선도 유지되려면 어느 조건과 독립적으로 처리해야 할까?
4. 선택 메뉴를 바꾸어도 입력 중 글자가 사라지지 않아야 하는 이유를 설명한다.

<details>
<summary>풀이와 채점 기준</summary>

숨김은 DOM 삭제가 아니므로 목록 길이는 같다. 삭제 뒤 refresh 호출을 본다. 취소선은 checked를 기준으로, 표시 여부는 checked와 currentView를 기준으로 따로 계산한다. 메뉴 함수가 입력 칸을 초기화할 필요는 없다. 답만 맞히는 것보다 어떤 값·요소·호출이 그 결과를 만드는지 설명했는지 확인한다.

</details>

> 💡 **TIP · 수업 범위 밖:** 새로고침 뒤 저장, 서버 동기화, 키보드 중심의 상세 접근성·복잡한 동적 자식의 위임 처리는 다음 단계다. 기본 정답에 해당 기능을 필수로 요구하지 않는다.

📚 **출처 · 본문 설명 확인:** [MDN 이벤트 버블링](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Event_bubbling). 실습과 풀이 자체는 수업 문법을 바탕으로 새로 구성했다.

[장별 문제로 돌아가기](실습/연습문제/README.md) · [과목 목차](README.md)
