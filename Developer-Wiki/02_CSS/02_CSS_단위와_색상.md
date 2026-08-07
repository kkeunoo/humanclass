---
title: CSS 단위와 색상
version: v2.0-final
last_updated: 2026-08-06
status: Completed
---

# CSS 단위와 색상

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `02_CSS_단위와_색상.md` |
| 분류 | `02_CSS` |
| 원본 기준 | `workspace_me/workspace_html/css/02_단위.html`, `workspace_teacher/workspace_html/css/02_단위.html` |
| 핵심 범위 | `px`, `%`, `em`, `rem`, `vw`, `vh`, `vmin`, `vmax`, 색상 이름, HEX, RGB, RGBA, 알파 채널, 상속 |
| 프로젝트 연결 | 글자 크기 체계, 반응형 레이아웃, 전체 화면 섹션, 디자인 토큰, 투명 배경 |
| 문서 형식 | CSS Developer-Wiki V2 확정 형식 |

> 이 문서는 내 코드와 강사님 코드의 단위·색상 실습을 함께 비교합니다. 원본의 실제 오류를 바로잡고, 같은 개념이 반응형 레이아웃과 디자인 시스템에서 어떻게 사용되는지 실무 예제로 연결합니다.

---

# 학습 목표

- CSS에서 길이 단위가 필요한 이유를 설명한다.
- 절대 단위와 상대 단위의 차이를 구분한다.
- `px`, `%`, `em`, `rem`의 기준값을 설명한다.
- 중첩된 `em`과 `%`가 누적되는 원리를 계산한다.
- `vw`, `vh`, `vmin`, `vmax`의 기준을 설명한다.
- 모바일 환경에서 `vh` 사용 시 발생할 수 있는 문제를 이해한다.
- 색상 이름, HEX, RGB, RGBA 표기법을 작성한다.
- 3자리·4자리·6자리·8자리 HEX의 차이를 구분한다.
- 알파 채널과 요소 전체 투명도의 차이를 설명한다.
- `font-size`의 상속과 `background-color`의 비상속을 구분한다.
- 내 코드와 강사님 코드의 차이와 오류를 찾는다.
- 반응형이고 접근 가능한 단위 선택 기준을 세운다.
- CSS 사용자 지정 속성으로 색상과 크기 값을 관리한다.

---

# 1. CSS 단위란?

CSS 속성에는 숫자만 사용하는 값과 단위를 함께 사용하는 값이 있습니다.

```css
.box {
  width: 320px;
  font-size: 1rem;
  margin-top: 5vh;
}
```

각 값은 서로 다른 기준으로 계산됩니다.

| 값 | 의미 |
| --- | --- |
| `320px` | CSS 픽셀 320개 |
| `1rem` | 루트 요소 글자 크기의 1배 |
| `5vh` | 뷰포트 높이의 5% |

단위 선택은 단순한 문법 문제가 아닙니다.

다음에 영향을 줍니다.

- 글자 확대
- 화면 크기 변화
- 반응형 디자인
- 컴포넌트 재사용
- 접근성
- 유지보수
- 레이아웃 안정성

---

# 2. 값이 `0`일 때

길이값이 `0`이면 대부분 단위를 생략할 수 있습니다.

```css
body {
  margin: 0;
}
```

다음도 동작하지만 단위가 불필요합니다.

```css
body {
  margin: 0px;
}
```

예외적으로 단위가 의미를 가지는 문맥이 있으므로 모든 CSS 숫자에서 무조건 제거하는 규칙은 아닙니다. 일반적인 길이 속성의 `0`은 단위 없이 작성합니다.

---

# 3. 절대 단위와 상대 단위

## 3.1 절대 단위

특정 기준에 고정된 단위입니다.

대표적으로 수업에서 다룬 `px`가 있습니다.

```css
.title {
  font-size: 32px;
}
```

CSS에는 `cm`, `mm`, `in`, `pt`, `pc`도 있지만 화면 UI에서는 주로 `px`를 사용합니다.

## 3.2 상대 단위

다른 값이나 화면 크기를 기준으로 계산됩니다.

```css
.title {
  font-size: 1.5rem;
}
```

```css
.hero {
  min-height: 100vh;
}
```

대표적인 상대 단위:

- `%`
- `em`
- `rem`
- `vw`
- `vh`
- `vmin`
- `vmax`

## 3.3 선택 기준

| 상황 | 자주 쓰는 단위 |
| --- | --- |
| 얇은 테두리 | `px` |
| 글자 크기 | `rem` |
| 컴포넌트 내부 글자 상대 크기 | `em` |
| 부모 너비 기준 크기 | `%` |
| 화면 기준 크기 | `vw`, `vh` |
| 최대·최소 범위 조절 | `clamp()`, `min()`, `max()` |

절대 단위가 나쁘고 상대 단위가 항상 좋은 것은 아닙니다. 속성의 목적에 맞게 선택합니다.

---

# 4. `px`

`px`는 CSS 픽셀 단위입니다.

```css
#pixel .box1 {
  font-size: 16px;
}
```

원본 내 코드 주석은 `px`를 “디스플레이에 절대적인 크기”라고 설명합니다.

입문 단계에서는 고정된 값으로 이해할 수 있지만, CSS의 `1px`가 물리 디스플레이의 하드웨어 픽셀 하나와 항상 정확히 같다는 뜻은 아닙니다.

고해상도 화면에서는 하나의 CSS 픽셀이 여러 물리 픽셀로 표현될 수 있습니다.

## 4.1 `px`가 적합한 경우

```css
.card {
  border: 1px solid #ddd;
}
```

```css
.icon {
  width: 24px;
  height: 24px;
}
```

- 얇은 테두리
- 작은 아이콘
- 정밀한 그림자 이동값
- 디자인에서 고정 기준이 필요한 세부 표현

## 4.2 글자 크기에서의 주의

```css
body {
  font-size: 16px;
}
```

브라우저는 일반적으로 기본 글자 크기로 `16px`을 사용하지만, 사용자의 브라우저 설정과 환경에 따라 다를 수 있습니다.

다음처럼 고정된 픽셀만 사용하면 사용자 글자 크기 설정을 충분히 반영하지 못하는 환경이 있을 수 있습니다.

```css
.title {
  font-size: 32px;
}
```

실무에서는 글자 크기에 `rem`을 많이 사용합니다.

```css
.title {
  font-size: 2rem;
}
```

---

# 5. 원본의 픽셀 실습

원본 코드:

```css
#pixel .box1 {
  font-size: 16px;
  background-color: rgb(255, 0, 0);
  color: #0f0;
}

#pixel .box1 .box2 {
  font-size: 32px;
  background-color: rgba(0, 0, 255, 0.4);
}

#pixel .box1 .box2 .box3 {
  font-size: 16px;
  background-color: #00ff00a0;
}
```

각 요소에 명시적인 글자 크기를 지정했습니다.

| 요소 | 계산된 `font-size` |
| --- | --- |
| `.box1` | `16px` |
| `.box2` | `32px` |
| `.box3` | `16px` |

부모의 글자 크기와 관계없이 각 요소에 직접 지정된 픽셀값을 사용합니다.

---

# 6. `%`

퍼센트는 속성마다 기준이 다릅니다.

원본에서는 `font-size`에 사용했습니다.

```css
#percent .box1 {
  font-size: 150%;
}
```

`font-size: 150%`는 부모 요소의 계산된 글자 크기를 기준으로 합니다.

부모가 `16px`이라면:

```text
16px × 1.5 = 24px
```

---

# 7. 중첩된 `%` 계산

원본:

```css
#percent .box1 {
  font-size: 150%;
}

#percent .box1 .box2 {
  font-size: 150%;
}

#percent .box1 .box2 .box3 {
  font-size: 150%;
}
```

브라우저 기본 글자 크기를 `16px`이라고 가정합니다.

| 요소 | 계산 | 결과 |
| --- | --- | --- |
| `.box1` | `16 × 1.5` | `24px` |
| `.box2` | `24 × 1.5` | `36px` |
| `.box3` | `36 × 1.5` | `54px` |

각 요소가 루트의 `150%`를 사용하는 것이 아니라 **직접 부모의 계산값**을 기준으로 다시 계산합니다.

