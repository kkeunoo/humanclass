---
title: CSS 종합실습
version: v3.0-encyclopedia
last_updated: 2026-08-07
status: Completed
---

# CSS 종합실습

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `17_CSS_종합실습.md` |
| 분류 | `02_CSS` |
| 실습 주제 | 반응형 교육 과정 대시보드 |
| 핵심 범위 | 선택자, 단위, 박스 모델, Display, 배경, 글꼴, Position, Overflow, Shadow, Transition, Transform, Media Query, Flexbox, Grid |
| 구현 방식 | 디자인 토큰, Mobile First, Component Class, 접근성 상태, 반응형 Layout |
| 문서 형식 | 요구사항 → 설계 → 단계별 구현 → 완성 코드 → 실행 결과 → 해설 → 개선 과제 |

> 이 문서는 CSS 01~16번에서 학습한 내용을 하나의 페이지로 연결한다.  
> 단순 속성 연습이 아니라 **디자인 토큰 → Layout → Component → 상태 → 반응형 → 접근성 → 검수** 흐름으로 완성한다.

---

# 프로젝트 개요

IT 교육 과정과 학습 현황을 보여 주는 반응형 대시보드를 만든다.

```text
Header
    ↓
Hero
    ↓
검색·필터 Toolbar
    ↓
과정 Card Grid
    ↓
공지·학습 현황 Panel
    ↓
CTA
    ↓
Footer
```

화면 크기에 따라 다음처럼 변경된다.

```text
Mobile
→ 1열
→ 세로 Navigation
→ Card 1열
→ Toolbar 세로 배치

Tablet
→ 2열 Card
→ 일부 Toolbar 가로 배치

Desktop
→ Sidebar + Main
→ Card 3열
→ 넓은 Hero
```

---

# 학습 목표

- 실제 페이지 요구사항을 Layout과 Component로 나눌 수 있다.
- CSS Custom Property로 색상·간격·Radius·Shadow를 관리할 수 있다.
- Mobile First 방식으로 Style을 작성할 수 있다.
- Flexbox와 Grid의 역할을 구분할 수 있다.
- Position을 Badge·Overlay처럼 필요한 곳에만 사용할 수 있다.
- 긴 Text와 Card Overflow를 안전하게 처리할 수 있다.
- Hover·Focus·Disabled 상태를 함께 설계할 수 있다.
- Transition과 Transform을 필요한 속성에만 적용할 수 있다.
- `prefers-reduced-motion`을 지원할 수 있다.
- `clamp()`, `min()`, `max()`로 유연한 크기를 만들 수 있다.
- Component Class와 Modifier를 사용할 수 있다.
- 접근성 있는 Focus Style과 충분한 Contrast를 제공할 수 있다.
- 개발자 도구로 Box Model·Grid·Flex·Overflow를 점검할 수 있다.

---

# 1. 요구사항

## 1-1. 전체 Layout

- Mobile First로 작성한다.
- 전체 너비를 제한하는 Container를 사용한다.
- Desktop에서는 Sidebar와 Main Content를 2열로 배치한다.
- Mobile에서는 한 열로 자연스럽게 쌓인다.

## 1-2. Header

- Logo와 Navigation을 표시한다.
- Mobile에서는 Navigation이 줄바꿈된다.
- 현재 Page Link를 시각적으로 구분한다.
- Hover와 Keyboard Focus 상태를 함께 제공한다.

## 1-3. Hero

- 배경 Gradient와 장식 효과를 사용한다.
- 제목 크기는 `clamp()`로 유연하게 설정한다.
- CTA Button 두 개를 배치한다.
- 작은 화면에서는 Button을 세로 배치한다.

## 1-4. 과정 Card

- 제목, 설명, Level, 진행률, 학습 Button을 포함한다.
- Card 수에 따라 Grid가 자동으로 조정된다.
- Hover 가능 장치에서만 Card가 살짝 올라간다.
- 긴 설명은 Layout을 깨지 않게 처리한다.

## 1-5. 상태와 접근성

- 완료 과정은 Modifier Class로 구분한다.
- 비활성 Button은 `disabled` 상태를 사용한다.
- Focus Outline을 제거하지 않는다.
- 움직임 감소 설정에서는 Transition을 제거한다.

---

# 2. HTML 구조

