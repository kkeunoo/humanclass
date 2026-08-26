---
title: CSS Position과 요소 위치
version: v3.0-encyclopedia
last_updated: 2026-08-06
status: Completed
---

# CSS Position과 요소 위치

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `08_CSS_Position과_요소위치.md` |
| 분류 | `02_CSS` |
| 원본 기준 | `workspace_html/css/08_position.html`, `workspace_html/css/asset/css/08_position.css`, `workspace_teacher/workspace_html/css/08_position.html`, `workspace_teacher/workspace_html/css/asset/css/08_position.css` |
| 핵심 범위 | `static`, `relative`, `absolute`, `fixed`, `sticky`, 기준 박스, 오프셋, `z-index`, `calc()`, CSS 변수 |
| 프로젝트 연결 | 고정 메뉴, 맨 위로 버튼, 드롭다운, 배지, 모달, 카드 오버레이, 중앙 배치, 레이어 순서 |

> 이 문서는 내 코드와 강사님 코드의 `08_position.html`, `08_position.css`를 비교해 Normal Flow와 `static`, `relative`, `absolute`, `fixed`, `sticky`의 위치 계산 방식을 정리한다. 기준 박스·Offset·Stacking Context 설명을 정확하게 보완하고, 배지·드롭다운·모달·고정 버튼 같은 실무 배치 패턴으로 연결한다.

---

# 학습 목표

- 일반 문서 흐름과 위치 지정 요소의 차이를 설명한다.
- `position: static`의 기본 동작을 이해한다.
- `relative`가 원래 공간을 유지한 채 시각적으로 이동한다는 점을 설명한다.
- `absolute`가 일반 흐름에서 빠지고 containing block을 기준으로 배치된다는 점을 이해한다.
- 절대 위치 요소의 기준 부모를 만드는 방법을 작성한다.
- `top`, `right`, `bottom`, `left`, `inset`을 구분한다.
- `fixed`가 일반적으로 뷰포트를 기준으로 고정되는 원리를 설명한다.
- `sticky`가 임계 위치에 도달한 뒤 스크롤 컨테이너 안에서 고정되는 조건을 설명한다.
- 위치 지정 요소의 박스가 blockification되는 의미를 이해한다.
- `z-index`와 stacking context의 관계를 설명한다.
- 단순히 큰 `z-index`만 지정해도 항상 앞으로 나오지 않는 이유를 이해한다.
- 인접 형제 선택자와 `:hover`로 만든 원본 서브메뉴의 한계를 설명한다.
- `calc()`로 중앙 위치를 계산하고 `transform` 방식과 비교한다.
- CSS 사용자 지정 속성으로 공통 색상을 관리한다.
- 내 코드와 강사님 코드의 차이와 원본 오류를 찾는다.
- 개발자 도구로 기준 박스, 오프셋, 레이어 순서를 확인한다.

---

# 1. 위치 지정이란?

일반적인 HTML 요소는 문서에 작성된 순서대로 배치됩니다.

```html
<div>첫 번째</div>
<div>두 번째</div>
<div>세 번째</div>
```

CSS의 `position` 속성은 요소가 어떤 기준으로 위치를 계산할지를 변경합니다.

대표 값:

```css
position: static;
position: relative;
position: absolute;
position: fixed;
position: sticky;
```

각 값은 다음 항목에 영향을 줍니다.

- 일반 문서 흐름에 남는가
- 원래 공간이 유지되는가
- 어느 박스를 기준으로 이동하는가
- 스크롤할 때 어떻게 움직이는가
- `z-index`를 어떻게 사용할 수 있는가

---

# 2. 원본 실습 구조

원본 HTML은 다음 순서로 위치 속성을 비교합니다.

1. 위치 속성이 없는 `LOVE`
2. `relative`가 적용된 `O`
3. `absolute`가 적용된 `O`, `E`
4. `relative` 부모 안의 `absolute`
5. 화면 오른쪽 아래의 `fixed` 맨 위로 버튼
6. 상단에 붙는 `sticky` 메뉴
7. 겹친 박스의 `z-index`
8. 메뉴와 인접한 서브메뉴
9. 부모 안의 자식 중앙 정렬
10. `:root` CSS 변수

이 구조는 위치 기준과 레이어 순서를 한 문서에서 단계적으로 확인하기 좋습니다.

---

# 3. 기본 LOVE 박스

원본 HTML:

```html
<div class="parent">
  <div>L</div>
  <div>O</div>
  <div>V</div>
  <div>E</div>
</div>
```

원본 CSS:

```css
.parent div {
  display: inline-block;
  width: 50px;
  height: 50px;
  border: 1px solid red;
  line-height: 50px;
  text-align: center;
  background: aqua;
}
```

각 글자는 `inline-block`이므로 같은 줄에 나란히 배치됩니다.

```text
L O V E
```

이 기본 결과를 기준으로 `relative`와 `absolute`가 문서 흐름에 어떤 차이를 만드는지 비교합니다.

---

# 4. `position: static`

`static`은 대부분 요소의 기본 위치 방식입니다.

```css
.box {
  position: static;
}
```

특징:

- 일반 문서 흐름에 따라 배치된다.
- `top`, `right`, `bottom`, `left` 오프셋이 적용되지 않는다.
- 위치 기준 부모 역할을 하지 않는다.
- 요소의 원래 자리를 그대로 사용한다.

원본에는 `static`을 직접 선언하지 않았지만 첫 번째 LOVE 박스가 기본 상태의 비교 대상입니다.

---

# 5. 오프셋 속성

위치 지정 요소는 다음 속성으로 이동하거나 고정 위치를 정합니다.

```css
top: 20px;
right: 20px;
bottom: 20px;
left: 20px;
```

논리적 단축 속성:

```css
inset: 20px;
```

이는 다음과 같습니다.

```css
top: 20px;
right: 20px;
bottom: 20px;
left: 20px;
```

축별 속성:

```css
inset-block: 20px;
inset-inline: 20px;
```

원본에서는 `top`, `left`, `right`, `bottom`을 직접 사용합니다.

---

# 6. `position: relative`

원본:

```css
.parent .relative {
  position: relative;
  top: -20px;
  left: 10px;
}
```

원래 위치를 기준으로 다음과 같이 이동합니다.

```text
위로 20px
오른쪽으로 10px
```

`top: -20px`은 위로 이동합니다.

`left: 10px`은 원래 왼쪽 위치에서 오른쪽으로 이동합니다.

---

# 7. `relative`의 원래 공간

원본 내 코드 주석:

```text
relative는 원래 위치를 기준으로 이동함
가지고 있던 공간은 유지됨
```

핵심적으로 정확합니다.

`O`가 시각적으로 이동해도 원래 `O`가 차지하던 자리에는 다른 요소가 들어오지 않습니다.

```text
문서 흐름:
L [O의 원래 자리] V E

화면 표시:
   O가 위·오른쪽으로 이동
```

따라서 이동한 `O`가 다른 요소와 겹칠 수 있습니다.

---

# 8. `relative`는 레이아웃 재배치가 아니다

```css
.box {
  position: relative;
  left: 100px;
}
```

요소가 오른쪽으로 이동해 보여도 다음 형제 요소는 원래 위치를 기준으로 배치됩니다.

즉, `relative` 이동은 일반 흐름의 자리 계산을 다시 하지 않습니다.

요소 사이의 실제 간격을 바꾸려는 목적이면 다음을 우선 검토합니다.

