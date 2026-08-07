---
title: HTML 이미지와 미디어
version: v2.0-final
last_updated: 2026-08-07
status: Completed
---

# HTML 이미지와 미디어

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `06_HTML_이미지와_미디어.md` |
| 분류 | `01_HTML` |
| 원본 기준 | `workspace_html/06_img.html`, `workspace_teacher/workspace_html/06_img.html` |
| 핵심 범위 | `img`, `src`, `alt`, `width`, `height`, `figure`, `picture`, `srcset`, `video`, `audio`, `iframe` |
| 학습 범위 | 이미지 경로, 대체 Text, 비율, 반응형 Image, Video·Audio·외부 Media 삽입 |
| 프로젝트 연결 | Profile, 상품 Image, Banner, Portfolio, 강의 Video, 지도·YouTube Embed |
| 문서 형식 | HTML Developer-Wiki V2 확정 형식 |

> 이 문서는 내 코드와 강사님 코드의 `06_img.html`을 비교해 `img`, `src`, `alt`, `width`, `height`, `video`, `controls`의 기본 동작을 정리한다. 원본의 `alt` 설명, 고정 Width·Height로 인한 비율 왜곡, 외부 Media URL 의존성, `iframe` Comment 예제를 교정하고 반응형 Image·Caption·Video·Audio·Embed 접근성과 성능까지 연결한다.

# 학습 목표

- `img` 요소의 역할과 빈 요소의 특징을 설명한다.
- `src`와 `alt`의 차이를 이해한다.
- 의미 있는 이미지와 장식용 이미지를 구분해 대체 텍스트를 작성한다.
- `width`와 `height`를 사용할 때 이미지 비율이 어떻게 달라지는지 설명한다.
- HTML 속성과 CSS 크기 조절의 역할을 구분한다.
- 상대 경로로 로컬 이미지를 연결한다.
- `figure`와 `figcaption`으로 이미지와 설명을 하나의 단위로 묶는다.
- `picture`와 `source`를 사용해 반응형 이미지를 구성한다.
- `video`, `audio`, `source`, `controls`의 역할을 설명한다.
- `iframe`의 목적과 사용할 때의 주의점을 이해한다.
- 원본 실습 코드와 강사님 코드를 비교하고 개선점을 찾는다.
- 접근성, 성능, 보안 관점에서 미디어 콘텐츠를 검토한다.

# 1. 웹에서 이미지와 미디어의 역할

웹페이지에는 다양한 시각·청각 콘텐츠가 사용됩니다.

| 콘텐츠 | 대표 용도 |
| --- | --- |
| 이미지 | 로고, 상품 사진, 프로필, 배너, 설명 그림 |
| 오디오 | 음악, 효과음, 음성 안내, 팟캐스트 |
| 비디오 | 강의, 홍보 영상, 사용 방법 안내 |
| 외부 문서 | 지도, 영상 플랫폼, 문서 뷰어 |

이미지와 영상은 사용자 이해를 돕지만 파일 크기가 크고 접근성에 영향을 주기 때문에 마크업만 작성하고 끝내면 안 됩니다.

확인해야 할 핵심 항목은 다음과 같습니다.

1. 파일 경로가 올바른가?
2. 대체 텍스트가 적절한가?
3. 원본 비율이 유지되는가?
4. 필요한 재생 제어 기능이 있는가?
5. 모바일에서도 화면이 깨지지 않는가?
6. 불필요하게 큰 파일을 내려받고 있지 않은가?
7. 외부 콘텐츠를 안전하게 삽입했는가?

# 2. `img`: 이미지 삽입

`img` 요소는 HTML 문서에 이미지를 표시합니다.

```html
<img src="asset/profile.png" alt="홍길동 프로필 사진">
```

| 구성 | 의미 |
| --- | --- |
| `img` | 이미지를 표시하는 요소 |
| `src` | 이미지 파일의 위치 |
| `alt` | 이미지를 대신하는 텍스트 |

`img`는 콘텐츠를 내부에 넣지 않는 **빈 요소**입니다.

```html
<img src="asset/logo.png" alt="ABC 서비스 로고">
```

다음처럼 닫는 태그를 작성하지 않습니다.

```html
<!-- 잘못된 형태 -->
<img src="asset/logo.png" alt="ABC 서비스 로고"></img>
```

# 3. `src`: 이미지 파일 경로

`src`는 source의 약자로 브라우저가 가져올 이미지 파일의 위치를 지정합니다.

```html
<img src="asset/photo.jpg" alt="공원 전경">
```

브라우저는 다음 순서로 이미지를 처리합니다.

1. HTML을 읽는다.
2. `src`에 적힌 위치를 확인한다.
3. 해당 파일을 요청한다.
4. 파일을 내려받는다.
5. 화면에 이미지를 렌더링한다.

따라서 경로가 잘못되면 이미지가 나타나지 않습니다.

```html
<img src="asset/not-found.png" alt="회사 건물 전경">
```

이미지가 실패해도 `alt`가 있으면 사용자에게 원래 콘텐츠의 의미를 전달할 수 있습니다.

# 4. 이미지 경로 작성

## 4.1 같은 폴더

```text
project/
├─ index.html
└─ logo.png
```

```html
<img src="logo.png" alt="서비스 로고">
```

## 4.2 하위 폴더

```text
project/
├─ index.html
└─ asset/
   └─ logo.png
```

```html
<img src="asset/logo.png" alt="서비스 로고">
```

## 4.3 상위 폴더

```text
project/
├─ asset/
│  └─ logo.png
└─ pages/
   └─ about.html
```

`about.html`에서 이미지를 연결합니다.

```html
<img src="../asset/logo.png" alt="서비스 로고">
```

## 4.4 외부 URL

```html
<img
  src="https://example.com/images/banner.jpg"
  alt="여름 이벤트 배너"
>
```

외부 이미지는 상대 서버 상태, 주소 변경, 접근 권한, 속도에 영향을 받습니다. 서비스 핵심 이미지라면 직접 관리하는 저장소나 CDN을 사용하는 것이 안정적입니다.

# 5. `alt`: 대체 텍스트

`alt`는 alternative text의 약자입니다.

```html
<img src="asset/cat.jpg" alt="창가에 앉아 밖을 바라보는 고양이">
```

대체 텍스트는 다음 상황에서 사용됩니다.

- 이미지가 로드되지 않았을 때
- 스크린 리더가 콘텐츠를 읽을 때
- 사용자가 이미지를 볼 수 없을 때
- 네트워크가 느려 이미지가 늦게 표시될 때

`alt`는 단순한 오류 메시지가 아니라 **이미지가 전달하는 의미를 대신하는 텍스트**입니다.

# 6. 좋은 `alt` 작성법

## 6.1 이미지의 목적을 설명한다

```html
<img src="asset/team.jpg" alt="회의실에서 프로젝트 일정을 논의하는 개발팀">
```

## 6.2 보이는 모든 것을 장황하게 나열하지 않는다

```html
<!-- 지나치게 장황함 -->
<img
  src="asset/team.jpg"
  alt="갈색 테이블과 흰색 벽이 있는 회의실에서 검은 옷을 입은 사람과 파란 옷을 입은 사람이 노트북 앞에 앉아 있는 사진"
>
```

문맥상 필요한 정보만 전달합니다.

```html
<img src="asset/team.jpg" alt="프로젝트 회의 중인 개발팀">
```

## 6.3 이미 주변 문장에 같은 설명이 있다면 반복을 피한다

