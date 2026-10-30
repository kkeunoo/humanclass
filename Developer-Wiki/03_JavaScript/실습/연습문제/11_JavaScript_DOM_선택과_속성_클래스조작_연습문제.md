# 11. DOM 선택 — 요소 하나와 목록부터 구분하기 — 연습문제

[본문](../../11_JavaScript_DOM_선택과_속성_클래스조작.md) · [문제 목차](README.md)

실제 수업 기능을 바탕으로 **새로 구성한 연습문제**다. 강사님 원본 퀴즈와 구분한다. 예상 → 이유 → 수정 순서로 풀고, 정답은 먼저 답한 뒤 펼친다.

## 목표와 실행 조건

DOM 선택 함수의 기준·반환·없을 때 결과를 비교한다. 찾는 범위와 실행 시점, 빈 목록의 참거짓을 설명한다.

[전체 실행 HTML](../책형_복습/11_JavaScript_DOM_선택과_속성_클래스조작.html)과 같은 폴더의 JS를 함께 준비한다. Console을 열고 새로고침하면 처음부터 실행한다. 원본과 별도 파일이므로 기존 변수·타이머·출력 변경 실험의 영향을 섞지 않는다. 실제 입력·현재 시각·난수는 고정 결과와 구별한다.

입력·버튼·키보드·스크롤 예제는 [본문의 3절](../../11_JavaScript_DOM_선택과_속성_클래스조작.md#example)에 적힌 조작 순서대로 결과를 예상한다. 통신 예제는 해당 절의 가상 JSON 파일과 로컬 웹 실행 준비가 필요하며 HTML을 직접 여는 조건과 다르다. Console 출력이 없는 문제는 화면의 값·개수·선택 상태를 답한다.

## 문제 1. 실행 순서와 결과 예상

다음은 **새 설명 예제**다. 출력 전에 어떤 값이 어떤 순서로 만들어지는지 적는다.

**필요한 HTML · 스크립트 앞:**

```html
    <div id="panel">
        <h2 id="book-title">안녕</h2>
        <p class="note">첫째</p>
        <p class="note">둘째</p>
    </div>
```

```javascript
const title = document.getElementById('book-title');
console.log(title.textContent);
const notes = document.querySelectorAll('#panel .note');
console.log(notes.length);
console.log(notes[0].textContent);
console.log(document.querySelector('.missing'));
const missing = document.querySelectorAll('.missing');
console.log(missing.length);
if (missing) {
    console.log('목록 객체 있음');
}
```

<details>
<summary>힌트와 풀이</summary>

**힌트:** 입력·현재 상태·실행 시점·반환값을 따로 표시한다.

```text
안녕
2
첫째
null
0
목록 객체 있음
```

title은 h2 하나이고 notes는 두 p의 목록이다. notes[0]은 첫 요소이며 그 textContent는 첫째다. 단일 선택의 missing은 null, 전체 선택은 길이0인 목록이다. 마지막 if는 원소가 있어서가 아니라 목록 객체가 존재해 실행된다. 스크립트는 이 HTML이 만들어진 뒤 연결한다.

</details>

## 문제 2. 개념을 자신의 말로 설명

1. querySelector와 All이 못 찾았을 때 각각 무엇인가?
2. 빈 목록이 참이면 원소도 있는가?
3. 부모 안 검색과 document 검색은 같은가?

<details>
<summary>풀이</summary>

null과 길이0 목록이다. 목록 객체가 참이라는 것과 원소 수는 별개다. 검색 범위가 달라 개수도 다를 수 있다.

| 원본 변수 | 결과 | 조건 |
| --- | --- | --- |
| view2 |두 번째 view |#view.pizza 두 조건 |
| view3 |첫 번째 view |div#view 첫 일치 |
| view4 |null |해당 요소 없음 |
| qsa |NodeList 2개 |#view 전체 일치 |

getElementsByTagName/ClassName의 HTMLCollection은 문서 변경을 반영한다. 원본 divs는 처음4개지만 뒤 div2.remove() 후3개다. querySelectorAll 목록은 선택 당시의 목록이며 그 안 요소의 속성 변경까지 멈추는 것은 아니다. 뒤 장의 remove를 배운 후 연결해 다시 확인한다.

</details>

## 문제 3. 한 가지를 바꾸어 확인

먼저 **첫선택ID만없는값으로**를 바꾸면 무엇이 달라질지 적는다. 그다음 실행 파일에 해당 변경만 적용해 실제 결과와 비교한다. 나머지 실험도 원래 예제로 돌아가 하나씩 수행한다.

<details>
<summary>변경 결과와 막힐 때 확인</summary>

| 한 가지 변경 | 예상 | 이유 |
| --- | --- | --- |
| 첫선택ID만없는값으로 |null속성읽기오류 |존재확인필요 |
| notes선택자만#panel로 |목록길이1 |부모하나선택 |
| 마지막if를missing.length>0으로 |마지막문구없음 |원소수검사 |

null이면 ID·선택자 철자·검색 범위·script 실행 시점을 본다. 목록에 바로 textContent를 읽는 대신 필요한 원소를 선택하거나 반복한다. 스크립트를 요소 앞으로 옮기면 아직 요소가 없어 결과가 달라질 수 있다.

</details>

## 채점과 복습

| 점검 | 확인할 것 |
| --- | --- |
| 예측 | 실행 전에 출력·상태를 적었는가? |
| 근거 | 문법·조건·반환·순서로 설명했는가? |
| 수정 | 한 조건만 바꾸었는가? |
| 확인 | 실제 관찰과 코드 기준 예상을 구분했는가? |

틀린 이유를 설명할 수 없다면 [본문](../../11_JavaScript_DOM_선택과_속성_클래스조작.md)의 작은 예제·내 원본 풀이로 돌아간다. TIP의 미학습 기능은 이 문제의 필수 정답이 아니다.
