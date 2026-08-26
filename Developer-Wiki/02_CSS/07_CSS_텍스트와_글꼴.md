---
title: CSS 텍스트와 글꼴
version: v3.0-encyclopedia
last_updated: 2026-08-06
status: Completed
---

# CSS 텍스트와 글꼴

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `07_CSS_텍스트와_글꼴.md` |
| 분류 | `02_CSS` |
| 원본 기준 | `workspace_html/css/07_font.html`, `workspace_html/css/asset/css/07_font.css`, `workspace_teacher/workspace_html/css/07_font.html`, `workspace_teacher/workspace_html/css/asset/css/07_font.css` |
| 핵심 범위 | `@font-face`, `font-family`, `font-size`, `font-style`, `font-weight`, `line-height`, `letter-spacing`, `text-align`, `text-decoration`, `white-space`, `text-overflow`, `overflow-wrap`, `word-break` |
| 프로젝트 연결 | 본문 타이포그래피, 제목 체계, 버튼·메뉴 글꼴, 한 줄 말줄임표, 긴 URL 처리, 웹폰트 성능, 접근성 |

> 이 문서는 내 코드와 강사님 코드의 `07_font.html`, `07_font.css`를 비교해 글꼴·크기·굵기·줄높이·자간·정렬·장식·줄바꿈의 실제 동작을 정리한다. 잘못된 HTML 중첩과 절대적인 글꼴 설명은 수정하고, 웹폰트 Fallback·가독성·말줄임표·긴 문자열 처리까지 실무 기준으로 연결한다.

---

# 학습 목표

- 웹폰트와 시스템 폰트의 차이를 설명한다.
- `@font-face`의 `font-family`, `src`, `format()`, `font-display` 역할을 설명한다.
- `font-family`에 대체 글꼴을 지정하는 이유를 이해한다.
- `font-size`와 상속의 관계를 설명한다.
- `font-style`과 의미 요소 `<em>`의 역할을 구분한다.
- `font-weight` 숫자값과 실제 폰트 파일 지원 범위를 구분한다.
- `line-height`를 단위 없는 값으로 작성하는 이유를 설명한다.
- 한 줄 텍스트의 수직 가운데 정렬에 `line-height`를 사용할 때의 한계를 이해한다.
- `letter-spacing`의 양수와 음수 효과를 설명한다.
- `text-align`이 블록 컨테이너 내부의 인라인 콘텐츠에 적용되는 원리를 이해한다.
- `text-decoration`으로 밑줄, 취소선, 링크 장식을 제어한다.
- `white-space`, `overflow`, `text-overflow`를 조합해 한 줄 말줄임표를 만든다.
- `overflow-wrap`과 `word-break`의 차이를 설명한다.
- 시각적으로 큰 글자와 의미상 제목 요소의 차이를 이해한다.
- 내 코드와 강사님 코드의 차이와 오류를 찾는다.
- 읽기 쉬운 본문 타이포그래피와 접근 가능한 링크 스타일을 작성한다.

---

# 1. 타이포그래피란?

웹 타이포그래피는 글자의 모양뿐 아니라 다음 요소를 함께 설계하는 작업입니다.

- 글꼴
- 글자 크기
- 굵기
- 기울임
- 줄 높이
- 자간
- 정렬
- 장식
- 줄바꿈
- 텍스트 넘침

```css
body {
  color: #222;
  font-family: Arial, sans-serif;
  font-size: 1rem;
  line-height: 1.6;
}
```

타이포그래피는 디자인과 가독성, 접근성, 브랜드 인상에 직접 영향을 줍니다.

---

# 2. 원본 실습 구조

원본 HTML은 다음 순서로 구성되어 있습니다.

1. 기본 글씨 비교
2. `font-size`
3. 웹폰트 `font-family`
4. `font-style`
5. 여러 `font-weight`
6. `line-height`
7. 한 줄 수직 가운데 정렬
8. `letter-spacing`
9. `text-align: justify`
10. 오른쪽 정렬
11. `text-decoration`
12. 링크 장식 제거와 방문 상태
13. 한 줄 말줄임표
14. 긴 단어 줄바꿈
15. 실제 `h1`과 CSS로 만든 가짜 제목 비교

이 흐름은 글꼴 속성에서 텍스트 배치와 넘침 처리까지 단계적으로 확인하기 좋습니다.

---

# 3. 원본 HTML 구조 오류

내 코드와 강사님 코드 모두 다음 구조를 사용합니다.

```html
<p class="size">
  글씨를 적어보자.
  <div>
    자식의 글씨를 적어보자.
  </div>
</p>
```

`p` 요소 안에는 일반적인 `div` 같은 흐름 콘텐츠를 넣을 수 없습니다.

브라우저는 실제 DOM을 자동 보정하여 `p`를 `div` 앞에서 닫을 수 있습니다.

개발자가 의도한 구조:

```html
<p class="size">
  글씨를 적어보자.
  <div>자식의 글씨</div>
</p>
```

실제 DOM은 다음과 비슷하게 바뀔 수 있습니다.

```html
<p class="size">
  글씨를 적어보자.
</p>

<div>
  자식의 글씨
</div>

<p></p>
```

따라서 자식에게 글자 크기나 글꼴이 상속되는 모습을 확인하려던 실습 결과가 의도와 달라질 수 있습니다.

---

# 4. 올바른 상속 실습 구조

블록 자식을 포함하려면 부모도 `div`를 사용합니다.

```html
<div class="size">
  글씨를 적어보자.

  <div>
    자식의 글씨를 적어보자.
  </div>
</div>
```

문단 안에서 인라인 자식을 확인하려면 `span`을 사용합니다.

```html
<p class="size">
  글씨를 적어보자.
  <span>자식의 글씨를 적어보자.</span>
</p>
```

이렇게 해야 `font-size`와 `font-family`의 상속을 정확히 확인할 수 있습니다.

---

# 5. `font-size`

원본:

```css
.size {
  font-size: 32px;
}
```

`font-size`는 글자 크기를 지정합니다.

자식에게 별도의 크기가 없으면 상속됩니다.

```css
.parent {
  font-size: 32px;
}
```

```html
<div class="parent">
  부모 글자
  <span>자식 글자</span>
</div>
```

`span`도 기본적으로 `32px`을 사용합니다.

---

# 6. 글자 크기 단위

대표 단위:

| 단위 | 기준 | 특징 |
| --- | --- | --- |
| `px` | CSS 픽셀 | 고정적인 수치 |
| `em` | 부모 또는 현재 글자 크기 | 중첩 시 누적 가능 |
| `rem` | 루트 `html` 글자 크기 | 일관된 크기 체계 |
| `%` | 부모 글자 크기 | `em`과 유사한 누적 가능 |
| `clamp()` | 최소·유동·최대 | 반응형 제목에 유용 |

원본은 `32px`을 사용합니다.

실무 제목 예:

```css
.page-title {
  font-size: clamp(2rem, 5vw, 4rem);
}
```

본문은 읽기 안정성을 위해 지나친 유동 크기를 피합니다.

```css
body {
  font-size: 1rem;
}
```

---

# 7. 웹폰트란?

사용자 컴퓨터에 설치되어 있지 않은 글꼴도 웹에서 내려받아 사용할 수 있습니다.

원본 내 코드 주석:

```text
웹폰트, 컴퓨터에 설치 없어도 쓰게 할 수 있도록
링크를 다운받아놓는 선언
```

핵심적으로 맞습니다.

