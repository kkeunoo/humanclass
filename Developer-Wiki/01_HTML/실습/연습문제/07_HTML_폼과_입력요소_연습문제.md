# 07 HTML 폼과 입력요소 — 연습문제

[해당 본문](../../07_HTML_폼과_입력요소.md) · [장별 문제 목차](README.md)

**새로 구성한 문제**다. [본문의 입력 상태와 버튼](../../07_HTML_폼과_입력요소.md)을 다른 문구로 다시 만든다. 우선 **초기 상태 → 사용자가 바꾼 상태 → 초기화 후 상태**를 종이에 적자.

## 문제

이름 입력과 오전·오후 선택, 제출·초기화 버튼이 있는 폼을 만든다. `label` 클릭도 확인하자.

**확인 기준:** 이름 글자를 눌렀을 때 입력 칸으로 이동하는지, 오전·오후 중 한 가지만 선택되는지, 초기화하면 처음 선택된 값으로 돌아오는지 확인한다.

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

오후를 선택하고 이름을 적은 뒤 초기화하면 이름은 빈칸, 시간은 오전으로 돌아간다. `name="time"`이 두 라디오에 같게 붙어 한 그룹이 된다. `value="am"`은 화면의 `오전` 글자와 구분되는 제출 값이다.

</details>

## 원본과 연결하기

강사님과 내 원본에서도 선택 상태, 표시 문구, 전송 값이 서로 다를 수 있었다. 이 문제의 값 `am`·`pm`은 새로 정한 연습 조건이다. 제출 버튼을 눌렀을 때 어떤 값이 전송되는지는 [다음 장의 GET·POST](../../07-02_HTML_폼_전송과_GET_POST.md)에서 이어서 확인한다.