이것이 중첩에 따른 누적 현상입니다.

---

# 8. `%`의 기준은 속성마다 다르다

`font-size`의 퍼센트 기준은 부모의 글자 크기입니다.

하지만 다른 속성에서는 기준이 달라집니다.

```css
.box {
  width: 50%;
}
```

보통 containing block의 너비를 기준으로 합니다.

```css
.child {
  padding-left: 10%;
}
```

퍼센트 패딩은 일반적으로 containing block의 **인라인 크기**, 보통 가로쓰기에서는 너비를 기준으로 계산됩니다.

따라서 `%`를 단순히 “부모 크기의 퍼센트”라고만 외우면 부족합니다.

항상 해당 속성의 계산 기준을 확인해야 합니다.

---

# 9. `em`

`em`은 현재 요소의 글자 크기를 기준으로 하는 상대 단위입니다.

`font-size` 속성에서 `em`을 사용할 때는 부모의 계산된 글자 크기를 기준으로 계산합니다.

```css
#em .box1 {
  font-size: 1.5em;
}
```

부모가 `16px`이라면 `.box1`은 `24px`입니다.

---

# 10. 중첩된 `em`

내 코드:

```css
#em .box1 {
  font-size: 1.5em;
}

#em .box1 .box2 {
  font-size: 1.5em;
}

#em .box1 .box2 .box3 {
  font-size: 1.5em;
}
```

기본값을 `16px`이라고 가정하면:

| 요소 | 계산 | 결과 |
| --- | --- | --- |
| `.box1` | `16 × 1.5` | `24px` |
| `.box2` | `24 × 1.5` | `36px` |
| `.box3` | `36 × 1.5` | `54px` |

`font-size`에서 `%`와 `em`은 비슷한 누적 결과를 만듭니다.

```text
150% = 1.5em
```

단, 다른 속성에서 `em`은 그 요소의 계산된 글자 크기를 기준으로 사용됩니다.

---

# 11. `em`의 실무 활용

컴포넌트 내부 간격이나 아이콘 크기를 글자에 비례시키고 싶을 때 유용합니다.

```css
.button {
  font-size: 1rem;
  padding: 0.75em 1.25em;
}
```

버튼의 글자 크기가 커지면 패딩도 함께 커집니다.

```css
.button--large {
  font-size: 1.25rem;
}
```

`padding`은 그대로 두어도 `em` 기준이 커져 버튼 전체 크기가 자연스럽게 증가합니다.

아이콘에도 활용할 수 있습니다.

```css
.icon {
  width: 1em;
  height: 1em;
}
```

현재 텍스트 크기와 맞춰집니다.

---

# 12. `em`의 누적 문제

컴포넌트가 중첩될 때 예상보다 빠르게 커질 수 있습니다.

```css
.menu {
  font-size: 1.2em;
}

.menu .menu {
  font-size: 1.2em;
}
```

중첩 메뉴에서는 다시 1.2배가 적용됩니다.

이런 경우 루트 기준인 `rem`이 더 예측 가능할 수 있습니다.

```css
.menu {
  font-size: 1.2rem;
}
```

---

# 13. `rem`

`rem`은 **root em**의 약자입니다.

루트 요소인 `html`의 계산된 `font-size`를 기준으로 합니다.

```css
html {
  font-size: 16px;
}

.title {
  font-size: 2rem;
}
```

계산:

```text
16px × 2 = 32px
```

부모가 몇 번 중첩되어도 기준은 루트입니다.

---

# 14. 원본 설명 보완

내 코드 주석:

```text
root em의 약자로 루트 html 요소의 글자 크기를 기준으로 한다
```

강사님 코드 주석:

```text
rem : root em, 루트 html 요소의 글자 크기를 기준으로 한다
```

정확한 기준은 `body`가 아니라 **루트 요소 `html`의 글자 크기**입니다.

```css
html {
  font-size: 16px;
}
```

```css
body {
  font-size: 20px;
}
```

```css
.title {
  font-size: 2rem;
}
```

`.title`은 `body`의 `20px`이 아니라 `html`의 `16px`을 기준으로 `32px`이 됩니다.

---

# 15. 중첩된 `rem`

내 코드:

```css
#rem .box1 {
  font-size: 1.5rem;
}

#rem .box1 .box2 {
  font-size: 1.5rem;
}

#rem .box1 .box2 .box3 {
  font-size: 1.5rem;
}
```

루트가 `16px`이라면 세 요소가 모두 같습니다.

| 요소 | 계산 | 결과 |
| --- | --- | --- |
| `.box1` | `16 × 1.5` | `24px` |
| `.box2` | `16 × 1.5` | `24px` |
| `.box3` | `16 × 1.5` | `24px` |

`em`처럼 부모 크기가 연속으로 곱해지지 않습니다.

---

# 16. `em`과 `rem` 비교

| 구분 | `em` | `rem` |
| --- | --- | --- |
| 기준 | 현재 요소 또는 부모 글자 크기 | 루트 `html` 글자 크기 |
| 중첩 영향 | 누적될 수 있음 | 중첩과 무관 |
| 장점 | 컴포넌트 비례 조절 | 전체 크기 체계가 예측 가능 |
| 대표 용도 | 버튼 패딩, 아이콘, 내부 간격 | 본문·제목 크기, 페이지 간격 |
| 주의 | 중첩 시 급격히 커질 수 있음 | 루트 크기 정책에 영향받음 |

실무에서 자주 사용하는 조합:

```css
body {
  font-size: 1rem;
}

.card-title {
  font-size: 1.5rem;
}

.button {
  padding: 0.75em 1.25em;
}
```

글자 체계는 `rem`, 컴포넌트 내부 비례는 `em`을 사용합니다.

---

# 17. 루트 글자 크기를 `62.5%`로 설정하는 방식

일부 프로젝트에서는 다음 패턴을 사용합니다.

```css
html {
  font-size: 62.5%;
}
```

브라우저 기본값을 `16px`로 가정하면:

```text
16px × 0.625 = 10px
```

따라서:

```css
.title {
  font-size: 2.4rem;
}
```

계산상 `24px`이 됩니다.

## 17.1 장점

- `rem` 값을 픽셀처럼 계산하기 쉽다.

## 17.2 주의

- 기본 글자 크기를 `10px`에 가깝게 변경한다.
- 팀원이 기준을 알아야 한다.
- 사용자 설정과 프로젝트 정책을 고려해야 한다.
- `1rem = 16px`이라는 일반적인 기대와 달라진다.

필수 방식이 아닙니다.

단순하고 명확하게 다음처럼 유지하는 프로젝트도 많습니다.

```css
html {
  font-size: 100%;
}
```

---

# 18. 사용자 글자 크기 설정 존중

다음처럼 루트에 고정 픽셀을 지정하면 사용자의 브라우저 기본 글자 설정을 덜 유연하게 반영할 수 있습니다.

```css
html {
  font-size: 16px;
}
```

다음은 브라우저 설정을 기준으로 유지합니다.

```css
html {
  font-size: 100%;
}
```

```css
body {
  font-size: 1rem;
}
```

실무에서는 프로젝트 요구, 접근성 기준, 기존 디자인 시스템을 함께 고려합니다.

---

# 19. 뷰포트란?

뷰포트는 브라우저에서 웹페이지가 보이는 영역입니다.

```html
<meta
  name="viewport"
  content="width=device-width, initial-scale=1.0"
>
```

모바일에서 뷰포트 기반 단위를 의도대로 사용하려면 위 메타 태그가 중요합니다.

뷰포트 단위는 화면 영역을 100등분한 값을 사용합니다.

---

# 20. `vw`

`vw`는 viewport width의 약자입니다.

```text
1vw = 뷰포트 너비의 1%
```

원본:

```css
#v2 {
  height: 20px;
  width: 50vw;
}
```

뷰포트 너비가 `1200px`이라면:

```text
1200 × 0.5 = 600px
```

`50vw`는 `600px`입니다.

## 20.1 활용 예

```css
.hero-title {
  font-size: 5vw;
}
```

화면이 커질수록 글자도 계속 커질 수 있으므로 최대·최소 범위를 함께 설정하는 것이 좋습니다.

