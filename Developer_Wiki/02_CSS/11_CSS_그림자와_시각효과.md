# CSS 그림자와 시각 효과

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `11_CSS_그림자와_시각효과.md` |
| 분류 | `02_CSS` |
| 권장 선수 학습 | `10_CSS_Float와_Clear.md` |
| 다음 학습 | `12_CSS_Transform.md` |
| 원본 기준 | `workspace_me/workspace_html/css/11_shadow.html`, `workspace_teacher/workspace_html/css/11_shadow.html` |
| 핵심 범위 | `text-shadow`, `box-shadow`, 오프셋, blur radius, spread radius, inset, 다중 그림자, hover 시각 효과 |
| 프로젝트 연결 | 카드 그림자, 버튼 hover, 텍스트 강조, 포커스 효과, 모달·드롭다운 깊이 표현 |

> 원본 CSS 11은 별도의 외부 CSS 파일 없이 `11_shadow.html` 내부 `<style>`에서 진행됩니다. 내 코드와 강사님 코드는 모두 `text-shadow` 두 가지, 기본 `box-shadow`, hover 시 박스 그림자를 실습합니다. 이 문서는 원본 구조를 그대로 보존하면서 그림자 문법, 접근성, 성능, hover·focus 상태, 다중 그림자는 **확장 학습**으로 구분해 보완했습니다.

---

# 학습 목표

- `text-shadow`와 `box-shadow`의 차이를 설명한다.
- 수평 오프셋과 수직 오프셋의 방향을 이해한다.
- blur radius가 그림자의 번짐 정도를 제어한다는 점을 설명한다.
- `box-shadow`의 spread radius와 `inset`을 이해한다.
- 색상 생략 시 `currentColor`가 사용될 수 있음을 이해한다.
- 여러 그림자를 쉼표로 겹쳐 사용할 수 있다.
- 텍스트 그림자가 글자 자체의 윤곽이나 대체 텍스트가 아니라는 점을 이해한다.
- 흰색 글자와 밝은 배경에서 대비 문제가 생길 수 있음을 설명한다.
- hover에만 시각 효과를 제공하지 않고 focus 상태도 함께 고려한다.
- 클릭 가능한 요소에는 실제 `button`이나 `a`를 사용한다.
- 그림자만으로 상태나 클릭 가능성을 전달하지 않는다.
- 과도한 blur와 큰 그림자가 렌더링 성능에 미치는 영향을 이해한다.
- 내 코드와 강사님 코드의 차이와 원본 주석의 부정확한 표현을 찾는다.

---

# 1. CSS 그림자란?

CSS 그림자는 요소나 텍스트 뒤에 시각적 깊이와 강조를 추가합니다.

대표 속성:

```css
text-shadow: ...;
box-shadow: ...;
```

구분:

| 속성 | 적용 대상 |
| --- | --- |
| `text-shadow` | 글자의 글리프 모양 |
| `box-shadow` | 요소의 박스 |

그림자는 레이아웃 공간을 차지하지 않습니다.

즉, 그림자가 바깥으로 커져도 주변 요소가 자동으로 밀려나지 않습니다.

---

# 2. 원본 실습 구조

원본 HTML에는 네 개의 실습 요소가 있습니다.

```html
<div class="red">
  한글 Shadow
</div>
```

```html
<div class="blur">
  한글 Shadow
</div>
```

```html
<div class="box">
  박스 Shadow
</div>
```

```html
<div class="box2">
  마우스를 올려보세요
</div>
```

강사님 마지막 문구는 다음과 같습니다.

```text
마우스 올려 보세요
```

내 코드:

```text
마우스를 올려보세요
```

의미는 같고 띄어쓰기와 조사 표현만 다릅니다.

---

# 3. `text-shadow` 기본 문법

```css
text-shadow:
  offset-x
  offset-y
  blur-radius
  color;
```

필수값:

```text
offset-x
offset-y
```

선택값:

```text
blur-radius
color
```

예:

```css
.title {
  text-shadow: 2px 2px 4px red;
}
```

의미:

```text
오른쪽 2px
아래쪽 2px
4px 번짐
빨간색 그림자
```

---

# 4. 수평 오프셋

```css
text-shadow: 10px 0 red;
```

수평 방향:

| 값 | 방향 |
| --- | --- |
| 양수 | 오른쪽 |
| 음수 | 왼쪽 |
| `0` | 좌우 이동 없음 |

예:

```css
.right-shadow {
  text-shadow: 8px 0 red;
}

.left-shadow {
  text-shadow: -8px 0 red;
}
```

---

# 5. 수직 오프셋

```css
text-shadow: 0 3px red;
```

수직 방향:

| 값 | 방향 |
| --- | --- |
| 양수 | 아래쪽 |
| 음수 | 위쪽 |
| `0` | 상하 이동 없음 |

예:

```css
.down-shadow {
  text-shadow: 0 4px red;
}

.up-shadow {
  text-shadow: 0 -4px red;
}
```

---

# 6. 원본 `.red`

내 코드:

```css
.red {
  /* offset-x, offset-y (떨어져있는 거리)만큼 띄워라 */
  text-shadow: 10px 3px red;
}
```

강사님 코드:

```css
.red {
  /* offset-x offset-y color */
  text-shadow: 10px 3px red;
}
```

최종 결과는 같습니다.

```text
오른쪽 10px
아래 3px
번짐 없음
빨간색 그림자
```

blur radius가 생략되어 그림자 가장자리가 비교적 선명하게 보입니다.

---

# 7. 내 코드 `.red` 주석 보완

원본:

```text
offset-x, offset-y (떨어져있는 거리)만큼 띄워라
```

초보자가 이해하기 좋은 방향입니다.

다만 “띄운다”는 표현만으로는 양수와 음수의 방향을 알기 어렵습니다.

개선:

```css
/*
  offset-x: 양수면 오른쪽, 음수면 왼쪽
  offset-y: 양수면 아래쪽, 음수면 위쪽
*/
```

---

# 8. Blur radius

