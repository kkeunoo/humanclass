---
title: HTML 시맨틱 태그와 페이지 구조
version: v2.0-final
last_updated: 2026-08-07
status: Completed
---

# HTML 시맨틱 태그와 페이지 구조

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `08_HTML_시맨틱태그와_페이지구조.md` |
| 분류 | `01_HTML` |
| 원본 기준 | 독립된 `08_*.html` 원본 없음 — HTML 01~07 학습 내용을 연결한 확장 단원 |
| 핵심 범위 | Semantic HTML, `header`, `nav`, `main`, `section`, `article`, `aside`, `footer`, Heading Structure, Landmark, 접근성 |
| 학습 범위 | Page 구조, 콘텐츠 영역 구분, 문서 제목 계층, Navigation·Article·Aside 선택 기준 |
| 프로젝트 연결 | Landing Page, Blog, News, Portfolio, 관리자 화면, 반응형 Web Layout |
| 문서 형식 | HTML Developer-Wiki V2 확정 형식 |

> HTML 수업 원본에는 독립된 `08_*.html` 파일이 없다. 따라서 이 문서는 존재하지 않는 내 코드·강사님 코드 차이를 만들지 않고 HTML 01~07에서 학습한 Heading, Link, List, Table, Media, Form 구조를 실제 Page 골격으로 연결한다. Semantic Element를 많이 쓰는 것보다 콘텐츠의 역할에 맞는 Element를 선택하고 Heading·Landmark·접근성 구조를 일관되게 만드는 것을 목표로 한다.

# 학습 목표

- 시맨틱 HTML의 의미와 필요성을 설명한다.
- `div`와 시맨틱 요소의 차이를 구분한다.
- `header`, `nav`, `main`, `section`, `article`, `aside`, `footer`의 역할을 설명한다.
- 페이지 전체 영역과 콘텐츠 내부 영역을 구분한다.
- 제목 태그를 문서 구조에 맞게 배치한다.
- 같은 시맨틱 요소를 여러 번 사용할 수 있는 경우를 이해한다.
- 랜드마크와 접근성의 관계를 이해한다.
- 목적에 맞는 HTML 요소를 선택한다.
- 실무형 페이지 골격을 작성한다.
- 잘못된 시맨틱 구조를 찾아 개선한다.
- CSS를 적용하기 전에도 의미가 분명한 마크업을 작성한다.

# 1. 시맨틱 HTML이란?

`semantic`은 “의미가 있는”이라는 뜻입니다.

시맨틱 HTML은 요소의 이름만 보고도 해당 콘텐츠의 역할을 이해할 수 있도록 작성하는 방식입니다.

다음 두 코드를 비교해 봅니다.

```html
<div class="header">
  <div class="logo">Developer Wiki</div>
</div>
```

```html
<header>
  <h1>Developer Wiki</h1>
</header>
```

두 코드 모두 CSS로 비슷하게 보이게 만들 수 있습니다.

그러나 두 번째 코드는 요소 자체가 페이지의 머리말 영역이라는 의미를 전달합니다.

시맨틱 HTML은 다음 대상에게 구조를 설명합니다.

- 개발자
- 브라우저
- 검색 엔진
- 스크린 리더
- 유지보수 도구
- 자동 분석 프로그램

# 2. 모양과 의미는 다르다

HTML은 콘텐츠의 의미와 구조를 담당합니다.

CSS는 화면에 보이는 모양을 담당합니다.

```html
<header class="site-header">
  <h1>Developer Wiki</h1>
</header>
```

```css
.site-header {
  display: flex;
  align-items: center;
  min-height: 80px;
}
```

`header`를 사용했다고 해서 자동으로 특정 색상이나 높이가 적용되는 것은 아닙니다.

반대로 `div`를 화면 위쪽에 배치했다고 해서 의미상 `header`가 되는 것도 아닙니다.

| 구분 | HTML | CSS |
| --- | --- | --- |
| 역할 | 의미와 구조 | 디자인과 배치 |
| 예 | 제목, 내비게이션, 본문 | 색상, 크기, 정렬 |
| 질문 | “이 콘텐츠는 무엇인가?” | “어떻게 보일 것인가?” |

# 3. 시맨틱 요소를 사용하는 이유

## 3.1 코드 이해가 쉬워진다

```html
<header>...</header>
<nav>...</nav>
<main>...</main>
<footer>...</footer>
```

클래스명을 자세히 읽지 않아도 페이지의 큰 구조를 파악할 수 있습니다.

## 3.2 유지보수가 쉬워진다

여러 개발자가 작업할 때 영역의 목적이 명확하면 수정 범위를 찾기 쉽습니다.

## 3.3 접근성이 좋아진다

스크린 리더 사용자는 랜드마크를 기준으로 주요 영역을 빠르게 이동할 수 있습니다.

## 3.4 검색 엔진이 문맥을 이해하는 데 도움을 준다

검색 엔진은 제목, 본문, 내비게이션, 독립 콘텐츠의 관계를 분석할 때 시맨틱 구조를 참고할 수 있습니다.

시맨틱 요소를 사용한다고 검색 순위가 자동으로 높아지는 것은 아니지만, 문서 구조를 명확하게 만드는 기본 요소입니다.

# 4. `div`는 잘못된 요소인가?

아닙니다.

`div`는 특별한 의미가 없는 일반 컨테이너입니다.

```html
<div class="card">
  <h2>HTML</h2>
  <p>웹 문서의 구조를 작성합니다.</p>
</div>
```

다음과 같은 경우 `div`가 적절합니다.

- CSS 배치를 위한 묶음
- 디자인 컴포넌트의 내부 래퍼
- 의미 있는 시맨틱 요소가 따로 없는 영역
- JavaScript 제어를 위한 일반 컨테이너

문제는 모든 영역을 이유 없이 `div`로만 작성하는 것입니다.

```html
<div class="header">
  <div class="nav">
    <div class="menu">HTML</div>
  </div>
</div>
```

다음처럼 역할에 맞는 요소를 우선 검토합니다.

```html
<header>
  <nav aria-label="주요 메뉴">
    <a href="/html">HTML</a>
  </nav>
</header>
```

# 5. 페이지의 기본 골격

대표적인 시맨틱 페이지 구조는 다음과 같습니다.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
  >
  <title>Developer Wiki</title>
</head>
<body>
  <header>
    <h1>Developer Wiki</h1>

    <nav aria-label="주요 메뉴">
      <ul>
        <li><a href="#html">HTML</a></li>
        <li><a href="#css">CSS</a></li>
        <li><a href="#javascript">JavaScript</a></li>
      </ul>
    </nav>
  </header>

  <main>
    <section id="html">
      <h2>HTML</h2>
      <p>웹 문서의 구조와 의미를 작성합니다.</p>
    </section>

    <section id="css">
      <h2>CSS</h2>
      <p>웹 문서의 디자인과 배치를 담당합니다.</p>
    </section>

    <section id="javascript">
      <h2>JavaScript</h2>
      <p>웹페이지에 동작과 상호작용을 추가합니다.</p>
    </section>
  </main>

  <footer>
    <p>&copy; 2026 Developer Wiki</p>
  </footer>
