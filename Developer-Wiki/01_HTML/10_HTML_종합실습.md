---
title: HTML 종합실습
version: v2.0-final
last_updated: 2026-08-07
status: Completed
---

# HTML 종합실습

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `10_HTML_종합실습.md` |
| 분류 | `01_HTML` |
| 실습 주제 | 반응형 IT 교육 과정 소개·신청 페이지 |
| 핵심 범위 | Document Structure, Semantic HTML, Heading, Link, List, Table, Media, Form, 접근성 |
| 구현 방식 | Native HTML 우선, Semantic Landmark, 접근 가능한 Form, 의미 있는 Content 구조 |
| 문서 형식 | 요구사항 → 설계 → 단계별 구현 → 완성 HTML → 검수 → 확장 과제 |

> 이 문서는 HTML 01~09에서 학습한 내용을 하나의 Page로 연결한다.  
> 단순 Tag 모음이 아니라 **Page 목적 정의 → Semantic 구조 설계 → Content 작성 → 접근성 연결 → 실제 제출 Form → Validator 검수** 순서로 완성한다.

---

# 프로젝트 개요

IT 국비교육 과정 소개 Page를 만든다.

Page에는 다음 영역이 포함된다.

```text
Header
    ↓
Navigation
    ↓
Hero
    ↓
교육 과정 소개
    ↓
과정 Card 목록
    ↓
주간 시간표 Table
    ↓
수업 Media
    ↓
교육 특징
    ↓
상담 신청 Form
    ↓
FAQ
    ↓
Footer
```

CSS와 JavaScript를 아직 적용하지 않아도 HTML만 읽었을 때 정보 구조가 이해되어야 한다.

---

# 학습 목표

- HTML5 기본 Document Structure를 직접 작성한다.
- `lang`, `charset`, `viewport`, `title`, `description`을 구성한다.
- `header`, `nav`, `main`, `section`, `article`, `aside`, `footer`를 목적에 맞게 사용한다.
- Heading Level을 Page 정보 계층에 맞게 구성한다.
- Navigation Link에 의미 있는 Link Text를 작성한다.
- List를 항목 관계에 따라 `ul`, `ol`, `dl`로 구분한다.
- Image에 목적에 맞는 `alt`를 제공한다.
- Video와 `iframe`에 필요한 접근성 정보를 제공한다.
- Table에 `caption`, `thead`, `tbody`, `th`, `scope`를 적용한다.
- Form Control에 `label`, `id`, `name`, `autocomplete`을 연결한다.
- Checkbox·Radio·Select·Textarea를 실제 신청 Form에 활용한다.
- GET과 POST의 목적을 구분한다.
- `fieldset`, `legend`로 Form Group을 구조화한다.
- `aria-current`, `aria-labelledby`, `aria-describedby`를 필요한 곳에 제한적으로 사용한다.
- Duplicate ID, 잘못된 중첩, 의미 없는 `<br>` 반복을 피한다.
- HTML Validator와 DevTools로 문서 구조를 검수한다.

---

# 1. 요구사항 정리

## 1.1 Header

- Site Logo
- 주요 Navigation
- 현재 Page 표시
- 상담 신청 Link

## 1.2 Hero

- Page 대표 Heading
- 소개 문단
- 과정 보기 Link
- 상담 신청 Link

## 1.3 과정 소개

- Section Heading
- 과정 Card 3개
- 각 Card는 독립된 `article`
- 기술 Stack은 List 사용
- 상세 Page Link 제공

## 1.4 시간표

- `table`
- `caption`
- Column Header
- Data Row
- 요일·시간·과목 관계가 명확해야 함

## 1.5 Media

- 교육 현장 Image
- Caption
- 소개 Video
- YouTube Embed 예시

## 1.6 상담 신청 Form

- 이름
- Email
- 전화번호
- 관심 과정
- 상담 방식
- 학습 목적
- 개인정보 동의
- 제출 Button

## 1.7 FAQ

- 질문과 답변
- `details`, `summary` 사용

## 1.8 Footer

- 사업자·교육기관 정보
- Footer Navigation
- Copyright

---

# 2. 전체 Semantic 구조

먼저 Page의 큰 영역을 작성한다.

```html
<body>
    <header class="site-header">
        ...
    </header>

    <main>
        <section class="hero">
            ...
        </section>

        <section class="courses">
            ...
        </section>

        <section class="schedule">
            ...
        </section>

        <section class="media">
            ...
        </section>

        <section class="consultation">
            ...
        </section>

        <section class="faq">
            ...
        </section>
    </main>

    <footer class="site-footer">
        ...
    </footer>
</body>
```

핵심 Content는 하나의 `main` 안에 배치한다.

---

# 3. 기본 Document Structure

```html
<!doctype html>
<html lang="ko">
    <head>
        <meta charset="UTF-8">

        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        >

        <meta
            name="description"
            content="HTML, CSS, JavaScript 기반 실무형 Frontend 국비교육 과정을 소개합니다."
        >

        <title>
            Frontend 국비교육 과정 | Developer Academy
        </title>
    </head>

    <body>
        ...
    </body>
</html>
```

---

# 4. Header

```html
<header class="site-header">
    <a
        href="./index.html"
        class="site-logo"
        aria-label="Developer Academy 홈"
    >
        Developer Academy
    </a>

    <nav aria-label="주요 메뉴">
        <ul class="site-nav">
            <li>
                <a
                    href="./index.html"
                    aria-current="page"
                >
                    과정 소개
                </a>
            </li>

            <li>
                <a href="./projects.html">
                    프로젝트
                </a>
            </li>

            <li>
                <a href="./reviews.html">
                    수강 후기
                </a>
            </li>

            <li>
                <a href="#consultation">
                    상담 신청
                </a>
            </li>
        </ul>
    </nav>
</header>
```