```css
@font-face {
  font-family: "CustomFont";
  src: url("custom-font.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

브라우저는 지정된 파일을 내려받아 해당 이름의 글꼴로 사용합니다.

---

# 8. 내 코드의 웹폰트

```css
@font-face {
  font-family: "NostalgicPoliceVibe";
  src:
    url("https://cdn.jsdelivr.net/gh/projectnoonnu/2601-6@1.0/Griun_PolSensibility-Rg.woff2")
    format("woff2");
  font-weight: normal;
  font-display: swap;
}
```

특징:

- 글꼴 이름: `NostalgicPoliceVibe`
- 파일 형식: WOFF2
- 굵기: `normal`
- 표시 정책: `swap`
- 외부 CDN 사용

내 코드의 `.font`:

```css
.font {
  font-family: "NostalgicPoliceVibe", Arial;
}
```

---

# 9. 강사님 코드의 웹폰트

```css
@font-face {
  font-family: "OngleipParkDahyeon";
  src:
    url("https://cdn.jsdelivr.net/gh/projectnoonnu/2411-3@1.0/Ownglyph_ParkDaHyun.woff2")
    format("woff2");
  font-weight: normal;
  font-display: swap;
}
```

```css
.font {
  font-family: "OngleipParkDahyeon", Arial;
}
```

내 코드와 강사님 코드는 서로 다른 웹폰트를 사용합니다.

이는 오류가 아니라 사용자가 다른 폰트로 교체해 실험한 차이입니다.

---

# 10. `@font-face` 주요 속성

## 10.1 `font-family`

웹폰트 내부에서 사용할 이름입니다.

```css
font-family: "ProjectFont";
```

이후 선택자에서 같은 이름을 사용합니다.

```css
.title {
  font-family: "ProjectFont", sans-serif;
}
```

## 10.2 `src`

폰트 파일 위치와 형식을 지정합니다.

```css
src:
  url("../fonts/project-font.woff2")
  format("woff2");