```html
<h2>2026 개발팀 워크숍</h2>
<img src="asset/workshop.jpg" alt="개발팀 워크숍 단체 사진">
```

## 6.4 파일명을 그대로 사용하지 않는다

```html
<!-- 좋지 않은 예 -->
<img src="asset/img_20260723_01.jpg" alt="img_20260723_01.jpg">
```

```html
<!-- 개선 예 -->
<img src="asset/img_20260723_01.jpg" alt="수료식을 마친 교육생들의 단체 사진">
```

## 6.5 `이미지`, `사진`이라는 표현은 꼭 필요할 때만 쓴다

스크린 리더는 해당 콘텐츠가 이미지임을 이미 알 수 있습니다.

```html
<img src="asset/search.svg" alt="검색">
```

버튼 안의 아이콘은 기능을 간결하게 설명합니다.

```html
<button type="button">
  <img src="asset/search.svg" alt="검색">
</button>
```

# 7. 장식용 이미지의 `alt`

내용 전달 없이 디자인만 위한 이미지는 빈 대체 텍스트를 사용합니다.

```html
<img src="asset/deco-line.svg" alt="">
```

`alt`를 생략하는 것과 `alt=""`는 의미가 다릅니다.

| 작성 방식 | 의미 |
| --- | --- |
| `alt=""` | 장식용 이미지이므로 읽지 않아도 됨 |
| `alt` 생략 | 대체 텍스트가 누락되었을 가능성이 있음 |

장식만을 위한 요소라면 가능하면 HTML 이미지보다 CSS 배경 이미지도 고려할 수 있습니다.

```css
.hero {
  background-image: url("../asset/pattern.svg");
}
```

# 8. 기능을 가진 이미지의 `alt`

링크나 버튼 안에 이미지가 있다면 이미지의 모양보다 **수행되는 기능**을 설명합니다.

```html
<a href="index.html">
  <img src="asset/logo.svg" alt="홈으로 이동">
</a>
```

```html
<button type="button">
  <img src="asset/close.svg" alt="창 닫기">
</button>
```

다만 버튼에 화면 텍스트가 함께 있다면 이미지의 `alt`를 비워 중복 읽기를 피할 수 있습니다.

```html
<button type="button">
  <img src="asset/search.svg" alt="">
  검색
</button>
```

# 9. `title`과 `alt`의 차이

`title`은 추가 설명을 제공할 수 있지만 `alt`를 대신하지 못합니다.

```html
<img
  src="asset/chart.png"
  alt="6월 매출은 5월보다 18% 증가했다"
  title="2026년 상반기 월별 매출 그래프"
>
```

| 속성 | 목적 |
| --- | --- |
| `alt` | 이미지의 의미를 대신 전달 |
| `title` | 부가 설명 제공 |

마우스를 사용할 수 없는 사용자나 터치 환경에서는 `title` 정보가 쉽게 전달되지 않을 수 있으므로 핵심 정보는 `alt`나 본문에 작성합니다.

# 10. 이미지 크기 지정

`width`와 `height`로 이미지의 표시 크기를 지정할 수 있습니다.

```html
<img
  src="asset/profile.png"
  alt="홍길동 프로필 사진"
  width="200"
  height="200"
>
```

HTML 속성의 숫자는 일반적으로 CSS 픽셀 기준으로 해석됩니다.

```html
<img src="asset/banner.jpg" alt="신규 과정 모집 배너" width="800" height="400">
```

# 11. 원본 비율과 이미지 왜곡

원본 이미지가 `800 × 400`이면 가로세로 비율은 `2:1`입니다.

다음은 같은 비율입니다.

```html
<img src="asset/banner.jpg" alt="신규 과정 모집 배너" width="400" height="200">
```

다음은 비율이 달라 이미지가 찌그러질 수 있습니다.

```html
<img src="asset/banner.jpg" alt="신규 과정 모집 배너" width="400" height="400">
```

초기 실습 코드에는 이미지에 `width="200"`, `height="300"`을 함께 지정한 예제가 있습니다.

```html
<img
  src="asset/Spongebob-Christmas-PNG-Picture.png"
  alt="스폰지밥이 웃고 있는 모습"
  width="200"
  height="300"
>
```

원본 이미지의 비율이 `2:3`이 아니라면 이미지가 왜곡됩니다. 학습 단계에서는 크기 속성을 확인하는 예제가 될 수 있지만 실제 화면에서는 원본 비율을 확인해야 합니다.

# 12. 한쪽 크기만 지정하기

너비만 지정하면 브라우저가 원본 비율에 맞춰 높이를 계산합니다.

```html
<img
  src="asset/Spongebob-Christmas-PNG-Picture.png"
  alt="스폰지밥이 웃고 있는 모습"
  width="200"
>
```

CSS에서는 다음처럼 작성할 수 있습니다.

```css
img {
  width: 200px;
  height: auto;
}
```

`height: auto`는 너비 변화에 맞춰 높이를 자동 계산하여 원본 비율을 유지합니다.

# 13. HTML 속성과 CSS의 역할

HTML에도 `width`, `height` 속성을 작성할 수 있고 CSS에서도 크기를 조절할 수 있습니다.

```html
<img
  class="profile-image"
  src="asset/profile.jpg"
  alt="홍길동 프로필 사진"
  width="400"
  height="400"
>
```

```css
.profile-image {
  width: 160px;
  height: 160px;
  object-fit: cover;
}
```

| 구분 | 역할 |
| --- | --- |
| HTML `width`, `height` | 이미지의 고유 비율과 렌더링 공간 정보를 브라우저에 제공 |
| CSS `width`, `height` | 화면 디자인에 맞는 실제 표시 크기 결정 |

HTML에 원본 비율에 맞는 너비와 높이를 함께 작성하면 이미지가 로드되기 전에도 브라우저가 공간을 미리 확보할 수 있어 레이아웃 흔들림을 줄이는 데 도움이 됩니다.

# 14. 반응형 이미지 기본 설정

이미지가 부모 영역보다 커지지 않도록 설정합니다.

```css
img {
  max-width: 100%;
  height: auto;
}
```

```html
<div class="content">
  <img src="asset/large-banner.jpg" alt="AI 과정 모집 안내">
</div>
```

`max-width: 100%`는 이미지가 원본보다 무조건 커지게 하는 속성이 아니라, 부모의 너비를 넘지 않도록 제한합니다.

# 15. `object-fit`으로 이미지 영역 맞추기

카드 썸네일처럼 일정한 크기의 영역에 여러 비율의 이미지를 넣을 때 `object-fit`을 사용합니다.

```html
<img class="thumbnail" src="asset/course.jpg" alt="노트북으로 코딩하는 교육생">
```

```css
.thumbnail {
  width: 320px;
  height: 180px;
  object-fit: cover;
}
```

| 값 | 동작 |
| --- | --- |
| `fill` | 영역에 맞게 늘어나며 비율이 깨질 수 있음 |
| `contain` | 전체 이미지가 보이도록 맞춤 |
| `cover` | 영역을 채우되 일부가 잘릴 수 있음 |
| `none` | 원본 크기를 유지 |
| `scale-down` | `none`과 `contain` 중 더 작은 결과 사용 |

프로필 이미지에는 정사각형 영역과 `cover`를 자주 사용합니다.

```css
.avatar {
  width: 96px;
  aspect-ratio: 1;
  border-radius: 50%;
  object-fit: cover;
}
```

# 16. `figure`와 `figcaption`

이미지와 설명이 하나의 독립적인 콘텐츠 단위를 이룰 때 `figure`를 사용합니다.