```css
.hero-title {
  font-size: clamp(2rem, 5vw, 4rem);
}
```

---

# 21. `vh`

`vh`는 viewport height의 약자입니다.

```text
1vh = 뷰포트 높이의 1%
```

원본:

```css
#v1 {
  height: 100vh;
}
```

뷰포트 높이가 `800px`이라면:

```text
800 × 1 = 800px
```

`100vh`는 화면 높이 전체에 해당합니다.

## 21.1 활용 예

```css
.hero {
  min-height: 100vh;
}
```

`height`보다 `min-height`가 콘텐츠 증가에 더 안전한 경우가 많습니다.

```css
.hero {
  min-height: 100vh;
}
```

콘텐츠가 화면보다 길어지면 영역도 늘어날 수 있습니다.

---

# 22. 모바일에서 `100vh` 주의

모바일 브라우저는 주소창과 하단 UI가 나타나거나 사라지면서 실제 보이는 영역이 변할 수 있습니다.

전통적인 `100vh`는 브라우저 UI를 포함한 기준 때문에 콘텐츠가 화면 아래로 밀리거나 잘리는 문제가 생길 수 있습니다.

최신 뷰포트 단위:

| 단위 | 의미 |
| --- | --- |
| `svh` | 작은 뷰포트 높이 |
| `lvh` | 큰 뷰포트 높이 |
| `dvh` | 동적으로 변하는 뷰포트 높이 |

실무 예:

```css
.hero {
  min-height: 100vh;
  min-height: 100dvh;
}
```

지원하지 않는 환경을 위해 `vh`를 먼저 작성하고 `dvh`를 뒤에 작성할 수 있습니다.

---

# 23. `vmin`

`vmin`은 뷰포트의 너비와 높이 중 **더 작은 값**의 1%입니다.

```css
#v3 {
  height: 90vmin;
}
```

뷰포트가 다음과 같다고 가정합니다.

```text
너비: 1200px
높이: 800px
```

더 작은 값은 `800px`입니다.

```text
90vmin = 800 × 0.9 = 720px
```

세로 화면:

```text
너비: 390px
높이: 844px
```

더 작은 값은 `390px`입니다.

```text
90vmin = 351px
```

정사각형, 원형, 화면 안에 들어가야 하는 시각 요소에 유용합니다.

```css
.avatar {
  width: 20vmin;
  height: 20vmin;
  border-radius: 50%;
}
```

---

# 24. `vmax`

`vmax`는 뷰포트의 너비와 높이 중 **더 큰 값**의 1%입니다.

```css
#v4 {
  height: 90vmax;
}
```

뷰포트가 `1200px × 800px`이라면 큰 값은 `1200px`입니다.

```text
90vmax = 1080px
```

화면 높이보다 커질 수 있으므로 스크롤이 생길 수 있습니다.

원본 주석은 `vmin`, `vmax`가 주로 사용되지 않는다고 설명합니다. 실제로 `vw`, `vh`, `rem`보다 사용 빈도가 낮은 편이지만, 화면 방향에 따라 정사각형 크기나 장식 요소를 조절할 때 유용합니다.

---

# 25. 뷰포트 단위 비교

| 단위 | 기준 | 예 |
| --- | --- | --- |
| `vw` | 뷰포트 너비 | `50vw` |
| `vh` | 뷰포트 높이 | `100vh` |
| `vmin` | 너비·높이 중 작은 값 | `90vmin` |
| `vmax` | 너비·높이 중 큰 값 | `90vmax` |
| `dvh` | 동적 뷰포트 높이 | `100dvh` |

---

# 26. `width: 100%`와 `width: 100vw`

두 값은 비슷해 보이지만 다를 수 있습니다.

```css
.box {
  width: 100%;
}
```

부모의 콘텐츠 영역을 기준으로 합니다.

```css
.box {
  width: 100vw;
}
```

뷰포트 전체 너비를 기준으로 합니다.

세로 스크롤바가 있는 환경에서 `100vw`가 스크롤바 너비까지 포함하여 가로 스크롤을 만들 수 있습니다.

페이지 전체 너비 요소에는 대부분 다음이 더 안전합니다.

```css
.box {
  width: 100%;
}
```

화면 가장자리를 기준으로 의도적으로 계산해야 할 때 `vw`를 사용합니다.

---

# 27. `height: 100%`와 `height: 100vh`

```css
.child {
  height: 100%;
}
```

퍼센트 높이는 부모의 명시적인 높이 계산 조건에 영향을 받습니다.

부모 높이가 `auto`이면 기대한 전체 화면 높이가 나오지 않을 수 있습니다.

```css
.hero {
  min-height: 100vh;
}
```

`vh`는 뷰포트 높이를 직접 기준으로 하므로 부모 높이에 의존하지 않습니다.

---

# 28. 확장 단위 `ch`

`ch`는 현재 글꼴의 숫자 `0` 글리프 너비를 기준으로 합니다.

긴 본문의 가독성 폭을 제한할 때 유용합니다.

```css
.article {
  max-width: 65ch;
}
```

한 줄이 지나치게 길어지는 것을 막을 수 있습니다.

`65ch`가 정확히 65글자라는 뜻은 아닙니다. 글자마다 너비가 다르기 때문입니다.

---

# 29. 확장 단위 `lh`

`lh`는 현재 요소의 계산된 줄 높이 한 줄을 기준으로 합니다.

```css
.notice {
  margin-top: 1lh;
}
```

본문 줄 높이에 비례한 간격을 만들 수 있습니다.

루트 줄 높이를 기준으로 하는 `rlh`도 있습니다.

---

# 30. 확장 단위와 사용 기준

| 단위 | 기준 | 대표 용도 |
| --- | --- | --- |
| `ch` | 문자 `0`의 너비 | 본문 최대 너비 |
| `lh` | 현재 줄 높이 | 텍스트 흐름 간격 |
| `dvh` | 동적 뷰포트 높이 | 모바일 전체 화면 |
| `svh` | 작은 뷰포트 높이 | 브라우저 UI가 보이는 안전 높이 |
| `lvh` | 큰 뷰포트 높이 | UI가 숨겨진 최대 높이 |

원본에 없는 확장 학습이므로 프로젝트의 브라우저 지원 범위를 확인해 적용합니다.

---

# 31. `calc()`

서로 다른 단위를 계산할 수 있습니다.

```css
.main {
  min-height: calc(100vh - 80px);
}
```

화면 전체 높이에서 고정 헤더 높이를 뺍니다.

연산자 주변에는 공백을 작성하는 것이 안전합니다.

```text
/* 권장 */
width: calc(100% - 32px);
```

```text
/* 피하기 */
width: calc(100%-32px);
```

실무 예:

```css
.container {
  width: min(100% - 2rem, 1200px);
  margin-inline: auto;
}
```

---

# 32. `min()`, `max()`, `clamp()`

## 32.1 `min()`

여러 값 중 더 작은 값을 사용합니다.

```css
.container {
  width: min(100% - 2rem, 1200px);
}
```

화면에서는 좌우 여백을 남기고, 최대 폭은 `1200px`을 넘지 않습니다.

## 32.2 `max()`

여러 값 중 더 큰 값을 사용합니다.

```css
.section {
  padding-inline: max(1rem, 4vw);
}
```

최소 `1rem` 이상을 유지합니다.

## 32.3 `clamp()`

최솟값, 선호값, 최댓값을 지정합니다.

```css
.hero-title {
  font-size: clamp(2rem, 5vw, 4rem);
}
```

구조:

```text
clamp(최솟값, 선호값, 최댓값)
```

화면에 따라 부드럽게 커지지만 `2rem`보다 작거나 `4rem`보다 커지지 않습니다.

---

# 33. 색상 표현 방법

원본에는 다음 색상 표기법이 등장합니다.

- `rgb()`
- `rgba()`
- 6자리 HEX
- 3자리 HEX
- 8자리 HEX

CSS에서는 다음 방식도 사용할 수 있습니다.

- 색상 키워드
- HSL
- 최신 공백 구문 RGB
- CSS 사용자 지정 속성

이 문서에서는 원본 중심으로 HEX와 RGB를 우선 정리합니다.

