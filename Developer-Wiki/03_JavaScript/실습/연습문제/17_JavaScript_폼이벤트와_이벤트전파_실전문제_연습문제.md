# 17. 폼 이벤트 — 입력을 관찰하고 제출을 판단하는 시점 — 연습문제

[본문](../../17_JavaScript_폼이벤트와_이벤트전파_실전문제.md) · [문제 목차](README.md)

실제 수업 기능을 바탕으로 **새로 구성한 연습문제**다. 강사님 원본 퀴즈와 구분한다. 예상 → 이유 → 수정 순서로 풀고, 정답은 먼저 답한 뒤 펼친다.

## 목표와 실행 조건

focus·blur·input·submit을 구분하고 trim한 검사값과 원래 value의 차이를 설명한다. 직접 제출 메서드와 submit 이벤트의 관계, 무작위 색의 범위, 입력 로그의 표시 방법을 읽는다.

[전체 실행 HTML](../책형_복습/17_JavaScript_폼이벤트와_이벤트전파_실전문제.html)과 같은 폴더의 JS를 함께 준비한다. Console을 열고 새로고침하면 처음부터 실행한다. 원본과 별도 파일이므로 기존 변수·타이머·출력 변경 실험의 영향을 섞지 않는다. 실제 입력·현재 시각·난수는 고정 결과와 구별한다.

입력·버튼·키보드·스크롤 예제는 [본문의 3절](../../17_JavaScript_폼이벤트와_이벤트전파_실전문제.md#example)에 적힌 조작 순서대로 결과를 예상한다. 통신 예제는 해당 절의 가상 JSON 파일과 로컬 웹 실행 준비가 필요하며 HTML을 직접 여는 조건과 다르다. Console 출력이 없는 문제는 화면의 값·개수·선택 상태를 답한다.

## 문제 1. 실행 순서와 결과 예상

다음은 **새 설명 예제**다. 출력 전에 어떤 값이 어떤 순서로 만들어지는지 적는다.

**필요한 HTML · 스크립트 앞:**

```html
    <form id="form">
        <label for="query">검색어 연습</label><input id="query" name="query">
        <button type="submit">검사</button>
    </form>
    <p id="message"></p>
```

```javascript
const form = document.getElementById('form');
const query = document.getElementById('query');
const message = document.getElementById('message');
query.addEventListener('focus', function () {
    query.style.backgroundColor = 'yellow';
});
query.addEventListener('blur', function () {
    query.style.backgroundColor = '';
});
query.addEventListener('input', function () {
    console.log('입력', query.value);
});
form.addEventListener('submit', function (event) {
    event.preventDefault();
    const checked = query.value.trim();
    if (checked.length < 2) {
        message.textContent = '두 글자 이상 입력';
    } else {
        message.textContent = '검사 통과, 원래 값: [' + query.value + ']';
    }
    console.log(message.textContent);
});
```

<details>
<summary>힌트와 풀이</summary>

**힌트:** 입력·현재 상태·실행 시점·반환값을 따로 표시한다.

```text
입력 가
두 글자 이상 입력
입력   가나  
검사 통과, 원래 값: [  가나  ]
```

가를 입력하고 검사 버튼을 누른 뒤, 앞뒤 공백 두 칸씩 있는 가나로 바꾸고 다시 누른다. 아래 입력 로그는 각 문자열로 한 번에 교체한 경우다. 직접 한 글자씩 타이핑하면 input이 여러 번 발생하므로 중간 로그도 더 생긴다. 새 예제는 외부 전송 대신 화면에 검사 결과만 표시한다. 원본의 form.submit()까지 그대로 실행한 예제가 아님을 구분한다. 마지막 대괄호 안의 공백은 원래 value가 남았다는 관찰 표시다.

</details>

## 문제 2. 개념을 자신의 말로 설명

1. value에 대입하면 input 리스너가 자동 실행되는가?
2. 검사에 trim을 쓰면 실제 value도 바뀌는가?
3. form.submit()은 이 submit 리스너를 다시 호출하는가?

<details>
<summary>풀이</summary>

세 가지 모두 아니다. 프로그램 대입과 사용자 input 이벤트, 새 문자열 반환과 원본 수정, 직접 제출 메서드와 submit 이벤트를 각각 구별한다.

| 입력 | trim 결과 길이 | 원본의 분기 | 원래 value |
| --- | --- | --- | --- |
| 빈 값·공백만 | 0 | 안내 | 그대로 |
| '가' | 1 | 안내 | 그대로 |
| '  가  ' | 1 | 안내 | 공백 포함 |
| '가나' | 2 | 직접 제출 | 그대로 |
| '  가나  ' | 2 | 직접 제출 | 공백 포함 |

form.submit()은 submit 이벤트 함수를 다시 부르지 않는 직접 제출 메서드이므로 이 원본이 무한히 자기 자신을 부르는 것은 아니다. 브라우저의 기본 제약 검증도 거치지 않는다. 이전 개편의 로컬 수신 검수에서는 공백이 전달되는 것을 확인했지만, 이번 작은 예제는 전송을 수행하지 않고 문자열 상태만 관찰했다. 확인 시점과 검수 범위를 혼동하지 않는다.

</details>

## 문제 3. 한 가지를 바꾸어 확인

먼저 **trim 제거**를 바꾸면 무엇이 달라질지 적는다. 그다음 실행 파일에 해당 변경만 적용해 실제 결과와 비교한다. 나머지 실험도 원래 예제로 돌아가 하나씩 수행한다.

<details>
<summary>변경 결과와 막힐 때 확인</summary>

| 한 가지만 변경 | 예상 | 해석 |
| --- | --- | --- |
| trim 제거 | 공백 두 칸도 길이 2로 통과 | 실제 의미 있는 글자 검사와 달라짐 |
| 검사 전 query.value에 trim 결과 대입 | 앞뒤 공백이 입력에서도 사라짐 | 검사와 수정의 차이 |
| input 로그를 keyup으로 변경 | 붙여넣기 등에서 관찰 차이 | 키 사건과 값 변경의 차이 |

검사 통과 뒤 화면이 이동한다면 기본 제출을 취소했는지 본다. 공백이 남아 있으면 trim의 반환값만 검사했는지 확인한다. 초점 색이 입력 후 바뀌면 input의 색상 대입 순서를 읽는다. 무작위 색이 예시와 달라도 범위를 만족하면 같은 로직이다.

</details>

## 채점과 복습

| 점검 | 확인할 것 |
| --- | --- |
| 예측 | 실행 전에 출력·상태를 적었는가? |
| 근거 | 문법·조건·반환·순서로 설명했는가? |
| 수정 | 한 조건만 바꾸었는가? |
| 확인 | 실제 관찰과 코드 기준 예상을 구분했는가? |

틀린 이유를 설명할 수 없다면 [본문](../../17_JavaScript_폼이벤트와_이벤트전파_실전문제.md)의 작은 예제·내 원본 풀이로 돌아간다. TIP의 미학습 기능은 이 문제의 필수 정답이 아니다.
