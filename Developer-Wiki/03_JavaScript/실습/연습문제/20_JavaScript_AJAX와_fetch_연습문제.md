# 20 JavaScript AJAX와 fetch — 연습문제

[해당 본문](../../20_JavaScript_AJAX와_fetch.md) · [장별 문제 목차](README.md)

**새로 구성한 연습문제**다. 먼저 해당 본문에서 강사님·내 코드와 실제 동작을 읽는다.

## 문제

수업 원본의 다음 흐름에서 각 단계가 무엇을 받는지 설명하자. 실제 주소·네트워크 실행은 하지 않는다.

```javascript
fetch('data.json')
  .then((response) => response.json())
  .then((data) => console.log(data))
  .catch((error) => console.log(error));
```

**확인 기준:** 첫 `then`의 `response`와 다음 `then`의 `data`를 구분한다. `catch`가 성공 때마다 실행되는지 생각한다.

<details>
<summary>해설 — 직접 해 본 뒤 펼치기</summary>

첫 `then`은 응답 객체를 받고 `response.json()`의 **결과를 이어 준다**. 다음 `then`은 JSON을 읽어 얻은 데이터를 받는다. 오류가 나면 `catch`에서 처리한다. 실제 파일의 내용과 서버 응답을 모르면 `data`의 구체적인 값을 `1,2`라고 확정할 수 없다. 원본의 `XMLHttpRequest`에서는 `onload`와 `responseText`를 읽었으므로 방식이 다르다.

</details>

`Promise.resolve()`로 응답을 가짜로 만드는 방법은 양쪽 수업 원본에서 확인되지 않는다. **추가로 알면 좋은 것**으로만 두고, 이 문제는 실제 배운 `fetch` 연결 순서를 읽는 연습이다.