- `margin`
- `padding`
- Flexbox
- Grid
- `gap`

`relative`는 다음과 같은 작은 시각적 이동에 적합합니다.

- 아이콘 미세 조정
- 배지 위치 조정
- 가상 요소 위치 기준
- 절대 위치 자식의 containing block 설정

---

# 9. 퍼센트 오프셋 보완

내 코드 주석:

```text
%로 주는것은 부모크기에 대한 %로 나를 기준해서 그대로 밀림
```

`relative`의 퍼센트 오프셋은 일반적으로 containing block의 크기를 기준으로 계산합니다.

```css
.relative {
  position: relative;
  left: 50%;
}
```

`left: 50%`는 요소 자신의 너비 절반만큼 이동한다는 뜻이 아닙니다.

가로 퍼센트 오프셋은 containing block의 너비를 기준으로 계산합니다.

요소 자신의 크기까지 고려해 가운데를 맞추려면 다음을 함께 사용할 수 있습니다.

```css
.box {
  position: relative;
  left: 50%;
  transform: translateX(-50%);
}
```

다만 일반 가운데 정렬에는 Flexbox, Grid, 자동 마진이 더 명확할 수 있습니다.

---

# 10. `position: absolute`

원본:

```css
.parent .absolute {
  position: absolute;
  top: 30px;
  left: 0;
}
```

특징:

- 일반 문서 흐름에서 빠진다.
- 원래 차지하던 공간이 사라진다.
- 다른 형제 요소는 해당 요소가 없는 것처럼 배치될 수 있다.
- 기준이 되는 containing block을 따라 오프셋을 계산한다.
- 다른 콘텐츠와 겹칠 수 있다.

원본에서 `O`가 흐름에서 빠지므로 `V`와 `E`가 왼쪽으로 당겨질 수 있습니다.

---

# 11. 원본의 중복 `top`

내 코드와 강사님 코드:

```css
position: absolute;
top: 0;
left: 0;

top: 30px;
```

같은 규칙 안에서 `top`이 두 번 선언되었습니다.

같은 중요도와 명시도이므로 뒤의 선언이 적용됩니다.

최종값:

```css
top: 30px;
left: 0;
```

앞의 `top: 0`은 실험 과정의 값으로 볼 수 있습니다.

최종 코드에서는 필요한 값 하나만 남깁니다.

---

# 12. 절대 위치의 기준 박스

원본 주석:

```text
부모중에 relative 등 static이 아닌 것 기준으로 이동
```

핵심 방향은 맞습니다.

정확한 설명:

- 가까운 조상 중 위치가 지정된 조상을 containing block으로 사용한다.
- 여기서 위치가 지정됐다는 것은 일반적으로 `position`이 `static`이 아닌 경우를 뜻한다.
- 특정 `transform`, `filter`, `contain` 등의 속성도 containing block을 만들 수 있다.
- 적절한 조상이 없으면 초기 containing block을 기준으로 배치된다.

입문 단계에서 가장 자주 사용하는 패턴:

```css
.parent {
  position: relative;
}

.child {
  position: absolute;
  top: 0;
  left: 0;
}
```

---

# 13. “부모가 없으면 body 기준” 설명 보완

원본 주석:

```text
이러한 부모가 없을 경우 body 기준
```

입문 실습에서는 화면상 `body`를 기준으로 움직이는 것처럼 보일 수 있습니다.

그러나 정확히는 항상 `body` 요소 자체를 기준으로 하는 것이 아니라 초기 containing block을 기준으로 계산합니다.

초기 containing block은 일반적으로 뷰포트와 관련된 기준 영역입니다.

복습 문서에서는 다음처럼 기억합니다.

```text
가까운 positioned 조상
→ 없으면 초기 containing block
```

---

# 14. 위치 기준 부모 만들기

원본:

```css
.rel {
  position: relative;
}
```

HTML:

```html
<div class="parent rel">
  <div>L</div>
  <div class="absolute">O</div>
  <div>V</div>
  <div class="abs-b">E</div>
</div>
```

`.parent.rel`은 절대 위치 자식의 기준이 됩니다.

```css
.parent.rel {
  position: relative;
}
```

`O`:

```css
.absolute {
  position: absolute;
  top: 30px;
  left: 0;
}
```

`E`:

```css
.abs-b {
  position: absolute;
  right: 0;
  bottom: 0;
}
```

두 요소 모두 해당 부모의 패딩 박스를 기준으로 위치를 계산합니다.

---

# 15. `absolute`의 blockification

원본 주석:

```text
absolute는 주었을 때 inline-block으로 바뀜
```

정확한 표현은 “자동으로 `inline-block`이 된다”가 아닙니다.

절대 위치 요소의 바깥쪽 표시 유형은 blockification 규칙의 영향을 받습니다.

쉽게 말하면:

- 일반 인라인 요소도 위치 지정 박스처럼 크기를 가질 수 있다.
- 계산된 `display` 동작이 블록화될 수 있다.
- 이것을 단순히 `inline-block`으로 바뀐다고 고정해서 설명하면 부정확하다.

입문 단계에서는 다음처럼 기억할 수 있습니다.

```text
absolute 요소는 일반 인라인 흐름에서 빠지고
독립적인 위치 지정 박스처럼 동작한다.
```

---

# 16. 절대 위치 남용 주석 보완

내 코드 주석:

```text
하나를 absolute를 주면 하위 자식까지 absolute를 주어야 함
```

이는 일반 규칙이 아닙니다.

절대 위치 요소의 자식은 기본적으로 정상적인 내부 문서 흐름을 유지할 수 있습니다.

```css
.card-badge {
  position: absolute;
}
```

```html
<div class="card-badge">
  <span>NEW</span>
  <strong>새 과정</strong>
</div>
```

내부 `span`, `strong`에 `absolute`를 줄 필요가 없습니다.

올바른 주의점:

- 모든 레이아웃을 좌표로 만들면 반응형 대응이 어려워진다.
- 일반적인 행·열 배치는 Flexbox나 Grid를 사용한다.
- 오버레이, 배지, 모서리 아이콘 등 명확한 겹침에 사용한다.

---

# 17. 오른쪽 아래 절대 배치

원본:

```css
.parent .abs-b {
  position: absolute;
  right: 0;
  bottom: 0;
}
```

위치 기준 조상이 없는 세 번째 LOVE 실습에서는 초기 containing block의 오른쪽 아래를 기준으로 배치될 수 있습니다.

위치 기준 부모가 있는 네 번째 실습에서는 `.parent.rel`의 오른쪽 아래에 배치됩니다.

같은 CSS라도 기준 조상의 유무에 따라 결과가 크게 달라지는 중요한 예제입니다.

---

# 18. body 크기 확장

원본:

```css
body {
  width: 200vw;
  height: 200vh;
}
```

목적:

- 가로 스크롤 생성
- 세로 스크롤 생성
- `fixed`, `sticky`, 절대 위치의 스크롤 동작 확인

실무 페이지에서는 불필요한 `200vw`가 가로 스크롤을 만들 수 있으므로 테스트가 끝나면 제거합니다.

스크롤 실습 전용으로 명시하는 것이 좋습니다.

```css
/* position 스크롤 동작 확인용 */
body {
  min-height: 200vh;
}
```

가로 스크롤이 꼭 필요하지 않다면 `width: 200vw`는 제거합니다.

---

# 19. `position: fixed`

원본:

