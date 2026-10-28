# 09 FastAPI Cookie Session 로그인 — 연습문제

[원본 비교 본문](../../09_FastAPI_Cookie_Session_로그인.md) · [연습문제 목차](README.md)

**새로 구성한 복습 문제**다. 강사님이 낸 시험이나 내 당시 구현 코드가 아니다. 본문의 강사님 코드와 내 코드를 읽고 답을 예상한다. 외부 DB·API를 실제로 호출하지 않아도 풀 수 있다.

## 문제

수업의 `/login`을 방문한 뒤 `/mypage`에 가면 어떤 세션 키를 확인하는가? `/logout` 뒤에는 같은 키가 어떻게 되는가? 이 과정에 비밀번호 검사가 있는지도 적자.

<details>
<summary>정답과 확인할 점</summary>

`/login`은 `request.session['isLogin'] = True`와 `['id'] = 'admin'`을 기록한다. `/mypage`는 `isLogin`을 읽고, 미들웨어도 보호 경로에서 그 키의 유무를 확인한다. `/logout`의 `request.session.clear()` 뒤에는 이 값들이 지워진다. **비밀번호를 검사하는 코드는 없다.** 브라우저의 쿠키와 `request.session`의 사용을 본문 원본에서 구분해 읽자.

입력→처리→결과의 실제 원본 사례는 [본문](../../09_FastAPI_Cookie_Session_로그인.md)에서 확인한다.

</details>

## 추가로 알면 좋은 것

본문에 없는 기능을 추가했다면 실제 수업 구현과 구별해 기록한다. 외부 서비스의 실제 응답이나 미완성 코드를 성공 사례로 가정하지 않는다.