---

# 5. `aria-current`

현재 Page Link에는 다음처럼 현재 상태를 표시할 수 있다.

```html
<a
    href="./index.html"
    aria-current="page"
>
    과정 소개
</a>
```

CSS Class만으로 시각적 표시를 하는 것보다 현재 Page라는 의미도 전달한다.

---

# 6. Hero

```html
<section
    class="hero"
    aria-labelledby="hero-title"
>
    <div class="hero__content">
        <p class="hero__eyebrow">
            실무 중심 Frontend Bootcamp
        </p>

        <h1 id="hero-title">
            HTML부터 Portfolio까지
            한 번에 완성하세요
        </h1>

        <p>
            Semantic HTML, Responsive CSS,
            JavaScript DOM과 실무 Project를
            단계적으로 학습합니다.
        </p>

        <div class="hero__actions">
            <a href="#course-list">
                과정 살펴보기
            </a>

            <a href="#consultation">
                상담 신청하기
            </a>
        </div>
    </div>

    <figure class="hero__figure">
        <img
            src="./assets/images/classroom.webp"
            alt="수강생들이 노트북으로 Frontend Project를 실습하는 교실"
            width="1200"
            height="800"
        >

        <figcaption>
            실습 중심 Frontend 수업
        </figcaption>
    </figure>
</section>
```

---

# 7. Hero Heading 구조

Page 대표 제목은 `h1`으로 작성한다.

```text
h1
→ Page 전체 대표 제목

h2
→ 주요 Section 제목

h3
→ Section 내부 Card·Article 제목
```

글씨 크기는 CSS에서 조정한다.

---

# 8. 과정 Section

```html
<section
    id="course-list"
    class="courses"
    aria-labelledby="course-list-title"
>
    <header class="section-heading">
        <p>
            Curriculum
        </p>

        <h2 id="course-list-title">
            학습 과정
        </h2>

        <p>
            기초부터 실무 프로젝트까지
            순서대로 학습합니다.
        </p>
    </header>

    <div class="course-grid">
        ...
    </div>
</section>
```

`course-grid`는 의미 없는 Layout Wrapper이므로 `div`를 사용한다.

---

# 9. Course Card를 `article`로 구성

```html
<article class="course-card">
    <img
        src="./assets/images/html-course.webp"
        alt=""
        width="640"
        height="360"
    >

    <h3>
        HTML
    </h3>

    <p>
        Semantic Markup과 접근성을
        중심으로 웹 문서 구조를 학습합니다.
    </p>

    <ul>
        <li>Document Structure</li>
        <li>Semantic HTML</li>
        <li>Form</li>
        <li>Accessibility</li>
    </ul>

    <a href="./courses/html.html">
        HTML 과정 자세히 보기
    </a>
</article>
```

Card 자체가 독립적인 과정 Content이므로 `article`이 적합하다.

---

# 10. 장식 Image의 `alt`

Card Image가 제목과 설명을 반복하는 단순 장식이라면 다음처럼 빈 `alt`를 사용할 수 있다.

```html
<img
    src="./assets/images/html-course.webp"
    alt=""
    width="640"
    height="360"
>
```

Screen Reader가 중복 정보를 읽는 것을 줄인다.

---

# 11. CSS 과정 Card

```html
<article class="course-card">
    <img
        src="./assets/images/css-course.webp"
        alt=""
        width="640"
        height="360"
    >

    <h3>
        CSS
    </h3>

    <p>
        Box Model, Flexbox, 반응형 Layout과
        UI Styling을 학습합니다.
    </p>

    <ul>
        <li>Box Model</li>
        <li>Flexbox</li>
        <li>Responsive Web</li>
        <li>Transition</li>
    </ul>

    <a href="./courses/css.html">
        CSS 과정 자세히 보기
    </a>
</article>
```

---

# 12. JavaScript 과정 Card

```html
<article class="course-card">
    <img
        src="./assets/images/javascript-course.webp"
        alt=""
        width="640"
        height="360"
    >

    <h3>
        JavaScript
    </h3>

    <p>
        변수, 함수, 배열, 객체, DOM,
        Event와 비동기 처리를 학습합니다.
    </p>

    <ul>
        <li>Variable</li>
        <li>Function</li>
        <li>Array</li>
        <li>DOM</li>
    </ul>

    <a href="./courses/javascript.html">
        JavaScript 과정 자세히 보기
    </a>
</article>
```

---

# 13. 순서가 중요한 학습 단계

```html
<section
    class="learning-flow"
    aria-labelledby="learning-flow-title"
>
    <h2 id="learning-flow-title">
        학습 진행 순서
    </h2>

    <ol>
        <li>HTML 문서 구조 이해</li>
        <li>CSS Layout 구현</li>
        <li>JavaScript Interaction 구현</li>
        <li>Portfolio Project 제작</li>
        <li>Code Review와 Refactoring</li>
    </ol>
</section>
```

절차이므로 `ol`이 적합하다.

---

# 14. 과정 정보 설명 목록

