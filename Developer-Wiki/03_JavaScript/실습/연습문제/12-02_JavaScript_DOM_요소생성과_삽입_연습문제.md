# 12-02 JavaScript DOM 요소생성과 삽입 — 연습문제

[해당 본문](../../12-02_JavaScript_DOM_요소생성과_삽입.md) · [장별 문제 목차](README.md)

**새로 구성한 연습문제**다. 먼저 해당 본문에서 강사님·내 코드와 실제 동작을 읽는다.

## 문제

배열 `["A", "B"]`를 순회해 `li` 두 개를 만들고 `ul`에 붙이자.

**확인 기준:** 목록에 A, B가 각각 한 줄씩 보인다.

<details>
<summary>해설 — 직접 해 본 뒤 펼치기</summary>

`document.createElement("li")`, `textContent`, `append` 순서로 처리한다.

</details>

원본 코드에서 같은 기능을 찾고, 입력값·반환값·화면 변화가 문제와 어디서 달라지는지 한 문장으로 적어 보자.