```css
text-shadow: 2px 2px 4px red;
```

세 번째 길이값은 blur radius입니다.

```text
값이 작음 → 비교적 선명
값이 큼 → 넓게 번짐
```

blur radius는 음수를 사용할 수 없습니다.

```css
/* 잘못된 사용 */
text-shadow: 2px 2px -4px red;
```

---

# 9. 원본 `.blur`

내 코드:

```css
.blur {
  /* offset-x, offset-y (떨어져있는 거리)만큼 띄우고 blur투명도처리 */
  text-shadow: 2px 2px 4px red;
  color: white;
  font-size: 2em;
}
```

강사님:

```css
.blur {
  /* offset-x offset-y blur-radius color */
  text-shadow: 2px 2px 4px red;
  color: white;
  font-size: 2em;
}
```

실제 속성은 같습니다.

---

# 10. “blur 투명도 처리” 설명 보완

내 코드 주석:

```text
blur투명도처리
```

blur radius는 색상의 투명도 값을 직접 변경하는 속성이 아닙니다.

정확한 설명:

```text
blur radius는 그림자의 가장자리를 퍼뜨리고 흐리게 만든다.
투명도는 색상의 alpha 값으로 직접 조절할 수 있다.
```

예:

```css
text-shadow:
  2px 2px 4px rgb(255 0 0 / 50%);
```

여기서 투명도는 `50%` alpha가 담당합니다.

---

# 11. 흰색 글자의 대비 문제

원본 `.blur`:

```css
color: white;
```

본문 배경색은 지정되지 않았습니다.

브라우저 기본 배경이 흰색이면 글자 본체가 배경과 같은 색이므로 빨간 그림자만 보이거나 글자가 흐릿해 보일 수 있습니다.

개선:

```css
.blur {
  padding: 1rem;
  color: white;
  background-color: #222;
  text-shadow: 2px 2px 4px red;
}
```

또는 글자색을 어둡게 유지합니다.

```css
.blur {
  color: #111;
}
```

그림자는 글자 대비를 보장하는 수단이 아닙니다.

---

# 12. `font-size: 2em`

원본:

```css
font-size: 2em;
```

`em`은 현재 요소가 상속받은 글자 크기를 기준으로 계산됩니다.

부모 글자 크기가 `16px`이면 일반적으로:

```text
16px × 2 = 32px
```

글자가 커지면 같은 `2px`, `4px` 그림자가 상대적으로 작게 느껴질 수 있습니다.

비례 효과가 필요하면 그림자에도 `em` 단위를 사용할 수 있습니다.

```css
.title {
  text-shadow:
    0.08em
    0.08em
    0.15em
    rgb(0 0 0 / 35%);
}
```

---

# 13. 색상 생략

다음처럼 색상을 생략할 수 있습니다.

```css
.title {
  color: navy;
  text-shadow: 2px 2px 4px;
}
```

색상 생략 시 현재 글자색인 `currentColor`가 사용될 수 있습니다.

명확성과 유지보수를 위해 색상을 직접 작성하는 편이 좋을 수 있습니다.

```css
text-shadow:
  2px 2px 4px
  rgb(0 0 0 / 35%);
```

---

# 14. 다중 텍스트 그림자

쉼표로 여러 그림자를 겹칠 수 있습니다.

```css
.title {
  text-shadow:
    1px 1px 0 white,
    2px 2px 0 black;
}
```

네온 효과:

```css
.neon {
  color: white;
  background-color: #111;
  text-shadow:
    0 0 4px #38bdf8,
    0 0 10px #38bdf8,
    0 0 20px #38bdf8;
}
```

효과가 강할수록 가독성과 성능을 함께 확인합니다.

---

# 15. 텍스트 외곽선처럼 만들기

여러 방향의 선명한 그림자를 겹칠 수 있습니다.

```css
.outline-text {
  color: white;
  text-shadow:
    -1px -1px 0 black,
    1px -1px 0 black,
    -1px 1px 0 black,
    1px 1px 0 black;
}
```

이는 실제 글자 테두리 속성과는 다릅니다.

작은 글자에서는 가장자리가 지저분하거나 읽기 어려울 수 있습니다.

---

# 16. `box-shadow` 기본 문법

```css
box-shadow:
  offset-x
  offset-y
  blur-radius
  spread-radius
  color;
```

예:

```css
.card {
  box-shadow:
    4px 4px 6px 0
    gray;
}
```

`spread-radius`는 생략할 수 있습니다.

```css
box-shadow: 4px 4px 6px gray;
```

원본은 이 형태입니다.

---

# 17. 원본 `.box`

내 코드:

```css
.box {
  border: 1px solid red;
  width: 100px;

  box-shadow: 4px 4px 6px gray;
}
```

강사님:

```css
.box {
  border: 1px solid red;
  width: 100px;

  box-shadow: 4px 4px 6px grey;
}
```

차이:

```text
내 코드: gray
강사님: grey
```

CSS에서 `gray`와 `grey`는 같은 색상 키워드로 처리됩니다.

오류가 아닙니다.

---

# 18. 원본 박스 그림자 해석

```css
box-shadow: 4px 4px 6px gray;
```

의미:

```text
오른쪽 4px
아래 4px
blur radius 6px
회색
spread radius 생략 → 0
```

박스의 오른쪽 아래에 부드러운 회색 그림자가 생깁니다.

---

# 19. 박스 높이

원본 `.box`는 너비만 지정했습니다.

```css
width: 100px;
```

높이는 콘텐츠와 줄 높이에 따라 자동 계산됩니다.

```html
<div class="box">
  박스 Shadow
</div>
```

따라서 `.box2`처럼 고정 높이 `200px`을 가지지 않습니다.

패딩이 없어 텍스트와 테두리가 가까워 보일 수 있습니다.

개선:

```css
.box {
  width: 100px;
  padding: 1rem;
}
```

---

# 20. Spread radius

네 번째 길이값입니다.

```css
box-shadow:
  0 0 8px 4px
  rgb(0 0 0 / 25%);
```

의미:

