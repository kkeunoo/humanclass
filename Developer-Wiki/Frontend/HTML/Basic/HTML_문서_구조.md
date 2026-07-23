---
title: HTML 문서 구조
version: v1.1
last_updated: 2026-07-21
status: Completed
---

# HTML 문서 구조

## 개요

HTML 문서는 일정한 기본 구조를 가진다.

브라우저는 HTML 파일을 위에서 아래로 해석하며, 문서에 작성된 태그를 바탕으로 페이지의 구조와 내용을 화면에 표시한다.

기본적인 HTML 문서는 다음 요소로 구성된다.

- `<!DOCTYPE html>`
- `<html>`
- `<head>`
- `<body>`

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>문서 제목</title>
</head>
<body>
    <h1>웹 페이지 제목</h1>
    <p>웹 페이지에 표시되는 내용입니다.</p>
</body>
</html>
```

이 구조는 대부분의 HTML 문서에서 사용하는 기본 골격이다.

---

# 핵심 개념

## HTML 문서의 구성

HTML 문서는 크게 다음 두 영역으로 구분할 수 있다.

| 영역 | 역할 |
|---|---|
| `<head>` | 문서의 설정과 부가 정보를 작성 |
| `<body>` | 브라우저 화면에 표시할 콘텐츠를 작성 |

```html
<html>
<head>
    <!-- 문서 설정 -->
</head>
<body>
    <!-- 화면에 표시할 콘텐츠 -->
</body>
</html>
```

`<head>`와 `<body>`는 서로 역할이 다르기 때문에 목적에 맞게 내용을 구분하여 작성해야 한다.

---

# 기본 문서 구조

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Developer Wiki</title>
</head>
<body>
    <h1>HTML 학습</h1>
    <p>HTML 문서 구조를 학습합니다.</p>
</body>
</html>
```

각 요소의 역할을 하나씩 살펴보면 다음과 같다.

---

# `<!DOCTYPE html>`

## 문서 유형 선언

```html
<!DOCTYPE html>
```

`<!DOCTYPE html>`은 현재 문서가 **HTML5 문서임을 브라우저에 알리는 선언문**이다.

HTML 태그처럼 보이지만 일반적인 HTML 요소는 아니다.

- 시작 태그와 종료 태그로 구성되지 않는다.
- 문서의 가장 첫 번째 줄에 작성한다.
- 브라우저가 표준 모드로 문서를 해석하도록 돕는다.

```html
<!DOCTYPE html>
<html lang="ko">
    ...
</html>
```

## DOCTYPE을 생략하면 안 되는 이유

DOCTYPE을 생략하면 일부 브라우저가 문서를 **호환 모드 또는 비표준 모드**로 해석할 수 있다.

이 경우 브라우저마다 CSS 레이아웃이나 요소의 크기가 다르게 표시될 가능성이 있다.

따라서 HTML 문서를 작성할 때는 항상 첫 줄에 다음 선언을 작성한다.

```html
<!DOCTYPE html>
```

> `DOCTYPE`은 대소문자를 구분하지 않지만, 일반적으로 `<!DOCTYPE html>` 형태로 작성한다.

---

# `<html>` 요소

## HTML 문서의 최상위 요소

```html
<html lang="ko">
    ...
</html>
```

`<html>` 요소는 HTML 문서 전체를 감싸는 **최상위 요소**, 즉 루트 요소이다.

DOCTYPE을 제외한 모든 HTML 요소는 `<html>` 내부에 작성한다.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    ...
</head>
<body>
    ...
