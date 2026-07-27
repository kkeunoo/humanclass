---
title: JavaScript DOM 선택과 변경
category: JavaScript
last_updated: 2026-07-27
version: v4.1
status: Active
---

# JavaScript DOM 선택과 변경

> [!IMPORTANT]
> **핵심 목표**  
> 이 문서는 수업 범위 안에서 `DOM 선택과 변경`의 개념, 사용 이유, 기본 문법, 예제, 실수 사례와 복습 질문을 한 번에 학습하도록 구성한다.

| 항목 | 내용 |
|---|---|
| 난이도 | ★★★☆☆ |
| 예상 학습 시간 | 35~50분 |
| 이전 학습 | `JS_Async_JSON_AJAX` |
| 다음 학습 | `JS_Date` |
| 문서 버전 | v4.1 · 2026-07-27 |

---

## 이번 문서에서 배우는 것

- `DOM 선택과 변경`이 무엇인지 자신의 말로 설명한다.
- 기본 문법을 읽고 실행 결과를 예상한다.
- 예제에서 입력 → 처리 → 출력의 흐름을 찾는다.
- 자주 발생하는 실수를 보고 원인을 설명한다.
- 수업 문제를 스스로 분석한 뒤 풀이와 비교한다.

## 왜 이 내용을 배우는가?

DOM 선택과 변경은(는) 이후 예제와 문제를 이해하기 위한 기본 도구다. 문법만 외우기보다 어떤 상황에서 필요하고, 코드가 어떤 순서로 동작하는지 이해해야 다른 문제에도 적용할 수 있다.

> [!TIP]
> 문법을 외우기 전에 **무엇을 해결하기 위한 문법인지** 먼저 확인한다. 같은 문법도 목적을 이해하면 다른 예제에서 다시 사용할 수 있다.


<!-- V4.1-QA-START -->
> [!NOTE]
> **💡 WHY — 왜 중요한가?**  
> DOM은 HTML을 JavaScript가 선택하고 변경할 수 있는 객체 구조로 표현한 것이다. DOM을 이해해야 클릭에 따라 문구, 클래스, 목록을 바꾸는 화면을 만들 수 있다.

> [!TIP]
> **⭐ 실무 TIP**  
> 선택 직후 결과가 단일 요소인지 NodeList인지 확인하고, 선택 실패 가능성도 고려한다.

> [!IMPORTANT]
> **📌 반드시 기억하기**  
> `querySelector()`는 첫 요소 하나, `querySelectorAll()`은 여러 요소를 담은 NodeList를 반환한다.

> [!WARNING]
> **⚠️ 주제별 자주 하는 실수**  
> NodeList 자체에 `classList`를 사용하면 오류가 나므로 요소 하나를 선택하거나 반복해야 한다.

> [!NOTE]
> **🏫 수업 메모**  
> 예제 코드를 실행한 뒤 값이나 선택자를 하나씩 바꾸고, 결과가 달라지는 이유를 자신의 말로 설명한다. 정답 코드보다 실행 순서와 오류 원인을 설명할 수 있는지가 더 중요하다.
<!-- V4.1-QA-END -->

## 학습 전 생각해 보기

1. 이 개념이 없으면 코드를 어떤 방식으로 작성해야 할까?
2. 현재 예제에서 입력값과 결과값은 무엇일까?
3. 코드 한 줄을 제거하면 어떤 변화가 생길까?

---

# 개념과 수업 예제

## 선택

```js
const title = document.querySelector('.title');
const items = document.querySelectorAll('.item');
```

`querySelectorAll` 결과는 여러 요소를 담은 NodeList다. NodeList 자체에는 개별 요소의 `classList`가 없다.

```js
items.forEach(item => {
  console.log(item.classList.contains('active'));
});
```

## 내용과 속성 변경

```js
title.textContent = '변경된 제목';
const image = document.querySelector('img');
image.setAttribute('alt', '상품 이미지');
```

