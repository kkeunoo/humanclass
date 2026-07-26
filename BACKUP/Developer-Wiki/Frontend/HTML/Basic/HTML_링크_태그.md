---
title: HTML 링크 태그
version: v1.0
last_updated: 2026-07-21
status: Completed
---

# HTML 링크 태그

## 개요

링크는 현재 문서에서 다른 문서, 웹사이트, 파일 또는 같은 페이지의 특정 위치로 이동할 수 있게 해 주는 기능이다.

웹 페이지들이 서로 연결될 수 있는 이유도 링크가 있기 때문이다.

HTML에서는 링크를 만들기 위해 `<a>` 태그를 사용한다.

```html
<a href="https://example.com">
    Example 사이트
</a>
```

`<a>`는 Anchor의 약자이며, `href` 속성에 이동할 주소를 지정한다.

링크는 다음과 같은 곳에서 사용한다.

- 내비게이션 메뉴
- 로고
- 게시글 제목
- 상품 카드
- 배너
- 외부 웹사이트
- 이메일 주소
- 전화번호
- 파일 다운로드
- 페이지 내부 목차
- 이전 페이지와 다음 페이지 이동

링크는 단순히 글자에 밑줄을 표시하는 기능이 아니라 사용자를 다른 위치나 자원으로 이동시키는 의미를 가진다.

---

# 핵심 개념

## 기본 구조

```html
<a href="이동할 주소">
    사용자에게 표시할 내용
</a>
```

예시

```html
<a href="https://www.google.com">
    Google
</a>
```

각 부분의 역할은 다음과 같다.

| 부분 | 역할 |
|---|---|
| `<a>` | 링크를 만드는 요소 |
| `href` | 링크가 이동할 위치 |
| 링크 텍스트 | 사용자가 링크의 목적을 이해할 수 있는 내용 |

---

# `<a>` 태그

## Anchor 요소

`<a>`는 Anchor의 약자로, 다른 위치나 자원을 연결하는 하이퍼링크를 만든다.

```html
<a href="./about.html">
    회사 소개
</a>
```

`<a>` 내부에는 텍스트뿐 아니라 이미지와 다른 요소도 포함할 수 있다.

```html
<a href="./index.html">
    <img
        src="./images/logo.png"
        alt="Developer Academy 홈"
    >
</a>
```

링크 내부 콘텐츠는 사용자가 클릭할 수 있는 영역이 된다.

---

# `href` 속성

`href`는 Hypertext Reference의 약자로, 링크가 이동할 주소를 지정한다.

```html
<a href="./courses.html">
    교육 과정
</a>
```

대표적인 `href` 값은 다음과 같다.

| 형태 | 의미 |
|---|---|
| `https://example.com` | 외부 웹사이트 |
| `./about.html` | 현재 위치를 기준으로 한 파일 |
| `../index.html` | 상위 폴더에 있는 파일 |
| `/courses` | 현재 사이트의 루트 기준 경로 |
| `#contact` | 같은 문서의 특정 위치 |
| `mailto:user@example.com` | 이메일 작성 |
| `tel:01012345678` | 전화 연결 |
| `./files/guide.pdf` | 파일 또는 문서 연결 |

---

# 링크 텍스트

링크 텍스트는 사용자가 클릭했을 때 어디로 이동하는지 이해할 수 있어야 한다.

## 의미가 명확한 링크

```html
<a href="./courses.html">
    전체 교육 과정 보기
</a>
```

```html
<a href="./portfolio.html">
    수강생 포트폴리오 확인하기
</a>
```

## 의미가 불명확한 링크

```html
<a href="./courses.html">
    클릭
</a>
```

```html
<a href="./portfolio.html">
    자세히
</a>
```

`클릭`, `여기`, `자세히`처럼 단독으로는 목적을 알기 어려운 문구는 접근성과 사용성 측면에서 좋지 않을 수 있다.

여러 링크에서 `자세히 보기`를 반복해야 한다면 주변 문맥이나 접근 가능한 이름을 통해 목적을 구분해야 한다.

```html
<article>
    <h2>프론트엔드 개발 과정</h2>

    <p>
        HTML, CSS, JavaScript와 React를 학습합니다.
    </p>

    <a href="./frontend-course.html">
        프론트엔드 개발 과정 자세히 보기
    </a>
</article>
```

---

# 내부 링크

내부 링크는 같은 웹사이트 안의 다른 페이지로 이동하는 링크이다.

```html
<a href="./about.html">
    회사 소개
</a>
```

```html
<a href="./courses/frontend.html">
    프론트엔드 과정
</a>
```

내부 링크에서는 일반적으로 상대 경로나 사이트 루트 기준 경로를 사용할 수 있다.

```html
<a href="/courses">
    교육 과정
</a>
```

사이트 개발 환경과 배포 방식에 따라 경로 작성 방법은 달라질 수 있다.

---

# 외부 링크

외부 링크는 현재 사이트가 아닌 다른 웹사이트로 이동하는 링크이다.

```html
<a href="https://github.com">
    GitHub
</a>
```

외부 주소는 일반적으로 프로토콜을 포함한 전체 URL을 작성한다.

```html
<a href="https://developer.mozilla.org">
    MDN Web Docs
</a>
```

다음처럼 프로토콜을 생략하면 현재 사이트 내부의 경로로 해석될 수 있다.

```html
<a href="developer.mozilla.org">
    MDN Web Docs
</a>
```

외부 사이트로 이동하려면 일반적으로 `https://`를 포함한다.

---

# URL의 기본 구조

URL은 웹상의 자원 위치를 나타낸다.

```text
https://example.com:443/courses/html?level=basic#intro
```

각 부분은 다음과 같다.

| 부분 | 예시 | 의미 |
|---|---|---|
| 프로토콜 | `https` | 통신 방식 |
| 도메인 | `example.com` | 웹사이트 주소 |
| 포트 | `443` | 서버 접속 포트 |
| 경로 | `/courses/html` | 자원의 위치 |
| 쿼리 문자열 | `?level=basic` | 추가 요청 정보 |
| 프래그먼트 | `#intro` | 문서 내부 위치 |

일반적인 링크에서는 다음과 같이 사용한다.

```html
<a href="https://example.com/courses/html?level=basic#intro">
    HTML 기초 과정
</a>
```

---

# 절대 경로

절대 경로는 자원의 위치를 완전한 주소로 작성하는 방식이다.

```html
<a href="https://example.com/about.html">
    회사 소개
</a>
```

외부 웹사이트에 연결할 때 주로 사용한다.

```html
<a href="https://github.com/example">
    GitHub 프로필
</a>
```

## 절대 URL의 특징

- 프로토콜부터 전체 주소를 작성한다.
- 현재 HTML 파일의 위치와 관계없이 같은 주소를 가리킨다.
- 외부 사이트 연결에 적합하다.
- 도메인이 변경되면 링크도 수정해야 한다.

---

# 상대 경로

상대 경로는 현재 HTML 파일의 위치를 기준으로 다른 파일의 위치를 작성하는 방식이다.

