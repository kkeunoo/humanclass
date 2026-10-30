# 21. 외부 AI 요청 — 요청 본문·응답 글·대화 배열의 연결 — 연습문제

[본문](../../21_JavaScript_외부AI_API요청과_대화기록.md) · [문제 목차](README.md)

실제 수업 기능을 바탕으로 **새로 구성한 연습문제**다. 강사님 원본 퀴즈와 구분한다. 예상 → 이유 → 수정 순서로 풀고, 정답은 먼저 답한 뒤 펼친다.

## 목표와 실행 조건

POST의 headers·body와 JSON 문자열을 설명한다. 중첩 응답에서 답변을 읽고 배열에 기록하는 흐름, 부모 내용 재대입이 자식에 미치는 결과, 새로고침과 메모리 기록의 관계를 추적한다.

[전체 실행 HTML](../책형_복습/21_JavaScript_외부AI_API요청과_대화기록.html)과 같은 폴더의 JS를 함께 준비한다. Console을 열고 새로고침하면 처음부터 실행한다. 원본과 별도 파일이므로 기존 변수·타이머·출력 변경 실험의 영향을 섞지 않는다. 실제 입력·현재 시각·난수는 고정 결과와 구별한다.

입력·버튼·키보드·스크롤 예제는 [본문의 3절](../../21_JavaScript_외부AI_API요청과_대화기록.md#example)에 적힌 조작 순서대로 결과를 예상한다. 통신 예제는 해당 절의 가상 JSON 파일과 로컬 웹 실행 준비가 필요하며 HTML을 직접 여는 조건과 다르다. Console 출력이 없는 문제는 화면의 값·개수·선택 상태를 답한다.

## 문제 1. 실행 순서와 결과 예상

다음은 **새 설명 예제**다. 출력 전에 어떤 값이 어떤 순서로 만들어지는지 적는다.

**필요한 HTML · 스크립트 앞:**

```html
    <label>질문 <input id="prompt"></label>
    <button id="add" type="button">가상 답변으로 기록 연습</button>
    <div id="result"></div>
```

```javascript
const list = { contents: [] };
function appendLine(role, text) {
    const line = document.createElement('p');
    line.textContent = role + ': ' + text;
    document.getElementById('result').append(line);
}
document.getElementById('add').addEventListener('click', function () {
    const prompt = document.getElementById('prompt').value;
    list.contents.push({ role: 'user', parts: [{ text: prompt }] });
    const body = JSON.stringify(list);
    console.log('요청 직전 항목', list.contents.length);
    console.log(typeof body);
    // 실제 AI 응답이 아닌, 구조 풀이용 가상 응답
    const result = { candidates: [{ content: { parts: [{ text: '연습 답변' }] } }] };
    const answer = result.candidates[0].content.parts[0].text;
    list.contents.push({ role: 'model', parts: [{ text: answer }] });
    appendLine('user', prompt);
    appendLine('model', answer);
    console.log('답변 기록 뒤 항목', list.contents.length);
});
```

<details>
<summary>힌트와 풀이</summary>

**힌트:** 입력·현재 상태·실행 시점·반환값을 따로 표시한다.

```text
요청 직전 항목 1
string
답변 기록 뒤 항목 2
요청 직전 항목 3
string
답변 기록 뒤 항목 4
```

안녕을 넣고 누른 뒤 다음 질문으로 바꿔 다시 누른다. 첫 질문을 넣으면 요청 본문을 만드는 순간 항목 수는 1, 가상 모델 답변을 기록하면 2다. 다음 클릭은 기존 두 항목 뒤에 사용자 글을 추가하여 3개를 본문으로 만들고 답변 뒤에는 4개다. appendLine의 정의는 role·text를 받아 p를 만들고 글자로 넣어 결과 영역 끝에 붙인다. 이 예제는 네트워크 요청이 전혀 없으며 가상 응답 구조를 읽는 연습이다. 실제 API 성공·AI 생성·대화 기억 기능으로 소개하지 않는다.

</details>

## 문제 2. 개념을 자신의 말로 설명

1. list와 list.contents 중 배열은 어느 쪽인가?
2. 둘째 질문 직후 본문에는 항목 몇 개가 있는가?
3. 응답 전체 문자열과 답변 문자열은 같은가?
4. 화면에 append한 뒤 부모 내용을 대입하면 자식은 유지되는가?

<details>
<summary>풀이</summary>

contents가 배열이다. 가상 예제에서는 3개다. 응답 전체는 메타 구조까지 담아 답변만과 다르다. 부모 내용을 교체하면 기존 자식은 유지되지 않는다.

| 순간 | contents 개수 | 담긴 것 |
| --- | --- | --- |
| 처음 | 0 | 빈 배열 |
| 첫 질문 직후 | 1 | user |
| 첫 답변 기록 뒤 | 2 | user, model |
| 둘째 질문 직후 | 3 | 이전 두 항목, 새 user |
| 둘째 답변 뒤 | 4 | 이전 세 항목, 새 model |
| 새로고침 | 0 | 초기화 |

원본의 모델명 문자열은 당시 파일의 값으로 보존한다. 현재 지원 모델이나 키를 확인한 실행 예제로 간주하지 않는다. 실제 응답에는 후보나 해당 경로가 없을 수도 있으므로 경로가 항상 존재한다고 외우지 않는다. 이번 자동 검수는 가상 값과 DOM 기록만 확인했다.

</details>

## 문제 3. 한 가지를 바꾸어 확인

먼저 **list를 클릭 함수 안으로 이동**를 바꾸면 무엇이 달라질지 적는다. 그다음 실행 파일에 해당 변경만 적용해 실제 결과와 비교한다. 나머지 실험도 원래 예제로 돌아가 하나씩 수행한다.

<details>
<summary>변경 결과와 막힐 때 확인</summary>

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| list를 클릭 함수 안으로 이동 | 클릭마다 이전 기록 사라짐 | 매번 새 객체 생성 |
| answer 대신 JSON.stringify(result) 기록 | 응답 구조 전체가 text에 들어감 | 답변 글과 응답 객체 차이 |
| appendLine 대신 부모 textContent 대입 | 이전 자식 기록이 사라짐 | 부모 내용 교체 |
| 새로고침 | 기록 초기화 | 별도 저장 없음 |

기록이 한 줄만 남으면 부모 전체 내용을 다시 대입하는지 본다. 다음 요청 항목이 이상하면 model의 text에 무엇을 넣었는지 확인한다. undefined 경로 오류는 실제 응답 구조를 먼저 확인한다. catch가 있다고 모든 HTTP 오류를 자동 실패로 판단하는 것은 아니므로 성공 상태 확인은 별도 확장으로 둔다.

</details>

## 채점과 복습

| 점검 | 확인할 것 |
| --- | --- |
| 예측 | 실행 전에 출력·상태를 적었는가? |
| 근거 | 문법·조건·반환·순서로 설명했는가? |
| 수정 | 한 조건만 바꾸었는가? |
| 확인 | 실제 관찰과 코드 기준 예상을 구분했는가? |

틀린 이유를 설명할 수 없다면 [본문](../../21_JavaScript_외부AI_API요청과_대화기록.md)의 작은 예제·내 원본 풀이로 돌아간다. TIP의 미학습 기능은 이 문제의 필수 정답이 아니다.