## 요소 생성

```js
const li = document.createElement('li');
li.textContent = '새 항목';
document.querySelector('ul').append(li);
```

## 주의사항

- 선택 결과가 없으면 null이므로 사용 전 확인한다.
- 사용자 입력을 넣을 때 `innerHTML`보다 `textContent`가 안전하다.
- 여러 요소를 선택했는지 단일 요소를 선택했는지 구분한다.

---

# 수업 문제와 풀이

> [!IMPORTANT]
> 아래 문제는 별도 문제 폴더에 있던 내용을 이 개념 문서로 통합한 것이다. 먼저 문제를 읽고 직접 풀이한 뒤 해설과 비교한다.

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


---

# 자주 하는 실수

- 예제 코드를 그대로 복사하고 각 줄의 역할을 확인하지 않는 실수
- 입력값과 출력값의 자료형을 확인하지 않는 실수
- 한 번에 많은 코드를 작성해 오류가 발생한 위치를 찾기 어렵게 만드는 실수
- 브라우저 또는 콘솔에서 직접 결과를 확인하지 않는 실수

> [!WARNING]
> 오류가 발생하면 코드를 한꺼번에 바꾸지 않는다. 선택 결과, 변수값, 자료형, 조건식 결과를 `console.log()` 또는 출력문으로 하나씩 확인한다.

# 실무 연결

수업에서 배운 문법은 작은 UI와 데이터 처리의 기본이 된다. 실무 사례를 볼 때도 새로운 기술 이름보다 **현재 코드가 어떤 값을 받고, 어떤 조건으로 처리하고, 무엇을 바꾸는지**에 집중한다.

# 직접 해보기

1. 문서의 첫 번째 예제를 직접 입력해 실행한다.
2. 값 하나를 바꾸고 실행 결과를 예상한 뒤 확인한다.
3. 조건이나 반복 횟수를 변경해 본다.
4. 오류가 발생하도록 일부 코드를 바꾸고 오류 메시지를 읽는다.
5. 예제를 보지 않고 핵심 부분을 다시 작성한다.

# Check Point

- [ ] 이 개념을 한 문장으로 설명할 수 있다.
- [ ] 왜 필요한지 예를 들어 설명할 수 있다.
- [ ] 기본 예제의 실행 순서를 말할 수 있다.
- [ ] 자주 하는 실수 한 가지와 해결 방법을 설명할 수 있다.
- [ ] 예제를 보지 않고 비슷한 코드를 작성할 수 있다.

# 예상 면접 질문

1. DOM 선택과 변경은(는) 무엇인가요?
2. DOM 선택과 변경을(를) 사용하는 이유는 무엇인가요?
3. 이 문서의 기본 예제를 말로 설명해 보세요.
4. 학습 중 가장 자주 발생할 수 있는 실수는 무엇인가요?

# 최종 요약

- `DOM 선택과 변경`의 이름만 외우지 않고 필요한 이유와 동작 순서를 함께 이해한다.
- 작은 예제를 실행하고 값을 바꾸면서 결과를 비교한다.
- 문제를 풀 때 입력 → 처리 → 출력으로 나눈다.
- 오류 메시지와 중간값을 확인하는 습관을 만든다.
- 다음 문서 `JS_Date`로 넘어가기 전에 Check Point를 확인한다.

# 복습 기록

| 복습 시점 | 완료 | 이해도 메모 |
|---|---|---|
| 학습 당일 | [ ] |  |
| 1일 후 | [ ] |  |
| 7일 후 | [ ] |  |
| 30일 후 | [ ] |  |

## 다음 문서를 보기 전에

아래 질문에 답할 수 있다면 다음 문서로 넘어간다.

1. 이 개념은 어떤 문제를 해결하는가?
2. 기본 문법을 직접 작성할 수 있는가?
3. 가장 흔한 실수는 무엇이며 왜 발생하는가?

➡️ **다음 학습:** `JS_Date`