```html
<body>
    <header class="site-header">
        <div class="container site-header__inner">
            <a
                href="#"
                class="site-logo"
            >
                Developer Academy
            </a>

            <nav
                class="site-nav"
                aria-label="주요 메뉴"
            >
                <a
                    href="#"
                    class="site-nav__link is-active"
                    aria-current="page"
                >
                    과정
                </a>

                <a
                    href="#"
                    class="site-nav__link"
                >
                    학습 현황
                </a>

                <a
                    href="#"
                    class="site-nav__link"
                >
                    커뮤니티
                </a>
            </nav>
        </div>
    </header>

    <main>
        <section class="hero">
            <div class="container hero__inner">
                <div class="hero__content">
                    <p class="hero__eyebrow">
                        실무 중심 Frontend 과정
                    </p>

                    <h1 class="hero__title">
                        기초부터 프로젝트까지
                        한 번에 학습하세요
                    </h1>

                    <p class="hero__description">
                        HTML, CSS, JavaScript를
                        실무 프로젝트 흐름으로 학습합니다.
                    </p>

                    <div class="hero__actions">
                        <a
                            href="#courses"
                            class="button button--primary"
                        >
                            과정 보기
                        </a>

                        <a
                            href="#progress"
                            class="button button--secondary"
                        >
                            학습 현황
                        </a>
                    </div>
                </div>

                <div
                    class="hero__visual"
                    aria-hidden="true"
                >
                    <span class="hero__code">
                        &lt;/&gt;
                    </span>
                </div>
            </div>
        </section>

        <div class="container dashboard">
            <aside class="dashboard__sidebar">
                <section class="panel">
                    <h2 class="panel__title">
                        학습 현황
                    </h2>

                    <div class="progress-summary">
                        <strong class="progress-summary__value">
                            68%
                        </strong>

                        <span class="progress-summary__label">
                            전체 진행률
                        </span>
                    </div>

                    <div
                        class="progress"
                        role="progressbar"
                        aria-valuemin="0"
                        aria-valuemax="100"
                        aria-valuenow="68"
                        aria-label="전체 학습 진행률"
                    >
                        <span
                            class="progress__bar"
                            style="--progress: 68%"
                        ></span>
                    </div>
                </section>

                <section class="panel">
                    <h2 class="panel__title">
                        공지
                    </h2>

                    <ul class="notice-list">
                        <li class="notice-list__item">
                            CSS 종합실습이 추가되었습니다.
                        </li>

                        <li class="notice-list__item">
                            다음 과정은 반응형 Layout입니다.
                        </li>
                    </ul>
                </section>
            </aside>

            <section
                class="dashboard__main"
                id="courses"
            >
                <div class="section-heading">
                    <div>
                        <p class="section-heading__eyebrow">
                            Courses
                        </p>

                        <h2 class="section-heading__title">
                            학습 과정
                        </h2>
                    </div>

                    <div class="course-toolbar">
                        <label class="search-field">
                            <span class="u-visually-hidden">
                                과정 검색
                            </span>

                            <input
                                type="search"
                                placeholder="과정 검색"
                            >
                        </label>

                        <select aria-label="난이도 선택">
                            <option>전체</option>
                            <option>입문</option>
                            <option>중급</option>
                        </select>
                    </div>
                </div>

                <div class="course-grid">
                    <article class="course-card">
                        <span class="course-card__badge">
                            입문
                        </span>

                        <div class="course-card__icon">
                            HTML
                        </div>

                        <h3 class="course-card__title">
                            HTML 기초
                        </h3>

                        <p class="course-card__description">
                            문서 구조와 의미 있는 Markup을
                            학습합니다.
                        </p>

                        <div class="course-card__footer">
                            <span>진행률 100%</span>

                            <button
                                type="button"
                                class="button button--small"
                            >
                                복습하기
                            </button>
                        </div>
                    </article>

                    <article class="course-card is-complete">
                        <span class="course-card__badge">
                            중급
                        </span>

                        <div class="course-card__icon">
                            CSS
                        </div>

                        <h3 class="course-card__title">
                            CSS Layout
                        </h3>

                        <p class="course-card__description">
                            Flexbox, Grid, 반응형 Layout을
                            실무 기준으로 학습합니다.
                        </p>

                        <div class="course-card__footer">
                            <span>진행률 82%</span>

                            <button
                                type="button"
                                class="button button--small"
                            >
                                이어서 학습
                            </button>
                        </div>
                    </article>

                    <article class="course-card">
                        <span class="course-card__badge">
                            중급
                        </span>

                        <div class="course-card__icon">
                            JS
                        </div>

                        <h3 class="course-card__title">
                            JavaScript DOM
                        </h3>

                        <p class="course-card__description">
                            Event와 DOM을 사용해
                            동적인 화면을 구현합니다.
                        </p>

                        <div class="course-card__footer">
                            <span>진행률 35%</span>

                            <button
                                type="button"
                                class="button button--small"
                                disabled
                            >
                                준비 중
                            </button>
                        </div>
                    </article>
                </div>
            </section>
        </div>

        <section class="cta">
            <div class="container cta__inner">
                <div>
                    <p class="cta__eyebrow">
                        Next Step
                    </p>

                    <h2 class="cta__title">
                        이제 직접 프로젝트를 시작하세요
                    </h2>
                </div>

                <a
                    href="#"
                    class="button button--light"
                >
                    프로젝트 보기
                </a>
            </div>
        </section>
    </main>

    <footer class="site-footer">
        <div class="container">
            Developer-Wiki · CSS 종합실습
        </div>
    </footer>
</body>
```

---

# 3. 디자인 토큰

```css
:root {
    --color-text: #1f2937;
    --color-text-muted: #6b7280;
    --color-surface: #ffffff;
    --color-surface-muted: #f8fafc;
    --color-border: #dbe3ed;
    --color-primary: #2563eb;
    --color-primary-dark: #1d4ed8;
    --color-primary-soft: #dbeafe;
    --color-success: #15803d;
    --color-success-soft: #dcfce7;
    --color-focus: #93c5fd;

    --space-1: 0.25rem;
    --space-2: 0.5rem;
    --space-3: 0.75rem;
    --space-4: 1rem;
    --space-5: 1.25rem;
    --space-6: 1.5rem;
    --space-8: 2rem;
    --space-10: 2.5rem;
    --space-12: 3rem;

    --radius-small: 0.5rem;
    --radius-medium: 0.875rem;
    --radius-large: 1.25rem;
    --radius-round: 999rem;

    --shadow-small:
        0 0.25rem 0.75rem
        rgb(15 23 42 / 0.08);

    --shadow-card:
        0 0.75rem 2rem
        rgb(15 23 42 / 0.12);

    --container-width: 75rem;
}
```

---

# 4. Reset과 기본 Style

```css
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
    min-block-size: 100dvh;
    background:
        var(--color-surface-muted);
    color: var(--color-text);
    font-family:
        system-ui,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif;
    line-height: 1.6;
}

img,
svg {
    display: block;
    max-inline-size: 100%;
}

button,
input,
select {
    font: inherit;
}

button,
a {
    -webkit-tap-highlight-color:
        transparent;
}
```

