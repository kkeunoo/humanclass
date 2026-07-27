---
title: JavaScript 이벤트와 폼
category: JavaScript
last_updated: 2026-07-27
version: v4
status: Active
---

# JavaScript 이벤트와 폼

> [!IMPORTANT]
> **핵심 목표**  
> 이 문서는 수업 범위 안에서 `이벤트와 폼`의 개념, 사용 이유, 기본 문법, 예제, 실수 사례와 복습 질문을 한 번에 학습하도록 구성한다.

| 항목 | 내용 |
|---|---|
| 난이도 | ★★☆☆☆ |
| 예상 학습 시간 | 20~35분 |
| 이전 학습 | `JS_Date` |
| 다음 학습 | `JS_External_API` |
| 문서 버전 | v4 · 2026-07-27 |

---

## 이번 문서에서 배우는 것

- `이벤트와 폼`이 무엇인지 자신의 말로 설명한다.
- 기본 문법을 읽고 실행 결과를 예상한다.
- 예제에서 입력 → 처리 → 출력의 흐름을 찾는다.
- 자주 발생하는 실수를 보고 원인을 설명한다.
- 수업 문제를 스스로 분석한 뒤 풀이와 비교한다.

## 왜 이 내용을 배우는가?

사용자가 클릭하고 입력하고 제출하는 순간을 JavaScript가 알아야 상호작용이 시작된다. 이벤트와 폼 처리를 배우면 메뉴, 검증, 버튼, 입력 안내처럼 실제 웹페이지의 동작을 구현할 수 있다.

> [!TIP]
> 문법을 외우기 전에 **무엇을 해결하기 위한 문법인지** 먼저 확인한다. 같은 문법도 목적을 이해하면 다른 예제에서 다시 사용할 수 있다.

## 학습 전 생각해 보기

1. 이 개념이 없으면 코드를 어떤 방식으로 작성해야 할까?
2. 현재 예제에서 입력값과 결과값은 무엇일까?
3. 코드 한 줄을 제거하면 어떤 변화가 생길까?

---

# 개념과 수업 예제

```js
const button = document.querySelector('#save');
button.addEventListener('click', () => {
  console.log('저장');
});
```

## 폼 submit

```js
const form = document.querySelector('form');
form.addEventListener('submit', event => {
  event.preventDefault();
  const id = form.querySelector('[name="userId"]').value.trim();
  if (!id) return alert('아이디를 입력하세요.');
});
```

## 체크된 요소

```js
const checked = document.querySelectorAll('input[name="topping"]:checked');
const values = [...checked].map(input => input.value);
```

## 이벤트 위임

동적으로 추가된 Todo 삭제 버튼은 부모에서 클릭을 받아 처리할 수 있다.

```js
list.addEventListener('click', event => {
  if (event.target.matches('.delete')) event.target.closest('li').remove();
});
```

## 주의사항

- 이벤트 객체의 `target`과 현재 리스너 요소인 `currentTarget`을 구분한다.
- submit에서는 새로고침을 막아야 할 때 `preventDefault()`를 사용한다.

---

# 수업 문제와 풀이

> [!IMPORTANT]
> 아래 문제는 별도 문제 폴더에 있던 내용을 이 개념 문서로 통합한 것이다. 먼저 문제를 읽고 직접 풀이한 뒤 해설과 비교한다.

개인 및 강사 `17_event_form.js`의 주문·배송, 로그인, 피자 주문, 메뉴 선택, Todo 문제를 바탕으로 이벤트 흐름과 폼 검증 방법을 정리한다.

> [!TIP]
> 문제를 바로 코드로 옮기지 말고 **입력 → 처리 → 출력**을 먼저 한 줄씩 적는다. 그 다음 필요한 변수, 반복 횟수, 조건식을 정하면 코드가 단순해진다.

## 폼 문제 해결 순서

1. 어떤 이벤트를 사용할지 정한다: `click`, `change`, `input`, `submit`.
2. 폼 제출이라면 기본 새로고침을 막아야 하는지 확인한다.
3. 입력값을 읽고 `trim()`으로 정리한다.
4. 검증에 실패하면 즉시 종료한다.
5. 정상일 때만 DOM 변경이나 금액 계산을 수행한다.
6. 작업 완료 뒤 입력값과 선택 상태를 초기화한다.

---

## 문제 1. 주문자 정보와 배송지 동일 처리