```html
<dl class="course-info">
    <div>
        <dt>
            교육 기간
        </dt>

        <dd>
            6개월
        </dd>
    </div>

    <div>
        <dt>
            교육 시간
        </dt>

        <dd>
            평일 09:00 ~ 18:00
        </dd>
    </div>

    <div>
        <dt>
            교육 방식
        </dt>

        <dd>
            오프라인 실습 중심
        </dd>
    </div>
</dl>
```

이름·값 관계이므로 `dl`이 적합하다.

---

# 15. 시간표 Section

```html
<section
    class="schedule"
    aria-labelledby="schedule-title"
>
    <h2 id="schedule-title">
        주간 시간표
    </h2>

    <div class="table-scroll">
        <table>
            <caption>
                Frontend 과정 주간 학습 일정
            </caption>

            <thead>
                <tr>
                    <th scope="col">
                        요일
                    </th>

                    <th scope="col">
                        오전
                    </th>

                    <th scope="col">
                        오후
                    </th>
                </tr>
            </thead>

            <tbody>
                <tr>
                    <th scope="row">
                        월요일
                    </th>

                    <td>
                        HTML
                    </td>

                    <td>
                        HTML 실습
                    </td>
                </tr>

                <tr>
                    <th scope="row">
                        화요일
                    </th>

                    <td>
                        CSS
                    </td>

                    <td>
                        Flexbox
                    </td>
                </tr>

                <tr>
                    <th scope="row">
                        수요일
                    </th>

                    <td>
                        JavaScript
                    </td>

                    <td>
                        DOM 실습
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</section>
```

---

# 16. Table Wrapper

반응형 화면에서 Table이 가로로 길어질 수 있으므로 CSS용 Wrapper를 둘 수 있다.

```html
<div class="table-scroll">
    <table>
        ...
    </table>
</div>
```

`table` 자체의 의미는 유지하면서 Wrapper가 Overflow를 담당한다.

---

# 17. 수업 Media Section

```html
<section
    class="media-section"
    aria-labelledby="media-title"
>
    <h2 id="media-title">
        수업 미리보기
    </h2>

    <figure>
        <img
            src="./assets/images/project-review.webp"
            alt="강사가 대형 화면으로 수강생 Project를 Code Review하는 모습"
            width="1200"
            height="800"
        >

        <figcaption>
            매주 진행하는 Project Code Review
        </figcaption>
    </figure>
</section>
```

---

# 18. Video

```html
<video
    controls
    preload="metadata"
>
    <source
        src="./assets/media/course-preview.webm"
        type="video/webm"
    >

    <source
        src="./assets/media/course-preview.mp4"
        type="video/mp4"
    >

    <track
        src="./assets/media/course-preview-ko.vtt"
        kind="captions"
        srclang="ko"
        label="한국어"
        default
    >

    Browser가 Video 재생을 지원하지 않습니다.
</video>
```

---

# 19. YouTube Embed

```html
<iframe
    src="https://www.youtube.com/embed/VIDEO_ID"
    title="Frontend 과정 소개 영상"
    loading="lazy"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen
></iframe>
```

`iframe`에는 내용을 설명하는 `title`을 제공한다.

---

# 20. 교육 특징

```html
<section
    class="features"
    aria-labelledby="features-title"
>
    <h2 id="features-title">
        교육 특징
    </h2>

    <ul>
        <li>
            실습 중심 수업
        </li>

        <li>
            GitHub 기반 학습 기록
        </li>

        <li>
            Portfolio Project
        </li>

        <li>
            Code Review
        </li>
    </ul>
</section>
```

순서가 중요하지 않은 특징 목록이므로 `ul`을 사용한다.

---

# 21. 보조 안내에 `aside`

```html
<aside
    class="notice"
    aria-labelledby="notice-title"
>
    <h2 id="notice-title">
        수강 전 확인
    </h2>

    <p>
        국비지원 자격은 개인 상황에 따라
        달라질 수 있습니다.
    </p>
</aside>
```

Page 핵심 흐름을 보조하는 Content이므로 `aside`를 사용할 수 있다.

---

# 22. 상담 신청 Section

```html
<section
    id="consultation"
    class="consultation"
    aria-labelledby="consultation-title"
>
    <h2 id="consultation-title">
        상담 신청
    </h2>

    <p id="consultation-help">
        필수 항목을 입력한 뒤
        상담 신청 Button을 눌러 주세요.
    </p>

    <form
        action="/api/consultation"
        method="post"
        aria-describedby="consultation-help"
    >
        ...
    </form>
</section>
```

---

# 23. 이름 Input

```html
<div class="form-field">
    <label for="name">
        이름
    </label>

    <input
        type="text"
        id="name"
        name="name"
        autocomplete="name"
        required
    >
</div>
```

---

# 24. Email Input

```html
<div class="form-field">
    <label for="email">
        Email
    </label>

    <input
        type="email"
        id="email"
        name="email"
        autocomplete="email"
        required
    >
</div>
```

---

# 25. 전화번호 Input

```html
<div class="form-field">
    <label for="phone">
        전화번호
    </label>

    <input
        type="tel"
        id="phone"
        name="phone"
        autocomplete="tel"
        placeholder="010-1234-5678"
    >
</div>
```

Placeholder는 Label 대신이 아니라 입력 예시로 사용한다.

---

# 26. 관심 과정 Select

```html
<div class="form-field">
    <label for="course">
        관심 과정
    </label>

    <select
        id="course"
        name="course"
        required
    >
        <option value="">
            선택해 주세요
        </option>

        <option value="frontend">
            Frontend
        </option>

        <option value="backend">
            Backend
        </option>

        <option value="fullstack">
            Full Stack
        </option>
    </select>
</div>
```