```html
<figure>
  <img src="asset/dashboard.png" alt="관리자 대시보드 메인 화면">
  <figcaption>회원 통계와 최근 활동을 보여주는 관리자 대시보드</figcaption>
</figure>
```

| 요소 | 역할 |
| --- | --- |
| `figure` | 이미지, 코드, 그래프 같은 독립 콘텐츠 묶음 |
| `figcaption` | 해당 콘텐츠의 제목이나 설명 |

`figcaption`은 이미지 아래에만 작성해야 하는 것은 아닙니다. `figure`의 첫 번째 또는 마지막 자식으로 사용할 수 있습니다.

```html
<figure>
  <figcaption>월별 신규 가입자 변화</figcaption>
  <img src="asset/signup-chart.png" alt="1월부터 6월까지 신규 가입자가 꾸준히 증가한 그래프">
</figure>
```

# 17. `alt`와 `figcaption`의 차이

두 요소는 서로 대체 관계가 아닙니다.

```html
<figure>
  <img
    src="asset/team-photo.jpg"
    alt="교육장 앞에서 손을 들고 웃는 20명의 수료생"
  >
  <figcaption>AI 서비스 개발 과정 1기 수료식</figcaption>
</figure>
```

| 구분 | 역할 |
| --- | --- |
| `alt` | 이미지를 볼 수 없을 때 이미지 자체를 대신 설명 |
| `figcaption` | 모든 사용자에게 이미지와 관련된 캡션 제공 |

# 18. `picture`: 화면 조건에 따라 이미지 선택

`picture`는 화면 크기나 이미지 형식에 따라 다른 파일을 제공할 때 사용합니다.

```html
<picture>
  <source media="(min-width: 1024px)" srcset="asset/banner-large.jpg">
  <source media="(min-width: 600px)" srcset="asset/banner-medium.jpg">
  <img src="asset/banner-small.jpg" alt="AI 개발자 과정 모집 배너">
</picture>
```

브라우저는 위에서부터 조건을 검사하고 적절한 이미지를 선택합니다. 마지막 `img`는 기본 이미지이자 대체 수단입니다.

# 19. 이미지 형식에 따른 선택

브라우저가 지원하는 형식에 따라 최신 이미지 포맷을 우선 제공할 수 있습니다.

```html
<picture>
  <source srcset="asset/course.avif" type="image/avif">
  <source srcset="asset/course.webp" type="image/webp">
  <img src="asset/course.jpg" alt="프로그래밍 수업을 듣는 교육생">
</picture>
```

| 형식 | 특징 |
| --- | --- |
| JPEG | 사진에 널리 사용 |
| PNG | 투명 배경과 선명한 그래픽에 적합 |
| SVG | 로고와 아이콘 같은 벡터 이미지 |
| WebP | 비교적 효율적인 압축과 다양한 기능 지원 |
| AVIF | 높은 압축 효율을 제공하는 최신 형식 |

파일 형식만 바꾸는 것으로 끝나지 않으며 실제 파일 크기와 화질을 비교해야 합니다.

# 20. `srcset`과 해상도 대응

같은 이미지의 해상도별 파일을 제공할 수 있습니다.

```html
<img
  src="asset/profile-400.jpg"
  srcset="
    asset/profile-400.jpg 1x,
    asset/profile-800.jpg 2x
  "
  alt="홍길동 프로필 사진"
  width="200"
  height="200"
>
```

고해상도 화면에서는 더 선명한 이미지를 선택할 수 있습니다.

너비 기준으로도 후보를 제공할 수 있습니다.

```html
<img
  src="asset/banner-800.jpg"
  srcset="
    asset/banner-480.jpg 480w,
    asset/banner-800.jpg 800w,
    asset/banner-1440.jpg 1440w
  "
  sizes="(max-width: 600px) 100vw, 800px"
  alt="AI 개발자 과정 모집 배너"
>
```

# 21. 이미지 지연 로딩

화면 아래에 있는 이미지는 사용자가 가까이 스크롤했을 때 불러오도록 설정할 수 있습니다.

```html
<img
  src="asset/project-preview.jpg"
  alt="포트폴리오 프로젝트 미리보기"
  loading="lazy"
  width="800"
  height="450"
>
```

`loading="lazy"`는 초기 다운로드 부담을 줄일 수 있습니다.

다만 첫 화면의 대표 이미지처럼 즉시 보여야 하는 콘텐츠에는 무조건 적용하지 않습니다.

```html
<img
  src="asset/hero.jpg"
  alt="AI Agent 개발 과정 메인 비주얼"
  width="1440"
  height="720"
>
```

# 22. 이미지 성능 최적화

이미지 최적화는 사용자 체감 속도에 큰 영향을 줍니다.

## 22.1 실제 표시 크기에 맞는 파일 사용

화면에서 `200 × 200`으로 보이는 프로필에 `6000 × 6000` 이미지를 그대로 사용하는 것은 비효율적입니다.

## 22.2 적절한 형식 선택

- 사진: JPEG, WebP, AVIF
- 투명 이미지: PNG, WebP
- 로고·아이콘: SVG

## 22.3 압축

화질을 크게 해치지 않는 범위에서 파일을 압축합니다.

## 22.4 크기 속성 제공

```html
<img
  src="asset/card.jpg"
  alt="프로젝트 카드 미리보기"
  width="640"
  height="360"
  loading="lazy"
>
```

## 22.5 의미 없는 이미지 요청 줄이기

단순 장식은 CSS로 처리할 수 있는지 검토합니다.

# 23. `video`: 동영상 삽입

`video` 요소는 HTML 문서 안에서 동영상을 재생합니다.

```html
<video src="asset/course-intro.mp4" controls></video>
```

`controls`는 재생, 일시 정지, 볼륨, 탐색 등의 기본 조작 UI를 제공합니다.

원본 실습에서는 다음 코드를 사용했습니다.

```html
<video
  controls="controls"
  loop="loop"
  src="https://www.w3schools.com/tags/movie.mp4">
</video>
```

불리언 속성은 속성명만 작성해도 됩니다.

```html
<video
  controls
  loop
  src="https://www.w3schools.com/tags/movie.mp4">
</video>
```

두 방식 모두 동작하지만 현재는 간결한 형태를 자주 사용합니다.

# 24. `video` 주요 속성

| 속성 | 역할 |
| --- | --- |
| `src` | 동영상 파일 경로 |
| `controls` | 기본 재생 제어 UI 표시 |
| `autoplay` | 자동 재생 시도 |
| `muted` | 음소거 |
| `loop` | 반복 재생 |
| `poster` | 재생 전 표시할 이미지 |
| `preload` | 미리 불러오기 정책 |
| `width`, `height` | 표시 크기 |
| `playsinline` | 모바일에서 페이지 내부 재생 유도 |

```html
<video
  controls
  poster="asset/course-poster.jpg"
  width="960"
  height="540"
>
  <source src="asset/course-intro.webm" type="video/webm">
  <source src="asset/course-intro.mp4" type="video/mp4">
  동영상을 재생할 수 없는 브라우저입니다.
</video>
```

# 25. `source`: 여러 영상 형식 제공

`video` 내부에 여러 `source`를 작성하면 브라우저가 지원하는 형식을 선택할 수 있습니다.

```html
<video controls>
  <source src="asset/demo.webm" type="video/webm">
  <source src="asset/demo.mp4" type="video/mp4">
  브라우저가 동영상 재생을 지원하지 않습니다.
</video>
```

`source`는 빈 요소입니다.

```html
<source src="asset/demo.mp4" type="video/mp4">
```

