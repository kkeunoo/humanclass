---
title: "JavaScript 비동기·JSON·AJAX"
area: "JavaScript"
version: "v4.3"
last_updated: "2026-07-27"
difficulty: "★★★☆☆☆"
estimated_time: "35~55분"
---

# JavaScript 비동기·JSON·AJAX

## 학습 목표

- 동기와 비동기의 차이를 이해하고 JSON 문자열과 객체를 변환한다.
- 예제의 실행 순서를 설명한다.
- 현재까지 배운 문법으로 문제를 해결한다.

## 왜 배우는가

JavaScript는 값과 화면을 연결하고 사용자 행동에 반응하게 만듭니다. 새로운 문법을 짧게 쓰는 것보다 실행 흐름을 정확히 이해하는 것이 우선입니다.

## 기본 개념

```javascript
const jsonText = '{"name":"근욱","age":20}';
const user = JSON.parse(jsonText);

console.log(user.name);

const result = JSON.stringify(user);
console.log(result);
```

## 수업 예제

예제를 직접 입력한 뒤 변수값과 실행 순서를 `console.log()`로 확인합니다.

## 수업 문제

### 문제

JSON 문자열을 객체로 바꾼 뒤 상품명과 가격을 출력하세요.

### 요구사항

- `JSON.parse()`를 사용합니다.
- 변환된 객체의 속성에 접근합니다.
- 네트워크 요청 없이 JSON 변환에 집중합니다.

### 직접 풀어 보기

해설을 열기 전에 입력값, 처리 과정, 출력 결과를 나누어 적고 코드를 작성합니다.

<details>
<summary>해설 보기</summary>

```javascript
const jsonText = '{"product":"키보드","price":45000}';
const product = JSON.parse(jsonText);

console.log(product.product);
console.log(product.price);
```

### 풀이 설명

현재 문서까지 배운 문법을 중심으로 작성했습니다. 먼저 기본 풀이를 이해한 뒤 더 알아보기의 짧은 문법과 비교합니다.

</details>

## 자주 하는 실수

- JSON 키와 문자열에 큰따옴표를 사용하지 않는 경우
- JSON 문자열과 JavaScript 객체를 같은 것으로 생각하는 경우
- 비동기 결과가 오기 전에 값을 사용하려는 경우

## 실무 연결

서버와 데이터를 주고받을 때 JSON 형식이 널리 사용됩니다. 응답 데이터를 객체로 변환한 뒤 화면에 표시합니다.

## 📌 더 알아보기

### Fetch API

Promise와 네트워크 요청을 학습한 뒤 서버 데이터를 요청할 수 있습니다.

```javascript
fetch('/data.json')
    .then(function (response) {
        return response.json();
    })
    .then(function (data) {
        console.log(data);
    })
    .catch(function (error) {
        console.error(error);
    });
```

`async/await`은 Promise 흐름을 이해한 뒤 배우는 다른 작성 방식입니다.

## 직접 해보기

- 예제의 값과 조건을 변경하고 결과를 예상한다.
- 중간 변수값을 출력해 실행 흐름을 확인한다.
- 오류가 발생한 줄과 오류 메시지를 읽고 원인을 기록한다.

## Check Point

- [ ] 동기와 비동기의 차이를 설명할 수 있다.
- [ ] JSON 문자열과 객체를 구분할 수 있다.
- [ ] JSON.parse와 JSON.stringify의 역할을 설명할 수 있다.

## 최종 요약

동기와 비동기의 차이를 이해하고 JSON 문자열과 객체를 변환한다.

## 복습 기록

- [ ] 예제를 직접 입력했다.
- [ ] 기본 풀이를 해설 없이 작성했다.
- [ ] 더 알아보기 문법과 기본 풀이를 비교했다.

## 이전 · 다음 학습

| 구분 | 문서 |
|---|---|
| 이전 학습 | [JavaScript 날짜와 시간](JS_Date.md) |
| 다음 학습 | [JavaScript 외부 API 활용](JS_External_API.md) |