</body>
</html>
```

`<html>` 내부에는 일반적으로 `<head>`와 `<body>`가 위치한다.

---

## `lang` 속성

```html
<html lang="ko">
```

`lang` 속성은 문서의 기본 언어를 나타낸다.

| 속성값 | 언어 |
|---|---|
| `ko` | 한국어 |
| `en` | 영어 |
| `ja` | 일본어 |
| `zh` | 중국어 |

한국어로 작성된 문서는 다음과 같이 설정한다.

```html
<html lang="ko">
```

`lang` 속성은 다음과 같은 환경에서 활용된다.

- 스크린 리더의 발음 결정
- 검색 엔진의 문서 언어 파악
- 브라우저의 번역 기능
- 맞춤법 검사 및 언어 처리

화면에 직접 표시되지 않더라도 접근성과 검색 엔진 최적화를 위해 적절한 언어를 지정하는 것이 좋다.

---

# `<head>` 요소

## 문서의 설정과 부가 정보

```html
<head>
    <meta charset="UTF-8">
    <title>문서 제목</title>
</head>
```

`<head>`는 HTML 문서에 관한 **설정과 메타데이터**를 작성하는 영역이다.

일반적으로 `<head>` 내부의 내용은 웹 페이지 본문에 직접 표시되지 않는다.

대표적으로 다음 요소들이 사용된다.

| 요소 | 역할 |
|---|---|
| `<meta>` | 문자 인코딩, 화면 설정, 문서 설명 등의 정보 |
| `<title>` | 브라우저 탭에 표시되는 문서 제목 |
| `<link>` | 외부 CSS, 아이콘 등의 외부 리소스 연결 |
| `<style>` | 문서 내부에 CSS 작성 |
| `<script>` | JavaScript 파일 연결 또는 코드 작성 |

```html
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Developer Wiki</title>

    <link rel="stylesheet" href="./css/style.css">
    <script src="./js/main.js" defer></script>
</head>
```

`<link>`, `<style>`, `<script>`는 이후 CSS와 JavaScript 문서에서 자세히 학습한다.

---

# `<meta charset="UTF-8">`

## 문자 인코딩 설정

```html
<meta charset="UTF-8">
```

`charset`은 HTML 문서에서 사용하는 문자 인코딩 방식을 지정한다.

`UTF-8`은 한글, 영어, 숫자, 특수문자 등 다양한 문자를 표현할 수 있는 국제 표준 문자 인코딩 방식이다.

문자 인코딩을 올바르게 설정하지 않으면 한글이 다음과 같이 깨져 보일 수 있다.

```text
�븳湲� 臾몄옄
```

따라서 일반적인 HTML 문서에서는 다음 코드를 `<head>` 상단에 작성한다.

```html
<meta charset="UTF-8">
```

---

# Viewport 설정

## 모바일 화면 크기 대응

```html
<meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
>
```

Viewport는 브라우저가 웹 페이지를 화면에 표시하는 영역을 의미한다.

모바일 기기는 데스크톱보다 화면이 작기 때문에 Viewport 설정이 없으면 웹 페이지가 축소되어 표시될 수 있다.

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

각 값의 의미는 다음과 같다.

| 설정 | 의미 |
|---|---|
| `width=device-width` | 페이지 너비를 기기의 화면 너비에 맞춤 |
| `initial-scale=1.0` | 페이지의 초기 확대 비율을 1배로 설정 |

반응형 웹 페이지를 제작할 때 기본적으로 사용하는 설정이다.

> Viewport 설정만 추가한다고 반응형 웹이 완성되는 것은 아니다. 실제 반응형 레이아웃은 CSS의 미디어 쿼리 등을 사용하여 구현한다.

---

# `<title>` 요소

## 문서 제목 설정

```html
<title>Developer Wiki</title>
```

`<title>` 요소는 HTML 문서의 제목을 설정한다.

작성한 제목은 일반적으로 다음 위치에서 사용된다.

- 브라우저 탭
- 브라우저 방문 기록
- 즐겨찾기 또는 북마크
- 검색 결과의 문서 제목 후보
- 페이지를 공유할 때 표시되는 정보의 일부

```html
<head>
    <title>HTML 문서 구조 | Developer Wiki</title>
