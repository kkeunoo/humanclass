---
title: CSS 배경 이미지와 배경 속성
version: v3.0-encyclopedia
last_updated: 2026-08-06
status: Completed
---

# CSS 배경 이미지와 배경 속성

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `06_CSS_배경이미지와_배경속성.md` |
| 분류 | `02_CSS` |
| 원본 기준 | `workspace_html/css/06_background.html`, `workspace_html/css/asset/css/06_background.css`, `workspace_teacher/workspace_html/css/06_background.html`, `workspace_teacher/workspace_html/css/asset/css/06_background.css` |
| 핵심 범위 | `background-image`, `background-repeat`, `background-size`, `background-position`, `background-attachment`, `background` 단축 속성 |
| 프로젝트 연결 | Hero 영역, 카드 배경, 프로필 이미지, 배경 오버레이, 패턴 이미지, 고정 배경 효과 |

> 이 문서는 내 코드와 강사님 코드의 `06_background.html`, `06_background.css`를 비교해 배경색·배경 이미지·반복·크기·위치·고정·단축 속성의 실제 동작을 정리한다. 원본의 외부 이미지 의존과 `cover`·`contain` 설명을 보완하고, Hero·Card·Overlay·Gradient를 실무 패턴으로 연결한다.

---

# 학습 목표

- CSS 배경이 요소의 콘텐츠가 아니라 장식 영역이라는 점을 설명한다.
- `background-image`로 이미지를 지정한다.
- `background-repeat`의 기본값과 주요 값을 구분한다.
- `background-size`의 고정값, 퍼센트, `cover`, `contain` 차이를 설명한다.
- `background-position`으로 이미지 위치를 조절한다.
- `background-attachment: fixed`와 `scroll`의 차이를 이해한다.
- `background` 단축 속성의 구성과 주의점을 설명한다.
- 배경 이미지와 실제 `<img>` 요소의 사용 목적을 구분한다.
- 원형 프로필 이미지에 배경 이미지를 사용할 때 발생하는 문제를 설명한다.
- 외부 이미지 URL 의존성과 성능 문제를 파악한다.
- 배경 이미지 위 텍스트의 대비를 개선한다.
- 내 코드와 강사님 코드의 차이와 주석 보완점을 찾는다.
- 모바일 환경에서 `background-attachment: fixed`의 한계를 이해한다.
- 여러 배경과 그라디언트를 조합한 실무 패턴을 작성한다.

---

# 1. CSS 배경이란?

CSS 배경은 요소의 뒤쪽에 색상이나 이미지를 그리는 기능입니다.

```css
.hero {
  background-color: #111;
  background-image: url("hero.webp");
}
```

배경은 일반적으로 다음 영역에 그려집니다.

```text
border 영역 안쪽
├─ padding
└─ content
```

정확한 그려지는 범위는 `background-clip`으로 바꿀 수 있습니다.

배경의 핵심 특징:

- HTML 콘텐츠 자체가 아니다.
- 장식 목적에 적합하다.
- 요소 크기가 있어야 보인다.
- 배경 이미지가 로드되지 않아도 대체 텍스트가 제공되지 않는다.
- 여러 개의 배경 이미지를 겹쳐 사용할 수 있다.

---

# 2. 원본 실습 구조

원본 HTML에는 네 개의 주요 실습 영역이 있습니다.

```html
<p id="back1">
  배경 이미지<br>
  배경 이미지<br>
  배경 이미지<br>
</p>
```

```html
<div id="back2">
  <p>
    글씨<br>
    두 줄 정도
  </p>
</div>
```

```html
<div class="profile"></div>
```

```html
<div id="back3">
  아무 글씨<br>
  아무 글자
</div>
```

각 영역의 목적:

| 영역 | 학습 내용 |
| --- | --- |
| `#back1` | 반복, 크기 조절 |
| `#back2` | `cover`, `fixed`, 내부 스크롤 |
| `.profile` | 위치 조절, 원형 배경 이미지 |
| `#back3` | `background` 단축 속성 |

---

# 3. `background-color`

원본 `#back3`의 단축 속성에는 배경색이 포함되어 있습니다.

```css
background: #abcdef url("image.webp") no-repeat center;
```

여기서 `#abcdef`는 배경색입니다.

개별 속성으로 작성하면:

```css
#back3 {
  background-color: #abcdef;
}
```

배경 이미지가 로드되지 않거나 이미지에 투명한 영역이 있으면 배경색이 보일 수 있습니다.

실무에서는 이미지와 대비되는 기본 배경색을 함께 지정하는 것이 좋습니다.

```css
.hero {
  background-color: #1f2937;
  background-image: url("hero.webp");
}
```

---

# 4. `background-image`

배경 이미지는 `url()`로 지정합니다.

```css
#back1 {
  background-image: url("image.webp");
}
```

상대 경로:

```css
.card {
  background-image: url("../images/card-bg.webp");
}
```

CSS 파일 기준으로 경로를 계산합니다.

```text
asset/
├── css/
│   └── style.css
└── images/
    └── card-bg.webp
```

```css
background-image: url("../images/card-bg.webp");
```

HTML 파일 기준이 아니라 **CSS 파일 위치 기준**이라는 점이 중요합니다.

---

# 5. 외부 URL 사용 시 주의

원본은 긴 외부 이미지 주소를 직접 사용합니다.

```css
background-image: url("https://i.namu.wiki/...");
```

학습 실습에는 사용할 수 있지만 실제 프로젝트에서는 다음 문제가 있습니다.

- 외부 서버 정책에 따라 차단될 수 있다.
- 주소가 변경되거나 삭제될 수 있다.
- 로딩 속도를 제어하기 어렵다.
- CORS와 핫링크 정책 영향을 받을 수 있다.
- 이미지 최적화와 캐시 정책을 관리하기 어렵다.

프로젝트 자산으로 관리하는 방식:

```css
background-image: url("../images/background.webp");
```

---

# 6. 배경 이미지가 보이려면 크기가 필요하다

빈 `div`에 배경 이미지를 지정해도 높이가 없으면 보이지 않을 수 있습니다.

```html
<div class="profile"></div>
```

```css
.profile {
  width: 100px;
  height: 100px;
  background-image: url("profile.webp");
}
```

원본 `.profile`은 너비와 높이를 직접 지정했기 때문에 배경이 표시됩니다.

다른 방법:

```css
.profile {
  width: 100px;
  aspect-ratio: 1;
}
```

---

# 7. `background-repeat`

배경 이미지가 요소보다 작으면 기본적으로 반복됩니다.