---

# 5. 공통 Container

```css
.container {
    width: min(
        100% - 2rem,
        var(--container-width)
    );

    margin-inline: auto;
}
```

---

# 6. 접근성 Utility

```css
.u-visually-hidden {
    position: absolute;
    inline-size: 1px;
    block-size: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip-path: inset(50%);
    white-space: nowrap;
    border: 0;
}
```

---

# 7. Header

```css
.site-header {
    position: sticky;
    inset-block-start: 0;
    z-index: 100;
    border-block-end:
        1px solid
        rgb(219 227 237 / 0.8);
    background:
        rgb(255 255 255 / 0.92);
    backdrop-filter: blur(0.75rem);
}

.site-header__inner {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content:
        space-between;
    gap: var(--space-4);
    min-block-size: 4.5rem;
    padding-block:
        var(--space-3);
}

.site-logo {
    color: var(--color-text);
    font-size: 1.125rem;
    font-weight: 800;
    text-decoration: none;
}

.site-nav {
    display: flex;
    flex-wrap: wrap;
    gap: var(--space-2);
}

.site-nav__link {
    padding:
        var(--space-2)
        var(--space-3);
    border-radius:
        var(--radius-small);
    color: var(--color-text-muted);
    font-weight: 700;
    text-decoration: none;
}

.site-nav__link:hover,
.site-nav__link:focus-visible,
.site-nav__link.is-active {
    background:
        var(--color-primary-soft);
    color: var(--color-primary-dark);
}

.site-nav__link:focus-visible {
    outline: 0.1875rem solid
        var(--color-focus);
    outline-offset: 0.125rem;
}
```

---

# 8. Hero Layout

```css
.hero {
    position: relative;
    overflow: hidden;
    color: white;
    background:
        radial-gradient(
            circle at 85% 15%,
            rgb(255 255 255 / 0.2),
            transparent 22rem
        ),
        linear-gradient(
            135deg,
            #1d4ed8,
            #4f46e5
        );
}

.hero::after {
    content: "";
    position: absolute;
    inset:
        auto -8rem -10rem auto;
    inline-size: 22rem;
    aspect-ratio: 1;
    border-radius: 50%;
    background:
        rgb(255 255 255 / 0.08);
}

.hero__inner {
    position: relative;
    z-index: 1;
    display: grid;
    gap: var(--space-8);
    align-items: center;
    padding-block:
        clamp(
            4rem,
            10vw,
            8rem
        );
}

.hero__content {
    max-inline-size: 42rem;
}

.hero__eyebrow,
.section-heading__eyebrow,
.cta__eyebrow {
    margin: 0 0 var(--space-2);
    font-size: 0.875rem;
    font-weight: 800;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}

.hero__title {
    margin: 0;
    max-inline-size: 14ch;
    font-size:
        clamp(
            2.25rem,
            8vw,
            5rem
        );
    line-height: 1.08;
    letter-spacing: -0.04em;
}

.hero__description {
    max-inline-size: 40rem;
    margin:
        var(--space-5)
        0 0;
    color:
        rgb(255 255 255 / 0.85);
    font-size:
        clamp(
            1rem,
            2vw,
            1.25rem
        );
}

.hero__actions {
    display: flex;
    flex-direction: column;
    gap: var(--space-3);
    margin-block-start:
        var(--space-6);
}

.hero__visual {
    display: grid;
    place-items: center;
    min-block-size: 15rem;
}

.hero__code {
    display: grid;
    place-items: center;
    inline-size:
        clamp(
            10rem,
            30vw,
            18rem
        );
    aspect-ratio: 1;
    border:
        1px solid
        rgb(255 255 255 / 0.3);
    border-radius: 2rem;
    background:
        rgb(255 255 255 / 0.12);
    box-shadow:
        0 2rem 4rem
        rgb(15 23 42 / 0.25);
    font-size:
        clamp(
            2rem,
            8vw,
            5rem
        );
    font-weight: 800;
    transform: rotate(-5deg);
}
```

---

# 9. 공통 Button

```css
.button {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-block-size: 2.75rem;
    padding-inline:
        var(--space-5);
    border: 0;
    border-radius:
        var(--radius-small);
    font-weight: 800;
    text-decoration: none;
    cursor: pointer;
    transition:
        background-color 0.2s,
        color 0.2s,
        transform 0.2s,
        box-shadow 0.2s;
}

.button--primary {
    background: white;
    color: var(--color-primary-dark);
}

.button--secondary {
    border:
        1px solid
        rgb(255 255 255 / 0.5);
    background:
        transparent;
    color: white;
}

.button--small {
    min-block-size: 2.25rem;
    padding-inline:
        var(--space-3);
    background:
        var(--color-primary);
    color: white;
    font-size: 0.875rem;
}

.button--light {
    background: white;
    color: var(--color-primary-dark);
}

.button:hover {
    box-shadow:
        0 0.5rem 1rem
        rgb(15 23 42 / 0.18);
}

.button:focus-visible {
    outline: 0.1875rem solid
        var(--color-focus);
    outline-offset: 0.1875rem;
}

.button:disabled {
    cursor: not-allowed;
    opacity: 0.5;
    box-shadow: none;
}
```

---

# 10. Dashboard Layout

```css
.dashboard {
    display: grid;
    gap: var(--space-8);
    padding-block:
        var(--space-10);
}

.dashboard__sidebar {
    display: grid;
    align-content: start;
    gap: var(--space-4);
}

.dashboard__main {
    min-width: 0;
}
```