```css
.fixed {
  position: fixed;
  right: 10px;
  bottom: 10px;
  width: 60px;
  height: 60px;
}
```

스크롤과 관계없이 화면 오른쪽 아래에 보이는 맨 위로 버튼입니다.

```html
<div class="fixed">
  <a href="#top">맨 위로</a>
</div>
```

일반적으로 뷰포트를 기준으로 위치를 계산합니다.

---

# 20. `fixed`의 일반 흐름

`fixed` 요소도 일반 문서 흐름에서 빠집니다.

따라서 원래 공간이 유지되지 않습니다.

다른 콘텐츠 위에 겹칠 수 있습니다.

```css
.back-to-top {
  position: fixed;
  right: 1rem;
  bottom: 1rem;
}
```

본문의 마지막 버튼이나 중요한 콘텐츠를 가리지 않도록 여백을 확보해야 합니다.

```css
body {
  padding-bottom: 6rem;
}
```

---

# 21. `fixed`도 inline-block인가?

원본 주석:

```text
fixed 도 inline-block요소로 변경됨
```

`absolute`와 마찬가지로 단순히 `inline-block`이 된다고 설명하는 것은 부정확합니다.

위치 지정에 따라 요소의 표시 유형이 blockification될 수 있으며 일반 흐름에서 독립적인 위치 지정 박스로 동작합니다.

정확한 복습 표현:

```text
fixed 요소는 일반 흐름에서 빠지고
고정 위치 박스처럼 동작한다.
```

---

# 22. 고정 맨 위로 링크 접근성

원본 링크:

```html
<a href="#top">맨 위로</a>
```

`body`에 `id="top"`이 있으므로 문서 위쪽으로 이동합니다.

개선:

```html
<a class="back-to-top" href="#top">
  맨 위로
</a>
```

```css
.back-to-top {
  display: inline-flex;
  position: fixed;
  right: 1rem;
  bottom: 1rem;
  min-width: 44px;
  min-height: 44px;
  align-items: center;
  justify-content: center;
}
```

확인 항목:

- 키보드 포커스 표시
- 충분한 클릭 영역
- 본문을 가리지 않는 위치
- 모바일 안전 영역
- 스크롤 시 항상 필요한지 여부

---

# 23. 모바일 안전 영역

스마트폰의 하단 홈 표시 영역을 고려할 수 있습니다.

```css
.back-to-top {
  right: 1rem;
  bottom:
    calc(1rem + env(safe-area-inset-bottom));
}
```

원본에는 없는 확장 학습입니다.

---

# 24. `position: sticky`

원본:

```css
.sticky {
  position: sticky;
  top: 0;
  top: 50px;
}
```

동일 속성이 두 번 선언되어 뒤의 값이 적용됩니다.

최종값:

```css
top: 50px;
```

요소가 스크롤되다가 뷰포트 상단에서 `50px` 위치에 도달하면 그 위치에 붙어 보입니다.

---

# 25. sticky의 동작 조건

`position: sticky`가 작동하려면 다음을 확인합니다.

- `top`, `bottom` 등 임계 오프셋이 지정되어 있는가
- 스크롤할 충분한 공간이 있는가
- 조상 요소의 높이가 너무 짧지 않은가
- 조상의 `overflow`가 별도 스크롤 컨테이너를 만들지 않았는가
- sticky 요소가 자신의 컨테이너 경계를 벗어나지 않는가

원본에서는 `body` 높이가 `200vh`이므로 세로 스크롤 공간이 있습니다.

---

# 26. sticky는 fixed와 완전히 같지 않다

| 구분 | `fixed` | `sticky` |
| --- | --- | --- |
| 일반 흐름 | 빠짐 | 원래 공간 유지 |
| 기준 | 일반적으로 뷰포트 | 스크롤 컨테이너와 containing block |
| 시작부터 고정 | 예 | 임계 위치 도달 후 |
| 부모 경계 | 일반적으로 무관 | 부모 경계 안에서 동작 |
| 대표 용도 | 플로팅 버튼, 모달 | 표 헤더, 섹션 메뉴 |

sticky 요소는 처음에는 일반 흐름에 있다가 임계점에서 고정되는 혼합 방식으로 이해할 수 있습니다.

---

# 27. sticky 메뉴 개선

```css
.sticky-menu {
  position: sticky;
  z-index: 10;
  top: 0;
  padding: 1rem;
  background-color: white;
  border-bottom: 1px solid #ddd;
}
```

배경색이 없으면 뒤의 콘텐츠가 비쳐 읽기 어려울 수 있습니다.

`z-index`가 없으면 다른 위치 지정 요소 아래로 들어갈 수 있습니다.

---

# 28. `z-index`

원본:

```css
.z1 {
  z-index: 2;
}

.z2 {
  z-index: 300;
}

.z3 {
  z-index: 99;
}
```

세 박스는 `.rel` 클래스로 다음을 공유합니다.

```css
.rel {
  position: relative;
}
```

서로 겹치는 영역에서 일반적으로 더 큰 `z-index`가 위에 표시됩니다.

```text
z2: 300
z3: 99
z1: 2
```

---

# 29. 원본 겹침 위치

```css
.z1 {
  top: 5px;
  left: 20px;
}

.z2 {
  top: -10px;
  left: 10px;
}

.z3 {
  top: -70px;
  left: 40px;
}
```

각 요소는 `position: relative`이므로 원래 공간을 유지하면서 시각적으로 이동합니다.

음수 `top`으로 위쪽 요소들과 겹치게 만든 뒤 `z-index` 순서를 관찰합니다.

---

# 30. 원본 `z-index` 주석 보완

내 코드 주석:

```text
z-index는 레이어의 순서를 변경해줌 (position에서만)
```

입문 설명으로는 이해하기 쉽지만 완전한 규칙은 아닙니다.

`z-index`는 다음 요소에서도 의미를 가질 수 있습니다.

- 위치 지정 요소
- Flex 항목
- Grid 항목
- stacking context 참여 요소

중요한 개념은 `position` 하나가 아니라 stacking context입니다.

---

# 31. stacking context란?

stacking context는 자식 레이어 순서를 하나의 그룹 안에서 계산하는 독립적인 쌓임 문맥입니다.

다음 속성들이 새 stacking context를 만들 수 있습니다.

- 위치 지정 요소와 특정 `z-index`
- `position: fixed`
- `position: sticky`
- `opacity`가 1보다 작음
- `transform`
- `filter`
- `isolation: isolate`
- 일부 `contain` 값

한 stacking context 안에서 매우 큰 `z-index`를 지정해도 부모 stacking context 자체가 다른 그룹 아래에 있으면 화면 최상단으로 나오지 못할 수 있습니다.

---

# 32. 큰 숫자가 항상 이기지 않는 이유

```css
.parent-a {
  position: relative;
  z-index: 1;
}

.parent-b {
  position: relative;
  z-index: 2;
}

.child-a {
  position: absolute;
  z-index: 9999;
}
```

`child-a`는 `parent-a`의 stacking context 안에 있습니다.

`parent-a` 전체가 `parent-b`보다 아래라면 `child-a`의 `9999`가 `parent-b` 위로 나오지 못할 수 있습니다.

따라서 `z-index` 문제는 부모 stacking context부터 확인합니다.

---

# 33. hover 시 레이어 변경

원본:

```css
.rel:hover {
  z-index: 999;
}
```

마우스를 올린 상대 위치 박스가 위로 올라옵니다.

