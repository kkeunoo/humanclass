---
title: HTML 링크 경로 이미지
category: HTML
last_updated: 2026-07-27
status: Active
---

# HTML 링크 경로 이미지


## 링크

```html
<a href="detail.html">상세 보기</a>
<a href="https://example.com" target="_blank">외부 사이트</a>
```

## 상대 경로

```text
index.html
asset/
  image.png
detail/
  page.html
```

```html
<img src="asset/image.png" alt="예시 이미지">
<a href="detail/page.html">상세</a>
```

하위 폴더에서 상위 폴더로 이동할 때는 `../`를 사용한다.

## 이미지

```html
<img src="asset/profile.png" alt="사용자 프로필 사진" width="200">
```

`alt`는 이미지가 보이지 않을 때 대체 설명을 제공한다.

## 주의사항

- Windows 경로의 역슬래시가 아니라 웹 경로의 `/`를 사용한다.
- 파일명 대소문자를 일관되게 작성한다.
- 이미지 크기를 HTML 속성만으로 무리하게 조절하기보다 CSS를 사용한다.