기본값:

```css
background-repeat: repeat;
```

원본 주석:

```text
repeat 기본값은 x,y축 반복
```

정확한 설명:

```text
repeat는 가로와 세로 방향 모두 이미지를 반복한다.
```

주요 값:

| 값 | 설명 |
| --- | --- |
| `repeat` | 가로·세로 반복 |
| `repeat-x` | 가로 반복 |
| `repeat-y` | 세로 반복 |
| `no-repeat` | 반복하지 않음 |
| `space` | 잘리지 않게 간격을 나누어 반복 |
| `round` | 이미지 크기를 조정해 반복 영역에 맞춤 |

---

# 8. 원본의 `background-repeat`

내 코드:

```css
background-repeat:
/*repeat-x*/
/*repeat-y*/
no-repeat;
```

강사님 코드:

```css
background-repeat: /*repeat-x*/ /*repeat-y*/ no-repeat;
```

실제 적용값은 모두 다음입니다.

```css
background-repeat: no-repeat;
```

주석 처리된 값은 번갈아 실험하기 위한 메모입니다.

가독성을 위해 다음처럼 한 줄씩 실험하는 편이 좋습니다.

```css
/* background-repeat: repeat-x; */
/* background-repeat: repeat-y; */
background-repeat: no-repeat;
```

---

# 9. 반복 패턴에 적합한 이미지

작은 점, 격자, 노이즈 패턴은 반복 배경에 적합합니다.

```css
.pattern {
  background-image: url("../images/dot-pattern.png");
  background-repeat: repeat;
}
```

원본 강사님 코드에는 다음 예제가 주석으로 남아 있습니다.

```css
/* background-image: url('http://poiemaweb.com/img/bg/dot.png'); */
```

이 주소는 `http`이고 외부 사이트에 의존하므로 실제 프로젝트에서는 로컬 이미지 또는 `https` 자산으로 대체하는 것이 좋습니다.

---

# 10. `background-size`

배경 이미지의 크기를 지정합니다.

원본에는 다음 실험값이 있습니다.

```css
/* background-size: 100px 200px; */
/* background-size: 100% 50%; */
/* background-size: 100% 100%; */
/* background-size: cover; */
background-size: contain;
```

값 하나:

```css
background-size: 100px;
```

가로 크기를 지정하고 세로는 비율에 따라 자동 계산됩니다.

값 두 개:

```css
background-size: 100px 200px;
```

```text
가로 100px
세로 200px
```

원본 비율이 달라지면 이미지가 왜곡될 수 있습니다.

---

# 11. 고정 크기 `background-size`

```css
.box {
  background-size: 100px 200px;
}
```

장점:

- 정확한 크기 제어
- 패턴이나 아이콘 배경에 사용 가능

주의:

- 원본 비율이 깨질 수 있다.
- 반응형 화면에 고정값이 맞지 않을 수 있다.
- 고해상도 화면에서 흐리게 보일 수 있다.

비율 유지가 중요하면 한쪽만 지정할 수 있습니다.

```css
background-size: 100px auto;
```

---

# 12. 퍼센트 `background-size`

```css
background-size: 100% 50%;
```

배경 위치 영역을 기준으로 크기가 계산됩니다.

```text
가로: 요소 배경 영역의 100%
세로: 요소 배경 영역의 50%
```

```css
background-size: 100% 100%;
```

요소 전체를 정확히 채우지만 원본 이미지 비율이 다르면 늘어나거나 찌그러질 수 있습니다.

원본 주석에 이 왜곡 가능성은 직접 적혀 있지 않으므로 복습 문서에서 보완해야 합니다.

---

# 13. `background-size: cover`

```css
background-size: cover;
```

원본 내 코드 주석:

```text
cover는 원본의 비율을 해치지 않고 전체를 덮어주는 것
```

좋은 핵심 설명입니다.

정확히는:

- 이미지 비율을 유지한다.
- 요소의 배경 영역을 빈 공간 없이 완전히 덮는다.
- 이미지 일부가 요소 밖으로 잘릴 수 있다.

예:

```text
요소가 가로로 넓고 이미지가 세로로 길다면
위·아래 또는 좌·우 일부가 잘릴 수 있다.
```

Hero 배경에 자주 사용합니다.

```css
.hero {
  background-size: cover;
  background-position: center;
}
```

---

# 14. `background-size: contain`

```css
background-size: contain;
```

원본 내 코드 주석:

```text
꽉 차지 않더라도 사진을 다 보여주고 싶다면 contain
```

정확한 설명입니다.

특징:

- 이미지 비율을 유지한다.
- 이미지 전체가 배경 영역 안에 들어오도록 축소 또는 확대한다.
- 남는 공간이 생길 수 있다.
- `no-repeat`을 함께 사용하지 않으면 남는 영역에서 반복될 수 있다.

권장 조합:

```css
.logo {
  background-repeat: no-repeat;
  background-position: center;
  background-size: contain;
}
```

---

# 15. `cover`와 `contain` 비교

| 구분 | `cover` | `contain` |
| --- | --- | --- |
| 비율 유지 | 예 | 예 |
| 영역 완전히 덮음 | 예 | 아니요 |
| 이미지 전체 표시 | 보장 안 됨 | 예 |
| 잘림 | 발생 가능 | 없음 |
| 빈 공간 | 없음 | 발생 가능 |
| 대표 용도 | Hero, 카드 배경 | 로고, 제품 이미지 |

---

# 16. `background-position`

배경 이미지가 배치되는 위치를 지정합니다.

원본 `.profile`:

```css
background-position: center;
```

원본 `#back3` 단축 속성:

```css
background: #abcdef url("image.webp") no-repeat center;
```

주요 키워드:

```css
background-position: left top;
background-position: center;
background-position: right bottom;
```

숫자값:

```css
background-position: 20px 40px;
```

퍼센트:

```css
background-position: 50% 50%;
```

`center`와 `50% 50%`는 일반적으로 같은 중앙 위치를 의미합니다.

---

# 17. `background-position` 두 값의 순서

```css
background-position: right top;
```

```text
첫 번째: 가로 위치
두 번째: 세로 위치
```

예:

```css
background-position: left center;
background-position: center bottom;
```

한 값만 쓰면 다른 축은 기본적으로 중앙으로 해석되는 경우가 많습니다.

```css
background-position: top;
```

개념적으로:

```text
center top
```

---

# 18. 프로필 배경 예제 분석

원본:

