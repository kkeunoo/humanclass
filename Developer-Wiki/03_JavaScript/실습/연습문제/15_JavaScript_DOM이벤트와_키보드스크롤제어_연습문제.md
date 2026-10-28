# 15 JavaScript DOM이벤트와 키보드스크롤제어 — 연습문제

[해당 본문](../../15_JavaScript_DOM이벤트와_키보드스크롤제어.md) · [장별 문제 목차](README.md)

**새로 구성한 연습문제**다. 먼저 해당 본문에서 강사님·내 코드와 실제 동작을 읽는다.

## 문제

버튼 하나에 클릭 리스너를 붙이고 클릭 횟수를 `#count`에 표시하자. `button.onclick`에 서로 다른 함수를 차례로 대입하는 경우와 `addEventListener`로 등록하는 경우도 구분하자.

```html
<button id="run">실행</button><span id="count">0</span>
```

**확인 기준:** 버튼을 누를 때마다 값이 한 번 증가하는지, 리스너 등록 방식이 결과에 어떤 영향을 주는지 확인한다.

<details>
<summary>해설 — 직접 해 본 뒤 펼치기</summary>

```javascript
let clicks = 0;
const button = document.querySelector('#run');
const count = document.querySelector('#count');
function recordClick() {
  clicks += 1;
  count.textContent = String(clicks);
}
button.addEventListener('click', recordClick);
```

두 번 누르면 1, 2로 바뀐다. `button.onclick = first; button.onclick = second;`처럼 같은 속성에 다시 대입하면 뒤의 `second`가 앞의 값을 대체한다. 별도 함수를 각각 `addEventListener('click', ...)`로 등록하면 둘 다 반응할 수 있다. 강사님·내 원본의 두 방식을 [본문 2절](../../15_JavaScript_DOM이벤트와_키보드스크롤제어.md)에서 대조하자.

</details>

키보드의 `event.key`는 [다음 15-02장](../../15-02_JavaScript_키보드와_스크롤.md)에서 연습한다. 이 장의 필수 문제는 클릭 리스너와 함수 참조다.