```text
offset-x: 0
offset-y: 0
blur: 8px
spread: 4px
```

spread 양수:

```text
그림자 영역 확장
```

spread 음수:

```text
그림자 영역 축소
```

예:

```css
.card {
  box-shadow:
    0 12px 24px -12px
    rgb(0 0 0 / 35%);
}
```

---

# 21. `inset`

안쪽 그림자를 만듭니다.

```css
.input {
  box-shadow:
    inset 0 1px 3px
    rgb(0 0 0 / 20%);
}
```

눌린 영역이나 입력창 안쪽 깊이를 표현할 수 있습니다.

주의:

- inset은 색상이나 길이값이 아니다.
- 일반적으로 앞이나 뒤에 작성할 수 있다.
- 과도하면 입력창이 비활성화된 것처럼 보일 수 있다.

---

# 22. 다중 박스 그림자

```css
.card {
  box-shadow:
    0 1px 2px rgb(0 0 0 / 10%),
    0 8px 24px rgb(0 0 0 / 15%);
}
```

첫 번째 그림자:

```text
박스 가까이에 얕은 경계
```

두 번째 그림자:

```text
더 넓고 부드러운 깊이
```

여러 그림자는 쉼표 순서대로 그려지며 첫 번째 그림자가 위쪽에 위치합니다.

---

# 23. 원본 `.box2`

```css
.box2 {
  border: 1px solid black;
  width: 150px;
  height: 200px;
  margin: 10px;
}
```

기본 상태에는 그림자가 없습니다.

```css
.box2:hover {
  box-shadow: 4px 4px 6px gray;
  cursor: pointer;
}
```

마우스를 올렸을 때만 그림자와 포인터 커서가 나타납니다.

강사님은 `grey`, 내 코드는 `gray`를 사용합니다.

---

# 24. `:hover`

`:hover`는 포인터가 요소 위에 있을 때 적용됩니다.

```css
.card:hover {
  box-shadow:
    0 8px 24px
    rgb(0 0 0 / 20%);
}
```

대표 용도:

- 카드 강조
- 버튼 상태 변화
- 링크 장식
- 이미지 확대
- 드롭다운 표시

터치 환경에서는 hover가 없거나 예측하기 어렵게 동작할 수 있습니다.

핵심 기능을 hover에만 의존하지 않습니다.

---

# 25. `cursor: pointer`

원본:

```css
cursor: pointer;
```

사용자는 해당 요소가 클릭 가능할 것이라고 예상할 수 있습니다.

그러나 원본 `.box2`는 `div`이며 실제 링크나 버튼 동작이 없습니다.

```html
<div class="box2">
  마우스를 올려보세요
</div>
```

단순 hover 시각 실습이라면 이해할 수 있지만, 실제 UI에서는 클릭 기능이 없는 요소에 pointer를 주면 오해를 유발합니다.

---

# 26. 클릭 가능한 카드라면

링크 목적:

```html
<a class="card" href="/course/css">
  CSS 과정
</a>
```

버튼 동작:

```html
<button class="card-button" type="button">
  상세 정보 열기
</button>
```

단순 시각 박스:

```html
<div class="card">
  카드 설명
</div>
```

단순 박스에는 기본 커서를 유지합니다.

---

# 27. Hover와 Focus

키보드 사용자는 hover를 사용할 수 없습니다.

링크나 버튼이면 다음 상태를 함께 제공합니다.

```css
.card-link:hover,
.card-link:focus-visible {
  box-shadow:
    0 8px 24px
    rgb(0 0 0 / 20%);
}
```

포커스 표시를 그림자만으로 대체하지 않는 것이 좋습니다.

```css
.card-link:focus-visible {
  outline: 3px solid #2563eb;
  outline-offset: 3px;
}
```

---

# 28. 그림자 전환

원본은 hover 순간 그림자가 즉시 나타납니다.

부드러운 전환:

```css
.card {
  transition:
    box-shadow 0.2s ease,
    transform 0.2s ease;
}

.card:hover,
.card:focus-visible {
  transform: translateY(-2px);
  box-shadow:
    0 10px 24px
    rgb(0 0 0 / 18%);
}
```

주의:

- 그림자 전환은 렌더링 비용이 발생할 수 있다.
- 많은 요소에서 큰 blur를 동시에 애니메이션하지 않는다.
- 이동 효과에는 움직임 감소 환경을 고려한다.

---

# 29. 움직임 감소 설정

```css
@media (prefers-reduced-motion: reduce) {
  .card {
    transition: none;
  }

  .card:hover,
  .card:focus-visible {
    transform: none;
  }
}
```

그림자 상태 변화는 남기되 이동과 애니메이션을 줄일 수 있습니다.

---

# 30. 그림자는 레이아웃 공간을 만들지 않는다

```css
.card {
  box-shadow:
    0 20px 40px
    rgb(0 0 0 / 30%);
}
```

그림자가 40px 이상 퍼져도 다음 요소가 자동으로 40px 밀리지 않습니다.

따라서 카드 사이 간격은 별도로 지정합니다.

```css
.card-list {
  display: grid;
  gap: 2rem;
}
```

그림자가 잘리거나 겹치는지 확인해야 합니다.

---

# 31. Overflow와 그림자

부모:

```css
.wrapper {
  overflow: hidden;
}
```

자식:

```css
.card {
  box-shadow:
    0 12px 24px
    rgb(0 0 0 / 20%);
}
```

그림자가 부모 경계를 벗어나면 잘릴 수 있습니다.

CSS 09에서 배운 overflow 동작과 연결됩니다.

해결 방향:

- 불필요한 `overflow: hidden` 제거
- 부모 패딩 확보
- 그림자를 안쪽으로 조절
- 레이어 구조 재설계

---

# 32. Border와 Shadow 차이

| 구분 | `border` | `box-shadow` |
| --- | --- | --- |
| 박스 크기 영향 | box model에 포함 | 일반적으로 레이아웃 공간 미포함 |
| 목적 | 경계선 | 깊이·강조·광택 |
| 다중 표현 | 각 방향 제어 | 쉼표로 여러 그림자 |
| 안쪽 효과 | 별도 border | `inset` |
| 포커스 표시 | 가능 | 가능하지만 단독 의존 주의 |

