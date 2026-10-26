# 07 HTML 폼과 입력요소 — 연습문제

[해당 본문](../../07_HTML_폼과_입력요소.md) · [장별 문제 목차](README.md)

**새로 구성한 문제**다. 먼저 강사님·내 코드의 실제 결과를 읽고 아래 조건을 직접 구현하거나 계산하자.

## 문제

이름 입력과 오전·오후 선택, 제출·초기화 버튼이 있는 폼을 만든다. `label` 클릭도 확인하자.

**확인 기준:** 이름 입력에 label이 연결되고 선택의 초기값과 reset 이후 값이 같다.

<details>
<summary>해설 — 먼저 풀고 펼치기</summary>

```html
<form method="get">
  <label for="learner">이름</label>
  <input id="learner" name="learner" type="text">
  <label><input name="time" type="radio" value="am" checked>오전</label>
  <label><input name="time" type="radio" value="pm">오후</label>
  <button type="submit">제출</button>
  <button type="reset">초기화</button>
</form>
```
첫 `label`은 `for`와 `id`로 연결하고, 선택지는 입력을 `label` 안에 넣었다. 초기화하면 처음 선택된 오전으로 돌아간다.

</details>

원본의 입력·구조·결과와 이 연습문제에서 바꾼 조건을 한 문장으로 비교해 보자.
