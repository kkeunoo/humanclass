# JavaScript 종합실습 — 메뉴 선택과 Todo 목록

[JavaScript 목차](README.md) · [실무 코딩 스타일](23_JavaScript_실무_코딩스타일.md) · [실습 폴더](실습/README.md)

이 문제는 [폼 값](13_JavaScript_DOM_폼요소와_입력값처리.md), [이벤트 위임](17-02_JavaScript_이벤트전파와_위임.md), [강사님·내 메뉴와 Todo 코드](17-04_JavaScript_메뉴와_Todo실습.md)를 연결해 **새로 구성한 종합 연습**이다. 양쪽 원본에 이 이름의 완성 프로젝트가 있었다는 뜻은 아니다. 원본 퀴즈 문제는 기존 17장과 분리해서 읽는다.

**이 연습의 핵심:** 항목을 추가하거나 지울 때마다 현재 화면의 항목 수를 다시 센다. 예를 들어 A·B를 만든 뒤 B를 지우면 남은 항목은 A 하나이고 표시할 개수는 `1`이다. 이 결과를 확인한 뒤 메뉴 선택과 완료 상태까지 연결한다.

| 17-04 수업 원본 | 실제로 확인한 상태 | 이번 종합실습에 적용할 점 |
| --- | --- | --- |
| 강사님 메뉴 | 이전 `bold`를 지우고 하나만 강조 | 선택 전에 이전 표시 제거 |
| 내 메뉴 | 같은 항목을 다시 누르면 `✔`가 누적 | 글자 추가 대신 클래스 사용 |
| 강사님 Todo | 새 항목을 위에 붙이고 항목별 삭제 연결 | 생성한 항목에서 버튼 선택 |
| 내 Todo | 빈 입력에서 빈 `div`가 남고 오류 발생 | 입력 검사 후 요소 만들기 |

## 만들 기능

한 HTML 화면에 `전체·할 일·완료` 보기 메뉴, 할 일 입력 폼, Todo 목록, **전체 항목 수**를 둔다. 메뉴는 선택 표시만 바꾸는 것이 아니라 현재 보기에 맞는 항목을 보여 준다.

1. 텍스트를 입력하고 제출하면 항목 하나를 추가한다. 공백만 입력하면 추가하지 않는다.
2. 각 항목은 체크박스와 삭제 버튼을 가진다. 삭제는 누른 항목만 지운다.
3. 체크박스를 바꾸면 완료 상태가 달라지고, `할 일` 보기에서는 미완료만, `완료` 보기에서는 완료만 보인다.
4. 메뉴를 누르면 **선택한 메뉴 하나만** 강조한다. 같은 메뉴를 여러 번 눌러도 표시가 누적되지 않는다.
5. 목록이 바뀔 때마다 **숨긴 항목도 포함한 전체 개수**를 다시 표시한다. 새로고침 후 저장은 요구하지 않는다.

**성공 기준:** A·B·C를 추가하면 전체 개수 3, B만 삭제하면 2다. A를 완료로 체크한 뒤 `할 일`을 고르면 C만, `완료`를 고르면 A만 보인다. 보기만 바꿔도 전체 개수는 2다. 메뉴를 두 번 클릭해도 선택 표시가 중복되지 않는다.

## 먼저 설계하기

| 입력 또는 동작 | 읽을 값 | 바꿀 대상 |
| --- | --- | --- |
| 폼 제출 | 입력의 현재 `value` | 새 `li`, 개수 표시 |
| 삭제 버튼 클릭 | 눌린 버튼의 부모 항목 | 해당 `li`, 개수 표시 |
| 체크박스 변경 | 현재 `checked` | 항목의 완료 표시와 현재 보기 |
| 메뉴 클릭 | `data-name` | 메뉴의 `selected` 클래스, 보이는 항목 |

`submit` 기본 동작을 막는 것과 클릭 이벤트의 전파를 막는 것은 다르다. 어느 쪽이 필요한지 [폼 이벤트 장](17_JavaScript_폼이벤트와_이벤트전파_실전문제.md)에서 확인한 뒤 작성한다.

<details>
<summary>핵심 해설 — 직접 만들어 본 뒤 펼치기</summary>

```javascript
const form = document.querySelector('#todo-form');
const input = document.querySelector('#todo-input');
const list = document.querySelector('#todo-list');
const count = document.querySelector('#todo-count');
const menu = document.querySelector('#menu');
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

form.addEventListener('submit', (event) => {
  event.preventDefault();
  const title = input.value.trim();
  if (!title) return;

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

menu.addEventListener('click', (event) => {
  const button = event.target;
  if (!button.hasAttribute('data-name')) return;
  menu.querySelectorAll('button').forEach((item) => item.classList.remove('selected'));
  button.classList.add('selected');
  currentView = button.dataset.name;
  refresh();
});
```

위 해설은 추가·삭제·완료·보기 변경의 핵심 JavaScript다. HTML에는 위 선택자와 일치하는 `#todo-form`, `#todo-input`, `#todo-list`, `#todo-count`, `#menu`가 필요하다. 전체 HTML은 [실행용 파일](실습/메뉴_Todo_복습.html)에 있다. 사용자 입력 문자열은 `innerHTML`에 이어 붙이지 않고 `textContent`로 넣는다.

</details>

직접 만든 뒤에는 [브라우저에서 실행할 수 있는 완성 예시](실습/메뉴_Todo_복습.html)와 비교한다. 이 HTML도 **새로 구성한 복습 파일**이며 원본 수업 코드가 아니다.

## 확장 연습

완료 체크한 항목의 개수도 표시해 보자. 이는 체크박스와 DOM 순회로 만들 수 있다. 외부 API·브라우저 저장소를 추가하지 않아도 기본 종합실습을 마칠 수 있다.

## 추가로 알면 좋은 것

브라우저를 닫아도 목록을 유지하는 저장소 설계는 이번 양쪽 원본 실습과 분리한다. 이 문제의 완료 기준에 넣지 않는다.
