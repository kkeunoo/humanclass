# 21 JavaScript 외부AI API요청과 대화기록 — 연습문제

[해당 본문](../../21_JavaScript_외부AI_API요청과_대화기록.md) · [장별 문제 목차](README.md)

**새로 구성한 연습문제**다. 먼저 해당 본문에서 강사님·내 코드와 실제 동작을 읽는다.

## 문제

대화 기록 배열에 사용자 문장과 미리 준비한 답변 문자열을 차례로 넣어 콘솔에 출력하자.

**확인 기준:** 질문과 답변을 배열에 넣은 순서대로 읽는다. 미리 준비한 답변을 **실제 AI 응답**으로 표시하지 않는다.

<details>
<summary>해설 — 직접 해 본 뒤 펼치기</summary>

```javascript
const history = [];
history.push({ role: 'user', text: '안녕' });
history.push({ role: 'model', text: '반가워요' });
history.forEach(function(entry) {
  console.log(entry.role + ': ' + entry.text);
});
```

출력 순서는 `user: 안녕` 다음 `model: 반가워요`다. 두 번째 문장은 **미리 정한 문자열**이므로 외부 모델의 답변을 받은 것이 아니다. 강사님·내 원본의 여러 번 질문하기에서도 기록의 순서와 요청에 포함된 내용을 구별해야 한다.

</details>

이 새 문제는 배열·객체·순회로 **기록을 읽는 부분**만 재구성한다. 실제 요청을 보내거나 API 키를 준비하는 단계는 실행 조건에 넣지 않는다.