---

# 11. Panel

```css
.panel {
    padding: var(--space-5);
    border:
        1px solid
        var(--color-border);
    border-radius:
        var(--radius-medium);
    background:
        var(--color-surface);
    box-shadow:
        var(--shadow-small);
}

.panel__title {
    margin:
        0 0 var(--space-4);
    font-size: 1.125rem;
}
```

---

# 12. Progress

```css
.progress-summary {
    display: flex;
    align-items: baseline;
    gap: var(--space-2);
}

.progress-summary__value {
    color: var(--color-primary);
    font-size: 2rem;
}

.progress-summary__label {
    color: var(--color-text-muted);
}

.progress {
    overflow: hidden;
    block-size: 0.75rem;
    margin-block-start:
        var(--space-4);
    border-radius:
        var(--radius-round);
    background:
        var(--color-primary-soft);
}

.progress__bar {
    display: block;
    inline-size:
        var(--progress, 0%);
    block-size: 100%;
    border-radius: inherit;
    background:
        linear-gradient(
            90deg,
            var(--color-primary),
            #7c3aed
        );
}
```

---

# 13. Notice List

```css
.notice-list {
    display: grid;
    gap: var(--space-3);
    margin: 0;
    padding: 0;
    list-style: none;
}

.notice-list__item {
    padding-block-end:
        var(--space-3);
    border-block-end:
        1px solid
        var(--color-border);
    color:
        var(--color-text-muted);
}

.notice-list__item:last-child {
    padding-block-end: 0;
    border-block-end: 0;
}
```

---

# 14. Section Heading과 Toolbar

```css
.section-heading {
    display: flex;
    flex-direction: column;
    gap: var(--space-4);
    margin-block-end:
        var(--space-6);
}

.section-heading__eyebrow {
    color: var(--color-primary);
}

.section-heading__title {
    margin: 0;
    font-size:
        clamp(
            1.75rem,
            4vw,
            2.5rem
        );
}

.course-toolbar {
    display: grid;
    gap: var(--space-3);
}

.search-field input,
.course-toolbar select {
    inline-size: 100%;
    min-block-size: 2.75rem;
    padding-inline:
        var(--space-3);
    border:
        1px solid
        var(--color-border);
    border-radius:
        var(--radius-small);
    background:
        var(--color-surface);
    color: var(--color-text);
}

.search-field input:focus,
.course-toolbar select:focus {
    border-color:
        var(--color-primary);
    outline: 0.1875rem solid
        var(--color-focus);
    outline-offset: 0.0625rem;
}
```

---

# 15. Course Grid

```css
.course-grid {
    display: grid;
    grid-template-columns:
        repeat(
            auto-fit,
            minmax(
                min(100%, 16rem),
                1fr
            )
        );
    gap: var(--space-6);
}
```

---

# 16. Course Card

```css
.course-card {
    position: relative;
    display: grid;
    align-content: start;
    gap: var(--space-4);
    min-width: 0;
    padding: var(--space-5);
    border:
        1px solid
        var(--color-border);
    border-radius:
        var(--radius-large);
    background:
        var(--color-surface);
    box-shadow:
        var(--shadow-small);
    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease,
        border-color 0.25s ease;
}

.course-card.is-complete {
    border-color:
        var(--color-success);
    background:
        linear-gradient(
            180deg,
            var(--color-success-soft),
            var(--color-surface)
        );
}

.course-card__badge {
    position: absolute;
    inset-block-start:
        var(--space-4);
    inset-inline-end:
        var(--space-4);
    padding:
        var(--space-1)
        var(--space-3);
    border-radius:
        var(--radius-round);
    background:
        var(--color-primary-soft);
    color:
        var(--color-primary-dark);
    font-size: 0.75rem;
    font-weight: 800;
}

.course-card__icon {
    display: grid;
    place-items: center;
    inline-size: 4rem;
    aspect-ratio: 1;
    border-radius:
        var(--radius-medium);
    background:
        linear-gradient(
            135deg,
            var(--color-primary),
            #7c3aed
        );
    color: white;
    font-weight: 900;
}

.course-card__title {
    margin: 0;
    padding-inline-end: 4rem;
    font-size: 1.25rem;
}

.course-card__description {
    margin: 0;
    color:
        var(--color-text-muted);
    overflow-wrap: anywhere;
}

.course-card__footer {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content:
        space-between;
    gap: var(--space-3);
    margin-block-start: auto;
    padding-block-start:
        var(--space-4);
    border-block-start:
        1px solid
        var(--color-border);
    font-size: 0.875rem;
}
```

---

# 17. CTA

```css
.cta {
    background:
        linear-gradient(
            135deg,
            #111827,
            #1e3a8a
        );
    color: white;
}

.cta__inner {
    display: flex;
    flex-direction: column;
    gap: var(--space-6);
    align-items: flex-start;
    justify-content:
        space-between;
    padding-block:
        var(--space-12);
}

.cta__title {
    margin: 0;
    max-inline-size: 22ch;
    font-size:
        clamp(
            1.75rem,
            5vw,
            3rem
        );
    line-height: 1.15;
}
```

---

# 18. Footer

```css
.site-footer {
    padding-block:
        var(--space-6);
    background: #0f172a;
    color:
        rgb(255 255 255 / 0.7);
    text-align: center;
}
```

---

# 19. Hover 가능 장치

```css
@media (
    hover: hover
) and (
    pointer: fine
) {
    .button:hover {
        transform:
            translateY(-0.125rem);
    }

    .course-card:hover {
        border-color:
            var(--color-primary);
        box-shadow:
            var(--shadow-card);
        transform:
            translateY(-0.375rem);
    }
}
```

