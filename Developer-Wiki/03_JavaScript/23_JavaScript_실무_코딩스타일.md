# 23. 실무 코딩 스타일 — 읽기 좋은 이름보다 먼저 동작의 책임 나누기

[JavaScript 목차](README.md) · [읽기 안내](00_JavaScript_V3_동작_백과_읽기법.md)

이 장은 원본 수업 23번이 아니라 수업에서 배운 문법을 실제 수정 관점으로 재구성한 연습이다. 스타일을 들여쓰기나 세미콜론 취향으로만 보지 않고, 입력 검사·화면 변경·공통 등록·상태 갱신의 책임을 분명히 하는 기준으로 익힌다.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

입력 검사 전에 화면을 바꾸지 않고, 함수 이름에서 하는 일을 찾을 수 있게 구성한다. 필요한 DOM 범위만 다루고, 수정 후에도 확인할 동작 목록을 만든다. 팀의 취향과 실제 오류를 구분한다.

입력·현재 상태·실행 순서·결과를 분리해 설명한다. 실제 수업 원본은 아래에 표시하고, 원본에 없는 선택 학습은 9절 TIP에 둔다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

유지보수는 처음 작성한 코드에 기능을 추가하거나 오류를 고치는 작업이다. 나중의 내가 왜 이 변수가 있고 어떤 함수가 화면을 바꾸는지 알 수 있어야 수정 범위를 정할 수 있다. 긴 함수를 무조건 잘게 쪼개는 것보다 한 함수가 맡은 일을 문장 하나로 설명할 수 있는지가 먼저다.

| 기준 | 읽는 사람의 질문 | 이 장의 적용 |
| --- | --- | --- |
| 구체적인 이름 | 무엇을 세고 바꾸는가? | count·updateCount |
| 조기 종료 | 실패 뒤 작업을 더 하는가? | 빈 입력이면 return |
| 조회 범위 | 어느 줄의 버튼인가? | 만든 row의 요소 참조 |
| 등록 위치 | 공통 처리가 몇 번 연결되는가? | 폼 리스너 한 번 |
| 상태 갱신 | 삭제 뒤에도 표시가 맞는가? | 추가·삭제 뒤 updateCount |

함수 분리 자체가 목적은 아니다. 아래 updateCount는 현재 항목을 다시 세어 같은 표시를 바꾼다. 추가와 삭제에서 반복될 규칙을 한 곳으로 모았기 때문에 이유가 있다. 한 번 쓰는 값을 얻으려고 의미 없는 중간 함수를 여러 개 만들지는 않는다.

문법 선택과 오류도 나눈다. 작은따옴표·세미콜론 사용은 팀 규칙에 맞춰 일관되게 정할 수 있다. 반면 선언되지 않은 변수, 빈 입력 뒤 null 호출, 누적 리스너는 실제 동작 문제다. 형식만 고쳤다고 그런 문제가 해결되지는 않는다.