</body>
</html>
```

이 구조가 모든 페이지의 정답은 아닙니다.

페이지의 콘텐츠와 목적에 따라 필요한 요소만 선택합니다.

# 6. `header`

`header`는 페이지나 콘텐츠 구역의 머리말을 나타냅니다.

페이지 전체의 `header` 예시:

```html
<header class="site-header">
  <h1>Developer Wiki</h1>

  <nav aria-label="주요 메뉴">
    <a href="/">홈</a>
    <a href="/docs">문서</a>
  </nav>
</header>
```

`article` 내부의 `header` 예시:

```html
<article>
  <header>
    <h2>HTML 시맨틱 태그</h2>
    <p>작성일: 2026-07-28</p>
  </header>

  <p>시맨틱 HTML은 콘텐츠의 의미를 표현합니다.</p>
</article>
```

따라서 한 문서에 `header`가 여러 개 존재할 수 있습니다.

중요한 것은 각 `header`가 어느 영역의 머리말인지 구조상 분명해야 한다는 점입니다.

# 7. `nav`

`nav`는 주요 탐색 링크 묶음을 나타냅니다.

```html
<nav aria-label="주요 메뉴">
  <ul>
    <li><a href="/">홈</a></li>
    <li><a href="/html">HTML</a></li>
    <li><a href="/css">CSS</a></li>
  </ul>
</nav>
```

모든 링크를 `nav`로 감싸는 것은 아닙니다.

다음은 일반 문장 속 링크이므로 별도의 `nav`가 필요하지 않습니다.

```html
<p>
  자세한 내용은
  <a href="/guide">사용 가이드</a>를 확인하세요.
</p>
```

`nav`가 적합한 예:

- 사이트 주요 메뉴
- 문서 목차
- 페이지네이션
- 사이드 메뉴
- 이전 글·다음 글 탐색

# 8. 여러 개의 `nav`

한 페이지에 여러 내비게이션이 존재할 수 있습니다.

```html
<header>
  <nav aria-label="주요 메뉴">
    <!-- 사이트 전체 메뉴 -->
  </nav>
</header>

<aside>
  <nav aria-label="HTML 문서 목차">
    <!-- 현재 문서의 목차 -->
  </nav>
</aside>

<footer>
  <nav aria-label="하단 메뉴">
    <!-- 이용약관, 개인정보처리방침 -->
  </nav>
</footer>
```

여러 `nav`가 있다면 `aria-label` 또는 연결된 제목으로 각각의 목적을 구분하는 것이 좋습니다.

# 9. `main`

`main`은 문서의 핵심 콘텐츠를 나타냅니다.

```html
<main>
  <h1>HTML 학습 문서</h1>
  <p>HTML의 핵심 개념을 정리합니다.</p>
</main>
```

일반적인 페이지에서는 보이는 핵심 콘텐츠를 담는 `main`을 하나 사용합니다.

다음 요소는 보통 `main` 바깥에 둡니다.

- 사이트 공통 헤더
- 사이트 공통 내비게이션
- 사이트 공통 푸터
- 반복되는 사이드 메뉴

```html
<header>사이트 공통 헤더</header>

<main>
  페이지별 핵심 콘텐츠
</main>

<footer>사이트 공통 푸터</footer>
```

`main`을 `article`, `aside`, `footer`, `header`, `nav` 안에 넣는 구조는 피합니다.

# 10. `section`

`section`은 하나의 주제를 가진 콘텐츠 구역입니다.

```html
<section>
  <h2>학습 목표</h2>
  <ul>
    <li>시맨틱 태그를 이해한다.</li>
    <li>페이지 구조를 작성한다.</li>
  </ul>
</section>
```

`section`은 단순히 CSS를 적용하기 위한 묶음이 아닙니다.

다음 질문으로 판단할 수 있습니다.

> 이 영역에 자연스러운 제목을 붙일 수 있는가?

제목을 붙일 수 있는 독립된 주제라면 `section`을 검토합니다.

단지 레이아웃을 위한 내부 래퍼라면 `div`가 더 적절할 수 있습니다.

```html
<section>
  <h2>추천 강의</h2>

  <div class="card-list">
    <!-- 레이아웃용 묶음 -->
  </div>
</section>
```

# 11. `section`과 제목

`section`에는 내용을 설명하는 제목을 제공하는 것이 좋습니다.

```html
<section>
  <h2>수강 후기</h2>
  <p>수강생의 후기를 확인할 수 있습니다.</p>
</section>
```

다음처럼 제목 없이 여러 `section`을 반복하면 각 구역의 의미가 불분명해질 수 있습니다.

```html
<section>
  <p>내용 1</p>
</section>

<section>
  <p>내용 2</p>
</section>
```

제목을 시각적으로 숨겨야 하는 디자인이라도 접근 가능한 제목을 제공하는 방법을 고려합니다.

```html
<section aria-labelledby="notice-title">
  <h2 id="notice-title" class="sr-only">공지사항</h2>
  <!-- 공지 목록 -->
</section>
```

# 12. `article`

`article`은 독립적으로 배포하거나 재사용할 수 있는 콘텐츠를 나타냅니다.

대표적인 예:

- 블로그 글
- 뉴스 기사
- 게시글
- 상품 리뷰
- 포럼 글
- 독립된 카드형 콘텐츠

```html
<article>
  <h2>HTML 시맨틱 태그 정리</h2>
  <p>시맨틱 요소의 역할을 알아봅니다.</p>
  <a href="/posts/semantic-html">글 읽기</a>
</article>
```

이 콘텐츠만 RSS, 검색 결과, 다른 페이지 카드로 옮겨도 의미가 유지된다면 `article`이 적합할 가능성이 높습니다.

# 13. `section`과 `article` 비교

| 구분 | `section` | `article` |
| --- | --- | --- |
| 핵심 기준 | 하나의 주제 구역 | 독립적으로 재사용 가능한 콘텐츠 |
| 제목 | 일반적으로 필요 | 일반적으로 필요 |
| 대표 예 | 소개, 기능, 후기 구역 | 게시글, 뉴스, 리뷰 |
| 독립 배포 | 필수 아님 | 가능해야 함 |

블로그 목록 예시:

```html
<section aria-labelledby="latest-posts-title">
  <h2 id="latest-posts-title">최신 글</h2>

  <article>
    <h3>HTML 기초</h3>
    <p>HTML 문서 구조를 학습합니다.</p>
  </article>

  <article>
    <h3>CSS 선택자</h3>
    <p>선택자의 종류를 학습합니다.</p>
  </article>
</section>
```

전체 목록은 하나의 주제이므로 `section`, 각각의 글은 독립 콘텐츠이므로 `article`을 사용했습니다.

# 14. `aside`

`aside`는 본문과 관련은 있지만 핵심 흐름에서 분리할 수 있는 보조 콘텐츠입니다.

```html
<aside>
  <h2>관련 문서</h2>
  <ul>
    <li><a href="/html/basic">HTML 기초</a></li>
    <li><a href="/html/forms">HTML 폼</a></li>
  </ul>
</aside>
```

대표적인 용도:

- 관련 글
- 광고
- 용어 설명
- 보조 팁
- 작성자 정보
- 사이드바

페이지 전체의 사이드바뿐 아니라 `article` 내부의 보조 설명에도 사용할 수 있습니다.

```html
<article>
  <h2>폼 데이터 전송</h2>
  <p>GET과 POST의 차이를 학습합니다.</p>

  <aside>
    <h3>참고</h3>
    <p>POST도 HTTPS가 없으면 자동으로 안전하지 않습니다.</p>
  </aside>