```js
const sameCheckbox = document.querySelector('#same');
const orderer = document.querySelector('#orderer');
const ordererPhone = document.querySelector('#ordererPhone');
const receiver = document.querySelector('#receiver');
const receiverPhone = document.querySelector('#receiverPhone');

sameCheckbox?.addEventListener('change', () => {
  if (sameCheckbox.checked) {
    receiver.value = orderer.value;
    receiverPhone.value = ordererPhone.value;
  } else {
    receiver.value = '';
    receiverPhone.value = '';
  }
});
```

### 개선 아이디어

체크한 뒤 주문자 정보를 수정하면 배송지에는 자동 반영되지 않는다. 요구사항에 따라 주문자 입력 이벤트에서도 동기화할 수 있다.

```js
function syncReceiver() {
  if (!sameCheckbox.checked) return;
  receiver.value = orderer.value;
  receiverPhone.value = ordererPhone.value;
}

orderer.addEventListener('input', syncReceiver);
ordererPhone.addEventListener('input', syncReceiver);
```

> [!TIP]
> 문제 요구사항을 먼저 확인한다. “체크 순간 한 번 복사”인지 “체크된 동안 계속 동기화”인지에 따라 구현이 달라진다.

---

## 문제 2. 로그인 폼 검증

```js
const loginForm = document.querySelector('#loginForm');

loginForm?.addEventListener('submit', event => {
  event.preventDefault();

  const id = loginForm.elements.id.value.trim();
  const password = loginForm.elements.password.value;

  if (id === '') {
    console.log('아이디를 입력하세요.');
    loginForm.elements.id.focus();
    return;
  }

  if (password === '') {
    console.log('비밀번호를 입력하세요.');
    loginForm.elements.password.focus();
    return;
  }

  console.log('로그인 요청을 보낼 수 있습니다.');
});
```

### 왜 `return`을 사용하는가

검증 실패 뒤 아래 코드가 계속 실행되지 않도록 즉시 함수를 끝낸다. 중첩 `if`가 많아지는 것도 줄일 수 있다.

---

## 문제 3. 피자 옵션과 총액 계산

```js
const selectedToppings = [
  ...document.querySelectorAll('[name="topping"]:checked')
];

const toppingTotal = selectedToppings.reduce((sum, topping) => {
  return sum + Number(topping.dataset.price);
}, 0);
```

### `dataset`은 여기서 어떻게 쓰였는가

```html
<label>
  <input type="checkbox" name="topping" data-price="1500">
  치즈 추가
</label>
```

`data-price="1500"`은 JavaScript에서 `topping.dataset.price`로 읽는다. 값은 문자열이므로 금액 계산 전에 `Number()`로 변환한다.

### 반복문으로 작성한 풀이

```js
let toppingTotal = 0;

for (const topping of selectedToppings) {
  toppingTotal += Number(topping.dataset.price);
}
```

현재 학습 단계에서는 반복문 풀이가 계산 과정을 확인하기 쉽고, `reduce()`를 학습한 뒤 두 방식을 비교하면 좋다.

> [!WARNING]
> 문자열을 숫자로 바꾸지 않으면 `0 + '1500'`이 문자열 결합으로 처리될 수 있다.

---

## 문제 4. Todo 추가

```js
const form = document.querySelector('.todo-form');
const input = document.querySelector('.todo-input');
const list = document.querySelector('.todo-list');

form?.addEventListener('submit', event => {
  event.preventDefault();

  const text = input.value.trim();

  if (text === '') {
    input.focus();
    return;
  }

  const li = document.createElement('li');
  const span = document.createElement('span');
  const deleteButton = document.createElement('button');

  span.textContent = text;
  deleteButton.type = 'button';
  deleteButton.className = 'delete';
  deleteButton.textContent = '삭제';

  li.append(span, deleteButton);
  list.append(li);

  input.value = '';
  input.focus();
});
```

### 개인 풀이와 강사 풀이 비교

- 강사 풀이는 제출 이벤트, 기본 동작 방지, 요소 생성의 기본 흐름을 간결하게 보여줬다.
- 개인 풀이는 전체 선택 해제, 선택 삭제 등 요구사항을 확장해 구현했다.
- 확장 기능은 한꺼번에 넣기보다 “추가 → 개별 삭제 → 완료 상태 → 전체 선택” 순으로 기능 하나씩 테스트하는 것이 좋다.