# 26. 자동 재생 주의점

자동 재생은 사용자를 놀라게 하거나 데이터 사용량을 증가시킬 수 있습니다. 많은 브라우저는 소리가 있는 자동 재생을 제한합니다.

```html
<video autoplay muted loop playsinline>
  <source src="asset/background-video.mp4" type="video/mp4">
</video>
```

배경 영상처럼 자동 재생이 꼭 필요한 경우에도 다음을 고려합니다.

- 기본 음소거
- 일시 정지 기능 제공
- 지나치게 긴 영상 피하기
- 텍스트 가독성 확보
- 모바일 데이터 사용량 고려
- 움직임에 민감한 사용자를 위한 대안 제공

# 27. `poster`: 영상 대표 이미지

```html
<video
  controls
  poster="asset/tutorial-poster.jpg"
  width="800"
  height="450"
>
  <source src="asset/tutorial.mp4" type="video/mp4">
</video>
```

`poster`는 영상이 재생되기 전에 표시할 이미지입니다. 대표 장면을 제공하면 사용자가 내용을 미리 이해할 수 있습니다.

# 28. 영상 자막

영상 콘텐츠에는 자막을 제공하는 것이 좋습니다.

```html
<video controls>
  <source src="asset/lecture.mp4" type="video/mp4">
  <track
    kind="subtitles"
    src="asset/lecture-ko.vtt"
    srclang="ko"
    label="한국어"
    default
  >
</video>
```

| 속성 | 의미 |
| --- | --- |
| `kind` | 트랙의 종류 |
| `src` | 자막 파일 경로 |
| `srclang` | 자막 언어 |
| `label` | 사용자에게 표시할 이름 |
| `default` | 기본 선택 여부 |

자막은 청각장애 사용자뿐 아니라 소리를 재생하기 어려운 환경에서도 도움이 됩니다.

# 29. `audio`: 오디오 삽입

```html
<audio controls src="asset/podcast.mp3"></audio>
```

여러 형식을 제공할 수 있습니다.

```html
<audio controls>
  <source src="asset/podcast.ogg" type="audio/ogg">
  <source src="asset/podcast.mp3" type="audio/mpeg">
  브라우저가 오디오 재생을 지원하지 않습니다.
</audio>
```

오디오에도 자동 재생을 남용하지 않습니다.

# 30. `iframe`: 외부 문서 삽입

`iframe`은 현재 문서 안에 다른 HTML 문서를 표시합니다.

```html
<iframe
  src="https://example.com"
  title="예제 사이트 미리보기"
></iframe>
```

초기 실습 주석에서는 `iframe`을 “브라우저 안에 또 다른 브라우저를 여는 것”으로 설명했습니다. 학습 관점에서는 이해하기 쉬운 표현이지만, 더 정확히는 **현재 문서 안에 별도의 문서 탐색 컨텍스트를 삽입하는 요소**입니다.

# 31. 유튜브 영상 삽입

영상 플랫폼에서 제공하는 임베드 코드를 사용할 수 있습니다.

```html
<iframe
  width="560"
  height="315"
  src="https://www.youtube.com/embed/VIDEO_ID"
  title="HTML 이미지와 미디어 강의"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
  referrerpolicy="strict-origin-when-cross-origin"
  allowfullscreen>
</iframe>
```

`iframe`에도 내용을 설명하는 `title`을 제공해야 합니다.

# 32. 반응형 `iframe`

고정 너비와 높이는 작은 화면에서 넘칠 수 있습니다.

```html
<div class="video-frame">
  <iframe
    src="https://www.youtube.com/embed/VIDEO_ID"
    title="프로젝트 시연 영상"
    allowfullscreen>
  </iframe>
</div>
```

```css
.video-frame {
  width: 100%;
  aspect-ratio: 16 / 9;
}

.video-frame iframe {
  width: 100%;
  height: 100%;
  border: 0;
}
```

# 33. `iframe` 사용 시 주의점

외부 문서를 삽입하면 다음 요소를 함께 검토합니다.

- 외부 서비스가 신뢰할 수 있는가?
- 개인정보나 쿠키 정책에 영향이 있는가?
- 로딩 속도가 느려지지 않는가?
- `title`이 제공되는가?
- 화면 크기에 대응하는가?
- 필요한 권한만 `allow`로 제공하는가?
- `sandbox`로 기능을 제한할 필요가 있는가?

```html
<iframe
  src="https://example.com/embed"
  title="외부 문서 미리보기"
  sandbox="allow-scripts allow-same-origin">
</iframe>
```

`sandbox`는 외부 문서의 동작을 제한하지만 필요한 기능까지 막을 수 있으므로 서비스 요구사항을 확인해야 합니다.

# 34. `br`로 미디어 간격 만들기

원본 실습 코드에서는 이미지 사이를 띄우기 위해 `br`을 사용했습니다.

```html
<img src="asset/photo1.png" alt="첫 번째 예시">
<br>
<img src="asset/photo2.png" alt="두 번째 예시">
```

학습 중 줄바꿈 결과를 확인하는 용도로는 가능하지만, 디자인 간격은 CSS를 사용하는 것이 좋습니다.

```html
<div class="image-list">
  <img src="asset/photo1.png" alt="첫 번째 예시">
  <img src="asset/photo2.png" alt="두 번째 예시">
</div>
```

```css
.image-list {
  display: grid;
  gap: 24px;
}
```

# 35. 여러 속성을 줄바꿈하여 작성하기

HTML 속성은 공백과 줄바꿈으로 구분할 수 있습니다.

```html
<img
  src="asset/Spongebob-Christmas-PNG-Picture.png"
  alt="스폰지밥이 웃고 있는 모습"
  width="200"
  height="300"
>
```

속성명 자체를 중간에서 나눌 수는 없습니다.

```html
<!-- 잘못된 예 -->
<img s
rc="asset/photo.png" alt="예제 이미지">
```

다음처럼 하나의 속성 단위를 유지해야 합니다.

```html
<img
  src="asset/photo.png"
  alt="예제 이미지"
>
```

# 36. 원본 실습 코드 분석

사용자 실습 코드의 핵심 구조는 다음과 같습니다.

```html
<img
  src="asset/Spongebob-Christmas-PNG-Picture.png"
  alt="스폰지밥이 웃고있는 사진"
>
<br>

<img
  src="asset/Spongebob-Christmas-PNG-Picture.png"
  alt="스폰지밥이 웃고있는 사진"
  width="200"
  height="300"
>
<br>

<video
  controls="controls"
  loop="loop"
  src="https://www.w3schools.com/tags/movie.mp4">
</video>
```

이 코드는 다음 개념을 한 파일에서 연습합니다.

- 로컬 이미지 경로
- `alt` 대체 텍스트
- 이미지 크기 속성
- 여러 줄 속성 작성
- 동영상 삽입
- 기본 재생 컨트롤
- 반복 재생

# 37. 내 코드와 강사님 코드 비교

두 원본은 같은 SpongeBob Image 두 개와 외부 MP4 Video를 사용한다. 내 코드는 `alt`, Image 비율, Browser Resource Loading, `iframe`, `controls`에 대한 Comment를 추가했고 강사님 코드는 Markup 자체를 더 간결하게 작성했다.

## 37.1 기본 문서 구조

두 코드 모두 HTML5 기본 구조를 사용한다.

```html
<!doctype html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        >
        <title>Document</title>
    </head>
</html>
```

본문이 한국어이므로 다음처럼 문서 언어를 맞추는 편이 적절하다.

```html
<html lang="ko">
```

