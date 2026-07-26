---
title: HTML 태그와 속성
version: v1.1
last_updated: 2026-07-21
status: Completed
---

# HTML 태그와 속성

## 📖 개요

HTML(HyperText Markup Language)은 웹 페이지의 **구조(Structure)** 를 정의하는 마크업 언어이다.

HTML은 데이터를 화면에 어떻게 배치할지 결정하며, CSS는 디자인을 담당하고 JavaScript는 동작을 담당한다.

HTML 문서는 **태그(Tag)** 와 **속성(Attribute)** 으로 구성된다.

---

# 핵심 개념

## HTML의 역할

웹 개발에서 각각의 역할은 다음과 같다.

| 기술 | 역할 |
|------|------|
| HTML | 웹 페이지의 구조 |
| CSS | 디자인 및 레이아웃 |
| JavaScript | 동적인 기능 |

예를 들어 집을 만든다고 생각하면

- HTML → 뼈대
- CSS → 인테리어
- JavaScript → 전기·자동문 등의 기능

이라고 이해하면 쉽다.

---

# 태그(Tag)

태그(Tag)는 HTML에서 요소를 정의하는 명령어이다.

예를 들어

```html
<h1>안녕하세요</h1>
```

여기에서

- `<h1>` : 시작 태그(Start Tag)
- `</h1>` : 종료 태그(End Tag)

를 의미한다.

---

## 요소(Element)

많은 사람들이 **태그(Tag)** 와 **요소(Element)** 를 같은 의미로 사용하지만 엄밀히는 다르다.

```html
<p>Hello HTML</p>
```

| 구분 | 의미 |
|------|------|
| `<p>` | 시작 태그 |
| `</p>` | 종료 태그 |
| `<p>Hello HTML</p>` | 요소(Element) |

즉,

> 요소(Element)는 **시작 태그 + 내용 + 종료 태그 전체**를 의미한다.

---

# 속성(Attribute)

속성(Attribute)은 태그에 **추가적인 정보**를 제공한다.

예를 들어 링크를 만들 때는 이동할 주소가 필요하다.

```html
<a href="https://google.com">
    Google
</a>
```

여기에서

- `href` → 속성 이름
- `"https://google.com"` → 속성 값(Value)

이다.

속성은 일반적으로

```html
속성이름="속성값"
```

형태로 작성한다.

---

## 여러 개의 속성 사용

하나의 태그에는 여러 개의 속성을 사용할 수 있다.

```html
<img
    src="cat.jpg"
    alt="고양이 사진"
    width="300"
>
```

| 속성 | 역할 |
|------|------|
| src | 이미지 위치 |
| alt | 이미지 설명 |
| width | 이미지 너비 |

---

# 빈 요소(Empty Element)

일부 태그는 종료 태그가 존재하지 않는다.

이를 **빈 요소(Empty Element)** 또는 **빈 태그**라고 한다.

대표적인 예

```html
<br>

<hr>

<img src="cat.jpg" alt="고양이">

<input type="text">
```

이러한 태그는 화면에 표시할 콘텐츠를 내부에 포함하지 않기 때문에 종료 태그가 필요하지 않다.

---

# HTML 작성 규칙

실무에서는 다음과 같은 작성 규칙을 지키는 것이 좋다.

✅ 태그 이름은 소문자로 작성

```html
<div></div>
```

---

✅ 속성값은 큰따옴표 사용

```html
<a href="/about">
```

---

✅ 들여쓰기를 통해 구조를 표현

```html
<body>

    <main>

        <section>

            <h1>HTML</h1>

        </section>

    </main>

</body>
```

---

✅ 의미 있는 태그 사용

나중에 배우게 될 `header`, `main`, `section`, `article` 등의 Semantic Tag를 적극적으로 사용하는 것이 좋다.

---

# 실무 활용

HTML 태그와 속성은 거의 모든 웹 페이지에서 사용된다.

예를 들어

- 로그인 페이지
- 쇼핑몰
- 게시판
- 기업 홈페이지

모두 태그와 속성을 조합하여 만들어진다.

태그는 **구조를 만들고**, 속성은 **세부 정보를 추가한다.**

---

# 실무 예제 프로젝트

다음은 기업 홈페이지 상단(Header)의 간단한 예시이다.

```html
<header>

    <h1>Developer Wiki</h1>

    <nav>

        <a href="/">Home</a>

        <a href="/courses">Courses</a>

        <a href="/contact">Contact</a>

    </nav>

</header>
```

### 사용된 태그

- `header`
- `h1`
- `nav`
- `a`

### 사용된 속성

- `href`

이처럼 하나의 화면도 여러 태그와 속성이 함께 사용되어 구성된다.

---

# 이번 문서에서 새롭게 배운 내용

| 개념 | 설명 |
|------|------|
| HTML | 웹 페이지의 구조를 만드는 마크업 언어 |
| Tag | HTML 명령어 |
| Element | 시작 태그부터 종료 태그까지의 전체 |
| Attribute | 태그의 추가 정보 |
| Empty Element | 종료 태그가 없는 요소 |

---

# 자주 하는 실수

### 1. 태그와 요소를 같은 의미로 생각한다.

```html
<p>Hello</p>
```

- `<p>` → 태그
- `<p>Hello</p>` → 요소

---

### 2. 속성값에 따옴표를 생략한다.

❌

```html
<a href=https://google.com>
```

✅

```html
<a href="https://google.com">
```

---

### 3. 닫는 태그를 빠뜨린다.

❌

```html
<p>Hello
```

✅

```html
<p>Hello</p>
```

---

# 면접 포인트

### Q1. HTML은 프로그래밍 언어인가요?

아니다.

HTML은 웹 문서의 구조를 정의하는 **마크업 언어**이다.

---

### Q2. 태그와 요소(Element)의 차이는 무엇인가요?

태그는 `<p>`와 같은 명령 자체를 의미하고,

요소(Element)는 시작 태그부터 종료 태그까지 전체를 의미한다.

---

### Q3. 속성(Attribute)은 무엇인가요?

태그에 추가 정보를 제공하는 값이다.

대표적으로 `href`, `src`, `alt`, `id`, `class` 등이 있다.

---

# 핵심 정리

- HTML은 웹 페이지의 구조를 정의하는 마크업 언어이다.
- HTML 문서는 태그와 속성으로 구성된다.
- 요소(Element)는 시작 태그부터 종료 태그까지 전체를 의미한다.
- 속성(Attribute)은 태그에 추가 정보를 제공한다.
- 일부 태그는 종료 태그가 없는 빈 요소이다.
- 실무에서는 가독성을 위해 들여쓰기와 의미 있는 태그를 사용하는 것이 중요하다.

---

# 변경 이력

| Version | 내용 |
|---------|------|
| v1.0 | 최초 작성 |
| v1.1 | 문서 구조 개선, 실무 예제 프로젝트 추가, 면접 포인트 및 핵심 정리 보강 |