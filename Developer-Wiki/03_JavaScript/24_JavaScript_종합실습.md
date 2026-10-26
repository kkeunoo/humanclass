# JavaScript 종합실습 — 메뉴 선택과 Todo 목록

[JavaScript 목차](README.md) · [실무 코딩 스타일](23_JavaScript_실무_코딩스타일.md) · [실습 폴더](실습/README.md)

직접 만들어 본 뒤에는 [브라우저에서 확인할 수 있는 완성 예시](실습/메뉴_Todo_복습.html)와 비교한다. 이 HTML도 **새로 구성한 복습 파일**이다.

이 문제는 [폼 값](13_JavaScript_DOM_폼요소와_입력값처리.md), [이벤트 위임](17-02_JavaScript_이벤트전파와_위임.md), [강사님·내 메뉴와 Todo 코드](17-04_JavaScript_메뉴와_Todo실습.md)를 연결해 **새로 구성한 종합 연습**이다. 양쪽 원본에 이 이름의 완성 프로젝트가 있었다는 뜻은 아니다. 원본 퀴즈 문제는 기존 17장과 분리해서 읽는다.

## 만들 기능

한 HTML 화면에 `전체·할 일·완료` 메뉴, 할 일 입력 폼, Todo 목록, 남은 항목 수를 둔다.

1. 텍스트를 입력하고 제출하면 항목 하나를 추가한다. 공백만 입력하면 추가하지 않는다.
2. 각 항목은 체크박스와 삭제 버튼을 가진다. 삭제는 누른 항목만 지운다.
3. 메뉴를 누르면 **선택한 메뉴 하나만** 강조한다. 같은 메뉴를 여러 번 눌러도 표시가 누적되지 않는다.
4. 목록이 바뀔 때마다 전체 개수를 다시 표시한다. 새로고침 후 저장은 요구하지 않는다.

**성공 기준:** A·B·C를 추가하면 개수 3, B만 삭제하면 2다. 메뉴를 두 번 클릭해도 체크 기호나 글자가 중복되지 않는다. 화면 요소가 없어도 오류가 어디서 나는지 확인할 수 있게 선택자 이름을 정한다.

## 먼저 설계하기

| 입력 또는 동작 | 읽을 값 | 바꿀 대상 |
| --- | --- | --- |
| 폼 제출 | 입력의 현재 `value` | 새 `li`, 개수 표시 |
| 삭제 버튼 클릭 | 눌린 버튼의 부모 항목 | 해당 `li`, 개수 표시 |
| 메뉴 클릭 | `data-name` | 메뉴의 `selected` 클래스, 선택 이름 |

`submit` 기본 동작을 막는 것과 클릭 이벤트의 전파를 막는 것은 다르다. 어느 쪽이 필요한지 [폼 이벤트 장](17_JavaScript_폼이벤트와_이벤트전파_실전문제.md)에서 확인한 뒤 작성한다.

<details>
<summary>핵심 해설 — 직접 만들어 본 뒤 펼치기</summary>

```javascript
const form = document.querySelector('#todo-form');
const input = document.querySelector('#todo-input');
const list = document.querySelector('#todo-list');
const count = document.querySelector('#todo-count');

function updateCount() {
  count.textContent = String(list.querySelectorAll('li').length);
}

form.addEventListener('submit', (event) => {
  event.preventDefault();
  const title = input.value.trim();
  if (!title) return;

  const item = document.createElement('li');
  const label = document.createElement('span');
  const removeButton = document.createElement('button');
  label.textContent = title;
  removeButton.type = 'button';
  removeButton.textContent = '삭제';
  item.append(label, removeButton);
  list.append(item);
  input.value = '';
  updateCount();
});

list.addEventListener('click', (event) => {
  if (event.target.tagName !== 'BUTTON') return;
  event.target.parentElement.remove();
  updateCount();
});
```

위 해설은 목록 추가·삭제의 한 구현이다. 메뉴는 [실무 스타일 장](23_JavaScript_실무_코딩스타일.md)의 재구성 예제와 이어 붙여 완성한다. `innerHTML`로 사용자가 입력한 문자열을 그대로 합치지 않고 `textContent`를 사용했다.

</details>

## 확장 연습

완료 체크한 항목의 개수도 표시해 보자. 이는 체크박스와 DOM 순회로 만들 수 있다. 외부 API·브라우저 저장소를 추가하지 않아도 기본 종합실습을 마칠 수 있다.

## 추가로 알면 좋은 것

브라우저를 닫아도 목록을 유지하는 저장소 설계는 이번 양쪽 원본 실습과 분리한다. 이 문제의 완료 기준에 넣지 않는다.
