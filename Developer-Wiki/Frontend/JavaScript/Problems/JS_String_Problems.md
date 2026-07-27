---
title: JavaScript 문자열 문제 풀이
category: JavaScript Problems
last_updated: 2026-07-27
status: Active
---

# JavaScript 문자열 문제 풀이

개인 및 강사 `10_string.html` 문제를 바탕으로 문자열의 위치를 찾고, 나누고, 가리는 과정을 단계별로 정리한다.

> [!TIP]
> 문제를 바로 코드로 옮기지 말고 **입력 → 처리 → 출력**을 먼저 한 줄씩 적는다. 그 다음 필요한 변수, 반복 횟수, 조건식을 정하면 코드가 단순해진다.

## 문자열 문제를 풀 때 확인할 것

- 구분자가 있는가? 예: `@`, `-`, 공백, `:`
- 필요한 부분의 시작 위치와 끝 위치는 어디인가?
- 문자열 길이가 예상보다 짧아도 동작해야 하는가?
- 원본 문자열은 바뀌지 않는다는 점을 알고 있는가?

---

## 문제 1. 이메일에서 아이디 추출

```js
const email = 'student@example.com';
const atIndex = email.indexOf('@');

if (atIndex === -1) {
  console.log('올바른 이메일 형식이 아닙니다.');
} else {
  const id = email.slice(0, atIndex);
  console.log(id);
}
```

### 접근 방법

1. `@`의 위치를 찾는다.
2. `@`가 없다면 잘못된 형식으로 처리한다.
3. 문자열 시작부터 `@` 직전까지 자른다.

### 더 간단한 풀이

```js
const [id] = email.split('@');
```

단, 이메일 형식 검증 없이 사용하면 `@`가 없는 문자열도 그대로 `id`가 된다.

---

## 문제 2. 날짜 문자열에서 월과 분 추출

```js
const value = '2026-07-14 12:43:19';
const [date, time] = value.split(' ');
const [, month] = date.split('-');
const [, minute] = time.split(':');

console.log('월:', month);
console.log('분:', minute);
```

### 풀이 전략

큰 구분자부터 작은 구분자 순서로 나눈다.

```text
전체 문자열
→ 공백 기준으로 날짜와 시간 분리
→ 날짜를 - 기준으로 분리
→ 시간을 : 기준으로 분리
```

> [!TIP]
> 한 번에 복잡한 인덱스를 계산하기보다 구조가 보이도록 단계별 변수에 나누면 디버깅하기 쉽다.

---

## 문제 3. 이메일 아이디 마스킹

### 요구사항 예시

앞의 두 글자만 보이고 나머지는 `*`로 가린다.

```js
const email = 'developer@example.com';
const [id, domain] = email.split('@');

if (!domain) {
  console.log('올바른 이메일 형식이 아닙니다.');
} else {
  const visibleLength = Math.min(2, id.length);
  const visible = id.slice(0, visibleLength);
  const hidden = '*'.repeat(id.length - visibleLength);
  const maskedEmail = `${visible}${hidden}@${domain}`;

  console.log(maskedEmail);
}
```

### 개인 풀이와 강사 풀이 비교

- 강사 풀이는 `slice`, `indexOf`, `split`의 핵심 사용법을 명확하게 보여줬다.
- 개인 풀이는 별표 개수와 최종 출력 모양까지 더 세밀하게 다뤘다.
- 개선 풀이에서는 아이디 길이가 1~2자인 경우 `repeat()`에 음수가 전달되지 않도록 처리했다.

> [!WARNING]
> `'*'.repeat(id.length - 2)`에서 아이디 길이가 1이면 음수가 되어 오류가 발생한다. `Math.max(0, ...)` 또는 `Math.min()`으로 범위를 제한한다.

---

## 문제 4. 파일 확장자 추출

```js
const fileName = 'profile.photo.png';
const dotIndex = fileName.lastIndexOf('.');

const extension = dotIndex === -1
  ? ''
  : fileName.slice(dotIndex + 1);

console.log(extension);
```

`indexOf('.')`를 사용하면 첫 번째 점을 찾으므로 여러 점이 있는 파일명에서 틀릴 수 있다. 마지막 점을 찾기 위해 `lastIndexOf()`를 사용한다.

---

## 문제 5. 입력값의 앞뒤 공백 제거

```js
const rawName = '   홍길동   ';
const name = rawName.trim();

if (name === '') {
  console.log('이름을 입력하세요.');
} else {
  console.log(name);
}
```

폼 입력값 검증에서는 사용자가 실수로 넣은 앞뒤 공백을 제거한 뒤 빈 문자열인지 확인한다.

## 더 좋은 문자열 풀이 습관

- 구분자가 없을 때 반환되는 값을 확인한다. `indexOf()`는 `-1`을 반환한다.
- `slice()`의 끝 인덱스는 포함되지 않는다.
- 문자열 메서드는 대부분 원본을 바꾸지 않고 새 문자열을 반환한다.
- 개인정보 마스킹은 화면 표시용일 뿐 실제 데이터 보호 방법은 아니다.

## 추가 연습

1. 휴대전화 번호 중간 네 자리를 `****`로 가린다.
2. 이름의 첫 글자만 남기고 나머지를 가린다.
3. URL에서 파일명만 추출한다.
4. 문장에서 특정 단어가 몇 번 등장하는지 센다.
