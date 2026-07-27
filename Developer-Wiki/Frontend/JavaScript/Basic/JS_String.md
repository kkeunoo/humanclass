---
title: "JavaScript 문자열"
area: "JavaScript"
version: "v4.3"
last_updated: "2026-07-27"
difficulty: "★★☆☆☆"
estimated_time: "35~55분"
---

# JavaScript 문자열

## 학습 목표

- 문자열 길이, 인덱스, 주요 메서드를 사용한다.
- 예제의 실행 순서를 설명한다.
- 현재까지 배운 문법으로 문제를 해결한다.

## 왜 배우는가

JavaScript는 값과 화면을 연결하고 사용자 행동에 반응하게 만듭니다. 새로운 문법을 짧게 쓰는 것보다 실행 흐름을 정확히 이해하는 것이 우선입니다.

## 기본 개념

```javascript
const text = '  JavaScript Study  ';
const cleanText = text.trim();

console.log(cleanText.length);
console.log(cleanText.includes('Study'));
```

## 수업 예제

예제를 직접 입력한 뒤 변수값과 실행 순서를 `console.log()`로 확인합니다.

## 수업 문제

### 문제

입력 문자열의 앞뒤 공백을 제거하고 소문자로 바꾼 뒤 길이를 출력하세요.

### 요구사항

- 원본 문자열과 변환 결과를 서로 다른 변수에 저장합니다.
- `trim()`과 `toLowerCase()`를 사용합니다.
- 최종 문자열과 길이를 출력합니다.

### 직접 풀어 보기

해설을 열기 전에 입력값, 처리 과정, 출력 결과를 나누어 적고 코드를 작성합니다.

<details>
<summary>해설 보기</summary>

```javascript
const input = '  Hello JavaScript  ';
const result = input.trim().toLowerCase();

console.log(result);
console.log(result.length);
```

### 풀이 설명

현재 문서까지 배운 문법을 중심으로 작성했습니다. 먼저 기본 풀이를 이해한 뒤 더 알아보기의 짧은 문법과 비교합니다.

</details>

## 자주 하는 실수

- 문자열 메서드가 원본을 직접 변경한다고 생각하는 경우
- 존재하지 않는 인덱스에 접근하는 경우
- 숫자와 문자열을 +로 연결하면서 결과를 잘못 예상하는 경우

## 실무 연결

검색어 정리, 사용자 입력 검증, 파일명과 URL 가공에 문자열 메서드를 사용합니다.

## 📌 더 알아보기

템플릿 리터럴은 백틱과 `${값}`으로 여러 값을 읽기 쉬운 문자열에 넣을 수 있습니다.

## 직접 해보기

- 예제의 값과 조건을 변경하고 결과를 예상한다.
- 중간 변수값을 출력해 실행 흐름을 확인한다.
- 오류가 발생한 줄과 오류 메시지를 읽고 원인을 기록한다.

## Check Point

- [ ] 문자열 인덱스가 0부터 시작함을 설명할 수 있다.
- [ ] trim, includes, replace를 사용할 수 있다.
- [ ] 문자열 변환 결과를 새 변수에 저장할 수 있다.

## 최종 요약

문자열 길이, 인덱스, 주요 메서드를 사용한다.

## 복습 기록

- [ ] 예제를 직접 입력했다.
- [ ] 기본 풀이를 해설 없이 작성했다.
- [ ] 더 알아보기 문법과 기본 풀이를 비교했다.

## 이전 · 다음 학습

| 구분 | 문서 |
|---|---|
| 이전 학습 | [JavaScript 함수와 화살표 함수](JS_Function_Arrow.md) |
| 다음 학습 | [JavaScript 배열](JS_Array.md) |