키보드 접근이 필요한 요소라면 `:focus-visible`도 함께 고려합니다.

```css
.layer-item:hover,
.layer-item:focus-visible {
  z-index: 999;
}
```

단순 `div`가 포커스를 받게 만들기보다 실제 링크나 버튼을 사용하는 것이 좋습니다.

---

# 34. 메뉴와 서브메뉴 구조

원본:

```html
<div class="menu">
  메뉴1-0 메뉴2-0 메뉴3-0
</div>

<div class="submenu">
  메뉴1-1 메뉴2-1 메뉴3-1<br>
  메뉴1-2 메뉴2-2 메뉴3-2
</div>
```

CSS:

```css
.submenu {
  display: none;
}

.menu:hover + .submenu {
  display: block;
  position: relative;
}
```

`+`는 인접 형제 선택자입니다.

`.menu` 바로 다음에 있는 `.submenu`만 선택합니다.

---

# 35. 내 코드와 강사님의 서브메뉴 차이

내 코드:

```css
.menu:hover + .submenu {
  top: 1px;
}
```

강사님 코드:

```css
.menu:hover + .submenu {
  top: -1px;
}
```

두 코드의 실제 결과가 다른 지점입니다.

- 내 코드: 아래로 1px 이동
- 강사님 코드: 위로 1px 이동

테두리 사이의 틈이나 겹침을 조정하려는 실험으로 볼 수 있습니다.

오류로 단정하기보다 시각적 의도 차이로 보존합니다.

---

# 36. hover 서브메뉴의 문제점

원본 방식은 마우스가 `.menu`를 벗어나는 순간 조건이 해제될 수 있습니다.

```text
.menu:hover + .submenu
```

서브메뉴 위로 마우스를 이동할 때 메뉴와 서브메뉴 사이에 작은 틈이 있으면 바로 닫힐 수 있습니다.

또한 다음 문제가 있습니다.

- 키보드로 열기 어려움
- 터치 환경에서 hover가 불안정함
- 메뉴 상태를 보조 기술에 전달하지 않음
- `div`라서 본래 메뉴 의미가 없음
- 서브메뉴 안에 실제 링크가 없음

실무 메뉴에는 버튼, 링크, 리스트, JavaScript 상태 관리가 필요합니다.

---

# 37. CSS hover 영역 개선

메뉴와 서브메뉴를 하나의 부모 안에 묶으면 hover 영역을 유지할 수 있습니다.

```html
<div class="menu-item">
  <button type="button">
    메뉴
  </button>

  <div class="submenu">
    서브메뉴
  </div>
</div>
```

```css
.menu-item {
  position: relative;
}

.submenu {
  display: none;
  position: absolute;
  top: 100%;
  left: 0;
}

.menu-item:hover .submenu,
.menu-item:focus-within .submenu {
  display: block;
}
```

이 방식도 복잡한 메뉴의 모든 접근성 요구를 자동 해결하지는 않습니다.

---

# 38. 접근 가능한 메뉴 토글

```html
<button
  class="menu-button"
  type="button"
  aria-expanded="false"
  aria-controls="submenu"
>
  메뉴
</button>

<nav id="submenu" hidden>
  <a href="/menu/1">메뉴 1</a>
  <a href="/menu/2">메뉴 2</a>
</nav>
```

JavaScript로 `hidden`과 `aria-expanded`를 동기화합니다.

드롭다운의 시각적 위치에는 `absolute`를 사용할 수 있지만 열림 상태는 버튼과 스크립트로 관리하는 것이 안전합니다.

---

# 39. 부모 안의 자식 박스

원본:

```css
.p1 {
  position: relative;
  width: 400px;
  height: 400px;
}
```

```css
.c1 {
  position: absolute;
  width: 100px;
  height: 100px;
}
```

HTML:

```html
<div class="p1">
  부모 박스
  <div class="c1">
    자식 박스
  </div>
</div>
```

`.p1`이 위치 기준 부모이고 `.c1`이 절대 위치 자식입니다.

---

# 40. 원본 중앙 계산

```css
.c1 {
  top: calc(400px / 2 - 100px / 2);
  left: calc(50% - (100px / 2));
}
```

세로 계산:

```text
부모 높이 절반 - 자식 높이 절반
400px / 2 - 100px / 2
= 200px - 50px
= 150px
```

가로 계산:

```text
부모 너비의 50% - 자식 너비 절반
50% - 50px
```

자식 박스의 왼쪽 위 모서리가 중앙점보다 자신의 절반만큼 위·왼쪽에 위치하므로 중앙에 배치됩니다.

---

# 41. 강사님 세미콜론 누락

강사님 코드:

```css
left: calc(50% - (100px / 2))
```

규칙의 마지막 선언이므로 브라우저가 처리할 수 있지만 세미콜론을 작성하는 것이 좋습니다.

```css
left: calc(50% - (100px / 2));
```

내 코드는 세미콜론이 있습니다.

---

# 42. `calc()` 공백

내 코드 주석:

```text
더하기나 빼기는 앞 뒤로 띄어쓰기 해야 함
```

중요한 문법입니다.

```css
/* 권장 */
width: calc(100% - 2rem);
```

```css
/* 파싱 문제가 생길 수 있음 */
width: calc(100%-2rem);
```

곱셈과 나눗셈 지원 여부와 문법은 브라우저 수준에 따라 확인해야 합니다.

원본은 다음처럼 나눗셈을 사용합니다.

```text
calc(400px / 2 - 100px / 2)
```

최신 환경에서는 지원될 수 있지만 호환성이 필요한 코드에서는 미리 계산한 값이나 다른 중앙 정렬 방식을 검토합니다.

---

# 43. 고정값 계산의 유지보수 문제

원본:

```css
top: calc(400px / 2 - 100px / 2);
```

부모나 자식 크기가 바뀌면 계산식도 함께 수정해야 할 수 있습니다.

```css
.p1 {
  width: 500px;
  height: 500px;
}
```

이때 기존 `400px` 계산은 더 이상 중앙이 아닙니다.

크기에 독립적인 방법이 더 유지보수하기 쉽습니다.

---

# 44. `transform` 중앙 정렬

```css
.parent {
  position: relative;
}

.child {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
```

계산 원리:

1. 자식의 왼쪽 위 모서리를 부모 중앙에 배치
2. 자식 자신의 너비·높이 절반만큼 되돌림

장점:

- 부모와 자식의 고정 크기를 몰라도 됨
- 반응형 크기에 대응
- 원본 `calc()`보다 유지보수하기 쉬움

---

# 45. Flexbox 중앙 정렬

겹침이 필요하지 않다면 위치 속성보다 Flexbox가 더 단순합니다.

```css
.parent {
  display: flex;
  min-height: 400px;
  align-items: center;
  justify-content: center;
}
```

Grid:

```css
.parent {
  display: grid;
  min-height: 400px;
  place-items: center;
}
```

선택 기준:

| 목적 | 권장 |
| --- | --- |
| 일반 레이아웃 중앙 정렬 | Flex/Grid |
| 다른 콘텐츠 위에 겹치는 자식 | absolute |
| 모서리 배지 | absolute |
| 화면 고정 버튼 | fixed |

---

# 46. CSS 사용자 지정 속성

원본:

```css
:root {
  --box-color: brown;
}
```

사용:

```css
.p1 {
  background: var(--box-color);
}

.c1 {
  background: var(--box-color);
}
```

