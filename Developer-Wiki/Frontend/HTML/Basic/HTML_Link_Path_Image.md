---
title: "HTML 링크·경로·이미지"
area: "HTML"
version: "v4.3"
last_updated: "2026-07-27"
difficulty: "★★☆☆☆"
estimated_time: "35~50분"
---

# HTML 링크·경로·이미지

## 학습 목표

- `a` 태그로 페이지를 연결할 수 있다.
- 상대 경로와 절대 경로를 구분할 수 있다.
- 이미지의 `src`와 `alt`를 올바르게 작성할 수 있다.

## 왜 배우는가

웹 페이지는 링크로 서로 연결되고 이미지는 경로를 통해 불러옵니다. 경로를 정확히 이해해야 이미지가 깨지거나 페이지 이동이 실패하는 문제를 해결할 수 있습니다.

## 기본 개념

### 링크

```html
<a href="about.html">소개 페이지</a>
<a href="https://example.com" target="_blank">외부 사이트</a>
```

### 이미지

```html
<img src="images/logo.png" alt="Developer Wiki 로고">
```

### 상대 경로

- 같은 폴더: `about.html`
- 하위 폴더: `images/photo.jpg`
- 상위 폴더: `../index.html`

## 수업 예제

```html
<a href="pages/course.html">강의 안내</a>
<a href="#contact">문의 영역으로 이동</a>
<img src="images/course.jpg" alt="노트북으로 공부하는 모습">

<section id="contact">
    <h2>문의</h2>
</section>
```

## 수업 문제

### 문제

상대 경로 이미지, 새 창 링크, 같은 페이지 이동 링크를 모두 작성하세요.

### 요구사항

- 이미지는 `images/profile.png`를 사용합니다.
- 외부 링크는 새 창에서 엽니다.
- `id="info"`인 영역으로 이동하는 내부 링크를 작성합니다.
- 모든 이미지에 의미 있는 `alt`를 작성합니다.

### 직접 풀어 보기

해설을 열기 전에 빈 HTML 파일에 직접 작성하고 브라우저에서 결과를 확인합니다.

<details>
<summary>해설 보기</summary>

```html
<a href="https://example.com" target="_blank">외부 사이트 열기</a>
<a href="#info">정보 영역으로 이동</a>

<img src="images/profile.png" alt="수강생 프로필 이미지">

<section id="info">
    <h2>과정 정보</h2>
    <p>프론트엔드 기초 과정입니다.</p>
</section>
```

### 풀이 설명

외부 주소는 전체 URL을 사용하고, 내부 이동은 `#id` 형식으로 연결합니다. 이미지 경로는 현재 HTML 파일의 위치를 기준으로 작성합니다.

</details>

## 자주 하는 실수

- 파일 위치를 기준으로 경로를 계산하지 않는 경우
- 장식이 아닌 이미지의 `alt`를 비워 두는 경우
- 새 창 링크에 불필요하게 모두 `target="_blank"`를 사용하는 경우

## 실무 연결

내비게이션, 상세 페이지 이동, 배너와 상품 이미지처럼 대부분의 웹 화면에서 링크와 경로를 사용합니다.

## 📌 더 알아보기

### 절대 경로와 루트 상대 경로

외부 사이트는 `https://`로 시작하는 절대 URL을 사용합니다. 서버 환경에서는 `/assets/logo.png`처럼 사이트 루트를 기준으로 작성할 수도 있습니다.

### 이미지 지연 로딩

```html
<img src="photo.jpg" alt="강의실" loading="lazy">
```

`loading="lazy"`는 화면에 가까워질 때 이미지를 불러오도록 브라우저에 요청하는 선택 사항입니다.

## 직접 해보기

- 이미지 파일을 다른 폴더로 옮겼다고 가정하고 경로를 수정한다.
- 내부 링크의 대상 `id`를 변경하고 함께 수정한다.
- `target="_blank"`를 제거했을 때 차이를 확인한다.

## Check Point

- [ ] 같은 폴더, 하위 폴더, 상위 폴더 경로를 작성할 수 있다.
- [ ] 링크의 `href`와 이미지의 `src` 역할을 구분할 수 있다.
- [ ] 이미지에 적절한 `alt`를 작성할 수 있다.

## 최종 요약

링크는 `href`, 이미지는 `src`로 경로를 지정합니다. 상대 경로는 현재 문서 위치를 기준으로 계산하며, 이미지에는 목적을 설명하는 `alt`가 필요합니다.

## 복습 기록

- [ ] 예제를 직접 입력했다.
- [ ] 수업 문제를 해설 없이 풀었다.
- [ ] 틀린 부분을 수정하고 이유를 기록했다.

## 이전 · 다음 학습

| 구분 | 문서 |
|---|---|
| 이전 학습 | [HTML 태그와 속성](HTML_Tag_Attribute.md) |
| 다음 학습 | [HTML 목록과 표](HTML_List_Table.md) |
