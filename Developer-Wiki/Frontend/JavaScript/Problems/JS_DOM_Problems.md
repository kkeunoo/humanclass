---
title: JavaScript DOM 문제 풀이
category: JavaScript Problems
last_updated: 2026-07-27
status: Active
---

# JavaScript DOM 문제 풀이


## 문제: tbody에 행 추가

```js
const tbody = document.querySelector('tbody');
const tr = document.createElement('tr');
const tdName = document.createElement('td');
tdName.textContent = '홍길동';
tr.append(tdName);
tbody.append(tr);
```

### 개인 풀이 특징

개인 코드에는 “한 단계씩 조립한다”는 주석과 함께 요소 생성, 내용 설정, 부모에 추가하는 과정을 세분화했다. DOM 학습에서 매우 좋은 접근이다.

### 강사 풀이 특징

강사 코드는 필요한 DOM 메서드를 간결하게 연결하여 최종 구조를 빠르게 보여준다.

### 비교 코멘트

초기 학습에서는 개인 방식처럼 중간 변수를 두어 각 노드가 무엇인지 확인하는 것이 좋다. 익숙해진 뒤에만 코드를 줄인다.

## 문제: 여러 요소의 클래스 확인

```js
const quizzes = document.querySelectorAll('div.quiz');
quizzes.forEach(quiz => {
  console.log(quiz.classList.contains('q2'));
});
```

`querySelectorAll`의 결과에 바로 `classList`를 사용하면 오류가 난다. 각 요소를 순회해야 한다.
