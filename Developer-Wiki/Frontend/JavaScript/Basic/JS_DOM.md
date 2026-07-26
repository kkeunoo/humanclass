---
title: JavaScript DOM 선택과 변경
category: JavaScript
last_updated: 2026-07-27
status: Active
---

# JavaScript DOM 선택과 변경


## 선택

```js
const title = document.querySelector('.title');
const items = document.querySelectorAll('.item');
```

`querySelectorAll` 결과는 여러 요소를 담은 NodeList다. NodeList 자체에는 개별 요소의 `classList`가 없다.

```js
items.forEach(item => {
  console.log(item.classList.contains('active'));
});
```

## 내용과 속성 변경

```js
title.textContent = '변경된 제목';
const image = document.querySelector('img');
image.setAttribute('alt', '상품 이미지');
```

## 요소 생성

```js
const li = document.createElement('li');
li.textContent = '새 항목';
document.querySelector('ul').append(li);
```

## 주의사항

- 선택 결과가 없으면 null이므로 사용 전 확인한다.
- 사용자 입력을 넣을 때 `innerHTML`보다 `textContent`가 안전하다.
- 여러 요소를 선택했는지 단일 요소를 선택했는지 구분한다.
