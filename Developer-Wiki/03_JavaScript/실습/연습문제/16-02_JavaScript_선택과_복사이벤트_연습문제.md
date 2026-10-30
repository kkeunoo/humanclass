# 16-02. 선택과 복사 — 기본 동작을 취소하고 데이터를 지정하기 — 연습문제

[본문](../../16-02_JavaScript_선택과_복사이벤트.md) · [문제 목차](README.md)

실제 수업 기능을 바탕으로 **새로 구성한 연습문제**다. 강사님 원본 퀴즈와 구분한다. 예상 → 이유 → 수정 순서로 풀고, 정답은 먼저 답한 뒤 펼친다.

## 목표와 실행 조건

선택 내용 읽기 → 빈 선택 검사 → 문자열 만들기 → 복사 데이터 지정 흐름을 설명한다. return·preventDefault와 이벤트 처리 방식의 차이, innerWidth·innerHeight의 기준을 구분한다.

[전체 실행 HTML](../책형_복습/16-02_JavaScript_선택과_복사이벤트.html)과 같은 폴더의 JS를 함께 준비한다. Console을 열고 새로고침하면 처음부터 실행한다. 원본과 별도 파일이므로 기존 변수·타이머·출력 변경 실험의 영향을 섞지 않는다. 실제 입력·현재 시각·난수는 고정 결과와 구별한다.

입력·버튼·키보드·스크롤 예제는 [본문의 3절](../../16-02_JavaScript_선택과_복사이벤트.md#example)에 적힌 조작 순서대로 결과를 예상한다. 통신 예제는 해당 절의 가상 JSON 파일과 로컬 웹 실행 준비가 필요하며 HTML을 직접 여는 조건과 다르다. Console 출력이 없는 문제는 화면의 값·개수·선택 상태를 답한다.

## 문제 1. 실행 순서와 결과 예상

다음은 **새 설명 예제**다. 출력 전에 어떤 값이 어떤 순서로 만들어지는지 적는다.

**필요한 HTML · 스크립트 앞:**

```html
    <p id="area" tabindex="0">복사 연습</p>
    <button id="preview" type="button">문자열 결과 미리 보기</button>
    <p id="result"></p>
    <p id="size">창 크기를 바꾸면 표시합니다.</p>
```

```javascript
const area = document.getElementById('area');
function makeCopyText(selection) {
    return selection + '[출처] www.naver.com';
}
document.getElementById('preview').addEventListener('click', function () {
    const result = makeCopyText('복사 연습');
    document.getElementById('result').textContent = result;
    console.log(result);
});
area.addEventListener('copy', function (event) {
    event.preventDefault();
    const selection = window.getSelection().toString();
    if (selection.length === 0) return;
    event.clipboardData.setData('text/plain', makeCopyText(selection));
});
window.addEventListener('resize', function () {
    document.getElementById('size').textContent =
        '가로 ' + window.innerWidth + ', 세로 ' + window.innerHeight;
});
```

<details>
<summary>힌트와 풀이</summary>

**힌트:** 입력·현재 상태·실행 시점·반환값을 따로 표시한다.

```text
복사 연습[출처] www.naver.com
```

먼저 미리 보기 버튼을 누르면 같은 문자열 처리 함수를 호출해 결과를 화면과 Console에 보여 준다. 이 버튼은 클립보드에 쓰지 않는다. 별도로 area의 글자를 선택하고 복사하면 copy 리스너가 선택 내용을 읽어 이번 복사 데이터를 지정한다. 함수 makeCopyText는 문자열을 받아 출처 문구를 붙인 문자열을 반환한다. 함수 정의·미리 보기 호출·복사 처리 호출을 모두 실어 연결을 따라갈 수 있게 했다. 자동 검증은 미리 보기 결과를 확인했으며, 운영체제 클립보드에 실제로 복사한 것으로 보고하지 않는다.

</details>

## 문제 2. 개념을 자신의 말로 설명

1. 빈 선택이면 기본 복사가 취소되기 전인가, 후인가?
2. makeCopyText는 클립보드에 직접 쓰는가?
3. innerHeight는 문서 전체 콘텐츠 높이인가?

<details>
<summary>풀이</summary>

이미 취소한 뒤 return으로 끝난다. makeCopyText는 문자열을 반환할 뿐이며 실제 데이터 지정은 copy 리스너의 setData가 한다. innerHeight는 뷰포트 안쪽 높이로 문서 전체 높이와 다르다.

| 순서 | 선택이 '복사 연습'인 경우 | 빈 선택인 경우 |
| --- | --- | --- |
| preventDefault | 기본 복사 취소 | 기본 복사 취소 |
| 선택 글자 읽기 | '복사 연습' | '' |
| 길이 검사 | 계속 진행 | return으로 종료 |
| setData | 출처를 붙인 문자열 지정 | 실행하지 않음 |

15장의 Ctrl+C 안내창은 키 조합을 보고 알림을 띄운다. 이 장의 copy 처리는 복사 사건의 기본 동작을 취소하고 데이터를 지정한다. 같은 키를 눌렀을 때 보였다는 이유로 두 처리를 같은 기능이라고 설명하지 않는다.

</details>

## 문제 3. 한 가지를 바꾸어 확인

먼저 **출처 앞에 공백 한 칸 추가**를 바꾸면 무엇이 달라질지 적는다. 그다음 실행 파일에 해당 변경만 적용해 실제 결과와 비교한다. 나머지 실험도 원래 예제로 돌아가 하나씩 수행한다.

<details>
<summary>변경 결과와 막힐 때 확인</summary>

| 한 가지만 변경 | 예상 결과 | 확인 지점 |
| --- | --- | --- |
| 출처 앞에 공백 한 칸 추가 | 결과 사이에도 공백 추가 | 문자열 그대로 연결 |
| 미리 보기 인수를 '연습'으로 변경 | 연습 뒤에 출처 문구 | 함수 입력과 반환 |
| resize 대신 최초 한 번 크기 읽기 | 이후 크기 변경은 반영 안 됨 | 관찰 시점과 등록의 차이 |

출처가 붙지 않으면 글자를 선택한 영역과 copy 등록 대상을 확인한다. 빈 선택이면 원본은 setData 전에 끝난다. 미리 보기 버튼으로 출력만 확인했다고 실제 복사가 완료되었다고 판단하지 않는다. 창 크기가 처음 안 보이면 resize가 실제 발생했는지 확인한다.

</details>

## 채점과 복습

| 점검 | 확인할 것 |
| --- | --- |
| 예측 | 실행 전에 출력·상태를 적었는가? |
| 근거 | 문법·조건·반환·순서로 설명했는가? |
| 수정 | 한 조건만 바꾸었는가? |
| 확인 | 실제 관찰과 코드 기준 예상을 구분했는가? |

틀린 이유를 설명할 수 없다면 [본문](../../16-02_JavaScript_선택과_복사이벤트.md)의 작은 예제·내 원본 풀이로 돌아간다. TIP의 미학습 기능은 이 문제의 필수 정답이 아니다.