```css
.profile {
  border: 1px solid black;
  height: 100px;
  width: 100px;
  background-image: url("image.webp");
  background-repeat: no-repeat;
  background-position: center;
  border-radius: 50%;
}
```

현재 문제:

- `background-size`가 주석 처리되어 있다.
- 원본 이미지 크기가 100px보다 크면 중앙 일부만 보일 수 있다.
- 이미지가 요소보다 작으면 주변 빈 공간이 생길 수 있다.
- 배경 이미지에는 대체 텍스트가 없다.

시각적 프로필 배경 개선:

```css
.profile {
  width: 100px;
  aspect-ratio: 1;
  border: 1px solid #000;
  border-radius: 50%;
  background:
    url("../images/profile.webp")
    center / cover
    no-repeat;
}
```

---

# 19. 프로필 이미지에는 `<img>`가 더 적절할 수 있다

프로필 사진이 사용자에게 의미 있는 콘텐츠라면 CSS 배경보다 `<img>`가 적합합니다.

```html
<img
  class="profile-image"
  src="profile.webp"
  alt="홍길동 프로필 사진"
>
```

```css
.profile-image {
  display: block;
  width: 100px;
  aspect-ratio: 1;
  border-radius: 50%;
  object-fit: cover;
}
```

CSS 배경을 사용할 경우 대체 텍스트를 제공할 수 없습니다.

구분:

| 목적 | 권장 |
| --- | --- |
| 장식용 이미지 | CSS 배경 |
| 콘텐츠 이미지 | `<img>` |
| 프로필 사진 | 일반적으로 `<img>` |
| 텍스트 위 Hero 장식 | CSS 배경 |
| 로고 | 의미에 따라 `<img>` 또는 SVG |

---

# 20. `background-attachment`

배경 이미지가 스크롤에 어떻게 반응하는지 지정합니다.

주요 값:

| 값 | 설명 |
| --- | --- |
| `scroll` | 요소와 함께 스크롤되는 기본 동작 |
| `fixed` | 뷰포트 기준으로 고정된 것처럼 표시 |
| `local` | 요소 내부 스크롤과 함께 움직임 |

원본:

```css
#back2 {
  background-attachment: fixed;
  overflow: auto;
}
```

원본 내 코드 주석:

```text
fixed를 적용하면 스크롤을 이용해도 이미지가 움직이지 않음
```

핵심적으로 맞습니다.

---

# 21. `background-attachment: fixed`

```css
.hero {
  background-attachment: fixed;
}
```

스크롤 시 배경이 뷰포트에 고정된 것처럼 보이는 효과를 만들 수 있습니다.

흔히 패럴랙스 느낌을 만들기 위해 사용합니다.

주의:

- 모바일 브라우저에서 지원이나 동작이 제한될 수 있다.
- 성능 비용이 커질 수 있다.
- 스크롤 중 페인팅 비용이 증가할 수 있다.
- 움직임에 민감한 사용자에게 불편할 수 있다.
- 요소 내부 스크롤과 뷰포트 스크롤의 기준을 혼동할 수 있다.

---

# 22. 원본 `#back2`의 내부 스크롤

원본:

```css
#back2 {
  height: 80vh;
  background-size: cover;
  background-attachment: fixed;
  overflow: auto;
}
```

```css
#back2 p {
  height: 200vh;
}
```

`#back2` 높이는 `80vh`, 내부 `p`는 `200vh`이므로 콘텐츠가 더 큽니다.

```css
overflow: auto;
```

때문에 내부 스크롤이 생성됩니다.

이 예제는 다음 두 스크롤 기준을 함께 보여 줍니다.

- 페이지 스크롤
- `#back2` 내부 스크롤

`background-attachment: fixed`는 요소 내부 스크롤 기준이 아니라 뷰포트 기준으로 보이는 효과를 만들 수 있습니다.

---

# 23. `background-attachment: local`

내부 스크롤 영역과 함께 배경이 움직이게 하려면 `local`을 실험할 수 있습니다.

```css
.scroll-box {
  height: 300px;
  overflow: auto;
  background-image: url("paper.webp");
  background-attachment: local;
}
```

원본에는 직접 등장하지 않는 확장 학습입니다.

비교:

```text
scroll → 요소 배경 위치에 고정
fixed  → 뷰포트에 고정된 듯 표시
local  → 요소 내부 콘텐츠 스크롤과 함께 이동
```

---

# 24. 모바일에서 `fixed` 대안

모바일에서 안정적인 배경 효과가 필요하면 고정 배경 요소를 별도 레이어로 구성할 수 있습니다.

```css
.hero {
  position: relative;
  overflow: hidden;
}

.hero::before {
  position: absolute;
  z-index: -1;
  inset: 0;
  background:
    url("../images/hero.webp")
    center / cover
    no-repeat;
  content: "";
}
```

진짜 고정 효과가 필요하면 `position: fixed` 레이어를 사용할 수도 있지만, 레이아웃·성능·접근성을 세심하게 설계해야 합니다.

---

# 25. `background` 단축 속성

원본:

```css
#back3 {
  background:
    #abcdef
    url("image.webp")
    no-repeat
    center;
  background-size: contain;
}
```

원본 주석:

```text
background: color || img || repeat || attachment || position
```

입문 설명으로 방향은 맞지만 실제 단축 속성에는 더 많은 하위 속성이 포함됩니다.

대표 구성:

```text
background-color
background-image
background-position
background-size
background-repeat
background-origin
background-clip
background-attachment
```

---

# 26. 단축 속성의 일반적인 작성 형태

```css
.hero {
  background:
    #111
    url("../images/hero.webp")
    center / cover
    no-repeat
    fixed;
}
```

중요:

```text
background-position / background-size
```

`background-size`를 단축 속성에 포함하려면 `/`를 사용합니다.

```css
background: url("image.webp") center / cover no-repeat;
```

원본은 `background-size: contain`을 별도 선언으로 작성했기 때문에 문법상 문제 없습니다.

---

# 27. 단축 속성이 기존 개별값을 초기화한다

```css
.box {
  background-size: cover;
  background-repeat: no-repeat;
  background: red;
}
```

마지막 `background: red`는 이미지, 크기, 반복 등 관련 속성을 기본값으로 초기화할 수 있습니다.

따라서 단축 속성은 관련 개별 속성 뒤에 무심코 작성하지 않습니다.

안전한 순서:

```css
.box {
  background:
    red
    url("image.webp")
    center / cover
    no-repeat;
}
```

또는 개별 속성만 일관되게 사용합니다.

---

# 28. 내 코드와 강사님 코드의 `#back3`

내 코드:

