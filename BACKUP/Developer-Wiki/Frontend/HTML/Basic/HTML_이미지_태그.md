---
title: HTML 이미지 태그
version: v1.0
last_updated: 2026-07-21
status: Completed
---

# HTML 이미지 태그

## 개요

이미지는 웹 페이지에서 정보를 전달하는 가장 중요한 요소 중 하나이다.

HTML에서는 `<img>` 태그를 사용하여 이미지를 화면에 표시한다.

이미지는 단순히 화면을 꾸미는 요소가 아니라 상품, 로고, 배너, 아이콘, 프로필 사진, 차트 등 다양한 정보를 전달하는 역할을 한다.

`<img>`는 종료 태그가 없는 **빈 요소(Empty Element)**이다.

```html
<img
    src="./images/logo.png"
    alt="Developer Academy 로고"
>
```

---

# 핵심 개념

이미지를 화면에 표시하려면 최소 두 가지 정보가 필요하다.

- 이미지 파일의 위치
- 이미지를 설명하는 대체 텍스트

```html
<img
    src="./images/profile.jpg"
    alt="강사의 프로필 사진"
>
```

| 속성 | 역할 |
|------|------|
| src | 이미지 파일 위치 |
| alt | 이미지를 설명하는 대체 텍스트 |

---

# img 태그

`img`는 Image의 약자이다.

```html
<img
    src="./images/html.png"
    alt="HTML 로고"
>
```

`img`는 콘텐츠를 포함하지 않는 빈 요소이므로 종료 태그가 없다.

```html
<img src="./images/html.png" alt="HTML 로고">
```

---

# src 속성

`src`는 Source의 약자이며 이미지 파일의 경로를 지정한다.

```html
<img
    src="./images/logo.png"
    alt="회사 로고"
>
```

사용할 수 있는 경로는 다음과 같다.

## 같은 폴더

```html
<img
    src="./logo.png"
    alt="회사 로고"
>
```

---

## 하위 폴더

```html
<img
    src="./images/logo.png"
    alt="회사 로고"
>
```

---

## 상위 폴더

```html
<img
    src="../images/logo.png"
    alt="회사 로고"
>
```

---

## 외부 이미지

```html
<img
    src="https://example.com/logo.png"
    alt="회사 로고"
>
```

외부 이미지는 해당 서버의 상태나 정책에 따라 표시되지 않을 수도 있다.

---

# alt 속성

`alt`는 Alternative Text의 약자이다.

이미지를 볼 수 없을 때 이미지를 대신 설명하는 텍스트이다.

```html
<img
    src="./images/student.jpg"
    alt="노트북으로 코딩하는 수강생"
>
```

다음과 같은 경우에 사용된다.

- 이미지 로딩 실패
- 화면 낭독기 사용
- 검색 엔진이 이미지 내용을 이해할 때

---

## 좋은 alt 작성

```html
<img
    src="./images/keyboard.jpg"
    alt="무선 기계식 키보드"
>
```

```html
<img
    src="./images/frontend-course.jpg"
    alt="프론트엔드 개발 과정 수업 장면"
>
```

이미지가 전달하는 정보를 자연스럽게 설명한다.

---

## 좋지 않은 alt

```html
alt="image"

alt="사진"

alt="img"

alt="123"
```

파일명이나 의미 없는 문구는 도움이 되지 않는다.

---

## 장식용 이미지

이미지가 단순한 장식이라면 빈 문자열을 사용한다.

```html
<img
    src="./images/background-decoration.png"
    alt=""
>
```

화면 낭독기는 장식 이미지를 건너뛸 수 있다.

---

# width와 height

이미지 크기를 지정할 수 있다.

```html
<img
    src="./images/logo.png"
    alt="Developer Academy 로고"
    width="200"
    height="80"
>
```

가능하면 이미지의 실제 비율에 맞는 값을 지정하는 것이 좋다.

브라우저가 이미지 공간을 미리 계산하여 화면 흔들림(CLS)을 줄이는 데 도움이 된다.

---

# 이미지 비율

가로와 세로 중 하나만 CSS로 변경하면 비율이 유지된다.

```css
img {
    width: 300px;
    height: auto;
}
```

가로와 세로를 모두 임의로 지정하면 이미지가 찌그러질 수 있다.

```css
img {
    width: 300px;
    height: 300px;
}
```

---

# figure와 figcaption

이미지와 설명을 하나의 의미 있는 그룹으로 묶을 수 있다.