</article>
```

# 15. `footer`

`footer`는 페이지 또는 콘텐츠 구역의 바닥글을 나타냅니다.

페이지 전체의 `footer`:

```html
<footer class="site-footer">
  <p>&copy; 2026 Developer Wiki</p>
  <a href="/privacy">개인정보처리방침</a>
</footer>
```

`article` 내부의 `footer`:

```html
<article>
  <h2>시맨틱 HTML</h2>
  <p>본문 내용...</p>

  <footer>
    <p>작성자: 홍길동</p>
    <a href="/tags/html">HTML 태그 모아보기</a>
  </footer>
</article>
```

한 페이지에 `footer`도 여러 개 존재할 수 있습니다.

# 16. 같은 태그를 여러 번 사용해도 되는가?

일부 시맨틱 요소는 문맥에 따라 여러 번 사용할 수 있습니다.

| 요소 | 여러 번 사용 | 설명 |
| --- | --- | --- |
| `header` | 가능 | 페이지 또는 각 구역의 머리말 |
| `nav` | 가능 | 목적이 다른 탐색 영역 |
| `section` | 가능 | 서로 다른 주제 구역 |
| `article` | 가능 | 여러 독립 콘텐츠 |
| `aside` | 가능 | 여러 보조 콘텐츠 |
| `footer` | 가능 | 페이지 또는 각 구역의 바닥글 |
| `main` | 일반적으로 하나 | 페이지의 핵심 콘텐츠 |

태그 개수만 외우기보다 요소가 어떤 콘텐츠 범위에 속하는지 이해해야 합니다.

# 17. 제목 태그와 문서 구조

제목 태그는 `h1`부터 `h6`까지 있습니다.

```html
<h1>페이지 제목</h1>
<h2>주요 장</h2>
<h3>하위 절</h3>
```

숫자는 글자 크기가 아니라 구조의 깊이를 나타냅니다.

```html
<h1>HTML</h1>

<section>
  <h2>시맨틱 태그</h2>

  <section>
    <h3>header</h3>
  </section>
</section>
```

CSS로 제목 크기를 자유롭게 조절할 수 있으므로 디자인 때문에 제목 단계를 건너뛰지 않습니다.

```html
<!-- 구조상 권장하지 않음 -->
<h1>HTML</h1>
<h4>시맨틱 태그</h4>
```

```html
<!-- 자연스러운 구조 -->
<h1>HTML</h1>
<h2>시맨틱 태그</h2>
```

# 18. `h1` 사용 기준

일반적인 실무 문서에서는 페이지의 핵심 제목에 명확한 `h1` 하나를 두는 방식이 이해하기 쉽습니다.

```html
<main>
  <h1>HTML 학습 로드맵</h1>
</main>
```

로고를 무조건 `h1`으로 만들 필요는 없습니다.

```html
<header>
  <a href="/" class="logo">Developer Wiki</a>
</header>

<main>
  <h1>HTML 시맨틱 태그</h1>
</main>
```

페이지마다 실제 핵심 제목이 달라지는 구조에서는 위 방식이 더 자연스러울 수 있습니다.

# 19. 제목을 크기 때문에 선택하지 않는다

```html
<!-- 작은 글자가 필요해서 h6 사용 -->
<h6>카드 제목</h6>
```

카드가 `h2` 구조에 해당한다면 `h2`를 사용하고 CSS로 크기를 조절합니다.

```html
<h2 class="card-title">카드 제목</h2>
```

```css
.card-title {
  font-size: 1rem;
}
```

의미는 HTML로, 크기는 CSS로 결정합니다.

# 20. 랜드마크란?

랜드마크는 사용자가 페이지의 주요 영역을 빠르게 파악하고 이동하도록 돕는 구조입니다.

대표적인 HTML 요소와 역할은 다음과 같습니다.

| HTML 요소 | 대표 역할 |
| --- | --- |
| `header` | 배너 또는 구역 머리말 |
| `nav` | 탐색 |
| `main` | 핵심 콘텐츠 |
| `aside` | 보조 콘텐츠 |
| `footer` | 콘텐츠 정보 또는 바닥글 |

스크린 리더 사용자는 제목과 랜드마크를 기준으로 긴 페이지를 탐색할 수 있습니다.

따라서 시맨틱 구조는 단순한 코드 취향이 아니라 사용자 경험과 연결됩니다.

# 21. `aria-label`은 언제 사용하는가?

보이는 제목이 없거나 같은 종류의 영역이 여러 개일 때 목적을 구분할 수 있습니다.

```html
<nav aria-label="주요 메뉴">
  ...
</nav>

<nav aria-label="문서 목차">
  ...
</nav>
```

보이는 제목이 있다면 `aria-labelledby`로 연결할 수도 있습니다.

```html
<aside aria-labelledby="related-title">
  <h2 id="related-title">관련 문서</h2>
  ...
</aside>
```

ARIA는 HTML의 의미를 보완하는 도구입니다.

적절한 기본 HTML 요소가 있다면 먼저 해당 요소를 사용합니다.

# 22. 시맨틱 요소와 클래스는 함께 사용할 수 있다

시맨틱 태그를 사용한다고 클래스를 사용하지 않는 것은 아닙니다.

```html
<header class="site-header">
  <nav class="global-nav" aria-label="주요 메뉴">
    ...
  </nav>
</header>
```

| 항목 | 역할 |
| --- | --- |
| 시맨틱 태그 | 콘텐츠의 의미 |
| `class` | CSS와 JavaScript에서 재사용할 식별자 |
| `id` | 문서 안에서 고유한 식별자 |

시맨틱 태그만으로 모든 스타일 대상을 구분하기 어렵기 때문에 실무에서는 클래스를 함께 사용합니다.

# 23. 나쁜 예: `div`만 사용하는 페이지

```html
<div class="page">
  <div class="top">
    <div class="title">Developer Wiki</div>

    <div class="menu">
      <div>HTML</div>
      <div>CSS</div>
      <div>JavaScript</div>
    </div>
  </div>

  <div class="content">
    <div class="content-title">HTML</div>
    <div>HTML 학습 내용</div>
  </div>

  <div class="bottom">
    Copyright
  </div>
</div>
```

문제점:

- 링크가 실제 `a` 요소가 아니다.
- 제목이 제목 태그가 아니다.
- 각 영역의 의미를 태그가 표현하지 않는다.
- 키보드 탐색과 접근성이 떨어질 수 있다.
- 유지보수자가 클래스명을 해석해야 한다.

# 24. 개선 예

```html
<header class="site-header">
  <a href="/" class="logo">Developer Wiki</a>

  <nav aria-label="주요 메뉴">
    <ul>
      <li><a href="/html">HTML</a></li>
      <li><a href="/css">CSS</a></li>
      <li><a href="/javascript">JavaScript</a></li>
    </ul>
  </nav>
</header>

<main>
  <article>
    <h1>HTML</h1>
    <p>HTML 학습 내용</p>
  </article>
</main>

