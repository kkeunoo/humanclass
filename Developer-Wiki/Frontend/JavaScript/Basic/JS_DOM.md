---
title: "JavaScript DOM 선택과 변경"
area: "JavaScript"
version: "v4.3"
last_updated: "2026-07-27"
difficulty: "★★★☆☆☆"
estimated_time: "35~55분"
---

# JavaScript DOM 선택과 변경

## 학습 목표

- 문서 요소를 선택하고 내용·속성·클래스를 변경한다.
- 예제의 실행 순서를 설명한다.
- 현재까지 배운 문법으로 문제를 해결한다.

## 왜 배우는가

JavaScript는 값과 화면을 연결하고 사용자 행동에 반응하게 만듭니다. 새로운 문법을 짧게 쓰는 것보다 실행 흐름을 정확히 이해하는 것이 우선입니다.

## 기본 개념

```javascript
const title = document.querySelector('#title');
const items = document.querySelectorAll('.item');

title.innerText = '변경된 제목';
title.classList.add('active');

for (let item of items) {
    item.classList.add('visible');
}
```

## 수업 예제

예제를 직접 입력한 뒤 변수값과 실행 순서를 `console.log()`로 확인합니다.

## 수업 문제

### 문제

버튼을 누르면 안내 문장의 내용과 클래스를 변경하세요.

### 요구사항

- `querySelector()`로 버튼과 문장을 각각 선택합니다.
- 일반 함수 형태의 이벤트 핸들러를 사용합니다.
- 문장의 `innerText`와 `classList`를 변경합니다.

### 직접 풀어 보기

해설을 열기 전에 입력값, 처리 과정, 출력 결과를 나누어 적고 코드를 작성합니다.

<details>
<summary>해설 보기</summary>

```javascript
const button = document.querySelector('.change-button');
const message = document.querySelector('.message');

button.addEventListener('click', function () {
    message.innerText = '내용이 변경되었습니다.';
    message.classList.add('active');
});
```

### 풀이 설명

현재 문서까지 배운 문법을 중심으로 작성했습니다. 먼저 기본 풀이를 이해한 뒤 더 알아보기의 짧은 문법과 비교합니다.

</details>

## 자주 하는 실수

- querySelectorAll 결과에 바로 classList를 사용하는 경우
- 선택자와 HTML의 id/class 이름이 다른 경우
- 요소가 존재하기 전에 스크립트를 실행하는 경우

## 실무 연결

탭, 모달, 메뉴, 알림 문구처럼 화면 상태가 바뀌는 기능은 DOM 선택과 변경을 기반으로 만듭니다.

## 📌 더 알아보기

### closest()

현재 요소부터 부모 방향으로 올라가며 가장 가까운 일치 요소를 찾습니다. 기본 과정에서는 `parentNode`와 구조를 먼저 이해한 뒤 사용합니다.

```javascript
const item = event.target.closest('li');
```

### Optional Chaining

`element?.classList`는 요소가 없을 때 접근을 중단합니다. 선택자가 틀린 문제를 숨길 수 있으므로 초반에는 요소 존재 여부를 직접 확인합니다.

## 직접 해보기

- 예제의 값과 조건을 변경하고 결과를 예상한다.
- 중간 변수값을 출력해 실행 흐름을 확인한다.
- 오류가 발생한 줄과 오류 메시지를 읽고 원인을 기록한다.

## Check Point

- [ ] querySelector와 querySelectorAll의 차이를 설명할 수 있다.
- [ ] NodeList를 반복문으로 처리할 수 있다.
- [ ] innerText와 classList를 사용할 수 있다.

## 최종 요약

문서 요소를 선택하고 내용·속성·클래스를 변경한다.

## 복습 기록

- [ ] 예제를 직접 입력했다.
- [ ] 기본 풀이를 해설 없이 작성했다.
- [ ] 더 알아보기 문법과 기본 풀이를 비교했다.

## 이전 · 다음 학습

| 구분 | 문서 |
|---|---|
| 이전 학습 | [JavaScript 배열](JS_Array.md) |
| 다음 학습 | [JavaScript 이벤트와 Form](JS_Event_Form.md) |
