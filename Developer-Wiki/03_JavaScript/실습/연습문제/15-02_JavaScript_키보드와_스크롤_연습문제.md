# 15-02. 키보드와 스크롤 — 키의 정보에서 위치 변경까지 — 연습문제

[본문](../../15-02_JavaScript_키보드와_스크롤.md) · [문제 목차](README.md)

실제 수업 기능을 바탕으로 **새로 구성한 연습문제**다. 강사님 원본 퀴즈와 구분한다. 예상 → 이유 → 수정 순서로 풀고, 정답은 먼저 답한 뒤 펼친다.

## 목표와 실행 조건

keydown·keyup·이벤트 객체를 구별한다. Enter로 포커스와 클릭 처리를 연결하고, 좌표를 10px씩 바꾸는 계산을 설명한다. 스크롤할 공간과 현재 위치, scrollTo 요청의 완료 시점을 구분한다.

[전체 실행 HTML](../책형_복습/15-02_JavaScript_키보드와_스크롤.html)과 같은 폴더의 JS를 함께 준비한다. Console을 열고 새로고침하면 처음부터 실행한다. 원본과 별도 파일이므로 기존 변수·타이머·출력 변경 실험의 영향을 섞지 않는다. 실제 입력·현재 시각·난수는 고정 결과와 구별한다.