<footer class="site-footer">
  <p>&copy; 2026 Developer Wiki</p>
</footer>
```

시맨틱 구조를 사용하면서 필요한 스타일 클래스도 유지했습니다.

# 25. 블로그 페이지 구조

```html
<body>
  <header class="site-header">
    <a href="/" class="logo">Dev Blog</a>

    <nav aria-label="주요 메뉴">
      <a href="/posts">글 목록</a>
      <a href="/about">소개</a>
    </nav>
  </header>

  <main class="layout">
    <article class="post">
      <header class="post-header">
        <h1>시맨틱 HTML 정리</h1>
        <p>작성일: 2026-07-28</p>
      </header>

      <section>
        <h2>시맨틱 HTML이란?</h2>
        <p>콘텐츠의 의미를 태그로 표현하는 방식입니다.</p>
      </section>

      <section>
        <h2>주요 요소</h2>
        <p>header, nav, main 등을 사용합니다.</p>
      </section>

      <footer class="post-footer">
        <p>태그: HTML, 접근성</p>
      </footer>
    </article>

    <aside class="sidebar">
      <h2>관련 글</h2>
      <ul>
        <li><a href="/posts/forms">HTML 폼</a></li>
        <li><a href="/posts/tables">HTML 테이블</a></li>
      </ul>
    </aside>
  </main>

  <footer class="site-footer">
    <p>&copy; 2026 Dev Blog</p>
  </footer>
</body>
```

# 26. 랜딩 페이지 구조

```html
<body>
  <header class="site-header">
    <a href="/" class="logo">AI Academy</a>

    <nav aria-label="주요 메뉴">
      <a href="#curriculum">교육과정</a>
      <a href="#projects">프로젝트</a>
      <a href="#reviews">수강 후기</a>
    </nav>
  </header>

  <main>
    <section class="hero" aria-labelledby="hero-title">
      <h1 id="hero-title">
        AI 서비스 개발자로 성장하세요
      </h1>
      <p>
        HTML부터 AI Agent 프로젝트까지 단계적으로 학습합니다.
      </p>
      <a href="#apply">과정 신청하기</a>
    </section>

    <section id="curriculum">
      <h2>교육과정</h2>
      <!-- 과정 카드 -->
    </section>

    <section id="projects">
      <h2>실무 프로젝트</h2>
      <!-- 프로젝트 목록 -->
    </section>

    <section id="reviews">
      <h2>수강 후기</h2>
      <!-- 후기 목록 -->
    </section>

    <section id="apply">
      <h2>과정 신청</h2>
      <!-- 신청 폼 -->
    </section>
  </main>

  <footer>
    <p>교육 문의: example@example.com</p>
  </footer>
</body>
```

# 27. 포트폴리오 페이지 구조

```html
<header class="site-header">
  <a href="/" class="logo">홍길동 Portfolio</a>

  <nav aria-label="포트폴리오 메뉴">
    <a href="#about">소개</a>
    <a href="#skills">기술</a>
    <a href="#projects">프로젝트</a>
    <a href="#contact">연락처</a>
  </nav>
</header>

<main>
  <section id="about">
    <h1>웹 개발자 홍길동입니다</h1>
    <p>사용자 문제를 해결하는 서비스를 만듭니다.</p>
  </section>

  <section id="skills">
    <h2>기술 스택</h2>
    <!-- 기술 목록 -->
  </section>

  <section id="projects">
    <h2>프로젝트</h2>

    <article>
      <h3>Developer Wiki</h3>
      <p>학습 내용을 구조화한 개발 문서 프로젝트입니다.</p>
    </article>

    <article>
      <h3>AI FAQ 서비스</h3>
      <p>RAG 기반 질의응답 서비스입니다.</p>
    </article>
  </section>

  <section id="contact">
    <h2>연락처</h2>
    <!-- 연락 폼 -->
  </section>
</main>

<footer>
  <p>&copy; 2026 홍길동</p>
</footer>
```

# 28. 뉴스 목록 구조

```html
<main>
  <h1>최신 뉴스</h1>

  <section aria-labelledby="technology-title">
    <h2 id="technology-title">기술</h2>

    <article>
      <h3>
        <a href="/news/1">새로운 웹 표준 소식</a>
      </h3>
      <p>기사 요약...</p>
    </article>

    <article>
      <h3>
        <a href="/news/2">브라우저 업데이트</a>
      </h3>
      <p>기사 요약...</p>
    </article>
  </section>
</main>
```

# 29. 관리자 화면 구조

관리자 화면도 의미 있는 영역으로 구성할 수 있습니다.

```html
<header class="admin-header">
  <h1>관리자 페이지</h1>
</header>

<nav class="admin-nav" aria-label="관리자 메뉴">
  <a href="/admin/dashboard">대시보드</a>
  <a href="/admin/users">회원 관리</a>
  <a href="/admin/posts">게시글 관리</a>
</nav>

<main>
  <section aria-labelledby="dashboard-title">
    <h2 id="dashboard-title">대시보드</h2>

    <section aria-labelledby="stats-title">
      <h3 id="stats-title">주요 통계</h3>
      <!-- 통계 카드 -->
    </section>

    <section aria-labelledby="recent-title">
      <h3 id="recent-title">최근 활동</h3>
      <!-- 활동 목록 -->
    </section>
  </section>
</main>
```

모든 화면을 `article`로 만들 필요는 없습니다.

독립 배포 콘텐츠가 아니라 관리 기능의 주제별 영역이라면 `section`이 더 자연스럽습니다.

# 30. `div`와 `section` 선택 기준

다음 질문을 순서대로 확인합니다.

1. 이 콘텐츠에 의미 있는 제목을 붙일 수 있는가?
2. 하나의 주제를 가진 구역인가?
3. 독립적으로 배포 가능한 콘텐츠인가?
4. 단지 스타일과 배치를 위한 묶음인가?

판단 예:

```html
<section>
  <h2>추천 과정</h2>

  <div class="course-grid">
    <article class="course-card">
      ...
    </article>
  </div>
</section>
```

- 추천 과정 전체: 주제가 있으므로 `section`
- 카드 목록 배치: 디자인용이므로 `div`
- 각 과정 카드: 독립 콘텐츠이면 `article`

# 31. 시맨틱 태그를 과도하게 사용하지 않는다

시맨틱 요소가 많다고 무조건 좋은 코드는 아닙니다.

```html
<section>
  <section>
    <section>
      <section>
        <p>내용</p>
      </section>
    </section>
  </section>
</section>
```

각 구역에 실제 주제와 제목이 없다면 구조만 복잡해집니다.

다음처럼 단순한 구조가 더 적절할 수 있습니다.

```html
<section>
  <h2>과정 소개</h2>

  <div class="content-wrapper">
    <p>내용</p>
  </div>
</section>
```

# 32. 잘못된 중첩 예

## 32.1 `main` 안에 또 다른 `main`

```html
<!-- 잘못된 구조 -->
<main>
  <main>
    <p>내용</p>
  </main>
</main>
```

페이지의 핵심 콘텐츠 영역은 일반적으로 하나의 `main`으로 구성합니다.

## 32.2 `header`에 페이지 전체 콘텐츠를 넣음

```html
<!-- 의미가 부자연스러움 -->
<header>
  <h1>사이트</h1>
  <article>
    <h2>본문</h2>
    <p>전체 글 내용...</p>
  </article>
