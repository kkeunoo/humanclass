---
title: JavaScript 이벤트와 폼
category: JavaScript
last_updated: 2026-07-27
status: Active
---

# JavaScript 이벤트와 폼


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
