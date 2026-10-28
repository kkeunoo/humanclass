# 19 JavaScript 객체와 JSON — 연습문제

[해당 본문](../../19_JavaScript_객체와_JSON.md) · [장별 문제 목차](README.md)

**새로 구성한 연습문제**다. 먼저 해당 본문에서 강사님·내 코드와 실제 동작을 읽는다.

## 문제

`{name:"A", done:false}`를 JSON 문자열로 만들었다가 다시 객체로 읽고 `done`을 확인하자.

**확인 기준:** 변환 전 객체, 중간 JSON 문자열, 다시 읽은 객체의 **자료형**을 구분한다.

<details>
<summary>해설 — 직접 해 본 뒤 펼치기</summary>

```javascript
const task = { name: 'A', done: false };
const text = JSON.stringify(task);
const parsed = JSON.parse(text);
console.log(text);        // '{"name":"A","done":false}'
console.log(parsed.done); // false
```

`JSON.stringify`는 객체를 **문자열**로 바꾸고 `JSON.parse`는 JSON 문자열을 다시 값으로 읽는다. JSON 텍스트의 키와 문자열 값은 큰따옴표를 사용한다. `false`는 따옴표가 없는 불리언이다.

</details>

강사님·내 원본의 객체 속성 읽기와 JSON 왕복을 같은 순서로 추적하자. 문자열을 화면에 표시한 것과 객체의 속성에 접근한 것은 다른 단계다.