다음 프로젝트 구조를 기준으로 살펴본다.

```text
project/
├── index.html
├── about.html
├── courses/
│   ├── frontend.html
│   └── backend.html
├── images/
│   └── logo.png
└── contact/
    └── index.html
```

---

## 같은 폴더의 파일

현재 파일이 `index.html`이고 같은 폴더의 `about.html`로 이동하려면 다음과 같이 작성한다.

```html
<a href="./about.html">
    회사 소개
</a>
```

다음처럼 `./`를 생략할 수도 있다.

```html
<a href="about.html">
    회사 소개
</a>
```

`./`는 현재 폴더를 의미한다.

---

## 하위 폴더의 파일

현재 파일이 루트의 `index.html`이고 `courses/frontend.html`로 이동하려면 다음과 같이 작성한다.

```html
<a href="./courses/frontend.html">
    프론트엔드 과정
</a>
```

```text
현재 위치
project/index.html

목적지
project/courses/frontend.html
```

현재 폴더에서 `courses` 폴더로 들어간 뒤 `frontend.html`을 찾는다.

---

## 상위 폴더의 파일

현재 파일이 `courses/frontend.html`이고 루트의 `index.html`로 이동하려면 다음과 같이 작성한다.

```html
<a href="../index.html">
    홈
</a>
```

`../`는 상위 폴더를 의미한다.

```text
현재 위치
project/courses/frontend.html

../
project/

목적지
project/index.html
```

---

## 상위 폴더의 다른 하위 폴더

현재 파일이 `courses/frontend.html`이고 `images/logo.png`를 연결하려면 다음과 같이 작성한다.

```html
<img
    src="../images/logo.png"
    alt="Developer Academy"
>
```

링크에서도 같은 방식으로 경로를 작성할 수 있다.

```html
<a href="../contact/index.html">
    문의하기
</a>
```

---

# 경로 기호 정리

| 경로 | 의미 |
|---|---|
| `./` | 현재 폴더 |
| `../` | 한 단계 상위 폴더 |
| `../../` | 두 단계 상위 폴더 |
| `/` | 웹사이트 루트 |
| `https://` | 전체 외부 주소 |

---

# 루트 상대 경로

슬래시(`/`)로 시작하는 경로는 일반적으로 현재 웹사이트의 루트를 기준으로 한다.

```html
<a href="/courses/frontend.html">
    프론트엔드 과정
</a>
```

현재 페이지가 어디에 있더라도 사이트 루트를 기준으로 경로를 해석한다.

```html
<a href="/">
    홈
</a>
```

다만 로컬에서 HTML 파일을 직접 실행하거나 특정 하위 경로에 배포하는 환경에서는 예상과 다르게 동작할 수 있다.

프로젝트의 서버 환경, 프레임워크, 배포 경로를 고려하여 사용해야 한다.

---

# 현재 경로와 사이트 루트의 차이

```html
<a href="./courses.html">
    교육 과정
</a>
```

현재 HTML 파일이 있는 폴더를 기준으로 한다.

```html
<a href="/courses.html">
    교육 과정
</a>
```

웹사이트의 최상위 루트를 기준으로 한다.

두 경로는 현재 파일의 위치에 따라 서로 다른 파일을 가리킬 수 있다.

---

# 같은 페이지 내부 이동

같은 페이지의 특정 위치로 이동하려면 `href`에 `#`과 대상 요소의 `id`를 작성한다.

```html
<a href="#curriculum">
    교육 과정으로 이동
</a>
```

이동할 대상에는 동일한 `id`를 지정한다.

```html
<section id="curriculum">
    <h2>교육 과정</h2>
</section>
```

전체 예시는 다음과 같다.

```html
<nav aria-label="페이지 목차">
    <ul>
        <li>
            <a href="#intro">과정 소개</a>
        </li>

        <li>
            <a href="#curriculum">교육 과정</a>
        </li>

        <li>
            <a href="#contact">문의하기</a>
        </li>
    </ul>
</nav>

<section id="intro">
    <h2>과정 소개</h2>
</section>

<section id="curriculum">
    <h2>교육 과정</h2>
</section>

<section id="contact">
    <h2>문의하기</h2>
</section>
```

---

# `id` 속성 사용 시 주의

하나의 HTML 문서에서 같은 `id`를 여러 요소에 반복해서 사용하면 안 된다.

## 잘못된 예

```html
<section id="course">
    <h2>프론트엔드 과정</h2>
</section>

<section id="course">
    <h2>백엔드 과정</h2>
</section>
```

## 올바른 예

```html
<section id="frontend-course">
    <h2>프론트엔드 과정</h2>
</section>

<section id="backend-course">
    <h2>백엔드 과정</h2>
</section>
```

`href="#frontend-course"`와 같이 대상의 고유한 `id`를 사용한다.

---

# 다른 페이지의 특정 위치로 이동

파일 경로 뒤에 `#id`를 함께 작성하면 다른 페이지의 특정 위치로 이동할 수 있다.

```html
<a href="./courses.html#frontend">
    프론트엔드 과정
</a>
```

대상 페이지

```html
<section id="frontend">
    <h2>프론트엔드 과정</h2>
</section>
```

---

# 페이지 상단으로 이동

문서 최상단에 특정 `id`를 지정할 수 있다.

```html
<body id="top">
```

하단에서 다음 링크를 제공한다.

```html
<a href="#top">
    페이지 상단으로 이동
</a>
```

빈 `href="#"`를 사용하는 방식도 있지만, 이동 목적을 명확하게 표현하려면 실제 대상 `id`를 사용하는 것이 좋다.

---

# `target` 속성

`target` 속성은 링크를 어디에서 열지 지정한다.

```html
<a
    href="https://github.com"
    target="_blank"
>
    GitHub
</a>
```

대표적인 값은 다음과 같다.

| 값 | 의미 |
|---|---|
| `_self` | 현재 창 또는 탭에서 열기 |
| `_blank` | 새 창 또는 새 탭에서 열기 |
| `_parent` | 부모 탐색 컨텍스트에서 열기 |
| `_top` | 최상위 탐색 컨텍스트에서 열기 |

일반적인 웹 페이지에서는 `_self`와 `_blank`를 주로 사용한다.

`target`을 작성하지 않으면 기본적으로 현재 탭에서 열린다.

---

# 새 탭으로 열기

```html
<a
    href="https://github.com"
    target="_blank"
>
    GitHub
</a>
```

`target="_blank"`는 브라우저 설정에 따라 새 탭이나 새 창으로 열릴 수 있다.

새 탭으로 열리는 링크는 사용자에게 이를 알리는 것이 도움이 될 수 있다.

```html
<a
    href="https://github.com"
    target="_blank"
    rel="noopener noreferrer"
>
    GitHub
    <span class="visually-hidden">
        새 탭에서 열림
    </span>
</a>
```

`visually-hidden` 클래스는 화면에서는 숨기되 화면 낭독기에는 전달되도록 CSS로 구현할 수 있다.

