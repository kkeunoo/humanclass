---
title: JavaScript 이벤트와 폼
version: v1.0
last_updated: 2026-07-25
status: Completed
---

# JavaScript 이벤트와 폼

## 개념

이벤트는 클릭, 입력, 제출 같은 사용자 동작이며 이벤트 객체는 발생 정보와 대상 요소를 제공한다.

## 문법

```javascript
button.addEventListener("click", function (event) {
    console.log(event.target);
});

form.addEventListener("submit", function (event) {
    event.preventDefault();
});
```

## 예제

```javascript
input.addEventListener("input", function () {
    result.textContent = input.value;
});
```

## 실무 예제

로그인 검증, 클릭 메뉴, 마우스 반응, 입력 미리보기 같은 동작을 구현한다.

## 주의사항

submit 버튼은 기본 전송 동작이 있다. 필요할 때만 preventDefault를 사용한다. 이벤트 이름 앞에 on을 붙이지 않는다.

## 면접 포인트

event.target과 currentTarget, preventDefault의 역할을 설명한다.

## 요약

이벤트는 사용자 동작과 실행할 함수를 연결한다.