레이아웃이 흔들리지 않는 강조 테두리에 그림자를 사용할 수도 있습니다.

```css
.input:focus {
  box-shadow:
    0 0 0 3px
    rgb(37 99 235 / 25%);
}
```

---

# 33. Focus ring으로서의 box-shadow

```css
.button:focus-visible {
  outline: 2px solid transparent;
  box-shadow:
    0 0 0 4px
    rgb(37 99 235 / 35%);
}
```

고대비 모드와 브라우저 환경에서는 그림자가 보이지 않을 수 있습니다.

따라서 네이티브 outline을 완전히 제거하지 않거나 대체가 확실한지 확인합니다.

안전한 조합:

```css
.button:focus-visible {
  outline: 3px solid #2563eb;
  outline-offset: 3px;
}
```

---

# 34. 그림자 색상

원본은 이름 색상을 사용합니다.

```css
red
gray
grey
black
white
```

실무에서는 alpha가 있는 색상을 자주 사용합니다.

```css
box-shadow:
  0 8px 24px
  rgb(0 0 0 / 15%);
```

완전 불투명한 회색 그림자보다 자연스럽게 배경과 섞입니다.

---

# 35. 그림자 디자인 토큰

```css
:root {
  --shadow-sm:
    0 1px 2px
    rgb(0 0 0 / 8%);

  --shadow-md:
    0 6px 16px
    rgb(0 0 0 / 14%);

  --shadow-lg:
    0 16px 40px
    rgb(0 0 0 / 18%);
}
```

사용:

```css
.card {
  box-shadow: var(--shadow-sm);
}

.card:hover {
  box-shadow: var(--shadow-md);
}
```

프로젝트 전체의 깊이 표현을 일관되게 관리할 수 있습니다.

---

# 36. 그림자 단계

예시:

| 단계 | 용도 |
| --- | --- |
| 없음 | 기본 평면 요소 |
| small | 입력창, 작은 버튼 |
| medium | 카드, 드롭다운 |
| large | 모달, 플로팅 패널 |

그림자 값은 브랜드와 배경색에 따라 조정합니다.

무조건 단계가 높다고 `z-index`도 높은 것은 아닙니다.

시각적 깊이와 실제 stacking order는 별개입니다.

---

# 37. 다크 모드 그림자

어두운 배경에서는 검정 그림자가 잘 보이지 않을 수 있습니다.

```css
.card {
  background-color: #1f2937;
  box-shadow:
    0 8px 24px
    rgb(0 0 0 / 40%);
}
```

테두리나 밝은 안쪽 하이라이트를 함께 사용할 수 있습니다.

```css
.card {
  border:
    1px solid
    rgb(255 255 255 / 10%);
  box-shadow:
    0 8px 24px
    rgb(0 0 0 / 45%);
}
```

---

# 38. Text-shadow 접근성

과도한 텍스트 그림자는 글자 경계를 흐리게 합니다.

특히 다음 경우 주의합니다.

- 작은 본문 글자
- 낮은 대비
- 여러 색상 네온 효과
- 밝은 배경의 흰색 글자
- dyslexia 등 읽기 어려움을 가진 사용자
- 고해상도와 저해상도 화면 차이

본문보다 제목이나 장식 텍스트에 제한적으로 사용합니다.

---

# 39. 상태 전달을 그림자에만 의존하지 않기

선택 상태:

```css
.card.is-selected {
  box-shadow:
    0 0 0 3px
    #2563eb;
}
```

그림자만으로 선택 상태를 표현하면 일부 사용자가 구분하기 어려울 수 있습니다.

함께 사용할 수 있는 것:

- 체크 아이콘
- 텍스트
- 배경색
- `aria-pressed`
- `aria-current`
- 실제 폼 상태

```html
<button
  class="card"
  type="button"
  aria-pressed="true"
>
  <span aria-hidden="true">✓</span>
  선택됨
</button>
```

---

# 40. 성능 고려

큰 blur 그림자는 넓은 픽셀 영역을 다시 그려야 할 수 있습니다.

부담이 커질 수 있는 경우:

- 수십 개 카드에 큰 그림자
- 스크롤 중 고정 요소의 그림자
- blur radius가 매우 큼
- 그림자를 지속적으로 애니메이션
- 반투명 레이어가 여러 개 겹침

개선 방향:

- 그림자 크기 최소화
- 애니메이션 요소 수 제한
- 이동은 `transform` 사용
- hover 대상만 그림자 강화
- 실제 저사양 모바일에서 테스트

---

# 41. 원본 문서 언어와 제목

내 코드와 강사님 코드:

```html
<html lang="en">
<title>Document</title>
```

본문은 한국어이므로 다음처럼 개선합니다.

```html
<html lang="ko">
<title>CSS 그림자</title>
```

---

# 42. 인라인 `<style>`

원본은 한 파일에서 빠르게 실습하기 위해 `<style>`을 사용합니다.

```html
<head>
  <style>
    ...
  </style>
</head>
```

학습 예제로는 적절합니다.

프로젝트에서는 외부 CSS로 분리할 수 있습니다.

```html
<link
  rel="stylesheet"
  href="asset/css/shadow.css"
>
```

장점:

- 여러 페이지에서 재사용
- 캐시 활용
- HTML 구조와 스타일 분리
- 코드 탐색 용이

---

# 43. My Code 분석

## 43.1 장점

- 첫 번째 텍스트 그림자에서 x·y 오프셋의 의미를 설명했다.
- 두 번째 예제에서 blur가 추가된다는 점을 기록했다.
- 기본 박스 그림자와 hover 그림자를 분리했다.
- 강사님 코드와 동일한 핵심 속성을 직접 실습했다.
- 간결한 예제로 결과를 빠르게 확인할 수 있다.

## 43.2 개선점