---

# `rel` 속성

`rel`은 현재 문서와 연결된 문서 사이의 관계를 나타낸다.

```html
<a
    href="https://github.com"
    target="_blank"
    rel="noopener noreferrer"
>
    GitHub
</a>
```

대표적인 값은 다음과 같다.

| 값 | 의미 |
|---|---|
| `noopener` | 새 페이지가 원래 페이지의 `window.opener`에 접근하지 못하도록 함 |
| `noreferrer` | 이동한 페이지에 현재 페이지의 참조 정보를 전달하지 않음 |
| `nofollow` | 검색 엔진에 링크를 따라가지 않도록 요청 |
| `external` | 외부 사이트 링크임을 표현 |
| `author` | 작성자 관련 페이지 |
| `license` | 라이선스 관련 페이지 |

---

## `noopener`

새 탭으로 열린 페이지가 원래 페이지의 창 객체에 접근하는 것을 제한한다.

```html
<a
    href="https://example.com"
    target="_blank"
    rel="noopener"
>
    외부 사이트
</a>
```

최신 브라우저에서는 `_blank` 링크에 `noopener` 동작이 기본 적용되는 경우가 많지만, 코드의 의도를 명확하게 표현하기 위해 작성할 수 있다.

---

## `noreferrer`

새 페이지에 현재 페이지의 주소와 관련된 참조 정보를 전달하지 않도록 한다.

```html
<a
    href="https://example.com"
    target="_blank"
    rel="noreferrer"
>
    외부 사이트
</a>
```

`noreferrer`는 분석 및 유입 경로 확인에 영향을 줄 수 있으므로 프로젝트 요구사항에 맞게 사용해야 한다.

무조건 모든 외부 링크에 적용하기보다는 보안과 분석 요구를 함께 고려한다.

---

## `nofollow`

검색 엔진에 해당 링크를 신뢰 또는 추천하는 링크로 처리하지 않도록 요청할 때 사용할 수 있다.

```html
<a
    href="https://example.com"
    rel="nofollow"
>
    외부 사이트
</a>
```

대표적으로 다음과 같은 상황에서 검토할 수 있다.

- 사용자 작성 콘텐츠
- 광고성 링크
- 신뢰 여부를 보장하기 어려운 링크

검색 엔진 정책과 프로젝트 요구사항을 확인하여 사용한다.

---

# 이메일 링크

`mailto:`를 사용하면 사용자의 기본 이메일 프로그램을 열 수 있다.

```html
<a href="mailto:contact@example.com">
    contact@example.com
</a>
```

제목과 본문을 미리 지정할 수도 있다.

```html
<a
    href="mailto:contact@example.com?subject=교육 과정 문의"
>
    이메일 문의
</a>
```

여러 쿼리 값을 연결할 때는 `&`를 HTML 문자 참조로 작성할 수 있다.

```html
<a
    href="mailto:contact@example.com?subject=교육 문의&amp;body=문의 내용을 작성해 주세요."
>
    이메일 문의
</a>
```

사용자의 기기에 이메일 프로그램이 설정되어 있지 않으면 기대한 동작을 하지 않을 수 있다.

---

# 전화 링크

`tel:`을 사용하면 전화 기능을 지원하는 기기에서 전화 연결을 시도할 수 있다.

```html
<a href="tel:0212345678">
    02-1234-5678
</a>
```

모바일 웹사이트의 고객센터나 매장 안내에서 자주 사용한다.

```html
<p>
    고객센터:
    <a href="tel:15881234">
        1588-1234
    </a>
</p>
```

`href` 값에는 공백과 구분 문자를 최소화한 번호를 사용할 수 있고, 화면에 표시되는 텍스트는 사용자가 읽기 편한 형태로 작성한다.

---

# 문자 메시지 링크

지원되는 환경에서는 `sms:`를 사용할 수 있다.

```html
<a href="sms:01012345678">
    문자 보내기
</a>
```

브라우저와 운영체제에 따라 동작이 달라질 수 있으므로 실제 대상 환경에서 확인해야 한다.

---

# 파일 링크

링크를 통해 PDF, 이미지, 압축 파일 등의 자원으로 이동할 수 있다.

```html
<a href="./files/course-guide.pdf">
    교육 과정 안내서 보기
</a>
```

브라우저에서 지원하는 파일은 새 페이지에서 표시될 수 있고, 지원하지 않는 형식은 다운로드될 수 있다.

---

# `download` 속성

`download` 속성은 연결된 자원을 다운로드하도록 브라우저에 요청한다.

```html
<a
    href="./files/course-guide.pdf"
    download
>
    교육 과정 안내서 다운로드
</a>
```

다운로드할 파일 이름을 지정할 수도 있다.

```html
<a
    href="./files/course-guide.pdf"
    download="developer-academy-guide.pdf"
>
    교육 과정 안내서 다운로드
</a>
```

## 사용 시 주의

`download` 속성의 실제 동작은 다음 요소의 영향을 받을 수 있다.

- 브라우저 정책
- 파일의 출처
- 서버 응답 헤더
- 교차 출처 제한
- 사용자의 브라우저 설정

특히 다른 도메인의 파일에서는 `download` 속성이 기대대로 동작하지 않을 수 있다.

---

# 이미지 링크

이미지를 `<a>` 내부에 넣으면 이미지 전체를 클릭 가능한 링크로 만들 수 있다.

```html
<a href="./index.html">
    <img
        src="./images/logo.png"
        alt="Developer Academy 홈"
    >
</a>
```

쇼핑몰 상품 카드에도 자주 사용한다.

```html
<a href="./products/keyboard.html">
    <img
        src="./images/keyboard.jpg"
        alt="Developer Keyboard"
    >

    <h2>Developer Keyboard</h2>
</a>
```

이미지가 링크의 목적을 전달하는 경우 `alt` 속성에 링크 목적이 드러나도록 작성해야 한다.

---

# 로고 링크

웹사이트의 로고는 홈으로 이동하는 링크로 구현하는 경우가 많다.

```html
<a
    href="./index.html"
    aria-label="Developer Academy 홈"
>
    <img
        src="./images/logo.svg"
        alt=""
    >
</a>
```

위 예제에서는 링크 자체에 `aria-label`로 이름을 제공했기 때문에 이미지의 `alt`를 비워 중복 낭독을 방지했다.

다음 방식도 가능하다.

```html
<a href="./index.html">
    <img
        src="./images/logo.svg"
        alt="Developer Academy 홈"
    >
</a>
```

두 방식 중 하나를 선택하여 링크 이름이 중복되지 않도록 구성한다.

---

# 링크 안에 다양한 콘텐츠 넣기

`<a>` 요소 안에는 링크 목적에 맞는 여러 콘텐츠를 포함할 수 있다.

```html
<a
    class="course-card"
    href="./courses/frontend.html"
>
    <article>
        <h2>프론트엔드 과정</h2>

        <p>
            HTML, CSS, JavaScript와 React를 학습합니다.
        </p>

        <span>과정 보기</span>
    </article>
</a>
```