---

# 20. Tablet 반응형

```css
@media (
    min-width: 40rem
) {
    .hero__actions {
        flex-direction: row;
    }

    .course-toolbar {
        grid-template-columns:
            minmax(14rem, 1fr)
            10rem;
    }

    .cta__inner {
        flex-direction: row;
        align-items: center;
    }
}
```

---

# 21. Desktop 반응형

```css
@media (
    min-width: 64rem
) {
    .hero__inner {
        grid-template-columns:
            minmax(0, 1.2fr)
            minmax(16rem, 0.8fr);
    }

    .dashboard {
        grid-template-columns:
            minmax(15rem, 18rem)
            minmax(0, 1fr);
    }

    .dashboard__sidebar {
        position: sticky;
        inset-block-start: 6rem;
        align-self: start;
    }

    .section-heading {
        flex-direction: row;
        align-items: end;
        justify-content:
            space-between;
    }
}
```

---

# 22. Reduced Motion

```css
@media (
    prefers-reduced-motion:
    reduce
) {
    html {
        scroll-behavior: auto;
    }

    .button,
    .course-card {
        transition: none;
    }

    .hero__code {
        transform: none;
    }
}
```

---

# 23. Dark Mode 선택 과제

```css
@media (
    prefers-color-scheme:
    dark
) {
    :root {
        --color-text: #f1f5f9;
        --color-text-muted: #94a3b8;
        --color-surface: #111827;
        --color-surface-muted: #020617;
        --color-border: #334155;
    }
}
```

프로젝트 요구사항에 따라 자동 Dark Mode 대신 사용자가 직접 선택하는 Theme Toggle을 사용할 수 있다.

---

# 24. 완성 CSS 코드

