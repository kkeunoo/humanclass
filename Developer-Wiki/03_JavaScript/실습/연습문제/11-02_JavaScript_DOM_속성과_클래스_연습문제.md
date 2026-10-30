# 11-02. 속성과 클래스 — 읽기·변경·제거의 대상 — 연습문제

[본문](../../11-02_JavaScript_DOM_속성과_클래스.md) · [문제 목차](README.md)

실제 수업 기능을 바탕으로 **새로 구성한 연습문제**다. 강사님 원본 퀴즈와 구분한다. 예상 → 이유 → 수정 순서로 풀고, 정답은 먼저 답한 뒤 펼친다.

## 목표와 실행 조건

속성 존재·값·쓰기·제거를 구분한다. dataset과 classList의 연속 상태, 클래스 제거와 요소 제거를 설명한다.

[전체 실행 HTML](../책형_복습/11-02_JavaScript_DOM_속성과_클래스.html)과 같은 폴더의 JS를 함께 준비한다. Console을 열고 새로고침하면 처음부터 실행한다. 원본과 별도 파일이므로 기존 변수·타이머·출력 변경 실험의 영향을 섞지 않는다. 실제 입력·현재 시각·난수는 고정 결과와 구별한다.

입력·버튼·키보드·스크롤 예제는 [본문의 3절](../../11-02_JavaScript_DOM_속성과_클래스.md#example)에 적힌 조작 순서대로 결과를 예상한다. 통신 예제는 해당 절의 가상 JSON 파일과 로컬 웹 실행 준비가 필요하며 HTML을 직접 여는 조건과 다르다. Console 출력이 없는 문제는 화면의 값·개수·선택 상태를 답한다.

## 문제 1. 실행 순서와 결과 예상

다음은 **새 설명 예제**다. 출력 전에 어떤 값이 어떤 순서로 만들어지는지 적는다.

**필요한 HTML · 스크립트 앞:**

```html
    <p id="notice" class="message" data-name="공지">안내</p>
```

**필요한 CSS · head의 style:**

```css
        .blue { color: blue; }
```

```javascript
const notice = document.getElementById('notice');
console.log(notice.hasAttribute('data-name'));
console.log(notice.getAttribute('data-name'));
console.log(notice.dataset.name);
notice.classList.add('blue');
notice.classList.add('blue');
console.log(notice.classList.contains('blue'));
notice.classList.toggle('blue');
console.log(notice.classList.contains('blue'));
notice.dataset.minsu = '학생';
console.log(notice.getAttribute('data-minsu'));
```

<details>
<summary>힌트와 풀이</summary>

**힌트:** 입력·현재 상태·실행 시점·반환값을 따로 표시한다.

```text
true
공지
공지
true
false
학생
```

data-name이 존재해 true, 두 읽기 방식 모두 공지를 얻는다. blue는 두 번 추가해도 하나이고 toggle로 제거해 최종 false다. 중간의 파란 화면이 매 단계 보인다고 보장하지 않고 최종 상태와 Console을 본다. 마지막 대입은 data-minsu 속성에 학생을 쓴다.

</details>

## 문제 2. 개념을 자신의 말로 설명

1. 문자열 값을 주는 속성 읽기는?
2. blue가 없는 상태에서 toggle 두 번 후는?
3. remove 후 변수는 자동 null인가?

<details>
<summary>풀이</summary>

getAttribute이며 없는 속성은 null이다. toggle 두 번이면 다시 없다. 요소가 분리되어도 변수 참조는 자동 null이 아니다.

| 원본 blue 조작 직후 | 상태 |
| --- | --- |
| add·add |있음·중복 없음 |
| remove·remove |없음·그대로 |
| toggle |있음 |
| 다시 toggle |없음 |
| contains |false·변경 없음 |

하나의 스크립트가 바로 실행되면 중간 색들이 화면에 차례로 보이지 않을 수 있다. 중간 상태 검사는 출력으로, 최종 표시는 최종 클래스로 구분한다.

</details>

## 문제 3. 한 가지를 바꾸어 확인

먼저 **작은예제toggle만제거**를 바꾸면 무엇이 달라질지 적는다. 그다음 실행 파일에 해당 변경만 적용해 실제 결과와 비교한다. 나머지 실험도 원래 예제로 돌아가 하나씩 수행한다.

<details>
<summary>변경 결과와 막힐 때 확인</summary>

| 한 가지 변경 | 예상 | 이유 |
| --- | --- | --- |
| 작은예제toggle만제거 |contains둘다true |blue유지 |
| 원래data-name값만복습으로 |두읽기결과복습 |같은속성 |
| 원래CSS.blue규칙만제거 |class결과는같음 |표시와속성분리 |

속성값 null과 존재 검사 false를 혼동하지 않는다. 색이 그대로라고 class 추가 실패부터 판단하지 말고 CSS 규칙·우선순위·최종 클래스를 본다. 요소가 없으면 속성 메서드를 호출하기 전 선택 결과를 확인한다.

</details>

## 채점과 복습

| 점검 | 확인할 것 |
| --- | --- |
| 예측 | 실행 전에 출력·상태를 적었는가? |
| 근거 | 문법·조건·반환·순서로 설명했는가? |
| 수정 | 한 조건만 바꾸었는가? |
| 확인 | 실제 관찰과 코드 기준 예상을 구분했는가? |

틀린 이유를 설명할 수 없다면 [본문](../../11-02_JavaScript_DOM_속성과_클래스.md)의 작은 예제·내 원본 풀이로 돌아간다. TIP의 미학습 기능은 이 문제의 필수 정답이 아니다.
