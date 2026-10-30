# 13. 폼 요소 — 현재 값과 선택 상태를 읽기 — 연습문제

[본문](../../13_JavaScript_DOM_폼요소와_입력값처리.md) · [문제 목차](README.md)

실제 수업 기능을 바탕으로 **새로 구성한 연습문제**다. 강사님 원본 퀴즈와 구분한다. 예상 → 이유 → 수정 순서로 풀고, 정답은 먼저 답한 뒤 펼친다.

## 목표와 실행 조건

value와 checked를 구별하고 input·radio·checkbox·select·textarea의 현재 상태를 읽는다. 목록과 요소의 차이, 날짜 문자열, 한 번 실행과 이벤트 갱신의 차이까지 연결한다.

[전체 실행 HTML](../책형_복습/13_JavaScript_DOM_폼요소와_입력값처리.html)과 같은 폴더의 JS를 함께 준비한다. Console을 열고 새로고침하면 처음부터 실행한다. 원본과 별도 파일이므로 기존 변수·타이머·출력 변경 실험의 영향을 섞지 않는다. 실제 입력·현재 시각·난수는 고정 결과와 구별한다.

입력·버튼·키보드·스크롤 예제는 [본문의 3절](../../13_JavaScript_DOM_폼요소와_입력값처리.md#example)에 적힌 조작 순서대로 결과를 예상한다. 통신 예제는 해당 절의 가상 JSON 파일과 로컬 웹 실행 준비가 필요하며 HTML을 직접 여는 조건과 다르다. Console 출력이 없는 문제는 화면의 값·개수·선택 상태를 답한다.

## 문제 1. 실행 순서와 결과 예상

다음은 **새 설명 예제**다. 출력 전에 어떤 값이 어떤 순서로 만들어지는지 적는다.

**필요한 HTML · 스크립트 앞:**

```html
    <label for="learner">이름</label><input id="learner" value="민지">
    <label><input class="topic" type="checkbox" value="html" checked>HTML</label>
    <label><input class="topic" type="checkbox" value="css">CSS</label>
    <label><input name="group" type="radio" value="A" checked>A</label>
    <label><input name="group" type="radio" value="B">B</label>
    <label for="lang">언어</label>
    <select id="lang"><option value="python">Python</option><option value="java">Java</option></select>
    <label for="memo">메모</label><textarea id="memo">첫 줄
둘째 줄</textarea>
    <div id="view"></div>
```

```javascript
const learner = document.getElementById('learner');
console.log(learner.value);
const topics = document.querySelectorAll('.topic');
console.log(topics[0].checked);
console.log(document.querySelectorAll('.topic:checked').length);
console.log(document.querySelector('[name=group]:checked').value);
const radios = document.querySelectorAll('[name=group]');
radios[1].checked = true;
console.log(document.querySelector('[name=group]:checked').value);
const lang = document.getElementById('lang');
console.log(lang.value);
lang.value = 'java';
console.log(lang.value);
const memo = document.getElementById('memo');
console.log(memo.value.indexOf('\n'));
document.getElementById('view').innerText = memo.value;
```

<details>
<summary>힌트와 풀이</summary>

**힌트:** 입력·현재 상태·실행 시점·반환값을 따로 표시한다.

```text
민지
true
1
A
B
python
java
3
```

초기 HTML에서 HTML 체크박스와 A 라디오를 선택했다. 따라서 처음 선택 개수는1, 라디오 값은A다. B의 checked를 true로 바꾸면 같은 그룹 A가 해제되고 현재 선택을 다시 찾을 때 B가 나온다. select는 Python을 먼저 읽고 java를 대입한 뒤 Java 선택을 읽는다. 메모의 줄바꿈은 인덱스3이며 innerText로 일반 글자와 줄바꿈을 보여 준다. 여기에는 입력 때마다 다시 실행하는 이벤트가 없다.

</details>

## 문제 2. 개념을 자신의 말로 설명

1. 체크박스 value가 a이면 checked도 a인가?
2. 목록의 각 상태를 읽으려면 어디에 [i]가 필요한가?
3. 원본 콜백이 끝난 뒤 입력한 글자가 자동으로 view에 들어가는가?

<details>
<summary>풀이</summary>

checked는 true 또는 false다. checks2[i].checked로 요소를 먼저 고른다. 원본은 한 번만 실행하므로 이후 변경을 자동 반영하지 않는다.

| 실행 시점·조건 | 읽거나 바뀌는 것 | 판단 |
| --- | --- | --- |
| 조작 없이 3초 대기 | 내 text 출력 12345 | 대입 후 읽음 |
| 하나 체크 후 3초 | 위 상태 출력은 true | checks2[i]로 요소를 읽음 |
| 같은 조건의 내 if | 추가 항목 출력 없음 | 목록.checked는 undefined |
| 반복 끝난 뒤 첫 항목 선택 | 현재 첫 항목 true | 과거 반복에는 영향 없음 |
| 콜백 종료 뒤 메모 수정 | view는 이전 글자 | 한 번 실행이며 자동 연결 아님 |

원본 textarea 초기 글자에는 줄바꿈이 없어 indexOf('\n')은 -1이다. 두 줄을 입력하면 위치가 달라진다. 위 새 예제는 처음부터 두 줄이므로 원본 초기 결과와 다르다. 원본의 /\n/g는 줄바꿈을 모두 br로 바꾸는 간단한 사용이며 정규표현식 전체를 배웠다는 근거로 넓히지 않는다.

</details>

## 문제 3. 한 가지를 바꾸어 확인

먼저 **첫 체크박스의 checked만 제거**를 바꾸면 무엇이 달라질지 적는다. 그다음 실행 파일에 해당 변경만 적용해 실제 결과와 비교한다. 나머지 실험도 원래 예제로 돌아가 하나씩 수행한다.

<details>
<summary>변경 결과와 막힐 때 확인</summary>

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| 첫 체크박스의 checked만 제거 | 선택 개수 0 | value가 html이어도 미선택 |
| Java option의 value만 js로 | java 대입 후 일치 option 없음 | 표시 글자와 값은 다름 |
| view의 innerText만 innerHTML로 | 입력 태그가 해석될 수 있음 | 콘텐츠 해석 방식 변경 |

체크했는데 추가 출력이 없으면 목록과 요소를 구별하고 실행 시점도 확인한다. 입력의 textContent가 아니라 value를 읽는다. 화면을 수정했는데 view가 따라오지 않는다면 이벤트가 등록된 코드인지부터 본다. 직접 넣은 태그의 해석과 원문 표시도 별도 확인한다.

</details>

## 채점과 복습

| 점검 | 확인할 것 |
| --- | --- |
| 예측 | 실행 전에 출력·상태를 적었는가? |
| 근거 | 문법·조건·반환·순서로 설명했는가? |
| 수정 | 한 조건만 바꾸었는가? |
| 확인 | 실제 관찰과 코드 기준 예상을 구분했는가? |

틀린 이유를 설명할 수 없다면 [본문](../../13_JavaScript_DOM_폼요소와_입력값처리.md)의 작은 예제·내 원본 풀이로 돌아간다. TIP의 미학습 기능은 이 문제의 필수 정답이 아니다.