---

# 34. 색상 키워드

미리 정의된 이름을 사용할 수 있습니다.

```css
.title {
  color: red;
}
```

```css
.box {
  background-color: transparent;
}
```

대표적인 키워드:

- `red`
- `blue`
- `green`
- `black`
- `white`
- `gray`
- `transparent`
- `currentColor`

간단한 실습에는 편리하지만 디자인 시스템에서는 정확한 색상값을 지정하는 경우가 많습니다.

---

# 35. RGB

RGB는 빨강, 초록, 파랑의 조합입니다.

```text
background-color: rgb(255, 0, 0);
```

각 채널의 전통적인 범위:

```text
0 ~ 255
```

예:

| 색상 | 값 |
| --- | --- |
| 빨강 | `rgb(255, 0, 0)` |
| 초록 | `rgb(0, 255, 0)` |
| 파랑 | `rgb(0, 0, 255)` |
| 검정 | `rgb(0, 0, 0)` |
| 흰색 | `rgb(255, 255, 255)` |

원본:

```text
background-color: rgb(255, 0, 0);
```

빨강 채널이 최대이고 나머지는 0이므로 빨간색입니다.

---

# 36. RGBA

RGBA는 RGB에 알파 채널을 추가한 표현입니다.

```text
background-color: rgba(0, 0, 255, 0.4);
```

알파값:

```text
0   = 완전히 투명
1   = 완전히 불투명
0.4 = 40% 불투명
```

원본의 `.box2`는 반투명한 파란 배경입니다.

아래의 부모 배경색이 비쳐 보입니다.

```css
#pixel .box1 {
  background-color: rgb(255, 0, 0);
}

#pixel .box1 .box2 {
  background-color: rgba(0, 0, 255, 0.4);
}
```

화면에서 보이는 최종 색상은 파랑과 부모의 빨강이 합성된 결과입니다.

---

# 37. 최신 RGB 알파 표기

다음처럼 `rgb()` 안에서 슬래시로 알파값을 작성할 수도 있습니다.

```text
background-color: rgb(0 0 255 / 40%);
```

기존 `rgba()`도 계속 사용할 수 있습니다.

프로젝트에서는 하나의 스타일을 일관되게 사용합니다.

---

# 38. HEX 6자리

HEX 색상은 16진수로 RGB 채널을 표현합니다.

```text
color: #00ffaa;
```

구조:

```text
# RR GG BB
```

```text
00 = 빨강
ff = 초록
aa = 파랑
```

각 채널 범위:

```text
00 ~ ff
```

16진수에서는 다음 문자를 사용합니다.

```text
0 1 2 3 4 5 6 7 8 9 a b c d e f
```

대소문자는 결과에 영향을 주지 않습니다.

```text
#00ffaa
#00FFAA
```

프로젝트에서는 하나의 표기 스타일을 유지합니다.

---

# 39. HEX 3자리 축약

원본:

```text
color: #0fa;
```

3자리 HEX는 각 문자를 두 번 반복한 6자리 값입니다.

```text
#0fa
= #00ffaa
```

다른 예:

```text
#fff = #ffffff
#000 = #000000
#f00 = #ff0000
```

모든 6자리 색상을 3자리로 줄일 수 있는 것은 아닙니다.

```text
#12abef
```

각 채널의 두 문자가 같지 않으므로 3자리 축약이 불가능합니다.

---

# 40. 원본의 반복 색상 선언

강사님 코드:

```text
color: #00ffaa;
color: #0fa;
```

같은 규칙 안에서 같은 속성을 두 번 작성했습니다.

두 값은 같은 색상입니다.

뒤의 선언이 최종 적용됩니다.

학습 목적은 6자리 HEX를 3자리로 줄이는 방법을 보여 주는 것입니다.

실무 최종 코드에서는 하나만 남깁니다.

```text
color: #0fa;
```

또는 가독성을 위해:

```text
color: #00ffaa;
```

---

# 41. HEX 8자리

원본:

```text
background-color: #00ff00a0;
```

구조:

```text
# RR GG BB AA
```

마지막 두 자리는 알파 채널입니다.

```text
00 = 완전히 투명
ff = 완전히 불투명
```

`a0`은 16진수 알파값입니다.

10진수로 변환하면:

```text
a0 = 160
```

비율:

```text
160 / 255 ≈ 0.627
```

약 62.7% 불투명입니다.

원본 내 코드의 주석은 “6자리 뒤에 2자리로 표현할 수 있음”이라고 적었습니다. 더 정확히는 6자리 RGB 뒤에 2자리 알파 채널을 추가하여 8자리 HEX로 표현합니다.

---

# 42. HEX 4자리

3자리 HEX에 알파 한 자리를 추가할 수 있습니다.

```text
background-color: #0f08;
```

확장:

```text
#0f08
= #00ff0088
```

구조:

```text
#RGBA
```

각 문자가 두 번 반복됩니다.

---

# 43. RGB와 HEX 비교

| 표현 | 예 | 장점 |
| --- | --- | --- |
| 색상 이름 | `red` | 읽기 쉬움 |
| 6자리 HEX | `#ff0000` | 디자인 도구와 많이 사용 |
| 3자리 HEX | `#f00` | 짧음 |
| RGB | `rgb(255, 0, 0)` | 채널 의미가 명확 |
| RGBA | `rgba(255, 0, 0, 0.5)` | 투명도 직관적 |
| 8자리 HEX | `#ff000080` | 색상과 알파를 한 값으로 표현 |

팀 규칙과 디자인 토큰에 맞춰 일관되게 사용합니다.

---

# 44. 알파 채널과 `opacity`의 차이

알파 채널:

```css
.card {
  background-color: rgba(0, 0, 255, 0.4);
}
```

배경색만 반투명해집니다.

`opacity`:

```css
.card {
  opacity: 0.4;
}
```

요소 전체와 자식 콘텐츠까지 함께 투명해집니다.

```html
<div class="card">
  <p>이 글자도 함께 투명해짐</p>
</div>
```

배경만 투명하게 만들고 글자는 선명하게 유지하려면 알파 색상을 사용합니다.

---

# 45. `transparent`

```css
.box {
  background-color: transparent;
}
```

투명한 색상입니다.

자식 요소의 배경 기본값은 일반적으로 투명하므로 부모 배경이 뒤에서 보입니다.

```css
.parent {
  background-color: red;
}

.child {
  background-color: transparent;
}
```

자식이 빨간색을 상속받은 것이 아닙니다.

---

# 46. `currentColor`

현재 요소의 `color` 값을 다른 색상 속성에 재사용합니다.

```css
.button {
  color: navy;
  border: 1px solid currentColor;
}
```

테두리 색상이 글자색과 같아집니다.

```css
.icon {
  fill: currentColor;
}
```

SVG 아이콘 색상을 텍스트 색상과 맞출 때 유용합니다.

---

# 47. HSL 확장 학습

HSL은 색상, 채도, 명도를 기준으로 표현합니다.

```text
color: hsl(220 80% 50%);
```

| 구성 | 의미 |
| --- | --- |
| `220` | 색상 각도 |
| `80%` | 채도 |
| `50%` | 명도 |

알파값:

```text
background-color: hsl(220 80% 50% / 40%);
```

원본에는 등장하지 않지만 같은 색의 밝기 변형을 만들 때 이해하기 쉬운 경우가 있습니다.

---

# 48. `color` 속성의 상속

원본 `.box1`:

```css
#pixel .box1 {
  color: #0f0;
}
```

`color`는 상속되는 속성입니다.

자식 요소가 별도의 `color`를 지정하지 않으면 부모의 녹색 글자색을 사용할 수 있습니다.

```html
<div class="box1">
  box1
  <div class="box2">
    box2
  </div>
</div>
```

`.box2`와 `.box3`의 텍스트도 녹색으로 보이는 이유입니다.

---

# 49. `font-size`의 상속

`font-size`도 상속되는 속성입니다.

```css
.parent {
  font-size: 20px;
}
```

```html
<div class="parent">
  <p>별도 크기가 없으면 상속</p>
</div>
```

자식이 직접 지정하면 상속값 대신 직접 지정된 값을 사용합니다.

