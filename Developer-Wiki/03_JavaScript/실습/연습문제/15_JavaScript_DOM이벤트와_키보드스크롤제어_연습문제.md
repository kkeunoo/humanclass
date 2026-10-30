# 15. DOM 이벤트 — 등록·호출·제거와 입력 검사 — 연습문제

[본문](../../15_JavaScript_DOM이벤트와_키보드스크롤제어.md) · [문제 목차](README.md)

실제 수업 기능을 바탕으로 **새로 구성한 연습문제**다. 강사님 원본 퀴즈와 구분한다. 예상 → 이유 → 수정 순서로 풀고, 정답은 먼저 답한 뒤 펼친다.

## 목표와 실행 조건

onclick의 교체와 addEventListener의 여러 함수 등록을 비교한다. 등록할 때 사용한 함수 참조로 제거하는 이유, HTML과 외부 JavaScript의 연결, 입력 검사와 실제 인증의 차이를 설명한다.

[전체 실행 HTML](../책형_복습/15_JavaScript_DOM이벤트와_키보드스크롤제어.html)과 같은 폴더의 JS를 함께 준비한다. Console을 열고 새로고침하면 처음부터 실행한다. 원본과 별도 파일이므로 기존 변수·타이머·출력 변경 실험의 영향을 섞지 않는다. 실제 입력·현재 시각·난수는 고정 결과와 구별한다.

