---
title: HTML 문서 기본 구조
category: HTML
last_updated: 2026-07-27
status: Active
---

# HTML 문서 기본 구조


## 기본 문법

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>문서 제목</title>
</head>
<body>
  <h1>페이지 제목</h1>
  <p>본문 내용</p>
</body>
</html>
```

## 각 영역의 역할

- `<!DOCTYPE html>`: HTML5 문서임을 브라우저에 알린다.
- `<html>`: 전체 문서의 최상위 요소다.
- `<head>`: 문자 인코딩, 화면 배율, 제목처럼 화면 본문 밖의 정보를 담는다.
- `<body>`: 사용자가 실제로 보는 콘텐츠를 담는다.
- `lang="ko"`: 문서의 기본 언어를 나타낸다.

## 실무 연결

모바일 화면에서 viewport 설정이 없으면 페이지가 축소되어 보일 수 있다. 수업에서 작성한 모든 기본 문서처럼 초기 템플릿에 포함하는 습관을 들인다.

## 주의사항

- `title`은 브라우저 탭과 검색 결과에 사용될 수 있으므로 비워두지 않는다.
- 태그 들여쓰기를 맞추면 부모와 자식 관계를 빠르게 파악할 수 있다.
- 닫는 태그 누락은 이후 레이아웃 오류의 원인이 된다.