```css
.parent p {
  font-size: 16px;
}
```

상대 단위인 `%`와 `em`은 부모의 계산값을 기준으로 새로운 값을 계산한 뒤 그 계산값이 다시 자식에게 상속됩니다.

---

# 50. `background-color`는 상속되지 않는다

원본 내 코드 주석:

```text
background 컬러는 상속은 안되지만,
나머지가 투명하기에 모두 붉게 보이는 것
```

이 설명은 핵심을 잘 짚고 있습니다.

```css
.parent {
  background-color: red;
}
```

자식은 기본적으로 투명한 배경을 가지므로 부모의 빨간색이 뒤에서 보입니다.

```css
.child {
  background-color: white;
}
```

자식에게 흰색을 지정하면 부모 배경이 가려집니다.

---

# 51. 상속 관련 키워드

## 51.1 `inherit`

부모의 계산값을 명시적으로 상속합니다.

```css
button {
  color: inherit;
}
```

## 51.2 `initial`

해당 속성의 CSS 초기값을 사용합니다.

```css
.title {
  color: initial;
}
```

## 51.3 `unset`

상속되는 속성이면 `inherit`, 상속되지 않는 속성이면 `initial`처럼 동작합니다.

```css
.component {
  color: unset;
}
```

## 51.4 `revert`

현재 작성자 스타일을 되돌려 사용자 또는 브라우저 기본 스타일 등 이전 캐스케이드 출처의 값을 사용할 수 있습니다.

```css
button {
  all: revert;
}
```

`all`은 강력하므로 필요한 상황에서 신중하게 사용합니다.

---

# 52. 내 코드 분석

내 코드는 강사님 코드에 단위의 의미와 결과를 상세히 주석으로 추가했습니다.

## 52.1 장점

- `px`와 디스플레이의 관계를 기록했다.
- `background-color`가 상속되지 않는 점을 설명했다.
- HEX 축약을 직접 기록했다.
- RGBA와 8자리 HEX 알파값을 실습했다.
- `%`와 `em`의 누적 특성을 설명했다.
- `rem` 전용 실습 구역을 별도로 추가했다.
- `vh`, `vw`, `vmin`, `vmax`를 화면 변화와 연결해 설명했다.
- 각 단위 구역마다 기본 글씨 비교 문장을 추가했다.
- 강사님 코드보다 중첩 구조와 닫는 태그를 더 정리했다.

복습 자료로서 단위가 무엇을 기준으로 계산되는지 추적하려는 시도가 좋습니다.

---

# 53. 내 코드 개선점

## 53.1 문서 언어

```html
<html lang="en">
```

본문이 한국어이므로 다음이 적절합니다.

```html
<html lang="ko">
```

## 53.2 `px` 설명

`px`는 CSS에서 고정 길이처럼 사용되지만 물리 화면 픽셀 하나와 항상 같은 것은 아닙니다.

“디스플레이에 절대적인 크기”보다 “CSS 픽셀 기준의 절대 길이 단위”라고 설명하는 편이 정확합니다.

## 53.3 기본값 `16px`

브라우저 기본 글자 크기는 일반적으로 `16px`이지만 사용자 설정으로 달라질 수 있습니다.

따라서 계산 예제에서는 다음처럼 전제를 명시합니다.

```text
루트 글자 크기를 16px이라고 가정하면
```

## 53.4 `rem`의 기준

```text
루트 html 요소의 글자 크기를 기준으로 한다
```

가 아니라:

```text
html 요소의 계산된 font-size를 기준으로 한다
```

## 53.5 HTML 중첩 들여쓰기

`em`과 `rem` 영역의 `.box3` 닫는 구조는 브라우저가 해석할 수 있지만 들여쓰기상 닫는 `div`가 부족해 보입니다.

명확하게 정리하면 다음과 같습니다.

```html
<div id="em">
  <div class="box1">
    box1
    <div class="box2">
      box2
      <div class="box3">
        box3
      </div>
    </div>
  </div>
</div>
```

## 53.6 `vmin`, `vmax` 설명

```text
높이의 경우 내가 가진 콘텐츠의 100%로 따지기 때문에
vh를 사용하는 것이 좋음
```

이 문장은 기준이 혼합되어 있습니다.

`vh`, `vmin`, `vmax`는 콘텐츠 크기가 아니라 모두 뷰포트를 기준으로 합니다.

- `vh`: 뷰포트 높이
- `vmin`: 뷰포트 너비·높이 중 작은 값
- `vmax`: 뷰포트 너비·높이 중 큰 값

## 53.7 색상 축약 설명

```text
2개씩 코드가 반복될 때 한 글자로 줄일 수 있음
```

더 정확히는 각 RGB 채널의 두 16진수 문자가 동일할 때 3자리 HEX로 축약할 수 있습니다.

```text
#00ffaa → #0fa
```

---

# 54. 강사님 코드 분석

강사님 코드는 다음 순서로 단위를 실습합니다.

1. `px`
2. RGB와 HEX 색상
3. `%`
4. `em`
5. `rem`
6. `vh`
7. `vw`
8. `vmin`
9. `vmax`

동일한 중첩 구조를 사용해 단위별 계산 결과를 비교하기 좋습니다.

---

# 55. 강사님 코드에서 확인된 문제

## 55.1 `rem` 선택자 오타

강사님 코드:

```css
#em .box1 .box2 .box3 {
  font-size: 1.5rem;
}
```

주석은 `rem`을 설명하지만 선택자는 여전히 `#em`입니다.

또한 HTML에도 별도의 `id="rem"` 영역이 없습니다.

따라서 강사님 예제는 다음 결과가 됩니다.

- `.box1`: `1.5em`
- `.box2`: `1.5em`
- `.box3`: `1.5rem`

이는 `em`과 `rem`의 차이를 한 구조 안에서 비교하는 실습으로 볼 수 있지만, 독립된 `rem` 구역을 보여 주는 구성은 아닙니다.

내 코드에서는 이를 다음처럼 별도 영역으로 보완했습니다.

```css
#rem .box1 {
  font-size: 1.5rem;
}

#rem .box1 .box2 {
  font-size: 1.5rem;
}

#rem .box1 .box2 .box3 {
  font-size: 1.5rem;
}
```

## 55.2 세미콜론 누락

```text
background-color: #00FF00a0
```

마지막 선언이라 브라우저가 처리할 수 있지만 다음처럼 작성합니다.

```text
background-color: #00ff00a0;
```

## 55.3 `body` 기준 설명

강사님도 `rem`이 `body` 크기를 활용한다고 기록했습니다.

정확한 기준은 `html`입니다.

## 55.4 문서 언어

```html
<html lang="en">
```

한국어 문서라면 `lang="ko"`를 사용합니다.

## 55.5 기본 글씨 비교 부족

강사님 코드에서는 픽셀 구역 위에만 기본 글씨가 표시되고 이후 구역에는 반복되지 않습니다.

내 코드는 각 단위 구역 앞에 기본 글씨를 추가해 시각 비교를 쉽게 했습니다.

## 55.6 `height: 100vh`

실습 목적에는 적절하지만 바로 뒤의 요소들이 화면 아래로 밀리므로 스크롤이 길어집니다.

실제 페이지에서는 전체 화면 섹션 목적이라면 `min-height`도 검토합니다.

---

# 56. 내 코드와 강사님 코드 비교

| 비교 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 설명량 | 계산 기준과 결과를 상세히 기록 | 핵심 정의 중심 |
| `%` | 누적되는 이유 설명 | 상대적 크기와 상속 설명 |
| `em` | 3단계 모두 `1.5em` | 3번째는 `1.5rem` |
| `rem` | 독립된 `#rem` 구역 추가 | 독립 구역 없음 |
| 색상 | 3자리·8자리 HEX 설명 추가 | 값 중심 실습 |
| 배경 상속 | 투명 배경 때문에 보인다고 설명 | 별도 설명 없음 |
| 뷰포트 | 화면 변화와 연결해 설명 | 정의 중심 |
| 기본 글씨 비교 | 각 구역 앞에 반복 | 픽셀 앞에만 표시 |
| HTML 구조 | `rem` 예제 추가 | `em` 구역까지만 있음 |
| 문서 언어 | `lang="en"` | `lang="en"` |
| 학습 성격 | 복습 주석형 | 수업 진행형 |