```css
background:
  #abcdef
  url("image.webp")
  no-repeat
  /*fixed*/
  center;
```

강사님 코드:

```css
background:
  #abcdef
  url("image.webp")
  no-repeat
  center;
```

실제 적용 결과는 같습니다.

내 코드의 `/*fixed*/`는 단축 속성 안에서 `background-attachment: fixed`를 실험하기 위한 메모입니다.

더 읽기 쉬운 방식:

```css
background:
  #abcdef
  url("image.webp")
  center / contain
  no-repeat;

/* background-attachment: fixed; */
```

---

# 29. 다중 배경 이미지

여러 배경은 쉼표로 구분합니다.

```css
.hero {
  background-image:
    linear-gradient(
      rgb(0 0 0 / 55%),
      rgb(0 0 0 / 55%)
    ),
    url("../images/hero.webp");
}
```

앞에 작성한 배경이 위에 그려집니다.

```text
첫 번째 배경 → 가장 위
마지막 배경 → 가장 아래
```

각 배경에 크기와 위치를 따로 지정할 수 있습니다.

```css
.hero {
  background-position:
    center,
    center;
  background-size:
    cover,
    cover;
  background-repeat:
    no-repeat,
    no-repeat;
}
```

---

# 30. 그라디언트도 배경 이미지다

```css
.box {
  background-image:
    linear-gradient(
      to right,
      #2563eb,
      #7c3aed
    );
}
```

CSS에서 그라디언트는 `background-image`로 취급됩니다.

종류:

- `linear-gradient()`
- `radial-gradient()`
- `conic-gradient()`
- 반복 그라디언트

```css
.pattern {
  background-image:
    repeating-linear-gradient(
      45deg,
      #fff 0 10px,
      #eee 10px 20px
    );
}
```

---

# 31. 배경 오버레이

텍스트 대비를 높이기 위해 이미지 위에 반투명 검정 레이어를 올릴 수 있습니다.

```css
.hero {
  color: white;
  background:
    linear-gradient(
      rgb(0 0 0 / 55%),
      rgb(0 0 0 / 55%)
    ),
    url("../images/hero.webp")
    center / cover
    no-repeat;
}
```

배경 이미지가 밝아도 흰색 텍스트가 읽히기 쉬워집니다.

단순히 `opacity`를 부모에 주면 텍스트까지 흐려지므로 사용하지 않습니다.

---

# 32. 배경 위 텍스트 접근성

배경 이미지 위 텍스트는 이미지 색상에 따라 대비가 달라집니다.

확인 항목:

- 밝은 이미지 위 흰 글자가 사라지지 않는가?
- 어두운 이미지 위 검은 글자가 사라지지 않는가?
- 모바일 크롭에서 텍스트 뒤 영역이 달라지지 않는가?
- 이미지가 로드되지 않아도 글자가 읽히는가?
- 중요한 내용이 이미지에만 들어 있지 않은가?

안전한 패턴:

```css
.hero {
  color: white;
  background-color: #111;
  background-image:
    linear-gradient(
      rgb(0 0 0 / 60%),
      rgb(0 0 0 / 60%)
    ),
    url("../images/hero.webp");
}
```

---

# 33. `background-origin`

배경 위치 계산의 기준 영역을 지정합니다.

대표 값:

- `padding-box`
- `border-box`
- `content-box`

```css
.box {
  background-origin: content-box;
}
```

원본에는 없는 확장 학습입니다.

배경 이미지의 시작 위치 기준을 콘텐츠, 패딩, 테두리 중 어디로 삼을지 결정합니다.

---

# 34. `background-clip`

배경이 그려지는 범위를 지정합니다.

```css
.box {
  background-clip: padding-box;
}
```

대표 값:

| 값 | 배경 그리기 범위 |
| --- | --- |
| `border-box` | 테두리 영역까지 |
| `padding-box` | 패딩 영역까지 |
| `content-box` | 콘텐츠 영역만 |
| `text` | 텍스트 모양에 배경 적용 |

텍스트 그라디언트 예:

```css
.gradient-text {
  color: transparent;
  background:
    linear-gradient(
      to right,
      #2563eb,
      #7c3aed
    );
  background-clip: text;
}
```

브라우저 지원을 위해 다음 접두사가 필요한 환경도 있습니다.

```css
-webkit-background-clip: text;
```

---

# 35. 원본 문서 언어와 제목

내 코드와 강사님 코드:

```html
<html lang="en">
```

본문은 한국어이므로:

```html
<html lang="ko">
```

가 적절합니다.

제목:

```html
<title>Document</title>
```

개선:

```html
<title>CSS 배경 이미지</title>
```

---

# 36. 반복 `<br>` 문제

내 코드 마지막:

```html
<br><br><br>...
```

강사님 코드에는 더 많은 `<br>`가 있습니다.

스크롤을 만들기 위한 실습으로 보입니다.

하지만 실제 문서 간격은 CSS로 작성해야 합니다.

```css
body {
  min-height: 200vh;
}
```

또는 테스트 영역:

```css
.scroll-test {
  min-height: 100vh;
}
```

최종 프로젝트에서는 불필요한 `<br>`를 제거합니다.

---

# 37. 내 코드 분석

## 37.1 장점

- `repeat` 기본값이 양축 반복이라는 점을 설명했다.
- `repeat-x`, `repeat-y`, `no-repeat`을 한 위치에서 비교했다.
- 고정 크기와 퍼센트 크기 실험값을 주석으로 보존했다.
- `cover`가 비율을 유지하며 영역을 덮는다는 점을 설명했다.
- `contain`이 전체 이미지를 보여주는 목적임을 설명했다.
- `fixed`가 스크롤에도 배경을 고정하는 효과임을 설명했다.
- `overflow: auto`가 내부 스크롤을 만든다는 점을 기록했다.
- 단축 속성의 구성 요소를 주석으로 정리했다.
- 강사님 코드와 동일한 주요 실습을 해설형으로 보완했다.

---

# 38. 내 코드 개선점

## 38.1 `cover` 설명 보완

원본 비율을 유지하고 영역 전체를 덮지만 이미지 일부가 잘릴 수 있다는 점을 추가해야 합니다.

## 38.2 `contain`과 반복

`contain`만 지정하면 남는 공간에 기본 반복이 발생할 수 있습니다.

원본은 `no-repeat`도 함께 지정했으므로 문제없지만 두 속성의 관계를 설명하면 좋습니다.

## 38.3 프로필 배경 크기 누락

```css
/* background-size: contain; */
```

