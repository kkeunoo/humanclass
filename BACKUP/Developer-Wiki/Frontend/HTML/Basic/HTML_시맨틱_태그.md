---
title: HTML 시맨틱 태그
version: v1.0
last_updated: 2026-07-21
status: Completed
---

# HTML 시맨틱 태그

## 개요

시맨틱(Semantic)은 '의미를 가진'이라는 뜻이다.

HTML에서 시맨틱 태그는 **요소가 화면에서 어떻게 보이는지가 아니라, 어떤 역할과 의미를 가지는지**를 나타낸다.

예를 들어 다음 두 코드는 화면에서는 비슷하게 보일 수 있다.

```html
<div class="header">
    ...
</div>
```

```html
<header>
    ...
</header>
```

하지만 `<header>`는 "이 영역은 문서 또는 섹션의 머리글"이라는 의미를 브라우저, 검색 엔진, 화면 낭독기에 전달한다.

---

# 핵심 개념

시맨틱 태그는 다음과 같은 장점을 가진다.

- 문서 구조를 명확하게 표현한다.
- 검색 엔진이 페이지를 이해하기 쉽다.
- 화면 낭독기가 페이지를 탐색하기 쉽다.
- 유지보수가 쉬워진다.
- 협업 시 구조를 빠르게 파악할 수 있다.

---

# div와 시맨틱 태그의 차이

`<div>`는 의미가 없는 일반 컨테이너이다.

```html
<div class="content">
</div>
```

반면 시맨틱 태그는 역할을 가진다.

```html
<main>

</main>
```

`main`이라는 이름만으로도 주요 콘텐츠라는 의미를 알 수 있다.

---

# HTML5 주요 시맨틱 태그

| 태그 | 의미 |
|------|------|
| header | 머리글 |
| nav | 내비게이션 |
| main | 주요 콘텐츠 |
| section | 주제별 구역 |
| article | 독립적인 콘텐츠 |
| aside | 부가 정보 |
| footer | 바닥글 |
| address | 연락처 정보 |
| figure | 독립 콘텐츠 |
| figcaption | 설명 |

---

# header

문서나 섹션의 머리 영역이다.

```html
<header>

    <h1>

        Developer Academy

    </h1>

</header>
```

주로 포함되는 요소

- 로고
- 제목
- 메뉴
- 검색

---

# nav

탐색 메뉴를 의미한다.

```html
<nav>

    <ul>

        <li><a href="/">홈</a></li>

        <li><a href="/courses">교육 과정</a></li>

    </ul>

</nav>
```

모든 링크를 `nav`에 넣는 것은 아니다.

주요 탐색 메뉴에 사용한다.

---

# main

문서의 핵심 콘텐츠이다.

```html
<main>

</main>
```

한 문서에는 일반적으로 하나만 사용한다.

---

# section

관련 내용을 하나의 주제로 묶는다.

```html
<section>

    <h2>

        교육 과정

    </h2>

</section>
```

주제가 있다면 section을 고려한다.

가능하면 제목(`h2`~`h6`)을 함께 사용하는 것이 좋다.

---

# article

독립적으로 배포하거나 재사용 가능한 콘텐츠이다.

예

- 게시글
- 뉴스
- 상품
- 댓글
- 블로그 글

```html
<article>

    <h2>

        HTML 입문

    </h2>

</article>
```

---

# article과 section 차이

section

↓

주제별 구역

article

↓

독립적인 콘텐츠

예

```text
교육 과정(section)

├ HTML(article)

├ CSS(article)

└ JavaScript(article)
```

---

# aside

부가 정보이다.

```html
<aside>

    최근 게시글

</aside>
```

예

- 광고
- 추천 글
- 사이드바
- 관련 링크

---

# footer

문서나 섹션의 바닥글이다.

```html
<footer>

    Copyright

</footer>
```

주로

- 회사 정보
- 저작권
- 개인정보 처리방침
- SNS

---

# address