카드 전체를 클릭 가능한 링크로 만들 수 있다.

다만 링크 내부에 또 다른 링크나 버튼처럼 별도의 상호작용 요소를 넣지 않도록 주의해야 한다.

---

# 링크 중첩 금지

`<a>` 안에 또 다른 `<a>`를 넣으면 안 된다.

## 잘못된 예

```html
<a href="./courses.html">
    교육 과정

    <a href="./apply.html">
        신청하기
    </a>
</a>
```

## 올바른 예

```html
<div class="course-card">
    <a href="./courses.html">
        교육 과정
    </a>

    <a href="./apply.html">
        신청하기
    </a>
</div>
```

각 링크를 형제 요소로 분리한다.

---

# 링크 내부의 버튼 사용 주의

링크 안에 `<button>`을 넣거나 버튼 안에 링크를 넣는 구조는 피해야 한다.

## 잘못된 예

```html
<a href="./apply.html">
    <button type="button">
        신청하기
    </button>
</a>
```

```html
<button type="button">
    <a href="./apply.html">
        신청하기
    </a>
</button>
```

링크 이동이 목적이라면 `<a>`만 사용한다.

```html
<a
    class="button-link"
    href="./apply.html"
>
    신청하기
</a>
```

동작 실행이 목적이라면 `<button>`을 사용한다.

```html
<button type="button">
    신청 내용 저장
</button>
```

---

# 링크와 버튼의 차이

링크와 버튼은 화면에서 비슷하게 디자인할 수 있지만 역할이 다르다.

| 구분 | `<a>` | `<button>` |
|---|---|---|
| 목적 | 다른 위치나 자원으로 이동 | 현재 화면에서 동작 실행 |
| 대표 기능 | 페이지 이동, 파일 열기 | 저장, 삭제, 메뉴 열기 |
| 핵심 속성 | `href` | `type` |
| 키보드 기본 동작 | Enter | Enter, Space |
| 브라우저 기능 | 새 탭 열기, 주소 복사 | 일반적으로 해당 기능 없음 |

---

## 링크를 사용해야 하는 경우

```html
<a href="./login.html">
    로그인 페이지로 이동
</a>
```

```html
<a href="./portfolio.pdf">
    포트폴리오 보기
</a>
```

```html
<a href="#contact">
    문의 영역으로 이동
</a>
```

다른 주소나 위치로 이동하므로 `<a>`를 사용한다.

---

## 버튼을 사용해야 하는 경우

```html
<button type="submit">
    로그인
</button>
```

```html
<button type="button">
    메뉴 열기
</button>
```

```html
<button type="button">
    장바구니에 추가
</button>
```

현재 화면에서 기능이나 상태 변경을 실행하므로 `<button>`을 사용한다.

---

# 버튼처럼 보이는 링크

페이지 이동 링크를 CSS로 버튼처럼 디자인할 수 있다.

```html
<a
    class="apply-link"
    href="./apply.html"
>
    수강 신청하기
</a>
```

```css
.apply-link {
    display: inline-block;
    padding: 12px 20px;
    border-radius: 8px;
    text-decoration: none;
}
```

모양은 버튼처럼 보여도 역할이 페이지 이동이라면 HTML 요소는 `<a>`가 적절하다.

---

# `href`가 없는 `<a>`

다음처럼 `href`가 없는 `<a>`는 일반적인 하이퍼링크 기능을 하지 않는다.

```html
<a>교육 과정</a>
```

페이지 이동이 목적이라면 실제 경로를 지정해야 한다.

```html
<a href="./courses.html">
    교육 과정
</a>
```

아직 주소가 정해지지 않았다면 임시 링크를 무분별하게 추가하기보다 개발 단계에서 명확하게 구분한다.

---

# 빈 `href`

```html
<a href="">
    홈
</a>
```

빈 `href`는 현재 문서를 다시 요청하거나 예상하지 못한 동작을 만들 수 있다.

실제 목적지 주소를 작성해야 한다.

```html
<a href="./index.html">
    홈
</a>
```

---

# `href="#"` 사용 시 주의

```html
<a href="#">
    메뉴 열기
</a>
```

`#`만 작성하면 페이지 상단으로 이동하거나 주소에 프래그먼트가 추가될 수 있다.

메뉴 열기처럼 동작 실행이 목적이라면 버튼을 사용한다.

```html
<button
    type="button"
    aria-expanded="false"
>
    메뉴 열기
</button>
```

페이지 내부 이동이 목적이라면 실제 대상 `id`를 지정한다.

```html
<a href="#contact">
    문의하기
</a>
```

---

# `javascript:void(0)` 사용 지양

과거에는 링크의 기본 이동을 막기 위해 다음과 같은 코드를 사용하기도 했다.

```html
<a href="javascript:void(0)">
    메뉴 열기
</a>
```

이 방식은 링크와 버튼의 역할을 혼동하게 만들 수 있다.

동작 실행이 목적이라면 `<button>`을 사용하는 것이 적절하다.

```html
<button type="button">
    메뉴 열기
</button>
```

---

# 현재 페이지 링크

현재 페이지와 같은 주소를 가리키는 링크에는 현재 위치임을 알릴 수 있다.

```html
<nav aria-label="주요 메뉴">
    <ul>
        <li>
            <a
                href="./index.html"
                aria-current="page"
            >
                홈
            </a>
        </li>

        <li>
            <a href="./courses.html">
                교육 과정
            </a>
        </li>
    </ul>
</nav>
```

`aria-current="page"`는 해당 링크가 현재 페이지를 나타낸다는 정보를 보조 기술에 전달한다.

CSS 선택자로 현재 메뉴를 디자인할 수도 있다.

```css
[aria-current="page"] {
    font-weight: 700;
}
```

---

# 링크 상태

브라우저는 링크 상태에 따라 CSS 가상 클래스를 제공한다.

```css
a:link {
    text-decoration: underline;
}

a:visited {
    text-decoration-style: dotted;
}

a:hover {
    text-decoration-thickness: 2px;
}

a:focus-visible {
    outline: 2px solid;
    outline-offset: 4px;
}

a:active {
    transform: translateY(1px);
}
```

대표적인 상태는 다음과 같다.

| 선택자 | 의미 |
|---|---|
| `:link` | 아직 방문하지 않은 링크 |
| `:visited` | 방문한 링크 |
| `:hover` | 마우스를 올린 상태 |
| `:focus` | 포커스를 받은 상태 |
| `:focus-visible` | 키보드 탐색 등에서 포커스 표시가 필요한 상태 |
| `:active` | 링크를 누르고 있는 상태 |

링크의 기본 밑줄이나 포커스 표시를 제거했다면 다른 방식으로 링크임을 분명하게 표현해야 한다.

---

# 링크와 접근성

## 링크 목적을 명확하게 작성하기

```html
<a href="./frontend.html">
    프론트엔드 과정 자세히 보기
</a>
```

