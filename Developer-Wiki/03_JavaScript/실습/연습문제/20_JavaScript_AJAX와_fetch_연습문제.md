# 20. AJAX와 fetch — 요청한 순간과 데이터를 받은 순간 나누기 — 연습문제

[본문](../../20_JavaScript_AJAX와_fetch.md) · [문제 목차](README.md)

실제 수업 기능을 바탕으로 **새로 구성한 연습문제**다. 강사님 원본 퀴즈와 구분한다. 예상 → 이유 → 수정 순서로 풀고, 정답은 먼저 답한 뒤 펼친다.

## 목표와 실행 조건

XMLHttpRequest의 생성·준비·전송·응답 처리를 설명한다. fetch의 응답 객체와 본문 읽기를 나누고 then의 return이 다음 단계에 무엇을 전달하는지 추적한다. 동기 예외와 비동기 체인의 오류 처리도 구별한다.

[전체 실행 HTML](../책형_복습/20_JavaScript_AJAX와_fetch.html)과 같은 폴더의 JS를 함께 준비한다. Console을 열고 새로고침하면 처음부터 실행한다. 원본과 별도 파일이므로 기존 변수·타이머·출력 변경 실험의 영향을 섞지 않는다. 실제 입력·현재 시각·난수는 고정 결과와 구별한다.

입력·버튼·키보드·스크롤 예제는 [본문의 3절](../../20_JavaScript_AJAX와_fetch.md#example)에 적힌 조작 순서대로 결과를 예상한다. 통신 예제는 해당 절의 가상 JSON 파일과 로컬 웹 실행 준비가 필요하며 HTML을 직접 여는 조건과 다르다. Console 출력이 없는 문제는 화면의 값·개수·선택 상태를 답한다.

## 문제 1. 실행 순서와 결과 예상

다음은 **새 설명 예제**다. 출력 전에 어떤 값이 어떤 순서로 만들어지는지 적는다.

**필요한 HTML · 스크립트 앞:**

```html
    <button id="xhr" type="button">XHR로 읽기</button>
    <button id="fetch" type="button">fetch로 읽기</button>
    <p id="result"></p>
```

```javascript
document.getElementById('xhr').addEventListener('click', function () {
    const xhr = new XMLHttpRequest();
    xhr.open('GET', 'book-users.json');
    xhr.onload = function () {
        const users = JSON.parse(xhr.responseText);
        console.log('XHR 응답', users[1].name);
        document.getElementById('result').textContent = users[1].name;
    };
    xhr.send();
    console.log('XHR 요청 뒤');
});
document.getElementById('fetch').addEventListener('click', function () {
    fetch('book-users.json', { method: 'GET' })
        .then(function (response) {
            return response.json();
        })
        .then(function (users) {
            console.log('fetch 응답', users[2].address.geo.lat);
            document.getElementById('result').textContent = users[2].address.geo.lat;
        })
        .catch(function (error) {
            document.getElementById('result').textContent = '읽기 실패';
            console.error(error);
        });
    console.log('fetch 요청 뒤');
});
```

<details>
<summary>힌트와 풀이</summary>

**힌트:** 입력·현재 상태·실행 시점·반환값을 따로 표시한다.

```text
XHR 요청 뒤
XHR 응답 준호
fetch 요청 뒤
fetch 응답 35.3
```

XHR로 읽기를 누르고 응답까지 확인한 다음 fetch로 읽기를 누른다. 각 버튼의 요청 뒤 로그가 먼저 나오고 응답 처리는 나중에 나온다. 가상 JSON의 배열 인덱스 1은 준호, 인덱스 2의 address.geo.lat는 문자열 35.3이다. 외부 사용자 서비스의 현재 데이터가 아니라 함께 제공한 연습 파일의 값이다. 두 버튼을 빠르게 연달아 누르면 요청들 사이의 응답 순서는 이 예시와 달라질 수 있으므로 조작 조건도 함께 지킨다.

</details>

## 문제 2. 개념을 자신의 말로 설명

1. 요청 직후 출력과 onload 중 어디에서 응답을 읽는가?
2. 첫 then의 response와 다음 users는 같은 값인가?
3. HTML을 JSON으로 읽으면 왜 실패하는가?

<details>
<summary>풀이</summary>

응답이 도착한 뒤 onload에서 읽는다. response는 응답 객체이고 users는 JSON 본문을 읽은 결과다. HTML은 JSON 문법이 아니어서 해석할 수 없다.

| 표현 | 그 순간 얻는 것 | 바로 데이터 배열인가? |
| --- | --- | --- |
| new XMLHttpRequest | 요청 객체 | 아님 |
| send 직후 responseText | 아직 빈 문자열일 수 있음 | 아님 |
| onload의 responseText | 응답 본문 문자열 | parse가 별도 필요 |
| fetch 반환 | Promise | 아님 |
| 첫 then의 response | 응답 객체 | 아님 |
| json을 반환한 다음 then | 해석한 값 | 이 연습 파일은 배열 |

연습 파일을 웹 서버에서 받아오는 것은 실제 로컬 HTTP 요청이다. 외부 서비스의 성공을 확인한 것은 아니다. 상대 주소가 잘못되어 HTML 오류 페이지를 받은 경우 JSON 해석 실패가 날 수 있으므로 “통신이 됐다”와 “원하는 데이터 형식이다”를 나누어 확인한다.

</details>

## 문제 3. 한 가지를 바꾸어 확인

먼저 **users[1]을 users[0]으로**를 바꾸면 무엇이 달라질지 적는다. 그다음 실행 파일에 해당 변경만 적용해 실제 결과와 비교한다. 나머지 실험도 원래 예제로 돌아가 하나씩 수행한다.

<details>
<summary>변경 결과와 막힐 때 확인</summary>

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| users[1]을 users[0]으로 | 민지 출력 | 배열 인덱스 차이 |
| 첫 then의 return 제거 | 다음 then은 undefined를 받을 수 있음 | 비동기 결과를 넘기지 않음 |
| JSON 파일 대신 HTML 요청 | JSON 읽기 실패 | 응답 형식 차이 |
| 요청 주소 오타 | 원하는 데이터 대신 오류·다른 응답 | 요청과 내용 확인 필요 |

파일 직접 열기에서 실패하면 먼저 웹으로 제공하는 실행 조건을 맞춘다. 응답은 왔는데 JSON 오류면 실제 응답 본문을 확인한다. 다음 then의 값이 없으면 return 위치를 본다. 고정 사용자 이름과 좌표는 원본 주석의 당시 예시이며 외부 API의 영구 정답으로 외우지 않는다.

</details>

## 채점과 복습

| 점검 | 확인할 것 |
| --- | --- |
| 예측 | 실행 전에 출력·상태를 적었는가? |
| 근거 | 문법·조건·반환·순서로 설명했는가? |
| 수정 | 한 조건만 바꾸었는가? |
| 확인 | 실제 관찰과 코드 기준 예상을 구분했는가? |

틀린 이유를 설명할 수 없다면 [본문](../../20_JavaScript_AJAX와_fetch.md)의 작은 예제·내 원본 풀이로 돌아간다. TIP의 미학습 기능은 이 문제의 필수 정답이 아니다.
