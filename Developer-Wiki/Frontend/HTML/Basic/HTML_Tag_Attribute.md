---
title: HTML 태그와 속성
category: HTML
last_updated: 2026-07-27
status: Active
---

# HTML 태그와 속성


## 태그 기본 형태

```html
<p>문단</p>
<a href="detail.html">상세 페이지</a>
<img src="asset/photo.png" alt="설명 문구">
```

`p`, `a`, `img`는 태그 이름이고 `href`, `src`, `alt`는 속성이다.

## 블록과 인라인의 기본 이해

HTML 요소는 기본적으로 줄 전체를 차지하는 요소와 콘텐츠 크기만큼 배치되는 요소로 나뉜다. 실제 배치 방식은 CSS `display`로 바꿀 수 있다.

```html
<div>새 줄에서 시작하는 영역</div>
<span>문장 안에 들어가는 영역</span>
```

## 자주 사용한 태그

- 제목: `h1`~`h6`
- 문단: `p`
- 줄바꿈: `br`
- 구분선: `hr`
- 영역: `div`, `span`
- 강조: `strong`, `em`

## 주의사항

- 태그를 화면 모양만 보고 선택하지 않는다.
- 같은 페이지에서 `h1`은 페이지의 대표 제목으로 사용한다.
- `br`을 여백 조절 목적으로 반복하지 않고 CSS margin을 사용한다.