```html
<figure>

    <img
        src="./images/classroom.jpg"
        alt="실무 프로젝트 발표 장면"
    >

    <figcaption>

        실무 프로젝트 발표 수업

    </figcaption>

</figure>
```

사진, 차트, 코드 예제 등에 자주 사용한다.

---

# 반응형 이미지

이미지는 부모 요소에 맞게 크기가 조정되는 경우가 많다.

```css
img {

    max-width:100%;

    height:auto;

}
```

실무에서 가장 많이 사용하는 기본 설정이다.

---

# loading 속성

브라우저가 이미지를 언제 불러올지 지정할 수 있다.

```html
<img
    src="./images/course.jpg"
    alt="교육 과정"
    loading="lazy"
>
```

| 값 | 의미 |
|------|------|
| eager | 바로 로딩 |
| lazy | 필요할 때 로딩 |

긴 페이지에서는 `lazy`가 성능 향상에 도움이 될 수 있다.

---

# decoding 속성

브라우저가 이미지를 디코딩하는 방식을 힌트로 전달할 수 있다.

```html
<img
    src="./images/banner.jpg"
    alt="메인 배너"
    decoding="async"
>
```

| 값 | 의미 |
|------|------|
| auto | 브라우저 기본 |
| sync | 동기 처리 |
| async | 비동기 처리 |

대부분의 경우 기본값이나 `async`를 사용한다.

---

# srcset

화면 크기나 해상도에 따라 다른 이미지를 사용할 수 있다.

```html
<img
    src="./images/card-small.jpg"
    srcset="
        ./images/card-small.jpg 480w,
        ./images/card-medium.jpg 768w,
        ./images/card-large.jpg 1200w
    "
    sizes="(max-width:768px) 100vw, 50vw"
    alt="교육 과정"
>
```

모바일과 데스크톱에 적절한 이미지를 제공할 수 있다.

---

# picture 요소

상황에 따라 완전히 다른 이미지를 제공할 수 있다.

```html
<picture>

    <source
        media="(min-width:768px)"
        srcset="./images/banner-desktop.jpg"
    >

    <source
        media="(max-width:767px)"
        srcset="./images/banner-mobile.jpg"
    >

    <img
        src="./images/banner-desktop.jpg"
        alt="Developer Academy 메인 배너"
    >

</picture>
```

반응형 배너에서 많이 사용한다.

---

# 이미지 최적화

이미지를 그대로 업로드하면 페이지가 느려질 수 있다.

실무에서는 다음을 고려한다.

- 적절한 해상도
- WebP, AVIF 사용
- 압축
- Lazy Loading
- CDN 활용
- srcset 활용

---

# 이미지 포맷

| 형식 | 특징 |
|------|------|
| JPG | 사진 |
| PNG | 투명 배경 |
| GIF | 간단한 애니메이션 |
| SVG | 로고, 아이콘 |
| WebP | 높은 압축률 |
| AVIF | 최신 고효율 포맷 |

---

# 이미지와 링크

이미지는 링크가 될 수도 있다.

```html
<a href="./index.html">

    <img
        src="./images/logo.svg"
        alt="Developer Academy 홈"
    >

</a>
```

로고는 일반적으로 홈으로 이동한다.

---

# 이미지와 접근성

좋은 예

```html
<img
    src="./images/course.jpg"
    alt="프론트엔드 개발 과정 수업 장면"
>
```

나쁜 예

```html
alt="photo"

alt="image"

alt="123"
```

장식 이미지

```html
alt=""
```

---

# 실무 활용

다음과 같은 화면에서 자주 사용한다.

- 회사 로고
- 쇼핑몰 상품
- 프로필 사진
- 배너
- 카드 UI
- 블로그 썸네일
- 교육 과정 소개
- 포트폴리오

---

# 실무 예제 프로젝트

```html
<header>

    <a href="./index.html">

        <img
            src="./images/logo.svg"
            alt="Developer Academy 홈"
            width="180"
            height="60"
        >

    </a>

</header>

<main>

    <section>

        <h1>프론트엔드 개발 과정</h1>

        <figure>

            <img
                src="./images/frontend-course.webp"
                alt="HTML과 CSS 수업을 진행하는 강사와 수강생"
                width="1200"
                height="700"
                loading="lazy"
            >

            <figcaption>

                실무 프로젝트 중심의 프론트엔드 수업

            </figcaption>

        </figure>

    </section>

</main>
```

---

# 이번 문서에서 새롭게 배운 내용

