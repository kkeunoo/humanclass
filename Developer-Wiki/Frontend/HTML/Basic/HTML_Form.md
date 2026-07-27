---
title: "HTML Form"
area: "HTML"
version: "v4.3"
last_updated: "2026-07-27"
difficulty: "★★★☆☆"
estimated_time: "40~60분"
---

# HTML Form

## 학습 목표

- `form`, `label`, `input`의 역할을 설명할 수 있다.
- 입력 목적에 맞는 `type`을 선택할 수 있다.
- `label`과 입력 요소를 연결할 수 있다.
- `name`, `value`, `required`의 기본 역할을 설명할 수 있다.

## 왜 배우는가

폼은 회원가입, 로그인, 검색, 문의처럼 사용자에게 값을 입력받는 모든 기능의 시작점입니다. 입력 목적과 구조를 올바르게 작성해야 사용성과 접근성이 좋아집니다.

## 기본 개념

### 기본 구조

```html
<form>
    <label for="user-name">이름</label>
    <input id="user-name" name="userName" type="text" required>

    <button type="submit">전송</button>
</form>
```

- `label`: 입력 항목의 이름을 제공합니다.
- `for`와 `id`: 레이블과 입력 요소를 연결합니다.
- `name`: 제출할 값의 이름을 정합니다.
- `required`: 필수 입력으로 지정합니다.
- `button type="submit"`: 폼 제출을 요청합니다.

## 수업 예제

```html
<form>
    <div>
        <label for="email">이메일</label>
        <input id="email" name="email" type="email" placeholder="name@example.com" required>
    </div>

    <div>
        <label for="password">비밀번호</label>
        <input id="password" name="password" type="password" required>
    </div>

    <button type="submit">로그인</button>
</form>
```

## 수업 문제

### 문제

이름, 이메일, 비밀번호를 입력받는 회원가입 폼을 작성하세요.

### 요구사항

- 모든 입력 요소에 연결된 `label`을 작성합니다.
- 이메일과 비밀번호에 알맞은 `type`을 사용합니다.
- 모든 입력 요소에 `name`을 지정합니다.
- 세 항목은 모두 필수 입력으로 지정합니다.
- 버튼은 제출 버튼으로 작성합니다.

### 직접 풀어 보기

해설을 열기 전에 빈 HTML 파일에 직접 작성하고 브라우저에서 결과를 확인합니다.

<details>
<summary>해설 보기</summary>

```html
<form>
    <div>
        <label for="name">이름</label>
        <input id="name" name="name" type="text" required>
    </div>

    <div>
        <label for="email">이메일</label>
        <input id="email" name="email" type="email" required>
    </div>

    <div>
        <label for="password">비밀번호</label>
        <input id="password" name="password" type="password" required>
    </div>

    <button type="submit">가입하기</button>
</form>
```

### 풀이 설명

각 `label`의 `for` 값과 입력 요소의 `id`를 같게 작성했습니다. `name`은 각 입력값을 구분하고, `required`는 비어 있는 상태의 제출을 제한합니다.

</details>

## 자주 하는 실수

- `label` 없이 placeholder만 사용하는 경우
- 서로 다른 입력 요소에 같은 `id`를 사용하는 경우
- 일반 버튼인데 `type`을 생략해 의도치 않게 제출되는 경우

## 실무 연결

회원가입, 로그인, 검색, 주문, 문의하기 화면은 모두 폼 요소로 구성됩니다. 입력 항목 이름과 타입을 명확히 작성하는 것이 기본입니다.

## 📌 더 알아보기

### 다양한 입력 요소

`select`, `textarea`, `radio`, `checkbox`를 사용하면 선택형 또는 긴 문장 입력을 만들 수 있습니다.

### FormData

JavaScript를 학습한 뒤에는 `FormData`로 폼의 `name`과 값을 읽을 수 있습니다. 현재 단계에서는 `name`이 제출 데이터의 이름이 된다는 점만 이해합니다.

```javascript
const formData = new FormData(form);
```

## 직접 해보기

- 이름 입력란에 `placeholder`를 추가한다.
- 전화번호 입력란을 하나 추가한다.
- 가입 버튼의 문구를 변경한다.

## Check Point

- [ ] `form`, `label`, `input`의 역할을 설명할 수 있다.
- [ ] `label`의 `for`와 입력 요소의 `id`를 연결할 수 있다.
- [ ] 입력 목적에 맞는 `type`을 선택할 수 있다.
- [ ] `name` 속성이 필요한 이유를 설명할 수 있다.

## 최종 요약

폼은 사용자 입력을 묶는 구조입니다. 레이블과 입력 요소를 연결하고, 입력 목적에 맞는 타입과 `name`을 지정해야 합니다.

## 복습 기록

- [ ] 예제를 직접 입력했다.
- [ ] 수업 문제를 해설 없이 풀었다.
- [ ] 틀린 부분을 수정하고 이유를 기록했다.

## 이전 · 다음 학습

| 구분 | 문서 |
|---|---|
| 이전 학습 | [HTML 목록과 표](HTML_List_Table.md) |
| 다음 학습 | [CSS README](../../CSS/README.md) |