이 주석 상태에서는 이미지 전체가 들어오지 않을 수 있습니다.

원형 프로필이라면 `cover`가 자연스러운 경우가 많습니다.

## 38.4 외부 이미지 URL

실습 안정성과 유지보수를 위해 로컬 자산을 권장합니다.

## 38.5 `fixed` 일반화

모바일에서 제한되거나 성능 문제가 있을 수 있음을 추가해야 합니다.

## 38.6 단축 속성 주석

```text
color || img || repeat || attachment || position
```

은 일부 구성만 보여 줍니다.

`size`, `origin`, `clip`도 포함될 수 있음을 보완합니다.

## 38.7 반복 `<br>`

스크롤 실습이라도 CSS 최소 높이나 별도 테스트 영역을 사용하는 것이 좋습니다.

---

# 39. 강사님 코드 분석

강사님 코드는 배경 속성을 다음 순서로 실습합니다.

1. 배경 이미지
2. 반복
3. 크기
4. `cover`, `contain`
5. 고정 배경
6. 내부 스크롤
7. 원형 프로필 배경
8. 배경 위치
9. 단축 속성

간결한 코드로 속성별 결과를 빠르게 확인하기 좋습니다.

---

# 40. 강사님 코드 개선점

## 40.1 `http` 이미지 예제

```css
/* background-image: url('http://poiemaweb.com/img/bg/dot.png'); */
```

주석 처리되어 실행되지는 않지만 보안 연결이 아닌 `http`입니다.

학습 문서에서는 `https` 또는 로컬 자산을 사용합니다.

## 40.2 외부 이미지 의존

내 코드와 동일하게 외부 서버 주소에 의존합니다.

## 40.3 결과 설명 부족

`cover`와 `contain`의 잘림·빈 공간 차이 설명이 코드에 없습니다.

수업 설명과 함께 사용된 것으로 보이며 독립 문서에서는 보완이 필요합니다.

## 40.4 프로필 이미지 의미

CSS 배경을 사용하면 대체 텍스트를 제공할 수 없습니다.

의미 있는 프로필 사진이라면 `<img>`가 적합합니다.

## 40.5 반복 `<br>`

강사님 HTML은 스크롤을 만들기 위해 약 50개의 `<br>`를 사용합니다.

테스트 목적은 이해되지만 최종 코드에서는 CSS로 대체합니다.

## 40.6 파일 제목

`Document` 대신 학습 주제를 표현하는 제목이 필요합니다.

---

# 41. 내 코드와 강사님 코드 비교

| 비교 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 구조 | 동일한 4개 실습 영역 | 동일한 4개 실습 영역 |
| 반복 설명 | 기본값과 축별 반복 주석 추가 | 값만 나열 |
| 크기 설명 | `cover`, `contain` 목적 설명 | 코드 중심 |
| `fixed` | 스크롤 시 고정 설명 | 코드만 |
| `overflow` | 내부 스크롤 생성 설명 | 코드만 |
| 단축 속성 | 구성 요소 주석 추가 | 주석 없음 |
| `#back3` | `fixed` 실험 주석 포함 | `fixed` 없음 |
| 마지막 텍스트 | `아무 글자` | `어떤 글자` |
| 반복 `<br>` | 약 20개 | 약 50개 |
| 주석 이미지 | 없음 | 과거 `http` 점 패턴 URL |
| 학습 성격 | 복습 해설형 | 수업 실습형 |

---

# 42. 원본 개선 통합 예제

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
  <title>CSS 배경 이미지</title>
  <link
    rel="stylesheet"
    href="asset/css/background.css"
  >
</head>
<body>
  <main class="page">
    <h1>CSS 배경 이미지</h1>

    <section class="background-demo">
      <h2>Contain</h2>
      <div class="background-demo__contain">
        이미지 전체 표시
      </div>
    </section>

    <section class="background-demo">
      <h2>Cover</h2>
      <div class="background-demo__cover">
        영역 전체 덮기
      </div>
    </section>

    <section class="hero">
      <div class="hero__content">
        <h2>AI 서비스 개발 과정</h2>
        <p>배경 위 텍스트 대비를 확인합니다.</p>
      </div>
    </section>
  </main>
</body>
</html>
```

## CSS

```css
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
  width: min(100% - 2rem, 72rem);
  margin-inline: auto;
  padding-block: 2rem;
}

.background-demo > div {
  min-height: 16rem;
  border: 1px solid #dc2626;
  background-color: #f3f4f6;
  background-image:
    url("../images/background.webp");
  background-position: center;
  background-repeat: no-repeat;
}

.background-demo__contain {
  background-size: contain;
}

.background-demo__cover {
  background-size: cover;
}

.hero {
  display: grid;
  min-height: 70vh;
  margin-top: 3rem;
  padding: 2rem;
  color: white;
  background:
    linear-gradient(
      rgb(0 0 0 / 55%),
      rgb(0 0 0 / 55%)
    ),
    url("../images/hero.webp")
    center / cover
    no-repeat;
  place-items: center;
}

.hero__content {
  max-width: 40rem;
  text-align: center;
}
```

---

# 43. 실무 Hero 패턴

```css
.hero {
  min-height: 100vh;
  min-height: 100dvh;
  color: white;
  background:
    linear-gradient(
      rgb(0 0 0 / 60%),
      rgb(0 0 0 / 60%)
    ),
    url("../images/hero.webp")
    center / cover
    no-repeat;
}
```

장점:

- 이미지 비율 유지
- 화면 전체 덮기
- 텍스트 대비 확보
- 이미지 로딩 실패 시 그라디언트와 기본 배경색 활용 가능

배경색까지 포함:

```css
.hero {
  background-color: #111;
}
```

---

# 44. 카드 배경 패턴

```css
.course-card {
  min-height: 18rem;
  padding: 1.5rem;
  border-radius: 1rem;
  color: white;
  background:
    linear-gradient(
      to top,
      rgb(0 0 0 / 75%),
      transparent 70%
    ),
    url("../images/course.webp")
    center / cover
    no-repeat;
}
```

카드 아래쪽에만 어두운 그라디언트를 두어 텍스트 가독성을 높입니다.

---

# 45. 패턴 배경

이미지 없이 CSS 그라디언트로 패턴을 만들 수 있습니다.

```css
.grid-pattern {
  background-color: #fff;
  background-image:
    linear-gradient(
      #e5e7eb 1px,
      transparent 1px
    ),
    linear-gradient(
      90deg,
      #e5e7eb 1px,
      transparent 1px
    );
  background-size: 24px 24px;
}
```

두 개의 선형 그라디언트를 겹쳐 격자를 만듭니다.

---

# 46. 배경 이미지 성능

배경 이미지도 페이지 로딩 성능에 영향을 줍니다.

확인 항목:

- 실제 표시 크기에 비해 이미지가 지나치게 큰가?
- WebP, AVIF 등 최적화 포맷을 사용할 수 있는가?
- 모바일용 작은 이미지를 제공해야 하는가?
- 장식 이미지가 꼭 필요한가?
- 반복 패턴을 작은 이미지나 CSS로 대체할 수 있는가?
- 첫 화면 Hero 이미지가 렌더링을 늦추는가?

CSS 배경에는 `<img loading="lazy">`를 직접 사용할 수 없습니다.

화면 아래 장식 배경은 지연 로딩 전략을 별도로 설계해야 합니다.

---

# 47. 반응형 배경 이미지

미디어 쿼리로 다른 이미지를 사용할 수 있습니다.

```css
.hero {
  background-image:
    url("../images/hero-mobile.webp");
}

