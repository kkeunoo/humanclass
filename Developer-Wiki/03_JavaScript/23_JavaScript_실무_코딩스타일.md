# JavaScript 실무 코딩 스타일 — 수업 코드에서 고쳐 보기

[JavaScript 목차](README.md) · [종합실습](24_JavaScript_종합실습.md) · [장별 연습문제](실습/연습문제/README.md)

이 문서는 강사님·내 **23번 수업 원본**이 아니다. [17-04 메뉴·Todo](17-04_JavaScript_메뉴와_Todo실습.md), [17-02 이벤트 위임](17-02_JavaScript_이벤트전파와_위임.md), [13장 폼 입력](13_JavaScript_DOM_폼요소와_입력값처리.md)에서 이미 사용한 문법을 **읽기·수정하기 쉬운 형태로 재구성한 실무 연습**이다. 새 규칙을 실제로 수업에서 배웠다는 뜻은 아니다.

이 장의 기준은 세 가지다. **값을 어디서 읽는가, 어느 조건에서 멈추는가, 화면의 어느 부분을 바꾸는가.** 코드를 고칠 때 이 순서를 따라가면 한 번의 클릭이 두 번 적용되거나 이전 상태가 남는 문제를 찾기 쉽다.

**작은 예제 — 원본 발췌 아님:** 값 검사를 화면 변경보다 먼저 한다.

```javascript
function addTodo(value) {
  const text = value.trim();
  if (text == '') return '추가 안 함';
  return '추가할 글: ' + text;
}
console.log(addTodo('   ')); // 추가 안 함
```

이 순서는 내 Todo 원본에서 빈 `div`를 먼저 붙여 남기는 문제를 고치는 기준이 된다. 실제 화면 추가 코드는 검사 뒤에 둔다.

## 1. DOM을 읽고, 값을 검사하고, 화면을 바꾸는 순서

내 메뉴 원본은 항목마다 리스너를 붙이고 클릭할 때 `✔`를 글자에 추가한다. 다시 클릭하면 `✔✔`가 쌓인다. 강사님 코드는 부모 `ul`에 리스너 하나를 붙여 기존 클래스를 지운 다음 선택한 항목만 강조한다. 원본과 결과 비교는 [17-04](17-04_JavaScript_메뉴와_Todo실습.md)에 있다.

| 수업 원본 | 두 번 클릭했을 때 | 이 장에서 가져올 점 |
| --- | --- | --- |
| 강사님 메뉴 코드 | 이전 `bold`를 지우고 현재 항목만 강조 | 기존 상태를 먼저 정리 |
| 내 메뉴 코드 | `✔`가 글자 앞에 누적될 수 있음 | 글자보다 클래스로 선택 상태 표시 |

아래는 **원본 발췌가 아닌 재구성 예제**다. 문자 자체를 바꿔 상태를 기억하지 않고, 선택 상태는 `class`로 표현한다.

```javascript
const menu = document.querySelector('#menu');
const selectedName = document.querySelector('#selected-name');

menu.addEventListener('click', function (event) {
  const button = event.target;
  if (!button.hasAttribute('data-name')) return;

  const buttons = menu.querySelectorAll('button');
  for (let i = 0; i < buttons.length; i++) buttons[i].classList.remove('selected');
  button.classList.add('selected');
  selectedName.textContent = button.dataset.name;
});
```

입력·처리·출력을 나눠 읽으면 `data-name`을 바꿔도 선택 동작은 같다. 수업 원본에서 사용한 `hasAttribute`와 `for`문으로 작성했다. `event.target`은 자식 요소일 수도 있으므로 **이 예제처럼 data-name은 버튼에만 있고 버튼 안에 다른 요소가 없다는 조건**을 지킨다. 그런 요소까지 허용하는 `closest()` 설계는 아래 `추가로 알면 좋은 것`에 둔다.

## 2. 상태와 화면을 한 번에 갱신하기

Todo의 항목 수를 여러 곳에서 각각 1씩 바꾸면 삭제·전체 삭제 때 값이 어긋나기 쉽다. 수업에서 배운 DOM 선택으로 동작 뒤에 현재 항목을 다시 세어 화면을 갱신할 수 있다. 아래는 수업 원본처럼 **항목이 `div`인 경우**의 재구성 예제다. 24장 새 종합실습은 `li`를 쓰므로 선택자도 그에 맞춰 다르다.

```javascript
function updateCount() {
  const count = document.querySelectorAll('#todo-list > div').length;
  document.querySelector('#todo-count').textContent = count;
}
```

함수 이름은 **무엇을 바꾸는지** 드러내고, 한 함수의 입력값과 화면 효과를 읽을 수 있게 한다. 함수·변수 이름 규칙 자체는 팀마다 다를 수 있다. 중요한 것은 한 파일에서 일관되게 적용하고 `data`, `temp`처럼 목적을 감추는 이름을 줄이는 것이다.

## 3. 제출 기본 동작, 오류, 외부 응답을 구별하기

- 폼을 현재 화면에서 처리할 때는 `submit` 이벤트에서 `preventDefault()`를 호출한다. 이는 기본 제출을 막을 뿐 이벤트 전파를 자동으로 막지 않는다.
- 입력값이 비어 있으면 목록을 만들지 않고 사용자에게 원인을 표시한다. 입력 검사를 먼저 하고 DOM 변경은 그다음 한다.
- `fetch`·외부 AI·웹훅 원본의 성공 예시를 실행 보장으로 쓰지 않는다. 요청 데이터, 성공 응답 처리, 실패 표시를 구별한다.
- API 키나 비밀 주소를 GitHub용 HTML·JavaScript에 직접 넣지 않는다. 이 문서의 실습은 외부 호출 없이 동작한다.

## 직접 점검할 질문

1. 같은 메뉴를 두 번 클릭해도 선택 표시가 하나만 남는가?
2. Todo를 삭제한 뒤 항목 수는 DOM의 실제 항목과 같은가?
3. `preventDefault()`와 `stopPropagation()`은 서로 다른 무엇을 막는가?

## 추가로 알면 좋은 것

> [!TIP]
> 더 큰 앱의 모듈 분리·빌드 도구·컴포넌트 아키텍처는 양쪽 수업 코드의 본문 범위가 아니다. 메뉴 예제의 버튼 안에 다른 태그도 넣고 싶다면 그때 필요한 이벤트 대상 처리 방법을 추가로 공부한다.

이벤트 처리의 일반 원칙은 [MDN 이벤트 가이드](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Events)와 [preventDefault 설명](https://developer.mozilla.org/en-US/docs/Web/API/Event/preventDefault)을 참고할 수 있다.