- blur를 “투명도 처리”라고 한 설명은 정확하지 않다.
- 흰색 글자에 배경색이 없어 대비가 낮을 수 있다.
- `.box`에 패딩이 없어 콘텐츠가 테두리에 가깝다.
- `.box2`는 실제 클릭 기능이 없는데 `cursor: pointer`를 사용한다.
- hover만 있고 키보드 focus 상태가 없다.
- 문서 언어가 `en`이다.
- 제목이 `Document`다.
- 이름 색상 대신 alpha 색상을 사용하면 자연스러운 그림자를 만들 수 있다.

---

# 44. Teacher Code 분석

## 44.1 장점

- `text-shadow` 문법을 정확한 순서로 주석 처리했다.
- `.blur`의 주석에 `blur-radius` 용어를 사용했다.
- `box-shadow`와 hover 상태를 최소 코드로 비교한다.
- 내 코드와 달리 blur를 투명도라고 설명하지 않는다.
- 전체 예제가 간결하다.

## 44.2 개선점

- 흰색 글자의 배경 대비가 부족할 수 있다.
- `.box2`는 실제 동작이 없는 `div`인데 pointer를 사용한다.
- 키보드 focus 상태가 없다.
- 그림자의 spread, inset, 다중 그림자 설명이 없다.
- 문서 언어가 `en`이다.
- 제목이 `Document`다.
- 인라인 스타일을 외부 CSS로 분리할 수 있다.

---

# 45. My Code vs Teacher Code

| 비교 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| `.red` 주석 | 거리 중심 한국어 설명 | 문법 순서 |
| `.blur` 주석 | “blur투명도처리” | `blur-radius` |
| 박스 그림자 색 | `gray` | `grey` |
| hover 색 | `gray` | `grey` |
| 마지막 문구 | `마우스를 올려보세요` | `마우스 올려 보세요` |
| HTML 구조 | 동일 | 동일 |
| CSS 결과 | 동일 | 동일 |
| 설명 정확성 | 친절하지만 blur 설명 보완 필요 | 짧지만 용어가 정확함 |
| 학습 성격 | 개인 복습 설명형 | 문법 중심 수업형 |

---

# 46. 원본 통합 개선 예제

## HTML

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
  >
  <title>CSS 그림자</title>
  <link
    rel="stylesheet"
    href="asset/css/shadow.css"
  >
</head>
<body>
  <main class="page">
    <h1>CSS 그림자</h1>

    <section>
      <h2>텍스트 그림자</h2>

      <p class="text-shadow-basic">
        한글 Shadow
      </p>

      <p class="text-shadow-blur">
        한글 Shadow
      </p>
    </section>

    <section>
      <h2>박스 그림자</h2>

      <div class="box-shadow-basic">
        박스 Shadow
      </div>

      <a
        class="shadow-card"
        href="/css"
      >
        CSS 학습 문서 보기
      </a>
    </section>
  </main>
</body>
</html>
```

## CSS

```css
:root {
  --shadow-sm:
    0 2px 6px
    rgb(0 0 0 / 16%);

  --shadow-md:
    0 10px 24px
    rgb(0 0 0 / 20%);
}

*,
*::before,
*::after {
  box-sizing: border-box;
}

body {
  margin: 0;
  color: #222;
  font-family: sans-serif;
}

.page {
  width: min(100% - 2rem, 50rem);
  margin-inline: auto;
  padding-block: 2rem;
}

.text-shadow-basic {
  text-shadow: 10px 3px red;
}

.text-shadow-blur {
  padding: 1rem;
  color: white;
  background-color: #222;
  font-size: 2rem;
  text-shadow:
    2px 2px 4px
    rgb(255 0 0 / 70%);
}

.box-shadow-basic {
  width: 10rem;
  padding: 1rem;
  border: 1px solid red;
  box-shadow: var(--shadow-sm);
}

.shadow-card {
  display: inline-block;
  width: 12rem;
  min-height: 10rem;
  margin-top: 2rem;
  padding: 1rem;
  border: 1px solid #d1d5db;
  color: inherit;
  text-decoration: none;
  transition:
    box-shadow 0.2s ease,
    transform 0.2s ease;
}