사용자는 링크 텍스트만 읽어도 목적을 이해할 수 있어야 한다.

---

## 색상만으로 링크를 구분하지 않기

본문 안의 링크를 색상만으로 구분하면 색상을 인식하기 어려운 사용자가 링크를 알아보기 힘들 수 있다.

```css
.article a {
    text-decoration: underline;
}
```

밑줄, 글꼴 두께, 아이콘 등의 시각적 단서를 함께 제공할 수 있다.

---

## 포커스 표시 유지하기

키보드 사용자는 Tab 키로 링크를 이동한다.

```css
a:focus-visible {
    outline: 2px solid;
    outline-offset: 3px;
}
```

포커스 표시를 특별한 대체 방식 없이 제거하면 안 된다.

```css
a {
    outline: none;
}
```

---

## 새 탭 열림 알리기

```html
<a
    href="https://github.com"
    target="_blank"
    rel="noopener"
>
    GitHub
    <span aria-hidden="true">↗</span>
    <span class="visually-hidden">
        새 탭에서 열림
    </span>
</a>
```

시각적 아이콘과 보조 기술용 텍스트를 함께 제공할 수 있다.

---

## URL 자체보다 목적을 표시하기

다음보다

```html
<a href="https://example.com/courses/frontend">
    https://example.com/courses/frontend
</a>
```

다음 방식이 사용자가 이해하기 쉽다.

```html
<a href="https://example.com/courses/frontend">
    프론트엔드 과정 보기
</a>
```

단, 이메일 주소나 참고용 URL을 그대로 보여 주어야 하는 상황에서는 URL 자체를 링크 텍스트로 사용할 수 있다.

---

# 링크와 검색 엔진

검색 엔진은 링크를 통해 페이지 사이의 관계를 파악할 수 있다.

링크 텍스트는 연결된 페이지의 내용을 설명하는 역할도 한다.

## 좋은 예

```html
<a href="./html-course.html">
    HTML 기초 과정
</a>
```

## 좋지 않은 예

```html
<a href="./html-course.html">
    클릭
</a>
```

의미 있는 링크 텍스트와 논리적인 내부 링크 구조는 사용자 경험과 검색 엔진의 문서 이해에 도움이 된다.

---

# 내비게이션 링크

주요 메뉴는 `<nav>`와 목록 태그를 함께 사용하는 경우가 많다.

```html
<nav aria-label="주요 메뉴">
    <ul>
        <li>
            <a href="./index.html">홈</a>
        </li>

        <li>
            <a href="./courses.html">교육 과정</a>
        </li>

        <li>
            <a href="./portfolio.html">포트폴리오</a>
        </li>

        <li>
            <a href="./contact.html">문의하기</a>
        </li>
    </ul>
</nav>
```

`<nav>`는 주요 탐색 영역이라는 의미를 나타내고, `<ul>`은 관련 링크들의 목록이라는 구조를 나타낸다.

---

# 하위 메뉴

중첩 목록을 사용하여 하위 메뉴 구조를 만들 수 있다.

```html
<nav aria-label="주요 메뉴">
    <ul>
        <li>
            <a href="./courses.html">
                교육 과정
            </a>

            <ul>
                <li>
                    <a href="./courses/frontend.html">
                        프론트엔드
                    </a>
                </li>

                <li>
                    <a href="./courses/backend.html">
                        백엔드
                    </a>
                </li>
            </ul>
        </li>
    </ul>
</nav>
```

메뉴를 펼치고 닫는 동작이 필요하다면 별도의 `<button>`을 사용하는 구조도 고려할 수 있다.

```html
<li>
    <a href="./courses.html">
        교육 과정
    </a>

    <button
        type="button"
        aria-expanded="false"
        aria-controls="course-submenu"
    >
        하위 메뉴 열기
    </button>

    <ul id="course-submenu">
        <li>
            <a href="./courses/frontend.html">
                프론트엔드
            </a>
        </li>

        <li>
            <a href="./courses/backend.html">
                백엔드
            </a>
        </li>
    </ul>
</li>
```

페이지 이동 링크와 메뉴 열기 기능을 분리한 구조이다.

---

# 카드 링크

상품이나 게시글 카드 전체를 링크로 만들 수 있다.

```html
<article class="course-card">
    <a href="./courses/frontend.html">
        <img
            src="./images/frontend-course.jpg"
            alt=""
        >

        <h2>프론트엔드 개발 과정</h2>

        <p>
            HTML, CSS, JavaScript와 React를 학습합니다.
        </p>
    </a>
</article>
```

이미지가 장식 목적이고 제목이 링크 목적을 충분히 설명한다면 `alt=""`를 사용할 수 있다.

카드 내부에 찜하기, 삭제하기 같은 별도 버튼이 있다면 카드 전체를 하나의 링크로 감싸는 구조는 피하는 것이 좋다.

---

# 실무 활용

## 기업 홈페이지

```html
<a href="./about.html">
    회사 소개
</a>
```

## 쇼핑몰 상품 링크

```html
<a href="./products/keyboard.html">
    Developer Keyboard
</a>
```

## 게시판 제목

```html
<a href="./notice/15.html">
    서비스 점검 안내
</a>
```

## 외부 SNS

```html
<a
    href="https://github.com/example"
    target="_blank"
    rel="noopener"
>
    GitHub
</a>
```

## 고객센터 전화

```html
<a href="tel:15881234">
    1588-1234
</a>
```

## 이메일 문의

```html
<a href="mailto:contact@example.com">
    이메일 문의
</a>
```

## 문서 다운로드

```html
<a
    href="./files/course-guide.pdf"
    download
>
    교육 과정 안내서 다운로드
</a>
```

## 페이지 내부 목차

```html
<a href="#faq">
    자주 묻는 질문
</a>
```

---

# 실무 예제 프로젝트

다음은 Developer Academy 홈페이지의 링크 구조를 포함한 예제이다.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0"
    >

    <title>Developer Academy</title>
