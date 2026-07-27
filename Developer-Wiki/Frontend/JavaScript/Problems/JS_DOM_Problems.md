---
title: JavaScript DOM 문제 풀이
category: JavaScript Problems
last_updated: 2026-07-27
status: Active
---

# JavaScript DOM 문제 풀이

개인 및 강사 `12_dom_content.html`과 관련 실습을 바탕으로 요소 선택, 생성, 조립, 클래스 확인 과정까지 정리한다.

> [!TIP]
> 문제를 바로 코드로 옮기지 말고 **입력 → 처리 → 출력**을 먼저 한 줄씩 적는다. 그 다음 필요한 변수, 반복 횟수, 조건식을 정하면 코드가 단순해진다.

## DOM 문제 해결 순서

1. 어떤 요소를 선택해야 하는지 CSS 선택자로 먼저 확인한다.
2. 선택 결과가 단일 요소인지 여러 요소인지 구분한다.
3. 읽기, 변경, 생성, 삭제 중 어떤 작업인지 결정한다.
4. 새 요소는 생성 → 내용 설정 → 속성 설정 → 부모에 추가 순서로 조립한다.
5. 요소를 찾지 못한 `null` 상황도 확인한다.

---

## 문제 1. `tbody`에 새로운 행 추가

### 완성 구조를 먼저 그리기

```html
<tr>
  <td>홍길동</td>
  <td>90</td>
</tr>
```

이 구조를 작은 요소부터 만든다.

```js
const tbody = document.querySelector('tbody');

if (tbody) {
  const tr = document.createElement('tr');
  const tdName = document.createElement('td');
  const tdScore = document.createElement('td');

  tdName.textContent = '홍길동';
  tdScore.textContent = '90';

  tr.append(tdName, tdScore);
  tbody.append(tr);
}
```

### 개인 풀이와 강사 풀이 비교

- 개인 풀이는 생성, 내용 설정, 추가 과정을 한 단계씩 변수로 나누어 DOM 구조를 이해하기 좋았다.
- 강사 풀이는 핵심 메서드를 간결하게 연결하여 최종 결과를 빠르게 확인할 수 있었다.
- 초반에는 개인 방식처럼 중간 변수를 유지하고, 익숙해진 후 반복되는 부분만 함수로 줄이는 편이 좋다.

### 반복되는 행을 함수로 만들기

```js
function createRow(name, score) {
  const tr = document.createElement('tr');
  const tdName = document.createElement('td');
  const tdScore = document.createElement('td');

  tdName.textContent = name;
  tdScore.textContent = score;
  tr.append(tdName, tdScore);

  return tr;
}

tbody.append(createRow('홍길동', 90));
tbody.append(createRow('김개발', 85));
```

> [!TIP]
> 함수는 “코드를 짧게 만들기 위해서”만 쓰는 것이 아니다. 같은 구조를 반복 생성할 때 값만 바꿔 재사용하기 위해 사용한다.

---

## 문제 2. 여러 요소의 클래스 포함 여부 확인

### 오류가 발생하는 코드

```js
const quizzes = document.querySelectorAll('div.quiz');
quizzes.classList.contains('q2');
```

`querySelectorAll()`은 요소 하나가 아니라 `NodeList`를 반환한다. 따라서 목록 자체에는 `classList`가 없다.

### 올바른 풀이

```js
const quizzes = document.querySelectorAll('div.quiz');

quizzes.forEach(quiz => {
  const hasQ2 = quiz.classList.contains('q2');
  console.log(hasQ2);
});
```

### 특정 요소 하나만 확인할 때

```js
const q2 = document.querySelector('div.quiz.q2');

if (q2) {
  console.log(q2.classList.contains('q2'));
}
```

> [!IMPORTANT]
> `querySelector()` → 요소 하나 또는 `null`  
> `querySelectorAll()` → 여러 요소를 담은 `NodeList`, 요소가 없어도 빈 목록

---

## 문제 3. 버튼을 눌러 클래스 토글

```js
const button = document.querySelector('.toggle-button');
const panel = document.querySelector('.panel');

button?.addEventListener('click', () => {
  panel?.classList.toggle('is-open');
});
```

```css
.panel {
  display: none;
}

.panel.is-open {
  display: block;
}
```

### 해결 구조

- JavaScript는 상태 클래스만 추가하거나 제거한다.
- 실제 표시 모양은 CSS가 담당한다.
- 스타일을 JavaScript에 여러 줄 직접 작성하는 것보다 역할 분리가 잘 된다.

---

## 문제 4. 목록 항목 삭제

```js
const list = document.querySelector('.todo-list');

list?.addEventListener('click', event => {
  if (!event.target.matches('.delete')) return;

  const item = event.target.closest('li');
  item?.remove();
});
```

### 왜 부모 요소에 이벤트를 연결하는가

나중에 추가된 삭제 버튼에도 같은 이벤트가 동작하도록 이벤트 위임을 사용한다. 현재 수업 범위에서는 `event.target`, `matches`, `closest`의 역할을 문제 안에서 필요한 만큼 이해한다.

## DOM 문제를 더 잘 푸는 방법

- 개발자 도구 콘솔에서 선택 결과를 먼저 출력한다.
- 선택자 오타와 요소 생성 순서를 확인한다.
- `innerHTML`은 빠르지만 사용자 입력을 그대로 넣지 않는다.
- 사용자 문자열은 `textContent`로 넣는 습관을 들인다.
- DOM 조작이 반복되면 생성 함수를 만든다.

## 추가 연습

1. 입력한 이름과 점수를 표에 추가한다.
2. 목록의 홀수 번째 항목에 클래스를 추가한다.
3. 전체 선택 버튼으로 체크박스를 모두 변경한다.
4. 선택된 항목만 삭제한다.
