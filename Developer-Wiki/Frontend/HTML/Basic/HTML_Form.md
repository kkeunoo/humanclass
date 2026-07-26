---
title: HTML Form
category: HTML
last_updated: 2026-07-27
status: Active
---

# HTML Form


## 기본 구조

```html
<form>
  <label for="user-id">아이디</label>
  <input id="user-id" name="userId" type="text">

  <label for="password">비밀번호</label>
  <input id="password" name="password" type="password">

  <button type="submit">로그인</button>
</form>
```

## 주요 입력 요소

```html
<input type="checkbox" name="agree" value="yes">
<input type="radio" name="size" value="large">
<select name="menu">
  <option value="coffee">커피</option>
  <option value="tea">차</option>
</select>
<textarea name="memo"></textarea>
```

## 이름이 중요한 이유

`name`은 선택된 값을 묶어서 처리할 때 기준이 된다. JavaScript에서 `FormData`를 사용하거나 서버로 전달할 때도 이름이 필요하다.

## 실무 연결

로그인, 주문, 배송지 복사, 피자 옵션 선택, Todo 입력과 같은 수업 문제에서 폼 요소의 값과 이벤트를 연결했다.

## 주의사항

- 버튼의 기본 type은 폼 안에서 `submit`일 수 있다. 단순 클릭 버튼이면 `type="button"`을 명시한다.
- 라디오 버튼은 같은 `name`을 사용해야 하나만 선택된다.
- `label for`와 `input id`를 연결한다.
