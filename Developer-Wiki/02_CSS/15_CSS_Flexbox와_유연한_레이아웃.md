# 15. Flexbox — 부모 축과 자식 크기·순서

[CSS 목차](README.md) · [읽기 안내](00_CSS_V3_동작_백과_읽기법.md)

부모가 직접 자식들을 한 축 중심으로 배치하는 방식이 Flexbox다. 부모의 정렬 설정과 자식의 크기·순서 설정을 나누어 읽어야 한다. 주석 실험을 전부 켜 놓은 것처럼 읽지 않는다.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [작은 예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

주축·교차축·정렬·줄바꿈을 설명한다. 원본 order 순서를 예상하고 grow·shrink가 언제 차이를 만드는지 조건을 확인한다.

이번 장의 개념과 원본 기능은 수업 범위다. 원본에 없는 선택 기능은 9절 TIP으로 구분한다. 결과를 읽을 때는 선택된 요소·속성·기준값·실행 상태를 함께 적는다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

display:flex를 부모에 주면 직접 자식이 Flex 항목이 된다. 기본 row인 이번 가로쓰기 조건에서는 주축이 가로, 교차축이 세로다. column으로 바꾸면 주축이 세로가 되어 정렬 속성을 읽는 방향도 바뀐다. row를 모든 쓰기 방향에서 항상 왼쪽→오른쪽이라고 일반화하지 않는다.

| 부모 속성 | 무엇을 정하는가? |
| --- | --- |
| flex-direction | 주축 방향 |
| flex-wrap | 한 줄 유지 또는 여러 줄 |
| justify-content | 주축의 남은 공간 배분 |
| align-items | 각 줄 안 교차축 항목 정렬 |
| align-content | 여러 줄의 교차축 여유 공간 배분 |

space-between은 양 끝을 붙이고 사이를 나눈다. space-around는 항목 양옆 공간이라 안쪽 간격이 끝의 두 배가 될 수 있고, space-evenly는 끝과 사이를 같게 나눈다. 나눌 남은 공간이 있는지도 먼저 본다.

자식의 order는 작은 수부터 시각 순서를 정하고 같은 값이면 원본 순서를 따른다. HTML 자체 순서를 바꾸지는 않는다. grow는 남는 공간, shrink는 부족 공간 분배와 관련 있지만 숫자가 곧 최종 너비 비율이라는 뜻은 아니다. 기준 크기와 min/max 제한도 영향을 준다.

> 📚 **출처 · 본문 설명 확인:** [W3C Flexbox](https://www.w3.org/TR/css-flexbox-1/). 설명과 비교 표는 수업 원본을 바탕으로 새로 풀어 썼다. 외부 원문을 직접 인용한 문장은 아니다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 파일.** [실행 파일](실습/책형_복습/15_CSS_Flexbox와_유연한_레이아웃.html)을 브라우저로 연다. 이 예제는 위 style 안에 CSS를 모두 넣어 외부 파일 연결이 필요 없다. 원본 CSS에 붙이면 다른 규칙이 섞일 수 있으므로 먼저 별도 파일로 확인한다.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>15. Flexbox — 부모 축과 자식 크기·순서</title>
    <style>
        .container { display: flex; flex-direction: row; width: 300px; height: 120px; justify-content: center; align-items: center; border: 1px solid black; }
        .item { width: 50px; height: 40px; border: 1px solid red; box-sizing: border-box; }
    </style>
</head>
<body>
    <h1>축과 순서</h1>
    <div class="container">
        <div class="item">1</div>
        <div class="item" style="order: 1">2</div>
        <div class="item" style="order: -1">3</div>
    </div>
</body>
</html>
```

항목 너비 합 150px에 남은 150px를 양쪽 75px로 두고 가운데 모인다. 높이 120px 안의 40px 항목은 교차축 중앙으로 가서 위아래 40px가 남는다. 시각 순서는 3·1·2다. 항목이 부모보다 작고 명시적 크기가 있으며 별도 margin·gap이 없는 조건에서 계산했다.

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 **내 원본 발췌**다. 주석의 표현도 원문대로 두었다. 설명에서 교정한 내용을 원본에 이미 수정한 것처럼 읽지 않는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/css/15_flex.html` 95–101행

```html
    <div class="container">
        <div class="item">1</div>
        <div class="item" style="order: 1">2</div>
        <div class="item" style="order: -1">3</div>
        <div class="item" style="flex-grow: 0; flex-shrink: 3; min-width: 50px;">4</div>
        <div class="item" style="flex-grow: 0; flex-shrink: 2;">5</div>
    </div>
```

**발췌 바로 풀이:** 순서는 order 작은 값부터이므로 화면 왼쪽부터 **3 → 1 → 4 → 5 → 2**다. 같은 order에서는 원본 순서를 따른다. HTML 자체의 순서가 바뀐 것은 아니다. order를 읽기 순서를 마음대로 고치는 도구로 사용하지 않는다.

현재 원본 container는 300×300px·flex·row다. wrap·정렬 실험 대부분과 item width는 주석이다. 다섯 항목의 order는 3번 -1, 2번 1, 나머지 0이어서 3→1→4→5→2다. 4·5번 grow는 0, shrink는 3·2지만 공간 부족이 없으면 축소 차이도 보이지 않는다. 4번의 min-width:50px도 조건에 포함한다.

<a id="connections"></a>

## 5. 파일·요소·값이 연결되는 흐름

부모 display → 주축 방향 → 줄바꿈 상태 → 직접 자식의 order와 크기 → 남는 공간 또는 부족 공간 → 정렬 순서로 읽는다. nowrap인 한 줄 컨테이너에서 align-content가 변화 없다면 오타부터 고치지 말고 여러 줄 조건을 본다. 실제 원본 width 주석을 해제해 100px 항목과 wrap을 비교하는 실험은 현재 실행 상태와 구별해 적는다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 부모 실험과 자식 인라인 설정을 한 파일에서 비교할 수 있다. **아쉬운 점:** 주석과 활성값을 구분하지 않으면 원래 화면을 다르게 예상한다. **개선 방향:** 한 축·한 속성씩 켜고 현재 조건을 기록한다. order를 논리적 읽기 순서를 마음대로 고치는 도구로 사용하지 않는다.

제안은 원본을 수정한 결과가 아니다. **실제 오류**, **관찰을 위한 수업용 단순화**, **목적에 따라 가능한 선택**을 구별한다. 단지 짧게 쓰거나 최신 기능을 쓴다고 더 좋은 코드는 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



양쪽 파일이 같아 중복 인용을 생략했다. 동일 코드의 주석 실험은 수업 관찰 근거가 되지만, 현재 모든 정렬이 켜진 결과로 설명하지 않는다. align-items와 justify-content의 축을 바꾸어 설명하면 틀린다.

<a id="results"></a>

## 8. 결과를 예상하고 한 가지 바꾸기

아래는 **명시한 조건에서의 코드 기준 예상**이다. 이번 편집에서 실제 브라우저 렌더링을 재실행했다는 기록과 구별한다. 매 실험은 원래 예제로 돌아가 한 조건만 바꾼다.

| 한 가지 변경 | 예상 | 조건 |
| --- | --- | --- |
| direction만 column | 주축이 세로로 변경 | 정렬 축도 바뀜 |
| 원래 justify만 space-between | 양 끝이 붙고 사이 75px씩 | 세 항목 합 150·부모 300px |
| 원래 3번 order만 0 | 시각 순서 1·3·2 | 0끼리는 원본 순서 |
| 원래 align-items만 flex-start | 위쪽에 정렬 | 가로 주축 유지 |

가로 중앙이 안 맞으면 direction과 justify부터 본다. grow:0 항목이 남은 공간에서 늘어나지 않는 것은 정상일 수 있다. shrink 3:2를 결과 너비 3:2로 읽지 않는다. 기준 크기·부족량·최소 폭이 관여한다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** flex-basis 명시 설정·flex 축약 상세 계산·gap·align-self·Grid·Container Query는 원본 밖 상세 학습이다. 기본 order·축·grow/shrink 관찰을 먼저 설명한다.

이하의 내용은 **수업 원본에서 확인된 필수 진도가 아닌 추가 학습**이다. 위의 기본 설명을 이해한 뒤 필요할 때 읽는다.

<a id="extra-01-1"></a>

### 1. Grid: 행과 열을 함께 맞추기

Flexbox는 주축을 중심으로 항목의 공간을 나누고, Grid는 행·열의 격자를 정의하여 배치한다. 여러 줄 Flex를 썼다고 서로 다른 줄의 열 경계까지 자동으로 맞는 것은 아니다.

```html
<!-- 추가 예제: 본문 조각 -->
<div class="cards">
    <div>HTML</div><div>CSS</div><div>JavaScript</div>
</div>
```

```css
/* 위 HTML에 연결할 추가 CSS */
.cards {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 16px;
}
.cards > div { border: 1px solid gray; padding: 16px; }
```

두 열을 만들고 세 번째 항목은 다음 행으로 간다. `fr`는 격자에서 남은 공간을 나누는 비율, gap은 칸 사이 간격이다. `minmax(0,1fr)`는 열의 최소 크기를 0으로 허용하여 긴 내용의 최소 크기가 열을 밀어내는 상황을 다루는 선택이다. 긴 글자 자체의 줄바꿈까지 대신 해결하지는 않는다. [Grid 표준](https://www.w3.org/TR/css-grid-1/)

| BACKUP의 확장 주제 | 다음에 확인할 질문 |
| --- | --- |
| grid-template-rows·columns | 몇 개의 행·열을 어떤 크기로 만드는가 |
| grid-row·column·area | 어느 격자선 사이를 차지하는가 |
| auto-fit·auto-fill | 남은 공간과 빈 트랙을 어떻게 처리하는가 |
| auto-rows·auto-flow | 명시하지 않은 항목의 행과 배치 순서는 무엇인가 |
| minmax·fr | 최소 크기와 남은 공간을 어떻게 나누는가 |

여기서는 전체 Grid 알고리즘을 배웠다고 간주하지 않는다. 기본 display 실습을 Grid 정답으로 교체하지 않는다.

<a id="extra-01-2"></a>

### 2. flex-basis와 축약 flex

수업에서는 grow·shrink가 쓰였지만 basis를 명시한 실험은 확인되지 않았다. basis는 여유·부족 공간을 나누기 전 주축 크기의 기준을 정하는 데 관여한다.

```css
/* 추가 예제: flex 컨테이너의 직접 자식에 적용 */
.item {
    flex: 1 1 200px;
}
```

이 세 값은 grow 1, shrink 1, basis 200px다. **최종 너비가 항상 200px라는 뜻은 아니다.** 부모의 크기, 다른 항목, min/max 제한, 콘텐츠가 결과에 영향을 준다. `flex:1` 같은 생략형을 정확한 세 값으로 읽는 연습은 이 다음 단계다. [Flexbox 표준](https://www.w3.org/TR/css-flexbox-1/#flex-property)

gap·align-self·flex-flow·Flex 안의 auto margin·최소 크기 조절도 원본 밖 상세 설계로 분리한다. 기본편의 원본 order·축·주석 실험을 먼저 설명할 수 있어야 한다.

<a id="extra-01-5"></a>

### 선택 복습

Grid로 바꾼 뒤 두 열이 보이면 수업의 inline-block 계산을 이해한 것일까?

<details>
<summary>해설</summary>

별개다. 기본 실습은 width·border-box·margin·공백·줄바꿈을 설명하는 연습이고, Grid는 새 배치 규칙을 학습하는 연습이다.

</details>

이 절의 확장은 기본 문제의 필수 조건이 아니다. 2절의 📚 출처는 배운 기능의 설명을 확인하는 근거이며, 출처가 있다는 이유로 모두 수업 밖 내용인 것은 아니다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. row에서 가로 정렬은 어느 속성인가?
2. order는 HTML 순서를 바꾸는가?
3. 부족 공간이 없어도 shrink 차이가 반드시 보이는가?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

justify-content다. order는 시각 배치 순서이며 HTML 순서를 바꾸지 않는다. 축소가 필요 없는 조건에서는 shrink 차이가 나타나지 않을 수 있다.

</details>

| 대상 | 속성 |
| --- | --- |
| 부모 축 | direction |
| 부모 정렬 | justify·align |
| 자식 순서 | order |
| 자식 공간 분배 | grow·shrink |

[장별 연습문제](실습/연습문제/15_CSS_Flexbox와_유연한_레이아웃_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [작성 스타일](16_CSS_실무_코딩스타일.md)과 [종합실습](17_CSS_종합실습.md)이다.

<!-- 이전 색인 이동 주소 보존 -->
<a id="css-12"></a>
<a id="css-15"></a>
<a id="css-16"></a>
<a id="css-27"></a>
<a id="css-4"></a>
<a id="css-41"></a>
<a id="css-47"></a>
<a id="css-52"></a>
<a id="css-60"></a>
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>

이전 절 주소로 왔다면 [이 장의 목차](#chapter-toc)에서 현재 설명을 찾는다.