---

# 57. 원본을 개선한 비교 실습

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
  <title>CSS 단위 비교</title>
  <link rel="stylesheet" href="asset/css/units.css">
</head>
<body>
  <main>
    <h1>CSS 글자 단위 비교</h1>

    <section class="unit-demo unit-demo--percent">
      <h2>%</h2>
      <div class="level-1">
        150%
        <div class="level-2">
          150%
          <div class="level-3">
            150%
          </div>
        </div>
      </div>
    </section>

    <section class="unit-demo unit-demo--em">
      <h2>em</h2>
      <div class="level-1">
        1.5em
        <div class="level-2">
          1.5em
          <div class="level-3">
            1.5em
          </div>
        </div>
      </div>
    </section>

    <section class="unit-demo unit-demo--rem">
      <h2>rem</h2>
      <div class="level-1">
        1.5rem
        <div class="level-2">
          1.5rem
          <div class="level-3">
            1.5rem
          </div>
        </div>
      </div>
    </section>
  </main>
</body>
</html>
```

## CSS

```css
html {
  font-size: 100%;
}

.unit-demo {
  margin-block: 2rem;
  border: 1px solid #ccc;
}

.unit-demo--percent .level-1,
.unit-demo--percent .level-2,
.unit-demo--percent .level-3 {
  font-size: 150%;
}

.unit-demo--em .level-1,
.unit-demo--em .level-2,
.unit-demo--em .level-3 {
  font-size: 1.5em;
}

.unit-demo--rem .level-1,
.unit-demo--rem .level-2,
.unit-demo--rem .level-3 {
  font-size: 1.5rem;
}
```

---

# 58. 실무 글자 크기 체계

CSS 사용자 지정 속성으로 크기를 관리할 수 있습니다.

```css
:root {
  --font-size-xs: 0.75rem;
  --font-size-sm: 0.875rem;
  --font-size-base: 1rem;
  --font-size-lg: 1.25rem;
  --font-size-xl: 1.5rem;
  --font-size-2xl: 2rem;
}
```

```css
body {
  font-size: var(--font-size-base);
}

.help-text {
  font-size: var(--font-size-sm);
}

.page-title {
  font-size: var(--font-size-2xl);
}
```

장점:

- 반복 값 감소
- 전체 디자인 변경 용이
- 이름을 통해 역할 전달
- 일관된 디자인 시스템 구성

---

# 59. 유동형 글자 크기

```css
:root {
  --font-size-heading: clamp(2rem, 4vw, 4rem);
}
```

```css
.hero-title {
  font-size: var(--font-size-heading);
}
```

화면 크기에 따라 부드럽게 변하면서 최소·최대 크기를 제한합니다.

본문은 지나치게 유동적으로 만들기보다 읽기 안정성을 우선합니다.

```css
body {
  font-size: 1rem;
}
```

---

# 60. 실무 색상 토큰

```css
:root {
  --color-text: #1f2937;
  --color-text-muted: #6b7280;
  --color-surface: #ffffff;
  --color-surface-muted: #f3f4f6;
  --color-primary: #2563eb;
  --color-danger: #dc2626;
  --color-border: #d1d5db;
}
```

```css
body {
  color: var(--color-text);
  background-color: var(--color-surface);
}

.button--primary {
  color: white;
  background-color: var(--color-primary);
}
```

색상값을 클래스 이름에 직접 넣기보다 역할 이름으로 관리합니다.

```css
/* 변경에 취약 */
.blue-button {
  background-color: #2563eb;
}
```

```css
/* 역할 중심 */
.button--primary {
  background-color: var(--color-primary);
}
```

---

# 61. 투명 색상 토큰

```css
:root {
  --overlay-dark: rgb(0 0 0 / 50%);
  --primary-soft: rgb(37 99 235 / 12%);
}
```

```css
.modal-backdrop {
  background-color: var(--overlay-dark);
}
```

```css
.badge {
  color: var(--color-primary);
  background-color: var(--primary-soft);
}
```

---

# 62. 대비와 접근성

글자와 배경색의 대비가 부족하면 읽기 어렵습니다.

```css
/* 대비가 낮을 수 있음 */
.help-text {
  color: #bbb;
  background-color: white;
}
```

색상은 장식뿐 아니라 정보 전달 수단이므로 다음을 확인합니다.

- 본문 글자와 배경의 대비
- 링크가 일반 텍스트와 구분되는가
- 오류를 빨간색만으로 표시하지 않는가
- 포커스 테두리가 배경에서 보이는가
- 비활성 상태가 너무 흐려 읽을 수 없는가

```html
<p class="error-message">
  <span aria-hidden="true">⚠</span>
  이메일 형식을 확인하세요.
</p>
```

색상 외에 아이콘과 텍스트를 함께 사용합니다.

---

# 63. 다크 모드 색상 구조

```css
:root {
  --color-text: #1f2937;
  --color-surface: #ffffff;
  --color-border: #d1d5db;
}

@media (prefers-color-scheme: dark) {
  :root {
    --color-text: #f3f4f6;
    --color-surface: #111827;
    --color-border: #374151;
  }
}
```

컴포넌트는 토큰을 사용하므로 개별 색상을 다시 작성하지 않아도 됩니다.

```css
.card {
  color: var(--color-text);
  background-color: var(--color-surface);
  border: 1px solid var(--color-border);
}
```

다크 모드는 이후 반응형·미디어 쿼리 문서에서 더 자세히 다룰 수 있습니다.

---

# 64. 반응형 컨테이너 예제

```css
.container {
  width: min(100% - 2rem, 72rem);
  margin-inline: auto;
}
```

의미:

- 작은 화면에서는 전체 너비에서 좌우 `1rem`씩 제외
- 큰 화면에서는 최대 `72rem`
- 가운데 정렬

기존 방식:

```css
.container {
  width: 1200px;
}
```

고정 너비는 작은 화면에서 가로 스크롤을 만들 수 있습니다.

---

# 65. 전체 화면 Hero 예제

```css
.hero {
  display: grid;
  min-height: 100vh;
  min-height: 100dvh;
  padding: clamp(1rem, 4vw, 4rem);
  place-items: center;
}
```

```css
.hero__title {
  max-width: 18ch;
  font-size: clamp(2rem, 7vw, 5rem);
}
```

사용 단위:

- `vh`, `dvh`: 화면 높이
- `clamp()`: 반응형 패딩과 글자
- `ch`: 제목 한 줄 길이 제한
- `rem`: 접근 가능한 최소·최대 크기

---

# 66. 카드 컴포넌트 예제

```css
.card {
  padding: 1.5rem;
  border: 1px solid rgb(0 0 0 / 12%);
  border-radius: 0.75rem;
  background-color: #fff;
}

.card__title {
  margin: 0;
  color: #1f2937;
  font-size: 1.25rem;
}