@media (min-width: 768px) {
  .hero {
    background-image:
      url("../images/hero-desktop.webp");
  }
}
```

텍스트와 오버레이도 함께 사용한다면 다중 배경 전체를 각 조건에서 다시 지정해야 할 수 있습니다.

```css
.hero {
  background:
    linear-gradient(
      rgb(0 0 0 / 55%),
      rgb(0 0 0 / 55%)
    ),
    url("../images/hero-mobile.webp")
    center / cover
    no-repeat;
}
```

---

# 48. 배경 이미지가 안 보일 때 점검 순서

1. 요소에 너비와 높이가 있는가?
2. 이미지 경로가 CSS 파일 기준으로 맞는가?
3. URL에 오타가 없는가?
4. 외부 서버가 이미지를 허용하는가?
5. `background-image: none`으로 덮였는가?
6. `background` 단축 속성이 기존 값을 초기화했는가?
7. 배경색과 이미지 색이 비슷한가?
8. 다른 요소가 위를 덮고 있는가?
9. 개발자 도구 Network에서 이미지가 로드됐는가?
10. Computed의 `background-image` 값은 무엇인가?

---

# 49. 이미지가 잘릴 때 점검 순서

1. `background-size: cover`인가?
2. 요소 비율과 이미지 비율이 다른가?
3. `background-position`이 중요한 영역을 가리키는가?
4. 모바일 화면에서 크롭 위치가 달라지는가?
5. `contain`이 더 적절한가?
6. 콘텐츠 이미지라면 `<img>`가 더 적절한가?
7. `object-fit`을 사용할 수 있는가?
8. 이미지 안에 텍스트가 포함되어 있지 않은가?
9. 중요한 피사체가 중앙에서 벗어나 있는가?
10. 화면별 이미지를 별도로 제공해야 하는가?

---

# 50. 배경이 반복될 때 점검 순서

1. `background-repeat` 기본값이 `repeat`임을 확인한다.
2. `no-repeat`이 단축 속성에서 초기화되지 않았는가?
3. `contain`으로 남는 공간이 생겼는가?
4. 이미지 자체 크기가 요소보다 작은가?
5. 다중 배경 각각의 반복값이 설정됐는가?
6. 쉼표 개수가 배경 레이어 수와 맞는가?
7. `repeat-x`, `repeat-y`가 남아 있는가?
8. CSS 규칙 순서에서 덮어쓰였는가?
9. 브라우저 개발자 도구에서 최종 값을 확인했는가?
10. 패턴 반복이 의도된 것인지 확인한다.

---

# 51. 자주 하는 실수

## 51.1 CSS 경로를 HTML 기준으로 작성

배경 이미지 URL은 CSS 파일 위치 기준입니다.

## 51.2 빈 `div`에 배경만 넣고 높이 미지정

박스 높이가 0이면 이미지가 보이지 않을 수 있습니다.

## 51.3 `contain`만 지정하고 반복 방지 누락

남는 영역에서 이미지가 반복될 수 있습니다.

## 51.4 `cover`가 이미지 전체를 보여 준다고 생각

영역은 덮지만 일부가 잘릴 수 있습니다.

## 51.5 `100% 100%`가 비율을 유지한다고 생각

요소 비율과 이미지 비율이 다르면 왜곡됩니다.

## 51.6 프로필 사진을 무조건 CSS 배경으로 사용

의미 있는 이미지라면 대체 텍스트가 가능한 `<img>`가 적절합니다.

## 51.7 `background: red`로 기존 이미지 유지 기대

단축 속성이 관련 배경 속성을 초기화할 수 있습니다.

## 51.8 `fixed`가 모든 모바일에서 동일하게 작동한다고 생각

지원과 성능이 다를 수 있습니다.

## 51.9 배경 이미지 위 텍스트 대비 미검수

이미지 크롭과 밝기에 따라 글자가 읽히지 않을 수 있습니다.

## 51.10 반복 `<br>`로 스크롤 생성

CSS 높이 또는 테스트 컨테이너를 사용합니다.

---


# 종합실습

## 문제 1. 배경 이미지

`.hero`에 `hero.webp`를 배경 이미지로 지정하세요. CSS 파일은 `asset/css/style.css`, 이미지는 `asset/images/hero.webp`에 있습니다.

## 문제 2. 반복 제거

배경 이미지가 반복되지 않도록 작성하세요.

## 문제 3. 가로 반복

배경 이미지를 가로 방향으로만 반복하세요.

## 문제 4. 고정 크기

배경 이미지 크기를 가로 `120px`, 세로 `80px`로 지정하세요.

## 문제 5. 비율 유지

배경 이미지의 가로를 `120px`로 지정하고 세로 비율은 자동 유지하세요.

## 문제 6. `cover`

`.hero`의 배경 이미지가 비율을 유지하면서 영역 전체를 덮도록 작성하세요.

## 문제 7. `contain`

`.logo`의 배경 이미지 전체가 보이도록 하고 중앙 배치하며 반복되지 않게 작성하세요.

## 문제 8. 위치

배경 이미지를 오른쪽 아래에 배치하세요.

## 문제 9. 전체 화면 Hero

`.hero`의 최소 높이를 `100dvh`로 지정하고 배경을 가운데 `cover`로 배치하세요. `100vh` 폴백도 포함하세요.

## 문제 10. 원형 프로필 배경

너비 `120px`인 원형 요소에 프로필 배경을 중앙 `cover`로 표시하세요.

## 문제 11. 접근성 판단

사용자의 프로필 사진이 중요한 콘텐츠입니다. CSS 배경과 `<img>` 중 무엇을 사용해야 하는지 이유와 함께 작성하세요.

## 문제 12. 고정 배경

`.section`의 배경을 스크롤 시 고정되도록 작성하세요.

## 문제 13. 내부 스크롤

높이 `300px`인 `.scroll-box`에 내부 스크롤을 만들고 배경이 내부 콘텐츠와 함께 움직이도록 작성하세요.

## 문제 14. 단축 속성

다음 값을 하나의 `background` 단축 속성으로 작성하세요.

- 배경색 `#111`
- 이미지 `hero.webp`
- 중앙 배치
- `cover`
- 반복 없음

