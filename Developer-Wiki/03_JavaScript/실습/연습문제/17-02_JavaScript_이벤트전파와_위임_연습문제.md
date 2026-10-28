# 17-02 JavaScript 이벤트전파와 위임 — 연습문제

[해당 본문](../../17-02_JavaScript_이벤트전파와_위임.md) · [장별 문제 목차](README.md)

**새로 구성한 연습문제**다. 먼저 해당 본문에서 강사님·내 코드와 실제 동작을 읽는다.

## 문제

부모 `ul` 하나에 클릭 리스너를 달아 `data-name`이 있는 자식 버튼만 처리하자.

```html
<ul id="menu"><li><button data-name="불고기">선택</button></li></ul>
```

**확인 기준:** 클릭한 실제 대상(`target`)과 리스너를 붙인 대상(`currentTarget`)을 구분한다. 빈 공간 클릭에서는 버튼 처리로 들어가지 않는지 확인한다.

<details>
<summary>해설 — 직접 해 본 뒤 펼치기</summary>

```javascript
const menu = document.querySelector('#menu');
menu.addEventListener('click', function(event) {
  if (!event.target.hasAttribute('data-name')) return;
  console.log(event.target.dataset.name);
});
```

버튼을 직접 누르면 `target`은 그 버튼이고, 리스너를 붙인 `currentTarget`은 `ul`이다. 빈 공간을 누르면 조건을 통과하지 않아 출력하지 않는다. 이 예제는 **data-name이 버튼에만 있고 버튼 안에 다른 자식 요소가 없다는 조건**을 둔다. 원본에서 배운 `hasAttribute`로 대상을 검사하며 새 `matches` 문법을 필수로 요구하지 않는다.

</details>

`data-name`과 `dataset.name`은 [11-02장](../../11-02_JavaScript_DOM_속성과_클래스.md)에서 이미 배운 문법이다. 여기서는 그것을 부모 이벤트 위임과 연결한다.
