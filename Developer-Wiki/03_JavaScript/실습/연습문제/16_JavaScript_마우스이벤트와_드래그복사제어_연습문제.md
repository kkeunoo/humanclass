# 16 JavaScript 마우스이벤트와 드래그복사제어 — 연습문제

[해당 본문](../../16_JavaScript_마우스이벤트와_드래그복사제어.md) · [장별 문제 목차](README.md)

**새로 구성한 연습문제**다. 먼저 해당 본문에서 강사님·내 코드와 실제 동작을 읽는다.

## 문제

상자에서 마우스를 **누르기 → 움직이기 → 놓기** 순서로 조작할 때 `mousedown`, `mousemove`, `mouseup`이 언제 발생하는지 기록하자. 이동 중에는 누르고 있는지 나타내는 변수도 바꾼다.

```html
<div id="box" style="width:150px;height:100px;border:1px solid black">상자</div>
```

**확인 기준:** 누르기 전 이동과 누른 뒤 이동을 구별하고, 손을 놓으면 드래그 상태가 꺼지는지 확인한다.

<details>
<summary>해설 — 직접 해 본 뒤 펼치기</summary>

```javascript
let dragging = false;
const box = document.querySelector('#box');
box.addEventListener('mousedown', () => { dragging = true; });
box.addEventListener('mousemove', () => {
  if (dragging) console.log('누른 채 이동');
});
box.addEventListener('mouseup', () => { dragging = false; });
```

이 코드는 상태만 기록하며 실제 위치 이동은 하지 않는다. 강사님·내 원본의 드래그는 좌표를 계산해 요소를 움직인다. **요소 밖에서 놓으면 `mouseup`을 놓칠 수 있다는 원본의 한계**도 [본문 6절](../../16_JavaScript_마우스이벤트와_드래그복사제어.md)에서 확인한다.

</details>

`dragstart`는 이 수업의 마우스 좌표 기반 드래그 원본에서 사용한 이벤트가 아니다. 따라서 기본 문제에 섞지 않는다.