## 문제 15. 단축 속성 초기화

다음 코드에서 이미지가 사라지는 이유를 설명하세요.

```css
.box {
  background-image: url("image.webp");
  background-size: cover;
  background: red;
}
```

## 문제 16. 오버레이

배경 이미지 위에 60% 불투명한 검정 오버레이를 적용하세요.

## 문제 17. 다중 배경

위쪽에 점 패턴, 아래쪽에 사진을 겹쳐 적용하는 CSS 구조를 작성하세요.

## 문제 18. 그라디언트

왼쪽 파랑에서 오른쪽 보라색으로 이어지는 선형 그라디언트를 작성하세요.

## 문제 19. 원본 프로필 개선

다음 원본을 의미 있는 프로필 이미지로 개선하세요.

```html
<div class="profile"></div>
```

```css
.profile {
  width: 100px;
  height: 100px;
  background-image: url("profile.webp");
  border-radius: 50%;
}
```

## 문제 20. 반복 `<br>` 개선

스크롤 실습을 위해 `<br>`를 30개 넣는 대신 CSS로 문서 최소 높이를 `200vh`로 만드세요.

## 문제 21. 반응형 배경

모바일에서는 `hero-mobile.webp`, `768px` 이상에서는 `hero-desktop.webp`를 사용하세요.

## 문제 22. 종합 Hero

다음 요구사항을 만족하는 Hero를 작성하세요.

- 최소 높이 `100vh`, `100dvh`
- 로컬 이미지
- 중앙 `cover`
- 반복 없음
- 이미지 위 검정 55% 오버레이
- 흰색 텍스트
- 텍스트 최대 폭 `40rem`
- 가운데 정렬
- 기본 배경색 제공
- 움직임 감소 사용자를 고려해 고정 배경은 사용하지 않음

---

# 정답과 해설

## 정답 1

```css
.hero {
  background-image:
    url("../images/hero.webp");
}
```

경로는 `asset/css/style.css` 기준입니다.

## 정답 2

```css
.hero {
  background-repeat: no-repeat;
}
```

## 정답 3

```css
.pattern {
  background-repeat: repeat-x;
}
```

## 정답 4

```css
.box {
  background-size: 120px 80px;
}
```

원본 비율과 다르면 왜곡될 수 있습니다.

## 정답 5

```css
.box {
  background-size: 120px auto;
}
```

## 정답 6

```css
.hero {
  background-size: cover;
}
```

이미지 일부가 잘릴 수 있습니다.

## 정답 7

```css
.logo {
  background-position: center;
  background-repeat: no-repeat;
  background-size: contain;
}
```

## 정답 8

```css
.box {
  background-position: right bottom;
}
```

## 정답 9

```css
.hero {
  min-height: 100vh;
  min-height: 100dvh;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}
```

## 정답 10

```css
.profile {
  width: 120px;
  aspect-ratio: 1;
  border-radius: 50%;
  background:
    url("../images/profile.webp")
    center / cover
    no-repeat;
}
```

장식 목적이라는 전제입니다.

## 정답 11

`<img>`를 사용합니다.

```html
<img
  class="profile-image"
  src="profile.webp"
  alt="홍길동 프로필 사진"
>
```

```css
.profile-image {
  display: block;
  width: 120px;
  aspect-ratio: 1;
  border-radius: 50%;
  object-fit: cover;
}
```

의미 있는 콘텐츠 이미지에는 대체 텍스트가 필요합니다.

## 정답 12

```css
.section {
  background-attachment: fixed;
}
```

모바일 지원과 성능을 확인해야 합니다.

## 정답 13

```css
.scroll-box {
  height: 300px;
  overflow: auto;
  background-attachment: local;
}
```

## 정답 14

```css
.hero {
  background:
    #111
    url("../images/hero.webp")
    center / cover
    no-repeat;
}
```

## 정답 15

마지막 `background: red` 단축 속성이 `background-image`, `background-size` 등 관련 속성을 기본값으로 초기화하기 때문입니다.

개선:

```css
.box {
  background:
    red
    url("image.webp")
    center / cover
    no-repeat;
}
```

## 정답 16

```css
.hero {
  background:
    linear-gradient(
      rgb(0 0 0 / 60%),
      rgb(0 0 0 / 60%)
    ),
    url("../images/hero.webp")
    center / cover
    no-repeat;
}
```

## 정답 17

```css
.box {
  background-image:
    url("../images/dot-pattern.png"),
    url("../images/photo.webp");
  background-position:
    left top,
    center;
  background-repeat:
    repeat,
    no-repeat;
  background-size:
    auto,
    cover;
}
```

첫 번째 배경이 가장 위에 표시됩니다.

## 정답 18

```css
.box {
  background-image:
    linear-gradient(
      to right,
      #2563eb,
      #7c3aed
    );
}
```

## 정답 19

### HTML

```html
<img
  class="profile-image"
  src="profile.webp"
  alt="홍길동 프로필 사진"
>
```

### CSS

```css
.profile-image {
  display: block;
  width: 100px;
  aspect-ratio: 1;
  border-radius: 50%;
  object-fit: cover;
}
```

## 정답 20

```css
body {
  min-height: 200vh;
}
```

테스트가 끝나면 제거합니다.

## 정답 21

```css
.hero {
  background-image:
    url("../images/hero-mobile.webp");
}

@media (min-width: 768px) {
  .hero {
    background-image:
      url("../images/hero-desktop.webp");
  }
}
```

## 정답 22

### HTML

```html
<section class="hero">
  <div class="hero__content">
    <h1 class="hero__title">
      AI 서비스 개발 과정
    </h1>

    <p class="hero__description">
      HTML, CSS, JavaScript부터
      AI Agent 프로젝트까지 학습합니다.
    </p>
  </div>
</section>
```

### CSS

