---
title: "JavaScript 이벤트와 Form"
area: "JavaScript"
version: "v4.3"
last_updated: "2026-07-27"
difficulty: "★★★☆☆☆"
estimated_time: "35~55분"
---

# JavaScript 이벤트와 Form

## 학습 목표

- 이벤트 객체와 폼 입력값을 읽고 기본 동작을 제어한다.
- 예제의 실행 순서를 설명한다.
- 현재까지 배운 문법으로 문제를 해결한다.

## 왜 배우는가

JavaScript는 값과 화면을 연결하고 사용자 행동에 반응하게 만듭니다. 새로운 문법을 짧게 쓰는 것보다 실행 흐름을 정확히 이해하는 것이 우선입니다.

## 기본 개념

```javascript
const form = document.querySelector('#login-form');

form.addEventListener('submit', function (event) {
    event.preventDefault();

    const userId = document.querySelector('#user-id');
    console.log(userId.value);
});
```

## 수업 예제

예제를 직접 입력한 뒤 변수값과 실행 순서를 `console.log()`로 확인합니다.

## 수업 문제

### 문제

로그인 폼을 제출할 때 아이디 또는 비밀번호가 비어 있으면 안내 문구를 표시하세요.

### 요구사항

- submit 이벤트를 사용합니다.
- `preventDefault()`로 기본 제출을 막습니다.
- `value.trim()`으로 빈 값을 확인합니다.
- 현재 배운 if문과 DOM 문법만 사용합니다.

### 직접 풀어 보기

해설을 열기 전에 입력값, 처리 과정, 출력 결과를 나누어 적고 코드를 작성합니다.

<details>
<summary>해설 보기</summary>

```javascript
const form = document.querySelector('#login-form');
const userId = document.querySelector('#user-id');
const password = document.querySelector('#password');
const message = document.querySelector('.message');

form.addEventListener('submit', function (event) {
    event.preventDefault();

    if (userId.value.trim() === '') {
        message.innerText = '아이디를 입력하세요.';
    } else if (password.value.trim() === '') {
        message.innerText = '비밀번호를 입력하세요.';
    } else {
        message.innerText = '입력이 완료되었습니다.';
    }
});
```

### 풀이 설명

현재 문서까지 배운 문법을 중심으로 작성했습니다. 먼저 기본 풀이를 이해한 뒤 더 알아보기의 짧은 문법과 비교합니다.

</details>

## 자주 하는 실수

- click 이벤트만 사용해 Enter 제출을 처리하지 못하는 경우
- value와 innerText를 혼동하는 경우
- preventDefault를 호출하지 않아 페이지가 새로고침되는 경우

## 실무 연결

로그인, 회원가입, 주문, 검색 폼의 입력 검증과 제출 처리에 사용합니다.

## 📌 더 알아보기

### data-*와 dataset

기본 과정에서는 속성을 다음처럼 읽습니다.

```javascript
button.getAttribute('data-id');
```

이후에는 `dataset`으로 짧게 접근할 수 있습니다.

```javascript
button.dataset.id;
```

### closest()와 이벤트 위임

동적으로 추가된 여러 버튼을 한 부모에서 처리할 때 유용하지만, 먼저 각 요소에 직접 이벤트를 등록하는 흐름을 이해합니다.

## 직접 해보기

- 예제의 값과 조건을 변경하고 결과를 예상한다.
- 중간 변수값을 출력해 실행 흐름을 확인한다.
- 오류가 발생한 줄과 오류 메시지를 읽고 원인을 기록한다.

## Check Point

- [ ] addEventListener로 이벤트를 등록할 수 있다.
- [ ] event.target과 현재 선택한 요소를 구분할 수 있다.
- [ ] input의 value와 checkbox의 checked를 읽을 수 있다.
- [ ] submit 이벤트의 기본 동작을 막을 수 있다.

## 최종 요약

이벤트 객체와 폼 입력값을 읽고 기본 동작을 제어한다.

## 복습 기록

- [ ] 예제를 직접 입력했다.
- [ ] 기본 풀이를 해설 없이 작성했다.
- [ ] 더 알아보기 문법과 기본 풀이를 비교했다.

## 이전 · 다음 학습

| 구분 | 문서 |
|---|---|
| 이전 학습 | [JavaScript DOM 선택과 변경](JS_DOM.md) |
| 다음 학습 | [JavaScript 날짜와 시간](JS_Date.md) |
