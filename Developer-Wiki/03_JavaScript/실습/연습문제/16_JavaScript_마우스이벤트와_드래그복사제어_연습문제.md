# 16. 마우스와 드래그 — 좌표의 기준과 상태를 함께 읽기 — 연습문제

[본문](../../16_JavaScript_마우스이벤트와_드래그복사제어.md) · [문제 목차](README.md)

실제 수업 기능을 바탕으로 **새로 구성한 연습문제**다. 강사님 원본 퀴즈와 구분한다. 예상 → 이유 → 수정 순서로 풀고, 정답은 먼저 답한 뒤 펼친다.

## 목표와 실행 조건

누르기·놓기·클릭을 구분하고 네 가지 좌표 기준을 비교한다. 포인터 따라가기와 드래그의 차이, 누른 위치를 빼는 이유, 요소 밖에서 놓았을 때의 한계를 설명한다.

[전체 실행 HTML](../책형_복습/16_JavaScript_마우스이벤트와_드래그복사제어.html)과 같은 폴더의 JS를 함께 준비한다. Console을 열고 새로고침하면 처음부터 실행한다. 원본과 별도 파일이므로 기존 변수·타이머·출력 변경 실험의 영향을 섞지 않는다. 실제 입력·현재 시각·난수는 고정 결과와 구별한다.

입력·버튼·키보드·스크롤 예제는 [본문의 3절](../../16_JavaScript_마우스이벤트와_드래그복사제어.md#example)에 적힌 조작 순서대로 결과를 예상한다. 통신 예제는 해당 절의 가상 JSON 파일과 로컬 웹 실행 준비가 필요하며 HTML을 직접 여는 조건과 다르다. Console 출력이 없는 문제는 화면의 값·개수·선택 상태를 답한다.

## 문제 1. 실행 순서와 결과 예상

다음은 **새 설명 예제**다. 출력 전에 어떤 값이 어떤 순서로 만들어지는지 적는다.

**필요한 HTML · 스크립트 앞:**

```html
    <div id="drag">여기를 잡고 이동</div>
    <p>상자의 왼쪽 위에서 20px·20px 지점을 누르고 이동해 보세요.</p>
```

**필요한 CSS · head의 style:**

```css
body { min-height: 800px; } #drag { position: absolute; left: 100px; top: 220px; width: 120px; height: 80px; background: lightblue; user-select: none; }
```

```javascript
const drag = document.getElementById('drag');
let isDrag = false;
let offsetX = 0;
let offsetY = 0;
drag.addEventListener('mousedown', function (event) {
    isDrag = true;
    offsetX = event.offsetX;
    offsetY = event.offsetY;
    console.log('시작', offsetX, offsetY);
});
document.body.addEventListener('mousemove', function (event) {
    if (isDrag) {
        drag.style.left = event.pageX - offsetX + 'px';
        drag.style.top = event.pageY - offsetY + 'px';
    }
});
window.addEventListener('mouseup', function () {
    if (isDrag) {
        isDrag = false;
        console.log('끝', drag.style.left, drag.style.top);
    }
});
```

<details>
<summary>힌트와 풀이</summary>

**힌트:** 입력·현재 상태·실행 시점·반환값을 따로 표시한다.

```text
시작 20 20
끝 200px 280px
```

스크롤이 0인 상태에서 상자 안의 문서 좌표 (120, 240)을 누르고 (220, 300)까지 옮긴 뒤 놓는다. 상자는 처음 (100, 220)에 있으므로 누른 위치는 (20, 20)이다. 마지막 좌표에서 이를 빼 left 200px·top 280px가 된다. 놓은 뒤 포인터만 더 움직여도 상자는 그대로다. 새 예제는 원본의 mouseup 범위를 window로 넓힌 개선안이며, 원본을 그대로 실행한 결과로 표시하지 않는다.

</details>

## 문제 2. 개념을 자신의 말로 설명

1. game의 따라가기와 img의 드래그는 언제 움직이는가?
2. offsetX가 15이고 pageX가 110이면 left는?
3. mouseup을 요소 밖에서 놓치면 어떤 상태가 남는가?

<details>
<summary>풀이</summary>

game은 이동할 때마다, img는 드래그 상태가 true인 이동 때 움직인다. left는 95px다. 해제되지 않은 true가 남아 이후 이동에도 상자가 움직일 수 있다.

| 순간 | isDrag | 저장·변경 내용 |
| --- | --- | --- |
| 처음 | false | 이동해도 좌표를 바꾸지 않음 |
| (120, 240)에서 누름 | true | offset (20, 20) 저장 |
| (220, 300)으로 이동 | true | left 200px, top 280px |
| 놓음 | false | 현재 위치 유지 |
| 이후 포인터만 이동 | false | 상자 위치 변화 없음 |

일반적인 왼쪽 클릭에서는 mousedown → mouseup → click을 관찰한다. 더블클릭에는 개별 click도 생기므로 dblclick만 발생한다고 생각하지 않는다. 원본에서 log에 문자열을 이어 붙이는 이유는 log(message)가 한 메시지를 받기 때문이며, 이벤트 매개변수가 하나여서 +를 써야 하는 것은 아니다.

</details>

## 문제 3. 한 가지를 바꾸어 확인

먼저 **offset을 빼지 않음**를 바꾸면 무엇이 달라질지 적는다. 그다음 실행 파일에 해당 변경만 적용해 실제 결과와 비교한다. 나머지 실험도 원래 예제로 돌아가 하나씩 수행한다.

<details>
<summary>변경 결과와 막힐 때 확인</summary>

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| offset을 빼지 않음 | 요소 모서리가 포인터로 이동 | 잡은 지점 보정이 사라짐 |
| if 조건 제거 | 누르지 않아도 따라옴 | 상태에 따른 제한이 사라짐 |
| window 대신 drag에 mouseup | 밖에서 놓을 때 해제를 놓칠 수 있음 | 이벤트 수신 범위가 좁아짐 |

움직일 때 튀면 좌표 기준과 offset 저장 시점을 확인한다. CSS에서 위치를 바꿀 수 있게 position을 지정했는지도 본다. 놓았는데 계속 움직이면 isDrag가 false로 바뀌었는지와 mouseup 등록 대상을 살핀다. 이름에 언더바를 붙였다고 자동으로 전역·비공개가 되는 것은 아니다.

</details>

## 채점과 복습

| 점검 | 확인할 것 |
| --- | --- |
| 예측 | 실행 전에 출력·상태를 적었는가? |
| 근거 | 문법·조건·반환·순서로 설명했는가? |
| 수정 | 한 조건만 바꾸었는가? |
| 확인 | 실제 관찰과 코드 기준 예상을 구분했는가? |

틀린 이유를 설명할 수 없다면 [본문](../../16_JavaScript_마우스이벤트와_드래그복사제어.md)의 작은 예제·내 원본 풀이로 돌아간다. TIP의 미학습 기능은 이 문제의 필수 정답이 아니다.
