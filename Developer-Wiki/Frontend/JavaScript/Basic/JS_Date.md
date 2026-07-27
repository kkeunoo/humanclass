---
title: "JavaScript 날짜와 시간"
area: "JavaScript"
version: "v4.3"
last_updated: "2026-07-27"
difficulty: "★★★☆☆☆"
estimated_time: "35~55분"
---

# JavaScript 날짜와 시간

## 학습 목표

- Date 객체로 현재 날짜의 연도·월·일을 읽는다.
- 예제의 실행 순서를 설명한다.
- 현재까지 배운 문법으로 문제를 해결한다.

## 왜 배우는가

JavaScript는 값과 화면을 연결하고 사용자 행동에 반응하게 만듭니다. 새로운 문법을 짧게 쓰는 것보다 실행 흐름을 정확히 이해하는 것이 우선입니다.

## 기본 개념

```javascript
const today = new Date();

console.log(today.getFullYear());
console.log(today.getMonth() + 1);
console.log(today.getDate());
```

## 수업 예제

예제를 직접 입력한 뒤 변수값과 실행 순서를 `console.log()`로 확인합니다.

## 수업 문제

### 문제

현재 날짜를 `2026년 7월 27일` 형식으로 출력하세요.

### 요구사항

- Date 객체를 생성합니다.
- 월 값에는 1을 더합니다.
- 템플릿 리터럴 또는 문자열 연결을 사용합니다.

### 직접 풀어 보기

해설을 열기 전에 입력값, 처리 과정, 출력 결과를 나누어 적고 코드를 작성합니다.

<details>
<summary>해설 보기</summary>

```javascript
const today = new Date();
const year = today.getFullYear();
const month = today.getMonth() + 1;
const date = today.getDate();

console.log(`${year}년 ${month}월 ${date}일`);
```

### 풀이 설명

현재 문서까지 배운 문법을 중심으로 작성했습니다. 먼저 기본 풀이를 이해한 뒤 더 알아보기의 짧은 문법과 비교합니다.

</details>

## 자주 하는 실수

- getMonth 결과가 0부터 시작하는 점을 잊는 경우
- 날짜 객체와 화면 표시 문자열을 혼동하는 경우
- 현재 시각에 의존하는 테스트를 고정값 없이 작성하는 경우

## 실무 연결

달력, 예약, 게시일, 남은 기간 계산 같은 기능에 사용합니다.

## 📌 더 알아보기

날짜 형식과 시간대 처리는 프로젝트 요구사항에 따라 복잡해질 수 있습니다. 국제화 API와 날짜 라이브러리는 기초 Date 사용 이후에 학습합니다.

## 직접 해보기

- 예제의 값과 조건을 변경하고 결과를 예상한다.
- 중간 변수값을 출력해 실행 흐름을 확인한다.
- 오류가 발생한 줄과 오류 메시지를 읽고 원인을 기록한다.

## Check Point

- [ ] Date 객체를 생성할 수 있다.
- [ ] 연도·월·일을 읽는 메서드를 사용할 수 있다.
- [ ] 월 값에 1을 더하는 이유를 설명할 수 있다.

## 최종 요약

Date 객체로 현재 날짜의 연도·월·일을 읽는다.

## 복습 기록

- [ ] 예제를 직접 입력했다.
- [ ] 기본 풀이를 해설 없이 작성했다.
- [ ] 더 알아보기 문법과 기본 풀이를 비교했다.

## 이전 · 다음 학습

| 구분 | 문서 |
|---|---|
| 이전 학습 | [JavaScript 이벤트와 Form](JS_Event_Form.md) |
| 다음 학습 | [JavaScript 비동기·JSON·AJAX](JS_Async_JSON_AJAX.md) |
