# 11-02 JavaScript DOM 속성과 클래스 — 연습문제

[해당 본문](../../11-02_JavaScript_DOM_속성과_클래스.md) · [장별 문제 목차](README.md)

**새로 구성한 연습문제**다. 먼저 해당 본문에서 강사님·내 코드와 실제 동작을 읽는다.

## 문제

`data-name="민지"`가 있는 버튼을 찾아 `dataset.name`을 읽고 콘솔에 출력하자. 같은 버튼에 `active` 클래스를 추가·제거했을 때 `contains('active')`의 결과도 순서대로 예상하자.

```html
<button data-name="민지">확인</button>
```

**확인 기준:** `data-name`과 `dataset.name`의 대응, `add`·`remove` 후 클래스 존재 여부를 설명한다.

<details>
<summary>해설 — 직접 해 본 뒤 펼치기</summary>

```javascript
const button = document.querySelector('button[data-name]');
console.log(button.dataset.name); // '민지'
button.classList.add('active');
console.log(button.classList.contains('active')); // true
button.classList.remove('active');
console.log(button.classList.contains('active')); // false
```

HTML `data-name`은 JavaScript에서 `dataset.name`으로 읽는다. 클래스 상태는 글자를 직접 덧붙이지 않고 `classList`로 바꾼다. 강사님 이벤트 퀴즈에도 `dataset` 사용이 있으므로 이 문법은 실제 학습 본문에 속한다.

</details>

버튼 클릭 후 화면 문구를 바꾸는 응용은 [다음 12장 내용 변경](../../12_JavaScript_DOM_콘텐츠생성과_스타일조작.md)과 [15장 이벤트](../../15_JavaScript_DOM이벤트와_키보드스크롤제어.md)를 배운 뒤 해도 된다.