---

# 27. 상담 방식 Radio Group

```html
<fieldset>
    <legend>
        상담 방식
    </legend>

    <label>
        <input
            type="radio"
            name="consultation_type"
            value="phone"
            checked
        >
        전화 상담
    </label>

    <label>
        <input
            type="radio"
            name="consultation_type"
            value="visit"
        >
        방문 상담
    </label>

    <label>
        <input
            type="radio"
            name="consultation_type"
            value="online"
        >
        온라인 상담
    </label>
</fieldset>
```

같은 Group은 같은 `name`을 사용한다.

---

# 28. 학습 목적 Checkbox

여러 항목을 선택할 수 있으므로 Checkbox를 사용한다.

```html
<fieldset>
    <legend>
        학습 목적
    </legend>

    <label>
        <input
            type="checkbox"
            name="goal"
            value="employment"
        >
        취업
    </label>

    <label>
        <input
            type="checkbox"
            name="goal"
            value="portfolio"
        >
        Portfolio
    </label>

    <label>
        <input
            type="checkbox"
            name="goal"
            value="skill-up"
        >
        실무 역량 향상
    </label>
</fieldset>
```

---

# 29. 상담 내용 Textarea

```html
<div class="form-field">
    <label for="message">
        상담 내용
    </label>

    <textarea
        id="message"
        name="message"
        rows="6"
        maxlength="1000"
        placeholder="궁금한 내용을 입력해 주세요."
    ></textarea>
</div>
```

Textarea 안에 `<br>`이나 HTML Comment를 구조용으로 넣지 않는다.

---

# 30. 개인정보 동의 Checkbox

```html
<label>
    <input
        type="checkbox"
        name="privacy_agree"
        value="yes"
        required
    >

    개인정보 수집 및 이용에 동의합니다.
</label>
```

실제 Service에서는 개인정보 처리방침 Link와 상세 동의 내용을 함께 제공해야 한다.

---

# 31. Submit Button

```html
<button type="submit">
    상담 신청
</button>
```

일반 Button과 Submit Button의 역할을 구분한다.

---

# 32. Form 전체 예제

```html
<form
    action="/api/consultation"
    method="post"
>
    <div class="form-field">
        <label for="name">
            이름
        </label>

        <input
            type="text"
            id="name"
            name="name"
            autocomplete="name"
            required
        >
    </div>

    <div class="form-field">
        <label for="email">
            Email
        </label>

        <input
            type="email"
            id="email"
            name="email"
            autocomplete="email"
            required
        >
    </div>

    <div class="form-field">
        <label for="course">
            관심 과정
        </label>

        <select
            id="course"
            name="course"
            required
        >
            <option value="">
                선택해 주세요
            </option>

            <option value="frontend">
                Frontend
            </option>

            <option value="backend">
                Backend
            </option>
        </select>
    </div>

    <fieldset>
        <legend>
            상담 방식
        </legend>

        <label>
            <input
                type="radio"
                name="consultation_type"
                value="phone"
                checked
            >
            전화 상담
        </label>

        <label>
            <input
                type="radio"
                name="consultation_type"
                value="visit"
            >
            방문 상담
        </label>
    </fieldset>

    <div class="form-field">
        <label for="message">
            상담 내용
        </label>

        <textarea
            id="message"
            name="message"
            rows="6"
        ></textarea>
    </div>

    <label>
        <input
            type="checkbox"
            name="privacy_agree"
            value="yes"
            required
        >
        개인정보 수집 및 이용에 동의합니다.
    </label>

    <button type="submit">
        상담 신청
    </button>
</form>
```

---

# 33. POST와 HTTPS

Form이 POST라고 자동으로 안전한 것은 아니다.

```text
POST
→ Request Body에 Data 전달

HTTPS
→ Network 전송 암호화

Server Validation
→ 입력값 검증
```

개인정보를 실제로 전송하는 Service는 HTTPS를 사용한다.

---

# 34. FAQ Section

```html
<section
    class="faq"
    aria-labelledby="faq-title"
>
    <h2 id="faq-title">
        자주 묻는 질문
    </h2>

    <details>
        <summary>
            비전공자도 수강할 수 있나요?
        </summary>

        <p>
            기초 과정부터 진행하므로
            비전공자도 참여할 수 있습니다.
        </p>
    </details>

    <details>
        <summary>
            Portfolio Project가 포함되나요?
        </summary>

        <p>
            과정 후반부에 Team·개인 Project를
            진행합니다.
        </p>
    </details>
</section>
```

`summary`는 `details`의 직접적인 Summary로 사용한다.

---

# 35. Footer

```html
<footer class="site-footer">
    <div>
        <strong>
            Developer Academy
        </strong>

        <address>
            충청남도 천안시 Example Road 10<br>
            대표 전화:
            <a href="tel:+82410000000">
                041-000-0000
            </a>
        </address>
    </div>

    <nav aria-label="Footer 메뉴">
        <ul>
            <li>
                <a href="./privacy.html">
                    개인정보 처리방침
                </a>
            </li>

            <li>
                <a href="./terms.html">
                    이용약관
                </a>
            </li>
        </ul>
    </nav>

    <p>
        &copy; 2026 Developer Academy
    </p>
</footer>
```

---

# 36. `address`

`address`는 단순 주소 Styling Element가 아니다.

현재 Page 또는 Article의 연락처 정보를 나타낼 때 사용한다.