연락처 정보이다.

```html
<address>

    contact@example.com

</address>
```

회사 주소

이메일

전화번호 등에 사용한다.

---

# section을 사용하면 안 되는 경우

스타일을 위한 단순 그룹

```html
<section>

    <button>

```

주제가 없다면 div가 적절할 수 있다.

---

# article을 사용하면 안 되는 경우

단순 레이아웃

```html
<article>

<div>

</article>
```

독립성이 없다면 section 또는 div가 적절하다.

---

# 제목 구조

좋은 구조

```text
h1

├ h2

│ ├ h3

│ └ h3

└ h2
```

제목 단계는 문서의 계층을 표현한다.

---

# 랜드마크(Landmark)

대표적인 랜드마크 요소

- header
- nav
- main
- aside
- footer

화면 낭독기 사용자는 랜드마크를 이용해 주요 영역으로 빠르게 이동할 수 있다.

---

# aria-label

랜드마크가 여러 개인 경우 구분할 수 있다.

```html
<nav aria-label="주요 메뉴">

</nav>

<nav aria-label="푸터 메뉴">

</nav>
```

---

# SEO와 시맨틱 태그

검색 엔진은 시맨틱 구조를 참고하여 문서를 이해한다.

다음 요소들이 중요하다.

- h1~h6
- header
- main
- article
- nav

시맨틱 태그만으로 검색 순위가 결정되는 것은 아니지만 문서 구조를 이해하는 데 도움이 된다.

---

# 실무 활용

대표적인 구성

- 기업 홈페이지
- 쇼핑몰
- 블로그
- 관리자 페이지
- 뉴스 사이트

---

# 실무 예제 프로젝트

```html
<body>

<header>

    <a href="/">

        <img
            src="./images/logo.svg"
            alt="Developer Academy 홈"
        >

    </a>

    <nav aria-label="주요 메뉴">

        <ul>

            <li><a href="/">홈</a></li>

            <li><a href="/courses">교육 과정</a></li>

            <li><a href="/projects">프로젝트</a></li>

            <li><a href="/contact">문의</a></li>

        </ul>

    </nav>

</header>

<main>

    <section>

        <h1>

            실무 중심 웹 개발자 과정

        </h1>

        <p>

            취업까지 연결되는 교육

        </p>

    </section>

    <section>

        <h2>

            교육 과정

        </h2>

        <article>

            <h3>

                HTML

            </h3>

        </article>

        <article>

            <h3>

                CSS

            </h3>

        </article>

        <article>

            <h3>

                JavaScript

            </h3>

        </article>

    </section>

    <aside>

        <h2>

            공지사항

        </h2>

    </aside>

</main>

<footer>

    <address>

        contact@example.com

    </address>

</footer>

</body>
```

---

# 예제 구조 분석

```text
body
├── header
│   ├── a
│   └── nav
├── main
│   ├── section
│   ├── section
│   │   ├── article
│   │   ├── article
│   │   └── article
│   └── aside
└── footer
    └── address
```

---

# 이번 문서에서 새롭게 배운 내용

| 개념 | 설명 |
|------|------|
| Semantic | 의미를 가진 마크업 |
| header | 머리글 |
| nav | 주요 탐색 |
| main | 주요 콘텐츠 |
| section | 주제별 영역 |
| article | 독립 콘텐츠 |
| aside | 부가 정보 |
| footer | 바닥글 |
| address | 연락처 |
| Landmark | 접근성 주요 영역 |
| aria-label | 랜드마크 이름 |

---

# 자주 하는 실수

## 1.

모든 요소를 div로 만든다.

→ 의미 있는 시맨틱 태그를 우선 고려한다.

---

## 2.

main을 여러 개 사용한다.

일반적으로 문서에는 하나의 `<main>`만 사용한다.

---

## 3.

section에 제목이 없다.

주제 구역이라면 제목을 함께 제공하는 것이 좋다.

---

## 4.

article을 단순 레이아웃에 사용한다.

