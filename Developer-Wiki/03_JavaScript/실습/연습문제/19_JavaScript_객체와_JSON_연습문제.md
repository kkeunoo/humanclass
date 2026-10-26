# 19 JavaScript 객체와 JSON — 연습문제

[해당 본문](../../19_JavaScript_객체와_JSON.md) · [장별 문제 목차](README.md)

**새로 구성한 연습문제**다. 먼저 해당 본문에서 강사님·내 코드와 실제 동작을 읽는다.

## 문제

`{name:"A", done:false}`를 JSON 문자열로 만들었다가 다시 객체로 읽고 `done`을 확인하자.

**확인 기준:** 문자열을 거쳐 돌아온 객체의 `done`은 `false`다.

<details>
<summary>해설 — 직접 해 본 뒤 펼치기</summary>

`JSON.stringify`는 문자열을, `JSON.parse`는 객체를 반환한다. JSON의 키·문자열은 큰따옴표로 표현된다.

</details>

원본 코드에서 같은 기능을 찾고, 입력값·반환값·화면 변화가 문제와 어디서 달라지는지 한 문장으로 적어 보자.