```html
<address>
    Email:
    <a href="mailto:study@example.com">
        study@example.com
    </a>
</address>
```

---

# 37. Page 내부 Fragment Link

Hero에서 상담 Form으로 이동할 수 있다.

```html
<a href="#consultation">
    상담 신청하기
</a>
```

대상:

```html
<section id="consultation">
    ...
</section>
```

`id`는 Page 안에서 고유해야 한다.

---

# 38. 외부 Link

```html
<a
    href="https://github.com/"
    target="_blank"
    rel="noopener"
>
    GitHub 보기
</a>
```

새 Tab이 필요한지 실제 UX 요구사항을 확인한다.

---

# 39. Download Link

```html
<a
    href="./assets/files/frontend-curriculum.pdf"
    download
>
    교육 과정표 PDF 받기
</a>
```

Cross-origin Resource나 Server Header에 따라 `download` 동작이 달라질 수 있다.

---

# 40. 날짜에는 `time`

```html
<p>
    개강일:
    <time datetime="2026-09-01">
        2026년 9월 1일
    </time>
</p>
```

Machine-readable 값을 제공한다.

---

# 41. 약어에는 `abbr`

```html
<p>
    <abbr title="HyperText Markup Language">
        HTML
    </abbr>
    기초부터 시작합니다.
</p>
```

문맥상 설명이 필요한 약어에 사용할 수 있다.

---

# 42. HTML Comment

좋은 Comment:

```html
<!-- Mobile에서도 같은 Navigation DOM을 사용해
     Keyboard Focus 순서를 유지한다. -->
```

좋지 않은 Comment:

```html
<!-- 비밀번호: admin1234 -->
```

민감 정보는 절대 남기지 않는다.

---

# 43. 완성 HTML