</head>
```

`<title>`은 `<head>` 내부에 작성하며, `<body>`의 제목 태그인 `<h1>`과 역할이 다르다.

| 요소 | 역할 |
|---|---|
| `<title>` | 브라우저와 문서 자체의 제목 |
| `<h1>` | 웹 페이지 본문에 표시되는 최상위 제목 |

```html
<head>
    <title>HTML 기초 강의</title>
</head>

<body>
    <h1>HTML 문서 구조</h1>
</body>
```

두 내용이 완전히 같을 필요는 없지만, 사용자가 문서의 목적을 이해할 수 있도록 서로 관련성 있게 작성하는 것이 좋다.

---

# `<body>` 요소

## 화면에 표시되는 콘텐츠

```html
<body>
    <h1>HTML 문서 구조</h1>
    <p>브라우저 화면에 표시되는 내용입니다.</p>
</body>
```

`<body>`는 사용자에게 보여 줄 웹 페이지의 콘텐츠를 작성하는 영역이다.

대표적으로 다음과 같은 내용이 포함된다.

- 제목
- 문단
- 이미지
- 링크
- 목록
- 표
- 입력 양식
- 버튼
- 주요 레이아웃 영역

```html
<body>
    <header>
        <h1>Developer Wiki</h1>
    </header>

    <main>
        <p>웹 개발 학습 내용을 정리합니다.</p>
    </main>
</body>
```

대부분의 시각적인 콘텐츠는 `<body>` 내부에 작성한다.

---

# `<head>`와 `<body>`의 차이

```html
<head>
    <title>HTML 문서 구조</title>
</head>

<body>
    <h1>HTML 문서 구조</h1>
</body>
```

| 구분 | `<head>` | `<body>` |
|---|---|---|
| 목적 | 문서의 설정과 부가 정보 | 사용자에게 보여 줄 콘텐츠 |
| 화면 표시 | 대부분 직접 표시되지 않음 | 브라우저 화면에 표시됨 |
| 주요 요소 | `meta`, `title`, `link`, `style`, `script` | `h1`, `p`, `a`, `img`, `section` 등 |
| 대상 | 브라우저, 검색 엔진, 외부 리소스 | 웹 페이지 사용자 |

단, `<title>`처럼 `<head>` 내부에 있으면서 브라우저 탭에 표시되는 요소도 있다.

따라서 `<head>`의 내용이 전혀 표시되지 않는다고 단정하기보다, **페이지 본문에 직접 렌더링되지 않는다**고 이해하는 것이 정확하다.

---

# 요소의 중첩 구조

HTML 요소는 다른 요소 내부에 포함될 수 있다. 이를 **중첩(Nesting)**이라고 한다.

```html
<body>
    <main>
        <section>
            <h1>HTML</h1>
            <p>HTML 문서 구조를 학습합니다.</p>
        </section>
    </main>
</body>
```

위 구조의 포함 관계는 다음과 같다.

```text
body
└── main
    └── section
        ├── h1
        └── p
```

HTML 문서는 이러한 부모·자식 관계를 가지는 트리 구조로 구성된다.

| 관계 | 설명 |
|---|---|
| 부모 요소 | 다른 요소를 내부에 포함하는 요소 |
| 자식 요소 | 다른 요소의 바로 내부에 포함된 요소 |
| 조상 요소 | 상위 단계에 위치한 모든 요소 |
| 후손 요소 | 하위 단계에 위치한 모든 요소 |
| 형제 요소 | 같은 부모 요소를 가지는 요소 |

위 예제에서는 다음 관계가 성립한다.

- `body`는 `main`의 부모 요소이다.
- `main`은 `section`의 부모 요소이다.
- `h1`과 `p`는 서로 형제 요소이다.
- `section`은 `h1`과 `p`의 부모 요소이다.
- `body`는 `h1`과 `p`의 조상 요소이다.

이러한 구조는 이후 CSS 선택자와 JavaScript DOM을 학습할 때 매우 중요하다.

---

# 올바른 중첩

HTML 요소는 먼저 연 태그를 나중에 닫는 방식으로 작성해야 한다.

## 잘못된 구조

```html
<p>
    HTML은 <strong>웹 문서의 구조를 만듭니다.