---

## 문제 5. Todo 삭제: 이벤트 위임

```js
list?.addEventListener('click', event => {
  if (!event.target.classList.contains('delete')) return;

  event.target.closest('li')?.remove();
});
```

새로 생성된 버튼마다 이벤트를 다시 등록하지 않아도 된다. 목록처럼 자식 요소가 계속 추가되는 구조에서 유용하다.

## 더 좋은 폼 풀이 습관

- 버튼의 기본 `type`을 확인한다. 폼 내부 버튼은 기본적으로 submit이 될 수 있다.
- 입력값 검증 뒤 `return`으로 중단한다.
- 사용자 입력을 `innerHTML`에 직접 넣지 않는다.
- 화면 상태 변경과 계산 로직을 작은 함수로 나눈다.
- 이벤트가 중복 등록되지 않았는지 확인한다.

## 추가 연습

1. 비밀번호와 비밀번호 확인 값이 일치하는지 검사한다.
2. 체크된 메뉴만 합산해 주문 결과를 출력한다.
3. Todo 완료 상태를 토글하고 완료된 항목만 삭제한다.
4. 전체 선택 체크박스와 개별 체크박스 상태를 동기화한다.


---

# 자주 하는 실수

- 이벤트 이름에 `on`을 붙여 `addEventListener("onclick", ...)`로 작성하는 실수
- 폼 제출 시 기본 새로고침을 막지 않는 실수
- 입력값은 문자열이라는 사실을 잊는 실수
- 이벤트 핸들러를 호출한 결과를 전달하는 실수

> [!WARNING]
> 오류가 발생하면 코드를 한꺼번에 바꾸지 않는다. 선택 결과, 변수값, 자료형, 조건식 결과를 `console.log()` 또는 출력문으로 하나씩 확인한다.

# 실무 연결

수업에서 배운 문법은 작은 UI와 데이터 처리의 기본이 된다. 실무 사례를 볼 때도 새로운 기술 이름보다 **현재 코드가 어떤 값을 받고, 어떤 조건으로 처리하고, 무엇을 바꾸는지**에 집중한다.

# 직접 해보기

1. 문서의 첫 번째 예제를 직접 입력해 실행한다.
2. 값 하나를 바꾸고 실행 결과를 예상한 뒤 확인한다.
3. 조건이나 반복 횟수를 변경해 본다.
4. 오류가 발생하도록 일부 코드를 바꾸고 오류 메시지를 읽는다.
5. 예제를 보지 않고 핵심 부분을 다시 작성한다.

# Check Point

- [ ] 이 개념을 한 문장으로 설명할 수 있다.
- [ ] 왜 필요한지 예를 들어 설명할 수 있다.
- [ ] 기본 예제의 실행 순서를 말할 수 있다.
- [ ] 자주 하는 실수 한 가지와 해결 방법을 설명할 수 있다.
- [ ] 예제를 보지 않고 비슷한 코드를 작성할 수 있다.

# 예상 면접 질문

1. 이벤트와 이벤트 핸들러는 무엇인가요?
2. `preventDefault()`는 언제 사용하나요?
3. `click` 이벤트와 `submit` 이벤트의 차이는 무엇인가요?
4. 폼 값 검증은 어떤 순서로 처리하면 좋나요?

# 최종 요약

- `이벤트와 폼`의 이름만 외우지 않고 필요한 이유와 동작 순서를 함께 이해한다.
- 작은 예제를 실행하고 값을 바꾸면서 결과를 비교한다.
- 문제를 풀 때 입력 → 처리 → 출력으로 나눈다.
- 오류 메시지와 중간값을 확인하는 습관을 만든다.
- 다음 문서 `JS_External_API`로 넘어가기 전에 Check Point를 확인한다.

# 복습 기록

| 복습 시점 | 완료 | 이해도 메모 |
|---|---|---|
| 학습 당일 | [ ] |  |
| 1일 후 | [ ] |  |
| 7일 후 | [ ] |  |
| 30일 후 | [ ] |  |

## 다음 문서를 보기 전에

아래 질문에 답할 수 있다면 다음 문서로 넘어간다.

1. 이 개념은 어떤 문제를 해결하는가?
2. 기본 문법을 직접 작성할 수 있는가?
3. 가장 흔한 실수는 무엇이며 왜 발생하는가?

➡️ **다음 학습:** `JS_External_API`