</head>
<body id="top">
    <header>
        <a href="./index.html">
            <img
                src="./images/logo.svg"
                alt="Developer Academy 홈"
            >
        </a>

        <nav aria-label="주요 메뉴">
            <ul>
                <li>
                    <a
                        href="./index.html"
                        aria-current="page"
                    >
                        홈
                    </a>
                </li>

                <li>
                    <a href="./courses.html">
                        교육 과정
                    </a>
                </li>

                <li>
                    <a href="./projects.html">
                        실무 프로젝트
                    </a>
                </li>

                <li>
                    <a href="./portfolio.html">
                        수강생 포트폴리오
                    </a>
                </li>

                <li>
                    <a href="./contact.html">
                        문의하기
                    </a>
                </li>
            </ul>
        </nav>

        <a
            class="apply-link"
            href="./apply.html"
        >
            수강 신청
        </a>
    </header>

    <main>
        <section aria-labelledby="hero-title">
            <h1 id="hero-title">
                실무 중심 웹 개발자 교육
            </h1>

            <p>
                HTML부터 React와 Spring Boot까지
                단계적으로 학습합니다.
            </p>

            <a href="./courses.html">
                전체 교육 과정 보기
            </a>

            <a href="#curriculum">
                학습 과정 바로 보기
            </a>
        </section>

        <section
            id="curriculum"
            aria-labelledby="curriculum-title"
        >
            <h2 id="curriculum-title">
                주요 교육 과정
            </h2>

            <ul>
                <li>
                    <article>
                        <a href="./courses/frontend.html">
                            <img
                                src="./images/frontend.jpg"
                                alt=""
                            >

                            <h3>프론트엔드 과정</h3>

                            <p>
                                HTML, CSS, JavaScript와
                                React를 학습합니다.
                            </p>
                        </a>
                    </article>
                </li>

                <li>
                    <article>
                        <a href="./courses/backend.html">
                            <img
                                src="./images/backend.jpg"
                                alt=""
                            >

                            <h3>백엔드 과정</h3>

                            <p>
                                Java와 Spring Boot를
                                학습합니다.
                            </p>
                        </a>
                    </article>
                </li>
            </ul>
        </section>

        <section
            id="resources"
            aria-labelledby="resources-title"
        >
            <h2 id="resources-title">
                학습 자료
            </h2>

            <p>
                자세한 교육 내용은 안내서를 통해
                확인할 수 있습니다.
            </p>

            <a
                href="./files/course-guide.pdf"
                download="developer-academy-guide.pdf"
            >
                교육 과정 안내서 다운로드
            </a>
        </section>

        <section
            id="contact"
            aria-labelledby="contact-title"
        >
            <h2 id="contact-title">
                상담 문의
            </h2>

            <p>
                전화:
                <a href="tel:0212345678">
                    02-1234-5678
                </a>
            </p>

            <p>
                이메일:
                <a href="mailto:contact@example.com">
                    contact@example.com
                </a>
            </p>
        </section>
    </main>

    <footer>
        <nav aria-label="관련 링크">
            <ul>
                <li>
                    <a
                        href="https://github.com/example"
                        target="_blank"
                        rel="noopener"
                    >
                        GitHub
                        <span class="visually-hidden">
                            새 탭에서 열림
                        </span>
                    </a>
                </li>

                <li>
                    <a
                        href="https://blog.example.com"
                        target="_blank"
                        rel="noopener"
                    >
                        기술 블로그
                        <span class="visually-hidden">
                            새 탭에서 열림
                        </span>
                    </a>
                </li>

                <li>
                    <a href="./privacy.html">
                        개인정보 처리방침
                    </a>
                </li>
            </ul>
        </nav>

        <a href="#top">
            페이지 상단으로 이동
        </a>
    </footer>
</body>
</html>
```

---

# 예제 구조 분석

```text
body#top
├── header
│   ├── a
│   │   └── img
│   ├── nav
│   │   └── ul
│   │       └── li
│   │           └── a
│   └── a
├── main
│   ├── section
│   │   ├── h1
│   │   ├── p
│   │   ├── a
│   │   └── a
│   ├── section#curriculum
│   │   ├── h2
│   │   └── ul
│   │       └── li
│   │           └── article
│   │               └── a
│   │                   ├── img
│   │                   ├── h3
│   │                   └── p
│   ├── section#resources
│   │   ├── h2
│   │   ├── p
│   │   └── a[download]
│   └── section#contact
│       ├── h2
│       └── p
│           └── a
└── footer
    ├── nav
    │   └── ul
    │       └── li
    │           └── a
    └── a[href="#top"]
```

---

# 예제에서 확인할 내용

- 로고를 홈으로 이동하는 링크로 만들었다.
- 주요 메뉴를 `<nav>`, `<ul>`, `<li>`, `<a>`로 구성했다.
- 현재 페이지 링크에 `aria-current="page"`를 사용했다.
- 수강 신청은 페이지 이동이므로 버튼이 아니라 `<a>`를 사용했다.
- 같은 페이지의 교육 과정으로 이동하기 위해 `#curriculum`을 사용했다.
- 과정 카드를 링크로 구성했다.
- 안내서에 `download` 속성을 사용했다.
- 이메일과 전화 링크를 각각 `mailto:`, `tel:`로 작성했다.
- 외부 링크에 `target="_blank"`와 `rel="noopener"`를 사용했다.
- 새 탭으로 열리는 링크에 안내 문구를 제공했다.
- 페이지 상단 이동을 위해 `#top`을 사용했다.

---

# 이번 문서에서 새롭게 배운 내용

| 개념 또는 속성 | 설명 |
|---|---|
| 하이퍼링크 | 다른 문서나 자원으로 연결하는 기능 |
| `<a>` | 링크를 만드는 Anchor 요소 |
| `href` | 링크의 목적지 주소 |
| 내부 링크 | 같은 사이트 내부 페이지로 이동하는 링크 |
| 외부 링크 | 다른 도메인의 웹사이트로 이동하는 링크 |
| 절대 경로 | 전체 주소를 작성하는 경로 |
| 상대 경로 | 현재 파일 위치를 기준으로 작성하는 경로 |
| `./` | 현재 폴더 |
| `../` | 상위 폴더 |
| `/` | 사이트 루트 |
| 프래그먼트 | `#id`를 이용한 문서 내부 위치 |
| `target` | 링크가 열릴 위치 지정 |
| `_blank` | 새 탭 또는 새 창으로 열기 |
| `rel` | 현재 문서와 연결 문서의 관계 |
| `noopener` | 새 페이지의 원본 창 접근 제한 |
| `noreferrer` | 참조 정보 전달 제한 |
| `nofollow` | 검색 엔진에 링크 추적 제한 요청 |
| `mailto:` | 이메일 프로그램 열기 |
| `tel:` | 전화 연결 |
| `sms:` | 문자 메시지 기능 연결 |
| `download` | 연결 자원 다운로드 요청 |
| `aria-current` | 현재 페이지 또는 현재 항목 표시 |
| 링크 상태 | 방문, 호버, 포커스, 활성 상태 |
| 링크 목적 | 사용자가 이동 결과를 이해할 수 있는 이름 |
| 링크와 버튼 | 이동과 동작 실행의 역할 구분 |

---

# 자주 하는 실수

## 1. 외부 링크에 프로토콜을 작성하지 않는다

### 잘못된 예

```html
<a href="google.com">
    Google
</a>
```

현재 사이트 내부의 `google.com` 경로로 해석될 수 있다.

### 올바른 예

```html
<a href="https://google.com">
    Google
</a>
```

---

## 2. `./`와 `../`를 혼동한다

```html
<a href="./index.html">
```

현재 폴더의 `index.html`을 의미한다.

```html
<a href="../index.html">
```

상위 폴더의 `index.html`을 의미한다.

현재 파일과 목적지 파일의 실제 폴더 구조를 기준으로 작성해야 한다.

---

## 3. Windows 파일 경로를 작성한다

### 잘못된 예

