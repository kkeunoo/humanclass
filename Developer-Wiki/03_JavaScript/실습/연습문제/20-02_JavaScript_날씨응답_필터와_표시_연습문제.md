# 20-02. 날씨 응답 — 항목을 고르는 일과 같은 시각으로 묶는 일 — 연습문제

[본문](../../20-02_JavaScript_날씨응답_필터와_표시.md) · [문제 목차](README.md)

실제 수업 기능을 바탕으로 **새로 구성한 연습문제**다. 강사님 원본 퀴즈와 구분한다. 예상 → 이유 → 수정 순서로 풀고, 정답은 먼저 답한 뒤 펼친다.

## 목표와 실행 조건

중첩 응답에서 item 배열을 찾고 filter 조건을 설명한다. 시각을 객체 키로 묶는 계산을 따라가며, 한 항목당 행과 한 시각당 행의 차이를 비교한다. 표의 tr·td 구조도 확인한다.

[전체 실행 HTML](../책형_복습/20-02_JavaScript_날씨응답_필터와_표시.html)과 같은 폴더의 JS를 함께 준비한다. Console을 열고 새로고침하면 처음부터 실행한다. 원본과 별도 파일이므로 기존 변수·타이머·출력 변경 실험의 영향을 섞지 않는다. 실제 입력·현재 시각·난수는 고정 결과와 구별한다.