입력·버튼·키보드·스크롤 예제는 [본문의 3절](../../15_JavaScript_DOM이벤트와_키보드스크롤제어.md#example)에 적힌 조작 순서대로 결과를 예상한다. 통신 예제는 해당 절의 가상 JSON 파일과 로컬 웹 실행 준비가 필요하며 HTML을 직접 여는 조건과 다르다. Console 출력이 없는 문제는 화면의 값·개수·선택 상태를 답한다.

## 문제 1. 실행 순서와 결과 예상

다음은 **새 설명 예제**다. 출력 전에 어떤 값이 어떤 순서로 만들어지는지 적는다.

**필요한 HTML · 스크립트 앞:**

```html
    <button id="first" type="button">속성 방식</button>
    <button id="second" type="button">여러 함수</button>
    <button id="removed" type="button">제거된 등록</button>
    <p><label for="user">연습 아이디</label><input id="user"></p>
    <p><label for="password">연습 비밀번호</label><input id="password" type="password"></p>
    <button id="check" type="button">입력 확인</button>
    <p id="warning"></p><div id="view"></div>
```

```javascript
function writeLog(message) {
    const p = document.createElement('p');
    p.textContent = message;
    document.getElementById('view').prepend(p);
    console.log(message);
}
const first = document.getElementById('first');
first.onclick = function () { console.log('교체 전'); };
first.onclick = function () { console.log('교체 후'); };
const second = document.getElementById('second');
second.addEventListener('click', function () { console.log('첫째'); });
second.addEventListener('click', function () { console.log('둘째'); });
function removedHandler() { console.log('제거한 함수'); }
const removed = document.getElementById('removed');
removed.addEventListener('click', removedHandler);
removed.removeEventListener('click', removedHandler);
function checkInput() {
    const user = document.getElementById('user');
    const password = document.getElementById('password');
    const warning = document.getElementById('warning');
    if (user.value.trim() === '') {
        warning.textContent = '아이디는 필수';
    } else if (password.value.trim() === '') {
        warning.textContent = '비밀번호는 필수';
    } else {
        warning.textContent = '';
    }
    writeLog(warning.textContent === '' ? '입력 확인' : warning.textContent);
}
document.getElementById('check').addEventListener('click', checkInput);
```

<details>
<summary>힌트와 풀이</summary>

**힌트:** 입력·현재 상태·실행 시점·반환값을 따로 표시한다.

```text
교체 후
첫째
둘째
아이디는 필수
비밀번호는 필수
입력 확인
```

파일을 열기만 하면 아직 Console 출력은 없다. **속성 방식 → 여러 함수 → 제거된 등록 → 빈 입력 확인 → 아이디에 student만 넣고 확인 → 비밀번호에 practice도 넣고 확인** 순서로 조작한다. 속성 방식은 뒤에 대입한 함수만 실행하고, 여러 함수 버튼은 등록한 두 함수를 차례로 실행한다. 제거된 등록 버튼은 아무것도 출력하지 않는다. 입력 확인을 세 번 마치면 현재 경고는 비어 있지만 view에는 과거 메시지 세 개가 남는다. 현재 경고와 과거 기록은 서로 다른 요소이기 때문이다. 두 입력값은 임의의 연습값이며 서버로 보내지 않는다.

</details>

## 문제 2. 개념을 자신의 말로 설명

1. onclick에 두 번 대입하면 두 함수가 모두 쌓이는가?
2. 등록했던 함수를 제거하려면 어떤 값을 보관해야 하는가?
3. 현재 경고를 비우면 과거 메시지도 자동으로 없어지는가?

<details>
<summary>풀이</summary>

같은 처리 속성은 뒤의 값으로 교체된다. 제거하려면 등록했던 함수 참조가 필요하다. warning과 view의 과거 자식 요소들은 다른 상태이므로 하나를 비운다고 다른 쪽이 자동으로 삭제되지 않는다.

| 원본에 주는 입력 | 내 화면의 경고 | 해석 |
| --- | --- | --- |
| 둘 다 비움 | 아이디 필수 | 첫 번째 조건에서 처리 |
| 아이디만 입력 | 아이디 필수라는 잘못된 문구 | 비밀번호 조건 안의 복사 오류 |
| 둘 다 입력 | 이전 경고 유지 | else가 없어 기존 표시를 바꾸지 않음 |
| 버튼 4 클릭 | 새 출력 없음 | 리스너가 제거된 상태 |

trim()은 앞뒤 공백을 제거한 새 문자열을 반환한다. 원래 input.value를 자동으로 고치지는 않는다. 공백만 입력한 값을 검사할 때 도움이 되지만, 검사와 입력값 수정은 별도 작업이다.

**개인 학습 메모 연결:** 첨부 메모에서 적은 개발자 도구의 Event Listeners 패널은 등록 상태를 살펴볼 때 활용한다. 패널 확인과 실제 클릭 결과를 함께 관찰한다. 메모를 원본 코드의 일부나 인증 구현의 증거로 취급하지 않는다.

</details>

## 문제 3. 한 가지를 바꾸어 확인

먼저 **first의 두 번째 대입 제거**를 바꾸면 무엇이 달라질지 적는다. 그다음 실행 파일에 해당 변경만 적용해 실제 결과와 비교한다. 나머지 실험도 원래 예제로 돌아가 하나씩 수행한다.

<details>
<summary>변경 결과와 막힐 때 확인</summary>

| 한 가지만 변경 | 예상 결과 | 확인하는 개념 |
| --- | --- | --- |
| first의 두 번째 대입 제거 | 교체 전 출력 | 첫 번째 속성 값이 유지됨 |
| removeEventListener 호출 제거 | 제거 버튼에서도 출력 | 등록이 남아 있음 |
| 성공 시 warning을 비우는 대입 제거 | 이전 경고가 남을 수 있음 | 등록 문제가 아닌 상태 갱신 문제 |

클릭 전부터 함수가 실행되면 등록 인수에 handler()처럼 괄호를 붙였는지 확인한다. 제거가 안 되면 등록했던 함수와 같은 참조를 넘기는지 본다. 요소가 null이면 선택자뿐 아니라 head에서의 실행 시점과 load 이후의 재선택도 확인한다. 문구가 틀리면 화면만 보지 말고 그 문구에 도달한 입력 조건부터 추적한다.

</details>

## 채점과 복습

| 점검 | 확인할 것 |
| --- | --- |
| 예측 | 실행 전에 출력·상태를 적었는가? |
| 근거 | 문법·조건·반환·순서로 설명했는가? |
| 수정 | 한 조건만 바꾸었는가? |
| 확인 | 실제 관찰과 코드 기준 예상을 구분했는가? |

틀린 이유를 설명할 수 없다면 [본문](../../15_JavaScript_DOM이벤트와_키보드스크롤제어.md)의 작은 예제·내 원본 풀이로 돌아간다. TIP의 미학습 기능은 이 문제의 필수 정답이 아니다.