</p>
</strong>
```

`<strong>`을 `<p>` 내부에서 열었지만, `<p>`를 먼저 닫았기 때문에 구조가 서로 교차한다.

## 올바른 구조

```html
<p>
    HTML은 <strong>웹 문서의 구조를 만듭니다.</strong>
</p>
```

태그를 여는 순서와 닫는 순서는 다음과 같다.

```text
<p> 열기
    <strong> 열기
    </strong> 닫기
</p> 닫기
```

> 나중에 연 요소를 먼저 닫는다고 기억하면 쉽다.

---

# 들여쓰기

브라우저는 대부분의 공백과 들여쓰기를 화면에 그대로 표시하지 않는다.

다음 두 코드는 브라우저에서 비슷하게 동작할 수 있다.

```html
<body><main><h1>HTML</h1><p>문서 구조</p></main></body>
```

```html
<body>
    <main>
        <h1>HTML</h1>
        <p>문서 구조</p>
    </main>
</body>
```

그러나 두 번째 코드가 구조를 확인하고 수정하기 훨씬 쉽다.

들여쓰기는 브라우저를 위한 문법이라기보다 **개발자의 가독성과 유지보수성을 위한 작성 습관**이다.

## 권장 방식

```html
<body>
    <main>
        <section>
            <h1>HTML</h1>
            <p>HTML 문서 구조를 학습합니다.</p>
        </section>
    </main>
</body>
```

프로젝트에서 탭 또는 공백을 사용할 수 있지만, 하나의 프로젝트 안에서는 동일한 규칙을 유지하는 것이 중요하다.

---

# HTML 주석

HTML 코드에 설명을 남기거나 특정 코드를 임시로 비활성화할 때 주석을 사용할 수 있다.

```html
<!-- HTML 주석입니다. -->
```

## 설명을 위한 주석

```html
<body>
    <!-- 사이트 상단 영역 -->
    <header>
        <h1>Developer Wiki</h1>
    </header>
</body>
```

## 코드를 임시로 숨기는 주석

```html
<!--
<section>
    <h2>공지사항</h2>
</section>
-->
```

주석은 브라우저 화면에는 표시되지 않지만, 개발자 도구나 HTML 원본에서 확인할 수 있다.

따라서 다음과 같은 민감한 정보는 주석에 작성하면 안 된다.

- 비밀번호
- API 키
- 개인정보
- 서버 접속 정보
- 보안 관련 내부 정보

주석은 코드를 설명하는 데 도움이 되지만, 코드만으로 목적을 이해할 수 있다면 불필요하게 남발하지 않는 것이 좋다.

---

# 기본 문서 작성 순서

새로운 HTML 파일을 만들 때 다음 순서로 작성하면 된다.

## 1. HTML 파일 생성

```text
index.html
```

웹 사이트의 시작 페이지는 일반적으로 `index.html`이라는 이름을 사용한다.

## 2. DOCTYPE 선언

```html
<!DOCTYPE html>
```

## 3. `<html>` 요소 작성

```html
<html lang="ko">
</html>
```

## 4. `<head>`와 `<body>` 작성

```html
<!DOCTYPE html>
<html lang="ko">
<head>
</head>
<body>
</body>
</html>
```

## 5. 기본 메타데이터 작성

```html
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>문서 제목</title>
</head>
```

## 6. 본문 콘텐츠 작성

```html
<body>
    <h1>Developer Wiki</h1>
    <p>HTML 학습 내용을 정리합니다.</p>
</body>
```

---

# VS Code에서 기본 구조 만들기

VS Code에서 Emmet 기능을 사용할 수 있다면 HTML 파일에서 다음 기호를 입력한다.

```text
!
```

그다음 Enter 또는 Tab을 누르면 기본 HTML 구조가 자동으로 생성된다.

생성되는 형태는 환경이나 설정에 따라 조금 다를 수 있다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

</body>
</html>
```

