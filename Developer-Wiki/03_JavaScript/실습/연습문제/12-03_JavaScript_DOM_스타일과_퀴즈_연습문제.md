# 12-03 JavaScript DOM 스타일과 퀴즈 — 연습문제

[해당 본문](../../12-03_JavaScript_DOM_스타일과_퀴즈.md) · [장별 문제 목차](README.md)

**새로 구성한 연습문제**다. 먼저 해당 본문에서 강사님·내 코드와 실제 동작을 읽는다.

## 문제

아래 요소들 중 정확히 `q2` 클래스가 있는 것만 찾아 글과 배경색을 바꾸자. 내 원본의 q2 퀴즈를 작은 예제로 다시 연습한다.

```html
<div class="quiz q2">대상</div>
<div class="quiz q2-1">대상 아님</div>
```

**확인 기준:** `q2`와 `q2-1`을 서로 다른 클래스 이름으로 구분하고, 조건에 맞는 요소의 글과 배경색만 바뀌는지 확인한다.

<details>
<summary>해설 — 직접 해 본 뒤 펼치기</summary>

```javascript
const items = document.querySelectorAll('div.quiz');
for (let i = 0; i < items.length; i++) {
  if (items[i].classList.contains('q2')) {
    items[i].textContent = '찾음';
    items[i].style.background = 'yellow';
  }
}
```

첫 번째 div만 `찾음`으로 바뀌고 노란 배경을 갖는다. 두 번째의 `q2-1`은 `q2` 클래스가 아니다. 내 원본의 실제 풀이와 강사님 원본의 문제 제시는 [본문 4절](../../12-03_JavaScript_DOM_스타일과_퀴즈.md)에서 구분한다.

</details>

폼 입력의 `value`와 버튼 클릭은 [13장 폼 입력](../../13_JavaScript_DOM_폼요소와_입력값처리.md)과 [15장 이벤트](../../15_JavaScript_DOM이벤트와_키보드스크롤제어.md)에서 배운 뒤 연습한다. 문자열인 `style.height`에 5를 더하는 실험은 본문의 단위 처리 절에서 따로 복습한다.
