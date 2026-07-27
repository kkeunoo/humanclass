---
title: JavaScript 이벤트와 폼 문제 풀이
category: JavaScript Problems
last_updated: 2026-07-27
status: Active
---

# JavaScript 이벤트와 폼 문제 풀이

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