Page 제목도 목적이 드러나도록 작성한다.

```html
<title>HTML 이미지와 미디어 실습</title>
```

## 37.2 복원 메모

내 코드에는 다음 개인 작업 기록이 있다.

```html
<!-- 0723_HTML_img/video_restore -->
```

학습 개념과 직접 관련이 없다면 Git Commit이나 별도 작업 기록으로 분리하는 편이 문서 집중도를 높인다.

## 37.3 `alt` 설명

내 코드에는 다음 설명이 있다.

```html
<!-- img를 사용할 때 alt
     (이미지가 없습니다, 무슨 이미지가 있었는지 등)는
     사용하는것이 좋음 -->
```

또한 다음 Comment도 있다.

```html
<!-- alt는 대체텍스트이며,
     웹 접근성에 이롭게 하기 위해 적어놓는 것 -->
```

핵심 방향은 맞지만 `alt`는 단순히 “이미지가 없습니다”라고 알려주는 Text가 아니다.

```text
alt
→ Image가 전달하는 정보·기능을 Text로 대체
```

좋은 예:

```html
<img
    src="./asset/spongebob.png"
    alt="스폰지밥이 웃고 있는 모습"
>
```

Image가 장식용이면 다음처럼 빈 `alt`를 사용할 수 있다.

```html
<img
    src="./asset/decorative-line.svg"
    alt=""
>
```

Screen Reader가 파일명이나 불필요한 정보를 읽지 않도록 Image 목적에 따라 결정한다.

## 37.4 첫 번째 Image

두 코드 모두 다음 Image를 사용한다.

```html
<img
    src="asset/Spongebob-Christmas-PNG-Picture.png"
    alt="스폰지밥이 웃고있는 사진"
>
```

구조는 같다. 다만 File Name은 공백·대문자·긴 이름을 피하고 Project 규칙에 맞게 단순화할 수 있다.

```html
<img
    src="./asset/spongebob-christmas.png"
    alt="스폰지밥이 웃고 있는 모습"
>
```

`./`는 필수는 아니지만 현재 폴더 기준이라는 의도를 드러낼 수 있다.

## 37.5 Attribute 줄바꿈

강사님 코드는 두 번째 Image의 Attribute를 여러 줄로 나눈다.

```html
<img
    src="asset/Spongebob-Christmas-PNG-Picture.png"
    alt="스폰지밥이 웃고있는 사진"
    width="200"
    height="300"
>
```

내 코드는 같은 내용을 한 줄로 작성한다.

```html
<img src="asset/Spongebob-Christmas-PNG-Picture.png" alt="스폰지밥이 웃고있는 사진" width="200" height="300">
```

두 방식 모두 유효하다. Attribute가 많아지면 한 줄씩 정렬하는 편이 Diff와 가독성에 유리하다.

내 코드의 다음 Comment는 방향은 맞다.

```html
<!-- 속성은 줄바꿈할 수 있으나
     src 같은 하나의 속성 이름 자체를 나눌 수는 없음 -->
```

다음처럼 Attribute 경계에서 줄바꿈한다.

```html
<img
    src="./asset/image.png"
    alt="설명"
>
```

## 37.6 Width와 Height 비율

두 코드 모두 다음 값을 지정한다.

```html
<img
    src="asset/Spongebob-Christmas-PNG-Picture.png"
    alt="스폰지밥이 웃고있는 사진"
    width="200"
    height="300"
>
```

내 코드 Comment에는 “너비나 높이를 하나만 지정하면 원본 비율을 유지한다”는 설명이 있다. 이 설명은 핵심적으로 맞다.

하지만 원본처럼 **원본 비율과 다른 `width`와 `height`를 동시에 강제하면 Image가 찌그러질 수 있다.**

```html
<img
    src="./asset/spongebob.png"
    alt="스폰지밥이 웃고 있는 모습"
    width="200"
>
```

또는 CSS에서 다음처럼 처리한다.

```css
.media-image {
    max-width: 100%;
    height: auto;
}
```

다만 HTML의 `width`와 `height`를 모두 생략하는 것이 항상 더 좋은 것은 아니다. 원본 Image 비율과 일치하는 실제 크기를 HTML Attribute로 제공하면 Browser가 Load 전에 Layout 공간을 확보해 Layout Shift를 줄일 수 있다.

```html
<img
    src="./asset/spongebob.png"
    alt="스폰지밥이 웃고 있는 모습"
    width="800"
    height="600"
>
```

CSS에서 표시 크기를 유연하게 조절한다.

## 37.7 Browser Resource Loading 설명

내 코드에는 Browser가 Image나 Video Resource를 가져와 표시한다는 Comment가 추가되어 있다.

```html
<!-- img태그도 해당 링크로 가서
     다운받아온 후 출력 -->
```

개념상 Browser가 `src` URL로 HTTP Request를 보내 Resource를 가져오는 방향은 맞다.

더 정확한 흐름:

```text
HTML Parse
→ src 발견
→ Resource Request
→ 응답 수신
→ Decode
→ Layout·Paint
```

Browser Cache, CORS, CSP, MIME Type, Network 오류에 따라 표시 결과가 달라질 수 있다.

## 37.8 `<br>` 반복

두 코드 모두 Image 사이에 `<br>`을 사용한다.

```html
<img ...>
<br>
<img ...>
<br>
```

학습 중 줄을 구분하는 데는 단순하지만 실제 Layout 간격은 CSS로 처리한다.

```css
.media-list {
    display: grid;
    gap: 1rem;
}
```

## 37.9 `iframe` 예제

내 코드에는 Comment 처리된 YouTube Embed가 추가되어 있다.

```html
<iframe
    width="560"
    height="315"
    src="https://www.youtube.com/embed/..."
    title="YouTube video player"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen
></iframe>
```

강사님 코드에는 `iframe` 예제가 없다.

내 코드의 다음 설명은 비유로는 이해하기 쉽지만 기술적으로 단순화되어 있다.

```text
iframe
→ 내 Browser 안에 또 다른 Browser를 연다
```

더 정확한 설명:

```text
iframe
→ 현재 HTML Document 안에
  다른 Browsing Context와 Document를 삽입
```

외부 Site는 `X-Frame-Options`, CSP `frame-ancestors` 등에 따라 Embed를 차단할 수 있다.

`frameborder`는 오래된 Presentational Attribute이므로 Border는 CSS로 처리한다.

## 37.10 Video 구조

두 코드 모두 같은 외부 Video URL을 사용한다.

```html
<video
    controls="controls"
    loop="loop"
    src="https://www.w3schools.com/tags/movie.mp4"
></video>
```

Boolean Attribute는 값 없이 작성할 수 있다.

```html
<video
    controls
    loop
    src="https://www.w3schools.com/tags/movie.mp4"
></video>
```

기능은 같다.

## 37.11 `controls`와 접근성

내 코드에는 다음 Comment가 있다.

```html
<!-- 웹 접근성을 용이하게 하기 위해
     controls등 옵션값은 넣어주는편이 좋음 -->
```

사용자가 직접 Play·Pause·Volume·Seek를 조작해야 하는 일반 Video에는 `controls`가 중요하다.

하지만 `controls` Attribute 하나만으로 모든 Video 접근성이 해결되는 것은 아니다.

추가로 검토할 항목:

```text
자막
→ track kind="captions"

음성 정보
→ 필요 시 Audio Description

자동 재생
→ 최소화

Keyboard 조작
→ Player 동작 확인

대체 Content
→ 지원하지 않는 Browser 안내
```

## 37.12 `loop`