</header>
```

`header`는 머리말 영역이지 전체 본문을 감싸는 요소가 아닙니다.

## 32.3 단순 장식에 `section` 사용

```html
<section class="red-background">
  <span>NEW</span>
</section>
```

주제 구역이 아니라 스타일용 묶음이라면 `div`가 더 적절합니다.

# 33. 링크와 버튼의 의미 구분

페이지 구조를 작성할 때 링크와 버튼을 혼동하지 않습니다.

링크는 다른 위치로 이동합니다.

```html
<a href="/courses">과정 보기</a>
```

버튼은 현재 화면에서 동작을 실행합니다.

```html
<button type="button">메뉴 열기</button>
```

다음처럼 이동 기능을 `div` 클릭으로 만들면 접근성이 떨어질 수 있습니다.

```html
<div onclick="location.href='/courses'">
  과정 보기
</div>
```

이동 목적이라면 기본 링크를 사용합니다.

# 34. 목록과 내비게이션

내비게이션 링크가 여러 개라면 목록으로 구성할 수 있습니다.

```html
<nav aria-label="주요 메뉴">
  <ul>
    <li><a href="/">홈</a></li>
    <li><a href="/courses">과정</a></li>
    <li><a href="/projects">프로젝트</a></li>
  </ul>
</nav>
```

CSS로 목록 표시를 제거하고 가로 메뉴로 만들 수 있습니다.

```css
nav ul {
  display: flex;
  gap: 1rem;
  list-style: none;
  padding: 0;
}
```

HTML에서는 메뉴 항목의 관계를 목록으로 표현하고, CSS에서는 보이는 형태를 조절합니다.

# 35. 이미지와 시맨틱 구조

이미지와 설명이 하나의 독립된 콘텐츠라면 `figure`와 `figcaption`을 사용할 수 있습니다.

```html
<figure>
  <img
    src="asset/dashboard.png"
    alt="Developer Wiki 대시보드 화면"
  >
  <figcaption>
    Developer Wiki 학습 대시보드
  </figcaption>
</figure>
```

`figure`가 반드시 이미지만 담는 것은 아닙니다.

코드, 표, 인용문 등 본문에서 참조할 수 있는 독립 콘텐츠에도 사용할 수 있습니다.

# 36. 폼과 시맨틱 구조

폼은 페이지 주제 안에 배치합니다.

```html
<main>
  <section aria-labelledby="contact-title">
    <h1 id="contact-title">문의하기</h1>

    <form action="/inquiries" method="post">
      <div class="form-field">
        <label for="email">이메일</label>
        <input
          type="email"
          id="email"
          name="email"
          required
        >
      </div>

      <div class="form-field">
        <label for="message">문의 내용</label>
        <textarea
          id="message"
          name="message"
          rows="8"
          required
        ></textarea>
      </div>

      <button type="submit">문의 등록</button>
    </form>
  </section>
</main>
```

폼 내부의 단순 배치 그룹에는 `div`가 적절합니다.

모든 입력 묶음을 `section`으로 만들 필요는 없습니다.

# 37. 표와 시맨틱 구조

```html
<main>
  <section aria-labelledby="schedule-title">
    <h1 id="schedule-title">교육 일정</h1>

    <table>
      <caption>2026년 HTML 교육 일정</caption>
      <thead>
        <tr>
          <th scope="col">날짜</th>
          <th scope="col">주제</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>7월 28일</td>
          <td>시맨틱 HTML</td>
        </tr>
      </tbody>
    </table>
  </section>
</main>
```

시맨틱 페이지 구조와 표 내부의 시맨틱 구조를 함께 사용합니다.

# 38. 원본 수업 코드와의 연결

HTML 08번은 독립된 원본 실습 파일이 없다.

```text
HTML 01
→ 기본 문서 구조

HTML 02
→ Heading·Paragraph·Text 의미

HTML 03
→ Link·Navigation

HTML 04
→ List·Menu 구조

HTML 05
→ Table Data 구조

HTML 06
→ Image·Media

HTML 07
→ Form·Input

HTML 08
→ 위 구조를 Semantic Page로 조립
```

따라서 이 단원에서는 내 코드와 강사님 코드의 “08번 차이”를 비교하지 않는다. 대신 앞선 원본에서 반복해서 확인한 구조를 Semantic Element에 연결한다.

## 38.1 Heading과 `header`

앞선 문서에서 사용한 `h1`~`h6`는 단순 글자 크기가 아니라 문서 제목 계층이다.

```html
<header class="site-header">
    <h1>Developer Wiki</h1>
</header>
```

`header`를 사용한다고 자동으로 제목이 생기지는 않는다. 필요한 Heading은 직접 작성한다.

## 38.2 Link·List와 `nav`

Navigation Link 묶음은 보통 List와 함께 구성할 수 있다.

```html
<nav aria-label="주요 메뉴">
    <ul>
        <li>
            <a href="./html.html">
                HTML
            </a>
        </li>

        <li>
            <a href="./css.html">
                CSS
            </a>
        </li>
    </ul>
</nav>
```

모든 Link 묶음을 무조건 `nav`로 만들 필요는 없다. Page의 주요 Navigation 영역인지 판단한다.

## 38.3 Table은 Semantic Layout 대체물이 아니다

Table은 행·열 관계가 있는 Data에 사용한다.

```html
<main>
    <section aria-labelledby="course-title">
        <h2 id="course-title">
            과정 현황
        </h2>

        <table>
            ...
        </table>
    </section>
</main>
```

Page 전체 Layout을 Table로 구성하지 않는다.

## 38.4 Media와 `figure`

Image와 Caption이 하나의 독립된 Content Unit이면 `figure`를 사용할 수 있다.

```html
<article>
    <h2>프로젝트 소개</h2>

    <figure>
        <img
            src="./images/project.webp"
            alt="교육 과정 대시보드 화면"
        >

        <figcaption>
            반응형 교육 과정 대시보드
        </figcaption>
    </figure>
</article>
```

모든 Image에 `figure`가 필요한 것은 아니다.

## 38.5 Form과 `main`

Login·Search·Contact Form도 Page의 의미 구조 안에 배치한다.

```html
<main>
    <section aria-labelledby="contact-title">
        <h2 id="contact-title">
            문의하기
        </h2>

        <form>
            ...
        </form>
    </section>
</main>
```

`section`은 Form을 감싸기 위한 장식 Wrapper가 아니라 독립된 주제 영역일 때 사용한다.

## 38.6 `div`는 여전히 필요하다

Semantic Element로 의미를 표현할 수 없는 순수 Layout Wrapper에는 `div`가 적합하다.

```html
<section>
    <h2>추천 과정</h2>

    <div class="course-grid">
        ...
    </div>
</section>
```

```text
section
→ 주제와 의미를 가진 영역