```css
.hero {
  display: grid;
  min-height: 100vh;
  min-height: 100dvh;
  padding: 2rem;
  color: white;
  background:
    linear-gradient(
      rgb(0 0 0 / 55%),
      rgb(0 0 0 / 55%)
    ),
    url("../images/hero.webp")
    center / cover
    no-repeat
    #111;
  place-items: center;
}

.hero__content {
  max-width: 40rem;
  text-align: center;
}
```

고정 배경을 사용하지 않아 모바일과 움직임 민감 사용자에 대한 부담을 줄였습니다.

---

# 최종 체크리스트

## 기본 배경 속성

- [ ] 배경 이미지 URL을 CSS 파일 기준으로 작성했다.
- [ ] 빈 요소에 필요한 크기를 지정했다.
- [ ] 반복 여부를 명시했다.
- [ ] `cover`와 `contain`의 목적을 구분했다.
- [ ] `cover`에서 이미지 일부가 잘릴 수 있음을 확인했다.
- [ ] `contain`에서 빈 공간과 반복 가능성을 확인했다.
- [ ] 배경 위치를 화면별로 검수했다.

## 단축 속성

- [ ] `background-position / background-size` 문법을 확인했다.
- [ ] 단축 속성이 기존 개별 속성을 초기화하지 않는지 확인했다.
- [ ] 색상, 이미지, 반복, 위치, 크기를 빠뜨리지 않았다.
- [ ] 다중 배경의 쉼표 순서를 확인했다.
- [ ] 첫 번째 배경이 위 레이어임을 확인했다.

## 접근성

- [ ] 의미 있는 이미지를 CSS 배경으로 숨기지 않았다.
- [ ] 프로필 사진에는 적절한 `alt`를 제공했다.
- [ ] 배경 이미지 위 텍스트 대비를 확인했다.
- [ ] 이미지가 로드되지 않아도 텍스트가 읽히는지 확인했다.
- [ ] 이미지 안의 텍스트에만 정보를 의존하지 않았다.
- [ ] 장식 이미지는 실제 콘텐츠와 분리했다.

## 성능과 반응형

- [ ] 외부 이미지 URL 의존성을 줄였다.
- [ ] 실제 표시 크기에 맞는 이미지 파일을 사용했다.
- [ ] 모바일용 이미지가 필요한지 검토했다.
- [ ] `background-attachment: fixed`의 모바일 지원을 확인했다.
- [ ] 고정 배경의 성능 비용을 확인했다.
- [ ] 불필요한 대형 배경 이미지를 제거했다.
- [ ] WebP 또는 AVIF 사용을 검토했다.

## 원본 코드 검수

- [ ] `lang="en"`을 `lang="ko"`로 개선했다.
- [ ] `Document` 제목을 학습 주제로 변경했다.
- [ ] 강사님 주석의 `http` 이미지 주소를 확인했다.
- [ ] 반복 `<br>`를 CSS 높이로 대체했다.
- [ ] 프로필 배경에 `background-size`가 빠져 있음을 설명했다.
- [ ] 내 코드의 `cover`, `contain` 설명을 잘림과 빈 공간까지 보완했다.
- [ ] `background` 단축 속성의 전체 범위를 보완했다.
- [ ] 내 코드와 강사님 코드의 `fixed` 주석 차이를 오류로 처리하지 않았다.

---

# 핵심 요약

- CSS 배경은 요소 뒤에 색상과 이미지를 그리는 장식 기능이다.
- 배경 이미지는 콘텐츠가 아니므로 대체 텍스트를 제공하지 않는다.
- 의미 있는 프로필 사진과 콘텐츠 이미지는 일반적으로 `<img>`를 사용한다.
- 배경 이미지 URL은 HTML이 아니라 CSS 파일 위치 기준으로 계산한다.
- 빈 요소는 너비와 높이가 있어야 배경 이미지가 보인다.
- `background-repeat`의 기본값은 가로와 세로 모두 반복하는 `repeat`다.
- `no-repeat`은 배경 이미지를 한 번만 표시한다.
- `background-size`에 두 값을 쓰면 가로와 세로를 직접 지정한다.
- `100% 100%`는 영역을 채우지만 원본 비율이 왜곡될 수 있다.
- `cover`는 비율을 유지하면서 영역을 완전히 덮고 일부가 잘릴 수 있다.
- `contain`은 이미지 전체를 보여 주지만 빈 공간이 생길 수 있다.
- `background-position: center`는 배경을 가로·세로 중앙에 배치한다.
- `background-attachment: fixed`는 고정 배경 효과를 만들지만 모바일 지원과 성능에 주의해야 한다.
- 원본 `#back2`는 `80vh` 요소 안에 `200vh` 콘텐츠를 넣어 내부 스크롤을 만든다.
- `background` 단축 속성은 색상, 이미지, 위치, 크기, 반복, 고정 등을 포함할 수 있다.
- 단축 속성에서 크기를 쓰려면 위치 뒤에 `/`를 사용한다.
- `background` 단축 속성은 기존 개별 배경 속성을 초기화할 수 있다.
- 여러 배경은 쉼표로 구분하며 먼저 작성한 배경이 위에 그려진다.
- 그라디언트는 CSS에서 배경 이미지로 취급된다.
- 이미지 위 텍스트에는 반투명 그라디언트 오버레이가 유용하다.
- 외부 이미지 주소는 변경, 차단, 성능 문제에 취약하므로 로컬 자산이 안정적이다.
- 내 코드는 강사님 코드보다 설명이 풍부하지만 `cover`의 잘림, `contain`의 빈 공간, `fixed`의 모바일 한계를 보완해야 한다.
- 강사님 코드의 주석 처리된 `http` 점 패턴 주소는 실제 프로젝트에서 사용하지 않는 것이 좋다.
- 반복 `<br>`는 스크롤 테스트용일 수 있지만 최종 코드에서는 CSS 높이로 대체한다.
# V3 렌더링 추적 카드 — 이미지 로드와 박스 배경 그리기

배경 이미지는 요소의 배경 영역에 그려지며 요소 크기가 0이면 보이지 않을 수 있다. URL은 CSS 파일 위치를 기준으로 해석하고 size, position, repeat가 표시 방식을 결정한다.

Network에서 이미지 404 여부, Computed의 background-image, Box Model의 실제 크기를 확인한다. `cover`는 비율을 유지하며 영역을 덮어 일부가 잘릴 수 있다.

**원본 연결:** 내 코드와 강사님 코드의 `workspace_html/css/06_background.html 및 asset/css/06_background.css`에서 실제 선택자·계산값·화면 차이를 확인한다.