입력·버튼·키보드·스크롤 예제는 [본문의 3절](../../15-02_JavaScript_키보드와_스크롤.md#example)에 적힌 조작 순서대로 결과를 예상한다. 통신 예제는 해당 절의 가상 JSON 파일과 로컬 웹 실행 준비가 필요하며 HTML을 직접 여는 조건과 다르다. Console 출력이 없는 문제는 화면의 값·개수·선택 상태를 답한다.

## 문제 1. 실행 순서와 결과 예상

다음은 **새 설명 예제**다. 출력 전에 어떤 값이 어떤 순서로 만들어지는지 적는다.

**필요한 HTML · 스크립트 앞:**

```html
    <p><label for="user">아이디 연습</label><input id="user"></p>
    <p><label for="pw">비밀번호 연습</label><input id="pw" type="password"></p>
    <button id="check" type="button">연습 확인</button>
    <div id="game">이동 상자</div>
    <p>스크롤 위치: <span id="position">0</span></p>
    <button id="top" type="button">맨 위로</button>
```

**필요한 CSS · head의 style:**

```css
body { min-height: 250vh; } #game { position: relative; width: 100px; height: 40px; background: lightblue; } #top { position: fixed; right: 10px; bottom: 10px; }
```

```javascript
const game = document.getElementById('game');
game.style.left = '10px';
game.style.top = '20px';
document.body.addEventListener('keydown', function (event) {
    let changed = true;
    if (event.keyCode === 39) game.style.left = parseInt(game.style.left) + 10 + 'px';
    else if (event.keyCode === 37) game.style.left = parseInt(game.style.left) - 10 + 'px';
    else if (event.keyCode === 40) game.style.top = parseInt(game.style.top) + 10 + 'px';
    else if (event.keyCode === 38) game.style.top = parseInt(game.style.top) - 10 + 'px';
    else changed = false;
    if (changed) console.log(game.style.left, game.style.top);
});
document.getElementById('user').addEventListener('keyup', function (event) {
    if (event.keyCode === 13) document.getElementById('pw').focus();
});
document.getElementById('pw').addEventListener('keyup', function (event) {
    if (event.keyCode === 13) document.getElementById('check').click();
});
document.getElementById('check').addEventListener('click', function () {
    console.log('연습 확인');
});
window.addEventListener('scroll', function () {
    document.getElementById('position').textContent = window.scrollY;
});
document.getElementById('top').addEventListener('click', function () {
    window.scrollTo({ top: 0, behavior: 'smooth' });
});
```

<details>
<summary>힌트와 풀이</summary>

**힌트:** 입력·현재 상태·실행 시점·반환값을 따로 표시한다.

```text
20px 20px
20px 30px
10px 30px
10px 20px
연습 확인
```

페이지의 빈 곳에서 **오른쪽 → 아래 → 왼쪽 → 위**를 한 번씩 누른다. 좌표가 바뀌다가 시작값인 left 10px·top 20px로 돌아온다. 아이디 칸에서 Enter를 누르면 비밀번호 칸으로 포커스가 옮겨지고, 비밀번호 칸에서 Enter를 누르면 연습 확인 버튼의 클릭 처리를 호출한다. 아래로 스크롤한 뒤 맨 위로 버튼을 누르면 최종 위치가 0으로 돌아온다. 아래 Console 출력은 이 조작 순서의 결과다. 원본과 구별한 새 전체 예제이며 실제 로그인 기능은 아니다.

</details>

## 문제 2. 개념을 자신의 말로 설명

1. 내 시작 좌표에서 오른쪽과 아래를 한 번씩 누르면 어디인가?
2. scrollTo의 객체 인수는 JSON 문자열인가?
3. Ctrl+C 안내창만으로 복사를 차단했다고 할 수 있는가?

<details>
<summary>풀이</summary>

left 20px·top 30px다. scrollTo에는 문자열이 아닌 객체를 전달했다. 안내창과 기본 동작 취소는 별개이므로 복사 차단으로 단정할 수 없다.

| 원본 비교 조건 | 강사님 | 내 코드 |
| --- | --- | --- |
| 시작 left / top | 20px / 10px | 10px / 20px |
| 오른쪽 한 번 후 | 30px / 10px | 20px / 20px |
| 구현한 방향 | 오른쪽 | 네 방향 |
| 긴 스크롤 영역 | 300vh | 관련 규칙이 주석 |

keyup만으로 붙여넣기를 포함한 모든 입력 변화를 감지한다고 일반화하지 않는다. Ctrl+C 안내가 뜬 사실과 복사 이벤트의 기본 동작을 취소한 것도 별개다. 스크롤 위치를 표시하는 글자와 실제로 스크롤할 수 있는 문서 높이 역시 구분한다.

</details>

## 문제 3. 한 가지를 바꾸어 확인

먼저 **시작 left만 20px**를 바꾸면 무엇이 달라질지 적는다. 그다음 실행 파일에 해당 변경만 적용해 실제 결과와 비교한다. 나머지 실험도 원래 예제로 돌아가 하나씩 수행한다.

<details>
<summary>변경 결과와 막힐 때 확인</summary>

| 한 가지만 변경 | 예상 결과 | 이유 |
| --- | --- | --- |
| 시작 left만 20px | 오른쪽 한 번 후 30px | 초기값만 바뀜 |
| body의 긴 높이 제거 | 내용이 짧으면 스크롤이 안 보임 | 움직일 공간이 없음 |
| 오른쪽 증가량만 5로 변경 | 한 번에 5px 이동 | 입력 횟수는 같고 이동량만 바뀜 |

parseInt 결과가 NaN이면 인라인 시작값을 준비했는지 확인한다. 입력 중에도 상자가 움직이면 이벤트가 body까지 전달되는 현재 처리 범위를 살핀다. 맨 위로 버튼을 눌러도 화면이 움직이지 않으면 코드 오류를 단정하기 전에 현재 위치와 스크롤할 여지가 있는지 확인한다.

</details>

## 채점과 복습

| 점검 | 확인할 것 |
| --- | --- |
| 예측 | 실행 전에 출력·상태를 적었는가? |
| 근거 | 문법·조건·반환·순서로 설명했는가? |
| 수정 | 한 조건만 바꾸었는가? |
| 확인 | 실제 관찰과 코드 기준 예상을 구분했는가? |

틀린 이유를 설명할 수 없다면 [본문](../../15-02_JavaScript_키보드와_스크롤.md)의 작은 예제·내 원본 풀이로 돌아간다. TIP의 미학습 기능은 이 문제의 필수 정답이 아니다.
