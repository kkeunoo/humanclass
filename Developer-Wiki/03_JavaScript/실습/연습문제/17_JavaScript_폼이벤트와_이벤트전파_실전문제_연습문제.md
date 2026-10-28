# 17 JavaScript 폼이벤트와 이벤트전파 실전문제 — 연습문제

[해당 본문](../../17_JavaScript_폼이벤트와_이벤트전파_실전문제.md) · [장별 문제 목차](README.md)

**새로 구성한 연습문제**다. 먼저 해당 본문에서 강사님·내 코드와 실제 동작을 읽는다.

## 문제

폼 `submit`에서 입력값을 읽고 브라우저 기본 제출을 막아 현재 화면에 요약을 표시하자.

```html
<form id="apply"><input id="name"><button type="submit">확인</button></form>
<p id="summary"></p>
```

**확인 기준:** `submit` 이벤트를 **폼**에 등록했는지, 값을 읽고 화면을 바꾼 뒤 기본 제출이 일어나지 않는지 확인한다.

<details>
<summary>해설 — 직접 해 본 뒤 펼치기</summary>

```javascript
const form = document.querySelector('#apply');
const nameInput = document.querySelector('#name');
const summary = document.querySelector('#summary');
form.addEventListener('submit', function(event) {
  event.preventDefault();
  summary.textContent = nameInput.value;
});
```

위 HTML의 form·input·출력 요소를 대상으로 한다. `preventDefault()`는 기본 제출을 막으므로 현재 페이지에서 결과를 확인한다. 이벤트가 부모로 전달되는 것을 막는 `stopPropagation()`과는 역할이 다르다.

</details>

강사님·내 원본의 **검사한 문자열과 실제 제출한 문자열**을 비교해 보자. 이 새 연습은 제출을 막고 화면에 현재 입력값을 보여 주는 조건이다.