.card__description {
  max-width: 60ch;
  color: #6b7280;
  font-size: 1rem;
  line-height: 1.6;
}
```

단위 선택 이유:

| 값 | 이유 |
| --- | --- |
| `1px` | 얇은 테두리 |
| `rem` | 사용자 글자 설정과 비례한 크기 |
| `ch` | 읽기 가능한 줄 길이 |
| 알파 RGB | 배경에 자연스럽게 섞이는 테두리 |

---

# 67. 개발자 도구로 계산값 확인

Elements에서 요소를 선택한 뒤 Computed 영역에서 다음을 확인합니다.

- `font-size`
- `width`
- `height`
- `color`
- `background-color`

예를 들어 CSS가 다음과 같아도:

```css
.box {
  font-size: 1.5em;
}
```

Computed에는 실제 계산된 값이 표시될 수 있습니다.

```text
font-size: 24px
```

중첩된 `em`, `%`, `rem`을 학습할 때 계산값을 직접 비교하면 이해하기 쉽습니다.

---

# 68. 단위가 기대와 다를 때 점검 순서

1. 기준 요소의 계산된 크기는 얼마인가?
2. 해당 속성에서 `%`의 기준은 무엇인가?
3. `em`이 부모의 글자 크기에 누적되고 있는가?
4. `rem`의 루트 글자 크기가 변경됐는가?
5. `width: 100%`의 containing block은 무엇인가?
6. 부모 높이가 `auto`인데 `height: 100%`를 사용했는가?
7. 모바일 브라우저에서 `100vh` 문제인가?
8. `box-sizing` 때문에 실제 크기 계산이 달라졌는가?
9. 더 높은 우선순위 규칙이 덮고 있는가?
10. Computed 값은 무엇인가?

---

# 69. 색상이 기대와 다를 때 점검 순서

1. 색상값 문법이 올바른가?
2. 3자리 HEX 축약이 정확한가?
3. 8자리 HEX의 마지막 두 자리가 알파인지 이해했는가?
4. 부모 배경과 반투명 색상이 합성되고 있는가?
5. `opacity`가 부모에 적용되어 자식도 흐려졌는가?
6. `color`가 상속되고 있는가?
7. 다른 규칙이 덮어썼는가?
8. 브라우저 개발자 도구의 색상 미리보기는 무엇인가?
9. 다크 모드 미디어 쿼리가 적용 중인가?
10. 사용자 지정 속성값이 올바른가?

---

# 70. 자주 하는 실수

## 70.1 `rem`을 `body` 기준으로 이해

기준은 루트 `html`입니다.

## 70.2 `%`의 기준을 항상 부모 너비라고 생각

속성마다 기준이 다릅니다.

## 70.3 중첩된 `em` 누적을 놓침

부모의 계산값에 다시 곱해집니다.

## 70.4 `100vw`를 페이지 전체 너비에 무조건 사용

스크롤바 때문에 가로 스크롤이 생길 수 있습니다.

## 70.5 `height: 100%`만으로 전체 화면 기대

부모 높이 계산 조건이 필요합니다.

## 70.6 `100vh`로 모바일 화면이 항상 정확하다고 생각

동적 브라우저 UI 때문에 `dvh`를 검토해야 합니다.

## 70.7 알파 색상과 `opacity` 혼동

알파 색상은 해당 색상만, `opacity`는 요소 전체와 자식까지 영향을 줍니다.

## 70.8 배경색이 상속됐다고 생각

자식의 투명 배경 뒤로 부모 색상이 보이는 것입니다.

## 70.9 6자리 HEX를 무조건 3자리로 축약

각 채널의 두 문자가 같아야 합니다.

## 70.10 색상만으로 상태 전달

텍스트, 아이콘, 형태를 함께 사용합니다.

---


# 종합실습

## 문제 1. 픽셀 단위

`.title`의 글자 크기를 `32px`, 테두리를 `1px solid #333`으로 지정하세요.

## 문제 2. 퍼센트 계산

부모 글자 크기가 `20px`일 때 자식의 `font-size: 150%`는 몇 px인가요?

## 문제 3. 중첩 퍼센트

루트 글자 크기를 `16px`로 가정합니다.

```css
.level-1 {
  font-size: 125%;
}

.level-2 {
  font-size: 125%;
}
```

`.level-2`의 최종 글자 크기를 계산하세요.

## 문제 4. 중첩 `em`

루트 글자 크기를 `16px`로 가정합니다.

```css
.a {
  font-size: 1.5em;
}

.b {
  font-size: 2em;
}
```

`.b`가 `.a`의 자식일 때 `.b`의 최종 크기를 계산하세요.

## 문제 5. `rem`

루트 `html`의 글자 크기가 `18px`일 때 `2rem`은 몇 px인가요?

## 문제 6. `em`과 `rem` 비교

부모의 글자 크기가 `24px`, 루트 글자 크기가 `16px`일 때 다음 값을 계산하세요.

```css
.a {
  font-size: 1.5em;
}

.b {
  font-size: 1.5rem;
}
```

## 문제 7. `vw`

뷰포트 너비가 `1440px`일 때 `25vw`는 몇 px인가요?

## 문제 8. `vh`

뷰포트 높이가 `900px`일 때 `80vh`는 몇 px인가요?

## 문제 9. `vmin`

뷰포트가 `1200px × 800px`일 때 `50vmin`은 몇 px인가요?

## 문제 10. `vmax`

뷰포트가 `390px × 844px`일 때 `10vmax`는 몇 px인가요?

## 문제 11. HEX 축약

다음 색상을 가능한 경우 3자리 HEX로 줄이세요.

1. `#ffffff`
2. `#00ffaa`
3. `#112233`
4. `#12abef`

## 문제 12. HEX 확장

다음 값을 6자리 또는 8자리로 확장하세요.

1. `#f00`
2. `#0fa`
3. `#0008`

## 문제 13. RGB 작성

다음 색상을 RGB로 작성하세요.

1. 빨강
2. 초록
3. 파랑
4. 검정
5. 흰색

## 문제 14. 반투명 배경

파란색을 40% 불투명도로 표현하는 CSS를 RGBA 방식으로 작성하세요.

## 문제 15. 알파와 `opacity`

배경만 반투명하게 만들고 내부 글자는 완전히 불투명하게 유지하려면 어떤 방식을 사용해야 하나요? 코드도 작성하세요.

## 문제 16. 상속 판단

다음 속성이 일반적으로 상속되는지 작성하세요.

1. `color`
2. `font-size`
3. `background-color`
4. `margin`
5. `line-height`

## 문제 17. 전체 화면 섹션

모바일 환경을 고려해 `.hero`가 최소 화면 높이를 차지하도록 작성하세요. `vh` 폴백과 `dvh`를 함께 사용하세요.

## 문제 18. 반응형 제목

`.hero-title`의 글자 크기가 최소 `2rem`, 선호 `6vw`, 최대 `5rem`이 되도록 작성하세요.

## 문제 19. 반응형 컨테이너

다음 조건의 컨테이너를 작성하세요.

- 화면 좌우에 최소 `1rem` 여백
- 최대 너비 `72rem`
- 가운데 정렬

## 문제 20. 원본 오류 수정

다음 설명과 코드를 수정하세요.

```css
/* rem은 body의 글자 크기를 기준으로 한다. */
#em .box1 .box2 .box3 {
  font-size: 1.5rem
}
```

독립적인 `#rem` 구역의 세 단계가 모두 `1.5rem`이 되도록 작성하세요.

## 문제 21. 사용자 지정 속성

본문색, 배경색, 주요색을 `:root`에 선언하고 `.button`에서 사용하세요.

## 문제 22. 종합 실습

다음 요구사항의 Hero 영역을 작성하세요.

- 최소 화면 높이
- 모바일 동적 뷰포트 지원
- 제목 크기 `clamp()`
- 제목 최대 줄 너비 `18ch`
- 좌우 패딩 최소 `1rem`, 화면에 따라 증가, 최대 `4rem`
- 반투명한 검정 오버레이
- 글자색 흰색
- 모든 색상과 크기는 가능한 한 의미 있는 사용자 지정 속성으로 관리

---

# 종합실습 정답과 해설

## 정답 1

```css
.title {
  border: 1px solid #333;
  font-size: 32px;
}
```

## 정답 2

```text
20px × 1.5 = 30px
```

정답은 `30px`입니다.

## 정답 3

```text
16px × 1.25 = 20px
20px × 1.25 = 25px
```

`.level-2`는 `25px`입니다.

## 정답 4

```text
.a: 16px × 1.5 = 24px
.b: 24px × 2 = 48px
```

`.b`는 `48px`입니다.

## 정답 5

```text
18px × 2 = 36px
```

정답은 `36px`입니다.

## 정답 6

```text
1.5em: 24px × 1.5 = 36px
1.5rem: 16px × 1.5 = 24px
```

## 정답 7

```text
1440px × 0.25 = 360px
```

정답은 `360px`입니다.

## 정답 8

```text
900px × 0.8 = 720px
```

정답은 `720px`입니다.

## 정답 9

작은 값은 `800px`입니다.

```text
800px × 0.5 = 400px
```

정답은 `400px`입니다.

## 정답 10

큰 값은 `844px`입니다.

```text
844px × 0.1 = 84.4px
```

정답은 `84.4px`입니다.

## 정답 11

