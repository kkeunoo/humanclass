# 12-02 JavaScript DOM 요소생성과 삽입 — 연습문제

[해당 본문](../../12-02_JavaScript_DOM_요소생성과_삽입.md) · [장별 문제 목차](README.md)

**새로 구성한 연습문제**다. 먼저 해당 본문에서 강사님·내 코드와 실제 동작을 읽는다.

## 문제

배열 `["A", "B"]`를 순회해 `li` 두 개를 만들고 `ul`에 붙이자.

```html
<ul id="list"></ul>
```

**확인 기준:** `createElement` 직후와 `append` 후에 새 항목이 화면에 있는지 구분한다. 배열 순서를 유지하는지도 확인한다.

<details>
<summary>해설 — 직접 해 본 뒤 펼치기</summary>

```javascript
const list = document.querySelector('#list');
const values = ['A', 'B'];
for (let i = 0; i < values.length; i++) {
  const item = document.createElement('li');
  item.textContent = values[i];
  list.append(item);
}
```

`createElement`는 요소를 만들지만 그때 바로 화면에 붙이지는 않는다. `append` 후에 A, B 순으로 나타난다. 위 HTML의 `ul`이 있어야 선택 결과가 `null`이 아니다. 반복 방식도 양쪽 수업 원본의 표 만들기와 같이 `for`문으로 맞췄다.

</details>

강사님·내 원본의 표 행 조립도 **요소 만들기 → 내용 넣기 → 부모에 붙이기** 순서다. 이 문제는 표 대신 목록으로 바꾼 새 연습이다.
