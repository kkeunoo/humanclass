---
title: CSS 선택자와 우선순위
category: CSS
last_updated: 2026-07-27
status: Active
---

# CSS 선택자와 우선순위


## 기본 선택자

```css
p { color: #333; }
.notice { color: orange; }
#main-title { color: navy; }
```

- 태그 선택자: 같은 태그 전체
- 클래스 선택자: 재사용 가능한 그룹
- 아이디 선택자: 문서에서 고유한 요소

## 관계 선택자

```css
.menu li { list-style: none; }
.menu > li { display: inline-block; }
.card:hover { transform: translateY(-4px); }
```

`A B`는 모든 후손, `A > B`는 바로 아래 자식만 선택한다.

## 우선순위

대체로 인라인 스타일 > id > class/가상 클래스 > 태그 순으로 강하다. 우선순위 문제를 `!important`로 덮기보다 선택자 구조를 단순하게 유지한다.

## 주의사항

- 클래스 이름은 역할이 드러나게 작성한다.
- 너무 긴 후손 선택자는 HTML 구조 변경에 취약하다.
- 같은 속성을 여러 곳에서 반복 선언하면 최종 적용 위치를 찾기 어렵다.