한국어 문서를 작성한다면 다음 부분을 수정한다.

```html
<html lang="ko">
```

그리고 문서 목적에 맞게 `<title>`을 변경한다.

```html
<title>Developer Wiki</title>
```

---

# 실무 활용

실무에서는 HTML 문서의 기본 구조에 CSS와 JavaScript 파일을 연결하여 사용한다.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Developer Wiki</title>

    <link rel="stylesheet" href="./css/style.css">
    <script src="./js/main.js" defer></script>
</head>
<body>
    <h1>Developer Wiki</h1>
</body>
</html>
```

각 파일의 역할은 다음과 같다.

```text
project/
├── index.html
├── css/
│   └── style.css
└── js/
    └── main.js
```

| 파일 | 역할 |
|---|---|
| `index.html` | 웹 페이지의 구조 |
| `style.css` | 디자인과 레이아웃 |
| `main.js` | 동작과 상호작용 |

HTML은 다른 웹 기술이 적용될 수 있는 기본 구조를 제공한다.

---

# 실무 예제 프로젝트

다음은 Developer Wiki 소개 페이지의 기본 구조 예제이다.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <meta
        name="description"
        content="웹 개발 학습 내용을 정리한 Developer Wiki입니다."
    >

    <title>Developer Wiki</title>
</head>
<body>
    <header>
        <h1>Developer Wiki</h1>

        <nav aria-label="주요 메뉴">
            <a href="./index.html">홈</a>
            <a href="./html.html">HTML</a>
            <a href="./css.html">CSS</a>
            <a href="./javascript.html">JavaScript</a>
        </nav>
    </header>

    <main>
        <section>
            <h2>학습 목표</h2>

            <p>
                웹 개발 과정에서 배운 내용을 기록하고
                실무와 면접 준비에 활용합니다.
            </p>
        </section>
    </main>

    <footer>
        <p>Developer Wiki</p>
    </footer>
</body>
</html>
```

## 구조 분석

```text
html
├── head
│   ├── meta
│   ├── meta
│   ├── meta
│   └── title
└── body
    ├── header
    │   ├── h1
    │   └── nav
    │       ├── a
    │       ├── a
    │       ├── a
    │       └── a
    ├── main
    │   └── section
    │       ├── h2
    │       └── p
    └── footer
        └── p
```

## 예제에서 확인할 내용

- `<!DOCTYPE html>`로 HTML5 문서를 선언했다.
- `<html lang="ko">`로 기본 언어를 지정했다.
- `<head>`에 문자 인코딩, Viewport, 설명, 제목을 작성했다.
- `<body>`에 사용자에게 보여 줄 콘텐츠를 작성했다.
- 태그의 포함 관계에 맞게 들여쓰기를 적용했다.
- 페이지 구조에 맞는 요소를 사용했다.

> `header`, `nav`, `main`, `section`, `footer`의 의미와 사용 기준은 Semantic HTML 문서에서 자세히 학습한다.

---

# 이번 문서에서 새롭게 배운 내용

| 개념 또는 요소 | 설명 |
|---|---|
| `<!DOCTYPE html>` | HTML5 문서임을 브라우저에 알리는 선언 |
| `<html>` | HTML 문서 전체를 감싸는 최상위 요소 |
| `lang` | 문서의 기본 언어를 지정하는 속성 |
| `<head>` | 문서 설정과 메타데이터를 작성하는 영역 |
| `<meta>` | 문자 인코딩, Viewport 등의 문서 정보를 제공하는 요소 |
| `charset` | 문서의 문자 인코딩 방식을 지정하는 속성 |
| Viewport | 브라우저가 웹 페이지를 표시하는 화면 영역 |
| `<title>` | 브라우저 탭 등에 사용되는 문서 제목 |
| `<body>` | 사용자에게 보여 줄 콘텐츠를 작성하는 영역 |
| 중첩 | 요소 내부에 다른 요소를 포함하는 구조 |
| 부모·자식 관계 | HTML 요소 사이의 포함 관계 |
| 주석 | 코드 설명 또는 임시 비활성화에 사용하는 문법 |