두 코드 모두 `loop`를 사용한다.

```html
<video controls loop>
```

반복 재생이 학습 목적에는 문제 없지만 긴 영상이나 중요한 Content에서는 사용자의 예상과 다를 수 있다. 반복이 실제 UX 요구사항인지 확인한다.

## 37.13 외부 Video URL 의존성

두 코드 모두 다음 외부 Resource를 직접 사용한다.

```html
src="https://www.w3schools.com/tags/movie.mp4"
```

학습 예제로는 편리하지만 실제 Project에서는 다음을 고려한다.

```text
외부 Site의 파일 삭제·변경
Traffic·Hotlink 정책
Network Latency
CORS·CSP
사용 권한
```

Project가 관리하는 Storage·CDN을 사용하는 편이 예측 가능하다.

## 37.14 내 코드와 강사님 코드 비교 요약

| 항목 | 내 코드 | 강사님 코드 | 개선 기준 |
| --- | --- | --- | --- |
| 복원 메모 | 있음 | 없음 | 작업 기록과 학습 내용 분리 |
| `alt` 설명 | 상세 | Markup만 있음 | Image 목적·정보를 대체하는 Text |
| Image Attribute | 한 줄 | 여러 줄 | Attribute가 많으면 여러 줄 권장 |
| `width`·`height` | `200 × 300` | `200 × 300` | 원본 비율과 일치하거나 CSS로 유연 처리 |
| Browser Loading 설명 | 있음 | 없음 | Request·Decode·Paint 흐름으로 보완 |
| `<br>` | 사용 | 사용 | Layout 간격은 CSS |
| `iframe` | Comment 예제 있음 | 없음 | Embedded Browsing Context로 설명 |
| `video controls` | 접근성 Comment 있음 | Markup만 있음 | Control·Caption 등 종합 검토 |
| Boolean Attribute | `controls="controls"` | `controls="controls"` | `controls`처럼 축약 가능 |
| 외부 Video URL | 사용 | 사용 | 안정성·권한·성능 확인 |
| `lang` | `en` | `en` | 한국어 문서는 `ko` |

# 38. 개선된 전체 예제

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>이미지와 미디어 실습</title>
  <style>
    .media-list {
      display: grid;
      gap: 24px;
      max-width: 800px;
      margin: 40px auto;
    }

    .media-list img,
    .media-list video {
      max-width: 100%;
      height: auto;
    }
  </style>
</head>
<body>
  <main class="media-list">
    <figure>
      <img
        src="asset/Spongebob-Christmas-PNG-Picture.png"
        alt="스폰지밥이 웃고 있는 모습"
        width="500"
        height="500"
      >
      <figcaption>로컬 이미지 파일 연결 예제</figcaption>
    </figure>

    <video controls loop width="640" poster="asset/video-poster.jpg">
      <source src="https://www.w3schools.com/tags/movie.mp4" type="video/mp4">
      동영상을 재생할 수 없는 브라우저입니다.
    </video>
  </main>
</body>
</html>
```

`width`와 `height` 값은 실제 이미지 원본 크기에 맞춰 수정해야 합니다.

# 39. 실무 예제: 프로필 이미지

```html
<article class="profile-card">
  <img
    class="profile-card__image"
    src="asset/profile-kim.jpg"
    alt="김개발 프로필 사진"
    width="320"
    height="320"
  >
  <div>
    <h2>김개발</h2>
    <p>프론트엔드 개발자</p>
  </div>
</article>
```

```css
.profile-card {
  display: flex;
  align-items: center;
  gap: 16px;
}

.profile-card__image {
  width: 96px;
  height: 96px;
  border-radius: 50%;
  object-fit: cover;
}
```

# 40. 실무 예제: 상품 카드

```html
<article class="product-card">
  <a href="product-detail.html">
    <img
      src="asset/notebook.jpg"
      alt="검은색 14인치 노트북"
      width="640"
      height="480"
      loading="lazy"
    >
    <h2>개발자용 노트북</h2>
    <p>1,290,000원</p>
  </a>
</article>
```

이미지 대체 텍스트는 상품명과 완전히 같은 문장을 기계적으로 반복하기보다 사용자가 구분하는 데 필요한 시각 정보를 포함할 수 있습니다.

# 41. 실무 예제: 포트폴리오 프로젝트

```html
<article class="project-card">
  <figure>
    <img
      src="asset/project-dashboard.webp"
      alt="매출 그래프와 주문 현황을 보여주는 쇼핑몰 관리자 대시보드"
      width="1200"
      height="675"
      loading="lazy"
    >
    <figcaption>Spring Boot와 React로 제작한 쇼핑몰 관리자 화면</figcaption>
  </figure>

  <h2>쇼핑몰 관리 시스템</h2>
  <p>상품, 주문, 회원 통계를 관리하는 웹 애플리케이션입니다.</p>
</article>
```

# 42. 실무 예제: 반응형 배너

```html
<picture>
  <source
    media="(min-width: 1024px)"
    srcset="asset/course-banner-desktop.webp"
  >
  <source
    media="(min-width: 600px)"
    srcset="asset/course-banner-tablet.webp"
  >
  <img
    src="asset/course-banner-mobile.webp"
    alt="AI Agent·RAG 기반 지능형 서비스 개발 과정 수강생 모집"
    width="750"
    height="1000"
  >
</picture>
```

모바일과 데스크톱에서 단순히 크기만 다른 것이 아니라 이미지 구도 자체를 바꾸는 아트 디렉션에 적합합니다.

# 43. 실무 예제: 강의 영상

```html
<section aria-labelledby="lecture-title">
  <h2 id="lecture-title">HTML 이미지와 미디어</h2>

  <video
    controls
    poster="asset/html-media-poster.jpg"
    preload="metadata"
    width="1280"
    height="720"
  >
    <source src="asset/html-media.webm" type="video/webm">
    <source src="asset/html-media.mp4" type="video/mp4">
    <track
      kind="subtitles"
      src="asset/html-media-ko.vtt"
      srclang="ko"
      label="한국어"
      default
    >
    브라우저가 영상 재생을 지원하지 않습니다.
  </video>
</section>
```

# 44. 자주 하는 실수

## 44.1 `src` 경로 오류

```html
<img src="assets/photo.png" alt="예제 사진">
```

실제 폴더명이 `asset`이라면 이미지가 표시되지 않습니다.

```html
<img src="asset/photo.png" alt="예제 사진">
```

## 44.2 `alt` 생략

```html
<img src="asset/profile.jpg">
```

```html
<img src="asset/profile.jpg" alt="홍길동 프로필 사진">
```

## 44.3 의미 없는 대체 텍스트

```html
<img src="asset/chart.png" alt="이미지">
```

```html
<img src="asset/chart.png" alt="1월부터 6월까지 가입자가 지속적으로 증가한 그래프">
```

## 44.4 파일 경로를 로컬 절대 경로로 작성

```html
<img src="D:\workspace\asset\photo.png" alt="예제 사진">
```

이 경로는 다른 컴퓨터나 서버에서 동작하지 않습니다.

```html
<img src="asset/photo.png" alt="예제 사진">
```

## 44.5 원본 비율과 다른 크기 강제 지정

```html
<img src="asset/banner.jpg" alt="과정 모집 배너" width="800" height="800">
```

```css
img {
  max-width: 100%;
  height: auto;
}
```

## 44.6 `br`을 레이아웃 간격으로 반복 사용

```html
<img src="asset/a.png" alt="A">
<br><br><br>
<img src="asset/b.png" alt="B">
```

```css
.gallery {
  display: grid;
  gap: 32px;
}
```

## 44.7 `iframe`에 `title` 누락

```html
<iframe src="https://www.youtube.com/embed/VIDEO_ID"></iframe>
```

```html
<iframe
  src="https://www.youtube.com/embed/VIDEO_ID"
  title="프로젝트 시연 영상">
