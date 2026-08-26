# JavaScript V3 동작 백과 읽기법

> JavaScript 문법을 외우는 문서가 아니라, 브라우저가 HTML과 JavaScript를 읽고 값·화면·네트워크를 어떻게 바꾸는지 다시 재현하기 위한 공통 안내서다.

## 1. 실행 환경과 전체 흐름

JavaScript 언어와 브라우저 기능은 같은 것이 아니다. 변수, 함수, 배열, 객체, Promise는 언어의 기능이다. `document`, `window`, DOM, `alert`, `fetch`, 이벤트는 브라우저가 제공하는 Web API다. 브라우저 예제를 Node.js에서 실행하면 `document is not defined` 같은 오류가 날 수 있다.

```text
HTML 파싱 → DOM 생성 → script 실행 → 값·함수 생성
→ DOM 선택·이벤트 등록 → 사용자/타이머/네트워크 이벤트 발생
→ 콜백 실행 → 상태·DOM 변경 → 브라우저가 화면 갱신
```

## 2. 값은 어디에서 들어오는가

| 출처 | 대표 코드 | 처음 받는 형태 | 확인 방법 |
|---|---|---|---|
| 소스 리터럴 | `const count = 1` | number | `typeof count` |
| 입력 요소 | `input.value` | string | Console과 Elements |
| 이벤트 | 콜백의 `event` | Event 객체 | `event.type`, `event.target` |
| DOM 속성 | `element.textContent` | 주로 string | DOM과 화면 비교 |
| 서버 응답 | `await response.json()` | Promise를 거친 JS 값 | Network와 Console |
| JSON 문자열 | `JSON.parse(text)` | 객체·배열 등 | 변환 전후 `typeof` |

## 3. 등록 시점과 실행 시점

```javascript
const button = document.querySelector("#save");
button.addEventListener("click", () => {
  const value = document.querySelector("#title").value;
  console.log(value);
});
```

script 실행 때 요소를 찾고 콜백을 등록하지만 입력값은 아직 읽지 않는다. 사용자가 클릭하면 브라우저가 Event 객체를 만들고 콜백을 실행하며, 그 시점의 `input.value`를 문자열로 읽어 Console에 출력한다.

## 4. 결과가 나타나는 위치

- `console.log()`: 개발자 도구 Console에 보인다.
- `textContent`, `classList`, `style`: DOM을 바꾸고 화면에 반영된다.
- `return`: 호출자에게 값을 돌려주며 자동 출력되지 않는다.
- `fetch()`: 즉시 본문이 아니라 Promise를 반환한다.
- Network 패널: 요청 URL, 메서드, 상태 코드, 응답을 확인한다.

## 5. 오류를 읽는 순서

Console의 오류 종류·메시지·파일명·줄 번호를 먼저 확인한다. `null`의 속성을 읽는 오류는 선택자, script 실행 시점, HTML 요소 존재를 역추적한다. 네트워크 문제는 Network에서 URL, 메서드, 상태 코드, 응답 본문과 CORS 여부를 확인한다.

## 6. 원본 비교 규칙

- 내 코드는 `workspace_html/javascript`의 번호형 HTML/JS 파일을 기준으로 한다.
- 강사님 코드는 같은 경로의 강사님 workspace 원본을 기준으로 한다.
- 실행 시점, 자료형, DOM 상태, 이벤트 전파, 오류 처리 차이를 비교한다.
- 원본에 없는 설명은 `Wiki 확장 학습`으로 표시한다.

## 7. 다시 작성 가능한지 확인하는 질문

1. 이 코드는 언제 실행되는가?
2. 값은 어디에서 왔고 현재 자료형은 무엇인가?
3. 원본 값이나 DOM이 실제로 바뀌는가?
4. Console, 화면, Network에는 각각 무엇이 보이는가?
5. 비동기 작업이라면 어떤 작업이 먼저 끝나는가?
6. 실패하면 어느 API가 어떤 오류를 만드는가?
7. 내 코드와 강사님 코드의 어느 파일에서 확인하는가?