```html
<!doctype html>
<html lang="ko">
    <head>
        <meta charset="UTF-8">

        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        >

        <meta
            name="description"
            content="HTML, CSS, JavaScript 기반 실무형 Frontend 국비교육 과정을 소개합니다."
        >

        <title>
            Frontend 국비교육 과정 | Developer Academy
        </title>

        <link
            rel="stylesheet"
            href="./assets/css/style.css"
        >
    </head>

    <body>
        <header class="site-header">
            <a
                href="./index.html"
                class="site-logo"
                aria-label="Developer Academy 홈"
            >
                Developer Academy
            </a>

            <nav aria-label="주요 메뉴">
                <ul class="site-nav">
                    <li>
                        <a
                            href="./index.html"
                            aria-current="page"
                        >
                            과정 소개
                        </a>
                    </li>

                    <li>
                        <a href="./projects.html">
                            프로젝트
                        </a>
                    </li>

                    <li>
                        <a href="./reviews.html">
                            수강 후기
                        </a>
                    </li>

                    <li>
                        <a href="#consultation">
                            상담 신청
                        </a>
                    </li>
                </ul>
            </nav>
        </header>

        <main>
            <section
                class="hero"
                aria-labelledby="hero-title"
            >
                <div class="hero__content">
                    <p>
                        실무 중심 Frontend Bootcamp
                    </p>

                    <h1 id="hero-title">
                        HTML부터 Portfolio까지
                        한 번에 완성하세요
                    </h1>

                    <p>
                        Semantic HTML,
                        Responsive CSS,
                        JavaScript DOM과
                        실무 Project를
                        단계적으로 학습합니다.
                    </p>

                    <div class="hero__actions">
                        <a href="#course-list">
                            과정 살펴보기
                        </a>

                        <a href="#consultation">
                            상담 신청하기
                        </a>
                    </div>
                </div>

                <figure>
                    <img
                        src="./assets/images/classroom.webp"
                        alt="수강생들이 노트북으로 Frontend Project를 실습하는 교실"
                        width="1200"
                        height="800"
                    >

                    <figcaption>
                        실습 중심 Frontend 수업
                    </figcaption>
                </figure>
            </section>

            <section
                id="course-list"
                aria-labelledby="course-list-title"
            >
                <header>
                    <p>
                        Curriculum
                    </p>

                    <h2 id="course-list-title">
                        학습 과정
                    </h2>
                </header>

                <div class="course-grid">
                    <article class="course-card">
                        <img
                            src="./assets/images/html-course.webp"
                            alt=""
                            width="640"
                            height="360"
                        >

                        <h3>
                            HTML
                        </h3>

                        <p>
                            Semantic Markup과
                            접근성을 학습합니다.
                        </p>

                        <ul>
                            <li>Document Structure</li>
                            <li>Semantic HTML</li>
                            <li>Form</li>
                            <li>Accessibility</li>
                        </ul>

                        <a href="./courses/html.html">
                            HTML 과정 자세히 보기
                        </a>
                    </article>

                    <article class="course-card">
                        <img
                            src="./assets/images/css-course.webp"
                            alt=""
                            width="640"
                            height="360"
                        >

                        <h3>
                            CSS
                        </h3>

                        <p>
                            Responsive Layout과
                            UI Styling을 학습합니다.
                        </p>

                        <ul>
                            <li>Box Model</li>
                            <li>Flexbox</li>
                            <li>Responsive Web</li>
                            <li>Transition</li>
                        </ul>

                        <a href="./courses/css.html">
                            CSS 과정 자세히 보기
                        </a>
                    </article>

                    <article class="course-card">
                        <img
                            src="./assets/images/javascript-course.webp"
                            alt=""
                            width="640"
                            height="360"
                        >

                        <h3>
                            JavaScript
                        </h3>

                        <p>
                            DOM과 Event를 이용한
                            동적 UI를 학습합니다.
                        </p>

                        <ul>
                            <li>Variable</li>
                            <li>Function</li>
                            <li>Array</li>
                            <li>DOM</li>
                        </ul>

                        <a href="./courses/javascript.html">
                            JavaScript 과정 자세히 보기
                        </a>
                    </article>
                </div>
            </section>

            <section
                aria-labelledby="learning-flow-title"
            >
                <h2 id="learning-flow-title">
                    학습 진행 순서
                </h2>

                <ol>
                    <li>HTML 문서 구조 이해</li>
                    <li>CSS Layout 구현</li>
                    <li>JavaScript Interaction 구현</li>
                    <li>Portfolio Project 제작</li>
                    <li>Code Review와 Refactoring</li>
                </ol>
            </section>

            <section
                aria-labelledby="schedule-title"
            >
                <h2 id="schedule-title">
                    주간 시간표
                </h2>

                <div class="table-scroll">
                    <table>
                        <caption>
                            Frontend 과정 주간 학습 일정
                        </caption>

                        <thead>
                            <tr>
                                <th scope="col">
                                    요일
                                </th>

                                <th scope="col">
                                    오전
                                </th>

                                <th scope="col">
                                    오후
                                </th>
                            </tr>
                        </thead>

                        <tbody>
                            <tr>
                                <th scope="row">
                                    월요일
                                </th>

                                <td>
                                    HTML
                                </td>

                                <td>
                                    HTML 실습
                                </td>
                            </tr>

                            <tr>
                                <th scope="row">
                                    화요일
                                </th>

                                <td>
                                    CSS
                                </td>

                                <td>
                                    Flexbox
                                </td>
                            </tr>

                            <tr>
                                <th scope="row">
                                    수요일
                                </th>

                                <td>
                                    JavaScript
                                </td>

                                <td>
                                    DOM 실습
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </section>

            <section
                aria-labelledby="media-title"
            >
                <h2 id="media-title">
                    수업 미리보기
                </h2>

                <figure>
                    <img
                        src="./assets/images/project-review.webp"
                        alt="강사가 대형 화면으로 수강생 Project를 Code Review하는 모습"
                        width="1200"
                        height="800"
                    >

                    <figcaption>
                        매주 진행하는 Project Code Review
                    </figcaption>
                </figure>

                <video
                    controls
                    preload="metadata"
                >
                    <source
                        src="./assets/media/course-preview.webm"
                        type="video/webm"
                    >

                    <source
                        src="./assets/media/course-preview.mp4"
                        type="video/mp4"
                    >

                    <track
                        src="./assets/media/course-preview-ko.vtt"
                        kind="captions"
                        srclang="ko"
                        label="한국어"
                        default
                    >

                    Browser가 Video 재생을 지원하지 않습니다.
                </video>
            </section>

            <aside
                aria-labelledby="notice-title"
            >
                <h2 id="notice-title">
                    수강 전 확인
                </h2>

                <p>
                    국비지원 자격은 개인 상황에 따라
                    달라질 수 있습니다.
                </p>
            </aside>

            <section
                id="consultation"
                aria-labelledby="consultation-title"
            >
                <h2 id="consultation-title">
                    상담 신청
                </h2>

                <form
                    action="/api/consultation"
                    method="post"
                >
                    <div class="form-field">
                        <label for="name">
                            이름
                        </label>

                        <input
                            type="text"
                            id="name"
                            name="name"
                            autocomplete="name"
                            required
                        >
                    </div>

                    <div class="form-field">
                        <label for="email">
                            Email
                        </label>

                        <input
                            type="email"
                            id="email"
                            name="email"
                            autocomplete="email"
                            required
                        >
                    </div>

                    <div class="form-field">
                        <label for="phone">
                            전화번호
                        </label>

                        <input
                            type="tel"
                            id="phone"
                            name="phone"
                            autocomplete="tel"
                            placeholder="010-1234-5678"
                        >
                    </div>

                    <div class="form-field">
                        <label for="course">
                            관심 과정
                        </label>

                        <select
                            id="course"
                            name="course"
                            required
                        >
                            <option value="">
                                선택해 주세요
                            </option>

                            <option value="frontend">
                                Frontend
                            </option>

                            <option value="backend">
                                Backend
                            </option>

                            <option value="fullstack">
                                Full Stack
                            </option>
                        </select>
                    </div>

                    <fieldset>
                        <legend>
                            상담 방식
                        </legend>

                        <label>
                            <input
                                type="radio"
                                name="consultation_type"
                                value="phone"
                                checked
                            >
                            전화 상담
                        </label>

                        <label>
                            <input
                                type="radio"
                                name="consultation_type"
                                value="visit"
                            >
                            방문 상담
                        </label>

                        <label>
                            <input
                                type="radio"
                                name="consultation_type"
                                value="online"
                            >
                            온라인 상담
                        </label>
                    </fieldset>

                    <fieldset>
                        <legend>
                            학습 목적
                        </legend>

                        <label>
                            <input
                                type="checkbox"
                                name="goal"
                                value="employment"
                            >
                            취업
                        </label>

                        <label>
                            <input
                                type="checkbox"
                                name="goal"
                                value="portfolio"
                            >
                            Portfolio
                        </label>

                        <label>
                            <input
                                type="checkbox"
                                name="goal"
                                value="skill-up"
                            >
                            실무 역량 향상
                        </label>
                    </fieldset>

                    <div class="form-field">
                        <label for="message">
                            상담 내용
                        </label>

                        <textarea
                            id="message"
                            name="message"
                            rows="6"
                            maxlength="1000"
                            placeholder="궁금한 내용을 입력해 주세요."
                        ></textarea>
                    </div>

                    <label>
                        <input
                            type="checkbox"
                            name="privacy_agree"
                            value="yes"
                            required
                        >
                        개인정보 수집 및 이용에 동의합니다.
                    </label>

                    <button type="submit">
                        상담 신청
                    </button>
                </form>
            </section>

            <section
                aria-labelledby="faq-title"
            >
                <h2 id="faq-title">
                    자주 묻는 질문
                </h2>

                <details>
                    <summary>
                        비전공자도 수강할 수 있나요?
                    </summary>

                    <p>
                        기초 과정부터 진행하므로
                        비전공자도 참여할 수 있습니다.
                    </p>
                </details>

                <details>
                    <summary>
                        Portfolio Project가 포함되나요?
                    </summary>

                    <p>
                        과정 후반부에 Team·개인 Project를
                        진행합니다.
                    </p>
                </details>
            </section>
        </main>

        <footer class="site-footer">
            <div>
                <strong>
                    Developer Academy
                </strong>

                <address>
                    충청남도 천안시 Example Road 10<br>

                    대표 전화:
                    <a href="tel:+82410000000">
                        041-000-0000
                    </a>
                </address>
            </div>

            <nav aria-label="Footer 메뉴">
                <ul>
                    <li>
                        <a href="./privacy.html">
                            개인정보 처리방침
                        </a>
                    </li>

                    <li>
                        <a href="./terms.html">
                            이용약관
                        </a>
                    </li>
                </ul>
            </nav>

            <p>
                &copy; 2026 Developer Academy
            </p>
        </footer>
    </body>
</html>
```

