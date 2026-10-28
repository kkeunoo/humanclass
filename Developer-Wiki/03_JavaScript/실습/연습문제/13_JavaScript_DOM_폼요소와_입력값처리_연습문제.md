# 13 JavaScript DOM 폼요소와 입력값처리 — 연습문제

[해당 본문](../../13_JavaScript_DOM_폼요소와_입력값처리.md) · [장별 문제 목차](README.md)

**새로 구성한 연습문제**다. 먼저 해당 본문에서 강사님·내 코드와 실제 동작을 읽는다.

## 문제

폼의 이름 입력과 선택 목록을 읽어 `이름: 선택값`을 콘솔에 표시하자. 선택을 바꾼 뒤 같은 값을 다시 읽으면 무엇이 달라지는지 확인하자.

**확인 기준:** 입력·선택의 **현재 값**을 읽는 시점을 명시한다. 화면의 안내 글자와 실제 `value`를 구분한다.

<details>
<summary>해설 — 직접 해 본 뒤 펼치기</summary>

```html
<input id="name" value="민지">
<select id="course">
  <option value="html">HTML</option>
  <option value="css">CSS</option>
</select>
```

```javascript
const nameInput = document.querySelector('#name');
const courseSelect = document.querySelector('#course');
console.log(nameInput.value + ': ' + courseSelect.value);
```

처음 읽으면 `민지: html`이다. CSS로 바꾼 뒤 콘솔에서 마지막 줄을 다시 실행하면 화면에 표시된 `CSS`가 아니라 옵션의 `value`인 `css`가 들어간다. `name` 속성은 제출 이름이고, 여기서 읽는 `.value`는 현재 값이다.

</details>

양쪽 원본의 폼 읽기 코드는 **읽는 순서**에 따라 바뀌기 전·후 값이 달랐다. 이 새 예제도 값을 저장한 문자열을 다시 출력하는 것과 요소의 현재 `value`를 새로 읽는 일을 구별한다. 버튼 이벤트에 연결하는 방법은 [15장](../../15_JavaScript_DOM이벤트와_키보드스크롤제어.md) 뒤에 응용한다.