</iframe>
```

## 44.8 영상 자동 재생 남용

소리가 갑자기 재생되면 사용자 경험과 접근성을 해칠 수 있습니다.

## 44.9 너무 큰 이미지 파일 사용

화면 표시 크기에 맞는 파일과 적절한 압축을 사용합니다.

# 45. 디버깅 체크리스트

이미지가 보이지 않을 때 다음 순서로 확인합니다.

1. 파일명이 정확한가?
2. 확장자가 정확한가?
3. 대소문자가 일치하는가?
4. 현재 HTML 파일 기준 경로가 맞는가?
5. 이미지 파일이 실제 폴더에 존재하는가?
6. 개발자 도구 Network 탭에서 `404`가 발생하는가?
7. 파일명에 공백이나 특수문자가 있는가?
8. 외부 URL의 접근 권한이 허용되는가?

영상이 재생되지 않을 때 확인합니다.

1. 파일 형식을 브라우저가 지원하는가?
2. `source`의 `type`이 올바른가?
3. 서버가 파일을 전달할 수 있는가?
4. 외부 서버에서 직접 연결을 차단하지 않는가?
5. 자동 재생 정책에 막힌 것은 아닌가?
6. 콘솔에 미디어 오류가 표시되는가?

# 46. 접근성 체크리스트

- 의미 있는 이미지에 적절한 `alt`가 있는가?
- 장식용 이미지에는 `alt=""`가 있는가?
- 링크 이미지의 대체 텍스트가 목적을 설명하는가?
- 영상에 `controls`가 제공되는가?
- 영상에 자막 또는 대체 콘텐츠가 있는가?
- `iframe`에 설명 가능한 `title`이 있는가?
- 자동 재생되는 콘텐츠를 멈출 수 있는가?
- 움직이는 배경이 텍스트 가독성을 해치지 않는가?
- 색상만으로 이미지 정보를 전달하지 않는가?

# 47. 성능 체크리스트

- 실제 표시 크기에 맞는 이미지인가?
- 압축된 파일인가?
- 최신 형식 제공을 검토했는가?
- 화면 아래 이미지는 지연 로딩할 수 있는가?
- 첫 화면 핵심 이미지는 지나치게 늦게 불러오지 않는가?
- `width`와 `height`로 공간을 예약했는가?
- 불필요한 외부 `iframe`이 여러 개 로드되지 않는가?
- 영상의 `preload` 설정이 적절한가?


# 48. 종합실습

## 문제 1. 기본 이미지 작성

`asset/logo.png` 파일을 표시하는 이미지를 작성하세요. 대체 텍스트는 `ABC 서비스 로고`입니다.

## 문제 2. 경로 수정

다음 폴더 구조에서 `pages/about.html`이 `asset/team.jpg`를 표시하도록 코드를 작성하세요.

```text
project/
├─ asset/
│  └─ team.jpg
└─ pages/
   └─ about.html
```

## 문제 3. 잘못된 대체 텍스트 개선

다음 코드를 개선하세요.

```html
<img src="asset/chart.png" alt="이미지">
```

그래프는 1월부터 6월까지 월별 가입자가 계속 증가하는 내용을 담고 있습니다.

## 문제 4. 장식용 이미지

단순 구분선 역할의 `asset/divider.svg`를 접근성에 맞게 작성하세요.

## 문제 5. 이미지 비율 유지

다음 CSS를 원본 비율이 유지되도록 수정하세요.

```css
.course-image {
  width: 400px;
  height: 400px;
}
```

이미지를 잘라내지 않고 전체가 보이게 해야 합니다.

## 문제 6. 프로필 이미지

`asset/profile.jpg`를 `120 × 120` 원형 프로필로 만들고, 영역을 채우되 이미지 비율을 유지하도록 HTML과 CSS를 작성하세요.

## 문제 7. `figure` 작성

`asset/dashboard.png`와 `쇼핑몰 관리자 대시보드`라는 캡션을 하나의 콘텐츠 단위로 작성하세요. 대체 텍스트에는 `매출과 주문 통계를 보여주는 관리자 화면`을 사용합니다.

## 문제 8. 여러 영상 형식

`asset/demo.webm`과 `asset/demo.mp4`를 순서대로 제공하는 `video`를 작성하세요. 기본 재생 조작 UI가 있어야 합니다.

## 문제 9. 자막 추가

문제 8의 영상에 한국어 자막 `asset/demo-ko.vtt`를 기본 자막으로 추가하세요.

## 문제 10. 반응형 유튜브 영상

`iframe`을 16:9 비율로 반응형 처리하는 HTML과 CSS를 작성하세요. `title`은 `프로젝트 시연 영상`입니다.

## 문제 11. 코드 오류 찾기

다음 코드의 문제점을 세 가지 이상 설명하세요.

```html
<img src="D:\workspace\images\banner.jpg" alt="사진" width="500" height="500">
<br><br><br>
<iframe src="https://www.youtube.com/embed/VIDEO_ID"></iframe>
```

## 문제 12. 반응형 이미지

화면 너비가 `1024px` 이상이면 `banner-large.jpg`, `600px` 이상이면 `banner-medium.jpg`, 그보다 작으면 `banner-small.jpg`를 사용하도록 작성하세요.

## 문제 13. 지연 로딩 판단

다음 이미지 중 `loading="lazy"`를 적용하기에 더 적절한 이미지를 고르고 이유를 설명하세요.

1. 첫 화면 상단의 메인 배너
2. 페이지 아래쪽 프로젝트 목록의 15번째 썸네일

## 문제 14. 내 코드 개선

원본 실습의 이미지와 영상 코드를 다음 기준으로 개선하세요.

- `lang="ko"`
- 자연스러운 대체 텍스트
- 이미지 비율 유지
- 불리언 속성 간소화
- `br` 대신 CSS 간격
- 반응형 크기

# 49. 정답과 해설

## 정답 1

```html
<img src="asset/logo.png" alt="ABC 서비스 로고">
```

`src`에는 파일 경로, `alt`에는 이미지 의미를 작성합니다.

## 정답 2

```html
<img src="../asset/team.jpg" alt="프로젝트 회의 중인 개발팀">
```

`about.html`은 `pages` 폴더 안에 있으므로 `..`로 상위 폴더에 이동한 뒤 `asset`으로 들어갑니다.

## 정답 3

```html
<img
  src="asset/chart.png"
  alt="1월부터 6월까지 월별 가입자가 계속 증가한 그래프"
>
```

`이미지`라는 표현만으로는 콘텐츠 의미를 알 수 없습니다.

## 정답 4

```html
<img src="asset/divider.svg" alt="">
```

장식용 이미지는 빈 대체 텍스트를 사용합니다.

## 정답 5

```css
.course-image {
  width: 400px;
  height: auto;
}
```

높이를 자동 계산하면 원본 비율이 유지됩니다.

## 정답 6

```html
<img
  class="profile-image"
  src="asset/profile.jpg"
  alt="홍길동 프로필 사진"
  width="400"
  height="400"
>
```

```css
.profile-image {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  object-fit: cover;
}
```

`object-fit: cover`는 비율을 유지하면서 영역을 채웁니다.

## 정답 7

```html
<figure>
  <img
    src="asset/dashboard.png"
    alt="매출과 주문 통계를 보여주는 관리자 화면"
  >
  <figcaption>쇼핑몰 관리자 대시보드</figcaption>