div
→ 별도 의미 없이 구조·Style을 위한 Group
```

## 38.7 원본 연결 요약

| 앞선 단원 | 배운 구조 | 08번에서 연결되는 의미 |
| --- | --- | --- |
| 01 | 기본 Document | `header`·`main`·`footer` Page 골격 |
| 02 | Heading·Text | Heading Hierarchy와 Section 제목 |
| 03 | Link | `nav`와 주요 Navigation |
| 04 | List | Menu·Navigation List |
| 05 | Table | Semantic Data 영역 |
| 06 | Media | `figure`·`figcaption`과 Article Content |
| 07 | Form | 의미 있는 Section 내부 Form |
| 08 | 통합 | Semantic Page Structure |

# 39. 통합 프로젝트 예제

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
  >
  <meta
    name="description"
    content="HTML, CSS, JavaScript 학습 문서를 제공하는 Developer Wiki"
  >
  <title>Developer Wiki</title>
</head>
<body>
  <header class="site-header">
    <a href="/" class="logo">
      Developer Wiki
    </a>

    <nav aria-label="주요 메뉴">
      <ul>
        <li><a href="#html">HTML</a></li>
        <li><a href="#css">CSS</a></li>
        <li><a href="#javascript">JavaScript</a></li>
      </ul>
    </nav>
  </header>

  <main>
    <section class="hero" aria-labelledby="hero-title">
      <h1 id="hero-title">
        개발 학습 내용을 하나의 위키로 정리합니다
      </h1>

      <p>
        개념, 예제, 실무 팁, 문제 풀이를 단계별로 학습하세요.
      </p>

      <a href="#html">HTML 학습 시작</a>
    </section>

    <section id="html" aria-labelledby="html-title">
      <h2 id="html-title">HTML</h2>

      <div class="card-list">
        <article class="learning-card">
          <h3>
            <a href="/html/basic">
              HTML 기초와 문서 구조
            </a>
          </h3>
          <p>HTML 문서의 기본 골격을 학습합니다.</p>
        </article>

        <article class="learning-card">
          <h3>
            <a href="/html/forms">
              폼과 입력 요소
            </a>
          </h3>
          <p>사용자 입력값을 구성하고 전송합니다.</p>
        </article>

        <article class="learning-card">
          <h3>
            <a href="/html/semantic">
              시맨틱 태그와 페이지 구조
            </a>
          </h3>
          <p>의미 있는 웹페이지 골격을 작성합니다.</p>
        </article>
      </div>
    </section>

    <section id="css" aria-labelledby="css-title">
      <h2 id="css-title">CSS</h2>
      <p>선택자, 박스 모델, 배치와 반응형 디자인을 학습합니다.</p>
    </section>

    <section
      id="javascript"
      aria-labelledby="javascript-title"
    >
      <h2 id="javascript-title">JavaScript</h2>
      <p>변수, 함수, DOM, 이벤트와 비동기 처리를 학습합니다.</p>
    </section>

    <section aria-labelledby="newsletter-title">
      <h2 id="newsletter-title">새 문서 알림 신청</h2>

      <form action="/newsletter" method="post">
        <label for="newsletter-email">
          이메일
        </label>

        <input
          type="email"
          id="newsletter-email"
          name="email"
          required
        >

        <button type="submit">
          신청하기
        </button>
      </form>
    </section>
  </main>

  <aside aria-labelledby="related-title">
    <h2 id="related-title">관련 링크</h2>
    <ul>
      <li><a href="/roadmap">전체 학습 로드맵</a></li>
      <li><a href="/projects">프로젝트 목록</a></li>
    </ul>
  </aside>

  <footer class="site-footer">
    <nav aria-label="하단 메뉴">
      <a href="/about">소개</a>
      <a href="/privacy">개인정보처리방침</a>
    </nav>

    <p>&copy; 2026 Developer Wiki</p>
  </footer>
</body>
</html>
```

# 40. 구조 설계 순서

실무에서 HTML 페이지를 작성할 때 다음 순서로 접근할 수 있습니다.

## 40.1 콘텐츠를 먼저 나눈다

- 사이트 헤더
- 주요 메뉴
- 페이지 핵심 콘텐츠
- 주제별 구역
- 보조 콘텐츠
- 사이트 푸터

## 40.2 각 영역의 목적을 질문한다

- 페이지의 핵심인가?
- 주요 탐색인가?
- 독립 콘텐츠인가?
- 하나의 주제 구역인가?
- 보조 콘텐츠인가?
- 단지 배치용인가?

## 40.3 제목 구조를 작성한다

```text
h1 페이지 제목
├─ h2 첫 번째 주요 구역
│  ├─ h3 하위 콘텐츠
│  └─ h3 하위 콘텐츠
└─ h2 두 번째 주요 구역
```

## 40.4 필요한 요소를 넣는다

- 링크
- 목록
- 이미지
- 표
- 폼

## 40.5 마지막에 CSS용 클래스를 추가한다

처음부터 디자인 이름만 생각하기보다 콘텐츠 구조를 먼저 완성합니다.

# 41. 자주 하는 실수

## 41.1 모든 컨테이너를 `section`으로 작성

`section`은 단순한 디자인 래퍼가 아닙니다.

주제가 없다면 `div`를 사용합니다.

## 41.2 모든 링크 묶음을 `nav`로 작성

본문의 관련 링크 한두 개까지 모두 `nav`로 감싸지 않습니다.

주요 탐색 영역에 사용합니다.

## 41.3 제목 단계 건너뛰기

```html
<h1>페이지 제목</h1>
<h4>첫 번째 구역</h4>
```

구조상 `h2`가 자연스럽다면 `h2`를 사용합니다.

## 41.4 디자인 때문에 제목 태그 선택

큰 글자는 `h1`, 작은 글자는 `h6`이라는 기준은 잘못되었습니다.

구조에 맞는 제목을 선택하고 CSS로 크기를 조절합니다.

## 41.5 여러 개의 핵심 `main`

하나의 페이지에서 핵심 본문을 여러 `main`으로 나누지 않습니다.

## 41.6 `article`과 `section`을 무조건 함께 사용

두 요소는 필요에 따라 독립적으로 사용할 수 있습니다.

```html
<article>
  <h1>게시글 제목</h1>
  <p>짧은 게시글 본문</p>
</article>
```

하위 주제가 없다면 내부 `section`이 없어도 됩니다.

## 41.7 시맨틱 요소만 쓰고 제목을 생략

```html
<section>
  <p>공지 내용...</p>
</section>
```

구역의 목적을 설명하는 제목을 제공하는 것이 좋습니다.

# 42. 디버깅과 검수 방법

## 42.1 CSS를 잠시 끈다

CSS 없이도 콘텐츠 순서와 제목 구조가 이해되는지 확인합니다.

## 42.2 제목만 읽어 본다

`h1`부터 하위 제목까지 읽었을 때 문서 목차처럼 자연스러운지 확인합니다.

## 42.3 랜드마크를 확인한다

- 핵심 콘텐츠에 `main`이 있는가?
- 주요 메뉴에 `nav`가 있는가?
- 보조 콘텐츠에 `aside`가 적절한가?
- 여러 `nav`의 목적이 구분되는가?

## 42.4 개발자 도구를 확인한다

Elements 탭에서 실제 DOM 구조와 브라우저의 자동 보정 결과를 확인합니다.

## 42.5 HTML 검사기를 사용한다

잘못된 중첩, 중복 `id`, 누락된 속성 등을 확인합니다.

# 43. 접근성 체크리스트