---

# 자주 하는 실수

## 1. DOCTYPE을 생략한다

### 잘못된 예

```html
<html lang="ko">
<head>
    <title>HTML 문서</title>
</head>
<body>
</body>
</html>
```

### 올바른 예

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <title>HTML 문서</title>
</head>
<body>
</body>
</html>
```

HTML 문서의 첫 줄에 DOCTYPE을 작성한다.

---

## 2. `lang`을 기본값인 `en`으로 그대로 둔다

### 문서가 한국어인 경우

```html
<html lang="ko">
```

Emmet으로 기본 구조를 생성하면 `lang="en"`으로 만들어질 수 있으므로 문서 언어에 맞게 변경해야 한다.

---

## 3. `<title>`을 수정하지 않는다

### 좋지 않은 예

```html
<title>Document</title>
```

### 권장 예

```html
<title>HTML 문서 구조 | Developer Wiki</title>
```

문서의 내용과 목적을 알 수 있는 제목을 작성한다.

---

## 4. 화면에 표시할 콘텐츠를 `<head>`에 작성한다

### 잘못된 예

```html
<head>
    <h1>Developer Wiki</h1>
</head>
```

### 올바른 예

```html
<head>
    <title>Developer Wiki</title>
</head>

<body>
    <h1>Developer Wiki</h1>
</body>
```

본문 콘텐츠는 `<body>` 내부에 작성한다.

---

## 5. 문자 인코딩을 설정하지 않는다

```html
<meta charset="UTF-8">
```

한글을 포함하는 문서에서는 문자 깨짐을 방지하기 위해 UTF-8을 지정한다.

---

## 6. Viewport 설정을 생략한다

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

모바일 화면을 고려하는 웹 페이지에서는 기본 Viewport 설정을 작성한다.

---

## 7. 태그를 잘못된 순서로 닫는다

### 잘못된 예

```html
<p>
    <strong>중요한 내용
</p>
</strong>
```

### 올바른 예

```html
<p>
    <strong>중요한 내용</strong>
</p>
```

나중에 연 태그를 먼저 닫아야 한다.

---

## 8. 들여쓰기를 사용하지 않는다

### 가독성이 낮은 코드

```html
<body><main><section><h1>HTML</h1></section></main></body>
```

### 가독성이 높은 코드

```html
<body>
    <main>
        <section>
            <h1>HTML</h1>
        </section>
    </main>