</figure>
```

## 정답 8

```html
<video controls>
  <source src="asset/demo.webm" type="video/webm">
  <source src="asset/demo.mp4" type="video/mp4">
  브라우저가 영상을 재생할 수 없습니다.
</video>
```

브라우저는 위에서부터 재생 가능한 형식을 찾습니다.

## 정답 9

```html
<video controls>
  <source src="asset/demo.webm" type="video/webm">
  <source src="asset/demo.mp4" type="video/mp4">
  <track
    kind="subtitles"
    src="asset/demo-ko.vtt"
    srclang="ko"
    label="한국어"
    default
  >
  브라우저가 영상을 재생할 수 없습니다.
</video>
```

## 정답 10

```html
<div class="video-frame">
  <iframe
    src="https://www.youtube.com/embed/VIDEO_ID"
    title="프로젝트 시연 영상"
    allowfullscreen>
  </iframe>
</div>
```

```css
.video-frame {
  width: 100%;
  aspect-ratio: 16 / 9;
}

.video-frame iframe {
  width: 100%;
  height: 100%;
  border: 0;
}
```

## 정답 11

문제점은 다음과 같습니다.

1. `D:\workspace\...`는 작성자 컴퓨터에서만 유효한 로컬 절대 경로입니다.
2. `alt="사진"`은 이미지 내용을 설명하지 못합니다.
3. 원본 비율을 확인하지 않고 `500 × 500`을 강제하면 이미지가 왜곡될 수 있습니다.
4. 디자인 간격을 위해 `br`을 반복 사용했습니다.
5. `iframe`에 `title`이 없습니다.
6. 고정 크기만 사용하면 모바일 화면 대응이 부족할 수 있습니다.

개선 예시는 다음과 같습니다.

```html
<div class="content-media">
  <img
    src="asset/banner.jpg"
    alt="AI 서비스 개발 과정 모집 배너"
    width="1200"
    height="600"
  >

  <div class="video-frame">
    <iframe
      src="https://www.youtube.com/embed/VIDEO_ID"
      title="과정 소개 영상"
      allowfullscreen>
    </iframe>
  </div>
</div>
```

```css
.content-media {
  display: grid;
  gap: 32px;
}

.content-media img {
  max-width: 100%;
  height: auto;
}
```

## 정답 12

```html
<picture>
  <source media="(min-width: 1024px)" srcset="asset/banner-large.jpg">
  <source media="(min-width: 600px)" srcset="asset/banner-medium.jpg">
  <img src="asset/banner-small.jpg" alt="AI 과정 모집 배너">
</picture>
```

## 정답 13

페이지 아래쪽의 15번째 프로젝트 썸네일이 더 적절합니다.

초기 화면에 바로 보이지 않으므로 사용자가 가까이 스크롤했을 때 불러와도 됩니다. 반면 첫 화면 메인 배너를 지연 로딩하면 주요 콘텐츠가 늦게 나타날 수 있습니다.

## 정답 14

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>이미지와 미디어 실습</title>
  <style>
    .media-list {
      display: grid;
      gap: 24px;
      max-width: 800px;
      margin: 40px auto;
    }

    .media-list img,
    .media-list video {
      display: block;
      max-width: 100%;
      height: auto;
    }
  </style>
</head>
<body>
  <main class="media-list">
    <img
      src="asset/Spongebob-Christmas-PNG-Picture.png"
      alt="스폰지밥이 웃고 있는 모습"
    >

    <video controls loop>
      <source src="https://www.w3schools.com/tags/movie.mp4" type="video/mp4">
      브라우저가 동영상을 재생할 수 없습니다.
    </video>
  </main>
</body>
</html>
```


# 50. 최종 체크리스트

- [ ] 정보성 Image에 목적을 설명하는 `alt`를 제공하는가?
- [ ] 장식용 Image에는 상황에 맞게 `alt=""`를 사용하는가?
- [ ] File Name 자체를 `alt`로 사용하지 않는가?
- [ ] Link Image의 `alt`가 이동 목적을 설명하는가?
- [ ] Image `src` 경로를 현재 HTML File 위치 기준으로 계산했는가?
- [ ] 외부 Image URL의 변경·삭제·사용 권한 문제를 고려하는가?
- [ ] 원본 비율과 다른 Width·Height를 동시에 강제하지 않는가?
- [ ] Layout Shift를 줄이기 위해 실제 비율에 맞는 `width`·`height` Attribute 제공을 검토했는가?
- [ ] CSS에서 반응형 Image에 `max-width: 100%`, `height: auto`를 검토했는가?
- [ ] `figure`와 `figcaption`이 실제 Caption 관계일 때 사용하는가?
- [ ] 화면 조건에 따라 다른 Image가 필요하면 `picture`를 검토했는가?
- [ ] 해상도별 Image가 필요하면 `srcset`을 검토했는가?
- [ ] 첫 화면 핵심 Image에 무조건 `loading="lazy"`를 적용하지 않는가?
- [ ] 일반 Video에 사용자가 조작할 수 있는 `controls`를 제공하는가?
- [ ] Video에 자막이 필요하면 `track`을 제공하는가?
- [ ] 자동 재생을 꼭 필요한 경우에만 사용하는가?
- [ ] `loop`가 실제 UX 요구사항인지 확인했는가?
- [ ] 여러 Video Format이 필요하면 `source` Element를 사용하는가?
- [ ] `iframe`에 내용을 설명하는 `title`을 제공하는가?
- [ ] 외부 Embed가 CSP·X-Frame-Options로 차단될 수 있음을 고려하는가?
- [ ] `frameborder` 같은 오래된 Presentational Attribute 대신 CSS를 사용하는가?
- [ ] 반복 `<br>`로 Media 간격을 만들지 않는가?
- [ ] 외부 Media의 성능·권한·안정성을 확인하는가?
- [ ] 한국어 문서라면 `lang="ko"`를 사용하는가?

---

# 51. 핵심 요약

- `img`는 이미지를 표시하는 빈 요소입니다.
- `src`에는 이미지 파일의 경로를 작성합니다.
- `alt`는 이미지가 전달하는 의미를 대신하는 텍스트입니다.
- 장식용 이미지는 `alt=""`로 작성합니다.
- `width`와 `height`를 함께 지정할 때는 원본 비율을 확인해야 합니다.
- 반응형 이미지의 기본은 `max-width: 100%`, `height: auto`입니다.
- 일정한 썸네일 영역에는 `object-fit`을 활용할 수 있습니다.
- `figure`와 `figcaption`은 이미지와 캡션을 하나의 단위로 묶습니다.
- `picture`, `source`, `srcset`은 조건에 맞는 이미지 파일 선택에 사용합니다.
- `loading="lazy"`는 화면 아래 이미지의 초기 로딩 부담을 줄일 수 있습니다.
- `video`와 `audio`에는 사용자가 조작할 수 있는 `controls`를 제공하는 것이 좋습니다.
- 영상에는 자막과 대체 콘텐츠를 검토해야 합니다.
- `iframe`은 외부 문서를 삽입하며 `title`, 반응형 처리, 권한과 보안을 함께 확인해야 합니다.
- `br`은 문장 안의 의미 있는 줄바꿈에 사용하고 디자인 간격은 CSS로 처리합니다.
- 이미지와 미디어는 마크업뿐 아니라 접근성, 성능, 반응형 디자인을 함께 고려해야 합니다.
