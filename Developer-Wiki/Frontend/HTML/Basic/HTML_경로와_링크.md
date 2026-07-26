---
title: HTML 경로와 링크
version: v1.0
last_updated: 2026-07-25
status: Completed
---

# HTML 경로와 링크

## 개념

링크는 다른 문서나 위치로 이동하게 하며, 상대 경로는 현재 파일 위치를 기준으로 자원을 찾는다.

## 문법

```html
<a href="detail.html">같은 폴더</a>
<a href="../index.html">상위 폴더</a>
<a href="https://example.com">외부 주소</a>
```

## 예제

```html
<a href="#contact">연락처로 이동</a>
<h2 id="contact">연락처</h2>
```

## 실무 예제

목록 페이지에서 상세 페이지로 이동하고, 상세 페이지에서 뒤로 돌아오는 구조를 만든다.

## 주의사항

상대 경로는 현재 HTML 파일 기준이다. 새 창이 꼭 필요할 때만 `target="_blank"`를 사용한다.

## 면접 포인트

절대 경로와 상대 경로의 차이를 설명한다.

## 요약

`href`와 올바른 경로 계산이 링크 구현의 핵심이다.