```css
:root {
    --color-text: #1f2937;
    --color-text-muted: #6b7280;
    --color-surface: #ffffff;
    --color-surface-muted: #f8fafc;
    --color-border: #dbe3ed;
    --color-primary: #2563eb;
    --color-primary-dark: #1d4ed8;
    --color-primary-soft: #dbeafe;
    --color-success: #15803d;
    --color-success-soft: #dcfce7;
    --color-focus: #93c5fd;

    --space-1: 0.25rem;
    --space-2: 0.5rem;
    --space-3: 0.75rem;
    --space-4: 1rem;
    --space-5: 1.25rem;
    --space-6: 1.5rem;
    --space-8: 2rem;
    --space-10: 2.5rem;
    --space-12: 3rem;

    --radius-small: 0.5rem;
    --radius-medium: 0.875rem;
    --radius-large: 1.25rem;
    --radius-round: 999rem;

    --shadow-small:
        0 0.25rem 0.75rem
        rgb(15 23 42 / 0.08);

    --shadow-card:
        0 0.75rem 2rem
        rgb(15 23 42 / 0.12);

    --container-width: 75rem;
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
    min-block-size: 100dvh;
    background:
        var(--color-surface-muted);
    color: var(--color-text);
    font-family:
        system-ui,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif;
    line-height: 1.6;
}

img,
svg {
    display: block;
    max-inline-size: 100%;
}

button,
input,
select {
    font: inherit;
}

button,
a {
    -webkit-tap-highlight-color:
        transparent;
}

.container {
    width: min(
        100% - 2rem,
        var(--container-width)
    );

    margin-inline: auto;
}

.u-visually-hidden {
    position: absolute;
    inline-size: 1px;
    block-size: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip-path: inset(50%);
    white-space: nowrap;
    border: 0;
}

.site-header {
    position: sticky;
    inset-block-start: 0;
    z-index: 100;
    border-block-end:
        1px solid
        rgb(219 227 237 / 0.8);
    background:
        rgb(255 255 255 / 0.92);
    backdrop-filter: blur(0.75rem);
}

.site-header__inner {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content:
        space-between;
    gap: var(--space-4);
    min-block-size: 4.5rem;
    padding-block:
        var(--space-3);
}

.site-logo {
    color: var(--color-text);
    font-size: 1.125rem;
    font-weight: 800;
    text-decoration: none;
}

.site-nav {
    display: flex;
    flex-wrap: wrap;
    gap: var(--space-2);
}

.site-nav__link {
    padding:
        var(--space-2)
        var(--space-3);
    border-radius:
        var(--radius-small);
    color: var(--color-text-muted);
    font-weight: 700;
    text-decoration: none;
}

.site-nav__link:hover,
.site-nav__link:focus-visible,
.site-nav__link.is-active {
    background:
        var(--color-primary-soft);
    color: var(--color-primary-dark);
}

.site-nav__link:focus-visible {
    outline: 0.1875rem solid
        var(--color-focus);
    outline-offset: 0.125rem;
}

.hero {
    position: relative;
    overflow: hidden;
    color: white;
    background:
        radial-gradient(
            circle at 85% 15%,
            rgb(255 255 255 / 0.2),
            transparent 22rem
        ),
        linear-gradient(
            135deg,
            #1d4ed8,
            #4f46e5
        );
}

.hero::after {
    content: "";
    position: absolute;
    inset:
        auto -8rem -10rem auto;
    inline-size: 22rem;
    aspect-ratio: 1;
    border-radius: 50%;
    background:
        rgb(255 255 255 / 0.08);
}

.hero__inner {
    position: relative;
    z-index: 1;
    display: grid;
    gap: var(--space-8);
    align-items: center;
    padding-block:
        clamp(
            4rem,
            10vw,
            8rem
        );
}

.hero__content {
    max-inline-size: 42rem;
}

.hero__eyebrow,
.section-heading__eyebrow,
.cta__eyebrow {
    margin: 0 0 var(--space-2);
    font-size: 0.875rem;
    font-weight: 800;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}

.hero__title {
    margin: 0;
    max-inline-size: 14ch;
    font-size:
        clamp(
            2.25rem,
            8vw,
            5rem
        );
    line-height: 1.08;
    letter-spacing: -0.04em;
}

.hero__description {
    max-inline-size: 40rem;
    margin:
        var(--space-5)
        0 0;
    color:
        rgb(255 255 255 / 0.85);
    font-size:
        clamp(
            1rem,
            2vw,
            1.25rem
        );
}

.hero__actions {
    display: flex;
    flex-direction: column;
    gap: var(--space-3);
    margin-block-start:
        var(--space-6);
}

.hero__visual {
    display: grid;
    place-items: center;
    min-block-size: 15rem;
}

.hero__code {
    display: grid;
    place-items: center;
    inline-size:
        clamp(
            10rem,
            30vw,
            18rem
        );
    aspect-ratio: 1;
    border:
        1px solid
        rgb(255 255 255 / 0.3);
    border-radius: 2rem;
    background:
        rgb(255 255 255 / 0.12);
    box-shadow:
        0 2rem 4rem
        rgb(15 23 42 / 0.25);
    font-size:
        clamp(
            2rem,
            8vw,
            5rem
        );
    font-weight: 800;
    transform: rotate(-5deg);
}

.button {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-block-size: 2.75rem;
    padding-inline:
        var(--space-5);
    border: 0;
    border-radius:
        var(--radius-small);
    font-weight: 800;
    text-decoration: none;
    cursor: pointer;
    transition:
        background-color 0.2s,
        color 0.2s,
        transform 0.2s,
        box-shadow 0.2s;
}

.button--primary {
    background: white;
    color: var(--color-primary-dark);
}

.button--secondary {
    border:
        1px solid
        rgb(255 255 255 / 0.5);
    background:
        transparent;
    color: white;
}

.button--small {
    min-block-size: 2.25rem;
    padding-inline:
        var(--space-3);
    background:
        var(--color-primary);
    color: white;
    font-size: 0.875rem;
}

.button--light {
    background: white;
    color: var(--color-primary-dark);
}

.button:hover {
    box-shadow:
        0 0.5rem 1rem
        rgb(15 23 42 / 0.18);
}

.button:focus-visible {
    outline: 0.1875rem solid
        var(--color-focus);
    outline-offset: 0.1875rem;
}

.button:disabled {
    cursor: not-allowed;
    opacity: 0.5;
    box-shadow: none;
}

.dashboard {
    display: grid;
    gap: var(--space-8);
    padding-block:
        var(--space-10);
}

.dashboard__sidebar {
    display: grid;
    align-content: start;
    gap: var(--space-4);
}

.dashboard__main {
    min-width: 0;
}

.panel {
    padding: var(--space-5);
    border:
        1px solid
        var(--color-border);
    border-radius:
        var(--radius-medium);
    background:
        var(--color-surface);
    box-shadow:
        var(--shadow-small);
}

.panel__title {
    margin:
        0 0 var(--space-4);
    font-size: 1.125rem;
}

.progress-summary {
    display: flex;
    align-items: baseline;
    gap: var(--space-2);
}

.progress-summary__value {
    color: var(--color-primary);
    font-size: 2rem;
}

.progress-summary__label {
    color: var(--color-text-muted);
}

.progress {
    overflow: hidden;
    block-size: 0.75rem;
    margin-block-start:
        var(--space-4);
    border-radius:
        var(--radius-round);
    background:
        var(--color-primary-soft);
}

.progress__bar {
    display: block;
    inline-size:
        var(--progress, 0%);
    block-size: 100%;
    border-radius: inherit;
    background:
        linear-gradient(
            90deg,
            var(--color-primary),
            #7c3aed
        );
}

.notice-list {
    display: grid;
    gap: var(--space-3);
    margin: 0;
    padding: 0;
    list-style: none;
}

.notice-list__item {
    padding-block-end:
        var(--space-3);
    border-block-end:
        1px solid
        var(--color-border);
    color:
        var(--color-text-muted);
}

.notice-list__item:last-child {
    padding-block-end: 0;
    border-block-end: 0;
}

.section-heading {
    display: flex;
    flex-direction: column;
    gap: var(--space-4);
    margin-block-end:
        var(--space-6);
}

.section-heading__eyebrow {
    color: var(--color-primary);
}

.section-heading__title {
    margin: 0;
    font-size:
        clamp(
            1.75rem,
            4vw,
            2.5rem
        );
}

.course-toolbar {
    display: grid;
    gap: var(--space-3);
}

.search-field input,
.course-toolbar select {
    inline-size: 100%;
    min-block-size: 2.75rem;
    padding-inline:
        var(--space-3);
    border:
        1px solid
        var(--color-border);
    border-radius:
        var(--radius-small);
    background:
        var(--color-surface);
    color: var(--color-text);
}

.search-field input:focus,
.course-toolbar select:focus {
    border-color:
        var(--color-primary);
    outline: 0.1875rem solid
        var(--color-focus);
    outline-offset: 0.0625rem;
}

.course-grid {
    display: grid;
    grid-template-columns:
        repeat(
            auto-fit,
            minmax(
                min(100%, 16rem),
                1fr
            )
        );
    gap: var(--space-6);
}

.course-card {
    position: relative;
    display: grid;
    align-content: start;
    gap: var(--space-4);
    min-width: 0;
    padding: var(--space-5);
    border:
        1px solid
        var(--color-border);
    border-radius:
        var(--radius-large);
    background:
        var(--color-surface);
    box-shadow:
        var(--shadow-small);
    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease,
        border-color 0.25s ease;
}

.course-card.is-complete {
    border-color:
        var(--color-success);
    background:
        linear-gradient(
            180deg,
            var(--color-success-soft),
            var(--color-surface)
        );
}

.course-card__badge {
    position: absolute;
    inset-block-start:
        var(--space-4);
    inset-inline-end:
        var(--space-4);
    padding:
        var(--space-1)
        var(--space-3);
    border-radius:
        var(--radius-round);
    background:
        var(--color-primary-soft);
    color:
        var(--color-primary-dark);
    font-size: 0.75rem;
    font-weight: 800;
}

.course-card__icon {
    display: grid;
    place-items: center;
    inline-size: 4rem;
    aspect-ratio: 1;
    border-radius:
        var(--radius-medium);
    background:
        linear-gradient(
            135deg,
            var(--color-primary),
            #7c3aed
        );
    color: white;
    font-weight: 900;
}

.course-card__title {
    margin: 0;
    padding-inline-end: 4rem;
    font-size: 1.25rem;
}

.course-card__description {
    margin: 0;
    color:
        var(--color-text-muted);
    overflow-wrap: anywhere;
}

.course-card__footer {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content:
        space-between;
    gap: var(--space-3);
    margin-block-start: auto;
    padding-block-start:
        var(--space-4);
    border-block-start:
        1px solid
        var(--color-border);
    font-size: 0.875rem;
}

.cta {
    background:
        linear-gradient(
            135deg,
            #111827,
            #1e3a8a
        );
    color: white;
}

.cta__inner {
    display: flex;
    flex-direction: column;
    gap: var(--space-6);
    align-items: flex-start;
    justify-content:
        space-between;
    padding-block:
        var(--space-12);
}

.cta__title {
    margin: 0;
    max-inline-size: 22ch;
    font-size:
        clamp(
            1.75rem,
            5vw,
            3rem
        );
    line-height: 1.15;
}

.site-footer {
    padding-block:
        var(--space-6);
    background: #0f172a;
    color:
        rgb(255 255 255 / 0.7);
    text-align: center;
}

@media (
    hover: hover
) and (
    pointer: fine
) {
    .button:hover {
        transform:
            translateY(-0.125rem);
    }

    .course-card:hover {
        border-color:
            var(--color-primary);
        box-shadow:
            var(--shadow-card);
        transform:
            translateY(-0.375rem);
    }
}

@media (
    min-width: 40rem
) {
    .hero__actions {
        flex-direction: row;
    }

    .course-toolbar {
        grid-template-columns:
            minmax(14rem, 1fr)
            10rem;
    }

    .cta__inner {
        flex-direction: row;
        align-items: center;
    }
}

@media (
    min-width: 64rem
) {
    .hero__inner {
        grid-template-columns:
            minmax(0, 1.2fr)
            minmax(16rem, 0.8fr);
    }

    .dashboard {
        grid-template-columns:
            minmax(15rem, 18rem)
            minmax(0, 1fr);
    }

    .dashboard__sidebar {
        position: sticky;
        inset-block-start: 6rem;
        align-self: start;
    }

    .section-heading {
        flex-direction: row;
        align-items: end;
        justify-content:
            space-between;
    }
}

@media (
    prefers-reduced-motion:
    reduce
) {
    html {
        scroll-behavior: auto;
    }

    .button,
    .course-card {
        transition: none;
    }

    .hero__code {
        transform: none;
    }
}
```