---

# 44. 사용된 HTML 개념

| 학습 범위 | 적용 위치 |
| --- | --- |
| 기본 문서 | `doctype`, `html`, `head`, `body` |
| Metadata | `lang`, `charset`, `viewport`, `description`, `title` |
| Text | `h1`~`h3`, `p`, `strong`, `abbr`, `time` |
| Link | Navigation, Fragment, 전화, Download |
| List | Course Stack, 학습 순서, Footer Navigation |
| 설명 목록 | 교육 기간·방식 정보 |
| Table | 주간 시간표 |
| Image | Hero, 과정 Card, 수업 Media |
| Media | `video`, `source`, `track`, `iframe` |
| Form | Text, Email, Tel, Select, Radio, Checkbox, Textarea |
| Form Group | `fieldset`, `legend` |
| Semantic | `header`, `nav`, `main`, `section`, `article`, `aside`, `footer` |
| 접근성 | `alt`, `aria-current`, `aria-labelledby`, `scope`, Label |
| 실무 작성 | 역할 Class, 고유 ID, 상대 경로, Meaning-first Markup |

---

# 45. 왜 이런 구조를 사용하는가?

## 45.1 Page 역할이 분명하다

```text
header
→ Site Header

nav
→ 주요 Navigation

main
→ 핵심 Content

section
→ 각 주제 영역

article
→ 독립 과정 Card

aside
→ 보조 안내

footer
→ Site 마무리 정보
```

## 45.2 CSS 없이도 읽기 쉽다

DOM 순서가 실제 읽는 순서와 같다.

## 45.3 JavaScript가 없어도 기본 기능이 가능하다

- Link는 기본 이동 가능
- Form은 기본 Submit 가능
- `details`는 기본 Toggle 가능
- Native Control은 Keyboard 조작 가능

Progressive Enhancement에 유리하다.

---

# 46. 대표 오류와 해결

## 46.1 `h1`이 여러 개라서 무조건 오류인가?

HTML5에서 여러 `h1` 자체가 문법 오류는 아니지만 Page 전체 정보 계층을 명확하게 만들기 위해 대표 제목 하나를 두고 하위 Heading을 계층적으로 구성하는 방식이 이해하기 쉽다.

## 46.2 `section` 안에 Heading이 없음

독립된 주제가 아니라 단순 Wrapper인지 먼저 확인한다.

필요하다면 `div`로 변경한다.

## 46.3 Image `alt`가 중복됨

Card 제목과 Link Text가 이미 같은 정보를 제공하면 장식 Image에 `alt=""`를 검토한다.

## 46.4 Form 값이 Server로 안 감

다음을 확인한다.

```text
name 존재 여부
disabled 여부
Control이 Form 내부인지
Submit Button 동작
Server Endpoint
```

## 46.5 Radio가 여러 개 동시에 선택됨

같은 Group이면 동일한 `name`을 사용한다.

## 46.6 Label 클릭이 Input과 연결되지 않음

`label for`와 `input id`가 정확히 일치하는지 확인한다.

## 46.7 Table Header 관계가 모호함

`scope="col"`과 `scope="row"`를 확인한다.

## 46.8 Fragment Link가 이동하지 않음

`href="#id"`와 대상 `id` 값이 일치하는지 확인한다.

---

# 47. Validator 검수 항목

- Duplicate ID
- 잘못된 Element 중첩
- 닫는 Tag 오류
- 잘못된 Attribute
- Table 구조 오류
- Form 관련 구조 오류
- `details`·`summary` 관계
- Unknown Element

Validator가 통과해도 접근성과 UX가 자동으로 보장되는 것은 아니다.

---