.shadow-card:hover,
.shadow-card:focus-visible {
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

.shadow-card:focus-visible {
  outline: 3px solid #2563eb;
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .shadow-card {
    transition: none;
  }

  .shadow-card:hover,
  .shadow-card:focus-visible {
    transform: none;
  }
}
```

---

# 47. 카드 그림자 실무 패턴

```css
.card {
  border:
    1px solid
    rgb(0 0 0 / 8%);
  border-radius: 1rem;
  background-color: white;
  box-shadow:
    0 1px 2px
    rgb(0 0 0 / 6%),
    0 8px 24px
    rgb(0 0 0 / 10%);
}
```

카드끼리 너무 가까우면 그림자가 겹쳐 탁해질 수 있습니다.

```css
.card-list {
  display: grid;
  gap: 2rem;
}
```

---

# 48. 드롭다운 그림자

```css
.dropdown {
  border:
    1px solid
    rgb(0 0 0 / 8%);
  background-color: white;
  box-shadow:
    0 12px 30px
    rgb(0 0 0 / 16%);
}
```

드롭다운의 실제 앞뒤 순서는 `z-index`와 stacking context가 담당합니다.

그림자는 시각적 깊이만 표현합니다.

---

# 49. 입력창 focus 효과

```css
.input {
  border: 1px solid #9ca3af;
}

.input:focus-visible {
  outline: none;
  border-color: #2563eb;
  box-shadow:
    0 0 0 3px
    rgb(37 99 235 / 25%);
}
```

`outline: none`을 사용했다면 대체 포커스 표시가 충분히 명확해야 합니다.

고대비 모드까지 고려하면 outline 유지가 더 안전할 수 있습니다.

---

# 50. 그림자가 보이지 않을 때 점검

1. 색상이 배경과 같은가?
2. alpha가 지나치게 낮은가?
3. 오프셋과 blur가 모두 `0`인가?
4. 부모 `overflow: hidden`에 잘리는가?
5. 다른 요소 뒤에 가려지는가?
6. `box-shadow: none`으로 덮였는가?
7. 선택자 명시도가 낮은가?
8. hover가 실제로 적용되는가?
9. 운영체제 고대비 설정이 영향을 주는가?
10. 개발자 도구에서 계산된 값을 확인했는가?

---

# 51. Hover 효과가 작동하지 않을 때 점검

1. 선택자 `.box2:hover`가 실제 클래스와 같은가?
2. 다른 요소가 위에서 포인터를 가로채는가?
3. `pointer-events: none`이 적용됐는가?
4. 터치 환경에서 테스트하는가?
5. hover 규칙이 뒤에서 덮였는가?
6. box-shadow 색상이 너무 연한가?
7. 부모 overflow에 잘리는가?
8. 요소 크기가 0인가?
9. 투명 요소가 위에 겹쳐 있는가?
10. 실제 클릭 요소라면 focus 상태도 확인했는가?

---

# 52. 자주 하는 실수

## 52.1 Blur를 투명도라고 이해

blur는 번짐이고 투명도는 색상의 alpha 값입니다.

## 52.2 흰색 텍스트에 흰색 배경

그림자만 보이고 글자 본체의 대비가 사라질 수 있습니다.

## 52.3 클릭되지 않는 div에 pointer

사용자가 클릭 기능을 기대하게 됩니다.

## 52.4 Hover만 상태 제공

키보드와 터치 환경에서 동일한 정보를 얻지 못할 수 있습니다.

## 52.5 그림자로 레이아웃 간격 기대

그림자는 주변 요소를 밀지 않습니다.

## 52.6 큰 blur 남용

성능 저하와 흐릿한 UI를 만들 수 있습니다.

## 52.7 부모 hidden에 그림자 잘림

카드 그림자가 경계에서 잘릴 수 있습니다.

## 52.8 그림자만으로 선택 상태 전달

아이콘, 텍스트, ARIA 상태를 함께 사용합니다.

## 52.9 `gray`와 `grey`를 오류로 처리

두 값은 같은 CSS 색상 키워드입니다.

## 52.10 포커스 outline 제거 후 대체 없음

키보드 사용자가 현재 위치를 알 수 없습니다.

---

# 53. 면접·복습 포인트

## Q1. `text-shadow`와 `box-shadow`의 차이는 무엇인가요?

`text-shadow`는 글자 모양에 그림자를 적용하고, `box-shadow`는 요소의 박스에 그림자를 적용합니다.

## Q2. 그림자 오프셋의 양수와 음수 방향은 무엇인가요?

수평 양수는 오른쪽, 음수는 왼쪽입니다. 수직 양수는 아래쪽, 음수는 위쪽입니다.

## Q3. Blur radius는 무엇을 하나요?

그림자 가장자리의 번짐 정도를 조절합니다. 투명도는 색상 alpha로 별도 지정합니다.

## Q4. `box-shadow`의 네 번째 길이값은 무엇인가요?

Spread radius이며 그림자 크기를 확장하거나 축소합니다.

## Q5. `inset`은 무엇인가요?

박스 바깥이 아닌 안쪽에 그림자를 그립니다.

## Q6. 그림자가 주변 레이아웃을 밀어내나요?

아닙니다. 그림자는 일반적으로 레이아웃 공간을 차지하지 않습니다.

## Q7. `gray`와 `grey`는 다른 색인가요?

CSS에서는 같은 색상 키워드입니다.

## Q8. Hover 카드에 focus 상태가 필요한 이유는 무엇인가요?

키보드 사용자는 hover를 사용할 수 없으므로 동일한 시각적 피드백과 명확한 포커스 표시가 필요합니다.

## Q9. 그림자와 `z-index`는 같은 개념인가요?

아닙니다. 그림자는 시각적 효과이고, 실제 레이어 순서는 stacking context와 `z-index`가 결정합니다.

## Q10. 큰 그림자 애니메이션의 문제는 무엇인가요?

넓은 영역을 다시 그려야 해 많은 요소에서 반복되면 렌더링 성능이 저하될 수 있습니다.

---

# Problems

## 문제 1. 기본 텍스트 그림자

글자를 오른쪽 `10px`, 아래 `3px` 이동한 빨간 그림자로 작성하세요.

## 문제 2. Blur 추가

오른쪽 `2px`, 아래 `2px`, blur `4px`, 빨간색 텍스트 그림자를 작성하세요.

## 문제 3. 음수 방향

왼쪽 `4px`, 위쪽 `2px`에 검정 그림자를 작성하세요.

## 문제 4. 투명 그림자

검정색 30% 불투명도의 `0 4px 8px` 텍스트 그림자를 작성하세요.

## 문제 5. 흰색 글자 대비

흰색 글자와 빨간 그림자가 읽히도록 어두운 배경을 추가하세요.

## 문제 6. 기본 박스 그림자

오른쪽 `4px`, 아래 `4px`, blur `6px`, 회색 박스 그림자를 작성하세요.

## 문제 7. Spread

오프셋 `0`, blur `8px`, spread `4px`, 검정 20% 박스 그림자를 작성하세요.

## 문제 8. Inset

입력창 안쪽에 `0 1px 3px` 검정 20% 그림자를 작성하세요.

## 문제 9. 다중 그림자

작은 그림자와 큰 그림자를 쉼표로 겹쳐 카드에 적용하세요.

## 문제 10. 원본 주석 수정

다음 설명을 정확하게 수정하세요.

```text
blur투명도처리
```

## 문제 11. Gray와 Grey

`gray`와 `grey`가 서로 다른 결과를 만드는지 설명하세요.

## 문제 12. Hover 카드

카드 hover 시 중간 크기 그림자가 나타나도록 작성하세요.

## 문제 13. Focus 상태

문제 12의 카드가 링크일 때 키보드 focus에도 같은 그림자와 outline을 제공하세요.

## 문제 14. Cursor

실제 클릭 기능이 없는 `div`에 `cursor: pointer`를 사용하는 문제를 설명하세요.

## 문제 15. 실제 요소

클릭 시 상세 페이지로 이동하는 카드에 적절한 HTML 요소를 작성하세요.

## 문제 16. 그림자 토큰

작은 그림자와 큰 그림자를 CSS 변수로 선언하세요.

## 문제 17. Overflow 잘림

부모의 `overflow: hidden` 때문에 그림자가 잘릴 때 해결 방향을 두 가지 작성하세요.

## 문제 18. 포커스 링

파란색 25% alpha를 사용하는 3px 포커스 링을 `box-shadow`로 작성하세요.

## 문제 19. 움직임 감소

hover 시 `translateY(-2px)` 전환을 사용하되 움직임 감소 환경에서는 이동과 transition을 제거하세요.

## 문제 20. 상태 전달

선택된 카드가 그림자만으로 상태를 전달하지 않도록 HTML과 ARIA 상태를 추가하세요.

## 문제 21. 성능

큰 blur 그림자를 수십 개 카드에서 계속 애니메이션할 때 발생할 수 있는 문제와 개선 방법을 작성하세요.

## 문제 22. 종합 카드

다음 요구사항을 만족하는 학습 카드 링크를 작성하세요.

- 실제 `<a>` 사용
- 기본 작은 그림자
- hover·focus 시 큰 그림자
- focus outline
- `transform` 이동
- 움직임 감소 대응
- CSS 변수로 그림자 관리
- `gray` 이름색 대신 alpha 색상
- 충분한 패딩
- 그림자가 레이아웃 간격을 대신하지 않도록 카드 목록에 `gap`

---

# Answers & Explanations

## 정답 1

```css
.text {
  text-shadow: 10px 3px red;
}
```

## 정답 2

```css
.text {
  text-shadow: 2px 2px 4px red;
}
```

## 정답 3

```css
.text {
  text-shadow: -4px -2px black;
}
```

## 정답 4

```css
.text {
  text-shadow:
    0 4px 8px
    rgb(0 0 0 / 30%);
}
```

## 정답 5

```css
.text {
  padding: 1rem;
  color: white;
  background-color: #222;
  text-shadow: 2px 2px 4px red;
}
```

## 정답 6

```css
.box {
  box-shadow: 4px 4px 6px gray;
}
```

`grey`도 같은 결과입니다.

## 정답 7

```css
.box {
  box-shadow:
    0 0 8px 4px
    rgb(0 0 0 / 20%);
}
```

## 정답 8

```css
.input {
  box-shadow:
    inset 0 1px 3px
    rgb(0 0 0 / 20%);
}
```

## 정답 9

```css
.card {
  box-shadow:
    0 1px 2px
    rgb(0 0 0 / 8%),
    0 8px 24px
    rgb(0 0 0 / 14%);
}
```

## 정답 10

```text
blur radius는 그림자의 가장자리를 흐리고 퍼뜨린다.
투명도는 색상의 alpha 값으로 조절한다.
```

## 정답 11

다른 결과를 만들지 않습니다. CSS의 `gray`와 `grey`는 같은 색상 키워드입니다.

## 정답 12

```css
.card:hover {
  box-shadow:
    0 8px 24px
    rgb(0 0 0 / 18%);
}
```

## 정답 13

```css
.card:hover,
.card:focus-visible {
  box-shadow:
    0 8px 24px
    rgb(0 0 0 / 18%);
}

.card:focus-visible {
  outline: 3px solid #2563eb;
  outline-offset: 3px;
}
```

## 정답 14

포인터 커서는 사용자가 클릭 가능한 요소라고 예상하게 만듭니다. 실제 동작이 없다면 오해를 유발하므로 기본 커서를 사용합니다.

## 정답 15

```html
<a class="card" href="/course/css">
  CSS 과정
</a>
```

## 정답 16

```css
:root {
  --shadow-sm:
    0 1px 2px
    rgb(0 0 0 / 8%);

  --shadow-lg:
    0 12px 30px
    rgb(0 0 0 / 18%);
}
```

## 정답 17

예:

```text
1. 불필요한 overflow: hidden을 제거한다.
2. 부모에 그림자가 들어갈 충분한 padding을 추가한다.
```

레이어 구조나 그림자 크기를 조정할 수도 있습니다.

## 정답 18

```css
.control:focus-visible {
  box-shadow:
    0 0 0 3px
    rgb(37 99 235 / 25%);
}
```

outline도 함께 유지하는 편이 안전합니다.

## 정답 19

```css
.card {
  transition:
    box-shadow 0.2s ease,
    transform 0.2s ease;
}

.card:hover,
.card:focus-visible {
  transform: translateY(-2px);
}

@media (prefers-reduced-motion: reduce) {
  .card {
    transition: none;
  }

  .card:hover,
  .card:focus-visible {
    transform: none;
  }
}
```

## 정답 20

```html
<button
  class="select-card"
  type="button"
  aria-pressed="true"
>
  <span aria-hidden="true">✓</span>
  선택됨
</button>
```

그림자 외에 아이콘, 텍스트, ARIA 상태를 제공합니다.

## 정답 21

큰 blur 그림자는 넓은 영역을 다시 그리게 해 스크롤과 애니메이션 성능을 떨어뜨릴 수 있습니다.

개선:

```text
- blur와 spread 크기를 줄인다.
- 동시에 애니메이션되는 요소 수를 제한한다.
- 기본 그림자는 작게 유지한다.
- 이동은 transform을 사용한다.
- 실제 모바일 기기에서 테스트한다.
```

## 정답 22

### HTML

```html
<div class="card-list">
  <a class="learning-card" href="/css/shadow">
    <h2>CSS 그림자</h2>
    <p>
      text-shadow와 box-shadow를 학습합니다.
    </p>
  </a>

  <a class="learning-card" href="/css/transform">
    <h2>CSS Transform</h2>
    <p>
      요소의 이동과 회전을 학습합니다.
    </p>
  </a>
</div>
```

### CSS

```css
:root {
  --shadow-sm:
    0 1px 3px
    rgb(0 0 0 / 10%);

  --shadow-lg:
    0 12px 30px
    rgb(0 0 0 / 20%);
}

.card-list {
  display: grid;
  gap: 2rem;
}

.learning-card {
  display: block;
  padding: 1.5rem;
  border:
    1px solid
    rgb(0 0 0 / 8%);
  border-radius: 1rem;
  color: inherit;
  text-decoration: none;
  box-shadow: var(--shadow-sm);
  transition:
    box-shadow 0.2s ease,
    transform 0.2s ease;
}

.learning-card:hover,
.learning-card:focus-visible {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
}

.learning-card:focus-visible {
  outline: 3px solid #2563eb;
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .learning-card {
    transition: none;
  }

  .learning-card:hover,
  .learning-card:focus-visible {
    transform: none;
  }
}
```

---

# Final Checklist

## Text shadow

- [ ] 수평·수직 오프셋 방향을 확인했다.
- [ ] blur radius와 투명도를 구분했다.
- [ ] 음수 blur를 사용하지 않았다.
- [ ] 흰색 글자와 배경의 대비를 확인했다.
- [ ] 작은 본문에 과도한 그림자를 적용하지 않았다.
- [ ] 다중 그림자의 가독성을 확인했다.

## Box shadow

- [ ] offset, blur, spread 순서를 확인했다.
- [ ] `inset`의 의미를 이해했다.
- [ ] 그림자가 레이아웃 공간을 차지하지 않음을 확인했다.
- [ ] 부모 overflow에 잘리지 않는지 확인했다.
- [ ] 카드 간격은 `gap`이나 margin으로 별도 지정했다.
- [ ] `gray`와 `grey`를 오류로 구분하지 않았다.

## 상호작용

- [ ] 실제 클릭 기능에 맞는 HTML 요소를 사용했다.
- [ ] 클릭 기능이 없는 div에 pointer를 사용하지 않았다.
- [ ] hover와 focus-visible을 함께 고려했다.
- [ ] 포커스 outline을 제거하지 않았다.
- [ ] 터치 환경에서도 기능을 사용할 수 있다.
- [ ] 움직임 감소 환경을 고려했다.

## 접근성과 상태

- [ ] 그림자만으로 선택 상태를 전달하지 않았다.
- [ ] 텍스트, 아이콘, 배경, ARIA 상태를 함께 검토했다.
- [ ] 텍스트 대비가 그림자 없이도 충분하다.
- [ ] 고대비 모드에서 포커스 표시를 확인했다.
- [ ] 장식 효과가 콘텐츠 읽기를 방해하지 않는다.

## 성능과 유지보수

- [ ] 큰 blur 그림자를 과도하게 사용하지 않았다.
- [ ] 많은 요소에서 그림자 애니메이션을 제한했다.
- [ ] 그림자 값을 CSS 변수로 관리했다.
- [ ] 이름 색상보다 alpha 색상을 검토했다.
- [ ] 다크 모드에서 그림자가 보이는지 확인했다.
- [ ] 실제 저사양 모바일 환경에서 테스트했다.

## 원본 코드 검수

- [ ] `lang="en"`을 `lang="ko"`로 개선했다.
- [ ] `Document` 제목을 학습 주제로 변경했다.
- [ ] 내 코드의 `blur투명도처리` 설명을 보완했다.
- [ ] 흰색 글자의 배경 대비 문제를 설명했다.
- [ ] `.box2`의 pointer와 실제 동작 불일치를 설명했다.
- [ ] hover 전용 상태를 focus까지 확장했다.
- [ ] `gray`와 `grey` 차이를 오류로 처리하지 않았다.
- [ ] 내 코드와 강사님의 마지막 문구 차이를 보존했다.

---

# Key Summary

- `text-shadow`는 글자에, `box-shadow`는 요소 박스에 그림자를 적용한다.
- 수평 오프셋 양수는 오른쪽, 음수는 왼쪽이다.
- 수직 오프셋 양수는 아래쪽, 음수는 위쪽이다.
- blur radius는 그림자를 흐리고 퍼뜨리며 음수를 사용할 수 없다.
- blur는 투명도 자체가 아니며 투명도는 색상의 alpha 값으로 조절한다.
- 내 코드의 `blur투명도처리` 주석은 이 차이를 보완해야 한다.
- 원본 `.red`는 오른쪽 10px, 아래 3px의 선명한 빨간 그림자를 만든다.
- 원본 `.blur`는 오른쪽 2px, 아래 2px, blur 4px의 빨간 그림자를 만든다.
- `.blur`의 흰색 글자는 기본 흰 배경에서 대비가 부족할 수 있다.
- `box-shadow`는 offset, blur, spread, color 순서로 작성할 수 있다.
- 원본 박스 그림자는 오른쪽 4px, 아래 4px, blur 6px이다.
- 내 코드의 `gray`와 강사님의 `grey`는 같은 CSS 색상이다.
- spread radius는 그림자 영역을 확장하거나 축소한다.
- `inset`은 박스 안쪽 그림자를 만든다.
- 여러 그림자는 쉼표로 겹쳐 사용할 수 있다.
- 그림자는 레이아웃 공간을 차지하지 않으므로 카드 간격을 대신하지 않는다.
- 부모의 `overflow: hidden`은 그림자를 잘라낼 수 있다.
- 원본 `.box2`는 hover 시 그림자와 pointer가 나타나지만 실제 클릭 동작이 없다.
- 실제 클릭 UI에는 `a` 또는 `button`을 사용한다.
- hover 효과는 키보드 사용자를 위해 `:focus-visible`과 함께 제공한다.
- 그림자만으로 선택이나 오류 상태를 전달하지 않는다.
- 큰 blur 그림자를 많은 요소에서 애니메이션하면 렌더링 성능이 저하될 수 있다.
- 그림자 토큰을 CSS 변수로 관리하면 프로젝트의 시각적 깊이를 일관되게 유지할 수 있다.