</body>
```

브라우저의 동작뿐 아니라 개발자가 읽고 관리하기 쉬운 코드도 중요하다.

---

## 9. 주석에 민감한 정보를 작성한다

```html
<!-- 관리자 비밀번호: 1234 -->
```

HTML 주석은 화면에 직접 표시되지 않을 뿐, 사용자가 원본 코드나 개발자 도구에서 확인할 수 있다.

---

# 면접 포인트

## Q1. HTML 문서의 기본 구조를 설명해 주세요

HTML 문서는 먼저 `<!DOCTYPE html>`로 HTML5 문서임을 선언한다.

그 아래에 최상위 요소인 `<html>`을 작성하고, 내부를 `<head>`와 `<body>`로 구분한다.

`<head>`에는 문자 인코딩, Viewport, 문서 제목, 외부 파일 연결 등의 정보를 작성하고, `<body>`에는 사용자에게 보여 줄 콘텐츠를 작성한다.

---

## Q2. `<!DOCTYPE html>`은 HTML 태그인가요?

일반적인 HTML 태그가 아니다.

`<!DOCTYPE html>`은 문서가 HTML5 형식임을 브라우저에 알리는 문서 유형 선언이다.

브라우저가 문서를 표준 모드로 해석할 수 있도록 HTML 문서의 첫 줄에 작성한다.

---

## Q3. `<head>`와 `<body>`의 차이는 무엇인가요?

`<head>`에는 문서 제목, 문자 인코딩, Viewport, 외부 파일 연결 등 문서의 설정과 부가 정보를 작성한다.

`<body>`에는 제목, 문단, 이미지, 링크, 버튼처럼 사용자에게 보여 줄 실제 콘텐츠를 작성한다.

---

## Q4. `<title>`과 `<h1>`의 차이는 무엇인가요?

`<title>`은 `<head>` 내부에 작성하며 브라우저 탭과 문서 제목 정보에 사용된다.

`<h1>`은 `<body>` 내부에 작성하며 웹 페이지 본문에서 가장 중요한 제목을 나타낸다.

---

## Q5. `<meta charset="UTF-8">`은 왜 사용하나요?

HTML 문서에서 사용하는 문자 인코딩 방식을 UTF-8로 지정하기 위해 사용한다.

문자 인코딩이 올바르게 설정되지 않으면 한글과 특수문자가 깨져 표시될 수 있다.

---

## Q6. Viewport 설정은 왜 필요한가요?

모바일 기기에서 웹 페이지의 너비와 초기 확대 비율을 기기 화면에 맞게 설정하기 위해 사용한다.

일반적으로 다음 코드를 사용한다.

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

---

## Q7. HTML 요소의 중첩이란 무엇인가요?

하나의 HTML 요소 내부에 다른 요소를 포함하는 구조를 의미한다.

중첩된 요소들은 부모, 자식, 조상, 후손, 형제 관계를 형성하며, 이러한 관계는 CSS 선택자와 JavaScript DOM 조작에서도 중요하게 사용된다.

---

## Q8. HTML에서 들여쓰기가 반드시 필요한 문법인가요?

대부분의 경우 들여쓰기가 없어도 브라우저는 HTML을 해석할 수 있다.

하지만 들여쓰기는 요소의 중첩 구조를 명확하게 보여 주고 코드의 가독성과 유지보수성을 높이기 때문에 실무에서 일관되게 적용해야 한다.

---

# 핵심 정리

- HTML 문서는 `<!DOCTYPE html>`, `<html>`, `<head>`, `<body>`를 기본 구조로 사용한다.
- `<!DOCTYPE html>`은 HTML5 문서임을 브라우저에 알리는 선언이다.
- `<html>`은 문서 전체를 감싸는 최상위 요소이다.
- `lang` 속성은 문서의 기본 언어를 지정한다.
- `<head>`에는 문서 설정과 메타데이터를 작성한다.
- `<body>`에는 사용자에게 보여 줄 콘텐츠를 작성한다.
- `<meta charset="UTF-8">`은 문자 인코딩을 설정한다.
- Viewport 메타 태그는 모바일 화면 대응을 위한 기본 설정이다.
- `<title>`은 브라우저 탭 등에 사용되는 문서 제목이다.
- HTML 요소는 부모와 자식 관계를 가지는 트리 구조로 중첩된다.
- 태그는 올바른 순서로 닫고, 들여쓰기를 통해 구조를 명확하게 표현해야 한다.
- HTML 주석에는 외부에 노출되면 안 되는 민감한 정보를 작성하지 않는다.

---

# 변경 이력

| Version | 날짜 | 변경 내용 |
|---|---|---|
| v1.0 | 이전 작성일 | HTML 문서 구조 최초 작성 |
| v1.1 | 2026-07-21 | 문서 전체 구조 개선 |
| v1.1 | 2026-07-21 | DOCTYPE, html, head, body의 역할 보강 |
| v1.1 | 2026-07-21 | 문자 인코딩과 Viewport 설명 추가 |
| v1.1 | 2026-07-21 | 요소의 중첩과 부모·자식 관계 추가 |
| v1.1 | 2026-07-21 | HTML 주석과 작성 순서 추가 |
| v1.1 | 2026-07-21 | 실무 예제 프로젝트와 구조 분석 추가 |
| v1.1 | 2026-07-21 | 자주 하는 실수와 면접 포인트 보강 |
