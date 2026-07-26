---
title: JavaScript DOM 내용·속성·스타일
version: v1.0
last_updated: 2026-07-25
status: Completed
---

# JavaScript DOM 내용·속성·스타일

## 개념

선택한 요소의 텍스트, HTML, 속성, 인라인 스타일과 class를 변경할 수 있다.

## 문법

```javascript
title.textContent = "변경";
image.setAttribute("src", "photo.png");
box.style.display = "none";
box.classList.add("active");
```

## 예제

```javascript
button.classList.toggle("on");
console.log(button.classList.contains("on"));
```

## 실무 예제

아코디언, 탭, 모달, 토글 버튼처럼 class를 바꿔 화면 상태를 제어한다.

## 주의사항

여러 요소가 담긴 NodeList에는 반복문으로 각각 접근한다. 디자인 변경은 style 직접 조작보다 class 변경을 우선한다.

## 면접 포인트

textContent와 innerHTML, classList 주요 메서드의 차이를 설명한다.

## 요약

내용·속성·스타일 변경은 선택한 단일 요소에 수행한다.