```text
#ffffff → #fff
#00ffaa → #0fa
#112233 → #123
#12abef → 축약 불가
```

각 RGB 채널의 두 문자가 같을 때만 줄일 수 있습니다.

## 정답 12

```text
#f00  → #ff0000
#0fa  → #00ffaa
#0008 → #00000088
```

## 정답 13

```css
.red {
  color: rgb(255, 0, 0);
}

.green {
  color: rgb(0, 255, 0);
}

.blue {
  color: rgb(0, 0, 255);
}

.black {
  color: rgb(0, 0, 0);
}

.white {
  color: rgb(255, 255, 255);
}
```

## 정답 14

```css
.box {
  background-color: rgba(0, 0, 255, 0.4);
}
```

최신 문법으로는 다음도 가능합니다.

```css
.box {
  background-color: rgb(0 0 255 / 40%);
}
```

## 정답 15

색상 자체에 알파 채널을 사용합니다.

```css
.card {
  color: #111;
  background-color: rgb(0 0 255 / 40%);
}
```

`opacity`를 부모에 지정하지 않으므로 내부 글자는 불투명하게 유지됩니다.

## 정답 16

| 속성 | 상속 |
| --- | --- |
| `color` | 예 |
| `font-size` | 예 |
| `background-color` | 아니요 |
| `margin` | 아니요 |
| `line-height` | 예 |

## 정답 17

```css
.hero {
  min-height: 100vh;
  min-height: 100dvh;
}
```

지원하지 않는 브라우저는 앞의 `vh`를 사용하고, 지원하는 브라우저는 뒤의 `dvh`로 덮어씁니다.

## 정답 18

```css
.hero-title {
  font-size: clamp(2rem, 6vw, 5rem);
}
```

## 정답 19

```css
.container {
  width: min(100% - 2rem, 72rem);
  margin-inline: auto;
}
```

전체 너비에서 좌우 `1rem`씩 총 `2rem`을 제외합니다.

## 정답 20

설명:

```css
/* rem은 루트 html 요소의 font-size를 기준으로 한다. */
```

코드:

```css
#rem .box1 {
  font-size: 1.5rem;
}

#rem .box1 .box2 {
  font-size: 1.5rem;
}

#rem .box1 .box2 .box3 {
  font-size: 1.5rem;
}
```

모든 단계가 루트를 기준으로 계산됩니다.

## 정답 21

```css
:root {
  --color-text: #1f2937;
  --color-surface: #ffffff;
  --color-primary: #2563eb;
}

body {
  color: var(--color-text);
  background-color: var(--color-surface);
}

.button {
  color: white;
  background-color: var(--color-primary);
}
```

## 정답 22

### HTML

```html
<section class="hero">
  <div class="hero__content">
    <h1 class="hero__title">
      AI 서비스 개발자로 성장하세요
    </h1>
    <p class="hero__description">
      HTML부터 AI Agent 프로젝트까지 학습합니다.
    </p>
  </div>
</section>
```

### CSS

```css
:root {
  --color-white: #ffffff;
  --color-overlay: rgb(0 0 0 / 55%);

  --space-page-min: 1rem;
  --space-page-fluid: 4vw;
  --space-page-max: 4rem;

  --font-title-min: 2rem;
  --font-title-fluid: 7vw;
  --font-title-max: 5rem;
}

.hero {
  display: grid;
  min-height: 100vh;
  min-height: 100dvh;
  padding-inline: clamp(
    var(--space-page-min),
    var(--space-page-fluid),
    var(--space-page-max)
  );
  color: var(--color-white);
  background:
    linear-gradient(
      var(--color-overlay),
      var(--color-overlay)
    ),
    url("../images/hero.jpg") center / cover;
  place-items: center;
}

.hero__title {
  max-width: 18ch;
  font-size: clamp(
    var(--font-title-min),
    var(--font-title-fluid),
    var(--font-title-max)
  );
}
```

---

# 최종 체크리스트

## 단위

- [ ] `px`, `%`, `em`, `rem`의 기준을 구분했다.
- [ ] `%`가 속성마다 다른 기준을 가질 수 있음을 확인했다.
- [ ] 중첩된 `em`과 `%`의 누적을 계산했다.
- [ ] `rem`이 `body`가 아니라 `html` 기준임을 확인했다.
- [ ] 글자 크기에는 사용자 설정을 고려했다.
- [ ] `width: 100%`와 `100vw`를 구분했다.
- [ ] `height: 100%`의 부모 높이 조건을 확인했다.
- [ ] 모바일 전체 화면에서 `dvh`를 검토했다.
- [ ] 고정값이 필요한 곳과 상대값이 필요한 곳을 구분했다.
- [ ] `clamp()`에 최소·선호·최대값을 설정했다.

## 색상

- [ ] HEX 3자리 축약 조건을 확인했다.
- [ ] 8자리 HEX의 마지막 두 자리가 알파임을 이해했다.
- [ ] RGBA 알파값 범위를 확인했다.
- [ ] 배경만 투명하게 할 때 `opacity`를 사용하지 않았다.
- [ ] `color`의 상속 여부를 확인했다.
- [ ] `background-color`가 상속되지 않음을 확인했다.
- [ ] 색상 대비를 확인했다.
- [ ] 색상만으로 오류나 상태를 전달하지 않았다.
- [ ] 반복 색상은 사용자 지정 속성으로 관리했다.
- [ ] 다크 모드에서도 대비를 확인했다.

## 원본 코드 검수

- [ ] `lang="ko"`를 사용했다.
- [ ] `rem` 기준 설명을 `html`로 수정했다.
- [ ] 강사님 코드의 `#em` / `rem` 혼합을 구분했다.
- [ ] 세미콜론 누락을 수정했다.
- [ ] 중첩 `div`의 닫는 구조를 확인했다.
- [ ] `vmin`, `vmax`가 콘텐츠가 아니라 뷰포트 기준임을 확인했다.
- [ ] 기본 `16px`은 가정값임을 명시했다.

---

# 핵심 요약

- CSS 단위는 값이 무엇을 기준으로 계산되는지를 결정한다.
- `px`는 CSS 픽셀 기준의 절대 길이 단위다.
- 브라우저 기본 글자 크기는 일반적으로 `16px`이지만 사용자 설정에 따라 달라질 수 있다.
- `font-size`의 `%`는 부모의 계산된 글자 크기를 기준으로 한다.
- 중첩된 `%`와 `em`은 부모 계산값에 다시 곱해져 누적될 수 있다.
- `rem`은 `body`가 아니라 루트 `html`의 글자 크기를 기준으로 한다.
- 글자 체계에는 `rem`, 컴포넌트 내부 비례에는 `em`이 유용하다.
- `vw`는 뷰포트 너비, `vh`는 뷰포트 높이를 기준으로 한다.
- `vmin`은 너비·높이 중 작은 값, `vmax`는 큰 값을 기준으로 한다.
- 모바일 전체 화면에서는 `100vh`와 함께 `100dvh`를 검토한다.
- `width: 100%`와 `100vw`는 기준이 다르다.
- `clamp()`는 반응형 값의 최소·선호·최대를 한 번에 지정한다.
- RGB는 빨강·초록·파랑 채널로 색상을 표현한다.
- RGBA와 8자리 HEX는 알파 채널을 포함한다.
- `#0fa`는 `#00ffaa`와 같다.
- 6자리 HEX는 각 채널의 두 문자가 같을 때만 3자리로 줄일 수 있다.
- 알파 색상은 해당 색상만 투명하게 하고 `opacity`는 자식까지 포함한 요소 전체를 투명하게 한다.
- `color`와 `font-size`는 상속되지만 `background-color`는 일반적으로 상속되지 않는다.
- 자식의 투명 배경 때문에 부모 배경이 보이는 현상은 상속이 아니다.
- 원본 강사님 코드의 세 번째 `em` 요소는 실제로 `rem`을 사용하며 독립된 `rem` 구역은 없다.
- 내 코드는 별도의 `#rem` 구역을 추가해 세 단위의 차이를 비교하기 쉽게 보완했다.
- 실무에서는 크기와 색상을 CSS 사용자 지정 속성으로 관리하면 일관성과 유지보수가 좋아진다.