독립성이 있는 콘텐츠에 사용한다.

---

## 5.

모든 링크를 nav에 넣는다.

주요 탐색 링크에 사용한다.

---

## 6.

footer를 화면 맨 아래라는 이유만으로 사용한다.

섹션 내부의 바닥글에도 사용할 수 있다.

---

## 7.

address에 일반 주소만 작성한다.

작성자나 조직의 연락처 정보를 표현하는 데 사용한다.

---

## 8.

제목 단계를 건너뛴다.

```text
h1

↓

h4
```

문서 구조가 이해하기 어려워질 수 있다.

---

## 9.

aside를 본문으로 사용한다.

본문의 핵심 내용은 `main`, `section`, `article`에 작성한다.

---

## 10.

랜드마크를 구분하지 않는다.

여러 `nav`가 있다면 `aria-label`을 사용하여 구분한다.

---

# 면접 포인트

### Q1.

시맨틱 태그란 무엇인가요?

→ 요소의 역할과 의미를 나타내는 HTML 태그이다.

---

### Q2.

div와 section의 차이는?

→ div는 의미 없는 컨테이너이고, section은 하나의 주제를 가진 영역이다.

---

### Q3.

section과 article의 차이는?

→ section은 주제별 구역, article은 독립적으로 재사용 가능한 콘텐츠이다.

---

### Q4.

main은 왜 하나만 사용하나요?

→ 문서의 핵심 콘텐츠를 나타내는 랜드마크이기 때문이다.

---

### Q5.

nav는 언제 사용하나요?

→ 주요 탐색 메뉴를 나타낼 때 사용한다.

---

### Q6.

SEO에 시맨틱 태그가 도움이 되나요?

→ 문서 구조를 이해하는 데 도움이 된다.

---

### Q7.

aside는 언제 사용하나요?

→ 광고, 추천 글, 관련 링크 등 부가 콘텐츠에 사용한다.

---

### Q8.

footer는 어디에서 사용할 수 있나요?

→ 문서 전체뿐 아니라 article, section 내부에서도 사용할 수 있다.

---

### Q9.

랜드마크란 무엇인가요?

→ 화면 낭독기가 주요 영역을 빠르게 탐색할 수 있도록 제공하는 구조이다.

---

### Q10.

aria-label은 왜 사용하나요?

→ 여러 랜드마크를 구분하기 위해 사용한다.

---

# 핵심 정리

- 시맨틱 태그는 요소의 의미를 표현한다.
- `div`는 의미 없는 컨테이너이다.
- `header`, `nav`, `main`, `section`, `article`, `aside`, `footer`, `address`는 대표적인 시맨틱 태그이다.
- `section`은 주제를 가진 영역, `article`은 독립적인 콘텐츠에 적합하다.
- 문서에는 일반적으로 하나의 `main`을 사용한다.
- `nav`는 주요 탐색 링크에 사용한다.
- 제목 구조(`h1`~`h6`)는 문서 계층을 표현한다.
- 랜드마크는 접근성과 탐색성을 향상시킨다.
- `aria-label`은 여러 랜드마크를 구분하는 데 도움을 준다.
- 시맨틱 마크업은 유지보수, 접근성, SEO에 긍정적인 영향을 준다.

---

# 변경 이력

| Version | 날짜 | 변경 내용 |
|------|------|----------|
| v1.0 | 2026-07-21 | 최초 작성 |
| v1.0 | 2026-07-21 | 주요 시맨틱 태그 정리 |
| v1.0 | 2026-07-21 | section과 article 비교 추가 |
| v1.0 | 2026-07-21 | 랜드마크와 접근성 설명 추가 |
| v1.0 | 2026-07-21 | SEO와 시맨틱 태그 관계 정리 |
| v1.0 | 2026-07-21 | 실무 예제 및 구조 분석 추가 |
| v1.0 | 2026-07-21 | 자주 하는 실수와 면접 포인트 추가 |