입력·버튼·키보드·스크롤 예제는 [본문의 3절](../../20-02_JavaScript_날씨응답_필터와_표시.md#example)에 적힌 조작 순서대로 결과를 예상한다. 통신 예제는 해당 절의 가상 JSON 파일과 로컬 웹 실행 준비가 필요하며 HTML을 직접 여는 조건과 다르다. Console 출력이 없는 문제는 화면의 값·개수·선택 상태를 답한다.

## 문제 1. 실행 순서와 결과 예상

다음은 **새 설명 예제**다. 출력 전에 어떤 값이 어떤 순서로 만들어지는지 적는다.

**필요한 HTML · 스크립트 앞:**

```html
    <table><thead><tr><th>시각</th><th>T1H</th><th>REH</th><th>RN1</th></tr></thead><tbody id="rows"></tbody></table>
```

**필요한 CSS · head의 style:**

```css
table { border-collapse: collapse; } th, td { border: 1px solid #777; padding: 8px; }
```

```javascript
const data = { response: { body: { items: { item: [
    { category: 'T1H', fcstTime: '0900', fcstValue: '25' },
    { category: 'REH', fcstTime: '0900', fcstValue: '70' },
    { category: 'RN1', fcstTime: '0900', fcstValue: '1' },
    { category: 'LGT', fcstTime: '0900', fcstValue: '0' },
    { category: 'T1H', fcstTime: '1000', fcstValue: '26' },
    { category: 'REH', fcstTime: '1000', fcstValue: '65' },
    { category: 'RN1', fcstTime: '1000', fcstValue: '0' }
] } } } };
const items = data.response.body.items.item;
const selected = items.filter(function (item) {
    return item.category === 'T1H' || item.category === 'REH' || item.category === 'RN1';
});
const groups = {};
for (const item of selected) {
    if (!groups[item.fcstTime]) groups[item.fcstTime] = {};
    groups[item.fcstTime][item.category] = item.fcstValue;
}
const times = Object.keys(groups).sort();
const rows = document.getElementById('rows');
rows.innerHTML = '';
for (const time of times) {
    const values = [time, groups[time].T1H, groups[time].REH, groups[time].RN1];
    const row = document.createElement('tr');
    for (const value of values) {
        const cell = document.createElement('td');
        cell.textContent = value === undefined ? '-' : value;
        row.append(cell);
    }
    rows.append(row);
    console.log(values.join(' | '));
}
console.log('원본 항목', items.length, '선택 항목', selected.length, '표 행', times.length);
```

<details>
<summary>힌트와 풀이</summary>

**힌트:** 입력·현재 상태·실행 시점·반환값을 따로 표시한다.

```text
0900 | 25 | 70 | 1
1000 | 26 | 65 | 0
원본 항목 7 선택 항목 6 표 행 2
```

실제 API 응답이 아닌 가상 객체를 코드 안에 넣어 네트워크 없이 실행한다. 전체 7개에서 LGT 하나를 제외하면 6개다. 같은 시각별로 묶으면 0900·1000의 두 객체가 되고 행도 2개다. 배열의 항목 수와 표 행 수가 달라진 이유를 설명할 수 있어야 한다. times.sort는 앞 장에서 배운 문자열 정렬로 네 자리 시각을 정리한 개선이다. Object.keys의 결과가 언제나 시간순이라고 가정하지 않는다. 빠진 종류는 -로 표시하며 실제 측정값 0과 구분한다.

</details>

## 문제 2. 개념을 자신의 말로 설명

1. filter는 같은 시각의 세 항목을 한 개로 합치는가?
2. groups[time][category]의 두 대괄호는 무엇을 고르는가?
3. 빠진 강수량과 강수량 0은 같은가?
4. 만든 td를 넣을 대상은 tbody인가, 해당 tr인가?

<details>
<summary>풀이</summary>

합치지 않고 조건에 맞는 항목만 남긴다. 첫 대괄호는 시각별 객체, 다음은 그 안의 종류 속성을 고른다. 누락과 0은 다르다. 셀은 해당 tr 안에 넣고 행을 tbody에 붙인다.

| 처리한 항목 | groups의 변화 |
| --- | --- |
| 0900 T1H 25 | 0900 객체 생성, T1H='25' |
| 0900 REH 70 | 같은 0900에 REH='70' 추가 |
| 0900 RN1 1 | 같은 0900에 RN1='1' 추가 |
| LGT 0 | 필터에서 제외되어 그룹 처리 안 함 |
| 1000 세 항목 | 별도 1000 객체에 값 저장 |

이 연습은 같은 예측 날짜의 한 묶음을 가정한다. 여러 날짜를 시간만으로 묶으면 같은 시각이 덮일 수 있다. 누락 종류와 중복 항목도 실제 응답 조건을 따로 확인해야 한다. 원본 키·전체 요청 URL은 싣지 않았고 이번에 외부 날씨 요청도 실행하지 않았다. 여기 숫자는 표 구조를 설명하는 가상 값으로 실제 날씨가 아니다.

</details>

## 문제 3. 한 가지를 바꾸어 확인

먼저 **1000 RN1 항목 제거**를 바꾸면 무엇이 달라질지 적는다. 그다음 실행 파일에 해당 변경만 적용해 실제 결과와 비교한다. 나머지 실험도 원래 예제로 돌아가 하나씩 수행한다.

<details>
<summary>변경 결과와 막힐 때 확인</summary>

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| 1000 RN1 항목 제거 | 둘째 행 강수 칸 - | 누락과 0을 구분 |
| LGT 필터 조건 추가 | 선택 항목 증가 | 표 열 구성은 자동 추가되지 않음 |
| rows 비우기 제거 후 같은 출력 반복 | 행 누적 가능 | 기존 DOM이 남음 |
| 그룹 없이 selected 반복 | 항목당 한 행 | 시간별 묶음이 아님 |

세 값이 한 행에 안 모이면 filter 뒤 자료구조부터 본다. 모든 칸이 기온이면 각 조건과 대입 값을 확인한다. 반복 실행 때 늘어나면 기존 출력 영역을 비웠는지 본다. 응답 경로 오류면 중간 객체가 실제로 있는지 확인하고 임의로 JSON.parse를 반복 호출하지 않는다.

</details>

## 채점과 복습

| 점검 | 확인할 것 |
| --- | --- |
| 예측 | 실행 전에 출력·상태를 적었는가? |
| 근거 | 문법·조건·반환·순서로 설명했는가? |
| 수정 | 한 조건만 바꾸었는가? |
| 확인 | 실제 관찰과 코드 기준 예상을 구분했는가? |

틀린 이유를 설명할 수 없다면 [본문](../../20-02_JavaScript_날씨응답_필터와_표시.md)의 작은 예제·내 원본 풀이로 돌아간다. TIP의 미학습 기능은 이 문제의 필수 정답이 아니다.