한 곳의 값을 수정하면 여러 요소가 함께 변경됩니다.

```css
:root {
  --box-color: royalblue;
}
```

---

# 47. 변수 이름과 범위

전역 변수:

```css
:root {
  --color-box: brown;
}
```

컴포넌트 범위:

```css
.card {
  --card-accent: royalblue;
}
```

```css
.card__badge {
  background-color: var(--card-accent);
}
```

이름은 값보다 역할을 나타내는 것이 좋습니다.

```css
/* 값 중심 */
--brown: brown;

/* 역할 중심 */
--color-box: brown;
```

---

# 48. 변수 fallback

```css
.box {
  background-color:
    var(--box-color, brown);
}
```

`--box-color`이 정의되지 않았으면 `brown`을 사용합니다.

원본에는 없는 확장 학습입니다.

---

# 49. 내 코드 분석

## 49.1 장점

- `relative`가 원래 위치를 기준으로 이동하고 공간을 유지한다고 설명했다.
- `absolute`가 일반 흐름에서 빠진다고 기록했다.
- 위치 기준 부모의 개념을 설명했다.
- `absolute`, `fixed` 남용이 반응형에서 어려울 수 있음을 경고했다.
- `fixed`와 `sticky`의 스크롤 차이를 설명했다.
- `z-index`가 레이어 순서를 바꾼다고 기록했다.
- 서브메뉴에 인접 형제 선택자를 사용했다.
- `calc()`의 연산자 공백 규칙을 설명했다.
- CSS 사용자 지정 속성의 선언과 사용을 기록했다.
- 강사님 코드보다 각 속성의 화면 결과에 대한 설명이 풍부하다.

---

# 50. 내 코드 개선점

## 50.1 문서 언어와 제목

```html
<html lang="en">
<title>Document</title>
```

개선:

```html
<html lang="ko">
<title>CSS Position</title>
```

## 50.2 “body 기준” 단정

기준 조상이 없으면 초기 containing block을 기준으로 한다고 보완합니다.

## 50.3 “inline-block으로 바뀜”

`absolute`, `fixed`는 blockification 규칙의 영향을 받는다고 설명해야 합니다.

## 50.4 모든 자식도 absolute라는 설명

절대 위치 요소의 자식까지 절대 위치로 만들 필요는 없습니다.

## 50.5 퍼센트 오프셋 설명

`left: 50%`는 자신의 크기가 아니라 containing block 너비 기준입니다.

## 50.6 `z-index`는 position에서만

Flex/Grid 항목과 stacking context에서도 사용할 수 있으므로 보완합니다.

## 50.7 `top` 중복 선언

```css
top: 0;
top: 30px;
```

최종값 하나만 남깁니다.

## 50.8 sticky 중복 선언

```css
top: 0;
top: 50px;
```

최종 적용값은 `50px`임을 명확히 합니다.

## 50.9 가로 `200vw`

불필요한 가로 스크롤을 만들 수 있으므로 실습 후 제거합니다.

## 50.10 hover 전용 서브메뉴

키보드, 터치, 접근성 상태를 함께 설계해야 합니다.

---

# 51. 강사님 코드 분석

## 51.1 장점

- `relative`, `absolute`, 기준 부모 비교가 간결하다.
- 같은 LOVE 구조를 반복해 흐름 차이를 쉽게 관찰할 수 있다.
- `fixed`, `sticky`, `z-index`, 드롭다운, 중앙 정렬까지 한 파일에서 실습한다.
- `.right` 또는 복잡한 추가 클래스 없이 핵심 위치 속성에 집중한다.
- CSS 변수의 기본 선언과 재사용을 보여 준다.

---

# 52. 강사님 코드 개선점

## 52.1 문서 언어와 제목

내 코드와 동일하게 `lang="en"`, `Document`를 사용합니다.

## 52.2 `absolute` 기준 설명

“없으면 body 기준”을 초기 containing block으로 보완합니다.

## 52.3 “자동으로 inline-block”

정확한 CSS 표시 유형 설명이 아닙니다.

## 52.4 중복 `top`

`absolute`와 `sticky` 규칙에 같은 속성이 중복되어 있습니다.

## 52.5 `z-index` 설명 부족

stacking context와 부모 레이어의 영향을 설명하지 않습니다.

## 52.6 서브메뉴 `top: -1px`

시각적 조정값이므로 목적을 주석으로 남기면 좋습니다.

## 52.7 `calc()` 마지막 세미콜론

```css
left: calc(50% - (100px / 2))
```

뒤에 세미콜론을 추가합니다.

## 52.8 고정 크기 중앙 계산

부모와 자식 크기가 변경되면 식을 다시 수정해야 합니다.

## 52.9 hover 전용 메뉴

키보드와 터치 입력을 지원하지 못할 수 있습니다.

---

# 53. 내 코드와 강사님 코드 비교

| 비교 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 네 번째 LOVE 설명 | “relative 아래 absolute 부모기준” 텍스트 추가 | 별도 설명 텍스트 없음 |
| `relative` 주석 | 겹침과 퍼센트 설명 추가 | 핵심 두 줄 |
| `absolute` 주석 | 반응형 남용 경고 추가 | 핵심 흐름 설명 |
| `abs-b` 주석 | 스크롤·우측 하단 관련 주석 추가 | 코드 중심 |
| `fixed` 주석 | 스크롤 고정과 표시 유형 설명 | 코드만 |
| `sticky` 주석 | 틀 고정 비유 | 코드만 |
| `z-index` 주석 | 레이어 순서 설명 | 별도 주석 없음 |
| 서브메뉴 위치 | `top: 1px` | `top: -1px` |
| 중앙 계산 주석 | 공식과 공백 규칙 설명 | 코드 중심 |
| `calc()` 세미콜론 | 있음 | 마지막 세미콜론 없음 |
| 배경 속성 | `background` 단축형 | `background-color` |
| 학습 성격 | 상세 복습 노트형 | 간결한 수업 진행형 |

---

# 54. 원본 통합 개선 예제

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
  <title>CSS Position</title>
  <link
    rel="stylesheet"
    href="asset/css/position.css"
  >
</head>
<body id="top">
  <header class="site-header">
    <nav aria-label="주요 메뉴">
      <a href="#relative">Relative</a>
      <a href="#absolute">Absolute</a>
      <a href="#fixed">Fixed</a>
    </nav>
  </header>

  <main class="page">
    <section id="relative">
      <h1>CSS Position</h1>

      <div class="love">
        <span>L</span>
        <span class="love__relative">O</span>
        <span>V</span>
        <span>E</span>
      </div>
    </section>

    <section id="absolute">
      <div class="card">
        <h2>과정 카드</h2>
        <span class="card__badge">
          NEW
        </span>
      </div>
    </section>

    <section>
      <div class="center-box">
        <div class="center-box__item">
          중앙
        </div>
      </div>
    </section>
  </main>

  <a class="back-to-top" href="#top">
    맨 위로
  </a>
</body>
</html>
```

## CSS

```css
:root {
  --color-accent: #2563eb;
  --color-surface: #fff;
  --color-border: #d1d5db;
}

*,
*::before,
*::after {
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  margin: 0;
  min-height: 200vh;
  color: #222;
  font-family: sans-serif;
}

.site-header {
  position: sticky;
  z-index: 10;
  top: 0;
  padding: 1rem;
  background-color: var(--color-surface);
  border-bottom: 1px solid var(--color-border);
}

