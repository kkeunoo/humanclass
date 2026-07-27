---
title: "HTML 문서 기본 구조"
area: "HTML"
version: "v4.3"
last_updated: "2026-07-27"
difficulty: "★☆☆☆☆"
estimated_time: "20~30분"
---

# HTML 문서 기본 구조

## 학습 목표

- HTML 문서의 기본 골격을 직접 작성할 수 있다.
- `head`와 `body`의 역할을 구분할 수 있다.
- `lang`, `charset`, `title`의 역할을 설명할 수 있다.

## 왜 배우는가

브라우저는 HTML 문서의 구조를 기준으로 페이지를 해석합니다. 기본 구조를 정확히 작성하면 한글 깨짐, 제목 누락, 잘못된 중첩 같은 문제를 줄일 수 있습니다.

## 기본 개념

### 기본 골격

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>문서 제목</title>
</head>
<body>
    화면에 표시할 내용
</body>
</html>
```

- `<!DOCTYPE html>`: HTML5 문서임을 알립니다.
- `<html lang="ko">`: 문서의 주 언어를 지정합니다.
- `<head>`: 문서 설정과 제목처럼 화면에 직접 표시되지 않는 정보를 담습니다.
- `<body>`: 사용자가 보는 실제 콘텐츠를 담습니다.

## 수업 예제

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>Developer Wiki</title>
</head>
<body>
    <h1>안녕하세요.</h1>
    <p>HTML 공부를 시작합니다.</p>
</body>
</html>
```

## 수업 문제

### 문제

HTML 기본 문서를 작성하고 브라우저 탭 제목과 본문 내용을 완성하세요.

### 요구사항

- 문서 언어는 한국어로 지정합니다.
- 브라우저 탭 제목은 `Developer Wiki`로 작성합니다.
- 본문에는 제목과 문단을 각각 한 개 작성합니다.

### 직접 풀어 보기

해설을 열기 전에 빈 HTML 파일에 직접 작성하고 브라우저에서 결과를 확인합니다.

<details>
<summary>해설 보기</summary>

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>Developer Wiki</title>
</head>
<body>
    <h1>안녕하세요.</h1>
    <p>HTML 공부를 시작합니다.</p>
</body>
</html>
```

### 풀이 설명

`head`에는 문서 설정과 탭 제목을 작성하고, `body`에는 화면에 표시할 제목과 문단을 작성합니다.

</details>

## 자주 하는 실수

- `<!DOCTYPE html>`을 빠뜨리는 경우
- `head` 안에 화면 콘텐츠를 작성하는 경우
- 시작 태그와 종료 태그의 중첩 순서가 어긋나는 경우

## 실무 연결

새 HTML 파일을 만들 때 가장 먼저 작성하는 기본 뼈대입니다. 페이지마다 동일한 골격을 유지하면 유지보수와 협업이 쉬워집니다.

## 📌 더 알아보기

### 들여쓰기

HTML에서 들여쓰기는 문법상 필수는 아니지만 부모와 자식 관계를 읽기 쉽게 만듭니다. 팀 프로젝트에서는 일관된 들여쓰기를 유지합니다.

## 직접 해보기

- `title` 내용을 바꾸고 브라우저 탭을 확인한다.
- `lang="ko"`를 다른 언어 코드로 바꾸어 본다.
- `body` 안에 제목과 문단을 하나씩 더 추가한다.

## Check Point

- [ ] HTML 기본 골격을 직접 작성할 수 있다.
- [ ] `head`와 `body`의 차이를 설명할 수 있다.
- [ ] `meta charset`과 `title`의 역할을 설명할 수 있다.

## 최종 요약

HTML 문서는 `doctype`, `html`, `head`, `body` 순서로 구성합니다. 문서 설정은 `head`, 실제 화면 콘텐츠는 `body`에 작성합니다.

## 복습 기록

- [ ] 예제를 직접 입력했다.
- [ ] 수업 문제를 해설 없이 풀었다.
- [ ] 틀린 부분을 수정하고 이유를 기록했다.

## 이전 · 다음 학습

| 구분 | 문서 |
|---|---|
| 이전 학습 | [HTML README](../README.md) |
| 다음 학습 | [HTML 태그와 속성](HTML_Tag_Attribute.md) |