---

# 25. 실행 결과

Mobile:

```text
Header Navigation 줄바꿈
Hero 1열
Button 세로 배치
Sidebar → Main 순서
Course Card 1열
CTA 세로 배치
```

Tablet:

```text
Hero Button 가로 배치
검색·필터 2열
Card 2열 이상 자동 배치
CTA 가로 배치
```

Desktop:

```text
Hero 2열
Sidebar Sticky
Main Content 확장
Card 3열 이상
Heading과 Toolbar 가로 정렬
```

---

# 26. 사용된 CSS 개념

| 학습 범위 | 적용 위치 |
| --- | --- |
| 선택자 | Component·Modifier·상태 Class |
| 단위 | `rem`, `%`, `vw`, `dvh`, `clamp()` |
| 박스 모델 | Padding·Border·`border-box` |
| Display | Block·Flex·Grid |
| 숨김 | Visually Hidden |
| Background | Gradient·Overlay |
| Typography | Scale·Line Height·Letter Spacing |
| Position | Sticky Header·Badge·장식 |
| Overflow | Hero Crop·Progress Bar |
| Shadow | Header·Panel·Card |
| Transition | Button·Card 상태 변화 |
| Transform | Hover 이동·Hero 장식 |
| Media Query | Tablet·Desktop·Hover 환경 |
| Flexbox | Header·Actions·Footer |
| Grid | Hero·Dashboard·Card 목록 |
| 실무 스타일 | Token·BEM·Mobile First·접근성 |

---

# 27. 실무에서는 왜 이렇게 작성하는가?

## 27-1. 디자인 토큰

색상·간격·Radius·Shadow를 한곳에서 관리한다.

```text
요구사항 변경
→ Token 수정
→ 여러 Component에 동시에 반영
```

## 27-2. Mobile First

작은 화면에서 기본 Layout을 만든 뒤 필요한 공간이 생길 때 확장한다.

## 27-3. Flex와 Grid 분리

- Header·Button Group → Flex
- Dashboard·Card 목록 → Grid
- Badge·장식 → Position

## 27-4. 상태 Class

```text
.course-card.is-complete
```

상태와 Component를 분리한다.