.page {
  width: min(100% - 2rem, 60rem);
  margin-inline: auto;
  padding-block: 3rem;
}

.love span {
  display: inline-grid;
  width: 3rem;
  aspect-ratio: 1;
  border: 1px solid #dc2626;
  background-color: aqua;
  place-items: center;
}

.love__relative {
  position: relative;
  top: -1rem;
  left: 0.5rem;
}

.card {
  position: relative;
  min-height: 12rem;
  padding: 1.5rem;
  border: 1px solid var(--color-border);
  border-radius: 1rem;
}

.card__badge {
  position: absolute;
  top: 1rem;
  right: 1rem;
  padding: 0.25rem 0.5rem;
  border-radius: 999px;
  color: white;
  background-color: var(--color-accent);
}

.center-box {
  display: grid;
  min-height: 20rem;
  border: 1px solid var(--color-border);
  place-items: center;
}

.back-to-top {
  display: inline-flex;
  position: fixed;
  right: 1rem;
  bottom:
    calc(1rem + env(safe-area-inset-bottom));
  z-index: 20;
  min-width: 3rem;
  min-height: 3rem;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  color: white;
  background-color: var(--color-accent);
}
```

---

# 55. 카드 배지 패턴

```css
.card {
  position: relative;
}

.card__badge {
  position: absolute;
  top: 0.75rem;
  right: 0.75rem;
}
```

`absolute`가 적절한 대표 상황입니다.

배지가 일반 카드 내용의 흐름을 밀지 않고 모서리에 겹쳐야 하기 때문입니다.

---

# 56. 이미지 오버레이 패턴

```css
.image-card {
  position: relative;
}

.image-card__caption {
  position: absolute;
  right: 0;
  bottom: 0;
  left: 0;
  padding: 1rem;
  color: white;
  background:
    linear-gradient(
      transparent,
      rgb(0 0 0 / 75%)
    );
}
```

`inset`을 사용할 수도 있습니다.

```css
.image-card__overlay {
  position: absolute;
  inset: 0;
}
```

---

# 57. 모달 기본 위치

```css
.modal {
  position: fixed;
  z-index: 1000;
  inset: 0;
  display: grid;
  background-color: rgb(0 0 0 / 50%);
  place-items: center;
}
```

주의:

- `z-index: 1000`만으로 항상 최상단이 되는 것은 아니다.
- 조상 stacking context를 확인한다.
- 포커스 관리와 배경 비활성화가 필요하다.
- 모달 패널이 화면보다 크면 스크롤 처리가 필요하다.

---

# 58. sticky 표 헤더

```css
.table-wrapper {
  max-height: 20rem;
  overflow: auto;
}

thead th {
  position: sticky;
  z-index: 1;
  top: 0;
  background-color: white;
}
```

sticky의 기준 스크롤 컨테이너는 `.table-wrapper`가 됩니다.

원본의 body 스크롤 sticky와 다른 실무 사용 예입니다.

---

# 59. 개발자 도구 확인 항목

Elements와 Computed 패널에서 다음을 확인합니다.

- 계산된 `position`
- `top`, `right`, `bottom`, `left`
- containing block
- 원래 공간의 유지 여부
- `z-index`
- stacking context 생성 원인
- 중복 선언의 취소선
- `calc()`의 최종 계산값
- CSS 변수의 실제 값

브라우저의 Layout 또는 Layers 도구가 제공된다면 레이어 순서를 시각적으로 확인할 수 있습니다.

---

# 60. absolute가 엉뚱한 곳에 갈 때 점검

1. 원하는 부모에 `position: relative`가 있는가?
2. 더 가까운 조상 중 positioned 요소가 있는가?
3. 조상에 `transform`이 있는가?
4. `top`, `left`가 중복 선언됐는가?
5. 퍼센트 기준을 자신의 크기로 오해했는가?
6. 부모의 패딩을 고려했는가?
7. 요소가 초기 containing block을 기준으로 하는가?
8. 스크롤 컨테이너가 달라졌는가?
9. 미디어 쿼리에서 위치값이 덮였는가?
10. 개발자 도구에서 containing block을 확인했는가?

---

# 61. sticky가 작동하지 않을 때 점검

1. `top` 또는 다른 임계 오프셋이 있는가?
2. 스크롤할 공간이 충분한가?
3. 부모 높이가 sticky 요소보다 큰가?
4. 조상 `overflow`가 스크롤 기준을 바꾸는가?
5. `overflow: hidden` 조상이 있는가?
6. sticky 요소가 부모 경계에 막히는가?
7. 표 요소에서 브라우저 지원 차이가 있는가?
8. `display` 구조가 예상과 다른가?
9. 중복 `top`의 최종값이 무엇인가?
10. 다른 요소에 가려진 것은 아닌가?

---

# 62. z-index가 작동하지 않을 때 점검

1. 요소가 stacking context에 참여하는가?
2. 부모가 별도 stacking context를 만드는가?
3. 부모의 `z-index`가 다른 그룹보다 낮은가?
4. `transform`, `opacity`, `filter`가 문맥을 만드는가?
5. 값이 같은 형제는 DOM 순서가 영향을 주는가?
6. 음수 `z-index`로 부모 배경 뒤에 들어갔는가?
7. `overflow`로 잘리고 있는가?
8. `position`과 Flex/Grid 항목 여부를 확인했는가?
9. 모달이 낮은 stacking context 내부에 있는가?
10. 개발자 도구 Layers 패널을 확인했는가?

---

# 63. 자주 하는 실수

## 63.1 기준 부모에 `position: relative` 누락

절대 위치 요소가 페이지 전체 기준으로 이동할 수 있습니다.

## 63.2 `absolute`가 body만 기준이라고 암기

정확히는 가까운 containing block을 찾고 없으면 초기 containing block을 사용합니다.

## 63.3 absolute를 주면 자식도 모두 absolute라고 생각

자식은 기본적으로 내부 정상 흐름을 유지할 수 있습니다.

## 63.4 relative 이동 후 형제가 다시 배치될 것으로 기대

원래 공간이 유지되므로 형제는 재배치되지 않습니다.

## 63.5 `top` 같은 속성을 여러 번 작성

뒤 선언만 적용됩니다.

## 63.6 sticky에 `top` 누락

임계 위치가 없으면 원하는 고정 효과가 나타나지 않습니다.

## 63.7 sticky 부모에 불필요한 `overflow: hidden`

스크롤 기준이 바뀌거나 동작하지 않는 것처럼 보일 수 있습니다.

## 63.8 무조건 큰 z-index 사용

부모 stacking context가 낮으면 큰 숫자도 소용없을 수 있습니다.

## 63.9 hover만으로 메뉴 구현

키보드와 터치 사용자가 조작하기 어렵습니다.

## 63.10 고정값 calc로 중앙 정렬

박스 크기가 바뀌면 중앙이 틀어질 수 있습니다.

---


# 종합실습

## 문제 1. 기본 위치

`position`을 지정하지 않은 일반 요소의 기본값을 작성하세요.

## 문제 2. 상대 위치

`.box`를 원래 위치에서 위로 `20px`, 오른쪽으로 `10px` 이동하세요. 원래 공간은 유지되어야 합니다.

## 문제 3. 절대 위치

`.badge`를 일반 흐름에서 제거하고 기준 부모의 오른쪽 위에 배치하세요.

## 문제 4. 기준 부모

문제 3의 `.badge`가 `.card`를 기준으로 배치되도록 `.card` CSS를 작성하세요.

## 문제 5. 중복 선언

다음 코드의 최종 `top` 값을 작성하세요.

```css
.box {
  position: absolute;
  top: 0;
  top: 30px;
}
```

## 문제 6. 기준 설명

절대 위치 요소에 적절한 positioned 조상이 없을 때 “무조건 body 기준”이라는 설명이 왜 부정확한지 작성하세요.

## 문제 7. 오른쪽 아래

절대 위치 자식을 부모의 오른쪽 아래에 붙이세요.

## 문제 8. 고정 버튼

화면 오른쪽 아래에서 각각 `16px` 떨어진 맨 위로 버튼을 고정하세요.

## 문제 9. 모바일 안전 영역

문제 8의 하단 위치에 `safe-area-inset-bottom`을 반영하세요.

## 문제 10. sticky 메뉴

메뉴가 스크롤 시 화면 위 `0` 위치에 붙도록 작성하세요. 다른 콘텐츠보다 위에 보이도록 배경색과 `z-index`도 포함하세요.

## 문제 11. sticky 조건

`position: sticky`가 작동하지 않을 때 확인할 조건을 세 가지 작성하세요.

## 문제 12. 레이어 순서

다음 세 요소의 일반적인 위에서 아래 순서를 작성하세요.

```css
.a { position: relative; z-index: 2; }
.b { position: relative; z-index: 300; }
.c { position: relative; z-index: 99; }
```

같은 stacking context의 겹치는 형제라는 전제입니다.

## 문제 13. stacking context

자식에게 `z-index: 9999`가 있지만 다른 부모 위로 나오지 못할 수 있는 이유를 설명하세요.

## 문제 14. hover 레이어

마우스와 키보드 포커스 시 `.layer-item`을 가장 위로 올리세요.

## 문제 15. 인접 형제

`.menu` 바로 다음의 `.submenu`를 `.menu` hover 시 표시하세요.

## 문제 16. 메뉴 접근성

문제 15의 hover 전용 방식이 가진 접근성 문제를 두 가지 작성하세요.

## 문제 17. 고정값 중앙 계산

부모 `400px`, 자식 `100px`일 때 자식의 중앙 위치를 `calc()`로 작성하세요.

## 문제 18. 유동 중앙 정렬

부모와 자식 크기를 몰라도 absolute 자식을 중앙 배치하는 코드를 작성하세요.

## 문제 19. 일반 중앙 정렬

겹침이 필요 없는 자식을 Grid로 가로·세로 중앙 정렬하세요.

## 문제 20. CSS 변수

`--color-accent`를 `#2563eb`로 전역 선언하고 `.badge` 배경에 사용하세요.

