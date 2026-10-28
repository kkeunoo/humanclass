# 07-02 HTML 폼 전송과 GET POST — 연습문제

[해당 본문](../../07-02_HTML_폼_전송과_GET_POST.md) · [장별 문제 목차](README.md)

**새로 구성한 문제**다. [본문의 실제 GET 제출](../../07-02_HTML_폼_전송과_GET_POST.md)을 다른 값으로 바꾸어 적용한다. 제출 전에는 화면에 보이는 글자와 서버로 보낼 이름·값을 따로 적자.

## 문제

다음 폼에서 제출 버튼을 누를 때 주소의 `?` 뒤에 들어갈 이름과 값을 예상하자. `checked`를 지우면 무엇이 달라지는지도 적어 보자.

```html
<form action="/apply" method="get">
  <input name="learner" value="kim">
  <label><input name="topic" type="checkbox" value="html" checked>HTML</label>
  <input name="note" value="보이지만 전송 안 함" disabled>
  <button type="submit">보내기</button>
</form>
```

**확인 기준:** `name`·`value`·선택 상태·`disabled`를 각 입력마다 확인했는가? 실제 URL에서는 한글이나 공백이 인코딩될 수 있으므로, 우선 이름과 값의 포함 여부를 맞힌다.

<details>
<summary>해설 — 먼저 풀고 펼치기</summary>

선택된 상태라면 전송 대상은 `learner=kim`과 `topic=html`이다. 쿼리는 보통 `learner=kim&topic=html`처럼 보인다. `note`는 값이 보여도 `disabled`이므로 제출되지 않는다. 체크를 풀면 `topic`도 빠져 `learner=kim`만 남는다. GET 주소에 값이 생긴 것은 **요청을 보냈다는 뜻**이다. `/apply`에서 서버가 무엇을 처리했는지는 별도로 확인해야 한다.

</details>

## 원본과 연결하기

강사님과 내 코드의 GET 예제에서도 입력의 **보이는 안내 글자**와 제출하는 **`name=value`**를 구분해야 했다. 이 문제의 `note`는 원본에서 배운 `disabled` 동작을 섞은 새 조건이다. `method="post"`로 바꾸면 같은 입력 값을 주소 쿼리로 읽지 않는다는 점은 [본문 POST 절](../../07-02_HTML_폼_전송과_GET_POST.md#post)에서 확인한다.
