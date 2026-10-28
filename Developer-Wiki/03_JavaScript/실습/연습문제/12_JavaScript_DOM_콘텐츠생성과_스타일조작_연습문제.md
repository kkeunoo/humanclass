# 12 JavaScript DOM 콘텐츠생성과 스타일조작 — 연습문제

[해당 본문](../../12_JavaScript_DOM_콘텐츠생성과_스타일조작.md) · [장별 문제 목차](README.md)

**새로 구성한 연습문제**다. 먼저 해당 본문에서 강사님·내 코드와 실제 동작을 읽는다.

## 문제

이미 있는 `<p id="result"></p>`에 `'<strong>완료</strong>'`라는 문자열을 `textContent`와 `innerHTML`로 각각 넣어 보자. 화면에 보이는 결과와 만들어진 요소 구조가 어떻게 다른가?

**확인 기준:** 같은 문자열이 **글자로 보이는지**, `strong` 태그로 해석되는지 구분한다.

<details>
<summary>해설 — 직접 해 본 뒤 펼치기</summary>

`result.textContent = '<strong>완료</strong>'`이면 꺾쇠까지 글자로 보인다. `result.innerHTML = '<strong>완료</strong>'`이면 브라우저가 `strong` 요소로 해석한다. 사용자가 입력한 문자열을 그대로 보여 주려면 `textContent` 쪽이 목적에 맞다.

</details>

새 `p`를 `createElement()`로 만드는 일은 [다음 12-02장](../../12-02_JavaScript_DOM_요소생성과_삽입.md)에서 연습한다. 이 장에서는 **이미 선택한 요소의 내용**을 바꾼다.