## 문제 21. 원본 오류 설명

다음 원본 주석을 정확하게 수정하세요.

```text
absolute는 주었을 때 inline-block으로 바뀜
```

## 문제 22. 종합 카드

다음 요구사항의 카드를 작성하세요.

- 카드가 배지의 위치 기준
- 카드 오른쪽 위에 `NEW` 배지
- 카드 이미지 아래쪽에 텍스트 오버레이
- 카드가 반응형 너비 사용
- 배지와 오버레이가 일반 콘텐츠 흐름을 밀지 않음
- 적절한 `z-index`
- CSS 변수로 강조색 관리
- 제목은 의미 있는 HTML 제목 사용

---

# 정답과 해설

## 정답 1

```css
position: static;
```

## 정답 2

```css
.box {
  position: relative;
  top: -20px;
  left: 10px;
}
```

`relative`이므로 원래 공간은 유지됩니다.

## 정답 3

```css
.badge {
  position: absolute;
  top: 0;
  right: 0;
}
```

## 정답 4

```css
.card {
  position: relative;
}
```

## 정답 5

```text
30px
```

같은 규칙 안에서 뒤의 동일 속성이 적용됩니다.

## 정답 6

적절한 positioned 조상이 없으면 항상 `body` 요소 자체를 기준으로 하는 것이 아니라 초기 containing block을 기준으로 위치를 계산하기 때문입니다.

## 정답 7

```css
.child {
  position: absolute;
  right: 0;
  bottom: 0;
}
```

부모에 `position: relative`가 필요합니다.

## 정답 8

```css
.back-to-top {
  position: fixed;
  right: 16px;
  bottom: 16px;
}
```

## 정답 9

```css
.back-to-top {
  position: fixed;
  right: 1rem;
  bottom:
    calc(1rem + env(safe-area-inset-bottom));
}
```

## 정답 10

```css
.sticky-menu {
  position: sticky;
  z-index: 10;
  top: 0;
  background-color: white;
}
```

## 정답 11

예:

```text
1. top 같은 임계 오프셋이 지정됐는가
2. 스크롤할 충분한 공간이 있는가
3. 조상의 overflow가 별도 스크롤 컨테이너를 만드는가
```

부모의 높이와 경계도 확인합니다.

## 정답 12

```text
위: .b (300)
중간: .c (99)
아래: .a (2)
```

## 정답 13

자식은 부모 stacking context 안에서만 레이어 순서를 경쟁합니다. 부모 stacking context 자체가 다른 부모보다 아래라면 자식의 큰 값이 외부 그룹을 넘어설 수 없습니다.

## 정답 14

```css
.layer-item:hover,
.layer-item:focus-visible {
  z-index: 999;
}
```

요소는 `z-index`가 의미를 가질 수 있는 레이아웃 상태여야 합니다.

## 정답 15

```css
.submenu {
  display: none;
}

.menu:hover + .submenu {
  display: block;
}
```

## 정답 16

예:

```text
1. 키보드 사용자에게 hover 상태가 제공되지 않을 수 있다.
2. 터치 화면에서 hover 동작이 불안정하거나 존재하지 않을 수 있다.
```

열림 상태도 보조 기술에 전달되지 않습니다.

## 정답 17

```css
.parent {
  position: relative;
  width: 400px;
  height: 400px;
}

.child {
  position: absolute;
  width: 100px;
  height: 100px;
  top: calc(400px / 2 - 100px / 2);
  left: calc(400px / 2 - 100px / 2);
}
```

계산 결과는 `150px`입니다.

## 정답 18

```css
.parent {
  position: relative;
}

.child {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
```

## 정답 19

```css
.parent {
  display: grid;
  min-height: 400px;
  place-items: center;
}
```

## 정답 20

```css
:root {
  --color-accent: #2563eb;
}

.badge {
  background-color:
    var(--color-accent);
}
```

## 정답 21

```text
absolute 요소는 일반 문서 흐름에서 빠지고,
위치 지정에 따라 표시 유형이 blockification되어
독립적인 위치 지정 박스처럼 동작한다.
```

## 정답 22

### HTML

```html
<article class="course-card">
  <img
    class="course-card__image"
    src="course.webp"
    alt="AI 서비스 개발 과정"
  >

  <span class="course-card__badge">
    NEW
  </span>

  <div class="course-card__overlay">
    <h2 class="course-card__title">
      AI 서비스 개발 과정
    </h2>
  </div>
</article>
```

### CSS

