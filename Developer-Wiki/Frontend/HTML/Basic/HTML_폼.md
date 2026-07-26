---
title: HTML 폼
version: v1.0
last_updated: 2026-07-25
status: Completed
---

# HTML 폼

## 개념

폼은 사용자가 입력한 값을 묶어 전달하는 구조다.

## 문법

```html
<form>
    <label for="userId">아이디</label>
    <input id="userId" name="userId" type="text">
    <button type="submit">전송</button>
</form>
```

## 예제

```html
<input type="radio" name="agree" value="yes"> 동의
<select name="area">
    <option value="seoul">서울</option>
</select>
```

## 실무 예제

로그인, 회원가입, 검색 화면처럼 입력 항목과 버튼을 의미 있게 연결한다.

## 주의사항

`label`의 `for`와 입력 요소의 `id`를 연결한다. 전송할 값에는 `name`이 필요하다. 버튼의 기본 동작을 확인한다.

## 면접 포인트

`id`, `name`, `value`의 차이를 설명한다.

## 요약

폼은 입력 요소, 라벨, 선택 요소, 버튼을 목적에 맞게 조합한다.