## 27-5. 접근성

- Focus Outline
- `aria-current`
- Progress ARIA
- Visually Hidden Label
- Reduced Motion
- Disabled Attribute

---

# 28. 대표 오류와 해결

## 28-1. Sticky Sidebar가 동작하지 않음

확인할 항목:

```text
부모 높이
부모 overflow
top 또는 inset-block-start
Scroll 공간
```

## 28-2. Card가 가로로 넘침

```css
.dashboard__main {
    min-width: 0;
}
```

Grid·Flex Item의 최소 크기를 줄일 수 있게 한다.

## 28-3. Hero Text가 너무 커짐

`clamp()`의 최대값을 조정한다.

## 28-4. Hover 확대가 Mobile에서도 남음

Hover 가능 장치 Media Query 안에서만 적용한다.

## 28-5. Progress Bar가 Container를 넘음

`--progress` 값을 0~100% 범위로 관리한다.

## 28-6. 가로 Scroll이 생김

다음을 확인한다.

```text
100vw
Absolute 장식
긴 문자열
Grid minmax()
고정 Width
음수 Offset
```

---

# 29. 개선 과제

- Mobile Navigation Toggle
- 실제 검색·필터 JavaScript 연결
- Dark Mode Toggle
- Card Skeleton Loading
- Toast Message
- Modal
- Accordion FAQ
- Container Query 적용
- Print Style
- CSS Module 또는 Scoped CSS 적용
- Stylelint 설정

---

# 30. 리팩토링 과제

다음 구조로 파일을 분리한다.

```text
styles/
├── reset.css
├── tokens.css
├── base.css
├── layout.css
├── components/
│   ├── button.css
│   ├── header.css
│   ├── hero.css
│   ├── panel.css
│   ├── course-card.css
│   └── cta.css
├── utilities.css
└── main.css
```

---

# 31. 종합실습 체크리스트

- [ ] 역할 기반 Class 이름을 사용했는가?
- [ ] ID와 긴 후손 Selector를 Style에 남용하지 않았는가?
- [ ] 색상과 간격을 Custom Property로 관리하는가?
- [ ] `border-box`를 전역으로 적용했는가?
- [ ] Container의 최대 너비와 Mobile Padding을 함께 처리했는가?
- [ ] Mobile First 방식으로 작성했는가?
- [ ] Flexbox와 Grid의 역할을 구분했는가?
- [ ] Position을 Badge·Sticky처럼 필요한 곳에만 사용했는가?
- [ ] `z-index`가 필요한 요소에만 적용되었는가?
- [ ] 긴 Text에 `overflow-wrap`을 적용했는가?
- [ ] Grid·Flex Item에 `min-width: 0`을 검토했는가?
- [ ] Hover뿐 아니라 Focus Style을 제공하는가?
- [ ] Focus Outline을 제거하지 않았는가?
- [ ] Disabled 상태에 HTML Attribute를 사용하는가?
- [ ] Transition 속성을 명시했는가?
- [ ] Hover Effect를 Hover 가능한 장치에만 적용했는가?
- [ ] Reduced Motion 환경을 지원하는가?
- [ ] Background 위 Text Contrast를 확보했는가?
- [ ] 콘텐츠 이미지를 Background로 대체하지 않았는가?
- [ ] Sticky 요소의 Scroll Container를 확인했는가?
- [ ] `100vw`로 불필요한 Overflow를 만들지 않았는가?
- [ ] Tablet·Desktop Breakpoint가 Layout 기준인가?
- [ ] Visually Hidden Label을 올바르게 제공했는가?
- [ ] Progress Bar에 ARIA 정보를 제공했는가?
- [ ] 개발자 도구로 Grid·Flex·Box Model을 검수했는가?

---

# 32. 핵심 요약

```text
Token
→ 색상
→ 간격
→ Radius
→ Shadow
```

```text
Mobile First
→ 기본 1열
→ 공간이 생기면 확장
```

```text
Flex
→ 한 축

Grid
→ 두 축

Position
→ 겹침·고정·배지
```

```text
상태
→ Modifier Class
→ Focus
→ Disabled
→ Reduced Motion
```

```text
반응형
→ clamp()
→ auto-fit
→ minmax()
→ Media Query
```

---

# 마무리

CSS 종합실습의 핵심은 여러 속성을 많이 사용하는 것이 아니다.

```text
요구사항을 Component와 Layout으로 나누고
    ↓
디자인 토큰으로 시각 규칙을 통일하고
    ↓
Flexbox·Grid·Position을 목적에 맞게 사용하고
    ↓
Mobile·Keyboard·Touch·Reduced Motion 환경을 고려하고
    ↓
수정 가능한 구조로 Style을 분리하는 것
```

이 페이지를 이해하고 직접 확장할 수 있다면 CSS 속성을 외우는 단계를 넘어, 실제 반응형 UI를 구조적으로 설계할 수 있다.
# V3 렌더링 추적 카드 — 요구사항에서 반응형 화면까지

먼저 DOM 구조와 레이아웃 영역을 정하고 박스 모델, typography, 색상, 상태, 반응형 순으로 구축한다. 각 단계에서 넓은 화면과 좁은 화면을 검증한다.

정상 콘텐츠뿐 아니라 긴 제목, 빈 이미지, 큰 글자 확대, 키보드 focus, overflow를 시험한다. 완성 화면 비교와 함께 Computed·Layout 근거를 기록한다.

**원본 연결:** 내 코드와 강사님 코드의 `workspace_html/css/01~15 전체 원본과 실습 폴더를 결합한 종합 확장`에서 실제 선택자·계산값·화면 차이를 확인한다.
