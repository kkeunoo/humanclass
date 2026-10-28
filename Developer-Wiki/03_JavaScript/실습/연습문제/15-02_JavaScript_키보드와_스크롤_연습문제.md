# 15-02 JavaScript 키보드와 스크롤 — 연습문제

[해당 본문](../../15-02_JavaScript_키보드와_스크롤.md) · [장별 문제 목차](README.md)

**새로 구성한 연습문제**다. 먼저 해당 본문에서 강사님·내 코드와 실제 동작을 읽는다.

## 문제

키를 누르면 수업 원본처럼 `event.keyCode`를 표시하고, 스크롤하면 현재 `scrollY`를 표시하자.

**확인 기준:** 키를 누른 사건과 페이지를 스크롤한 사건을 별도 리스너로 다룬다. 스크롤할 만큼 페이지가 긴지도 확인한다.

<details>
<summary>해설 — 직접 해 본 뒤 펼치기</summary>

```javascript
window.addEventListener('keydown', function(event) {
  console.log(event.keyCode);
});
window.addEventListener('scroll', function() {
  console.log(window.scrollY);
});
```

`event.keyCode`는 원본이 사용한 키 식별 숫자다. Enter는 13, 오른쪽 방향키는 39로 확인한다. `scrollY`는 현재 세로 스크롤 위치다. 페이지가 짧아 스크롤 자체가 안 되면 0만 보거나 스크롤 이벤트가 발생하지 않을 수 있다. 실제 화면 글자 갱신은 같은 값을 선택한 요소의 `textContent`에 넣으면 된다.

</details>

강사님·내 원본의 Enter 포커스 이동은 키를 **읽는 일** 다음에 조건에 따라 **동작을 수행하는 일**이다. 위 코드는 우선 읽은 값만 확인한다.

> [!TIP]
> `event.key`는 키 이름을 문자열로 읽는 방법이다. 원본에서는 출력 예제가 주석에만 있어 이번 필수 문제의 답은 실제 실행 코드의 `keyCode`로 맞췄다.
