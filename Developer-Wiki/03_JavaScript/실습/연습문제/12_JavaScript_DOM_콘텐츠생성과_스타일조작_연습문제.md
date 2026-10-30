# 12. DOM 콘텐츠 — 글자·HTML·숫자·현재 시각 — 연습문제

[본문](../../12_JavaScript_DOM_콘텐츠생성과_스타일조작.md) · [문제 목차](README.md)

실제 수업 기능을 바탕으로 **새로 구성한 연습문제**다. 강사님 원본 퀴즈와 구분한다. 예상 → 이유 → 수정 순서로 풀고, 정답은 먼저 답한 뒤 펼친다.

## 목표와 실행 조건

textContent·innerText·innerHTML을 구분한다. 화면 문자열의 숫자 변환과 반복마다 Date를 새로 만드는 이유를 설명한다.

[전체 실행 HTML](../책형_복습/12_JavaScript_DOM_콘텐츠생성과_스타일조작.html)과 같은 폴더의 JS를 함께 준비한다. Console을 열고 새로고침하면 처음부터 실행한다. 원본과 별도 파일이므로 기존 변수·타이머·출력 변경 실험의 영향을 섞지 않는다. 실제 입력·현재 시각·난수는 고정 결과와 구별한다.

입력·버튼·키보드·스크롤 예제는 [본문의 3절](../../12_JavaScript_DOM_콘텐츠생성과_스타일조작.md#example)에 적힌 조작 순서대로 결과를 예상한다. 통신 예제는 해당 절의 가상 JSON 파일과 로컬 웹 실행 준비가 필요하며 HTML을 직접 여는 조건과 다르다. Console 출력이 없는 문제는 화면의 값·개수·선택 상태를 답한다.

## 문제 1. 실행 순서와 결과 예상

다음은 **새 설명 예제**다. 출력 전에 어떤 값이 어떤 순서로 만들어지는지 적는다.

**필요한 HTML · 스크립트 앞:**

```html
    <div id="plain"></div>
    <div id="markup"></div>
    <p id="count">0</p>
```

```javascript
const plain = document.getElementById('plain');
const markup = document.getElementById('markup');
plain.textContent = '<b>안녕</b>';
markup.innerHTML = '<b>안녕</b>';
console.log(plain.textContent);
console.log(markup.textContent);
console.log(markup.querySelector('b') !== null);
const count = document.getElementById('count');
console.log(count.textContent + 1);
count.textContent = Number(count.textContent) + 1;
console.log(count.textContent);
```

<details>
<summary>힌트와 풀이</summary>

**힌트:** 입력·현재 상태·실행 시점·반환값을 따로 표시한다.

```text
<b>안녕</b>
안녕
true
01
1
```

두 영역에 같은 문자열을 넣었지만 plain은 태그 모양의 글자, markup은 실제 b 요소가 된다. markup 안의 b를 선택해 null이 아님을 확인했다. count를 읽으면 문자열0이므로 첫 덧셈은01이다. Number 뒤 대입은 숫자1을 화면 글자로 써 최종1이 된다.

</details>

## 문제 2. 개념을 자신의 말로 설명

1. 태그 모양을 글자 그대로 넣으려면?
2. 카운터에서 읽은 값은 숫자인가?
3. Date를 반복 밖에서 한 번만 만들면 현재 시각이 자동 갱신되는가?

<details>
<summary>풀이</summary>

textContent 등 텍스트 속성을 쓴다. 읽은 값은 문자열이라 숫자 계산 전 변환한다. 새 순간을 얻으려면 반복 안마다 다시 Date를 만든다.

| 원본 단계 | 그때 내용 | 다음 대입 뒤 유지? |
| --- | --- | --- |
| textContent |h1 모양 글자 |교체됨 |
| innerText |h1 모양 글자 |교체됨 |
| innerHTML |h1 요소 |뒤 링크 대입으로 교체 |
| 마지막 HTML |눌러봐 링크 |최종 남음 |

원본 javascript: 링크는 클릭 시 alert를 실행하는 주소다. 글을 넣는 방법을 무조건 게시글 저장 기능과 같다고 생각하지 않는다. 단순 카운터는 '0'→0→1→화면 '1'의 변환으로 설명한다.

</details>

## 문제 3. 한 가지를 바꾸어 확인

먼저 **plain속성만innerHTML로**를 바꾸면 무엇이 달라질지 적는다. 그다음 실행 파일에 해당 변경만 적용해 실제 결과와 비교한다. 나머지 실험도 원래 예제로 돌아가 하나씩 수행한다.

<details>
<summary>변경 결과와 막힐 때 확인</summary>

| 한 가지 변경 | 예상 | 이유 |
| --- | --- | --- |
| plain속성만innerHTML로 |두영역모두b요소 |해석방식변경 |
| 원래markup속성만textContent로 |b선택false |텍스트로넣음 |
| 원래count대입의Number만제거 |마지막01 |문자열연결 |

태그가 글자로 보이면 텍스트 대입을 확인한다. 반대로 사용자 글이 태그가 되면 HTML 해석 경로를 본다. 숫자 카운터가011처럼 이어지면 Number 변환이 있는지 확인한다. 시계가 멈추면 Date 생성 위치를 본다.

</details>

## 채점과 복습

| 점검 | 확인할 것 |
| --- | --- |
| 예측 | 실행 전에 출력·상태를 적었는가? |
| 근거 | 문법·조건·반환·순서로 설명했는가? |
| 수정 | 한 조건만 바꾸었는가? |
| 확인 | 실제 관찰과 코드 기준 예상을 구분했는가? |

틀린 이유를 설명할 수 없다면 [본문](../../12_JavaScript_DOM_콘텐츠생성과_스타일조작.md)의 작은 예제·내 원본 풀이로 돌아간다. TIP의 미학습 기능은 이 문제의 필수 정답이 아니다.