```

## 10.3 `font-weight`

해당 파일이 어떤 굵기를 제공하는지 선언합니다.

```css
font-weight: 400;
```

## 10.4 `font-style`

해당 파일의 스타일을 지정합니다.

```css
font-style: normal;
```

원본에서는 생략되어 기본값 `normal`이 사용됩니다.

## 10.5 `font-display`

폰트 파일이 로드되는 동안 텍스트를 어떻게 표시할지 지정합니다.

```css
font-display: swap;
```

---

# 11. `font-display: swap`

원본의 두 웹폰트 모두 다음을 사용합니다.

```css
font-display: swap;
```

동작 개념:

1. 먼저 대체 글꼴로 텍스트를 표시한다.
2. 웹폰트 로드가 완료되면 교체한다.

장점:

- 텍스트가 빈 화면으로 오래 남는 것을 줄인다.
- 콘텐츠를 빠르게 읽을 수 있다.

주의:

- 대체 글꼴과 웹폰트의 글자 폭이 다르면 레이아웃 이동이 발생할 수 있다.
- 폰트 크기와 자간 차이 때문에 줄바꿈이 바뀔 수 있다.

---

# 12. 대체 글꼴

원본:

```css
font-family: "NostalgicPoliceVibe", Arial;
```

웹폰트 로드에 실패하면 `Arial`을 사용합니다.

마지막에는 일반 글꼴 계열을 추가하는 것이 좋습니다.

```css
.font {
  font-family:
    "NostalgicPoliceVibe",
    Arial,
    sans-serif;
}
```

한글 폰트의 대체 체계도 고려합니다.

```css
body {
  font-family:
    "Pretendard",
    "Noto Sans KR",
    Arial,
    sans-serif;
}
```

---

# 13. 로컬 폰트와 외부 CDN

원본은 jsDelivr CDN의 웹폰트를 사용합니다.

장점:

- 실습이 간편하다.
- 별도 파일 관리가 필요 없다.

주의:

- 외부 서비스 장애에 영향을 받는다.
- 주소 변경이나 제거 가능성이 있다.
- 개인정보·보안·사내 정책 검토가 필요할 수 있다.
- 성능과 캐시 정책을 직접 제어하기 어렵다.

프로젝트 로컬 관리:

```css
@font-face {
  font-family: "ProjectFont";
  src:
    url("../fonts/project-font.woff2")
    format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

---

# 14. 여러 굵기의 웹폰트

각 굵기 파일을 별도로 등록할 수 있습니다.

```css
@font-face {
  font-family: "ProjectFont";
  src: url("../fonts/project-regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: "ProjectFont";
  src: url("../fonts/project-bold.woff2") format("woff2");
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}
```

```css
body {
  font-family: "ProjectFont", sans-serif;
}

strong {
  font-weight: 700;
}
```

지원하지 않는 굵기를 지정하면 브라우저가 가장 가까운 굵기를 선택하거나 합성할 수 있습니다.

---

# 15. `font-family`

```css
.font {
  font-family: "NostalgicPoliceVibe", Arial, sans-serif;
}
```

`font-family`도 상속되는 속성입니다.

```html
<div class="font">
  부모 글꼴
  <span>자식 글꼴</span>
</div>
```

자식에 별도 글꼴이 없으면 부모 글꼴을 사용합니다.

원본의 `p > div` 구조 오류 때문에 상속 실험이 정확하지 않을 수 있으므로 올바른 중첩으로 수정해야 합니다.

---

# 16. `font-style`

원본:

```css
.style {
  font-style: italic;
}
```

대표 값:

| 값 | 설명 |
| --- | --- |
| `normal` | 기본 스타일 |
| `italic` | 이탤릭 글꼴 사용 |
| `oblique` | 기울인 형태 |

웹폰트가 실제 이탤릭 파일을 제공하지 않으면 브라우저가 기울임을 합성할 수 있습니다.

```css
em {
  font-style: italic;
}
```

---

# 17. `font-style`과 `<em>`

내 코드 주석:

```text
html em으로 감싸도 되지만, 그건 강조체 css는 예쁘게표현
```

이 설명은 의미와 표현을 구분해야 합니다.

```html
<em>중요한 강조</em>
```

`em`은 의미상 강조를 나타냅니다.

```css
.decorative-italic {
  font-style: italic;
}
```

`font-style`은 시각적 표현입니다.

정리:

- 의미상 강조가 필요하면 `<em>`
- 단순 디자인 기울임이면 CSS 클래스
- `<em>`의 기본 기울임은 CSS로 변경될 수 있음
- 기울임 모양만으로 의미를 전달하지 않음

---

# 18. `font-weight`

원본은 다음 값을 비교합니다.

```css
.fw-100 { font-weight: 100; }
.fw-300 { font-weight: 300; }
.fw-500 { font-weight: 500; }
.fw-700 { font-weight: 700; }
.fw-900 { font-weight: 900; }
.fw-1000 { font-weight: 1000; }
.fw-2000 { font-weight: 2000; }
.fw-bold { font-weight: bold; }
```

일반적으로 많이 사용하는 값:

```text
100, 200, 300, 400, 500, 600, 700, 800, 900
```

가변 폰트는 더 연속적인 범위를 지원할 수 있습니다.

---

# 19. `font-weight` 기본값

강사님 코드 주석:

```text
기본값: 500
```

이 설명은 잘못되었습니다.

`font-weight`의 기본값은 다음입니다.

```css
font-weight: normal;
```

`normal`은 일반적으로 `400`에 해당합니다.

```text
normal ≈ 400
bold   ≈ 700
```

브라우저와 폰트의 실제 렌더링은 제공되는 굵기에 따라 달라질 수 있습니다.

---

# 20. `font-weight` 범위 보완

내 코드 주석:

```text
font-weight는 100 ~ 1,000적용이며 100단위로 사용할 수 있다
```

강사님 주석:

```text
100 ~ 1000까지 100단위로 사용 가능
```

전통적인 정적 폰트 설명에서는 `100`부터 `900`까지의 100 단위값을 주로 사용합니다.

가변 폰트의 CSS 문법은 더 넓고 연속적인 숫자 범위를 지원할 수 있지만, 실제 사용 가능 범위는 폰트가 제공하는 축에 따라 달라집니다.

원본의 다음 값:

```css
font-weight: 1000;
font-weight: 2000;
```

은 학습 실험으로 보존할 수 있지만 일반적인 폰트에서 기대한 굵기로 렌더링되지 않을 수 있습니다.

실무 기본값은 `100`부터 `900` 범위 안에서 폰트 지원 여부를 확인합니다.

---

# 21. 실제 폰트가 제공하는 굵기

내 코드 주석:

```text
단, 100, 300, 900 3개의 패밀리만 가지고 있다면
이것만 표현될수도 있음
```

핵심적으로 맞습니다.

CSS에서 `500`을 요청해도 폰트 파일이 `400`과 `700`만 제공하면 브라우저가 가까운 굵기를 선택할 수 있습니다.

```css
.text {
  font-weight: 500;
}
```

실제 결과는 폰트 파일 구성에 따라 달라집니다.

개발자 도구의 Fonts 패널에서 실제 렌더링 폰트를 확인할 수 있습니다.

---

# 22. `bold`와 숫자값

```css
.fw-bold {
  font-weight: bold;
}
```

`bold`는 일반적으로 `700`에 해당합니다.

```css
strong {
  font-weight: 700;
}
```

`bolder`, `lighter`는 부모 굵기를 기준으로 상대적으로 더 굵거나 얇게 선택합니다.

```css
.child {
  font-weight: bolder;
}
```

팀 코드에서는 명확한 숫자 체계를 사용하는 경우가 많습니다.

---

# 23. `line-height`

원본:

```css
.lh {
  line-height: 300%;
}
```

`line-height`는 줄 상자의 높이를 지정합니다.

부모 글자 크기가 `16px`이면:

```text
16px × 300% = 48px
```

두 줄 사이의 간격이 매우 넓어집니다.

---

# 24. `line-height` 값 방식

```css
.text {
  line-height: 1.6;
}
```

단위 없는 값은 현재 요소의 글자 크기에 곱해집니다.

```css
.text {
  font-size: 20px;
  line-height: 1.6;
}
```

```text
20px × 1.6 = 32px
```

다른 방식:

```css
line-height: 32px;
line-height: 160%;
line-height: 2em;
```

실무 본문에는 단위 없는 값을 많이 사용합니다.

```css
body {
  line-height: 1.6;
}
```

---

# 25. 단위 없는 `line-height`의 장점

```css
.parent {
  line-height: 1.6;
}
```

자식이 다른 글자 크기를 사용하면 자식의 글자 크기에 맞춰 줄 높이가 계산됩니다.

```css
.parent {
  font-size: 16px;
  line-height: 1.6;
}

.child {
  font-size: 24px;
}
```

자식 줄 높이:

```text
24px × 1.6 = 38.4px
```

퍼센트나 고정 길이 상속은 예상하지 못한 줄 높이를 만들 수 있으므로 본문 체계에는 단위 없는 값을 권장하는 경우가 많습니다.

---

# 26. 한 줄 수직 가운데 정렬

원본:

```css
.middle {
  border: 1px solid red;
  height: 100px;
  line-height: 100px;
  width: 300px;
  text-align: center;
}
```

한 줄 텍스트의 줄 높이를 요소 높이와 같게 만들어 세로 중앙처럼 보이게 합니다.

```text
height: 100px
line-height: 100px
```

가로 가운데 정렬:

```css
text-align: center;
```

---

# 27. `line-height` 수직 정렬의 한계

내 코드 주석:

```text
height를 주고 line-height를 주면 가운데 정렬 가능
```

한 줄 텍스트에서는 사용할 수 있지만 일반적인 수직 정렬 방법으로 확장하면 안 됩니다.

문제:

- 두 줄이 되면 전체 높이가 200px이 될 수 있다.
- 반응형 글자 확대에 취약하다.
- 아이콘과 텍스트 조합에서 어긋날 수 있다.
- 고정 높이에 의존한다.

현대적인 방법:

```css
.middle {
  display: flex;
  width: 300px;
  min-height: 100px;
  align-items: center;
  justify-content: center;
}
```

---

# 28. `letter-spacing`

원본 내 코드:

```css
.spacing {
  letter-spacing: 0em;
}
```

주석 실험값:

```css
/* letter-spacing: 1em */
/* letter-spacing: -0.1em */
```

강사님 최종 적용값:

```css
letter-spacing: -0.1em;
```

내 코드 최종 적용값:

```css
letter-spacing: 0em;
```

두 코드의 화면 결과가 다른 주요 지점입니다.

---

# 29. `letter-spacing`의 의미

글자 사이 간격을 조절합니다.

```css
.wide {
  letter-spacing: 0.1em;
}
```

```css
.tight {
  letter-spacing: -0.05em;
}
```

원본 내 코드 주석:

```text
0이 기본값이며 1em은 1글자가 들어갈 자리를 만듦
```

보완:

- 기본값은 `normal`이다.
- `0`은 추가 간격이 없는 상태로 `normal`과 비슷해 보일 수 있다.
- `1em`은 현재 글자 크기만큼의 추가 간격을 각 문자 사이에 넣는다.
- “한 글자가 들어갈 자리”라는 표현은 근사적 설명이다.
- 한글과 영문에서 시각 효과가 다를 수 있다.

---

# 30. 자간 사용 주의

너무 큰 양수 자간:

```css
.title {
  letter-spacing: 1em;
}
```

문장이 과도하게 벌어져 읽기 어렵습니다.

너무 큰 음수 자간:

```css
.text {
  letter-spacing: -0.2em;
}
```

글자가 겹칠 수 있습니다.

실무 예:

```css
.page-title {
  letter-spacing: -0.02em;
}
```

본문은 브라우저와 폰트 기본 자간을 유지하는 경우가 많습니다.

---

# 31. `text-align`

원본:

```css
.justify {
  text-align: justify;
}
```

`text-align`은 블록 컨테이너 내부의 인라인 콘텐츠 정렬을 지정합니다.

대표 값:

- `left`
- `right`
- `center`
- `justify`
- `start`
- `end`

논리 방향을 고려하면 `start`, `end`도 유용합니다.

```css
.text {
  text-align: start;
}
```

---

# 32. `text-align: justify`

```css
.justify {
  text-align: justify;
}
```

각 줄의 양쪽 끝을 맞추기 위해 단어 사이 간격을 조정합니다.

장점:

- 좌우 가장자리가 정렬된 시각적 형태

주의:

- 좁은 영역에서 단어 사이가 과도하게 벌어질 수 있다.
- 영문과 한글에서 결과가 다를 수 있다.
- 마지막 줄은 일반적으로 양쪽 정렬되지 않는다.
- 긴 단어가 있으면 간격이 불균형해질 수 있다.

본문 가독성을 실제 화면에서 확인해야 합니다.

---

# 33. 오른쪽 정렬 원본 비교

내 코드:

```html
<a href="#">inline 요소</a>

<div class="right">
  <a href="#">inline 요소</a>
</div>
```

강사님 코드:

```html
<a href="#" class="right">inline 요소</a>

<div class="right">
  <a href="#">inline 요소</a>
</div>
```

CSS:

```css
.right {
  text-align: right;
}
```

강사님 첫 링크에 `.right`를 직접 적용해도 일반 인라인 요소는 자신의 콘텐츠 너비만큼만 공간을 차지하므로 눈에 보이는 이동이 거의 없습니다.

부모 블록에 적용하면 부모의 사용 가능한 너비 안에서 링크가 오른쪽으로 정렬됩니다.

```css
.right {
  text-align: right;
}
```

```html
<div class="right">
  <a href="#">inline 요소</a>
</div>
```

---

# 34. 내 코드 주석 보완

내 코드:

```text
inline요소지만 공간이 가득차있기 때문에 그 공간에서만 움직임
```

이 주석은 `.right`가 `div`에 적용된 상황과 인라인 요소의 정렬 원리를 섞어 설명합니다.

정확한 표현:

```text
text-align은 블록 컨테이너 내부의 인라인 콘텐츠를 정렬한다.
인라인 요소 자체에 지정하면 자신의 좁은 콘텐츠 영역 안에서만
내부 텍스트를 정렬하므로 이동 효과가 보이지 않을 수 있다.
```

---

# 35. `text-decoration`

원본:

```css
.lt {
  text-decoration: line-through;
}

.ul {
  text-decoration: underline;
}

.none {
  text-decoration: none;
}
```

대표 값:

| 값 | 설명 |
| --- | --- |
| `underline` | 밑줄 |
| `line-through` | 취소선 |
| `overline` | 윗줄 |
| `none` | 장식 없음 |

```css
.deleted-price {
  text-decoration: line-through;
}
```

```css
.link {
  text-decoration: underline;
}
```

---

# 36. 의미 요소와 장식

삭제된 내용:

```html
<del>50,000원</del>
```

시각적 취소선만 필요한 경우:

```css
.line-through {
  text-decoration: line-through;
}
```

`del`은 삭제된 콘텐츠라는 의미를 제공합니다.

단순 디자인 효과와 문서 의미를 구분합니다.

밑줄도 마찬가지입니다.

```html
<ins>추가된 내용</ins>
```

```css
.emphasis-line {
  text-decoration: underline;
}
```

---

# 37. 링크 밑줄 제거

원본:

```css
.none {
  text-decoration: none;
}
```

링크 기본 밑줄을 제거합니다.

```html
<a href="#" class="none">a 태그</a>
```

주의:

밑줄을 제거하면 링크가 일반 텍스트와 구분되지 않을 수 있습니다.

대안:

```css
.link {
  color: #2563eb;
  text-decoration-thickness: 0.08em;
  text-underline-offset: 0.15em;
}
```

호버와 포커스:

```css
.link:hover,
.link:focus-visible {
  text-decoration-thickness: 0.14em;
}
```

---

# 38. `:link`와 `:visited`

원본:

```css
.none:link {
  color: aqua;
}

.none:visited {
  color: aqua;
}
```

두 상태를 같은 색으로 지정해 방문 여부가 시각적으로 구분되지 않습니다.

실습 목적은 두 가상 클래스 확인으로 볼 수 있습니다.

대표 상태:

```css
a:link {
  color: #2563eb;
}

a:visited {
  color: #7c3aed;
}

a:hover {
  text-decoration-thickness: 0.14em;
}

a:focus-visible {
  outline: 3px solid #2563eb;
}

a:active {
  color: #dc2626;
}
```

방문 정보는 개인정보 보호를 위해 브라우저가 적용 가능한 CSS 속성을 제한합니다.

---

# 39. 한 줄 말줄임표

원본:

```css
.nowrap {
  border: 1px solid red;
  width: 200px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
```

원본 내 코드 주석:

```text
3개가 조합으로 많이 쓰임, 가린 뒤 ... 표시를 하기 위해
```

정확한 핵심 조합입니다.

필수 조건:

```css
white-space: nowrap;
overflow: hidden;
text-overflow: ellipsis;
```

그리고 너비 제한이 있어야 넘침이 발생합니다.

```css
width: 200px;
```

---

# 40. `white-space: nowrap`

텍스트의 자동 줄바꿈을 막습니다.

```css
.nowrap {
  white-space: nowrap;
}
```

결과:

- 텍스트를 한 줄로 유지
- 요소 너비보다 길면 가로로 넘침
- `overflow` 처리에 따라 스크롤 또는 잘림 발생

내 코드 주석:

```text
모든 content를 한 줄로 포기하고 싶을 때 쓰는 선언
```

`포기`는 오타성 표현으로 보입니다.

정확한 표현:

```text
모든 텍스트를 한 줄로 표시하고 싶을 때 사용한다.
```

---

# 41. `overflow: hidden`

```css
.nowrap {
  overflow: hidden;
}
```

요소 경계를 넘은 콘텐츠를 숨깁니다.

말줄임표 조합에서는 넘친 텍스트를 가리는 역할을 합니다.

주의:

- 실제 텍스트 데이터가 삭제되는 것은 아니다.
- 복사, 접근성 탐색, `title` 등에서 전체 텍스트를 제공할 수 있다.
- 포커스 테두리나 자식 요소도 잘릴 수 있다.

---

# 42. `text-overflow: ellipsis`

```css
.nowrap {
  text-overflow: ellipsis;
}
```

넘친 텍스트 끝에 말줄임표를 표시합니다.

`text-overflow`만 단독으로 작성해서는 동작하지 않을 수 있습니다.

```css
/* 불충분 */
.nowrap {
  text-overflow: ellipsis;
}
```

너비 제한과 줄바꿈·넘침 설정을 함께 확인합니다.

---

# 43. `title` 속성 원본

원본 `.nowrap`에는 전체 문자열이 `title`에 반복되어 있습니다.

```html
<div
  class="nowrap"
  title="Lorem ipsum dolor sit amet..."
>
  Lorem ipsum dolor sit amet...
</div>
```

마우스를 올리면 일부 환경에서 툴팁이 표시됩니다.

주의:

- 키보드와 터치 사용자에게 일관되게 제공되지 않을 수 있다.
- 긴 텍스트 설명의 주된 접근성 수단으로 의존하지 않는다.
- 필요하면 펼치기 버튼, 상세 영역, 접근 가능한 툴팁을 사용한다.

---

# 44. 여러 줄 말줄임표 확장 학습

```css
.multiline-ellipsis {
  display: -webkit-box;
  overflow: hidden;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 3;
}
```

세 줄 이후 내용을 숨깁니다.

주의:

- 전체 콘텐츠 접근 방법을 제공해야 할 수 있다.
- 브라우저 지원과 표준화 상태를 확인한다.
- 줄 높이와 박스 높이를 함께 설계한다.

원본에는 한 줄 말줄임표만 직접 등장합니다.

---

# 45. 긴 단어 줄바꿈

원본은 두 방법을 비교합니다.

```css
.word-wrap {
  word-wrap: break-word;
}

.word-break {
  word-break: break-all;
}
```

실습 텍스트는 공백 없이 매우 긴 영문 문자열입니다.

일반적인 문장 줄바꿈과 다른 결과를 확인하기 위한 예입니다.

---

# 46. `word-wrap`과 `overflow-wrap`

`word-wrap`은 오래된 이름이며 현재 표준 이름은 `overflow-wrap`입니다.

```css
.word-wrap {
  overflow-wrap: break-word;
}
```

기존 코드:

```css
word-wrap: break-word;
```

도 호환을 위해 널리 지원됩니다.

의미:

- 긴 단어나 URL이 컨테이너 밖으로 넘칠 때 줄바꿈 허용
- 가능한 경우 정상적인 단어 경계를 우선 유지
- 레이아웃 넘침 방지에 유용

---

# 47. `word-break: break-all`

```css
.word-break {
  word-break: break-all;
}
```

필요하면 글자 사이 어디에서든 줄을 끊을 수 있습니다.

내 코드 주석:

```text
단점은 단어가 중간에 끊어질 수 있음
```

이 주석은 `word-wrap` 바로 위에 있어 어떤 속성의 단점인지 혼동될 수 있습니다.

`break-all`의 대표 단점으로 설명하는 편이 정확합니다.

영문 단어가 임의의 문자 위치에서 끊어져 가독성이 떨어질 수 있습니다.

---

# 48. `overflow-wrap`과 `word-break` 비교

| 구분 | `overflow-wrap: break-word` | `word-break: break-all` |
| --- | --- | --- |
| 목적 | 긴 문자열의 넘침 방지 | 글자 단위 강제 줄바꿈 |
| 일반 단어 경계 | 가능한 유지 | 유지하지 않을 수 있음 |
| 영문 가독성 | 비교적 좋음 | 낮아질 수 있음 |
| 긴 URL | 유용 | 가능하지만 과도함 |
| 추천 | 일반적인 긴 문자열 처리 | 제한적인 특수 상황 |

실무 기본:

```css
.content {
  overflow-wrap: anywhere;
}
```

또는:

```css
.content {
  overflow-wrap: break-word;
}
```

브라우저 지원과 원하는 줄바꿈 규칙을 확인합니다.

---

# 49. `overflow-wrap: anywhere`

확장 학습:

```css
.text {
  overflow-wrap: anywhere;
}
```

긴 문자열이 넘칠 가능성이 있으면 필요한 위치에서 줄바꿈합니다.

`break-word`와 최소 콘텐츠 크기 계산에서 차이가 있을 수 있습니다.

현대적인 레이아웃에서는 긴 URL과 코드 조각을 처리할 때 유용합니다.

```css
.comment {
  overflow-wrap: anywhere;
}
```

---

# 50. 한국어 줄바꿈과 `word-break`

한글 문장은 영문과 줄바꿈 특성이 다릅니다.

```css
.korean {
  word-break: keep-all;
}
```

`keep-all`은 한글 단어 단위 줄바꿈을 유지하는 데 사용할 수 있습니다.

```css
.heading {
  word-break: keep-all;
}
```

주의:

- 좁은 화면에서 긴 단어가 넘칠 수 있다.
- `overflow-wrap`과 함께 검토한다.

```css
.heading {
  word-break: keep-all;
  overflow-wrap: break-word;
}
```

원본에는 없는 확장 학습입니다.

---

# 51. 실제 `h1`과 가짜 제목

원본:

```html
<h1>h1</h1>
<div class="fake-h1">fake-h1</div>
```

```css
.fake-h1 {
  font-weight: bold;
  font-size: 2em;
}
```

강사님 코드:

```css
.fake-h1 {
  font-size: 2em;
  font-weight: 700;
}
```

화면상 비슷하게 보일 수 있습니다.

하지만 의미는 다릅니다.

---

# 52. 의미와 모양의 차이

```html
<h1>페이지 제목</h1>
```

브라우저와 보조 기술에 문서의 최상위 제목이라는 의미를 전달합니다.

```html
<div class="fake-h1">페이지 제목</div>
```

CSS로 크게 보여도 일반 `div`입니다.

원본 내 코드 주석:

```text
css로도 h1과 같이 만들 수 있지만 html의미를 잘 쓰는것이 더 좋음
```

정확한 핵심입니다.

원칙:

- 제목이면 `h1`~`h6`
- 크기는 CSS로 조정
- 모양 때문에 제목 단계를 선택하지 않음
- 제목 단계를 단순히 크기 순서로 사용하지 않음

---

# 53. 브라우저 기본 `h1`과 가짜 제목 차이

브라우저 기본 스타일에서 `h1`은 일반적으로 다음과 유사합니다.

```css
h1 {
  display: block;
  margin-block: 0.67em;
  font-size: 2em;
  font-weight: bold;
}
```

정확한 값은 브라우저 스타일시트에 따라 다를 수 있습니다.

원본 `.fake-h1`은 `font-size`와 `font-weight`만 지정하므로 다음 차이가 남습니다.

- 기본 마진
- 제목 의미
- 문서 개요
- 스크린 리더 탐색
- 검색 엔진 문맥
- 기본 표시 규칙

---

# 54. 반복 `<br>` 문제

내 코드 마지막에는 약 20개의 `<br>`가 있습니다.

강사님 코드에는 약 50개의 `<br>`가 있습니다.

스크롤을 만들거나 하단 여백을 확보하기 위한 실습으로 보입니다.

실제 문서에서는 CSS를 사용합니다.

```css
body {
  min-height: 200vh;
}
```

또는:

```css
.page {
  padding-bottom: 20rem;
}
```

최종 코드에서는 의미 없는 반복 `<br>`를 제거합니다.

---

# 55. 세미콜론 누락

내 코드:

```css
.spacing {
  letter-spacing: 0em
}
```

마지막 선언이므로 브라우저가 처리할 수 있지만 세미콜론을 작성합니다.

```css
.spacing {
  letter-spacing: 0;
}
```

강사님 코드의 `.font`:

```css
.font {
  font-family: "OngleipParkDahyeon", Arial
}
```

마찬가지로 마지막 선언이라 동작할 수 있지만 세미콜론을 추가합니다.

```css
.font {
  font-family: "OngleipParkDahyeon", Arial, sans-serif;
}
```

---

# 56. 내 코드 분석

## 56.1 장점

- 웹폰트를 사용 목적과 함께 설명했다.
- 웹폰트가 컴퓨터에 설치되지 않아도 사용할 수 있음을 기록했다.
- `font-weight`가 폰트 파일 지원 범위에 영향을 받는다고 설명했다.
- 한 줄 수직 가운데 정렬에서 `height`와 `line-height` 관계를 설명했다.
- `letter-spacing`의 양수와 음수 실험값을 보존했다.
- 인라인 요소 정렬의 공간 문제를 설명하려 했다.
- 링크의 방문 전·후 상태를 구분했다.
- 한 줄 말줄임표의 세 속성 조합을 설명했다.
- `word-wrap`과 `word-break` 실습을 분리했다.
- CSS로 제목 모양을 만들어도 HTML 의미를 우선해야 한다고 기록했다.

---

# 57. 내 코드 개선점

## 57.1 잘못된 `p > div`

상속 실습을 정확히 하려면 `div > div` 또는 `p > span`으로 수정합니다.

## 57.2 `font-weight` 범위

일반적인 정적 폰트의 표준 사용은 `100`부터 `900`입니다.

`1000`, `2000`은 일반 폰트에서 기대한 결과가 나오지 않을 수 있음을 명확히 합니다.

## 57.3 `font-style`과 `<em>`

`em`은 단순한 기울임 태그가 아니라 의미상 강조 요소입니다.

## 57.4 `letter-spacing` 기본값

기본값은 `0`이 아니라 `normal`입니다.

## 57.5 `text-align` 주석

정렬 속성은 인라인 요소 자체를 이동시키기보다 블록 컨테이너 내부의 인라인 콘텐츠를 정렬합니다.

## 57.6 “한 줄로 포기” 오타성 표현

```text
한 줄로 표시
```

로 수정합니다.

## 57.7 `word-wrap` 주석 위치

“단어가 중간에 끊어질 수 있음”은 `word-break: break-all`에 더 직접적으로 연결됩니다.

## 57.8 세미콜론

```css
letter-spacing: 0em
```

뒤에 세미콜론을 추가합니다.

## 57.9 링크 접근성

밑줄과 방문 색을 모두 제거하거나 동일하게 만들면 링크 구분이 약해질 수 있습니다.

---

# 58. 강사님 코드 분석

## 58.1 장점

- 원본 수업 흐름이 간결하다.
- 웹폰트, 굵기, 줄 높이, 자간, 정렬, 장식, 넘침을 한 문서에서 비교한다.
- 내 코드보다 첫 링크에 직접 `.right` 클래스를 적용해 인라인 요소에서 `text-align` 효과가 제한적임을 확인할 수 있다.
- `letter-spacing: -0.1em`을 최종 적용하여 음수 자간 결과가 실제로 보인다.
- `font-weight: 700`로 가짜 제목을 명시적으로 구성한다.

---

# 59. 강사님 코드 개선점

## 59.1 `font-weight` 기본값 오류

```text
기본값: 500
```

은 잘못된 설명입니다.

기본값은 `normal`, 일반적으로 `400`입니다.

## 59.2 `1000`, `2000`

일반적인 정적 폰트 범위를 넘어서는 값이며 실제 폰트 지원을 확인해야 합니다.

## 59.3 잘못된 HTML 중첩

내 코드와 동일하게 `p` 안에 `div`가 있습니다.

## 59.4 웹폰트 대체 계열 누락

```css
font-family: "OngleipParkDahyeon", Arial;
```

뒤에 `sans-serif`를 추가하는 것이 좋습니다.

## 59.5 세미콜론 누락

`.font`의 마지막 선언 뒤 세미콜론이 없습니다.

## 59.6 링크 상태

방문 전과 방문 후를 모두 `aqua`로 지정하여 상태 구분이 없습니다.

## 59.7 반복 `<br>`

약 50개의 줄바꿈은 CSS 공간으로 대체합니다.

## 59.8 결과 설명 부족

`word-wrap`과 `word-break`의 실제 차이, 말줄임표의 필수 조건, `line-height` 중앙 정렬 한계는 독립 문서에서 보완해야 합니다.

---

# 60. 내 코드와 강사님 코드 비교

| 비교 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 웹폰트 | `NostalgicPoliceVibe` | `OngleipParkDahyeon` |
| 웹폰트 설명 | 설치 없이 사용 가능 설명 | `웹폰트` 한 줄 |
| 글자 내용 | “글씨를 적어보자” | “글씨를 좀 적습니다” |
| `font-weight` 설명 | 폰트 파일 지원 범위 언급 | 기본값을 `500`으로 잘못 표기 |
| `.spacing` 최종값 | `0em` | `-0.1em` |
| 오른쪽 정렬 첫 링크 | 클래스 없음 | 링크에 `.right` 직접 적용 |
| 가운데 문구 | `middle 줄` | `뭐했다고?` |
| 말줄임표 | 동일한 3속성 조합 | 동일 |
| 가짜 제목 굵기 | `bold` | `700` |
| 반복 `<br>` | 약 20개 | 약 50개 |
| 학습 성격 | 상세 주석형 | 간결한 수업형 |

---

# 61. 원본 통합 개선 예제

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
  <title>CSS 텍스트와 글꼴</title>
  <link
    rel="stylesheet"
    href="asset/css/font.css"
  >
</head>
<body>
  <main class="page">
    <h1 class="page__title">
      CSS 텍스트와 글꼴
    </h1>

    <section class="demo">
      <h2>글자 크기와 상속</h2>

      <div class="size-demo">
        부모 글자
        <span>자식 글자</span>
      </div>
    </section>

    <section class="demo">
      <h2>웹폰트</h2>

      <p class="web-font">
        웹폰트가 적용된 문장입니다.
      </p>
    </section>

    <section class="demo">
      <h2>한 줄 말줄임표</h2>

      <p class="ellipsis">
        매우 긴 제목이 컨테이너 너비를 넘어가면
        말줄임표로 표시됩니다.
      </p>
    </section>

    <section class="demo">
      <h2>긴 문자열 줄바꿈</h2>

      <p class="break-text">
        https://example.com/very-long-path-without-space
      </p>
    </section>
  </main>
</body>
</html>
```

## CSS

```css
@font-face {
  font-family: "ProjectFont";
  src:
    url("../fonts/project-font.woff2")
    format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}

*,
*::before,
*::after {
  box-sizing: border-box;
}

body {
  margin: 0;
  color: #222;
  font-family:
    Arial,
    sans-serif;
  font-size: 1rem;
  line-height: 1.6;
}

.page {
  width: min(100% - 2rem, 48rem);
  margin-inline: auto;
  padding-block: 2rem;
}

.page__title {
  font-size: clamp(2rem, 5vw, 3.5rem);
  letter-spacing: -0.03em;
}

.size-demo {
  font-size: 2rem;
}

.web-font {
  font-family:
    "ProjectFont",
    Arial,
    sans-serif;
}

.ellipsis {
  width: 20rem;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.break-text {
  overflow-wrap: anywhere;
}
```

---

# 62. 실무 본문 타이포그래피

```css
body {
  color: #1f2937;
  font-family:
    "Pretendard",
    "Noto Sans KR",
    Arial,
    sans-serif;
  font-size: 1rem;
  line-height: 1.7;
}
```

본문 폭:

```css
.article {
  max-width: 65ch;
}
```

문단 간격:

```css
.article p {
  margin-block: 0 1em;
}
```

읽기 쉬운 타이포그래피는 글자 크기 하나가 아니라 줄 높이, 줄 길이, 대비를 함께 설계합니다.

---

# 63. 제목 체계

```css
h1,
h2,
h3 {
  line-height: 1.25;
  text-wrap: balance;
}

h1 {
  font-size: clamp(2rem, 5vw, 4rem);
  letter-spacing: -0.04em;
}

h2 {
  font-size: 2rem;
  letter-spacing: -0.03em;
}

h3 {
  font-size: 1.5rem;
}
```

제목은 본문보다 줄 높이를 좁게 사용할 수 있습니다.

의미상 제목 단계는 HTML 구조를 기준으로 정하고 크기는 CSS로 조절합니다.

---

# 64. 링크 스타일

```css
a {
  color: #1d4ed8;
  text-decoration-line: underline;
  text-decoration-thickness: 0.08em;
  text-underline-offset: 0.18em;
}

a:visited {
  color: #6d28d9;
}

a:hover {
  text-decoration-thickness: 0.14em;
}

a:focus-visible {
  outline: 3px solid #2563eb;
  outline-offset: 3px;
}
```

링크를 색상만으로 구분하지 않도록 밑줄을 유지하는 것이 안전합니다.

---

# 65. 버튼 텍스트

```css
.button {
  font: inherit;
  font-weight: 700;
  line-height: 1.2;
}
```

폼 컨트롤은 브라우저 기본 글꼴을 사용할 수 있으므로 다음 초기화가 유용합니다.

```css
button,
input,
textarea,
select {
  font: inherit;
}
```

버튼 수직 정렬은 고정 `line-height`보다 Flexbox와 패딩을 사용합니다.

```css
.button {
  display: inline-flex;
  min-height: 44px;
  padding: 0.75rem 1rem;
  align-items: center;
  justify-content: center;
}
```

---

# 66. 긴 URL과 코드 문자열

```css
.content {
  overflow-wrap: anywhere;
}
```

코드 블록:

```css
pre {
  overflow-x: auto;
}
```

일반 본문에서 코드를 강제로 문자 단위로 모두 끊으면 읽기 어려울 수 있습니다.

상황별 선택:

- 일반 긴 URL: `overflow-wrap: anywhere`
- 코드 블록: 가로 스크롤
- 제목: `word-break: keep-all`
- 특수 테이블 셀: 제한적인 `break-all`

---

# 67. 개발자 도구로 글꼴 확인

브라우저 개발자 도구에서 확인할 항목:

- 계산된 `font-family`
- 실제 렌더링된 폰트
- `font-size`
- `font-weight`
- `line-height`
- 상속 출처
- 취소선 처리된 폰트 선언
- 웹폰트 네트워크 요청 성공 여부

웹폰트가 로드되지 않으면 대체 글꼴이 적용됩니다.

Network 탭에서 WOFF2 요청 상태를 확인합니다.

---

# 68. 웹폰트가 적용되지 않을 때 점검

1. `@font-face`의 이름과 사용 이름이 같은가?
2. URL 경로가 맞는가?
3. Network 요청이 성공했는가?
4. 외부 CDN이 차단됐는가?
5. 파일 형식과 `format()`이 맞는가?
6. `font-weight`와 `font-style`이 요청값과 일치하는가?
7. 더 높은 우선순위의 `font-family`가 덮었는가?
8. 잘못된 HTML 중첩 때문에 상속 대상이 달라졌는가?
9. CORS 오류가 있는가?
10. 실제 렌더링 폰트를 개발자 도구에서 확인했는가?

---

# 69. 말줄임표가 안 될 때 점검

1. 너비 또는 최대 너비가 제한됐는가?
2. `white-space: nowrap`이 있는가?
3. `overflow: hidden`이 있는가?
4. `text-overflow: ellipsis`가 있는가?
5. 요소가 인라인이라 너비가 적용되지 않는가?
6. `display: block` 또는 `inline-block`이 필요한가?
7. Flex 자식이라 `min-width: 0`이 필요한가?
8. 부모가 충분히 넓어 넘침이 발생하지 않는가?
9. 다중 줄 말줄임표를 한 줄 방식으로 구현하려는가?
10. 다른 규칙이 `white-space`를 덮었는가?

Flex 항목 예:

```css
.card__title {
  min-width: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
```

---

# 70. 자주 하는 실수

## 70.1 `p` 안에 `div`를 넣음

브라우저가 DOM을 자동 보정하여 상속 실험이 달라질 수 있습니다.

## 70.2 웹폰트 이름 불일치

`@font-face` 이름과 `font-family` 사용 이름이 같아야 합니다.

## 70.3 대체 글꼴 미지정

웹폰트 로드 실패 시 읽기 어려운 기본값이 사용될 수 있습니다.

## 70.4 `font-weight` 기본값을 500으로 이해

기본값은 `normal`, 일반적으로 400입니다.

## 70.5 폰트가 제공하지 않는 굵기 기대

가장 가까운 굵기 또는 합성 굵기가 표시될 수 있습니다.

## 70.6 `line-height`로 여러 줄 수직 중앙 정렬

한 줄을 넘어가면 레이아웃이 깨질 수 있습니다.

## 70.7 `text-align`을 인라인 요소 이동 속성으로 이해

부모 컨테이너 안의 인라인 콘텐츠를 정렬합니다.

## 70.8 링크 밑줄을 없애고 대체 구분 없음

링크가 일반 텍스트와 구분되지 않을 수 있습니다.

## 70.9 `text-overflow`만 작성

`white-space`, `overflow`, 너비 제한이 함께 필요합니다.

## 70.10 `word-break: break-all` 남용

영문 단어가 임의 위치에서 끊어져 가독성이 떨어집니다.

---


# 종합실습

## 문제 1. 글자 크기

`.title`의 글자 크기를 `32px`로 지정하세요.

## 문제 2. 올바른 상속 구조

다음 잘못된 HTML을 수정하세요.

```html
<p class="size">
  부모
  <div>자식</div>
</p>
```

블록 자식을 유지해야 합니다.

## 문제 3. 웹폰트 등록

`asset/fonts/project.woff2` 파일을 `ProjectFont`라는 이름으로 등록하세요.

조건:

- 굵기 400
- 스타일 normal
- `font-display: swap`

## 문제 4. 대체 글꼴

`.content`에 `ProjectFont`, `Arial`, 일반 sans-serif 순서로 적용하세요.

## 문제 5. 굵기

다음을 숫자값으로 작성하세요.

1. 일반 굵기
2. 굵은 굵기

## 문제 6. 원본 오류

강사님 코드의 다음 주석을 수정하세요.

```css
/* 기본값: 500 */
```

## 문제 7. 부분 지원

폰트 파일이 400과 700만 제공하는데 `font-weight: 500`을 지정했습니다. 어떤 점을 주의해야 하는지 설명하세요.

## 문제 8. 이탤릭과 의미

의미상 강조 문장을 HTML로 작성하고, 단순 장식 기울임 클래스를 CSS로 작성하세요.

## 문제 9. 줄 높이

본문의 줄 높이를 글자 크기의 1.7배로 지정하세요.

## 문제 10. 한 줄 가운데 정렬

높이 `100px`, 너비 `300px`인 한 줄 텍스트 박스를 `line-height` 방식으로 가로·세로 가운데 정렬하세요.

## 문제 11. 다중 줄 개선

문제 10을 여러 줄에도 안전한 Flexbox 방식으로 개선하세요.

## 문제 12. 자간

제목 자간을 `-0.03em`으로 지정하세요.

## 문제 13. 오른쪽 정렬

블록 부모 내부의 링크를 오른쪽에 배치하세요.

## 문제 14. 링크 접근성

링크 밑줄을 유지하면서 밑줄과 글자 사이 간격을 `0.2em`으로 지정하세요.

## 문제 15. 방문 링크

방문하지 않은 링크는 파랑, 방문한 링크는 보라색으로 지정하세요.

## 문제 16. 한 줄 말줄임표

너비 `240px`인 제목에 한 줄 말줄임표를 적용하세요.

## 문제 17. Flex 말줄임표

Flex 항목 내부 제목의 말줄임표가 동작하도록 필요한 추가 속성을 포함해 작성하세요.

## 문제 18. 긴 URL

긴 URL이 컨테이너를 넘지 않도록 일반적인 줄바꿈 속성을 작성하세요.

## 문제 19. 단어 강제 분리

문자 사이 어디에서나 줄바꿈하도록 작성하고, 단점을 한 줄로 설명하세요.

## 문제 20. 한글 제목 줄바꿈

한글 제목이 단어 중간에서 쉽게 끊기지 않도록 하되 긴 문자열은 넘치지 않게 작성하세요.

## 문제 21. 실제 제목

다음 코드를 의미 있는 제목 구조로 개선하세요.

```html
<div class="fake-h1">Developer Wiki</div>
```

## 문제 22. 종합 타이포그래피

다음 요구사항을 만족하는 기사 본문 스타일을 작성하세요.

- 시스템 대체 글꼴 포함
- 본문 `1rem`
- 줄 높이 `1.7`
- 최대 줄 길이 `65ch`
- 제목 반응형 크기
- 제목 음수 자간
- 링크 밑줄 유지
- 긴 URL 줄바꿈
- 한 줄 카드 제목 말줄임표
- 폼 요소가 본문 글꼴 상속

---

# 정답과 해설

## 정답 1

```css
.title {
  font-size: 32px;
}
```

## 정답 2

```html
<div class="size">
  부모
  <div>자식</div>
</div>
```

블록 자식을 포함하므로 부모도 블록 컨테이너를 사용합니다.

## 정답 3

```css
@font-face {
  font-family: "ProjectFont";
  src:
    url("../fonts/project.woff2")
    format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

CSS 파일이 `asset/css`에 있다는 전제입니다.

## 정답 4

```css
.content {
  font-family:
    "ProjectFont",
    Arial,
    sans-serif;
}
```

## 정답 5

```css
.normal {
  font-weight: 400;
}

.bold {
  font-weight: 700;
}
```

## 정답 6

```css
/* 기본값은 normal이며 일반적으로 400에 해당한다. */
```

## 정답 7

브라우저가 실제로 제공되는 400 또는 700 중 가까운 굵기를 선택하거나 합성할 수 있습니다. CSS 숫자만 지정한다고 폰트에 없는 실제 500 굵기가 자동 생성되는 것은 아닙니다.

## 정답 8

### 의미상 강조

```html
<p>
  제출 전에는 <em>반드시 검토</em>하세요.
</p>
```

### 장식 기울임

```css
.decorative-italic {
  font-style: italic;
}
```

## 정답 9

```css
body {
  line-height: 1.7;
}
```

단위 없는 값입니다.

## 정답 10

```css
.middle {
  width: 300px;
  height: 100px;
  line-height: 100px;
  text-align: center;
}
```

한 줄 텍스트에만 안전합니다.

## 정답 11

```css
.middle {
  display: flex;
  width: 300px;
  min-height: 100px;
  align-items: center;
  justify-content: center;
  text-align: center;
}
```

## 정답 12

```css
.title {
  letter-spacing: -0.03em;
}
```

## 정답 13

```html
<div class="link-wrapper">
  <a href="#">링크</a>
</div>
```

```css
.link-wrapper {
  text-align: right;
}
```

## 정답 14

```css
a {
  text-decoration-line: underline;
  text-underline-offset: 0.2em;
}
```

## 정답 15

```css
a:link {
  color: #2563eb;
}

a:visited {
  color: #7c3aed;
}
```

## 정답 16

```css
.card-title {
  width: 240px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
```

## 정답 17

```css
.card__content {
  min-width: 0;
}

.card__title {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
```

Flex 항목은 기본 최소 콘텐츠 크기 때문에 줄어들지 않을 수 있어 `min-width: 0`이 필요할 수 있습니다.

## 정답 18

```css
.content {
  overflow-wrap: anywhere;
}
```

## 정답 19

```css
.text {
  word-break: break-all;
}
```

영문 단어가 문자 중간에서 끊겨 가독성이 떨어질 수 있습니다.

## 정답 20

```css
.heading {
  word-break: keep-all;
  overflow-wrap: break-word;
}
```

## 정답 21

```html
<h1>Developer Wiki</h1>
```

크기는 CSS로 조절합니다.

```css
h1 {
  font-size: 2rem;
}
```

## 정답 22

```css
body {
  margin: 0;
  color: #1f2937;
  font-family:
    "Pretendard",
    "Noto Sans KR",
    Arial,
    sans-serif;
  font-size: 1rem;
  line-height: 1.7;
}

article {
  max-width: 65ch;
}

article h1 {
  font-size: clamp(2rem, 5vw, 4rem);
  line-height: 1.2;
  letter-spacing: -0.04em;
}

article a {
  color: #1d4ed8;
  text-decoration-line: underline;
  text-underline-offset: 0.18em;
}

article p,
article li {
  overflow-wrap: anywhere;
}

.card-title {
  min-width: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

button,
input,
textarea,
select {
  font: inherit;
}
```

---

# 최종 체크리스트

## HTML 구조

- [ ] `p` 안에 `div`를 넣지 않았다.
- [ ] 블록 자식은 올바른 블록 부모 안에 배치했다.
- [ ] 실제 제목은 `h1`~`h6`를 사용했다.
- [ ] 의미상 강조는 `<em>`을 사용했다.
- [ ] 삭제·추가 의미가 있으면 `<del>`, `<ins>`를 검토했다.

## 웹폰트

- [ ] `@font-face` 이름과 사용 이름이 일치한다.
- [ ] WOFF2 경로가 올바르다.
- [ ] `font-weight`와 `font-style`을 등록했다.
- [ ] `font-display` 정책을 확인했다.
- [ ] 시스템 대체 글꼴을 지정했다.
- [ ] 외부 CDN 의존성을 검토했다.
- [ ] 실제 제공되는 굵기 파일을 확인했다.

## 글자 크기와 굵기

- [ ] 본문 글자 크기가 너무 작지 않다.
- [ ] `font-weight` 기본값을 500으로 오해하지 않았다.
- [ ] 일반 정적 폰트에서 100~900 범위를 우선 사용했다.
- [ ] 폰트에 없는 굵기를 무리하게 요청하지 않았다.
- [ ] 제목 크기와 HTML 제목 단계를 분리해서 판단했다.

## 줄 높이와 자간

- [ ] 본문에 단위 없는 `line-height`를 검토했다.
- [ ] 한 줄 중앙 정렬 핵을 다중 줄에 사용하지 않았다.
- [ ] 지나치게 큰 양수·음수 자간을 피했다.
- [ ] 강사님 코드의 `-0.1em` 결과를 실제로 확인했다.
- [ ] 내 코드의 `0em` 세미콜론을 보완했다.

## 정렬과 장식

- [ ] `text-align`을 부모 블록에 적용했다.
- [ ] 인라인 요소 자체에 정렬할 공간이 있는지 확인했다.
- [ ] 링크 밑줄 제거 시 대체 구분을 제공했다.
- [ ] `:link`, `:visited`, `:hover`, `:focus-visible` 상태를 검토했다.
- [ ] 방문 링크 상태를 개인정보 보호 범위 안에서 사용했다.

## 넘침과 줄바꿈

- [ ] 한 줄 말줄임표에 너비 제한이 있다.
- [ ] `white-space`, `overflow`, `text-overflow`를 모두 확인했다.
- [ ] Flex 항목에 `min-width: 0`이 필요한지 확인했다.
- [ ] `word-wrap`의 표준 이름 `overflow-wrap`을 이해했다.
- [ ] `word-break: break-all`을 남용하지 않았다.
- [ ] 한글 제목에는 `keep-all`이 적절한지 확인했다.
- [ ] 전체 텍스트 접근 방법을 제공했다.

## 원본 코드 검수

- [ ] `lang="en"`을 `lang="ko"`로 개선했다.
- [ ] `Document` 제목을 학습 주제로 변경했다.
- [ ] 내 코드와 강사님 코드의 웹폰트 차이를 오류로 처리하지 않았다.
- [ ] 강사님 주석의 `기본값: 500` 오류를 수정했다.
- [ ] `1000`, `2000` 굵기의 한계를 설명했다.
- [ ] “한 줄로 포기” 표현을 수정했다.
- [ ] `word-break` 단점 설명 위치를 명확히 했다.
- [ ] 반복 `<br>`를 CSS 공간으로 대체했다.

---

# 핵심 요약

- CSS 타이포그래피는 글꼴, 크기, 굵기, 줄 높이, 자간, 정렬, 장식, 줄바꿈을 함께 다룬다.
- 원본의 `p` 안에 `div`를 넣은 구조는 유효하지 않으며 브라우저가 DOM을 자동 보정할 수 있다.
- 상속 실습은 `div > div` 또는 `p > span`처럼 올바른 구조로 작성해야 한다.
- `font-size`와 `font-family`는 자식에게 상속된다.
- `@font-face`는 외부 폰트 파일을 CSS 글꼴 이름으로 등록한다.
- `font-display: swap`은 대체 글꼴로 먼저 표시한 뒤 웹폰트로 교체한다.
- 웹폰트에는 반드시 적절한 대체 글꼴 체계를 제공하는 것이 좋다.
- 내 코드와 강사님 코드는 서로 다른 웹폰트를 사용하며 이는 오류가 아니다.
- `font-style`은 시각적 표현이고 `<em>`은 의미상 강조다.
- `font-weight` 기본값은 `normal`, 일반적으로 400이다.
- 강사님 코드의 “기본값 500” 주석은 잘못된 설명이다.
- 일반적인 정적 폰트는 주로 100부터 900까지의 굵기를 사용한다.
- `1000`, `2000`은 실제 폰트 지원 여부에 따라 기대한 결과가 나오지 않을 수 있다.
- CSS에서 요청한 굵기를 폰트 파일이 제공하지 않으면 가장 가까운 굵기나 합성 굵기가 사용될 수 있다.
- 본문 `line-height`에는 단위 없는 값을 많이 사용한다.
- `height`와 같은 `line-height`는 한 줄 텍스트 중앙 정렬에만 제한적으로 사용한다.
- 여러 줄 수직 정렬은 Flexbox가 더 안전하다.
- `letter-spacing`의 기본값은 `normal`이며 내 코드의 0과 강사님 코드의 `-0.1em`은 실제 결과가 다르다.
- `text-align`은 블록 컨테이너 내부의 인라인 콘텐츠를 정렬한다.
- 인라인 링크 자체에 `text-align`을 지정해도 정렬할 남는 공간이 없어 이동 효과가 없을 수 있다.
- 링크 밑줄을 제거할 때는 링크를 구분할 다른 시각적 단서를 제공해야 한다.
- 한 줄 말줄임표에는 너비 제한, `white-space: nowrap`, `overflow: hidden`, `text-overflow: ellipsis`가 필요하다.
- `word-wrap`의 표준 이름은 `overflow-wrap`이다.
- `word-break: break-all`은 단어 중간을 끊어 영문 가독성을 떨어뜨릴 수 있다.
- CSS로 `div`를 크게 만들어도 의미상 제목이 되지 않으므로 실제 제목은 `h1`~`h6`를 사용한다.
- 반복 `<br>`는 스크롤 테스트용일 수 있지만 최종 문서에서는 CSS 여백이나 높이로 대체한다.
# V3 렌더링 추적 카드 — 글꼴 선택과 텍스트 줄 배치

브라우저는 font-family 목록에서 사용할 수 있는 첫 글꼴을 고르고 글자 크기·굵기·line-height를 계산해 줄 상자를 만든다. 웹 폰트 로딩 전후 모양이 달라질 수 있다.

`line-height`는 글자 자체 높이와 같지 않다. Computed Fonts와 계산된 font-size/line-height를 확인하고, 긴 문장·한글·영문·숫자로 줄바꿈을 시험한다.

**원본 연결:** 내 코드와 강사님 코드의 `workspace_html/css/07_font.html 및 asset/css/07_font.css`에서 실제 선택자·계산값·화면 차이를 확인한다.