```html
<a href="C:\workspace\project\about.html">
    회사 소개
</a>
```

웹 경로에는 운영체제의 로컬 파일 경로를 사용하지 않는다.

### 권장 예

```html
<a href="./about.html">
    회사 소개
</a>
```

---

## 4. 경로에 역슬래시를 사용한다

### 잘못된 예

```html
<a href="courses\frontend.html">
    프론트엔드
</a>
```

### 올바른 예

```html
<a href="./courses/frontend.html">
    프론트엔드
</a>
```

웹 경로에서는 `/`를 사용한다.

---

## 5. `href`를 생략한다

```html
<a>교육 과정</a>
```

이동 목적의 링크라면 실제 주소를 작성한다.

```html
<a href="./courses.html">
    교육 과정
</a>
```

---

## 6. 빈 `href`를 사용한다

```html
<a href="">
    홈
</a>
```

현재 페이지를 다시 요청하거나 예상하지 못한 동작이 발생할 수 있다.

```html
<a href="./index.html">
    홈
</a>
```

---

## 7. 버튼 기능에 `href="#"`를 사용한다

### 좋지 않은 예

```html
<a href="#">
    메뉴 열기
</a>
```

### 권장 방식

```html
<button type="button">
    메뉴 열기
</button>
```

현재 화면의 기능 실행은 버튼을 사용한다.

---

## 8. `javascript:void(0)`을 사용한다

```html
<a href="javascript:void(0)">
    팝업 열기
</a>
```

동작 실행이라면 버튼이 적절하다.

```html
<button type="button">
    팝업 열기
</button>
```

---

## 9. `target="_blank"`를 무조건 사용한다

모든 링크를 새 탭에서 열면 사용자가 탭을 관리하기 어려워질 수 있다.

사용자의 흐름을 유지할 필요가 있는 외부 자료 등에서 선택적으로 사용한다.

---

## 10. 새 탭 링크임을 알리지 않는다

```html
<a
    href="https://example.com"
    target="_blank"
    rel="noopener"
>
    외부 자료
</a>
```

필요한 경우 시각적 아이콘이나 보조 기술용 문구로 새 탭 열림을 안내한다.

---

## 11. 링크 텍스트를 모두 `클릭` 또는 `자세히`로 작성한다

### 좋지 않은 예

```html
<a href="./frontend.html">
    자세히 보기
</a>

<a href="./backend.html">
    자세히 보기
</a>
```

### 권장 방식

```html
<a href="./frontend.html">
    프론트엔드 과정 자세히 보기
</a>

<a href="./backend.html">
    백엔드 과정 자세히 보기
</a>
```

링크 텍스트만으로 목적을 구분할 수 있어야 한다.

---

## 12. `<a>` 안에 다른 `<a>`를 넣는다

```html
<a href="./courses.html">
    교육 과정

    <a href="./apply.html">
        신청
    </a>
</a>
```

링크를 서로 분리한다.

```html
<a href="./courses.html">
    교육 과정
</a>

<a href="./apply.html">
    신청
</a>
```

---

## 13. 링크 안에 버튼을 넣는다

```html
<a href="./apply.html">
    <button type="button">
        신청하기
    </button>
</a>
```

페이지 이동이면 링크만 사용한다.

```html
<a
    class="button-link"
    href="./apply.html"
>
    신청하기
</a>
```

---

## 14. 페이지 이동에 버튼을 사용한다

```html
<button type="button">
    회사 소개
</button>
```

회사 소개 페이지로 이동하는 목적이라면 링크가 적절하다.

```html
<a href="./about.html">
    회사 소개
</a>
```

---

## 15. 같은 `id`를 여러 번 사용한다

```html
<section id="course"></section>
<section id="course"></section>
```

각 `id`는 문서 안에서 고유해야 한다.

```html
<section id="frontend-course"></section>
<section id="backend-course"></section>
```

---

## 16. 존재하지 않는 `id`로 이동한다

```html
<a href="#contact">
    문의하기
</a>
```

문서 안에 `id="contact"`가 없다면 원하는 위치로 이동할 수 없다.

```html
<section id="contact">
    <h2>문의하기</h2>
</section>
```

---

## 17. 링크의 기본 밑줄과 포커스를 모두 제거한다

```css
a {
    text-decoration: none;
    outline: none;
}
```

링크 여부와 키보드 포커스를 확인하기 어려워질 수 있다.

밑줄을 제거했다면 다른 시각적 단서를 제공하고 포커스 스타일을 유지한다.

```css
a:focus-visible {
    outline: 2px solid;
    outline-offset: 3px;
}
```

---

## 18. 카드 안의 모든 기능을 하나의 링크로 감싼다

카드 내부에 찜하기, 삭제하기, 옵션 선택 같은 버튼이 있다면 카드 전체를 하나의 링크로 감싸지 않는 것이 좋다.

각 상호작용 요소의 역할을 분리해야 한다.

---

## 19. 파일 다운로드가 반드시 동작한다고 가정한다

`download` 속성은 브라우저 정책, 서버 설정, 교차 출처 여부에 따라 다르게 동작할 수 있다.

실제 배포 환경에서 테스트해야 한다.

---

## 20. `noreferrer`를 목적 없이 사용한다

`noreferrer`는 참조 정보를 전달하지 않기 때문에 분석 도구에서 유입 경로를 확인하기 어려워질 수 있다.

보안 및 분석 요구사항을 고려하여 사용한다.

---

# 면접 포인트

## Q1. `<a>` 태그는 어떤 역할을 하나요?

`<a>` 태그는 다른 문서, 웹사이트, 파일 또는 현재 문서의 특정 위치로 이동할 수 있는 하이퍼링크를 만든다.

일반적으로 `href` 속성에 이동할 목적지를 지정한다.

---

## Q2. `href` 속성은 무엇인가요?

링크가 이동할 주소 또는 자원의 위치를 지정하는 속성이다.

내부 페이지, 외부 URL, 문서 내부 `id`, 이메일 주소, 전화번호 등을 값으로 사용할 수 있다.

---

## Q3. 절대 경로와 상대 경로의 차이는 무엇인가요?

절대 경로는 프로토콜과 도메인을 포함한 전체 주소를 작성한다.

```html
<a href="https://example.com/about.html">
```

상대 경로는 현재 파일이나 사이트의 위치를 기준으로 목적지를 작성한다.

```html
<a href="./about.html">
```

외부 사이트는 절대 경로, 같은 프로젝트 내부 파일은 상대 경로를 주로 사용한다.

---

## Q4. `./`와 `../`의 차이는 무엇인가요?

`./`는 현재 폴더를 의미하고 `../`는 한 단계 상위 폴더를 의미한다.

```html
<a href="./about.html">
```

현재 폴더의 `about.html`로 이동한다.

```html
<a href="../index.html">
```

상위 폴더의 `index.html`로 이동한다.

---

## Q5. 페이지 내부의 특정 위치로 이동하려면 어떻게 하나요?