```css
:root {
  --color-accent: #2563eb;
}

.course-card {
  position: relative;
  width: min(100%, 28rem);
  overflow: hidden;
  border-radius: 1rem;
}

.course-card__image {
  display: block;
  width: 100%;
  aspect-ratio: 16 / 10;
  object-fit: cover;
}

.course-card__badge {
  position: absolute;
  z-index: 2;
  top: 1rem;
  right: 1rem;
  padding: 0.3rem 0.6rem;
  border-radius: 999px;
  color: white;
  background-color:
    var(--color-accent);
}

.course-card__overlay {
  position: absolute;
  z-index: 1;
  right: 0;
  bottom: 0;
  left: 0;
  padding: 2rem 1rem 1rem;
  color: white;
  background:
    linear-gradient(
      transparent,
      rgb(0 0 0 / 80%)
    );
}

.course-card__title {
  margin: 0;
}
```

---

# 최종 체크리스트

## 기본 위치

- [ ] 기본값 `static`의 의미를 이해했다.
- [ ] `relative`는 원래 공간을 유지함을 확인했다.
- [ ] `absolute`는 일반 흐름에서 빠짐을 확인했다.
- [ ] 같은 오프셋 속성이 중복 선언되지 않았는지 확인했다.
- [ ] 퍼센트 오프셋의 기준 박스를 확인했다.

## 기준 박스

- [ ] 절대 위치 자식의 기준 부모를 명확히 했다.
- [ ] 필요한 부모에 `position: relative`를 지정했다.
- [ ] “무조건 body 기준”으로 설명하지 않았다.
- [ ] 조상의 `transform`, `filter`, `contain` 영향을 검토했다.
- [ ] 부모 패딩과 테두리까지 고려했다.

## fixed와 sticky

- [ ] 고정 요소가 본문 콘텐츠를 가리지 않는다.
- [ ] 모바일 안전 영역을 검토했다.
- [ ] sticky에 `top` 등의 임계값이 있다.
- [ ] sticky 조상의 `overflow`를 확인했다.
- [ ] sticky에 불투명 배경과 필요한 `z-index`를 제공했다.
- [ ] `fixed`와 `sticky`의 흐름 차이를 구분했다.

## z-index

- [ ] 요소의 stacking context를 확인했다.
- [ ] 큰 숫자만 무작정 사용하지 않았다.
- [ ] 부모 stacking context의 순서를 확인했다.
- [ ] `transform`, `opacity`, `filter`의 문맥 생성을 확인했다.
- [ ] 레이어 숫자 체계를 프로젝트에서 일관되게 사용했다.

## 메뉴와 상호작용

- [ ] hover만으로 중요한 메뉴를 구현하지 않았다.
- [ ] 키보드 포커스와 터치 입력을 지원했다.
- [ ] 실제 버튼과 링크 요소를 사용했다.
- [ ] 열림 상태를 `aria-expanded`와 동기화했다.
- [ ] 서브메뉴 이동 중 작은 틈으로 닫히지 않는지 확인했다.

## 중앙 정렬과 변수

- [ ] 고정 크기 `calc()`가 유지보수 가능한지 확인했다.
- [ ] 유동 크기에는 `transform` 또는 Flex/Grid를 검토했다.
- [ ] `calc()`의 `+`, `-` 주변 공백을 작성했다.
- [ ] 강사님 코드의 세미콜론 누락을 보완했다.
- [ ] 공통 색상을 CSS 변수로 관리했다.
- [ ] 변수 이름을 역할 중심으로 작성했다.

## 원본 코드 검수

- [ ] `lang="en"`을 `lang="ko"`로 개선했다.
- [ ] `Document` 제목을 학습 주제로 변경했다.
- [ ] `absolute`, `fixed`가 단순히 `inline-block`이 된다는 설명을 보완했다.
- [ ] 모든 자식도 absolute여야 한다는 설명을 수정했다.
- [ ] `z-index`가 position에서만 가능하다는 설명을 보완했다.
- [ ] 내 코드 `top: 1px`과 강사님 `top: -1px` 차이를 보존했다.
- [ ] 테스트용 `200vw`의 가로 스크롤을 검토했다.
- [ ] 중복 `top` 선언의 최종 적용값을 설명했다.

---

# 핵심 요약

- `position`은 요소가 어떤 기준으로 배치되고 스크롤에 어떻게 반응할지 결정한다.
- 대부분 요소의 기본값은 `static`이다.
- `static` 요소에는 일반적으로 `top`, `left` 같은 오프셋이 적용되지 않는다.
- `relative`는 원래 공간을 유지한 채 원래 위치를 기준으로 시각적으로 이동한다.
- 상대 위치 요소가 이동해도 형제 요소는 원래 자리를 기준으로 배치된다.
- `absolute`는 일반 문서 흐름에서 빠지고 containing block을 기준으로 배치된다.
- 절대 위치의 가장 가까운 기준 부모에는 `position: relative`를 자주 사용한다.
- 적절한 기준 조상이 없으면 단순히 body가 아니라 초기 containing block을 기준으로 한다.
- `absolute`, `fixed`가 단순히 `inline-block`으로 변경된다고 설명하는 것은 부정확하다.
- 절대 위치 요소의 자식까지 모두 절대 위치로 만들 필요는 없다.
- 모든 레이아웃을 absolute로 만들면 반응형 대응과 유지보수가 어려워진다.
- `fixed`는 일반 흐름에서 빠지고 일반적으로 뷰포트에 고정된다.
- `sticky`는 원래 공간을 유지하다 임계 위치에 도달하면 스크롤 컨테이너 안에서 붙는다.
- sticky에는 `top` 같은 임계 오프셋과 충분한 스크롤 공간이 필요하다.
- 원본의 `top: 0` 뒤 `top: 30px`, `top: 50px`은 뒤 값이 최종 적용된다.
- `z-index`는 단순 숫자 비교만이 아니라 stacking context 안에서 계산된다.
- 자식의 큰 `z-index`도 낮은 부모 stacking context를 벗어나지 못할 수 있다.
- 원본의 `.z2` 300, `.z3` 99, `.z1` 2는 같은 문맥에서 그 순서대로 겹친다.
- 내 코드의 서브메뉴는 `top: 1px`, 강사님 코드는 `top: -1px`이다.
- hover와 인접 형제 선택자로 서브메뉴를 보일 수 있지만 키보드와 터치 접근성이 부족하다.
- 고정 크기 `calc()` 중앙 계산은 박스 크기가 바뀌면 다시 수정해야 한다.
- 유동 크기 absolute 중앙 정렬은 `top: 50%`, `left: 50%`, `transform` 조합을 사용할 수 있다.
- 겹침이 필요 없는 일반 중앙 정렬은 Flexbox나 Grid가 더 적절하다.
- `:root`의 CSS 사용자 지정 속성은 공통 값을 한 곳에서 관리하게 한다.
- 원본의 `body { width: 200vw; height: 200vh; }`는 스크롤 실습용이며 최종 프로젝트에서는 필요성을 검토해야 한다.
# V3 렌더링 추적 카드 — containing block과 좌표 계산

`relative`는 정상 위치를 기준으로 이동하며 원래 자리도 남는다. `absolute`는 보통 가장 가까운 positioned 조상을 기준으로 배치되고, 없으면 초기 containing block까지 올라간다. `fixed`는 주로 viewport 기준이다.

absolute 요소가 엉뚱한 위치에 있으면 부모의 `position:relative`, offset 속성, 실제 containing block을 확인한다. `z-index`는 쌓임 맥락 안에서 비교된다.

**원본 연결:** 내 코드와 강사님 코드의 `workspace_html/css/08_position.html 및 asset/css/08_position.css`에서 실제 선택자·계산값·화면 차이를 확인한다.