| 개념 | 설명 |
|------|------|
| img | 이미지 요소 |
| src | 이미지 위치 |
| alt | 대체 텍스트 |
| width | 가로 크기 |
| height | 세로 크기 |
| figure | 이미지 그룹 |
| figcaption | 이미지 설명 |
| loading | 이미지 지연 로딩 |
| decoding | 이미지 디코딩 방식 |
| srcset | 반응형 이미지 |
| picture | 상황별 이미지 |
| WebP | 고효율 이미지 포맷 |
| SVG | 벡터 이미지 |
| CLS | 레이아웃 흔들림 감소 |

---

# 자주 하는 실수

## 1.

`alt`를 작성하지 않는다.

```html
<img src="./logo.png">
```

→ 접근성이 크게 떨어진다.

---

## 2.

파일명을 alt로 작성한다.

```html
alt="logo.png"
```

---

## 3.

장식 이미지에도 설명을 작성한다.

```html
alt="배경 장식"
```

→ 장식 이미지는 `alt=""`

---

## 4.

가로 세로를 모두 임의 지정한다.

이미지가 찌그러질 수 있다.

---

## 5.

10MB 이미지를 그대로 사용한다.

압축하여 업로드한다.

---

## 6.

PNG로 사진을 저장한다.

사진은 JPG 또는 WebP가 적절한 경우가 많다.

---

## 7.

로고에 alt를 비워 둔다.

링크 목적을 다른 방식으로 제공하지 않는다면 로고의 역할을 설명해야 한다.

---

## 8.

모든 이미지를 eager로 불러온다.

긴 페이지에서는 `loading="lazy"`를 고려한다.

---

# 면접 포인트

### Q1.

img 태그의 필수 속성은?

→ `src`

접근성과 의미 전달을 위해 `alt`도 함께 작성하는 것이 권장된다.

---

### Q2.

alt는 왜 필요한가?

이미지를 볼 수 없는 환경에서도 내용을 전달하기 위해 사용한다.

---

### Q3.

장식 이미지는 어떻게 작성하나요?

```html
alt=""
```

---

### Q4.

figure는 언제 사용하나요?

사진, 차트, 코드처럼 설명과 함께 하나의 콘텐츠를 구성할 때 사용한다.

---

### Q5.

loading="lazy"는 무엇인가요?

화면에 가까워질 때 이미지를 불러와 초기 로딩 성능을 개선하는 데 도움이 되는 속성이다.

---

### Q6.

srcset은 왜 사용하나요?

화면 크기와 해상도에 맞는 이미지를 제공하여 품질과 성능을 함께 개선하기 위해 사용한다.

---

### Q7.

SVG와 PNG의 차이는?

SVG는 벡터 이미지라 확대해도 품질이 유지되며 로고와 아이콘에 적합하다.

PNG는 비트맵 이미지로 투명 배경을 지원한다.

---

# 핵심 정리

- `<img>`는 이미지를 표시하는 빈 요소이다.
- `src`에는 이미지 경로를 작성한다.
- `alt`는 이미지의 의미를 설명하는 대체 텍스트이다.
- 장식 이미지는 `alt=""`를 사용한다.
- `width`와 `height`를 함께 지정하면 레이아웃 안정성에 도움이 된다.
- 반응형 이미지는 `max-width: 100%`와 `height: auto`를 자주 사용한다.
- `loading="lazy"`는 긴 페이지의 성능 개선에 도움이 된다.
- `srcset`과 `picture`를 사용하면 화면 환경에 맞는 이미지를 제공할 수 있다.
- `figure`와 `figcaption`은 이미지와 설명을 하나의 의미 있는 콘텐츠로 묶는다.
- 적절한 이미지 포맷과 최적화는 웹 성능에 큰 영향을 준다.

---

# 변경 이력

| Version | 날짜 | 변경 내용 |
|------|------|----------|
| v1.0 | 2026-07-21 | 최초 작성 |
| v1.0 | 2026-07-21 | img, src, alt 설명 추가 |
| v1.0 | 2026-07-21 | figure, figcaption 추가 |
| v1.0 | 2026-07-21 | loading, decoding, srcset, picture 추가 |
| v1.0 | 2026-07-21 | 이미지 최적화 및 포맷 정리 |
| v1.0 | 2026-07-21 | 실무 예제 프로젝트 추가 |
| v1.0 | 2026-07-21 | 접근성, 면접 포인트, 자주 하는 실수 보강 |