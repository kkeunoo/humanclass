---
title: JavaScript 이벤트 폼 문제 풀이
category: JavaScript Problems
last_updated: 2026-07-27
status: Active
---

# JavaScript 이벤트 폼 문제 풀이


개인 및 강사 `17_event_form.js`에서 주문·배송, 로그인, 피자 주문, 메뉴 선택, Todo List 문제를 확인했다.

## 주문자와 배송지 동일

```js
sameCheckbox.addEventListener('change', () => {
  if (sameCheckbox.checked) {
    receiver.value = orderer.value;
    receiverPhone.value = ordererPhone.value;
  } else {
    receiver.value = '';
    receiverPhone.value = '';
  }
});
```

## 피자 옵션과 총액

```js
const selected = [...document.querySelectorAll('[name="topping"]:checked')];
const total = selected.reduce((sum, item) => sum + Number(item.dataset.price), 0);
```

현재 Wiki에서는 `dataset`을 독립 심화 문서로 만들지 않지만, 실제 수업 코드에 사용된 경우 해당 문제 안에서 필요한 만큼만 설명한다.

## Todo 추가와 삭제

```js
form.addEventListener('submit', event => {
  event.preventDefault();
  const text = input.value.trim();
  if (!text) return;
  const li = document.createElement('li');
  li.innerHTML = `<span></span><button type="button" class="delete">삭제</button>`;
  li.querySelector('span').textContent = text;
  list.append(li);
  input.value = '';
});
```

### 비교 코멘트

개인 코드는 전체 선택 해제, 선택 삭제 등 요구사항을 더 많이 구현했다. 강사 코드는 이벤트와 폼의 기본 흐름을 명확히 제시했다. 확장 기능을 추가할 때는 하나씩 완성하고 테스트하는 방식이 좋다.
