# 22. 웹훅 POST — 보낼 내용을 만들고 전송 단계와 구별하기 — 연습문제

[본문](../../22_JavaScript_웹훅_POST요청.md) · [문제 목차](README.md)

실제 수업 기능을 바탕으로 **새로 구성한 연습문제**다. 강사님 원본 퀴즈와 구분한다. 예상 → 이유 → 수정 순서로 풀고, 정답은 먼저 답한 뒤 펼친다.

## 목표와 실행 조건

username·content 객체와 JSON 문자열의 차이를 설명한다. open → 헤더 지정 → send → 응답 처리의 순서를 읽고, 본문 미리 보기와 실제 메시지 전달 성공을 구별한다.

[전체 실행 HTML](../책형_복습/22_JavaScript_웹훅_POST요청.html)과 같은 폴더의 JS를 함께 준비한다. Console을 열고 새로고침하면 처음부터 실행한다. 원본과 별도 파일이므로 기존 변수·타이머·출력 변경 실험의 영향을 섞지 않는다. 실제 입력·현재 시각·난수는 고정 결과와 구별한다.

입력·버튼·키보드·스크롤 예제는 [본문의 3절](../../22_JavaScript_웹훅_POST요청.md#example)에 적힌 조작 순서대로 결과를 예상한다. 통신 예제는 해당 절의 가상 JSON 파일과 로컬 웹 실행 준비가 필요하며 HTML을 직접 여는 조건과 다르다. Console 출력이 없는 문제는 화면의 값·개수·선택 상태를 답한다.

## 문제 1. 실행 순서와 결과 예상

다음은 **새 설명 예제**다. 출력 전에 어떤 값이 어떤 순서로 만들어지는지 적는다.

**필요한 HTML · 스크립트 앞:**

```html
    <label>메시지 연습 <input id="prompt" value="안녕하세요"></label>
    <button id="preview" type="button">본문 미리 보기</button>
    <pre id="result"></pre>
```

```javascript
function makePayload(text) {
    return { username: '연습', content: text };
}
document.getElementById('preview').addEventListener('click', function () {
    const text = document.getElementById('prompt').value;
    const param = makePayload(text);
    const body = JSON.stringify(param);
    document.getElementById('result').textContent = body;
    console.log(typeof param, typeof body);
    console.log(body);
});
```

<details>
<summary>힌트와 풀이</summary>

**힌트:** 입력·현재 상태·실행 시점·반환값을 따로 표시한다.

```text
object string
{"username":"연습","content":"안녕하세요"}
```

미리 보기 버튼은 입력을 makePayload에 넘긴다. 함수는 두 속성을 가진 객체를 반환하고, 콜백은 stringify하여 화면과 Console에 표시한다. 미리 보기에는 웹훅 주소와 send 호출이 없으므로 메시지를 전송하지 않는다. 예상 출력은 객체·문자열 변환의 결과이며 전송 성공 메시지가 아니다. 원본의 전송 연결은 아래 실제 코드에서 별도로 읽는다.

</details>

## 문제 2. 개념을 자신의 말로 설명

1. stringify만 호출하면 전송되는가?
2. 헤더 지정은 open과 send 사이 중 어디인가?
3. 미리 보기 출력이 실제 채널 도착의 증거인가?

<details>
<summary>풀이</summary>

문자열만 만들어지며 전송은 별도다. open 뒤 send 전에 지정한다. 미리 보기는 요청 본문의 확인일 뿐 실제 전달의 증거가 아니다.

| 확인 단계 | 코드만으로 확인 가능한 것 | 아직 확인하지 않은 것 |
| --- | --- | --- |
| 객체 생성 | username·content 값 | 요청 전송 |
| stringify | JSON 문자열 결과 | 서버 수신 |
| send 호출 | 요청을 시작하는 코드 | 메시지 생성 성공 |
| onload | 응답을 읽는 처리 | 실제 채널의 표시 결과 |

현재 공식 문서는 웹훅 실행의 요청 필드와 응답 동작을 구분한다. 이 장은 실제 전송을 재현하지 않고 원본 요청 구성과 로컬 본문 미리 보기만 검증했다. 수업 코드의 주소를 다시 쓰거나 메시지를 보내며 확인한 것으로 보고하지 않는다.

</details>

## 문제 3. 한 가지를 바꾸어 확인

먼저 **입력을 다른 글로 변경**를 바꾸면 무엇이 달라질지 적는다. 그다음 실행 파일에 해당 변경만 적용해 실제 결과와 비교한다. 나머지 실험도 원래 예제로 돌아가 하나씩 수행한다.

<details>
<summary>변경 결과와 막힐 때 확인</summary>

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| 입력을 다른 글로 변경 | content 문자열만 변경 | 클릭 때 현재 값 읽기 |
| 표시 이름 변경 | username만 변경 | 객체 속성 값 차이 |
| 입력에 큰따옴표 포함 | JSON 출력에서 필요한 이스케이프 | stringify가 형식 구성 |
| body를 표시만 하기 | 네트워크 요청 없음 | 문자열 생성과 전송은 별개 |

표시는 되는데 전달이 안 된다는 판단 전에 예제가 미리 보기인지 실제 send가 있는지 확인한다. JSON 문자열을 손으로 이어 붙이지 말고 객체를 stringify한 결과를 관찰한다. 응답이 빈 글자여도 본문 유무만으로 성공·실패를 결정하지 않는다.

</details>

## 채점과 복습

| 점검 | 확인할 것 |
| --- | --- |
| 예측 | 실행 전에 출력·상태를 적었는가? |
| 근거 | 문법·조건·반환·순서로 설명했는가? |
| 수정 | 한 조건만 바꾸었는가? |
| 확인 | 실제 관찰과 코드 기준 예상을 구분했는가? |

틀린 이유를 설명할 수 없다면 [본문](../../22_JavaScript_웹훅_POST요청.md)의 작은 예제·내 원본 풀이로 돌아간다. TIP의 미학습 기능은 이 문제의 필수 정답이 아니다.