# 48. 접근성 검수 항목

- Keyboard만으로 Navigation 가능
- Focus 순서가 DOM 순서와 일치
- Heading 구조가 Page Contents를 설명
- Landmark가 과도하지 않음
- 모든 Form Control에 Label 존재
- Image `alt`가 목적에 맞음
- Table Header 관계가 명확함
- Video Caption 제공
- Icon-only Control에 Accessible Name 제공
- 현재 Page Link에 상태 정보 제공

---

# 49. DevTools 검수 항목

```text
Elements
→ Browser가 보정한 실제 DOM 확인

Accessibility
→ Role·Name·State 확인

Network
→ Image·Video·CSS 404 확인

Console
→ Resource·Script 오류 확인
```

---

# 50. 확장 과제

- Mobile Navigation Toggle 추가
- Skip Link 추가
- Breadcrumb 추가
- 실제 Course Detail Page 제작
- Form Error Message 연결
- `aria-live` 기반 제출 결과 Message
- Dark Mode Toggle
- Search Form
- 실제 YouTube Embed 연결
- 실제 PDF Download
- Schema.org Structured Data 검토

---

# 51. 리팩토링 과제

다음처럼 Project 구조를 분리한다.

```text
project/
├── index.html
├── courses/
│   ├── html.html
│   ├── css.html
│   └── javascript.html
├── projects.html
├── reviews.html
├── privacy.html
├── terms.html
└── assets/
    ├── css/
    │   └── style.css
    ├── js/
    │   └── main.js
    ├── images/
    ├── media/
    └── files/
```

각 Page의 상대 경로를 다시 계산한다.

---

# 52. 종합실습 체크리스트

- [ ] `doctype`을 작성했는가?
- [ ] `lang="ko"`를 작성했는가?
- [ ] `charset`, `viewport`, `title`, `description`이 있는가?
- [ ] Page 대표 Heading이 명확한가?
- [ ] Heading 계층이 자연스러운가?
- [ ] `main`이 하나의 핵심 Content 영역을 나타내는가?
- [ ] 주요 Navigation에 `nav`를 사용하는가?
- [ ] Navigation Item을 List로 구성했는가?
- [ ] 현재 Page에 `aria-current`를 제공했는가?
- [ ] 단순 Wrapper와 `section`을 구분했는가?
- [ ] 독립 Course Card에 `article`을 사용했는가?
- [ ] 보조 안내에 `aside`를 사용했는가?
- [ ] Link와 Button 역할을 구분했는가?
- [ ] Fragment Link와 대상 ID가 일치하는가?
- [ ] 상대 경로를 현재 File 위치 기준으로 계산했는가?
- [ ] Image `alt`가 목적에 맞는가?
- [ ] 장식 Image에 `alt=""`를 검토했는가?
- [ ] Image `width`, `height`를 비율에 맞게 제공했는가?
- [ ] Video에 `controls`를 제공했는가?
- [ ] Video Caption을 검토했는가?
- [ ] `iframe`에 `title`을 제공했는가?
- [ ] 순서 있는 절차에 `ol`을 사용했는가?
- [ ] 이름·값 정보에 `dl`을 사용했는가?
- [ ] Table에 `caption`을 제공했는가?
- [ ] Table Header에 `scope`를 사용했는가?
- [ ] Form Control에 Label을 연결했는가?
- [ ] Form 제출 Control에 `name`이 있는가?
- [ ] `id`가 중복되지 않는가?
- [ ] Radio Group이 같은 `name`을 사용하는가?
- [ ] Checkbox에 의미 있는 `value`가 있는가?
- [ ] `fieldset`, `legend`로 관련 Group을 묶었는가?
- [ ] Placeholder를 Label 대신 사용하지 않는가?
- [ ] Form Button의 `type`을 명시했는가?
- [ ] POST와 HTTPS의 역할을 구분하는가?
- [ ] 개인정보 Form에서 Server Validation을 전제로 하는가?
- [ ] `details` 안에 `summary`를 올바르게 사용했는가?
- [ ] 반복 `<br>`로 Layout을 만들지 않는가?
- [ ] Comment에 민감 정보를 남기지 않는가?
- [ ] Validator로 Markup 오류를 확인했는가?
- [ ] Keyboard와 Accessibility Tree를 확인했는가?

---

# 53. 핵심 요약

```text
Document
→ Metadata
→ Semantic Structure
```

```text
Content
→ Heading
→ Paragraph
→ Link
→ List
→ Table
→ Media
→ Form
```

```text
Accessibility
→ alt
→ label
→ scope
→ aria-current
→ aria-labelledby
```

```text
Project Quality
→ 의미 있는 File Name
→ 상대 경로
→ Native Element 우선
→ Validator
→ DevTools
```

---

# 마무리

HTML 종합실습의 핵심은 많은 Tag를 한 Page에 넣는 것이 아니다.

```text
Page 목적을 먼저 정의하고
    ↓
Content를 의미 단위로 나누고
    ↓
Heading과 Landmark를 설계하고
    ↓
Link·List·Table·Media·Form을 역할에 맞게 선택하고
    ↓
접근성 정보를 연결하고
    ↓
CSS와 JavaScript 없이도 이해 가능한 문서를 만들고
    ↓
Validator와 실제 Browser에서 검수하는 것
```

이 구조를 이해하고 직접 수정할 수 있다면 HTML Tag를 암기하는 단계를 넘어, 실제 Web Page의 정보 구조와 접근성을 설계할 수 있다.