링크의 `href`에 `#id`를 작성하고 대상 요소에 동일한 `id`를 지정한다.

```html
<a href="#contact">
    문의하기
</a>

<section id="contact">
    <h2>문의하기</h2>
</section>
```

---

## Q6. `target="_blank"`는 무엇인가요?

링크를 새 탐색 컨텍스트에서 열도록 지정한다.

일반적으로 새 탭 또는 새 창으로 열린다.

외부 자료를 현재 페이지와 별도로 열어야 할 때 선택적으로 사용할 수 있다.

---

## Q7. `noopener`는 왜 사용하나요?

새 탭으로 열린 문서가 원래 문서의 `window.opener`를 통해 원본 창에 접근하지 못하도록 제한하기 위해 사용한다.

```html
<a
    href="https://example.com"
    target="_blank"
    rel="noopener"
>
    외부 사이트
</a>
```

---

## Q8. `noreferrer`는 무엇인가요?

이동할 페이지에 현재 페이지의 참조 정보를 전달하지 않도록 요청한다.

유입 경로 분석에 영향을 줄 수 있으므로 프로젝트의 보안 및 분석 요구사항에 맞게 사용해야 한다.

---

## Q9. 링크와 버튼의 차이는 무엇인가요?

링크는 다른 페이지, 파일 또는 문서 위치로 이동할 때 사용한다.

버튼은 폼 제출, 메뉴 열기, 모달 실행처럼 현재 화면에서 기능이나 상태 변경을 실행할 때 사용한다.

화면 모양이 아니라 동작의 목적을 기준으로 선택해야 한다.

---

## Q10. 링크를 버튼처럼 디자인해도 되나요?

가능하다.

페이지 이동이 목적이라면 `<a>`를 사용하고 CSS로 버튼처럼 디자인할 수 있다.

```html
<a
    class="button-link"
    href="./apply.html"
>
    신청하기
</a>
```

---

## Q11. `mailto:`와 `tel:`은 무엇인가요?

`mailto:`는 사용자의 이메일 프로그램을 열기 위한 링크이고, `tel:`은 전화 기능을 지원하는 기기에서 전화 연결을 시도하는 링크이다.

```html
<a href="mailto:contact@example.com">
    이메일 문의
</a>

<a href="tel:0212345678">
    전화 문의
</a>
```

---

## Q12. `download` 속성은 무엇인가요?

연결된 자원을 브라우저에서 열기보다 다운로드하도록 요청하는 속성이다.

```html
<a
    href="./files/guide.pdf"
    download
>
    안내서 다운로드
</a>
```

브라우저와 서버 정책에 따라 실제 동작이 달라질 수 있다.

---

## Q13. `href="#"`를 버튼 대신 사용하면 안 되는 이유는 무엇인가요?

`#` 링크는 페이지 상단으로 이동하거나 URL에 프래그먼트를 추가할 수 있다.

메뉴 열기나 모달 실행처럼 이동이 아닌 동작에는 의미상 `<button>`이 적절하다.

---

## Q14. 링크 텍스트가 중요한 이유는 무엇인가요?

사용자는 링크 텍스트를 통해 이동할 목적지를 예측한다.

화면 낭독기 사용자는 링크 목록만 별도로 탐색할 수도 있으므로 `클릭`, `여기`보다 목적이 명확한 링크 텍스트를 작성해야 한다.

---

## Q15. `aria-current="page"`는 언제 사용하나요?

내비게이션에서 해당 링크가 현재 페이지를 나타낼 때 사용한다.

```html
<a
    href="./index.html"
    aria-current="page"
>
    홈
</a>
```

보조 기술에 현재 위치를 전달하고 CSS로 현재 메뉴를 표현할 수도 있다.

---

# 핵심 정리

- `<a>`는 다른 문서, 자원 또는 위치로 이동하는 링크를 만든다.
- `href`에는 링크의 목적지 주소를 작성한다.
- 같은 사이트 내부 페이지는 상대 경로나 루트 경로를 사용할 수 있다.
- 외부 사이트에는 일반적으로 `https://`를 포함한 전체 주소를 작성한다.
- `./`는 현재 폴더, `../`는 상위 폴더를 의미한다.
- `/`로 시작하는 경로는 일반적으로 사이트 루트를 기준으로 한다.
- `#id`를 사용하면 같은 문서의 특정 위치로 이동할 수 있다.
- 다른 페이지의 특정 위치는 `파일경로#id`로 연결할 수 있다.
- `target="_blank"`는 링크를 새 탭 또는 새 창으로 연다.
- 새 탭 링크에는 필요에 따라 `rel="noopener"`를 사용한다.
- `noreferrer`는 참조 정보 전달을 제한하므로 분석 요구사항을 고려해야 한다.
- `mailto:`는 이메일, `tel:`은 전화 연결에 사용한다.
- `download` 속성은 연결된 파일의 다운로드를 요청한다.
- 이미지와 카드도 링크 콘텐츠로 사용할 수 있다.
- 링크 안에 또 다른 링크나 버튼을 넣지 않는다.
- 페이지 이동에는 `<a>`, 현재 화면의 기능 실행에는 `<button>`을 사용한다.
- 버튼처럼 보이는 이동 요소도 의미상 `<a>`를 사용해야 한다.
- 링크 텍스트만으로 이동 목적을 이해할 수 있도록 작성한다.
- 링크는 색상뿐 아니라 밑줄이나 다른 시각적 단서로 구분하는 것이 좋다.
- 키보드 사용자를 위해 포커스 표시를 유지한다.
- 현재 페이지 링크에는 `aria-current="page"`를 사용할 수 있다.

---

# 변경 이력

| Version | 날짜 | 변경 내용 |
|---|---|---|
| v1.0 | 2026-07-21 | HTML 링크 태그 문서 최초 작성 |
| v1.0 | 2026-07-21 | `a`와 `href` 기본 문법 정리 |
| v1.0 | 2026-07-21 | 내부 링크와 외부 링크 설명 추가 |
| v1.0 | 2026-07-21 | 절대 경로와 상대 경로 설명 추가 |
| v1.0 | 2026-07-21 | `./`, `../`, `/` 경로 작성법 추가 |
| v1.0 | 2026-07-21 | 페이지 내부 이동과 프래그먼트 설명 추가 |
| v1.0 | 2026-07-21 | `target`, `rel`, `noopener`, `noreferrer` 설명 추가 |
| v1.0 | 2026-07-21 | `mailto`, `tel`, `sms`, `download` 링크 추가 |
| v1.0 | 2026-07-21 | 링크와 버튼의 의미 차이 추가 |
| v1.0 | 2026-07-21 | 링크 접근성과 검색 엔진 관련 내용 추가 |
| v1.0 | 2026-07-21 | 내비게이션, 카드, 로고 링크 실무 활용 추가 |
| v1.0 | 2026-07-21 | 실무 예제 프로젝트와 구조 분석 추가 |
| v1.0 | 2026-07-21 | 자주 하는 실수와 면접 포인트 추가 |