1. 페이지의 핵심 제목이 명확한가?
2. 제목 단계가 자연스러운가?
3. 주요 메뉴가 실제 링크로 구성되어 있는가?
4. `main`이 핵심 콘텐츠를 감싸는가?
5. 여러 내비게이션의 목적이 구분되는가?
6. `section`에 이해 가능한 제목이 있는가?
7. 클릭 가능한 요소에 `a` 또는 `button`을 사용했는가?
8. 이미지의 `alt`가 목적에 맞는가?
9. 폼 입력 요소에 `label`이 연결되어 있는가?
10. 키보드로 콘텐츠를 자연스럽게 탐색할 수 있는가?

# 44. 실무 리뷰 기준

코드 리뷰에서 다음 질문을 사용할 수 있습니다.

- 이 태그를 선택한 이유를 설명할 수 있는가?
- 클래스명을 지워도 콘텐츠 역할을 이해할 수 있는가?
- 이 `section`에는 실제 주제가 있는가?
- 이 `article`은 독립 콘텐츠인가?
- 이 `aside`는 본문에서 분리 가능한가?
- 제목 순서가 콘텐츠 계층을 반영하는가?
- 반복되는 페이지 공통 영역과 페이지별 본문이 구분되는가?
- CSS를 적용하지 않아도 읽는 순서가 자연스러운가?


# 45. 종합실습

## 문제 1. 기본 페이지 골격

다음 요소를 사용해 기본 페이지 구조를 작성하세요.

- `header`
- `nav`
- `main`
- `footer`

사이트 이름은 `Developer Wiki`이며 메뉴는 HTML, CSS, JavaScript입니다.

## 문제 2. `div`와 `section`

다음 두 영역에 알맞은 요소를 선택하세요.

1. `추천 강의`라는 제목과 강의 목록이 있는 영역
2. 추천 강의 카드를 가로로 배치하기 위한 내부 래퍼

## 문제 3. `section`과 `article`

최신 블로그 글 3개를 보여 주는 영역을 작성하세요.

- 전체 목록 제목은 `최신 글`
- 각각의 글은 독립된 콘텐츠
- 글 제목과 요약 포함

## 문제 4. 여러 내비게이션

한 페이지에 다음 두 내비게이션을 작성하세요.

- 사이트 주요 메뉴
- 현재 문서 목차

스크린 리더가 두 영역을 구분할 수 있도록 작성하세요.

## 문제 5. 제목 구조 수정

다음 코드의 제목 구조를 개선하세요.

```html
<h1>HTML</h1>
<h4>시맨틱 태그</h4>
<h2>header</h2>
<h5>사용 예</h5>
```

## 문제 6. 잘못된 구조 찾기

다음 코드의 문제를 설명하고 수정하세요.

```html
<header>
  <h1>사이트 제목</h1>

  <main>
    <article>
      <h2>게시글</h2>
      <p>본문...</p>
    </article>
  </main>
</header>
```

## 문제 7. `article` 내부 구조

게시글 하나를 다음 요소로 구성하세요.

- 게시글 제목
- 작성일
- 본문
- 작성자 정보

게시글의 머리말과 바닥글에도 시맨틱 요소를 사용하세요.

## 문제 8. 포트폴리오 구조

다음 구역을 가진 포트폴리오 페이지 구조를 작성하세요.

- 사이트 헤더
- 소개
- 기술 스택
- 프로젝트 목록
- 연락처
- 사이트 푸터

프로젝트는 각각 독립된 콘텐츠로 작성하세요.

## 문제 9. 잘못된 클릭 요소

다음 코드를 의미에 맞게 수정하세요.

```html
<div onclick="location.href='/courses'">
  과정 보기
</div>

<span onclick="openMenu()">
  메뉴
</span>
```

첫 번째 요소는 페이지 이동, 두 번째 요소는 현재 페이지의 메뉴 열기 기능입니다.

## 문제 10. 종합 실습

Developer Wiki 홈 화면의 HTML 골격을 작성하세요.

조건:

- 사이트 헤더와 주요 메뉴
- 페이지 핵심 제목
- HTML, CSS, JavaScript 학습 구역
- 각 학습 구역에 문서 카드 2개
- 관련 링크 사이드 영역
- 뉴스레터 신청 폼
- 사이트 푸터
- 자연스러운 제목 단계

# 46. 정답과 해설

## 정답 1

```html
<header>
  <h1>Developer Wiki</h1>

  <nav aria-label="주요 메뉴">
    <ul>
      <li><a href="/html">HTML</a></li>
      <li><a href="/css">CSS</a></li>
      <li><a href="/javascript">JavaScript</a></li>
    </ul>
  </nav>
</header>

<main>
  <p>Developer Wiki 학습 콘텐츠</p>
</main>

<footer>
  <p>&copy; 2026 Developer Wiki</p>
</footer>
```

`nav` 안의 메뉴를 링크와 목록으로 작성했습니다.

## 정답 2

```html
<section>
  <h2>추천 강의</h2>

  <div class="course-list">
    <!-- 강의 카드 -->
  </div>
</section>
```

추천 강의 전체는 제목이 있는 주제 구역이므로 `section`, 내부 배치 래퍼는 `div`가 적절합니다.

## 정답 3

```html
<section aria-labelledby="latest-title">
  <h2 id="latest-title">최신 글</h2>

  <article>
    <h3>HTML 시맨틱 태그</h3>
    <p>시맨틱 요소의 역할을 정리합니다.</p>
  </article>

  <article>
    <h3>CSS 선택자</h3>
    <p>기본 선택자의 사용법을 정리합니다.</p>
  </article>

  <article>
    <h3>JavaScript 변수</h3>
    <p>변수 선언 방식의 차이를 정리합니다.</p>
  </article>
</section>
```

전체 목록은 `section`, 각 글은 독립 콘텐츠이므로 `article`입니다.

## 정답 4

```html
<nav aria-label="주요 메뉴">
  <a href="/">홈</a>
  <a href="/docs">문서</a>
</nav>

<nav aria-label="현재 문서 목차">
  <a href="#header">header</a>
  <a href="#main">main</a>
  <a href="#footer">footer</a>
</nav>
```

같은 `nav` 요소가 여러 개 있으므로 각각의 목적을 `aria-label`로 구분했습니다.

## 정답 5

```html
<h1>HTML</h1>
<h2>시맨틱 태그</h2>
<h3>header</h3>
<h4>사용 예</h4>
```

각 제목이 상위 주제의 하위 단계가 되도록 순서를 정리했습니다.

## 정답 6

```html
<header>
  <h1>사이트 제목</h1>
</header>

<main>
  <article>
    <h2>게시글</h2>
    <p>본문...</p>
  </article>
</main>
```

`main`은 페이지의 핵심 콘텐츠이므로 사이트 머리말인 `header` 안에 넣지 않습니다.

## 정답 7

```html
<article>
  <header>
    <h1>시맨틱 HTML 정리</h1>
    <p>작성일: 2026-07-28</p>
  </header>

  <p>시맨틱 HTML은 콘텐츠의 의미를 표현합니다.</p>

  <footer>
    <p>작성자: 홍길동</p>
  </footer>
</article>
```

`header`와 `footer`는 페이지 전체뿐 아니라 `article` 내부에서도 사용할 수 있습니다.