> 📚 **출처 · 본문 설명 확인:** [MDN 이벤트 처리](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Events), [Element.querySelector](https://developer.mozilla.org/en-US/docs/Web/API/Element/querySelector). 배운 기능의 뜻을 확인한 근거다. 예제·표·풀이 흐름은 수업 코드를 바탕으로 새로 작성했으며 외부 문장을 직접 인용하지 않았다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 스크립트.** [HTML 실행 파일](실습/책형_복습/23_JavaScript_실무_코딩스타일.html)과 같은 폴더의 [JS 파일](실습/책형_복습/23_JavaScript_실무_코딩스타일.js)을 함께 내려받는다. HTML을 브라우저로 열고 Console에서 결과를 확인한다. script는 필요한 HTML 뒤에 연결한다. 콘솔 출력은 페이지 본문에 자동으로 쓰이지 않는다.

**먼저 준비할 HTML · body 안:**

```html
    <form id="todoForm"><label>할 일 <input id="todoInput"></label><button type="submit">추가</button></form>
    <p id="warning"></p><p>현재 항목 <span id="count">0</span>개</p><ul id="list"></ul>
```

```javascript
const form = document.getElementById('todoForm');
const input = document.getElementById('todoInput');
const list = document.getElementById('list');
const count = document.getElementById('count');
const warning = document.getElementById('warning');
function updateCount() {
    count.textContent = list.querySelectorAll('li').length;
}
form.addEventListener('submit', function (event) {
    event.preventDefault();
    const title = input.value.trim();
    if (title === '') {
        warning.textContent = '내용을 입력하세요';
        return;
    }
    warning.textContent = '';
    const row = document.createElement('li');
    const text = document.createElement('span');
    text.textContent = title;
    const removeButton = document.createElement('button');
    removeButton.type = 'button';
    removeButton.textContent = '삭제';
    removeButton.addEventListener('click', function () {
        row.remove();
        updateCount();
    });
    row.append(text, removeButton);
    list.append(row);
    input.value = '';
    updateCount();
});
```

공백으로 제출한 뒤 A·B를 추가하고 A를 삭제한다. DOM을 바꾸기 전에 검사하므로 첫 실패는 빈 li도 만들지 않는다. 추가 뒤와 삭제 뒤 모두 updateCount를 호출하여 현재 li 수를 표시한다. 제목 글자는 textContent로 넣는다. 삭제 버튼은 생성한 removeButton에 직접 등록하므로 다른 항목을 문서 전체에서 다시 찾지 않는다. 이 코드의 구조는 새 연습이며 수업 원본을 몰래 덮어쓴 결과가 아니다.

**예상 출력 또는 관찰:**

```text
공백 제출 → 경고·0개
A·B 추가 → 2개
A 삭제 → B만 남고 1개
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본의 일부다. 원본에 의존하는 앞 선언·HTML·함수는 다음 절의 연결까지 읽는다. 주석의 잘못된 표현도 원문대로 보존하고 설명에서 교정한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/asset/js/17_event_form.js` 418–432행

```javascript
        for(let i=1; i<2; i++) {
            divAdd.classList.add(`col${divCnt}`)
        }
        column.prepend(divAdd)

        // console.log(inputText.innerText)
        if(inputText.value.trim() == '') {
            alert('할일은 한 글자 이상 입력하세요.')
        } else {
            divAdd.innerHTML = `
            <input type="checkbox" class=deleteChk>
            ${inputText.value}
            <button type="button" class="deleteCol">삭제</button>
            `

```

아래 내 Todo 발췌는 새 div를 먼저 붙이고 그 뒤 빈 입력을 검사하는 부분이다. 검사 자체는 있지만 위치 때문에 실패한 경우에도 화면을 바꾼다. 이 장의 개선은 검사식을 더 복잡하게 만드는 것이 아니라 순서를 바꾸는 것이다. 원본 전체의 등록 누적·j 오류·빈 입력 뒤 조회 문제는 17-04에서 읽고, 여기서는 그 문제를 다시 만들지 않는 작성 기준으로 연결한다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

submit 이벤트 → 현재 input.value → trim 결과 title → 실패면 안내 후 return → 성공이면 row와 버튼 생성 → 자식 연결 → list에 추가 → updateCount다. 삭제 콜백은 자신이 만든 row를 가리킨다. updateCount의 선언은 위에 있고 추가·삭제 두 곳에서 호출한다. 입력 결과와 DOM 효과가 있는 함수를 구별하여 “어느 호출이 화면을 바꾸는가”를 추적한다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**살릴 점:** 내 원본은 입력 검사와 삭제 함수를 직접 작성하여 요구 기능을 시도했다. **바꿀 점:** 검사 순서와 등록 범위가 요구사항을 흔든다. **이 개선의 이점:** 현재 DOM에서 개수를 다시 세므로 카운터를 여러 곳에서 가감하다 어긋나는 문제를 피하기 쉽다. **적용 조건:** 작은 학습 화면에 맞춘 방식이다. 큰 데이터 목록에서 매번 전체 조회하는 비용까지 해결한 구조라고 주장하지 않는다.

개선안은 원본을 수정한 결과가 아니다. 실제 오류, 수업용 단순화, 목적에 따른 선택을 구별해 판단한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



필요한 비교는 17-04에 모았다. 강사님의 기존 상태 제거와 공통 버튼 등록 위치는 참고하고, 내 빈 값 검사와 취소선 의도는 보존한다. 강사님 코드라고 모든 줄을 정답으로 복제하지 않으며, 이 장에서 더 짧은 코드만을 좋은 코드의 기준으로 삼지 않는다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 확인 항목 | 기대하는 동작 | 실패하면 볼 위치 |
| --- | --- | --- |
| 공백 제출 | DOM 변화 없음 | 검사와 생성 순서 |
| 항목 두 개 추가 | 서로 다른 두 줄 | 요소 생성 위치 |
| 첫 항목 삭제 | 해당 줄만 삭제 | 참조한 row |
| 삭제 뒤 개수 | 실제 목록과 일치 | updateCount 호출 |
| 연속 추가 | 제출당 한 번 추가 | 폼 등록 위치 |

실무에서도 “한 번 실행됐는가”만 확인하지 않는다. 빈 입력·반복 입력·삭제 뒤 상태처럼 이전 동작이 남기는 영향을 함께 확인한다. 이 표는 이번 작은 화면에 필요한 회귀 확인 목록이며 모든 프로젝트에 같은 항목 수의 검사를 강요하는 규칙은 아니다.

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| 삭제 뒤 updateCount 제거 | 목록과 개수가 어긋남 | 화면 요약 갱신 누락 |
| 검사 전에 list.append 이동 | 빈 줄이 남을 수 있음 | 실패 전 부수 효과 |
| textContent 대신 입력을 innerHTML에 넣기 | 태그 모양 글자의 해석 차이 | 글자와 HTML 구분 |

함수가 많아져도 어떤 효과가 있는지 모르면 이름과 호출 지점을 다시 적는다. 삭제 대상이 다르면 선택 범위를 좁히거나 생성한 요소 참조를 사용한다. 코드 형식을 정리한 뒤에도 동일 조작 순서로 결과를 확인해야 실제 동작 보존을 판단할 수 있다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** ESLint·Prettier 설정, ES 모듈·빌드 도구, 자동화 테스트 도구의 체계적인 도입과 컴포넌트 설계는 추가 학습이다. 도구 이름을 본문 필수 조건으로 앞당기지 않는다.



이 절의 확장은 기본 문제의 필수 조건이 아니다. 📚 출처가 있다는 것과 수업 밖 기능이라는 것은 다른 구분이다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. 검사식이 있어도 빈 줄이 생길 수 있는 이유는?
2. updateCount는 왜 두 곳에서 호출하는가?
3. 세미콜론을 통일하면 j 미선언 오류도 해결되는가?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

검사보다 먼저 DOM을 바꾸면 실패해도 흔적이 남는다. 추가·삭제 모두 항목 수를 바꾸므로 같은 규칙을 호출한다. 형식 통일과 변수 선언 오류는 별개다.

</details>

| 순서 | 질문 |
| --- | --- |
| 읽기 | 값의 출처가 분명한가? |
| 검사 | 실패 전에 화면을 바꾸지 않았나? |
| 변경 | 어떤 요소를 바꾸나? |
| 확인 | 반복 조작 뒤에도 같은 규칙인가? |

[장별 연습문제](실습/연습문제/23_JavaScript_실무_코딩스타일_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [종합실습](24_JavaScript_종합실습.md)이다.
