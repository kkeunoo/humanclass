# 08-03 JavaScript 타이머와 취소 — 연습문제

[해당 본문](../../08-03_JavaScript_타이머와_취소.md) · [장별 문제 목차](README.md)

**새로 구성한 연습문제**다. 먼저 해당 본문에서 강사님·내 코드와 실제 동작을 읽는다.

## 문제

`setTimeout`으로 1초 뒤 메시지를 예약한 다음 **즉시** `clearTimeout`으로 취소하자. 취소 줄을 지우고 다시 실행했을 때의 결과도 예상하자.

**확인 기준:** 예약·취소·콜백 실행을 시간 순서로 적는다. `clearTimeout`을 실행한 때와 실행하지 않은 때의 출력을 구분한다.

<details>
<summary>해설 — 직접 해 본 뒤 펼치기</summary>

```javascript
const timerId = setTimeout(function() {
  console.log('완료');
}, 1000);
clearTimeout(timerId);
```

이 순서에서는 1초가 지나기 전에 예약을 지우므로 `완료`는 출력되지 않는다. 마지막 줄을 삭제하면 약 1초 뒤 출력된다. 이미 실행된 콜백을 나중에 취소해도 **이전 출력은 되돌아가지 않는다.**

</details>

강사님·내 원본에서 **반복 예약**인 `setInterval`은 `clearInterval`과 짝을 이룬다. 이 문제는 한 번 예약하는 `setTimeout`만 다룬다. 버튼 클릭과 타이머를 합치는 응용은 [15장 이벤트](../../15_JavaScript_DOM이벤트와_키보드스크롤제어.md) 뒤에 해도 된다.