## 정답 8

```html
<header>
  <a href="/">홍길동 Portfolio</a>

  <nav aria-label="포트폴리오 메뉴">
    <a href="#about">소개</a>
    <a href="#skills">기술</a>
    <a href="#projects">프로젝트</a>
    <a href="#contact">연락처</a>
  </nav>
</header>

<main>
  <section id="about">
    <h1>웹 개발자 홍길동입니다</h1>
    <p>사용자 문제를 해결하는 개발자입니다.</p>
  </section>

  <section id="skills">
    <h2>기술 스택</h2>
    <p>HTML, CSS, JavaScript</p>
  </section>

  <section id="projects">
    <h2>프로젝트</h2>

    <article>
      <h3>Developer Wiki</h3>
      <p>개발 학습 문서 프로젝트입니다.</p>
    </article>

    <article>
      <h3>AI FAQ 서비스</h3>
      <p>RAG 기반 질의응답 서비스입니다.</p>
    </article>
  </section>

  <section id="contact">
    <h2>연락처</h2>
    <p>example@example.com</p>
  </section>
</main>

<footer>
  <p>&copy; 2026 홍길동</p>
</footer>
```

프로젝트는 다른 위치에서도 소개할 수 있는 독립 콘텐츠이므로 `article`로 작성했습니다.

## 정답 9

```html
<a href="/courses">
  과정 보기
</a>

<button type="button" onclick="openMenu()">
  메뉴
</button>
```

페이지 이동은 링크, 현재 화면의 동작 실행은 버튼을 사용합니다.

## 정답 10

```html
<header class="site-header">
  <a href="/" class="logo">Developer Wiki</a>

  <nav aria-label="주요 메뉴">
    <a href="#html">HTML</a>
    <a href="#css">CSS</a>
    <a href="#javascript">JavaScript</a>
  </nav>
</header>

<main>
  <h1>개발 학습 로드맵</h1>

  <section id="html">
    <h2>HTML</h2>

    <article>
      <h3>HTML 기초</h3>
      <p>문서 구조를 학습합니다.</p>
    </article>

    <article>
      <h3>HTML 폼</h3>
      <p>입력 요소를 학습합니다.</p>
    </article>
  </section>

  <section id="css">
    <h2>CSS</h2>

    <article>
      <h3>CSS 선택자</h3>
      <p>요소를 선택하는 방법을 학습합니다.</p>
    </article>

    <article>
      <h3>CSS 박스 모델</h3>
      <p>크기와 여백을 학습합니다.</p>
    </article>
  </section>

  <section id="javascript">
    <h2>JavaScript</h2>

    <article>
      <h3>변수와 자료형</h3>
      <p>데이터 저장 방법을 학습합니다.</p>
    </article>

    <article>
      <h3>함수</h3>
      <p>재사용 가능한 코드를 학습합니다.</p>
    </article>
  </section>

  <section aria-labelledby="newsletter-title">
    <h2 id="newsletter-title">뉴스레터 신청</h2>

    <form action="/newsletter" method="post">
      <label for="email">이메일</label>
      <input
        type="email"
        id="email"
        name="email"
        required
      >
      <button type="submit">신청</button>
    </form>
  </section>
</main>

<aside aria-labelledby="related-title">
  <h2 id="related-title">관련 링크</h2>
  <a href="/roadmap">전체 로드맵</a>
</aside>

<footer>
  <p>&copy; 2026 Developer Wiki</p>
</footer>
```


# 47. 최종 체크리스트

- [ ] Page의 주요 Content를 하나의 `main` 영역으로 구분했는가?
- [ ] `main`을 Page 안에 중첩하지 않는가?
- [ ] `header`와 `footer`를 Page 전체 또는 Section 문맥에 맞게 사용하는가?
- [ ] 주요 Navigation에 `nav`를 사용하는가?
- [ ] 모든 Link 묶음을 무조건 `nav`로 만들지 않는가?
- [ ] `section`에 독립된 주제와 필요한 Heading이 있는가?
- [ ] 단순 Style Wrapper에 `section` 대신 `div`를 고려했는가?
- [ ] 독립적으로 배포·재사용 가능한 Content에 `article`을 고려했는가?
- [ ] 보조 Content에 `aside`를 사용하는가?
- [ ] Heading을 글자 크기 때문에 선택하지 않는가?
- [ ] Heading Level이 콘텐츠 계층을 반영하는가?
- [ ] `h1` 이후 하위 Heading 구조가 이해 가능한가?
- [ ] Semantic Element가 자동으로 CSS Style을 해결한다고 오해하지 않는가?
- [ ] 같은 `header`, `nav`, `footer`가 문맥에 따라 여러 번 존재할 수 있음을 이해하는가?
- [ ] 주요 Landmark가 중복될 때 필요하면 Accessible Name을 제공하는가?
- [ ] `aria-label`을 보이는 Heading 대신 무조건 사용하지 않는가?
- [ ] Link와 Button의 역할을 구분하는가?
- [ ] Navigation List에 의미 있는 Link Text를 사용하는가?
- [ ] Table을 Page Layout 용도로 사용하지 않는가?
- [ ] Image와 Caption의 관계가 있을 때 `figure`·`figcaption`을 검토하는가?
- [ ] Form을 의미 있는 Page 영역 안에 배치하는가?
- [ ] Semantic Tag를 많이 쓰는 것 자체를 목표로 하지 않는가?
- [ ] CSS를 꺼도 콘텐츠 구조와 읽는 순서가 이해 가능한가?
- [ ] Keyboard와 Screen Reader에서 Landmark·Heading 구조를 확인했는가?
- [ ] HTML Validator와 DevTools로 잘못된 중첩을 검수했는가?
- [ ] 독립된 08번 원본 파일이 없다는 사실을 문서에서 명확히 기록했는가?

---

# 48. 핵심 요약

- 시맨틱 HTML은 태그를 통해 콘텐츠의 의미와 역할을 표현한다.
- HTML은 구조와 의미를, CSS는 디자인과 배치를 담당한다.
- `div`는 의미 없는 일반 컨테이너이며 잘못된 요소가 아니다.
- `header`와 `footer`는 페이지 또는 콘텐츠 구역마다 사용할 수 있다.
- `nav`는 주요 탐색 링크 묶음에 사용한다.
- `main`은 페이지의 핵심 콘텐츠를 나타내며 일반적으로 하나를 사용한다.
- `section`은 제목을 붙일 수 있는 하나의 주제 구역이다.
- `article`은 독립적으로 배포하거나 재사용할 수 있는 콘텐츠다.
- `aside`는 본문에서 분리할 수 있는 관련 보조 콘텐츠다.
- 제목 태그는 글자 크기가 아니라 문서 계층에 따라 선택한다.
- 시맨틱 태그와 CSS용 클래스는 함께 사용할 수 있다.
- 모든 컨테이너를 무조건 시맨틱 태그로 바꾸지 않는다.
- 페이지 이동에는 `a`, 현재 화면 동작에는 `button`을 사용한다.
- CSS 없이도 콘텐츠 순서와 구조가 이해되어야 한다.
- 원본 HTML 자료는 01~07까지이며, 이 08번 문서는 앞선 단원을 실무형 페이지 구조로 연결한 확장 문서다.
